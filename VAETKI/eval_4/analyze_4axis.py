"""4-axis evaluation analyzer.

Reads a multi-turn run CSV (output of run_multiturn_generative.py) over the
4-axis seed and produces:
  - Per-track success rate
  - Per-axis specialized auto-classification
  - Failure-class distribution
  - Per-session turn-by-turn matrix
  - Markdown report

Specialized classes added on top of the generic ones (EMPTY / THINK_RUNAWAY /
REPETITION_LOOP / EMPTY_AFTER_THINK / PROMPT_IGNORED / SUCCESS):

  Persona track (only on the *final* turn that asks for an integrated persona):
    - PERSONA_RECALL_FAIL  : final answer omits one or more required tokens
                              listed in `gold_answer_or_rule` (must_include=...)
  Multiturn track (only on turns that explicitly ask for recall):
    - CONTEXT_LOSS         : recall turn answer doesn't surface the original
                              referenced entity
  Foreigner_lang track (every turn):
    - VOCAB_MISMATCH       : violates the per-session rule
                              (avoid_hanja=true / vocab_level=beginner / ...)
  Recommendation track (only on the final synthesis turn):
    - RECOMMENDATION_GENERIC : final answer doesn't reference the user-provided
                                constraints (must_include tokens absent)

Generic classes still apply first; specialized class only fires when the generic
class is SUCCESS (i.e., we don't double-flag an EMPTY).
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from statistics import mean, median
from typing import Dict, List, Optional, Tuple


# ---------- Generic classification (mirrors analyze_multiturn_comparison_v2) ----------

def has_close_think(text: str) -> bool:
    return "</think>" in text


def visible_answer(text: str) -> str:
    if "</think>" in text:
        return text.split("</think>", 1)[1].strip()
    if text.startswith("<think>"):
        return ""
    return text.strip()


def detect_repetition_loop(text: str) -> bool:
    if len(text) < 1500:
        return False
    n = len(text)
    for start in range(0, min(n - 200, 3000), 100):
        chunk = text[start:start + 60].strip()
        if len(chunk) < 30:
            continue
        if text.count(chunk) >= 4:
            return True
    return False


def classify_generic(content: str, mode: str) -> str:
    raw = content or ""
    if not raw.strip():
        return "EMPTY"
    if detect_repetition_loop(raw):
        return "REPETITION_LOOP"
    if mode == "no_think":
        if "<think>" in raw or "</think>" in raw:
            return "PROMPT_IGNORED"
        if len(raw.strip()) < 30:
            return "QUALITY_LOW"
        return "SUCCESS"
    if not has_close_think(raw) and len(raw) > 800:
        return "THINK_RUNAWAY"
    final = visible_answer(raw)
    if not final:
        return "EMPTY_AFTER_THINK"
    return "SUCCESS"


# ---------- Gold rule parsing ----------

def parse_gold_rule(rule: str) -> Dict[str, str]:
    """Parse `key=value;key=value` pairs.

    `must_include=a|b|c` becomes {'must_include': 'a|b|c'}. The pipe-separated
    list is later split into individual required tokens.
    """
    out: Dict[str, str] = {}
    if not rule:
        return out
    for part in rule.split(";"):
        part = part.strip()
        if not part or "=" not in part:
            continue
        k, v = part.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def required_tokens(rule_dict: Dict[str, str]) -> List[str]:
    raw = rule_dict.get("must_include", "")
    if not raw:
        return []
    return [t.strip() for t in raw.split("|") if t.strip()]


def excluded_tokens(rule_dict: Dict[str, str]) -> List[str]:
    raw = rule_dict.get("exclude_keyword", "")
    if not raw:
        return []
    return [t.strip() for t in raw.split("|") if t.strip()]


# ---------- Specialized classifiers ----------

PERSONA_RECALL_TRIGGERS = (
    "정리해줘", "정리해 줘", "정리.", "요약해줘", "요약해 줘",
    "페르소나", "내가 누구", "누구인지",
)

RECALL_TRIGGERS = (
    "다시 말해", "기억", "잊지 않았", "처음에", "아까", "잠깐 뭐로", "맞췄는지", "맞춰봐",
)

CLARIFY_INVITE_TRIGGERS = (
    "먼저 질문", "먼저 물어", "더 알아야", "정보가 부족",
)

# Hanja-derived Korean nouns commonly avoided when teaching beginners.
HANJA_VOCAB_HINTS = re.compile(
    r"(전통|문화|행사|풍습|역사|관광|체험|국가|지역|건축|유산|"
    r"고궁|민속|민족|예술|기념|교육|학습|환영|초대|준비|정보)"
)

ROMAN_PATTERN = re.compile(r"[A-Za-z]")
ENGLISH_TOKEN_PATTERN = re.compile(r"\b[A-Za-z]{2,}\b")

# Patterns to count enumerated items in a response.
NUMBERED_ITEM_RE = re.compile(r"(?m)^\s*\d+\s*[.)]\s+\S")
BULLET_ITEM_RE = re.compile(r"(?m)^\s*[-*•·]\s+\S")
CIRCLED_NUM_RE = re.compile(r"[①-⑳]")


def count_list_items(text: str) -> int:
    nums = NUMBERED_ITEM_RE.findall(text)
    if nums:
        return len(nums)
    bullets = BULLET_ITEM_RE.findall(text)
    if bullets:
        return len(bullets)
    circled = CIRCLED_NUM_RE.findall(text)
    if circled:
        return len(circled)
    return 0


def is_persona_recall_turn(user_msg: str) -> bool:
    return any(tok in user_msg for tok in PERSONA_RECALL_TRIGGERS)


def is_recall_turn(user_msg: str) -> bool:
    return any(tok in user_msg for tok in RECALL_TRIGGERS)


def is_clarify_invite_turn(user_msg: str) -> bool:
    return any(tok in user_msg for tok in CLARIFY_INVITE_TRIGGERS)


def specialized_classify(
    track: str,
    turn_idx: int,
    total_turns: int,
    user_msg: str,
    answer: str,
    gold_dict: Dict[str, str],
) -> Optional[str]:
    """Return a specialized failure label, or None if no specialized issue."""
    answer = answer or ""
    final_text = visible_answer(answer)
    if not final_text:
        return None

    if track == "persona":
        if is_persona_recall_turn(user_msg):
            tokens = required_tokens(gold_dict)
            if tokens:
                missing = [t for t in tokens if t not in final_text]
                if missing:
                    return f"PERSONA_RECALL_FAIL(missing={','.join(missing)})"
        return None

    if track == "multiturn":
        if is_recall_turn(user_msg):
            tokens = required_tokens(gold_dict)
            if tokens:
                missing = [t for t in tokens if t not in final_text]
                if len(missing) == len(tokens) and tokens:
                    return f"CONTEXT_LOSS(missing={','.join(missing)})"
        # item_count check: only on the final turn (when user asks for "최종본")
        if turn_idx == total_turns and "item_count" in gold_dict:
            try:
                expected = int(gold_dict["item_count"])
                actual = count_list_items(final_text)
                if actual != expected:
                    return f"ITEM_COUNT_MISMATCH(expected={expected},got={actual})"
            except ValueError:
                pass
        return None

    if track == "foreigner_lang":
        violations = []
        if gold_dict.get("avoid_hanja") == "true":
            hits = HANJA_VOCAB_HINTS.findall(final_text)
            if len(hits) >= 3:
                violations.append(f"hanja_hits={len(hits)}")
        if gold_dict.get("vocab_level") == "beginner":
            sentences = re.split(r"[.!?。\n]+", final_text)
            long_count = sum(1 for s in sentences if len(s.strip()) > 40)
            if long_count >= 2:
                violations.append(f"long_sentences={long_count}")
        if gold_dict.get("include_romanization") == "true":
            if not ROMAN_PATTERN.search(final_text):
                violations.append("no_romanization")
        if gold_dict.get("trilingual_format") == "true":
            has_korean = bool(re.search(r"[가-힣]", final_text))
            has_english = len(ENGLISH_TOKEN_PATTERN.findall(final_text)) >= 3
            if not (has_korean and has_english):
                violations.append("not_trilingual")
        if gold_dict.get("banmal_required") == "true":
            if "습니다" in final_text or "세요" in final_text:
                violations.append("uses_formal_register")
        if gold_dict.get("include_english_terms") == "true":
            english_hits = len(ENGLISH_TOKEN_PATTERN.findall(final_text))
            if english_hits == 0:
                violations.append("no_english_terms")
        # allow_english_gloss=true is a permission (no failure if absent),
        # so we don't add a violation for it.
        if violations:
            return f"VOCAB_MISMATCH({';'.join(violations)})"
        return None

    if track == "recommendation":
        # clarify_first check: at the turn that invites clarification, model
        # should ask a question instead of dumping a full recommendation list.
        if (
            gold_dict.get("clarify_first") == "true"
            and is_clarify_invite_turn(user_msg)
        ):
            has_question = "?" in final_text or "？" in final_text
            recs_dumped = count_list_items(final_text) >= 3
            if not has_question or recs_dumped:
                return "CLARIFY_SKIPPED(no_question_or_dumped_list)"
        if turn_idx == total_turns:  # final synthesis turn
            tokens = required_tokens(gold_dict)
            if tokens:
                missing = [t for t in tokens if t not in final_text]
                if len(missing) >= max(1, len(tokens) // 2):
                    return f"RECOMMENDATION_GENERIC(missing={','.join(missing)})"
            excluded = excluded_tokens(gold_dict)
            if excluded:
                hit_excluded = [t for t in excluded if t in final_text]
                if hit_excluded:
                    return f"RECOMMENDATION_GENERIC(included_excluded={','.join(hit_excluded)})"
        return None

    return None


# ---------- Loading ----------

def load_run(path: str, mode: str) -> List[Dict]:
    sessions = []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            try:
                conv = json.loads(row.get("generated_conversation_json", "[]"))
            except Exception:
                conv = []
            try:
                lats = json.loads(row.get("turn_latencies_ms_a", "[]"))
            except Exception:
                lats = []
            user_turns: List[str] = []
            assistant_turns: List[Dict] = []
            for m in conv:
                role = m.get("role")
                content = m.get("content") or ""
                if role == "user":
                    user_turns.append(content)
                elif role == "assistant":
                    assistant_turns.append({"raw": content})

            track = (row.get("task_track") or "").strip()
            gold_dict = parse_gold_rule(row.get("gold_answer_or_rule") or "")
            total_turns = len(user_turns)

            classified = []
            for i, (u, a) in enumerate(zip(user_turns, assistant_turns), start=1):
                generic = classify_generic(a["raw"], mode)
                spec = None
                if generic == "SUCCESS":
                    spec = specialized_classify(
                        track, i, total_turns, u, a["raw"], gold_dict
                    )
                final_class = spec if spec else generic
                classified.append({
                    "turn_idx": i,
                    "user_msg": u,
                    "raw": a["raw"],
                    "final_text": visible_answer(a["raw"]),
                    "generic": generic,
                    "specialized": spec,
                    "class": final_class,
                    "latency_ms": lats[i - 1] if i - 1 < len(lats) else None,
                })

            sessions.append({
                "session_id": row.get("session_id", ""),
                "task_track": track,
                "task_subtype": row.get("task_subtype", ""),
                "gold_rule": row.get("gold_answer_or_rule", ""),
                "turns": classified,
            })
    return sessions


# ---------- Reporting ----------

def render_report(sessions: List[Dict], mode: str) -> str:
    lines: List[str] = []
    lines.append(f"# 4축 평가 결과 ({mode} 모드)\n")

    # Overall
    all_turns = [t for s in sessions for t in s["turns"]]
    total = len(all_turns)
    success = sum(1 for t in all_turns if t["class"] == "SUCCESS")
    lines.append("## 1. 전체 요약")
    lines.append("")
    lines.append(f"- 세션 수: {len(sessions)}")
    lines.append(f"- 총 turn: {total}")
    lines.append(f"- 성공 turn: {success} ({success / total * 100:.1f}%)" if total else "- 성공 turn: 0")
    success_lats = [t["latency_ms"] for t in all_turns if t["class"] == "SUCCESS" and t["latency_ms"]]
    fail_lats = [t["latency_ms"] for t in all_turns if t["class"] != "SUCCESS" and t["latency_ms"]]
    if success_lats:
        lines.append(f"- 성공 latency 중앙값: {median(success_lats) / 1000:.1f}s")
    if fail_lats:
        lines.append(f"- 실패 latency 중앙값: {median(fail_lats) / 1000:.1f}s")
    lines.append("")

    # Per-track
    lines.append("## 2. 트랙별 성공률")
    lines.append("")
    lines.append("| 트랙 | 성공/전체 | 성공률 |")
    lines.append("|---|---|---|")
    by_track = defaultdict(list)
    for s in sessions:
        for t in s["turns"]:
            by_track[s["task_track"]].append(t)
    for track in ["persona", "multiturn", "foreigner_lang", "recommendation"]:
        ts = by_track.get(track, [])
        if not ts:
            continue
        suc = sum(1 for t in ts if t["class"] == "SUCCESS")
        lines.append(f"| {track} | {suc}/{len(ts)} | {suc / len(ts) * 100:.1f}% |")
    lines.append("")

    # Failure distribution
    lines.append("## 3. 실패 유형 분포")
    lines.append("")
    lines.append("### 3.1 일반 실패")
    counter_generic = Counter(t["generic"] for t in all_turns if t["generic"] != "SUCCESS")
    if counter_generic:
        lines.append("")
        lines.append("| 유형 | 개수 |")
        lines.append("|---|---|")
        for k, v in counter_generic.most_common():
            lines.append(f"| {k} | {v} |")
    else:
        lines.append("")
        lines.append("(없음)")

    lines.append("")
    lines.append("### 3.2 4축 특화 실패 (generic=SUCCESS이지만 트랙 기준 미충족)")
    spec_counter = Counter()
    for t in all_turns:
        if t["specialized"]:
            head = t["specialized"].split("(", 1)[0]
            spec_counter[head] += 1
    if spec_counter:
        lines.append("")
        lines.append("| 유형 | 개수 |")
        lines.append("|---|---|")
        for k, v in spec_counter.most_common():
            lines.append(f"| {k} | {v} |")
    else:
        lines.append("")
        lines.append("(없음)")
    lines.append("")

    # Per-session matrix
    lines.append("## 4. 세션별 turn 결과")
    lines.append("")
    for s in sessions:
        lines.append(f"### {s['session_id']} ({s['task_track']} / {s['task_subtype']})")
        lines.append("")
        lines.append("| Turn | User (요약) | 분류 | 답 길이 | latency(s) |")
        lines.append("|---|---|---|---|---|")
        for t in s["turns"]:
            user_short = (t["user_msg"][:40] + "…") if len(t["user_msg"]) > 40 else t["user_msg"]
            user_short = user_short.replace("|", "/").replace("\n", " ")
            cls_short = t["class"]
            if len(cls_short) > 60:
                cls_short = cls_short[:57] + "…"
            lat = f"{t['latency_ms'] / 1000:.1f}" if t["latency_ms"] else "-"
            lines.append(
                f"| {t['turn_idx']} | {user_short} | {cls_short} | {len(t['final_text'])} | {lat} |"
            )
        lines.append("")

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="run_multiturn_generative.py output CSV")
    p.add_argument("--mode", choices=["think", "no_think"], default="think")
    p.add_argument("--output", required=True, help="markdown report path")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    sessions = load_run(args.input, args.mode)
    report = render_report(sessions, args.mode)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"wrote {args.output}: {len(sessions)} sessions")


if __name__ == "__main__":
    main()
