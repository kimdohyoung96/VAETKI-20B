# 4축 평가 결과 (think 모드)

## 1. 전체 요약

- 세션 수: 20
- 총 turn: 200
- 성공 turn: 123 (61.5%)
- 성공 latency 중앙값: 4.6s
- 실패 latency 중앙값: 7.8s

## 2. 트랙별 성공률

| 트랙 | 성공/전체 | 성공률 |
|---|---|---|
| persona | 29/50 | 58.0% |
| multiturn | 39/50 | 78.0% |
| foreigner_lang | 27/50 | 54.0% |
| recommendation | 28/50 | 56.0% |

## 3. 실패 유형 분포

### 3.1 일반 실패

| 유형 | 개수 |
|---|---|
| THINK_RUNAWAY | 36 |
| EMPTY | 26 |
| REPETITION_LOOP | 2 |

### 3.2 4축 특화 실패 (generic=SUCCESS이지만 트랙 기준 미충족)

| 유형 | 개수 |
|---|---|
| VOCAB_MISMATCH | 6 |
| PERSONA_RECALL_FAIL | 2 |
| RECOMMENDATION_GENERIC | 2 |
| CONTEXT_LOSS | 1 |
| ITEM_COUNT_MISMATCH | 1 |
| CLARIFY_SKIPPED | 1 |

## 4. 세션별 turn 결과

### PER-MT-101 (persona / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 안녕하세요. 박물관 가이드 도움 받고 싶어요. | EMPTY | 0 | 34.0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | EMPTY | 0 | 33.7 |
| 3 | 한국어는 일상 회화 정도만 가능해요. | SUCCESS | 696 | 5.1 |
| 4 | 한국 역사 잘 몰라요. 조선시대 이런 거 들어본 적 없어요. | SUCCESS | 732 | 6.5 |
| 5 | 그림이나 도자기 같은 거 보는 거 좋아해요. | THINK_RUNAWAY | 807 | 5.5 |
| 6 | 8살 딸이랑 같이 가요. 짧게 보고 싶어요. | THINK_RUNAWAY | 904 | 6.1 |
| 7 | 딸은 오래 걷는 걸 싫어해서 이동이 적었으면 해요. | THINK_RUNAWAY | 1121 | 7.3 |
| 8 | 저는 쉬운 한국어 설명이 있으면 좋아요. | THINK_RUNAWAY | 1138 | 6.6 |
| 9 | 영어 안내가 있으면 도움은 되지만 꼭 필요하진 않아요. | THINK_RUNAWAY | 1138 | 7.0 |
| 10 | 위 정보를 모두 반영해서 저와 딸의 관람 페르소나를 한 단락으로 정리해주… | THINK_RUNAWAY | 1138 | 7.8 |

### PER-MT-102 (persona / defector_settlement)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 안녕하세요. 도움 받고 싶어서요. | SUCCESS | 234 | 3.4 |
| 2 | 작년에 한국 왔어요. 50대 여자입니다. | SUCCESS | 256 | 3.3 |
| 3 | 혼자 살고 있어요. 평양 출신이에요. | SUCCESS | 204 | 3.3 |
| 4 | 장사 좀 해보고 싶은데 한국 시스템을 잘 몰라요. 컴퓨터도 약해요. | SUCCESS | 557 | 4.6 |
| 5 | 스마트폰은 전화랑 문자 정도만 익숙해요. | SUCCESS | 253 | 3.6 |
| 6 | 온라인 신청이라는 말이 나오면 긴장이 돼요. | SUCCESS | 542 | 5.4 |
| 7 | 가게를 바로 크게 시작할 생각은 없어요. | SUCCESS | 226 | 3.9 |
| 8 | 먼저 배워보고 천천히 준비하고 싶어요. | EMPTY | 0 | 34.4 |
| 9 | 서울에 살지만 동네 밖으로 멀리 가는 건 부담돼요. | SUCCESS | 648 | 5.2 |
| 10 | 위 정보로 제 상황을 한 단락 페르소나로 정리해주세요. | PERSONA_RECALL_FAIL(missing=평양) | 128 | 2.4 |

### PER-MT-103 (persona / elderly_culture)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 안녕하세요. 우리 동네 문화센터 어떻게 다닐지 좀 알려줘요. | SUCCESS | 647 | 4.3 |
| 2 | 75살이고 무릎이 안 좋아서 멀리는 못 다녀요. | THINK_RUNAWAY | 945 | 6.4 |
| 3 | 글씨 작은 건 잘 안 보여요. 큰 글씨로 부탁해요. | THINK_RUNAWAY | 947 | 5.5 |
| 4 | 옛날에 노래 부르는 거 좋아했어요. 가곡 같은 거. | SUCCESS | 313 | 4.4 |
| 5 | 친구 사귀고 싶어요. 혼자 너무 적적해요. | THINK_RUNAWAY | 992 | 6.6 |
| 6 | 계단이 많은 곳은 피하고 싶어요. | THINK_RUNAWAY | 963 | 6.4 |
| 7 | 버스로 한 번에 갈 수 있으면 좋겠어요. | THINK_RUNAWAY | 963 | 6.7 |
| 8 | 오전보다는 오후 시간이 편해요. | THINK_RUNAWAY | 963 | 6.1 |
| 9 | 수업 시간이 너무 길면 힘들어요. | THINK_RUNAWAY | 963 | 6.7 |
| 10 | 위 정보로 제 문화센터 이용 페르소나를 정리해주세요. | THINK_RUNAWAY | 1410 | 8.8 |

### PER-MT-104 (persona / office_worker_fitness)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 운동 좀 시작하려고. | SUCCESS | 390 | 3.7 |
| 2 | 32살 직장인이고 사무실에서 하루 종일 앉아 있어. | SUCCESS | 294 | 5.1 |
| 3 | 키 175, 몸무게 82kg. | SUCCESS | 307 | 5.3 |
| 4 | 허리가 자주 아파. | SUCCESS | 290 | 5.2 |
| 5 | 헬스장은 부담스럽고 집에서 할 수 있는 거 좋아. | SUCCESS | 298 | 4.7 |
| 6 | 시간은 평일 저녁 30분 정도밖에 못 내. | SUCCESS | 255 | 34.1 |
| 7 | 식단도 신경 쓰고 싶은데 요리는 잘 못해. | SUCCESS | 545 | 4.6 |
| 8 | 아침은 자주 거르고 점심은 회사 근처에서 먹어. | SUCCESS | 298 | 5.5 |
| 9 | 퇴근하면 피곤해서 강도 높은 운동은 자신 없어. | SUCCESS | 312 | 5.6 |
| 10 | 위 정보 다 종합해서 내 운동 페르소나를 한 단락으로 정리해줘. | PERSONA_RECALL_FAIL(missing=집,30분) | 360 | 6.4 |

### PER-MT-105 (persona / parent_kid_education)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 우리 아이 학습 도움 받고 싶어요. | SUCCESS | 220 | 2.9 |
| 2 | 초등학교 3학년 딸이에요. | SUCCESS | 252 | 3.3 |
| 3 | 수학을 어려워해요. 특히 분수 부분. | EMPTY | 0 | 34.1 |
| 4 | 책 읽는 건 좋아하는데 혼자만 하려고 해요. | SUCCESS | 671 | 5.5 |
| 5 | 문제집을 오래 붙잡고 있으면 금방 지쳐요. | SUCCESS | 787 | 6.4 |
| 6 | 그림이 있는 설명은 잘 보는 편이에요. | SUCCESS | 653 | 5.3 |
| 7 | 말로 설명하면 중간에 딴생각을 해요. | SUCCESS | 668 | 5.6 |
| 8 | 분모와 분자를 자꾸 헷갈려요. | EMPTY | 0 | 35.7 |
| 9 | 학교 숙제는 미루다가 밤에 하는 편이에요. | SUCCESS | 687 | 6.1 |
| 10 | 위 정보로 우리 아이 학습 페르소나를 정리해주세요. | SUCCESS | 764 | 7.8 |

### MTN-MT-101 (multiturn / intent_repair)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 저녁 메뉴 추천해줘. | SUCCESS | 250 | 3.1 |
| 2 | 한식 말고. | SUCCESS | 171 | 2.7 |
| 3 | 아 미안, 한식도 괜찮아. 단 너무 매운 건 빼고. | EMPTY | 0 | 33.5 |
| 4 | 고기는 가능하지만 튀김은 싫어. | SUCCESS | 331 | 3.7 |
| 5 | 조리 시간은 20분 안쪽이면 좋겠어. | SUCCESS | 162 | 3.6 |
| 6 | 집에 계란이랑 두부가 있어. | SUCCESS | 399 | 4.2 |
| 7 | 밥은 이미 해놨어. | SUCCESS | 450 | 4.3 |
| 8 | 국물 요리는 오늘은 별로야. | SUCCESS | 430 | 4.0 |
| 9 | 냉장고에 애호박도 조금 있어. | SUCCESS | 443 | 4.3 |
| 10 | 최종 저녁 메뉴와 이유를 짧게 다시 말해줘. | CONTEXT_LOSS(missing=저녁) | 372 | 3.8 |

### MTN-MT-102 (multiturn / tone_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 안녕하세요. 한국 여행 정보 부탁드립니다. | SUCCESS | 183 | 3.2 |
| 2 | 정중하게 안내해주세요. 저는 외국인이에요. | SUCCESS | 265 | 2.3 |
| 3 | 경주 추천 받고 싶어요. | SUCCESS | 237 | 3.0 |
| 4 | 역사 설명은 너무 어렵지 않게 부탁드립니다. | SUCCESS | 237 | 3.0 |
| 5 | 하루 일정으로만 보고 싶습니다. | SUCCESS | 396 | 3.5 |
| 6 | 이제 친구처럼 편하게 말해줘. 반말로. | SUCCESS | 236 | 3.3 |
| 7 | 거기서 뭘 봐야 돼? | SUCCESS | 447 | 3.9 |
| 8 | 밥 먹을 곳도 하나 넣어줘. | SUCCESS | 267 | 3.2 |
| 9 | 걷는 시간이 너무 길면 힘들어. | SUCCESS | 396 | 4.6 |
| 10 | 처음부터 지금까지 말투가 몇 번 바뀌었는지도 알려 주세요. | SUCCESS | 158 | 3.1 |

### MTN-MT-103 (multiturn / reference_tracking)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 무릎 통증 때문에 병원 두 곳 알아봤어요. 정형외과랑 한의원. | THINK_RUNAWAY | 821 | 5.6 |
| 2 | 거기 둘 중 70대한테 더 맞는 곳은? | THINK_RUNAWAY | 1116 | 7.8 |
| 3 | 정형외과는 검사 장비가 있다고 들었어요. | THINK_RUNAWAY | 1134 | 10.7 |
| 4 | 한의원은 침 치료가 가능하대요. | SUCCESS | 373 | 5.5 |
| 5 | 그 곳 보험 적용돼요? | THINK_RUNAWAY | 847 | 6.1 |
| 6 | 어느 쪽이 먼저 진단받기에 좋아요? | SUCCESS | 551 | 7.6 |
| 7 | 통증이 오래됐으면 어디가 우선이에요? | SUCCESS | 766 | 35.1 |
| 8 | 걷기 힘든 날에는 대기 시간이 짧은 곳이 좋아요. | SUCCESS | 780 | 5.9 |
| 9 | 약을 많이 먹는 건 부담스러워요. | THINK_RUNAWAY | 879 | 7.5 |
| 10 | 내 조건 중 나이와 무릎 통증을 포함해서 최종 정리해주세요. | SUCCESS | 255 | 8.3 |

### MTN-MT-104 (multiturn / topic_switch_return)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 회의록 정리하는 법 알려줘. | EMPTY | 0 | 33.5 |
| 2 | 가장 효과적인 방법은? | SUCCESS | 423 | 4.6 |
| 3 | 회의 참석자가 8명 정도일 때 기준으로 알려줘. | SUCCESS | 278 | 7.7 |
| 4 | 결정사항과 액션아이템을 분리하고 싶어. | SUCCESS | 311 | 6.9 |
| 5 | 잠깐, 다른 거 물어봐도 돼? 노션이랑 옵시디언 차이가 뭐야? | SUCCESS | 666 | 7.3 |
| 6 | 둘 중 회의록에 더 적합한 건? | SUCCESS | 800 | 4.6 |
| 7 | 가격은 어떻게 돼? | SUCCESS | 677 | 5.0 |
| 8 | 회사 공유용이면 어떤 도구가 나아? | SUCCESS | 727 | 5.7 |
| 9 | 개인 지식관리용이면 어떤 도구가 좋아? | SUCCESS | 640 | 3.8 |
| 10 | 최종적으로 회의록 정리 프로세스만 5단계로 출력해줘. | THINK_RUNAWAY | 1803 | 9.2 |

### MTN-MT-105 (multiturn / constraint_accumulation)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 한국 정착할 때 신청해야 하는 지원금 알려주세요. | SUCCESS | 592 | 4.4 |
| 2 | 정확히 3가지만. | SUCCESS | 21 | 2.8 |
| 3 | 각 항목 옆에 신청 기관도 같이. | SUCCESS | 46 | 2.2 |
| 4 | 각 항목 30자 이내로 짧게. | SUCCESS | 46 | 1.9 |
| 5 | 마지막은 새터민이 가장 먼저 알아야 할 순서로 정렬해주세요. | SUCCESS | 46 | 2.2 |
| 6 | 온라인 신청이 필요한지 여부도 표시해주세요. | SUCCESS | 82 | 1.2 |
| 7 | 컴퓨터가 약한 사람 기준으로 쉬운 순서를 원해요. | EMPTY | 0 | 34.3 |
| 8 | 전화 문의가 가능한지도 적어주세요. | SUCCESS | 112 | 3.3 |
| 9 | 금액은 확실하지 않으면 쓰지 마세요. | SUCCESS | 82 | 1.4 |
| 10 | 마지막에 추가 설명은 쓰지 마세요. | ITEM_COUNT_MISMATCH(expected=3,got=0) | 82 | 1.1 |

### FRN-MT-101 (foreigner_lang / beginner_restaurant)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 한국어 잘 못해요. 천천히 쉽게 말해주세요. | SUCCESS | 627 | 33.9 |
| 2 | 식당에서 주문하고 싶어요. 어떻게 말해요? | SUCCESS | 604 | 34.3 |
| 3 | "이거 주세요" 무엇이에요? | SUCCESS | 364 | 33.6 |
| 4 | 매운 거 싫어요. 어떻게 말해요? | EMPTY | 0 | 33.8 |
| 5 | 물 주세요는 어떻게 말해요? | EMPTY | 0 | 34.3 |
| 6 | 계산하고 싶을 때 뭐라고 해요? | EMPTY | 0 | 34.2 |
| 7 | 고기 안 먹어요. 쉬운 말로 알려주세요. | SUCCESS | 796 | 34.2 |
| 8 | 혼자 먹어도 돼요? 어떻게 물어요? | EMPTY | 0 | 34.8 |
| 9 | 포장하고 싶어요. 짧게 말해주세요. | EMPTY | 0 | 35.1 |
| 10 | 지금까지 얘기 다시. 짧게. 쉬운 단어만. | EMPTY | 0 | 34.7 |

### FRN-MT-102 (foreigner_lang / code_switching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 안녕하세요. I'm learning Korean. | SUCCESS | 336 | 3.4 |
| 2 | "처마" 무슨 뜻이에요? Is it about the roof? | VOCAB_MISMATCH(no_english_terms) | 265 | 2.9 |
| 3 | 한옥 설명해주세요. 어려우면 영어 단어 쓰셔도 돼요. | VOCAB_MISMATCH(no_english_terms) | 222 | 3.2 |
| 4 | 기와는 영어로 roof tile 맞아요? | SUCCESS | 212 | 2.5 |
| 5 | 마루는 floor랑 같아요? | SUCCESS | 227 | 2.8 |
| 6 | 온돌은 heating system이라고 보면 돼요? | SUCCESS | 187 | 2.4 |
| 7 | 한옥 보러 가고 싶어요. 어디 가요? | EMPTY | 0 | 4.4 |
| 8 | 서울에서 가기 쉬운 곳이면 좋아요. | VOCAB_MISMATCH(no_english_terms) | 599 | 3.8 |
| 9 | 입장료 비싸요? | VOCAB_MISMATCH(no_english_terms) | 326 | 3.6 |
| 10 | 위 내용 다시 정리. Korean first, then English s… | EMPTY | 0 | 34.3 |

### FRN-MT-103 (foreigner_lang / english_to_korean_teaching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | Hi! Can you help me practice Korean? | SUCCESS | 538 | 4.1 |
| 2 | I want to order food in Korean. Teach me… | SUCCESS | 497 | 3.4 |
| 3 | How do I say "no spicy please"? | SUCCESS | 245 | 6.2 |
| 4 | 한국어로 다시 말해주세요. 천천히. | SUCCESS | 245 | 3.6 |
| 5 | 발음도 알려줘요. 로마자로요. | SUCCESS | 245 | 4.2 |
| 6 | "감사합니다" 발음도 알려주세요. | EMPTY | 0 | 33.8 |
| 7 | Can you include English meaning every ti… | SUCCESS | 260 | 6.7 |
| 8 | I need Korean, romanization, and English… | SUCCESS | 260 | 3.5 |
| 9 | How do I say "water please"? | SUCCESS | 260 | 2.5 |
| 10 | 마지막에 가장 중요한 표현 2개만 다시 골라주세요. | SUCCESS | 260 | 3.0 |

### FRN-MT-104 (foreigner_lang / avoid_hanja_hospital)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 한국어 공부해요. 한자어 어려워요. 병원 갈 때 쉬운 말로 알려주세요. | SUCCESS | 379 | 4.9 |
| 2 | "감기" 같은 단어 말고 다른 쉬운 말로 증상 설명하는 법. | SUCCESS | 472 | 33.4 |
| 3 | 머리가 아파요를 더 쉬운 말로도 알려주세요. | EMPTY | 0 | 34.3 |
| 4 | 배가 아플 때 말하는 문장 알려주세요. | REPETITION_LOOP | 7818 | 33.9 |
| 5 | 열이 나는 것 같아요를 쉬운 말로요. | EMPTY | 0 | 37.6 |
| 6 | 목이 따가워요는 어떻게 말해요? | SUCCESS | 357 | 4.9 |
| 7 | 기침이 나와요는 쉬운가요? | EMPTY | 0 | 37.3 |
| 8 | 병원에서 접수하는 법 쉽게 알려주세요. | SUCCESS | 550 | 6.3 |
| 9 | 이름을 말할 때 문장 알려주세요. | SUCCESS | 259 | 4.1 |
| 10 | 병원에서 처음부터 끝까지 말할 순서만 알려주세요. | SUCCESS | 554 | 6.7 |

### FRN-MT-105 (foreigner_lang / register_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 한국어 책으로 공부했어요. 너무 formal해요. | EMPTY | 0 | 33.5 |
| 2 | 친구한테 쓸 말 알려주세요. 평어/반말로요. | THINK_RUNAWAY | 1727 | 10.8 |
| 3 | "안녕하세요" → 친구한테는 어떻게 말해요? "감사합니다"는요? | EMPTY | 0 | 34.5 |
| 4 | 카페에서 음료 주문할 때 일상적인 말투로. | REPETITION_LOOP | 7495 | 34.2 |
| 5 | 친구에게 밥 먹자고 말하는 표현 알려줘. | SUCCESS | 463 | 37.2 |
| 6 | 미안해를 자연스럽게 말하는 방법은? | SUCCESS | 318 | 37.4 |
| 7 | 괜찮습니다 말고 편한 말로 바꿔줘. | VOCAB_MISMATCH(uses_formal_register) | 362 | 37.6 |
| 8 | 잘 지내세요 말고 친구한테 쓰는 말은? | VOCAB_MISMATCH(uses_formal_register) | 338 | 38.2 |
| 9 | 너무 무례하지 않은 반말이면 좋겠어. | SUCCESS | 306 | 38.0 |
| 10 | 마지막에는 반말 표현만 번호로 정리해줘. | SUCCESS | 321 | 38.8 |

### REC-MT-101 (recommendation / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 한국 박물관 가보고 싶어요. 어디가 좋을까요? | THINK_RUNAWAY | 1952 | 10.4 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | 214 | 3.7 |
| 3 | 한국어는 일상 회화 정도예요. | SUCCESS | 438 | 4.9 |
| 4 | 한국 역사 잘 몰라요. | SUCCESS | 384 | 4.1 |
| 5 | 그림이나 도자기 좋아해요. | SUCCESS | 326 | 3.1 |
| 6 | 8살 딸이랑 같이 가요. | THINK_RUNAWAY | 1136 | 8.6 |
| 7 | 너무 길거나 어려운 곳 말고요. | THINK_RUNAWAY | 1584 | 9.8 |
| 8 | 대중교통으로 가기 쉬운 곳이면 좋겠어요. | THINK_RUNAWAY | 1146 | 7.1 |
| 9 | 아이에게 설명하기 쉬운 전시가 필요해요. | THINK_RUNAWAY | 1227 | 7.3 |
| 10 | 위 정보 다 반영해서 박물관 3곳 추천 + 각각 이유. | THINK_RUNAWAY | 1225 | 7.6 |

### REC-MT-102 (recommendation / defector_settlement_program)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 한국 정착 프로그램 추천해주세요. | SUCCESS | 274 | 3.8 |
| 2 | 50대 여자, 평양 출신이에요. 작년에 한국 왔어요. | SUCCESS | 557 | 4.9 |
| 3 | 혼자 살고 있어요. | SUCCESS | 420 | 3.6 |
| 4 | 장사 해보고 싶어요. 컴퓨터는 약해요. | SUCCESS | 445 | 5.6 |
| 5 | 서울에 살아요. | EMPTY | 0 | 34.2 |
| 6 | 너무 빨리 진행되는 건 따라가기 힘들어요. | SUCCESS | 452 | 4.3 |
| 7 | 온라인 신청보다 방문 상담이 편해요. | SUCCESS | 396 | 4.1 |
| 8 | 창업 전에 기초 교육부터 받고 싶어요. | SUCCESS | 332 | 4.5 |
| 9 | 소상공인이라는 말도 아직 어려워요. | SUCCESS | 351 | 4.4 |
| 10 | 위 조건 다 반영해서 정착 지원 프로그램 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=50대,장사,서울,혼자) | 339 | 7.6 |

### REC-MT-103 (recommendation / elderly_culture_event)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 우리 동네 문화행사 추천 좀 해주세요. | THINK_RUNAWAY | 1528 | 8.6 |
| 2 | 75살이에요. 무릎이 안 좋아요. | SUCCESS | 765 | 9.7 |
| 3 | 큰 글씨, 큰 화면이면 좋아요. | THINK_RUNAWAY | 971 | 7.7 |
| 4 | 가곡이나 옛날 노래 좋아해요. | SUCCESS | 462 | 7.1 |
| 5 | 친구 사귈 수 있는 곳이면 더 좋고요. | SUCCESS | 314 | 7.4 |
| 6 | 오래 서 있는 행사는 어렵습니다. | THINK_RUNAWAY | 819 | 8.1 |
| 7 | 버스로 갈 수 있는 곳이 좋아요. | EMPTY | 0 | 5.0 |
| 8 | 계단이 적은 장소를 원해요. | SUCCESS | 318 | 35.4 |
| 9 | 오후 시간이 편합니다. | SUCCESS | 323 | 35.8 |
| 10 | 위 조건 다 반영해서 행사 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=가곡) | 404 | 36.0 |

### REC-MT-104 (recommendation / office_worker_fitness_diet)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 운동 루틴이랑 식단 추천해줘. | SUCCESS | 476 | 4.5 |
| 2 | 32살 사무직, 허리가 자주 아파. | SUCCESS | 601 | 9.3 |
| 3 | 집에서 할 수 있는 거 위주. | SUCCESS | 311 | 7.1 |
| 4 | 평일 저녁 30분. | SUCCESS | 651 | 4.9 |
| 5 | 요리 잘 못해. | SUCCESS | 537 | 4.6 |
| 6 | 키 175에 몸무게 82kg이야. | THINK_RUNAWAY | 854 | 6.2 |
| 7 | 헬스장은 당분간 안 갈 생각이야. | THINK_RUNAWAY | 922 | 6.9 |
| 8 | 요가매트는 있어. | SUCCESS | 764 | 5.8 |
| 9 | 허리에 부담 가는 윗몸일으키기는 싫어. | THINK_RUNAWAY | 908 | 6.1 |
| 10 | 위 정보로 1주 운동 + 식단 표로 추천해줘. | THINK_RUNAWAY | 876 | 6.6 |

### REC-MT-105 (recommendation / student_learning_resource)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 학습 자료 추천해줘. | SUCCESS | 648 | 4.7 |
| 2 | 정보 부족하면 먼저 질문해줘. | CLARIFY_SKIPPED(no_question_or_dumped_list) | 648 | 4.2 |
| 3 | 컴퓨터공학 전공 3학년이야. | SUCCESS | 728 | 5.0 |
| 4 | 머신러닝 기초 공부하고 싶어. | SUCCESS | 746 | 5.4 |
| 5 | 한국어 자료가 더 편해. 영어도 가능은 함. | SUCCESS | 625 | 7.1 |
| 6 | 책보단 무료 강의가 좋아. | SUCCESS | 279 | 7.5 |
| 7 | 수학 백그라운드는 미적분/선형대수 학부 수준. | EMPTY | 0 | 34.9 |
| 8 | 파이썬은 기본 문법 정도 알아. | EMPTY | 0 | 34.9 |
| 9 | 딥러닝보다 머신러닝 개념부터 하고 싶어. | THINK_RUNAWAY | 965 | 7.2 |
| 10 | 위 정보로 학습 자료 3개 추천 + 각각 이유. | THINK_RUNAWAY | 965 | 6.0 |
