# VAEKI 4축 평가 인프라 — 파일 설명

> 첨부 파일 4종에 대한 안내 문서
> 작성일: 2026-05-07

VAETKI 모델의 4축 평가(페르소나 도출 / 멀티턴 유지 / 외국인 언어 적응 / 맞춤형 추천)를 수행하기 위한 최소 구성 4파일입니다. 시드 → 러너 → 분류기 순서로 흐릅니다.

---

## 파일 목록 한눈에

| 파일 | 역할 |
|---|---|
| `build_4axis_seed.py` | 시드 빌더 (재실행 가능, 시드 수정 시 여기 수정) |
| `evaluation_4axis_seed.csv` | **4축 평가 시드 — 20세션 / 123턴** |
| `run_multiturn_generative.py` | 멀티턴 러너 (생성형 — 모델이 자기 응답을 누적해서 진짜 멀티턴 수행) |
| `analyze_4axis.py` | 자동 분류기 (4축 특화 실패 분류 + 리포트 생성) |

---

## 1. `build_4axis_seed.py` — 시드 빌더

**무엇을 하는가**
4축 평가용 시드 CSV(`evaluation_4axis_seed.csv`)를 코드로 생성합니다. 트랙별 시나리오, 사용자 발화 5~8턴, 자동 채점 룰(DSL)이 모두 이 파일 안에 하드코딩되어 있습니다.

**언제 건드리는가**
- 시드 시나리오를 추가/수정/삭제할 때 (CSV를 직접 편집하지 말고 여기서 수정 후 재생성)
- 트랙별 세션 수를 늘릴 때 (예: 약한 트랙만 +5세션 보강)

**산출물**
`evaluation_4axis_seed.csv` (20세션 / 123턴)

**실행**
```bash
PYTHONIOENCODING=utf-8 python build_4axis_seed.py
```

---

## 2. `evaluation_4axis_seed.csv` — 평가 시드

**무엇이 들어있나**
- 20세션 × 평균 6턴 = **총 123턴**의 사용자 발화
- 트랙별 5세션씩: `persona` / `multiturn` / `foreigner_lang` / `recommendation`
- 각 세션마다 자동 채점 룰(`gold_answer_or_rule` 컬럼, DSL 형식)

**핵심 컬럼**
| 컬럼 | 의미 |
|---|---|
| `session_id` | PER/MTN/FRN/REC + 번호 |
| `task_track` | 4축 중 하나 (러너가 트랙별 시스템 프롬프트 분기에 사용) |
| `task_subtype` | 세부 시나리오 라벨 |
| `gold_answer_or_rule` | 자동 분류기가 읽는 평가 룰 (DSL) |
| `notes` | `user_group=다문화` 형태로 사용자 집단 기록 |
| `conversation_json` | **유저 발화 5~8턴 (JSON 배열)** — 러너가 한 턴씩 흘려보냄 |

> 시드에는 `[user]` 발화만 미리 정의되어 있고, 모델 응답은 러너가 실시간 생성·누적합니다.

**분포**
- 턴 수: 4턴 2 / 5턴 5 / 6턴 5 / 7턴 4 / 8턴 4
- 사용자 집단: 다문화 8 / 새터민 3 / 노년층 3 / 직장인 3 / 부모 1 / 학생 1 / 일반 1
- 도메인: 박물관·정착·생활문화(과제 PDF 타깃) 8 + 운동·교육·의료·직장·행정·일상·관광 12

---

## 3. `run_multiturn_generative.py` — 멀티턴 러너 (생성형)

**무엇을 하는가**
시드의 user 발화를 한 턴씩 모델에 입력하고, **모델 자기 응답을 history에 누적해 진짜 멀티턴 대화를 수행**합니다. 트랙별로 시스템 프롬프트를 분기합니다.

**왜 새로 만들었나 (1차 시드와의 차이)**
1차 멀티턴 시드는 `[assistant]`가 스크립트된 가짜 응답이라 진짜 멀티턴이 아니었습니다. 이 러너는 user 발화만 입력으로 받고, 매 턴 모델이 자기 응답을 history에 쌓아가며 실제 대화를 시뮬레이션합니다.

**핵심 설계 결정**
- **think-strip**: 매 턴 모델 출력에서 `<think>...</think>`를 제거한 뒤 history에 넣음 → 컨텍스트 폭증 완화
- **skip-empty**: EMPTY 응답은 history에 넣지 않음 → 후속 턴 cascade 가속 방지
- **`--resume`**: 중단 시 이미 완료된 세션 스킵
- **`--no-think`**: 시스템 프롬프트로 reasoning 금지 모드 비교 실행

**실행 (think 사용 모드, 본실행)**
```bash
PYTHONIOENCODING=utf-8 python -u run_multiturn_generative.py \
  --input evaluation_4axis_seed.csv \
  --output multiturn_4axis_20b_results.csv \
  --base-url-a http://[VLLM_HOST]/v1 --model-a vaetki20b \
  --only-a --temperature 0.2 --top-p 0.9 --max-tokens 4096 --timeout 600 \
  2>&1 | tee multiturn_4axis_20b_run.log
```

**예상 소요시간**: 2~5시간 (실패 turn은 timeout 530s까지 도달 가능)

**산출물**: `multiturn_4axis_20b_results.csv` (각 턴의 모델 응답 + 메타데이터)

---

## 4. `analyze_4axis.py` — 자동 분류기

**무엇을 하는가**
러너 결과 CSV를 읽어 **2단계로 실패를 분류**하고 마크다운 리포트를 생성합니다.

**2단계 분류**

1단계 — Generic 분류 (모든 turn에 적용, 6종)
- `SUCCESS` / `EMPTY` / `THINK_RUNAWAY` / `EMPTY_AFTER_THINK` / `REPETITION_LOOP` / `PROMPT_IGNORED` / `QUALITY_LOW`

2단계 — 4축 특화 분류 (1단계 SUCCESS만 재판정)
- `PERSONA_RECALL_FAIL` (persona): 누적 정보 토큰 누락
- `CONTEXT_LOSS` / `ITEM_COUNT_MISMATCH` (multiturn): 회상·항목수 위반
- `VOCAB_MISMATCH` (foreigner_lang): 한자어/긴문장/로마자/반말/영어 위반
- `RECOMMENDATION_GENERIC` (recommendation): 사용자 조건 절반 이상 누락
- `CLARIFY_SKIPPED` (recommendation): 질문 없이 추천 dump

**Gold rule DSL** (`gold_answer_or_rule` 컬럼)

세미콜론으로 키-값 쌍 구분, `must_include`는 파이프(`|`)로 다중 토큰:
```
must_include=베트남|2년|딸;exclude_keyword=책;item_count=3
```

지원 키:
| 키 | 적용 트랙 | 동작 |
|---|---|---|
| `must_include=A\|B\|C` | persona, multiturn, recommendation | 마지막 답변에 토큰 포함 검사 |
| `exclude_keyword=X\|Y` | recommendation | 답변에 들어가면 안 되는 토큰 |
| `item_count=N` | multiturn | 마지막 답변에 항목이 정확히 N개 |
| `vocab_level=beginner` | foreigner_lang | 긴 문장(40자+) 2개+ 시 위반 |
| `avoid_hanja=true` | foreigner_lang | 한자어 빈도 3+ 시 위반 |
| `include_romanization=true` | foreigner_lang | 로마자 알파벳 부재 시 위반 |
| `trilingual_format=true` | foreigner_lang | 한국어+영어 동시 부재 시 위반 |
| `banmal_required=true` | foreigner_lang | "습니다"/"세요" 출현 시 위반 |
| `include_english_terms=true` | foreigner_lang | 영어 토큰 0개 시 위반 |
| `clarify_first=true` | recommendation | turn 2에서 질문 없이 추천 dump 시 위반 |

**실행**
```bash
PYTHONIOENCODING=utf-8 python analyze_4axis.py \
  --input multiturn_4axis_20b_results.csv \
  --mode think \
  --output multiturn_4axis_20b_report.md
```

**산출물**: 마크다운 리포트 (요약 / 트랙별 성공률 / 실패 유형 분포 / 세션별 turn 매트릭스)

**룰 추가/수정**
`specialized_classify()` 함수에 트랙별 분기로 키를 추가하면 됩니다.

---

## 실행 순서 (전체 파이프라인)

```
[수정 시] build_4axis_seed.py
              ↓ 생성
       evaluation_4axis_seed.csv
              ↓ 입력
     run_multiturn_generative.py  (vLLM 엔드포인트 호출)
              ↓ 산출
     multiturn_4axis_20b_results.csv
              ↓ 입력
       analyze_4axis.py
              ↓ 산출
     multiturn_4axis_20b_report.md  ← 최종 리포트
```

---

## 환경 요구사항

- Python 3.13
- 패키지: `openai` (OpenAI 호환 API 클라이언트)
- vLLM 서버: VAETKI 20B (또는 비교 대상 모델)가 OpenAI 호환 모드로 떠 있어야 함
- 인코딩: 모든 CSV는 UTF-8 with BOM (`utf-8-sig`). Windows 콘솔에서 한글 출력 시 `PYTHONIOENCODING=utf-8` 환경변수 필수
