"""Run generative multi-turn dialog with summary memory + recent 2 turns.

This runner is designed for VAETKI-20B-A2B long multi-turn experiments.
It replaces full-history accumulation with:
  1) track system prompt
  2) compact summary memory
  3) recent N user-assistant turns only (default: 2)
  4) current user message

It keeps the same 4-axis CSV style while adding diagnostics:
  - prompt/history token estimates per turn
  - summary-memory size per turn
  - raw/clean reply token+char lengths
  - collapse status: NORMAL / EMPTY / RUNAWAY / REPETITION_LOOP
  - clean source: visible / think_fallback / raw_short_fallback / empty
  - raw conversation JSON and cleaned conversation JSON separately

Important design:
  - generated_conversation_json stores CLEANED assistant replies for evaluator stability.
  - model_a_raw_conversation_json stores RAW assistant replies for debugging <think>, repetition, etc.
  - next-turn prompt uses only CLEANED recent turns + compact summary memory.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import time
from typing import Dict, List, Tuple

from openai import OpenAI

try:
    import tiktoken  # type: ignore
except Exception:
    tiktoken = None


THINK_PAIR_RE = re.compile(r"<think>.*?</think>\s*", re.DOTALL)
THINK_INNER_RE = re.compile(r"<think>(.*?)</think>", re.DOTALL)
BAD_SYMBOL_RE = re.compile(r"[{}\[\]<>~=\\|]{3,}")
SPACE_RE = re.compile(r"\s+")

if tiktoken is not None:
    _ENC = tiktoken.get_encoding("cl100k_base")
else:
    _ENC = None


def compact_text(text: str, max_chars: int) -> str:
    if not text:
        return ""
    text = SPACE_RE.sub(" ", text).strip()
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "…"


def count_text_tokens(text: str) -> int:
    if not text:
        return 0
    if _ENC is not None:
        return len(_ENC.encode(text))
    return max(1, len(text) // 2)


def count_tokens(messages: List[Dict[str, str]]) -> int:
    text = ""
    for m in messages:
        text += f"{m.get('role', '')}: {m.get('content', '')}\n"
    return count_text_tokens(text)


def detect_collapse(reply: str) -> str:
    """Heuristic status of raw model output."""
    if not reply or len(reply.strip()) == 0:
        return "EMPTY"
    if len(reply) > 7000:
        return "RUNAWAY"

    bad_patterns = [
        ">>>>", "<<<<", "{{{{", "}}}}", "[[[[", "]]}}", "]]", "||||",
        "해야겠", "구성 예정", "전략", "알고리즘", "시나리오", "메타",
        "음...", "음..", "음,,", "음냐", "음흠", "고고", "ㅋㅋㅋ",
    ]
    pattern_hits = sum(1 for p in bad_patterns if p in reply)
    symbol_hits = len(BAD_SYMBOL_RE.findall(reply))
    if pattern_hits >= 2 or symbol_hits >= 2:
        return "REPETITION_LOOP"
    return "NORMAL"


def strip_think_visible_answer(text: str) -> str:
    """Remove normal paired think blocks and keep visible answer."""
    if not text:
        return ""
    cleaned = THINK_PAIR_RE.sub("", text).strip()
    if "</think>" in cleaned:
        cleaned = cleaned.split("</think>")[-1].strip()
    cleaned = re.sub(r"</?think>", "", cleaned).strip()
    return cleaned


def extract_think_inner_fallback(text: str) -> str:
    """Return inner text of the last complete <think>...</think> block.

    This is used only when the model puts all useful content inside think and
    visible answer becomes empty. It prevents excessive EMPTY results while
    still removing the literal tags from history/CSV.
    """
    if not text:
        return ""
    matches = THINK_INNER_RE.findall(text)
    if not matches:
        return ""
    inner = matches[-1].strip()
    inner = re.sub(r"</?think>", "", inner).strip()
    return inner


def dedupe_repeated_answer(text: str) -> str:
    """Remove repeated paragraphs/list blocks/sentences from a cleaned answer."""
    if not text:
        return ""
    text = text.strip()
    if len(text) < 250:
        return text

    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    deduped_paragraphs: List[str] = []
    seen_keys = set()
    for p in paragraphs:
        key = re.sub(r"\s+", " ", p).strip()[:240]
        if key in seen_keys:
            continue
        seen_keys.add(key)
        deduped_paragraphs.append(p)
    text = "\n\n".join(deduped_paragraphs).strip()

    n = len(text)
    if n >= 500:
        mid = n // 2
        first = text[:mid].strip()
        second = text[mid:].strip()
        first_key = re.sub(r"\s+", " ", first[:280]).strip()
        second_norm = re.sub(r"\s+", " ", second).strip()
        if len(first_key) >= 120 and first_key in second_norm:
            return second.strip()

    markers = ["### ", "## ", "다음은", "추천해 드리겠습니다", "추천드립니다", "정리하면", "요약하면", "1. ", "**1.", "- **"]
    for marker in markers:
        first_pos = text.find(marker)
        if first_pos == -1:
            continue
        second_pos = text.find(marker, first_pos + len(marker))
        if second_pos == -1:
            continue
        before = text[:second_pos].strip()
        after = text[second_pos:].strip()
        if len(before) >= 250 and len(after) >= 250:
            return before

    sentences = re.split(r"(?<=[.!?。！？요다])\s+", text)
    cleaned_sentences: List[str] = []
    seen_sentence_keys = set()
    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue
        key = re.sub(r"\s+", " ", sent)[:180]
        if len(key) >= 40 and key in seen_sentence_keys:
            continue
        seen_sentence_keys.add(key)
        cleaned_sentences.append(sent)
    if cleaned_sentences:
        text = " ".join(cleaned_sentences).strip()
    return text


def clean_reply_for_storage(reply: str, fallback_long_think: bool = True) -> Tuple[str, str]:
    """Return cleaned assistant reply and source label.

    source labels:
      - visible: normal answer outside <think> was used
      - think_fallback: no visible answer, so inner think text was used
      - raw_short_fallback: no tags, short raw text was used
      - empty: no usable text
    """
    if not reply or not reply.strip():
        return "", "empty"

    visible = strip_think_visible_answer(reply)
    if visible:
        visible = dedupe_repeated_answer(visible)
        visible = re.sub(r"</?think>", "", visible).strip()
        if visible:
            return visible, "visible"

    think_inner = extract_think_inner_fallback(reply)
    if think_inner and fallback_long_think:
        think_inner = dedupe_repeated_answer(think_inner)
        think_inner = re.sub(r"</?think>", "", think_inner).strip()
        if think_inner:
            return think_inner, "think_fallback"

    raw = re.sub(r"</?think>", "", reply).strip()
    if raw and len(raw) <= 1200:
        raw = dedupe_repeated_answer(raw)
        return raw, "raw_short_fallback"

    return "", "empty"


def build_memory_message(memory: str, track: str) -> Dict[str, str]:
    if not memory.strip():
        memory = "아직 누적된 대화 요약이 없습니다."
    content = (
        "[대화 요약 메모리]\n"
        f"트랙: {track or 'unknown'}\n"
        f"{memory.strip()}\n\n"
        "[응답 규칙]\n"
        "- 위 메모리와 최근 대화만 근거로 현재 사용자 요청에 답하라.\n"
        "- 최종 답변만 출력하라. 내부 추론, 계획, <think> 블록은 출력하지 마라.\n"
        "- 같은 문장을 반복하지 마라.\n"
        "- 정보 제공/조건 누적 turn에서는 길게 추천하지 말고 짧게 확인하라.\n"
        "- 최종 정리/추천 요청일 때만 조건을 종합해 답하라.\n"
        "- 가능하면 5문장 또는 5개 bullet 이내로 답하라."
    )
    return {"role": "system", "content": content}


def recent_history_for_prompt(clean_turns: List[Dict[str, str]], recent_turns: int) -> List[Dict[str, str]]:
    if not clean_turns:
        return []
    # Recent N user-assistant turns ~= last 2N messages. If an assistant was
    # skipped, this still keeps the latest compact context.
    recent = clean_turns[-recent_turns * 2 :]
    clipped: List[Dict[str, str]] = []
    for m in recent:
        role = m.get("role", "")
        content = m.get("content", "")
        if role == "assistant":
            content = compact_text(content, 500)
        elif role == "user":
            content = compact_text(content, 300)
        clipped.append({"role": role, "content": content})
    return clipped


def update_summary_memory(
    memory: str,
    user_msg: str,
    cleaned_reply: str,
    max_lines: int,
    max_chars: int,
) -> str:
    """Deterministic memory update without extra model calls."""
    user_part = compact_text(user_msg, 120)
    assistant_part = compact_text(cleaned_reply, 160)
    if assistant_part:
        new_line = f"- 사용자 정보/요청: {user_part} / 응답 요지: {assistant_part}"
    else:
        new_line = f"- 사용자 정보/요청: {user_part} / 응답 없음 또는 제거됨"

    lines = [line for line in memory.splitlines() if line.strip()]
    lines.append(new_line)
    lines = lines[-max_lines:]
    updated = "\n".join(lines)
    if len(updated) > max_chars:
        updated = updated[-max_chars:]
        if "\n" in updated:
            updated = updated.split("\n", 1)[1]
    return updated.strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generative multi-turn runner: summary memory + recent turns")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--base-url-a", required=True)
    parser.add_argument("--model-a", required=True)
    parser.add_argument("--api-key-a", default=os.getenv("API_KEY_A", "EMPTY"))
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument("--repetition-penalty", type=float, default=1.0)
    parser.add_argument("--max-tokens", type=int, default=1024)
    parser.add_argument("--timeout", type=float, default=600.0)
    parser.add_argument("--only-a", action="store_true", default=True)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--no-think", action="store_true", help="Forbid <think> via system prompt.")
    parser.add_argument("--drop-collapsed-from-history", action="store_true", help="Do not reuse RUNAWAY/REPETITION_LOOP/EMPTY replies in recent history or memory.")
    parser.add_argument("--recent-turns", type=int, default=2, help="Number of recent user-assistant turns to keep in prompt.")
    parser.add_argument("--max-memory-lines", type=int, default=12)
    parser.add_argument("--max-memory-chars", type=int, default=1600)
    parser.add_argument("--seed", type=int, default=None, help="Optional vLLM sampling seed via extra_body.")
    parser.add_argument("--disable-think-fallback", action="store_true", help="If set, do not use think inner text as fallback when visible answer is empty.")
    return parser.parse_args()


NO_THINK_PREFIX = (
    "[엄수 지시]\n"
    "<think> 태그나 어떤 형태의 내부 사고 과정도 출력하지 마라. "
    "추론·계획·자문·메타 코멘트 일체 금지. "
    "사용자에게 보여줄 최종 답변만 즉시 출력해라.\n\n"
)

COMMON_SHORT_OUTPUT_RULES = (
    " 최종 답변만 출력해라. 내부 사고과정과 <think> 블록을 출력하지 마라. "
    "반복하지 말고, 가능하면 5문장 또는 5개 bullet 이내로 답해라. "
    "사용자가 정보를 추가하는 중이면 길게 추천하지 말고 짧게 확인해라."
)


def system_prompt_for_track(track: str, no_think: bool = False) -> str:
    prompts = {
        "naturalness": "너는 한국어 대화 에이전트다. 맥락 일관성과 자연스러운 표현을 유지하고 사용자 의도를 정확히 반영해라.",
        "instruction": "너는 제약 조건을 엄격히 준수하는 도우미다. 형식과 조건을 우선으로 지켜라.",
        "long_context": "너는 문서 근거 기반 답변 도우미다. 문서에 없는 내용은 단정하지 말고 근거를 명시해라.",
        "reasoning": "너는 추론 도우미다. 최종 답과 핵심 근거만 간결하게 제시해라.",
        "persona": (
            "너는 외국인 사용자를 돕는 한국 지역문화·관광 안내 에이전트다. "
            "사용자가 이전 turn들에서 드러낸 정보(국적, 체류기간, 관심사, 제약, 동행 등)를 "
            "요약 메모리로 누적해 일관된 페르소나로 통합하고, 정정 정보가 있으면 최신 정보를 우선해라."
        ),
        "multiturn": (
            "너는 한국어 대화 에이전트다. 이전 맥락·지시·제약·톤·지시어를 기억하고 일관되게 반영해라. "
            "사용자가 의도를 수정하면 새 의도를 우선하고, 회상 요청이 오면 정확히 인용해라."
        ),
        "foreigner_lang": (
            "너는 한국어를 배우는 외국인을 돕는 안내 에이전트다. "
            "사용자의 한국어 수준에 맞춰 어휘 난이도, 문장 길이, 격식체/평어, 한자어 사용을 조정해라. "
            "로마자 표기나 영어 보조 요청이 있으면 반드시 반영해라."
        ),
        "recommendation": (
            "너는 외국인을 위한 한국 여행·문화 추천 도우미다. "
            "사용자가 turn들에 걸쳐 제공한 조건(국적, 체류기간, 예산, 동행, 제약, 선호)을 모두 반영해라. "
            "정보가 부족하면 일반적 추천을 쏟아내지 말고 먼저 짧게 질문해라."
        ),
    }
    base = prompts.get(track, "너는 정확하고 간결한 한국어 도우미다.") + COMMON_SHORT_OUTPUT_RULES
    return (NO_THINK_PREFIX + base) if no_think else base


def extract_user_turns(conversation_json: str) -> List[str]:
    try:
        conv = json.loads(conversation_json or "[]")
    except Exception:
        return []
    return [
        m["content"]
        for m in conv
        if isinstance(m, dict) and m.get("role") == "user" and isinstance(m.get("content"), str)
    ]


def call_model(
    client: OpenAI,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    top_p: float,
    repetition_penalty: float,
    max_tokens: int,
    timeout: float,
    seed: int | None,
) -> Tuple[str, int, str]:
    start = time.perf_counter()
    try:
        kwargs = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": max_tokens,
            "timeout": timeout,
        }
        extra_body = {}
        if repetition_penalty and repetition_penalty != 1.0:
            extra_body["repetition_penalty"] = repetition_penalty
        if seed is not None:
            extra_body["seed"] = seed
        if extra_body:
            kwargs["extra_body"] = extra_body

        resp = client.chat.completions.create(**kwargs)
        latency_ms = int((time.perf_counter() - start) * 1000)
        text = resp.choices[0].message.content if resp.choices else ""
        return text or "", latency_ms, ""
    except Exception as exc:
        latency_ms = int((time.perf_counter() - start) * 1000)
        return "", latency_ms, str(exc)


def render_conversation(turns: List[Dict[str, str]]) -> str:
    lines = []
    for m in turns:
        role = m.get("role", "")
        content = m.get("content", "")
        if role == "user":
            lines.append(f"[user] {content}")
        elif role == "assistant":
            lines.append(f"[assistant] {content}")
    return "\n".join(lines)


def ensure_columns(rows: List[Dict[str, str]], fieldnames: List[str]) -> None:
    required = [
        "model_a_output", "model_b_output", "model_a_raw_output", "latency_ms_a", "latency_ms_b",
        "error_flag_a", "error_flag_b", "model_a_name_hidden", "model_b_name_hidden", "p95_group_tag",
        "generated_conversation_json", "model_a_raw_conversation_json", "turn_latencies_ms_a", "num_turns_a",
        "turn_prompt_tokens_a", "turn_prompt_chars_a", "turn_memory_tokens_a", "turn_memory_chars_a",
        "turn_reply_tokens_a", "turn_reply_chars_a", "turn_clean_tokens_a", "turn_clean_chars_a",
        "turn_status_a", "turn_clean_source_a", "first_collapse_turn_a", "first_collapse_type_a",
        "max_prompt_tokens_a", "summary_memory_a", "history_strategy_a",
    ]
    for name in required:
        if name not in fieldnames:
            fieldnames.append(name)
    for row in rows:
        for name in required:
            row.setdefault(name, "")


def main() -> None:
    args = parse_args()

    with open(args.input, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    ensure_columns(rows, fieldnames)

    client = OpenAI(base_url=args.base_url_a, api_key=args.api_key_a)
    total = len(rows)

    for idx, row in enumerate(rows, start=1):
        sid = row.get("session_id", f"row-{idx}")
        if args.resume and row.get("model_a_output"):
            print(f"[{idx}/{total}] {sid} skipped (resume)", flush=True)
            continue

        user_turns = extract_user_turns(row.get("conversation_json", ""))
        if not user_turns:
            print(f"[{idx}/{total}] {sid} skipped (no user turns)", flush=True)
            row["error_flag_a"] = "1"
            row["notes"] = (row.get("notes") or "") + " | NO_USER_TURNS"
            continue

        track = (row.get("task_track") or "").strip()
        system_msg = {"role": "system", "content": system_prompt_for_track(track, no_think=args.no_think)}

        raw_turns: List[Dict[str, str]] = []
        clean_turns: List[Dict[str, str]] = []
        summary_memory = ""

        turn_latencies: List[int] = []
        turn_prompt_tokens: List[int] = []
        turn_prompt_chars: List[int] = []
        turn_memory_tokens: List[int] = []
        turn_memory_chars: List[int] = []
        turn_reply_tokens: List[int] = []
        turn_reply_chars: List[int] = []
        turn_clean_tokens: List[int] = []
        turn_clean_chars: List[int] = []
        turn_statuses: List[str] = []
        turn_clean_sources: List[str] = []
        turn_errors: List[str] = []
        any_error = False
        first_collapse_turn = ""
        first_collapse_type = ""

        for turn_i, user_msg in enumerate(user_turns, start=1):
            prompt_messages: List[Dict[str, str]] = [system_msg, build_memory_message(summary_memory, track)]
            prompt_messages.extend(recent_history_for_prompt(clean_turns, args.recent_turns))
            prompt_messages.append({"role": "user", "content": user_msg})

            prompt_tokens = count_tokens(prompt_messages)
            prompt_chars = sum(len(m.get("content", "")) for m in prompt_messages)
            memory_tokens = count_text_tokens(summary_memory)
            memory_chars = len(summary_memory)

            raw_turns.append({"role": "user", "content": user_msg})
            clean_turns.append({"role": "user", "content": user_msg})

            reply, latency, err = call_model(
                client=client,
                model=args.model_a,
                messages=prompt_messages,
                temperature=args.temperature,
                top_p=args.top_p,
                repetition_penalty=args.repetition_penalty,
                max_tokens=args.max_tokens,
                timeout=args.timeout,
                seed=args.seed,
            )
            turn_latencies.append(latency)

            if err:
                any_error = True
                turn_errors.append(f"turn{turn_i}:{err[:120]}")
                raw_turns.append({"role": "assistant", "content": ""})
                clean_turns.append({"role": "assistant", "content": ""})
                turn_prompt_tokens.append(prompt_tokens)
                turn_prompt_chars.append(prompt_chars)
                turn_memory_tokens.append(memory_tokens)
                turn_memory_chars.append(memory_chars)
                turn_reply_tokens.append(0)
                turn_reply_chars.append(0)
                turn_clean_tokens.append(0)
                turn_clean_chars.append(0)
                turn_statuses.append("ERROR")
                turn_clean_sources.append("error")
                if not first_collapse_turn:
                    first_collapse_turn = str(turn_i)
                    first_collapse_type = "ERROR"
                print(f"[{idx}/{total}] {sid} turn{turn_i} ERROR prompt_tokens={prompt_tokens} ({latency}ms): {err[:100]}", flush=True)
                break

            status = detect_collapse(reply)
            cleaned_reply, clean_source = clean_reply_for_storage(reply, fallback_long_think=not args.disable_think_fallback)

            if status != "NORMAL" and not first_collapse_turn:
                first_collapse_turn = str(turn_i)
                first_collapse_type = status

            # If requested, prevent bad raw generations from contaminating future prompts.
            if args.drop_collapsed_from_history and status in {"RUNAWAY", "REPETITION_LOOP", "EMPTY"}:
                cleaned_for_history = ""
            else:
                cleaned_for_history = cleaned_reply

            raw_turns.append({"role": "assistant", "content": reply})
            # Cleaned conversation is used by analyzer/human review and future context.
            clean_turns.append({"role": "assistant", "content": cleaned_for_history})

            summary_memory = update_summary_memory(
                summary_memory,
                user_msg,
                cleaned_for_history,
                max_lines=args.max_memory_lines,
                max_chars=args.max_memory_chars,
            )

            turn_prompt_tokens.append(prompt_tokens)
            turn_prompt_chars.append(prompt_chars)
            turn_memory_tokens.append(memory_tokens)
            turn_memory_chars.append(memory_chars)
            turn_reply_tokens.append(count_text_tokens(reply))
            turn_reply_chars.append(len(reply))
            turn_clean_tokens.append(count_text_tokens(cleaned_reply))
            turn_clean_chars.append(len(cleaned_reply))
            turn_statuses.append(status)
            turn_clean_sources.append(clean_source)

            empty_marker = " [EMPTY/reply not reused]" if not cleaned_for_history else ""
            print(
                f"[{idx}/{total}] {sid} turn{turn_i}/{len(user_turns)} "
                f"status={status} source={clean_source} "
                f"prompt_tokens={prompt_tokens} memory_tokens={memory_tokens} "
                f"reply_tokens={turn_reply_tokens[-1]} "
                f"({latency}ms, raw {len(reply)} chars / clean {len(cleaned_reply)} chars)"
                f"{empty_marker}",
                flush=True,
            )

        row["model_a_name_hidden"] = "A"
        row["model_b_name_hidden"] = "B"
        row["model_a_output"] = render_conversation(clean_turns)
        row["model_a_raw_output"] = render_conversation(raw_turns)
        row["latency_ms_a"] = str(sum(turn_latencies))
        row["turn_latencies_ms_a"] = json.dumps(turn_latencies)
        row["num_turns_a"] = str(sum(1 for m in clean_turns if m["role"] == "assistant"))
        row["generated_conversation_json"] = json.dumps(clean_turns, ensure_ascii=False)
        row["model_a_raw_conversation_json"] = json.dumps(raw_turns, ensure_ascii=False)
        row["error_flag_a"] = "1" if any_error else "0"
        row["p95_group_tag"] = track or "multiturn"
        row["turn_prompt_tokens_a"] = json.dumps(turn_prompt_tokens)
        row["turn_prompt_chars_a"] = json.dumps(turn_prompt_chars)
        row["turn_memory_tokens_a"] = json.dumps(turn_memory_tokens)
        row["turn_memory_chars_a"] = json.dumps(turn_memory_chars)
        row["turn_reply_tokens_a"] = json.dumps(turn_reply_tokens)
        row["turn_reply_chars_a"] = json.dumps(turn_reply_chars)
        row["turn_clean_tokens_a"] = json.dumps(turn_clean_tokens)
        row["turn_clean_chars_a"] = json.dumps(turn_clean_chars)
        row["turn_status_a"] = json.dumps(turn_statuses, ensure_ascii=False)
        row["turn_clean_source_a"] = json.dumps(turn_clean_sources, ensure_ascii=False)
        row["first_collapse_turn_a"] = first_collapse_turn
        row["first_collapse_type_a"] = first_collapse_type
        row["max_prompt_tokens_a"] = str(max(turn_prompt_tokens) if turn_prompt_tokens else 0)
        row["summary_memory_a"] = summary_memory
        row["history_strategy_a"] = f"summary_memory_plus_recent_{args.recent_turns}_turns"

        if turn_errors:
            row["notes"] = (row.get("notes") or "") + " | A_ERR: " + " ; ".join(turn_errors)

        with open(args.output, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)

    print(f"Saved: {args.output}", flush=True)


if __name__ == "__main__":
    main()
