# 평가 결과

## 1. 전체 요약

- 세션 수: 20
- 총 turn: 200
- 성공 turn: 137 (68.5%)
- 성공 latency 중앙값: 3.5s
- 실패 latency 중앙값: 34.4s

## 1-1. Summary Memory / Recent-Turn 진단

- prompt token 중앙값: 1366
- prompt token 최대값: 2123
- memory token 중앙값: 423
- memory token 최대값: 799
- reply token 중앙값: 492
- reply token 최대값: 4995
- clean source 분포: visible=200
- debug status 분포: NORMAL=130, RUNAWAY=64, REPETITION_LOOP=6

## 2. 트랙별 성공률

| 트랙 | 성공/전체 | 성공률 |
|---|---|---|
| persona | 40/50 | 80.0% |
| multiturn | 48/50 | 96.0% |
| foreigner_lang | 14/50 | 28.0% |
| recommendation | 35/50 | 70.0% |

## 3. 실패 유형 분포

### 3.1 일반 실패

| 유형 | 개수 |
|---|---|
| REPETITION_LOOP | 29 |
| THINK_RUNAWAY | 11 |

### 3.2 4축 특화 실패 (generic=SUCCESS이지만 트랙 기준 미충족)

| 유형 | 개수 |
|---|---|
| VOCAB_MISMATCH | 13 |
| PERSONA_RECALL_FAIL | 4 |
| RECOMMENDATION_GENERIC | 4 |
| ITEM_COUNT_MISMATCH | 1 |
| CLARIFY_SKIPPED | 1 |

## 4. 세션별 turn 결과

### PER-MT-101 (persona / multicultural_museum)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 박물관 가이드 도움 받고 싶어요. | SUCCESS | NORMAL | visible | 283 | 288 | 192 | 2.8 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | NORMAL | visible | 494 | 272 | 228 | 2.3 |
| 3 | 한국어는 일상 회화 정도만 가능해요. | SUCCESS | NORMAL | visible | 731 | 317 | 227 | 2.5 |
| 4 | 한국 역사 잘 몰라요. 조선시대 이런 거 들어본 적 없어요. | SUCCESS | NORMAL | visible | 972 | 262 | 185 | 2.3 |
| 5 | 그림이나 도자기 같은 거 보는 거 좋아해요. | SUCCESS | NORMAL | visible | 1195 | 368 | 275 | 3.2 |
| 6 | 8살 딸이랑 같이 가요. 짧게 보고 싶어요. | SUCCESS | NORMAL | visible | 1340 | 389 | 240 | 3.5 |
| 7 | 딸은 오래 걷는 걸 싫어해서 이동이 적었으면 해요. | SUCCESS | NORMAL | visible | 1452 | 346 | 228 | 3.0 |
| 8 | 저는 쉬운 한국어 설명이 있으면 좋아요. | SUCCESS | NORMAL | visible | 1560 | 628 | 240 | 5.0 |
| 9 | 영어 안내가 있으면 도움은 되지만 꼭 필요하진 않아요. | SUCCESS | NORMAL | visible | 1585 | 356 | 240 | 2.9 |
| 10 | 위 정보를 모두 반영해서 저와 딸의 관람 페르소나를 한 단락으로 정리해주… | PERSONA_RECALL_FAIL(missing=베트남,일상 회화,딸,조선) | NORMAL | visible | 1580 | 277 | 233 | 2.4 |

### PER-MT-102 (persona / defector_settlement)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 도움 받고 싶어서요. | SUCCESS | NORMAL | visible | 279 | 258 | 73 | 1.9 |
| 2 | 작년에 한국 왔어요. 50대 여자입니다. | SUCCESS | NORMAL | visible | 384 | 281 | 82 | 2.2 |
| 3 | 혼자 살고 있어요. 평양 출신이에요. | SUCCESS | NORMAL | visible | 508 | 316 | 137 | 2.6 |
| 4 | 장사 좀 해보고 싶은데 한국 시스템을 잘 몰라요. 컴퓨터도 약해요. | THINK_RUNAWAY | RUNAWAY | visible | 695 | 4144 | 825 | 34.2 |
| 5 | 스마트폰은 전화랑 문자 정도만 익숙해요. | SUCCESS | NORMAL | visible | 1076 | 485 | 360 | 3.6 |
| 6 | 온라인 신청이라는 말이 나오면 긴장이 돼요. | SUCCESS | NORMAL | visible | 1325 | 398 | 360 | 3.0 |
| 7 | 가게를 바로 크게 시작할 생각은 없어요. | THINK_RUNAWAY | RUNAWAY | visible | 1568 | 4264 | 854 | 34.5 |
| 8 | 먼저 배워보고 천천히 준비하고 싶어요. | SUCCESS | NORMAL | visible | 1853 | 212 | 422 | 1.5 |
| 9 | 서울에 살지만 동네 밖으로 멀리 가는 건 부담돼요. | SUCCESS | NORMAL | visible | 1912 | 218 | 434 | 1.7 |
| 10 | 위 정보로 제 상황을 한 단락 페르소나로 정리해주세요. | SUCCESS | NORMAL | visible | 2002 | 227 | 453 | 1.8 |

### PER-MT-103 (persona / elderly_culture)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 우리 동네 문화센터 어떻게 다닐지 좀 알려줘요. | SUCCESS | NORMAL | visible | 287 | 360 | 408 | 2.7 |
| 2 | 75살이고 무릎이 안 좋아서 멀리는 못 다녀요. | SUCCESS | REPETITION_LOOP | visible | 612 | 483 | 494 | 4.0 |
| 3 | 글씨 작은 건 잘 안 보여요. 큰 글씨로 부탁해요. | SUCCESS | NORMAL | visible | 987 | 503 | 408 | 4.1 |
| 4 | 옛날에 노래 부르는 거 좋아했어요. 가곡 같은 거. | SUCCESS | NORMAL | visible | 1320 | 332 | 291 | 2.9 |
| 5 | 친구 사귀고 싶어요. 혼자 너무 적적해요. | THINK_RUNAWAY | RUNAWAY | visible | 1593 | 3848 | 867 | 34.2 |
| 6 | 계단이 많은 곳은 피하고 싶어요. | REPETITION_LOOP | RUNAWAY | visible | 1734 | 4066 | 1691 | 34.5 |
| 7 | 버스로 한 번에 갈 수 있으면 좋겠어요. | REPETITION_LOOP | RUNAWAY | visible | 1837 | 4278 | 8556 | 34.8 |
| 8 | 오전보다는 오후 시간이 편해요. | REPETITION_LOOP | RUNAWAY | visible | 1980 | 4284 | 8567 | 35.0 |
| 9 | 수업 시간이 너무 길면 힘들어요. | SUCCESS | NORMAL | visible | 2072 | 465 | 460 | 3.9 |
| 10 | 위 정보로 제 문화센터 이용 페르소나를 정리해주세요. | PERSONA_RECALL_FAIL(missing=혼자) | NORMAL | visible | 2051 | 381 | 316 | 3.2 |

### PER-MT-104 (persona / office_worker_fitness)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 운동 좀 시작하려고. | SUCCESS | NORMAL | visible | 276 | 333 | 329 | 2.5 |
| 2 | 32살 직장인이고 사무실에서 하루 종일 앉아 있어. | SUCCESS | NORMAL | visible | 551 | 462 | 329 | 3.8 |
| 3 | 키 175, 몸무게 82kg. | SUCCESS | NORMAL | visible | 836 | 485 | 468 | 4.3 |
| 4 | 허리가 자주 아파. | SUCCESS | NORMAL | visible | 1184 | 414 | 430 | 3.5 |
| 5 | 헬스장은 부담스럽고 집에서 할 수 있는 거 좋아. | SUCCESS | NORMAL | visible | 1519 | 431 | 368 | 3.7 |
| 6 | 시간은 평일 저녁 30분 정도밖에 못 내. | SUCCESS | NORMAL | visible | 1649 | 459 | 399 | 4.0 |
| 7 | 식단도 신경 쓰고 싶은데 요리는 잘 못해. | SUCCESS | NORMAL | visible | 1788 | 588 | 694 | 4.8 |
| 8 | 아침은 자주 거르고 점심은 회사 근처에서 먹어. | SUCCESS | NORMAL | visible | 1912 | 387 | 348 | 3.2 |
| 9 | 퇴근하면 피곤해서 강도 높은 운동은 자신 없어. | SUCCESS | NORMAL | visible | 1887 | 958 | 254 | 7.8 |
| 10 | 위 정보 다 종합해서 내 운동 페르소나를 한 단락으로 정리해줘. | PERSONA_RECALL_FAIL(missing=32,집) | NORMAL | visible | 1833 | 459 | 438 | 3.9 |

### PER-MT-105 (persona / parent_kid_education)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 우리 아이 학습 도움 받고 싶어요. | SUCCESS | NORMAL | visible | 280 | 439 | 475 | 3.4 |
| 2 | 초등학교 3학년 딸이에요. | SUCCESS | NORMAL | visible | 625 | 497 | 483 | 3.9 |
| 3 | 수학을 어려워해요. 특히 분수 부분. | SUCCESS | NORMAL | visible | 985 | 631 | 678 | 5.3 |
| 4 | 책 읽는 건 좋아하는데 혼자만 하려고 해요. | SUCCESS | NORMAL | visible | 1359 | 641 | 701 | 5.4 |
| 5 | 문제집을 오래 붙잡고 있으면 금방 지쳐요. | SUCCESS | NORMAL | visible | 1734 | 357 | 217 | 2.8 |
| 6 | 그림이 있는 설명은 잘 보는 편이에요. | SUCCESS | RUNAWAY | visible | 1709 | 4122 | 292 | 34.9 |
| 7 | 말로 설명하면 중간에 딴생각을 해요. | SUCCESS | NORMAL | visible | 1719 | 420 | 404 | 3.5 |
| 8 | 분모와 분자를 자꾸 헷갈려요. | SUCCESS | NORMAL | visible | 1771 | 395 | 503 | 3.7 |
| 9 | 학교 숙제는 미루다가 밤에 하는 편이에요. | SUCCESS | NORMAL | visible | 1769 | 408 | 402 | 3.3 |
| 10 | 위 정보로 우리 아이 학습 페르소나를 정리해주세요. | PERSONA_RECALL_FAIL(missing=초등,3학년,분수) | NORMAL | visible | 1869 | 330 | 189 | 2.8 |

### MTN-MT-101 (multiturn / intent_repair)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 저녁 메뉴 추천해줘. | SUCCESS | NORMAL | visible | 257 | 304 | 288 | 2.5 |
| 2 | 한식 말고. | SUCCESS | RUNAWAY | visible | 501 | 3604 | 283 | 33.8 |
| 3 | 아 미안, 한식도 괜찮아. 단 너무 매운 건 빼고. | SUCCESS | NORMAL | visible | 761 | 502 | 288 | 4.3 |
| 4 | 고기는 가능하지만 튀김은 싫어. | SUCCESS | RUNAWAY | visible | 1029 | 4097 | 183 | 33.9 |
| 5 | 조리 시간은 20분 안쪽이면 좋겠어. | SUCCESS | RUNAWAY | visible | 1240 | 4096 | 182 | 34.3 |
| 6 | 집에 계란이랑 두부가 있어. | SUCCESS | RUNAWAY | visible | 1291 | 3816 | 232 | 34.0 |
| 7 | 밥은 이미 해놨어. | SUCCESS | RUNAWAY | visible | 1367 | 3921 | 185 | 34.4 |
| 8 | 국물 요리는 오늘은 별로야. | SUCCESS | RUNAWAY | visible | 1406 | 4010 | 189 | 34.2 |
| 9 | 냉장고에 애호박도 조금 있어. | SUCCESS | RUNAWAY | visible | 1508 | 3647 | 238 | 34.9 |
| 10 | 최종 저녁 메뉴와 이유를 짧게 다시 말해줘. | SUCCESS | RUNAWAY | visible | 1540 | 3648 | 192 | 34.4 |

### MTN-MT-102 (multiturn / tone_shift)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 한국 여행 정보 부탁드립니다. | SUCCESS | REPETITION_LOOP | visible | 263 | 645 | 536 | 5.3 |
| 2 | 정중하게 안내해주세요. 저는 외국인이에요. | SUCCESS | REPETITION_LOOP | visible | 627 | 476 | 543 | 4.0 |
| 3 | 경주 추천 받고 싶어요. | SUCCESS | NORMAL | visible | 996 | 501 | 609 | 4.5 |
| 4 | 역사 설명은 너무 어렵지 않게 부탁드립니다. | SUCCESS | NORMAL | visible | 1366 | 388 | 267 | 3.3 |
| 5 | 하루 일정으로만 보고 싶습니다. | SUCCESS | NORMAL | visible | 1622 | 377 | 318 | 3.2 |
| 6 | 이제 친구처럼 편하게 말해줘. 반말로. | SUCCESS | NORMAL | visible | 1631 | 387 | 315 | 3.3 |
| 7 | 거기서 뭘 봐야 돼? | SUCCESS | NORMAL | visible | 1635 | 307 | 315 | 2.8 |
| 8 | 밥 먹을 곳도 하나 넣어줘. | SUCCESS | NORMAL | visible | 1641 | 313 | 448 | 3.0 |
| 9 | 걷는 시간이 너무 길면 힘들어. | SUCCESS | NORMAL | visible | 1724 | 68 | 134 | 0.7 |
| 10 | 처음부터 지금까지 말투가 몇 번 바뀌었는지도 알려 주세요. | SUCCESS | NORMAL | visible | 1727 | 736 | 661 | 6.3 |

### MTN-MT-103 (multiturn / reference_tracking)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 무릎 통증 때문에 병원 두 곳 알아봤어요. 정형외과랑 한의원. | SUCCESS | REPETITION_LOOP | visible | 269 | 409 | 320 | 3.4 |
| 2 | 거기 둘 중 70대한테 더 맞는 곳은? | SUCCESS | NORMAL | visible | 548 | 345 | 277 | 2.8 |
| 3 | 정형외과는 검사 장비가 있다고 들었어요. | SUCCESS | NORMAL | visible | 809 | 282 | 127 | 2.3 |
| 4 | 한의원은 침 치료가 가능하대요. | SUCCESS | NORMAL | visible | 977 | 377 | 236 | 3.1 |
| 5 | 그 곳 보험 적용돼요? | SUCCESS | NORMAL | visible | 1211 | 466 | 313 | 3.7 |
| 6 | 어느 쪽이 먼저 진단받기에 좋아요? | SUCCESS | NORMAL | visible | 1298 | 369 | 331 | 3.2 |
| 7 | 통증이 오래됐으면 어디가 우선이에요? | SUCCESS | NORMAL | visible | 1426 | 477 | 269 | 3.9 |
| 8 | 걷기 힘든 날에는 대기 시간이 짧은 곳이 좋아요. | SUCCESS | NORMAL | visible | 1601 | 530 | 278 | 4.4 |
| 9 | 약을 많이 먹는 건 부담스러워요. | SUCCESS | NORMAL | visible | 1619 | 405 | 278 | 3.4 |
| 10 | 내 조건 중 나이와 무릎 통증을 포함해서 최종 정리해주세요. | SUCCESS | NORMAL | visible | 1713 | 719 | 288 | 6.3 |

### MTN-MT-104 (multiturn / topic_switch_return)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 회의록 정리하는 법 알려줘. | SUCCESS | NORMAL | visible | 259 | 427 | 427 | 3.2 |
| 2 | 가장 효과적인 방법은? | SUCCESS | NORMAL | visible | 576 | 373 | 279 | 2.7 |
| 3 | 회의 참석자가 8명 정도일 때 기준으로 알려줘. | SUCCESS | NORMAL | visible | 836 | 380 | 261 | 2.9 |
| 4 | 결정사항과 액션아이템을 분리하고 싶어. | SUCCESS | NORMAL | visible | 1091 | 667 | 433 | 5.9 |
| 5 | 잠깐, 다른 거 물어봐도 돼? 노션이랑 옵시디언 차이가 뭐야? | THINK_RUNAWAY | NORMAL | visible | 1428 | 974 | 1177 | 7.6 |
| 6 | 둘 중 회의록에 더 적합한 건? | SUCCESS | NORMAL | visible | 1576 | 211 | 130 | 1.7 |
| 7 | 가격은 어떻게 돼? | SUCCESS | NORMAL | visible | 1586 | 148 | 132 | 1.3 |
| 8 | 회사 공유용이면 어떤 도구가 나아? | SUCCESS | NORMAL | visible | 1601 | 574 | 543 | 4.7 |
| 9 | 개인 지식관리용이면 어떤 도구가 좋아? | SUCCESS | NORMAL | visible | 1744 | 289 | 117 | 2.3 |
| 10 | 최종적으로 회의록 정리 프로세스만 5단계로 출력해줘. | SUCCESS | NORMAL | visible | 1531 | 387 | 347 | 3.2 |

### MTN-MT-105 (multiturn / constraint_accumulation)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국 정착할 때 신청해야 하는 지원금 알려주세요. | SUCCESS | NORMAL | visible | 265 | 427 | 314 | 3.5 |
| 2 | 정확히 3가지만. | SUCCESS | NORMAL | visible | 531 | 175 | 24 | 1.5 |
| 3 | 각 항목 옆에 신청 기관도 같이. | SUCCESS | NORMAL | visible | 590 | 127 | 123 | 1.1 |
| 4 | 각 항목 30자 이내로 짧게. | SUCCESS | NORMAL | visible | 749 | 85 | 49 | 0.9 |
| 5 | 마지막은 새터민이 가장 먼저 알아야 할 순서로 정렬해주세요. | SUCCESS | NORMAL | visible | 844 | 163 | 77 | 1.5 |
| 6 | 온라인 신청이 필요한지 여부도 표시해주세요. | SUCCESS | NORMAL | visible | 789 | 336 | 68 | 2.7 |
| 7 | 컴퓨터가 약한 사람 기준으로 쉬운 순서를 원해요. | SUCCESS | NORMAL | visible | 878 | 104 | 49 | 1.0 |
| 8 | 전화 문의가 가능한지도 적어주세요. | SUCCESS | NORMAL | visible | 892 | 413 | 84 | 3.7 |
| 9 | 금액은 확실하지 않으면 쓰지 마세요. | SUCCESS | NORMAL | visible | 975 | 71 | 21 | 0.6 |
| 10 | 마지막에 추가 설명은 쓰지 마세요. | ITEM_COUNT_MISMATCH(expected=3,got=0) | NORMAL | visible | 974 | 209 | 84 | 1.9 |

### FRN-MT-101 (foreigner_lang / beginner_restaurant)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국어 잘 못해요. 천천히 쉽게 말해주세요. | SUCCESS | NORMAL | visible | 275 | 460 | 232 | 4.0 |
| 2 | 식당에서 주문하고 싶어요. 어떻게 말해요? | SUCCESS | NORMAL | visible | 504 | 173 | 107 | 1.6 |
| 3 | "이거 주세요" 무엇이에요? | SUCCESS | NORMAL | visible | 651 | 271 | 241 | 2.6 |
| 4 | 매운 거 싫어요. 어떻게 말해요? | VOCAB_MISMATCH(long_sentences=2) | NORMAL | visible | 890 | 58 | 114 | 0.7 |
| 5 | 물 주세요는 어떻게 말해요? | VOCAB_MISMATCH(long_sentences=4) | RUNAWAY | visible | 1042 | 3736 | 308 | 35.1 |
| 6 | 계산하고 싶을 때 뭐라고 해요? | REPETITION_LOOP | RUNAWAY | visible | 1178 | 3734 | 1955 | 34.3 |
| 7 | 고기 안 먹어요. 쉬운 말로 알려주세요. | REPETITION_LOOP | RUNAWAY | visible | 1474 | 3831 | 2118 | 35.1 |
| 8 | 혼자 먹어도 돼요? 어떻게 물어요? | REPETITION_LOOP | RUNAWAY | visible | 1709 | 3851 | 7701 | 34.7 |
| 9 | 포장하고 싶어요. 짧게 말해주세요. | REPETITION_LOOP | RUNAWAY | visible | 2004 | 3709 | 7418 | 34.9 |
| 10 | 지금까지 얘기 다시. 짧게. 쉬운 단어만. | VOCAB_MISMATCH(long_sentences=7) | NORMAL | visible | 2101 | 3449 | 516 | 35.0 |

### FRN-MT-102 (foreigner_lang / code_switching)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. I'm learning Korean. | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 276 | 311 | 237 | 2.7 |
| 2 | "처마" 무슨 뜻이에요? Is it about the roof? | VOCAB_MISMATCH(no_english_terms) | RUNAWAY | visible | 516 | 4199 | 265 | 34.2 |
| 3 | 한옥 설명해주세요. 어려우면 영어 단어 쓰셔도 돼요. | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 782 | 232 | 216 | 1.9 |
| 4 | 기와는 영어로 roof tile 맞아요? | SUCCESS | NORMAL | visible | 1017 | 304 | 202 | 2.5 |
| 5 | 마루는 floor랑 같아요? | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 1238 | 236 | 112 | 2.0 |
| 6 | 온돌은 heating system이라고 보면 돼요? | REPETITION_LOOP | RUNAWAY | visible | 1253 | 4184 | 3055 | 34.7 |
| 7 | 한옥 보러 가고 싶어요. 어디 가요? | VOCAB_MISMATCH(no_english_terms) | RUNAWAY | visible | 1469 | 4183 | 234 | 34.3 |
| 8 | 서울에서 가기 쉬운 곳이면 좋아요. | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 1574 | 400 | 310 | 3.3 |
| 9 | 입장료 비싸요? | REPETITION_LOOP | RUNAWAY | visible | 1617 | 4165 | 4164 | 34.3 |
| 10 | 위 내용 다시 정리. Korean first, then English s… | REPETITION_LOOP | RUNAWAY | visible | 1923 | 4183 | 1603 | 34.4 |

### FRN-MT-103 (foreigner_lang / english_to_korean_teaching)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | Hi! Can you help me practice Korean? | VOCAB_MISMATCH(no_romanization;not_trilingual) | NORMAL | visible | 281 | 344 | 129 | 2.7 |
| 2 | I want to order food in Korean. Teach me… | SUCCESS | NORMAL | visible | 464 | 320 | 344 | 3.1 |
| 3 | How do I say "no spicy please"? | SUCCESS | RUNAWAY | visible | 780 | 4004 | 284 | 33.6 |
| 4 | 한국어로 다시 말해주세요. 천천히. | SUCCESS | RUNAWAY | visible | 1048 | 4177 | 324 | 33.9 |
| 5 | 발음도 알려줘요. 로마자로요. | SUCCESS | RUNAWAY | visible | 1329 | 4200 | 285 | 34.7 |
| 6 | "감사합니다" 발음도 알려주세요. | REPETITION_LOOP | RUNAWAY | visible | 1500 | 3847 | 2934 | 34.2 |
| 7 | Can you include English meaning every ti… | SUCCESS | RUNAWAY | visible | 1672 | 4202 | 498 | 34.9 |
| 8 | I need Korean, romanization, and English… | VOCAB_MISMATCH(no_romanization;not_trilingual) | NORMAL | visible | 1898 | 317 | 126 | 2.6 |
| 9 | How do I say "water please"? | REPETITION_LOOP | RUNAWAY | visible | 1806 | 4394 | 8787 | 34.4 |
| 10 | 마지막에 가장 중요한 표현 2개만 다시 골라주세요. | SUCCESS | RUNAWAY | visible | 1906 | 4178 | 410 | 34.8 |

### FRN-MT-104 (foreigner_lang / avoid_hanja_hospital)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국어 공부해요. 한자어 어려워요. 병원 갈 때 쉬운 말로 알려주세요. | SUCCESS | NORMAL | visible | 282 | 291 | 155 | 2.7 |
| 2 | "감기" 같은 단어 말고 다른 쉬운 말로 증상 설명하는 법. | SUCCESS | NORMAL | visible | 485 | 236 | 158 | 2.1 |
| 3 | 머리가 아파요를 더 쉬운 말로도 알려주세요. | SUCCESS | RUNAWAY | visible | 693 | 3699 | 372 | 34.1 |
| 4 | 배가 아플 때 말하는 문장 알려주세요. | REPETITION_LOOP | RUNAWAY | visible | 1003 | 3685 | 7370 | 34.2 |
| 5 | 열이 나는 것 같아요를 쉬운 말로요. | REPETITION_LOOP | RUNAWAY | visible | 1374 | 3717 | 3993 | 34.3 |
| 6 | 목이 따가워요는 어떻게 말해요? | REPETITION_LOOP | RUNAWAY | visible | 1637 | 4252 | 8504 | 34.9 |
| 7 | 기침이 나와요는 쉬운가요? | REPETITION_LOOP | RUNAWAY | visible | 1899 | 4260 | 8519 | 35.2 |
| 8 | 병원에서 접수하는 법 쉽게 알려주세요. | REPETITION_LOOP | RUNAWAY | visible | 2060 | 4275 | 8549 | 34.7 |
| 9 | 이름을 말할 때 문장 알려주세요. | REPETITION_LOOP | RUNAWAY | visible | 2052 | 4259 | 8518 | 35.2 |
| 10 | 병원에서 처음부터 끝까지 말할 순서만 알려주세요. | REPETITION_LOOP | RUNAWAY | visible | 2049 | 4266 | 8532 | 34.8 |

### FRN-MT-105 (foreigner_lang / register_shift)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국어 책으로 공부했어요. 너무 formal해요. | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 276 | 357 | 163 | 2.9 |
| 2 | 친구한테 쓸 말 알려주세요. 평어/반말로요. | SUCCESS | NORMAL | visible | 470 | 188 | 78 | 1.8 |
| 3 | "안녕하세요" → 친구한테는 어떻게 말해요? "감사합니다"는요? | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 589 | 3369 | 581 | 33.9 |
| 4 | 카페에서 음료 주문할 때 일상적인 말투로. | REPETITION_LOOP | NORMAL | visible | 969 | 3443 | 2755 | 34.2 |
| 5 | 친구에게 밥 먹자고 말하는 표현 알려줘. | REPETITION_LOOP | RUNAWAY | visible | 1343 | 4082 | 8164 | 34.3 |
| 6 | 미안해를 자연스럽게 말하는 방법은? | REPETITION_LOOP | RUNAWAY | visible | 1613 | 4085 | 8170 | 34.5 |
| 7 | 괜찮습니다 말고 편한 말로 바꿔줘. | REPETITION_LOOP | RUNAWAY | visible | 1928 | 4079 | 8157 | 34.5 |
| 8 | 잘 지내세요 말고 친구한테 쓰는 말은? | REPETITION_LOOP | RUNAWAY | visible | 2022 | 4086 | 8171 | 35.2 |
| 9 | 너무 무례하지 않은 반말이면 좋겠어. | REPETITION_LOOP | RUNAWAY | visible | 2123 | 4082 | 8164 | 35.3 |
| 10 | 마지막에는 반말 표현만 번호로 정리해줘. | REPETITION_LOOP | RUNAWAY | visible | 2121 | 4084 | 8167 | 35.1 |

### REC-MT-101 (recommendation / multicultural_museum)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국 박물관 가보고 싶어요. 어디가 좋을까요? | SUCCESS | NORMAL | visible | 280 | 490 | 405 | 3.9 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | RUNAWAY | visible | 598 | 4100 | 497 | 34.5 |
| 3 | 한국어는 일상 회화 정도예요. | SUCCESS | NORMAL | visible | 967 | 230 | 458 | 1.7 |
| 4 | 한국 역사 잘 몰라요. | SUCCESS | NORMAL | visible | 1311 | 206 | 410 | 1.6 |
| 5 | 그림이나 도자기 좋아해요. | REPETITION_LOOP | RUNAWAY | visible | 1631 | 4196 | 4196 | 34.7 |
| 6 | 8살 딸이랑 같이 가요. | SUCCESS | RUNAWAY | visible | 1771 | 4303 | 469 | 35.0 |
| 7 | 너무 길거나 어려운 곳 말고요. | SUCCESS | NORMAL | visible | 1852 | 224 | 446 | 1.8 |
| 8 | 대중교통으로 가기 쉬운 곳이면 좋겠어요. | SUCCESS | RUNAWAY | visible | 1950 | 4346 | 212 | 34.6 |
| 9 | 아이에게 설명하기 쉬운 전시가 필요해요. | SUCCESS | RUNAWAY | visible | 1854 | 4343 | 312 | 34.3 |
| 10 | 위 정보 다 반영해서 박물관 3곳 추천 + 각각 이유. | THINK_RUNAWAY | RUNAWAY | visible | 1768 | 4380 | 1168 | 34.6 |

### REC-MT-102 (recommendation / defector_settlement_program)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국 정착 프로그램 추천해주세요. | SUCCESS | NORMAL | visible | 276 | 311 | 225 | 2.0 |
| 2 | 50대 여자, 평양 출신이에요. 작년에 한국 왔어요. | SUCCESS | NORMAL | visible | 504 | 256 | 177 | 1.9 |
| 3 | 혼자 살고 있어요. | SUCCESS | NORMAL | visible | 713 | 432 | 485 | 3.3 |
| 4 | 장사 해보고 싶어요. 컴퓨터는 약해요. | SUCCESS | NORMAL | visible | 1069 | 628 | 475 | 4.6 |
| 5 | 서울에 살아요. | SUCCESS | NORMAL | visible | 1421 | 761 | 307 | 5.7 |
| 6 | 너무 빨리 진행되는 건 따라가기 힘들어요. | SUCCESS | NORMAL | visible | 1560 | 720 | 522 | 5.4 |
| 7 | 온라인 신청보다 방문 상담이 편해요. | SUCCESS | NORMAL | visible | 1821 | 724 | 522 | 5.4 |
| 8 | 창업 전에 기초 교육부터 받고 싶어요. | THINK_RUNAWAY | RUNAWAY | visible | 1939 | 4490 | 821 | 35.1 |
| 9 | 소상공인이라는 말도 아직 어려워요. | THINK_RUNAWAY | RUNAWAY | visible | 1953 | 4652 | 841 | 35.4 |
| 10 | 위 조건 다 반영해서 정착 지원 프로그램 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=50대,장사,서울) | RUNAWAY | visible | 2058 | 4519 | 549 | 35.3 |

### REC-MT-103 (recommendation / elderly_culture_event)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 우리 동네 문화행사 추천 좀 해주세요. | SUCCESS | REPETITION_LOOP | visible | 278 | 410 | 353 | 3.2 |
| 2 | 75살이에요. 무릎이 안 좋아요. | SUCCESS | NORMAL | visible | 564 | 609 | 747 | 5.1 |
| 3 | 큰 글씨, 큰 화면이면 좋아요. | SUCCESS | NORMAL | visible | 933 | 299 | 403 | 2.5 |
| 4 | 가곡이나 옛날 노래 좋아해요. | SUCCESS | NORMAL | visible | 1252 | 3193 | 389 | 34.2 |
| 5 | 친구 사귈 수 있는 곳이면 더 좋고요. | THINK_RUNAWAY | RUNAWAY | visible | 1565 | 4281 | 1211 | 34.3 |
| 6 | 오래 서 있는 행사는 어렵습니다. | SUCCESS | NORMAL | visible | 1741 | 742 | 688 | 6.1 |
| 7 | 버스로 갈 수 있는 곳이 좋아요. | SUCCESS | NORMAL | visible | 1842 | 509 | 652 | 4.2 |
| 8 | 계단이 적은 장소를 원해요. | SUCCESS | NORMAL | visible | 1990 | 495 | 414 | 3.8 |
| 9 | 오후 시간이 편합니다. | SUCCESS | NORMAL | visible | 1999 | 507 | 513 | 4.1 |
| 10 | 위 조건 다 반영해서 행사 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=가곡) | RUNAWAY | visible | 1998 | 4191 | 362 | 34.8 |

### REC-MT-104 (recommendation / office_worker_fitness_diet)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 운동 루틴이랑 식단 추천해줘. | SUCCESS | NORMAL | visible | 275 | 333 | 286 | 2.6 |
| 2 | 32살 사무직, 허리가 자주 아파. | SUCCESS | REPETITION_LOOP | visible | 527 | 785 | 555 | 6.6 |
| 3 | 집에서 할 수 있는 거 위주. | THINK_RUNAWAY | NORMAL | visible | 896 | 880 | 1153 | 7.3 |
| 4 | 평일 저녁 30분. | THINK_RUNAWAY | NORMAL | visible | 1260 | 773 | 878 | 6.8 |
| 5 | 요리 잘 못해. | THINK_RUNAWAY | RUNAWAY | visible | 1620 | 3948 | 1095 | 34.0 |
| 6 | 키 175에 몸무게 82kg이야. | SUCCESS | RUNAWAY | visible | 1823 | 4385 | 308 | 34.9 |
| 7 | 헬스장은 당분간 안 갈 생각이야. | REPETITION_LOOP | RUNAWAY | visible | 1828 | 4409 | 1706 | 35.2 |
| 8 | 요가매트는 있어. | SUCCESS | RUNAWAY | visible | 1925 | 4451 | 414 | 34.7 |
| 9 | 허리에 부담 가는 윗몸일으키기는 싫어. | SUCCESS | RUNAWAY | visible | 1984 | 4173 | 389 | 35.0 |
| 10 | 위 정보로 1주 운동 + 식단 표로 추천해줘. | RECOMMENDATION_GENERIC(missing=30분) | NORMAL | visible | 1940 | 3195 | 479 | 34.7 |

### REC-MT-105 (recommendation / student_learning_resource)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 학습 자료 추천해줘. | SUCCESS | NORMAL | visible | 273 | 376 | 294 | 2.9 |
| 2 | 정보 부족하면 먼저 질문해줘. | CLARIFY_SKIPPED(no_question_or_dumped_list) | NORMAL | visible | 524 | 242 | 293 | 1.8 |
| 3 | 컴퓨터공학 전공 3학년이야. | SUCCESS | NORMAL | visible | 788 | 489 | 668 | 4.0 |
| 4 | 머신러닝 기초 공부하고 싶어. | SUCCESS | NORMAL | visible | 1155 | 616 | 623 | 4.2 |
| 5 | 한국어 자료가 더 편해. 영어도 가능은 함. | SUCCESS | NORMAL | visible | 1526 | 315 | 296 | 2.3 |
| 6 | 책보단 무료 강의가 좋아. | SUCCESS | NORMAL | visible | 1632 | 372 | 294 | 2.9 |
| 7 | 수학 백그라운드는 미적분/선형대수 학부 수준. | SUCCESS | NORMAL | visible | 1736 | 610 | 500 | 4.5 |
| 8 | 파이썬은 기본 문법 정도 알아. | SUCCESS | NORMAL | visible | 1842 | 714 | 697 | 4.8 |
| 9 | 딥러닝보다 머신러닝 개념부터 하고 싶어. | REPETITION_LOOP | RUNAWAY | visible | 1848 | 4995 | 4995 | 34.6 |
| 10 | 위 정보로 학습 자료 3개 추천 + 각각 이유. | RECOMMENDATION_GENERIC(missing=3학년) | RUNAWAY | visible | 1955 | 4866 | 581 | 34.5 |
