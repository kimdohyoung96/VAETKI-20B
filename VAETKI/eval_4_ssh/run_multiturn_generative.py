"""Run generative multi-turn dialog.

Reads conversation_json, extracts user turns only, and generates assistant
replies iteratively — each subsequent turn sees the model's own prior replies
as history. This truly tests multi-turn dialogue ability.

Current mode: --only-a (model A / 20B only). Model B columns are left blank.
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


def strip_think_for_history(text: str) -> str:
    """Remove <think>...</think> blocks before re-feeding the assistant turn
    into history. The original output (with think) is still saved separately
    for inspection — only the next-turn context sees the cleaned version.
    """
    if not text:
        return text
    cleaned = THINK_PAIR_RE.sub("", text)
    if "</think>" in cleaned:
        return cleaned.split("</think>", 1)[1].strip()
    # No closing </think>: either a short non-reasoning answer (keep) or a
    # reasoning runaway that never closed (drop to keep history clean).
    cleaned = cleaned.strip()
    if len(cleaned) > 800:
        return ""
    return cleaned


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generative multi-turn runner")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--base-url-a", required=True)
    parser.add_argument("--model-a", required=True)
    parser.add_argument("--api-key-a", default=os.getenv("API_KEY_A", "EMPTY"))
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument("--max-tokens", type=int, default=4096)
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


def system_prompt_for_track(track: str, no_think: bool = False) -> str:
    prompts = {
        "naturalness": (
            "너는 한국어 대화 에이전트다. 최종 답변만 간결하게 출력해라. "
            "맥락 일관성과 자연스러운 표현을 유지하고, 불필요한 반복을 피하며 "
            "사용자 의도를 정확히 반영해라."
        ),
        "instruction": "너는 제약 조건을 엄격히 준수하는 도우미다. 최종 출력만 제공하고 형식과 조건을 우선으로 지켜라.",
        "long_context": "너는 문서 근거 기반 답변 도우미다. 최종 답변만 간결히 제시하고 문서에 없는 내용은 단정하지 말며 근거를 명시해라.",
        "reasoning": "너는 추론 도우미다. 내부 사고과정은 노출하지 말고, 최종 답과 핵심 근거만 간결하게 제시해라.",
        "persona": (
            "너는 외국인 사용자를 돕는 한국 지역문화·관광 안내 에이전트다. "
            "사용자가 이전 turn들에서 드러낸 정보(국적, 체류기간, 관심사, 제약, 동행 등)를 "
            "누적해 일관된 페르소나로 통합하고, 사용자가 정보를 정정하면 정정 후 정보로 갱신해라. "
            "최종 답변만 간결하게 출력해라."
        ),
        "multiturn": (
            "너는 한국어 대화 에이전트다. 이전 turn의 맥락·지시·제약·톤·지시어를 "
            "모두 기억하고 일관되게 반영해라. 사용자가 의도를 수정하면 새 의도를 우선하고, "
            "회상 요청이 오면 정확히 인용해라. 최종 답변만 간결하게 출력해라."
        ),
        "foreigner_lang": (
            "너는 한국어를 배우는 외국인을 돕는 안내 에이전트다. "
            "사용자의 한국어 수준에 맞춰 어휘 난이도, 문장 길이, 격식체/평어, 한자어 사용을 조정해라. "
            "사용자가 영어를 섞어 쓰면 영어 보조 어휘 사용을 허용하고, "
            "발음 표기(로마자) 요청이 오면 한글·로마자·의미를 함께 제시해라. "
            "최종 답변만 간결하게 출력해라."
        ),
        "recommendation": (
            "너는 외국인을 위한 한국 여행·문화 추천 도우미다. "
            "사용자가 turn들에 걸쳐 제공한 조건(국적, 체류기간, 예산, 동행, 제약, 선호)을 "
            "모두 반영한 구체적이고 개인화된 추천을 제공해라. "
            "정보가 부족하면 일반적 답변을 내지 말고 먼저 짧게 질문해라. "
            "최종 답변만 간결하게 출력해라."
        ),
    }
    base = prompts.get(track, "너는 정확하고 간결한 한국어 도우미다.")
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
        history: List[Dict[str, str]] = [system_msg]
        generated_turns: List[Dict[str, str]] = []
        turn_latencies: List[int] = []
        turn_errors: List[str] = []
        any_error = False

        for turn_i, user_msg in enumerate(user_turns, start=1):
            history.append({"role": "user", "content": user_msg})
            generated_turns.append({"role": "user", "content": user_msg})

            reply, latency, err = call_model(
                client=client,
                model=args.model_a,
                messages=history,
                temperature=args.temperature,
                top_p=args.top_p,
                max_tokens=args.max_tokens,
                timeout=args.timeout,
            )
            turn_latencies.append(latency)

            if err:
                any_error = True
                turn_errors.append(f"turn{turn_i}:{err[:120]}")
                history.append({"role": "assistant", "content": ""})
                generated_turns.append({"role": "assistant", "content": ""})
                print(f"[{idx}/{total}] {sid} turn{turn_i} ERROR ({latency}ms): {err[:80]}", flush=True)
                break

            cleaned_reply = strip_think_for_history(reply)
            # Skip empty assistant turns from history to prevent failure cascading.
            # The user turn we just appended stays — preserving user intent —
            # so the next turn sees consecutive user messages, which models
            # handle as the user adding more context.
            if cleaned_reply:
                history.append({"role": "assistant", "content": cleaned_reply})
            generated_turns.append({"role": "assistant", "content": reply})
            empty_marker = " [EMPTY-skipped from history]" if not cleaned_reply else ""
            print(
                f"[{idx}/{total}] {sid} turn{turn_i}/{len(user_turns)} ok "
                f"({latency}ms, raw {len(reply)} chars / clean {len(cleaned_reply)} chars)"
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
        if turn_errors:
            row["notes"] = (row.get("notes") or "") + " | A_ERR: " + " ; ".join(turn_errors)

        # Incremental save after every row
        with open(args.output, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)

    print(f"Saved: {args.output}", flush=True)


if __name__ == "__main__":
    main()
