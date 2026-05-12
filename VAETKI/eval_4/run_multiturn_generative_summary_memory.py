"""Run generative multi-turn dialog with summary memory.

Reads conversation_json, extracts user turns only, and generates assistant
replies iteratively. To reduce context accumulation / reasoning runaway,
each request is built from:
  1) track system prompt
  2) compact summary memory
  3) recent 2 turns only
  4) current user message

The full raw generated conversation is still saved for later analysis.
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


THINK_PAIR_RE = re.compile(r"<think>.*?</think>\s*", re.DOTALL)
SPACE_RE = re.compile(r"\s+")

# History control: keep only recent 2 user-assistant turns in the prompt.
RECENT_USER_ASSISTANT_TURNS = 2
# Summary memory control: keep compact text to avoid context explosion.
MAX_MEMORY_LINES = 10
MAX_MEMORY_CHARS = 1200
MAX_USER_SNIPPET_CHARS = 90
MAX_ASSISTANT_SNIPPET_CHARS = 140


def compact_text(text: str, max_chars: int) -> str:
    """Normalize whitespace and clip text for memory/recent history."""
    if not text:
        return ""
    text = SPACE_RE.sub(" ", text).strip()
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "…"


def strip_think_for_history(text: str) -> str:
    """Remove <think>...</think> blocks before re-feeding assistant output.

    The original output is still saved separately for inspection. Only the next
    request context sees this cleaned text. VAETKI sometimes emits reasoning
    without an opening <think> but with a closing </think>, so we also split on
    the first closing tag.
    """
    if not text:
        return text

    cleaned = THINK_PAIR_RE.sub("", text)

    # Some outputs look like: "reasoning... </think> final answer".
    if "</think>" in cleaned:
        cleaned = cleaned.split("</think>", 1)[1]

    cleaned = cleaned.strip()

    # If no closing tag exists and the output is very long, it is likely a
    # reasoning runaway. Drop it from history to prevent cascading failure.
    if "</think>" not in text and len(cleaned) > 800:
        return ""

    return cleaned


def build_memory_message(memory: str, track: str) -> Dict[str, str]:
    """Create a compact summary-memory system message."""
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
        "- 답변은 가능하면 5문장 또는 5개 bullet 이내로 제한하라."
    )
    return {"role": "system", "content": content}


def recent_history_for_prompt(clean_turns: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Return recent 2 user-assistant turns for the next prompt.

    clean_turns stores only cleaned assistant answers. Raw outputs are stored in
    generated_turns for analysis and are not reused as model input.
    """
    if not clean_turns:
        return []

    # recent 2 user-assistant turns = last 4 messages.
    recent = clean_turns[-RECENT_USER_ASSISTANT_TURNS * 2 :]
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


def update_summary_memory(memory: str, user_msg: str, cleaned_reply: str) -> str:
    """Update compact memory without calling another LLM.

    This intentionally uses deterministic clipping instead of summarization by
    the target model, so evaluation cost and failure modes do not increase.
    """
    user_part = compact_text(user_msg, MAX_USER_SNIPPET_CHARS)
    assistant_part = compact_text(cleaned_reply, MAX_ASSISTANT_SNIPPET_CHARS)

    if assistant_part:
        new_line = f"- 사용자 정보/요청: {user_part} / 응답 요지: {assistant_part}"
    else:
        new_line = f"- 사용자 정보/요청: {user_part} / 응답 없음 또는 reasoning runaway로 history 제외"

    lines = [line for line in memory.splitlines() if line.strip()]
    lines.append(new_line)
    lines = lines[-MAX_MEMORY_LINES:]

    updated = "\n".join(lines)
    if len(updated) > MAX_MEMORY_CHARS:
        updated = updated[-MAX_MEMORY_CHARS:]
        # Avoid starting mid-line when clipping from the left.
        if "\n" in updated:
            updated = updated.split("\n", 1)[1]
    return updated.strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generative multi-turn runner with summary memory")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--base-url-a", required=True)
    parser.add_argument("--model-a", required=True)
    parser.add_argument("--api-key-a", default=os.getenv("API_KEY_A", "EMPTY"))
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument("--max-tokens", type=int, default=768)
    parser.add_argument("--timeout", type=float, default=600.0)
    parser.add_argument("--only-a", action="store_true", default=True)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument(
        "--no-think",
        action="store_true",
        help="Forbid the model from emitting <think> blocks via system prompt.",
    )
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
        "naturalness": (
            "너는 한국어 대화 에이전트다. 맥락 일관성과 자연스러운 표현을 유지하고, "
            "사용자 의도를 정확히 반영해라."
        ),
        "instruction": "너는 제약 조건을 엄격히 준수하는 도우미다. 형식과 조건을 우선으로 지켜라.",
        "long_context": "너는 문서 근거 기반 답변 도우미다. 문서에 없는 내용은 단정하지 말고 근거를 명시해라.",
        "reasoning": "너는 추론 도우미다. 최종 답과 핵심 근거만 간결하게 제시해라.",
        "persona": (
            "너는 외국인 사용자를 돕는 한국 지역문화·관광 안내 에이전트다. "
            "사용자가 이전 turn들에서 드러낸 정보(국적, 체류기간, 관심사, 제약, 동행 등)를 "
            "대화 요약 메모리로 누적해 일관된 페르소나로 통합하고, 정정 정보가 있으면 최신 정보를 우선해라."
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
    max_tokens: int,
    timeout: float,
) -> Tuple[str, int, str]:
    start = time.perf_counter()
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            timeout=timeout,
            ## stop=["<|END|>"],
        )
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
        "model_a_output",
        "model_b_output",
        "latency_ms_a",
        "latency_ms_b",
        "error_flag_a",
        "error_flag_b",
        "model_a_name_hidden",
        "model_b_name_hidden",
        "p95_group_tag",
        "generated_conversation_json",
        "turn_latencies_ms_a",
        "num_turns_a",
        # New diagnostics for summary-memory runner.
        "turn_prompt_chars_a",
        "turn_memory_chars_a",
        "turn_raw_chars_a",
        "turn_clean_chars_a",
        "summary_memory_a",
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

        # generated_turns: full raw conversation for analyzer/report.
        generated_turns: List[Dict[str, str]] = []
        # clean_turns: cleaned recent history only for next model input.
        clean_turns: List[Dict[str, str]] = []
        summary_memory = ""

        turn_latencies: List[int] = []
        turn_prompt_chars: List[int] = []
        turn_memory_chars: List[int] = []
        turn_raw_chars: List[int] = []
        turn_clean_chars: List[int] = []
        turn_errors: List[str] = []
        any_error = False

        for turn_i, user_msg in enumerate(user_turns, start=1):
            # Build model input from summary memory + recent 2 turns + current user.
            prompt_messages: List[Dict[str, str]] = [
                system_msg,
                build_memory_message(summary_memory, track),
            ]
            prompt_messages.extend(recent_history_for_prompt(clean_turns))
            prompt_messages.append({"role": "user", "content": user_msg})

            prompt_chars = sum(len(m.get("content", "")) for m in prompt_messages)
            turn_prompt_chars.append(prompt_chars)
            turn_memory_chars.append(len(summary_memory))

            generated_turns.append({"role": "user", "content": user_msg})
            clean_turns.append({"role": "user", "content": user_msg})

            reply, latency, err = call_model(
                client=client,
                model=args.model_a,
                messages=prompt_messages,
                temperature=args.temperature,
                top_p=args.top_p,
                max_tokens=args.max_tokens,
                timeout=args.timeout,
            )
            turn_latencies.append(latency)
            turn_raw_chars.append(len(reply))

            if err:
                any_error = True
                turn_errors.append(f"turn{turn_i}:{err[:120]}")
                generated_turns.append({"role": "assistant", "content": ""})
                turn_clean_chars.append(0)
                print(f"[{idx}/{total}] {sid} turn{turn_i} ERROR ({latency}ms): {err[:80]}", flush=True)
                break

            cleaned_reply = strip_think_for_history(reply)
            turn_clean_chars.append(len(cleaned_reply))

            # Save raw output for analysis; reuse only cleaned output for future prompt.
            generated_turns.append({"role": "assistant", "content": reply})
            if cleaned_reply:
                clean_turns.append({"role": "assistant", "content": cleaned_reply})
            else:
                # Keep turn alignment in clean history small by not adding empty assistant.
                # The next prompt will still see the user message in recent history and summary.
                pass

            summary_memory = update_summary_memory(summary_memory, user_msg, cleaned_reply)

            empty_marker = " [EMPTY-skipped from recent history]" if not cleaned_reply else ""
            print(
                f"[{idx}/{total}] {sid} turn{turn_i}/{len(user_turns)} ok "
                f"({latency}ms, prompt {prompt_chars} chars, memory {len(summary_memory)} chars, "
                f"raw {len(reply)} chars / clean {len(cleaned_reply)} chars)"
                f"{empty_marker}",
                flush=True,
            )

        row["model_a_name_hidden"] = "A"
        row["model_b_name_hidden"] = "B"
        row["model_a_output"] = render_conversation(generated_turns)
        row["latency_ms_a"] = str(sum(turn_latencies))
        row["turn_latencies_ms_a"] = json.dumps(turn_latencies)
        row["num_turns_a"] = str(sum(1 for m in generated_turns if m["role"] == "assistant"))
        row["generated_conversation_json"] = json.dumps(generated_turns, ensure_ascii=False)
        row["error_flag_a"] = "1" if any_error else "0"
        row["p95_group_tag"] = track or "multiturn"

        # Diagnostics for checking whether summary memory reduced context growth.
        row["turn_prompt_chars_a"] = json.dumps(turn_prompt_chars)
        row["turn_memory_chars_a"] = json.dumps(turn_memory_chars)
        row["turn_raw_chars_a"] = json.dumps(turn_raw_chars)
        row["turn_clean_chars_a"] = json.dumps(turn_clean_chars)
        row["summary_memory_a"] = summary_memory

        if turn_errors:
            row["notes"] = (row.get("notes") or "") + " | A_ERR: " + " ; ".join(turn_errors)

        # Incremental save after every row.
        with open(args.output, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)

    print(f"Saved: {args.output}", flush=True)


if __name__ == "__main__":
    main()
