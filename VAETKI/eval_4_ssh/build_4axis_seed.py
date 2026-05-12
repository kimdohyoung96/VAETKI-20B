"""Build evaluation seed for the 4-axis VAEKI evaluation.

Axes:
  1. persona         — accumulated info → integrated persona
  2. multiturn       — context recall, intent repair, tone shift, constraint accumulation
  3. foreigner_lang  — adapt vocabulary/length/formality to learner level (foreigner-only)
  4. recommendation  — personalized recommendation grounded in accumulated context

User groups (mixed across axes 1/2/4; axis 3 is foreigner-only by definition):
  - 다문화 (multicultural foreigner) — PDF target
  - 새터민 (North Korean defector)   — PDF target
  - 노년층 (elderly)                 — PDF target
  - 직장인 (office worker), 육아 부모, 대학생, 일반인 — diversity

Domains: 박물관·정착·생활문화 (PDF) + 운동·의료·교육·직장·행정·관광·일상

Output: evaluation_4axis_seed.csv (5 sessions per axis = 20 sessions, 4~8 turns mixed)
"""

from __future__ import annotations

import csv
import json
from typing import Dict, List


def s(
    session_id: str,
    track: str,
    subtype: str,
    difficulty: str,
    domain: str,
    length_bucket: str,
    constraint_level: str,
    gold_rule: str,
    user_turns: List[str],
    user_group: str = "",
) -> Dict[str, str]:
    conv = [{"role": "user", "content": t} for t in user_turns]
    notes = f"user_group={user_group}" if user_group else ""
    return {
        "session_id": session_id,
        "task_track": track,
        "task_subtype": subtype,
        "difficulty": difficulty,
        "domain": domain,
        "length_bucket": length_bucket,
        "constraint_level": constraint_level,
        "prompt_text": "",
        "expected_format": "free_text",
        "gold_answer_or_rule": gold_rule,
        "model_a_name_hidden": "A",
        "model_b_name_hidden": "B",
        "notes": notes,
        "conversation_json": json.dumps(conv, ensure_ascii=False),
    }


# ---------- Axis 1: persona (5 sessions, turns: 7/5/6/8/5) ----------
PERSONA_SESSIONS = [
    s(
        "PER-MT-101", "persona", "multicultural_museum", "high", "museum", "medium", "high",
        "must_include=베트남|2년|일상 회화|딸|조선",
        [
            "안녕하세요. 박물관 가이드 도움 받고 싶어요.",
            "베트남에서 왔고 한국 온 지 2년 됐어요.",
            "한국어는 일상 회화 정도만 가능해요.",
            "한국 역사 잘 몰라요. 조선시대 이런 거 들어본 적 없어요.",
            "그림이나 도자기 같은 거 보는 거 좋아해요.",
            "8살 딸이랑 같이 가요. 짧게 보고 싶어요.",
            "위 정보 종합해서 저랑 딸의 관람 페르소나 한 단락으로 정리해주세요.",
        ],
        user_group="다문화",
    ),
    s(
        "PER-MT-102", "persona", "defector_settlement", "high", "settlement", "short", "high",
        "must_include=50대|평양|혼자|컴퓨터",
        [
            "안녕하세요. 도움 받고 싶어서요.",
            "작년에 한국 왔어요. 50대 여자입니다.",
            "혼자 살고 있어요. 평양 출신이에요.",
            "장사 좀 해보고 싶은데 한국 시스템을 잘 몰라요. 컴퓨터도 약해요.",
            "위 정보로 제 상황 한 단락으로 정리해주세요.",
        ],
        user_group="새터민",
    ),
    s(
        "PER-MT-103", "persona", "elderly_culture", "medium", "elderly_culture", "medium", "medium",
        "must_include=75|무릎|가곡|혼자",
        [
            "안녕하세요. 우리 동네 문화센터 어떻게 다닐지 좀 알려줘요.",
            "75살이고 무릎이 안 좋아서 멀리는 못 다녀요.",
            "글씨 작은 건 잘 안 보여요. 큰 글씨로 부탁해요.",
            "옛날에 노래 부르는 거 좋아했어요. 가곡 같은 거.",
            "친구 사귀고 싶어요. 혼자 너무 적적해요.",
            "위 정보로 제 페르소나 정리해주세요.",
        ],
        user_group="노년층",
    ),
    s(
        "PER-MT-104", "persona", "office_worker_fitness", "high", "fitness", "long", "medium",
        "must_include=32|허리|집|30분",
        [
            "운동 좀 시작하려고.",
            "32살 직장인이고 사무실에서 하루 종일 앉아 있어.",
            "키 175, 몸무게 82kg.",
            "허리가 자주 아파.",
            "헬스장은 부담스럽고 집에서 할 수 있는 거 좋아.",
            "시간은 평일 저녁 30분 정도밖에 못 내.",
            "식단도 신경 쓰고 싶은데 요리는 잘 못해.",
            "위 정보 다 종합해서 내 페르소나 한 단락으로 정리해줘.",
        ],
        user_group="직장인",
    ),
    s(
        "PER-MT-105", "persona", "parent_kid_education", "medium", "education", "short", "medium",
        "must_include=초등|3학년|수학|분수",
        [
            "우리 아이 학습 도움 받고 싶어요.",
            "초등학교 3학년 딸이에요.",
            "수학을 어려워해요. 특히 분수 부분.",
            "책 읽는 건 좋아하는데 혼자만 하려고 해요.",
            "위 정보로 우리 아이 학습 페르소나 정리해주세요.",
        ],
        user_group="육아 부모",
    ),
]


# ---------- Axis 2: multiturn (5 sessions, turns: 4/7/5/8/6) ----------
MULTITURN_SESSIONS = [
    s(
        "MTN-MT-101", "multiturn", "intent_repair", "medium", "food", "short", "medium",
        "must_include=저녁",
        [
            "저녁 메뉴 추천해줘.",
            "한식 말고.",
            "아 미안, 한식도 괜찮아. 단 너무 매운 건 빼고.",
            "내가 처음에 뭘 부탁했지?",
        ],
        user_group="일반",
    ),
    s(
        "MTN-MT-102", "multiturn", "tone_shift", "high", "tourism", "medium", "high",
        "must_include=경주",
        [
            "안녕하세요. 한국 여행 정보 부탁드립니다.",
            "정중하게 안내해주세요. 저는 외국인이에요.",
            "경주 추천 받고 싶어요.",
            "이제 친구처럼 편하게 말해줘. 반말로.",
            "거기서 뭘 봐야 돼?",
            "다시 정중하게 돌아가 주세요. 격식체로요.",
            "위에서 추천한 곳들 격식체로 한 줄씩 다시 정리해 주세요.",
        ],
        user_group="다문화",
    ),
    s(
        "MTN-MT-103", "multiturn", "reference_tracking", "medium", "healthcare", "short", "medium",
        "must_include=정형외과|한의원",
        [
            "무릎 통증 때문에 병원 두 곳 알아봤어요. 정형외과랑 한의원.",
            "거기 둘 중 70대한테 더 맞는 곳은?",
            "그 곳 보험 적용돼요?",
            "거기 가는 길에 약국도 들를 수 있나요?",
            "처음에 비교한 두 군데 이름 다시 말해줘요.",
        ],
        user_group="노년층",
    ),
    s(
        "MTN-MT-104", "multiturn", "topic_switch_return", "high", "work", "long", "medium",
        "must_include=회의록|노션",
        [
            "회의록 정리하는 법 알려줘.",
            "가장 효과적인 방법은?",
            "잠깐, 다른 거 물어봐도 돼? 노션이랑 옵시디언 차이가 뭐야?",
            "둘 중 회의록에 더 적합한 건?",
            "가격은 어떻게 돼?",
            "아까 회의록 얘기로 돌아가서, 두 번째로 효과적인 정리 방법은?",
            "그 방법 단점도 알려줘.",
            "우리가 회의록 얘기 하다가 잠깐 뭐로 빠졌었지?",
        ],
        user_group="직장인",
    ),
    s(
        "MTN-MT-105", "multiturn", "constraint_accumulation", "high", "settlement", "medium", "high",
        "must_include=지원금;item_count=3",
        [
            "한국 정착할 때 신청해야 하는 지원금 알려주세요.",
            "정확히 3가지만.",
            "각 항목 옆에 신청 기관도 같이.",
            "각 항목 30자 이내로 짧게.",
            "마지막은 새터민이 가장 먼저 알아야 할 순서로 정렬해주세요.",
            "위 모든 제약 다 지켜서 최종본만 출력.",
        ],
        user_group="새터민",
    ),
]


# ---------- Axis 3: foreigner_lang (5 sessions, all foreigner — turns: 5/6/7/4/5) ----------
FOREIGNER_LANG_SESSIONS = [
    s(
        "FRN-MT-101", "foreigner_lang", "beginner_restaurant", "high", "food", "short", "high",
        "vocab_level=beginner;avoid_hanja=true;short_sentences=true",
        [
            "한국어 잘 못해요. 천천히 쉽게 말해주세요.",
            "식당에서 주문하고 싶어요. 어떻게 말해요?",
            "\"이거 주세요\" 무엇이에요?",
            "매운 거 싫어요. 어떻게 말해요?",
            "지금까지 얘기 다시. 짧게. 쉬운 단어만.",
        ],
        user_group="다문화",
    ),
    s(
        "FRN-MT-102", "foreigner_lang", "code_switching", "medium", "culture", "medium", "medium",
        "allow_english_gloss=true;include_english_terms=true",
        [
            "안녕하세요. I'm learning Korean.",
            "\"처마\" 무슨 뜻이에요? Is it about the roof?",
            "한옥 설명해주세요. 어려우면 영어 단어 쓰셔도 돼요.",
            "한옥 보러 가고 싶어요. 어디 가요?",
            "입장료 비싸요?",
            "위 내용 다시 정리. Korean first, then English summary.",
        ],
        user_group="다문화",
    ),
    s(
        "FRN-MT-103", "foreigner_lang", "english_to_korean_teaching", "high", "language_learning", "medium", "high",
        "include_romanization=true;trilingual_format=true",
        [
            "Hi! Can you help me practice Korean?",
            "I want to order food in Korean. Teach me basic phrases.",
            "How do I say \"no spicy please\"?",
            "한국어로 다시 말해주세요. 천천히.",
            "발음도 알려줘요. 로마자로요.",
            "\"감사합니다\" 발음도 알려주세요.",
            "위 표현 5개 정리. 한국어 + 로마자 발음 + 영어 의미 형식으로.",
        ],
        user_group="다문화",
    ),
    s(
        "FRN-MT-104", "foreigner_lang", "avoid_hanja_hospital", "high", "healthcare", "short", "high",
        "avoid_hanja=true;use_native_korean=true",
        [
            "한국어 공부해요. 한자어 어려워요. 병원 갈 때 쉬운 말로 알려주세요.",
            "\"감기\" 같은 단어 말고 다른 쉬운 말로 증상 설명하는 법.",
            "병원에서 접수하는 법 쉽게 알려주세요.",
            "지금까지 다 정리해주세요. 한자어 0개로.",
        ],
        user_group="다문화",
    ),
    s(
        "FRN-MT-105", "foreigner_lang", "register_shift", "medium", "language_learning", "short", "medium",
        "use_casual_speech=true;banmal_required=true",
        [
            "한국어 책으로 공부했어요. 너무 formal해요.",
            "친구한테 쓸 말 알려주세요. 평어/반말로요.",
            "\"안녕하세요\" → 친구한테는 어떻게 말해요? \"감사합니다\"는요?",
            "카페에서 음료 주문할 때 일상적인 말투로.",
            "위 전부 다시. 친구한테 말하는 말투로.",
        ],
        user_group="다문화",
    ),
]


# ---------- Axis 4: recommendation (5 sessions, turns: 8/7/6/6/8) ----------
RECOMMENDATION_SESSIONS = [
    s(
        "REC-MT-101", "recommendation", "multicultural_museum", "high", "museum", "long", "high",
        "must_include=베트남|딸|도자기|박물관",
        [
            "한국 박물관 가보고 싶어요. 어디가 좋을까요?",
            "베트남에서 왔고 한국 온 지 2년 됐어요.",
            "한국어는 일상 회화 정도예요.",
            "한국 역사 잘 몰라요.",
            "그림이나 도자기 좋아해요.",
            "8살 딸이랑 같이 가요.",
            "너무 길거나 어려운 곳 말고요.",
            "위 정보 다 반영해서 박물관 3곳 추천 + 각각 이유.",
        ],
        user_group="다문화",
    ),
    s(
        "REC-MT-102", "recommendation", "defector_settlement_program", "high", "settlement", "medium", "high",
        "must_include=50대|장사|서울|혼자",
        [
            "한국 정착 프로그램 추천해주세요.",
            "50대 여자, 평양 출신이에요. 작년에 한국 왔어요.",
            "혼자 살고 있어요.",
            "장사 해보고 싶어요. 컴퓨터는 약해요.",
            "서울에 살아요.",
            "너무 빨리 진행되는 건 따라가기 힘들어요.",
            "위 조건 다 반영해서 정착 지원 프로그램 3개 추천 + 이유.",
        ],
        user_group="새터민",
    ),
    s(
        "REC-MT-103", "recommendation", "elderly_culture_event", "medium", "elderly_culture", "medium", "high",
        "must_include=75|가곡|친구",
        [
            "우리 동네 문화행사 추천 좀 해주세요.",
            "75살이에요. 무릎이 안 좋아요.",
            "큰 글씨, 큰 화면이면 좋아요.",
            "가곡이나 옛날 노래 좋아해요.",
            "친구 사귈 수 있는 곳이면 더 좋고요.",
            "위 조건 다 반영해서 행사 3개 추천 + 이유.",
        ],
        user_group="노년층",
    ),
    s(
        "REC-MT-104", "recommendation", "office_worker_fitness_diet", "medium", "fitness", "medium", "high",
        "must_include=허리|집|30분",
        [
            "운동 루틴이랑 식단 추천해줘.",
            "32살 사무직, 허리가 자주 아파.",
            "집에서 할 수 있는 거 위주.",
            "평일 저녁 30분.",
            "요리 잘 못해.",
            "위 정보로 1주 운동 + 식단 표로 추천해줘.",
        ],
        user_group="직장인",
    ),
    s(
        "REC-MT-105", "recommendation", "student_learning_resource", "high", "education", "long", "high",
        "must_include=머신러닝|3학년;clarify_first=true",
        [
            "학습 자료 추천해줘.",
            "정보 부족하면 먼저 질문해줘.",
            "컴퓨터공학 전공 3학년이야.",
            "머신러닝 기초 공부하고 싶어.",
            "한국어 자료가 더 편해. 영어도 가능은 함.",
            "책보단 무료 강의가 좋아.",
            "수학 백그라운드는 미적분/선형대수 학부 수준.",
            "위 정보로 학습 자료 3개 추천 + 각각 이유.",
        ],
        user_group="대학생",
    ),
]


def main() -> None:
    all_sessions = (
        PERSONA_SESSIONS
        + MULTITURN_SESSIONS
        + FOREIGNER_LANG_SESSIONS
        + RECOMMENDATION_SESSIONS
    )

    fieldnames = [
        "session_id",
        "task_track",
        "task_subtype",
        "difficulty",
        "domain",
        "length_bucket",
        "constraint_level",
        "prompt_text",
        "expected_format",
        "gold_answer_or_rule",
        "model_a_name_hidden",
        "model_b_name_hidden",
        "model_a_output",
        "model_b_output",
        "auto_format_pass_a",
        "auto_format_pass_b",
        "auto_constraint_pass_a",
        "auto_constraint_pass_b",
        "auto_accuracy_a",
        "auto_accuracy_b",
        "human_naturalness_a",
        "human_naturalness_b",
        "human_consistency_a",
        "human_consistency_b",
        "human_tone_a",
        "human_tone_b",
        "human_safety_a",
        "human_safety_b",
        "winner_human",
        "latency_ms_a",
        "latency_ms_b",
        "p95_group_tag",
        "cost_per_req_a",
        "cost_per_req_b",
        "error_flag_a",
        "error_flag_b",
        "notes",
        "conversation_json",
    ]

    out_path = "evaluation_4axis_seed.csv"
    with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for sess in all_sessions:
            row = {k: sess.get(k, "") for k in fieldnames}
            writer.writerow(row)

    by_track: Dict[str, List[int]] = {}
    by_group: Dict[str, int] = {}
    by_domain: Dict[str, int] = {}
    total_turns = 0
    for sess in all_sessions:
        n_turns = len(json.loads(sess["conversation_json"]))
        by_track.setdefault(sess["task_track"], []).append(n_turns)
        total_turns += n_turns
        # parse user_group from notes
        notes = sess.get("notes", "")
        for kv in notes.split(";"):
            if kv.startswith("user_group="):
                ug = kv.split("=", 1)[1]
                by_group[ug] = by_group.get(ug, 0) + 1
        by_domain[sess["domain"]] = by_domain.get(sess["domain"], 0) + 1

    print(f"wrote {out_path}: {len(all_sessions)} sessions, {total_turns} total user turns")
    print()
    for track, turns in by_track.items():
        print(f"  {track}: {len(turns)} sessions, turns={turns}")
    print()
    print("user_group distribution:")
    for g, n in sorted(by_group.items(), key=lambda x: -x[1]):
        print(f"  {g}: {n}")
    print()
    print("domain distribution:")
    for d, n in sorted(by_domain.items(), key=lambda x: -x[1]):
        print(f"  {d}: {n}")


if __name__ == "__main__":
    main()
