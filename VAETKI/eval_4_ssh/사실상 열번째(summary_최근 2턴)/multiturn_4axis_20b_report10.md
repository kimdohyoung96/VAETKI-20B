# 평가 결과

## 1. 전체 요약

- 세션 수: 20
- 총 turn: 200
- 성공 turn: 147 (73.5%)
- 성공 latency 중앙값: 3.5s
- 실패 latency 중앙값: 34.1s

## 1-1. Summary Memory / Recent-Turn 진단

- prompt token 중앙값: 1061
- prompt token 최대값: 1614
- memory token 중앙값: 424
- memory token 최대값: 795
- reply token 중앙값: 489
- reply token 최대값: 9394
- clean source 분포: visible=200
- debug status 분포: NORMAL=147, RUNAWAY=44, REPETITION_LOOP=9

## 2. 트랙별 성공률

| 트랙 | 성공/전체 | 성공률 |
|---|---|---|
| persona | 39/50 | 78.0% |
| multiturn | 47/50 | 94.0% |
| foreigner_lang | 17/50 | 34.0% |
| recommendation | 44/50 | 88.0% |

## 3. 실패 유형 분포

### 3.1 일반 실패

| 유형 | 개수 |
|---|---|
| REPETITION_LOOP | 23 |
| THINK_RUNAWAY | 7 |

### 3.2 4축 특화 실패 (generic=SUCCESS이지만 트랙 기준 미충족)

| 유형 | 개수 |
|---|---|
| VOCAB_MISMATCH | 14 |
| PERSONA_RECALL_FAIL | 4 |
| RECOMMENDATION_GENERIC | 3 |
| CONTEXT_LOSS | 1 |
| ITEM_COUNT_MISMATCH | 1 |

## 4. 세션별 turn 결과

### PER-MT-101 (persona / multicultural_museum)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 박물관 가이드 도움 받고 싶어요. | SUCCESS | NORMAL | visible | 283 | 133 | 109 | 1.7 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | NORMAL | visible | 427 | 334 | 208 | 2.8 |
| 3 | 한국어는 일상 회화 정도만 가능해요. | SUCCESS | NORMAL | visible | 654 | 254 | 131 | 2.0 |
| 4 | 한국 역사 잘 몰라요. 조선시대 이런 거 들어본 적 없어요. | SUCCESS | NORMAL | visible | 756 | 262 | 221 | 2.2 |
| 5 | 그림이나 도자기 같은 거 보는 거 좋아해요. | SUCCESS | NORMAL | visible | 872 | 464 | 590 | 3.6 |
| 6 | 8살 딸이랑 같이 가요. 짧게 보고 싶어요. | SUCCESS | NORMAL | visible | 1161 | 519 | 621 | 4.0 |
| 7 | 딸은 오래 걷는 걸 싫어해서 이동이 적었으면 해요. | SUCCESS | NORMAL | visible | 1402 | 519 | 615 | 4.2 |
| 8 | 저는 쉬운 한국어 설명이 있으면 좋아요. | SUCCESS | NORMAL | visible | 1508 | 477 | 601 | 3.7 |
| 9 | 영어 안내가 있으면 도움은 되지만 꼭 필요하진 않아요. | SUCCESS | NORMAL | visible | 1614 | 323 | 493 | 2.5 |
| 10 | 위 정보를 모두 반영해서 저와 딸의 관람 페르소나를 한 단락으로 정리해주… | PERSONA_RECALL_FAIL(missing=베트남,2년,일상 회화,조선) | NORMAL | visible | 1542 | 393 | 275 | 3.4 |

### PER-MT-102 (persona / defector_settlement)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 도움 받고 싶어서요. | SUCCESS | NORMAL | visible | 279 | 205 | 81 | 1.6 |
| 2 | 작년에 한국 왔어요. 50대 여자입니다. | SUCCESS | NORMAL | visible | 392 | 279 | 158 | 2.2 |
| 3 | 혼자 살고 있어요. 평양 출신이에요. | SUCCESS | NORMAL | visible | 591 | 341 | 154 | 2.7 |
| 4 | 장사 좀 해보고 싶은데 한국 시스템을 잘 몰라요. 컴퓨터도 약해요. | SUCCESS | NORMAL | visible | 736 | 731 | 668 | 5.9 |
| 5 | 스마트폰은 전화랑 문자 정도만 익숙해요. | SUCCESS | NORMAL | visible | 1018 | 471 | 426 | 4.0 |
| 6 | 온라인 신청이라는 말이 나오면 긴장이 돼요. | SUCCESS | NORMAL | visible | 1257 | 539 | 514 | 4.5 |
| 7 | 가게를 바로 크게 시작할 생각은 없어요. | SUCCESS | RUNAWAY | visible | 1353 | 4084 | 444 | 34.7 |
| 8 | 먼저 배워보고 천천히 준비하고 싶어요. | REPETITION_LOOP | RUNAWAY | visible | 1466 | 4453 | 1500 | 34.4 |
| 9 | 서울에 살지만 동네 밖으로 멀리 가는 건 부담돼요. | THINK_RUNAWAY | NORMAL | visible | 1571 | 994 | 1235 | 7.8 |
| 10 | 위 정보로 제 상황을 한 단락 페르소나로 정리해주세요. | PERSONA_RECALL_FAIL(missing=컴퓨터) | NORMAL | visible | 1546 | 617 | 183 | 5.2 |

### PER-MT-103 (persona / elderly_culture)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 우리 동네 문화센터 어떻게 다닐지 좀 알려줘요. | SUCCESS | NORMAL | visible | 287 | 265 | 315 | 2.1 |
| 2 | 75살이고 무릎이 안 좋아서 멀리는 못 다녀요. | SUCCESS | REPETITION_LOOP | visible | 565 | 571 | 642 | 4.8 |
| 3 | 글씨 작은 건 잘 안 보여요. 큰 글씨로 부탁해요. | SUCCESS | NORMAL | visible | 944 | 508 | 500 | 4.1 |
| 4 | 옛날에 노래 부르는 거 좋아했어요. 가곡 같은 거. | SUCCESS | NORMAL | visible | 1140 | 549 | 538 | 4.7 |
| 5 | 친구 사귀고 싶어요. 혼자 너무 적적해요. | SUCCESS | NORMAL | visible | 1244 | 453 | 496 | 3.7 |
| 6 | 계단이 많은 곳은 피하고 싶어요. | SUCCESS | NORMAL | visible | 1340 | 449 | 542 | 3.9 |
| 7 | 버스로 한 번에 갈 수 있으면 좋겠어요. | THINK_RUNAWAY | RUNAWAY | visible | 1438 | 9394 | 917 | 34.5 |
| 8 | 오전보다는 오후 시간이 편해요. | REPETITION_LOOP | RUNAWAY | visible | 1541 | 5695 | 5447 | 34.5 |
| 9 | 수업 시간이 너무 길면 힘들어요. | REPETITION_LOOP | RUNAWAY | visible | 1532 | 5840 | 2314 | 34.4 |
| 10 | 위 정보로 제 문화센터 이용 페르소나를 정리해주세요. | REPETITION_LOOP | RUNAWAY | visible | 1532 | 3989 | 3246 | 34.6 |

### PER-MT-104 (persona / office_worker_fitness)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 운동 좀 시작하려고. | SUCCESS | NORMAL | visible | 276 | 430 | 432 | 3.3 |
| 2 | 32살 직장인이고 사무실에서 하루 종일 앉아 있어. | SUCCESS | NORMAL | visible | 603 | 448 | 427 | 3.9 |
| 3 | 키 175, 몸무게 82kg. | SUCCESS | NORMAL | visible | 940 | 521 | 519 | 4.4 |
| 4 | 허리가 자주 아파. | SUCCESS | NORMAL | visible | 1073 | 538 | 507 | 4.5 |
| 5 | 헬스장은 부담스럽고 집에서 할 수 있는 거 좋아. | SUCCESS | NORMAL | visible | 1206 | 349 | 500 | 3.0 |
| 6 | 시간은 평일 저녁 30분 정도밖에 못 내. | SUCCESS | NORMAL | visible | 1315 | 427 | 303 | 3.5 |
| 7 | 식단도 신경 쓰고 싶은데 요리는 잘 못해. | SUCCESS | NORMAL | visible | 1327 | 507 | 598 | 4.5 |
| 8 | 아침은 자주 거르고 점심은 회사 근처에서 먹어. | SUCCESS | NORMAL | visible | 1430 | 375 | 351 | 3.3 |
| 9 | 퇴근하면 피곤해서 강도 높은 운동은 자신 없어. | SUCCESS | NORMAL | visible | 1462 | 444 | 412 | 3.7 |
| 10 | 위 정보 다 종합해서 내 운동 페르소나를 한 단락으로 정리해줘. | PERSONA_RECALL_FAIL(missing=32,집,30분) | NORMAL | visible | 1423 | 532 | 201 | 4.3 |

### PER-MT-105 (persona / parent_kid_education)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 우리 아이 학습 도움 받고 싶어요. | SUCCESS | NORMAL | visible | 280 | 470 | 521 | 3.7 |
| 2 | 초등학교 3학년 딸이에요. | SUCCESS | NORMAL | visible | 637 | 409 | 487 | 3.3 |
| 3 | 수학을 어려워해요. 특히 분수 부분. | THINK_RUNAWAY | NORMAL | visible | 999 | 702 | 831 | 5.9 |
| 4 | 책 읽는 건 좋아하는데 혼자만 하려고 해요. | SUCCESS | NORMAL | visible | 1103 | 571 | 571 | 5.1 |
| 5 | 문제집을 오래 붙잡고 있으면 금방 지쳐요. | SUCCESS | NORMAL | visible | 1218 | 495 | 637 | 4.1 |
| 6 | 그림이 있는 설명은 잘 보는 편이에요. | SUCCESS | RUNAWAY | visible | 1322 | 4301 | 588 | 34.8 |
| 7 | 말로 설명하면 중간에 딴생각을 해요. | SUCCESS | RUNAWAY | visible | 1423 | 4435 | 420 | 34.6 |
| 8 | 분모와 분자를 자꾸 헷갈려요. | SUCCESS | RUNAWAY | visible | 1481 | 4431 | 442 | 35.2 |
| 9 | 학교 숙제는 미루다가 밤에 하는 편이에요. | SUCCESS | RUNAWAY | visible | 1452 | 4424 | 473 | 34.5 |
| 10 | 위 정보로 우리 아이 학습 페르소나를 정리해주세요. | PERSONA_RECALL_FAIL(missing=초등,3학년) | NORMAL | visible | 1487 | 223 | 109 | 1.9 |

### MTN-MT-101 (multiturn / intent_repair)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 저녁 메뉴 추천해줘. | SUCCESS | REPETITION_LOOP | visible | 257 | 413 | 458 | 3.4 |
| 2 | 한식 말고. | SUCCESS | RUNAWAY | visible | 580 | 3772 | 250 | 33.7 |
| 3 | 아 미안, 한식도 괜찮아. 단 너무 매운 건 빼고. | SUCCESS | NORMAL | visible | 824 | 233 | 462 | 1.9 |
| 4 | 고기는 가능하지만 튀김은 싫어. | SUCCESS | NORMAL | visible | 941 | 246 | 74 | 1.9 |
| 5 | 조리 시간은 20분 안쪽이면 좋겠어. | SUCCESS | NORMAL | visible | 917 | 278 | 89 | 2.4 |
| 6 | 집에 계란이랑 두부가 있어. | SUCCESS | NORMAL | visible | 791 | 217 | 61 | 1.9 |
| 7 | 밥은 이미 해놨어. | SUCCESS | NORMAL | visible | 831 | 209 | 52 | 1.8 |
| 8 | 국물 요리는 오늘은 별로야. | SUCCESS | NORMAL | visible | 853 | 145 | 75 | 1.2 |
| 9 | 냉장고에 애호박도 조금 있어. | SUCCESS | NORMAL | visible | 917 | 112 | 53 | 1.0 |
| 10 | 최종 저녁 메뉴와 이유를 짧게 다시 말해줘. | CONTEXT_LOSS(missing=저녁) | NORMAL | visible | 971 | 267 | 53 | 2.3 |

### MTN-MT-102 (multiturn / tone_shift)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 한국 여행 정보 부탁드립니다. | SUCCESS | REPETITION_LOOP | visible | 263 | 483 | 446 | 3.9 |
| 2 | 정중하게 안내해주세요. 저는 외국인이에요. | SUCCESS | NORMAL | visible | 600 | 55 | 107 | 0.5 |
| 3 | 경주 추천 받고 싶어요. | SUCCESS | NORMAL | visible | 746 | 517 | 405 | 4.1 |
| 4 | 역사 설명은 너무 어렵지 않게 부탁드립니다. | SUCCESS | NORMAL | visible | 825 | 287 | 405 | 2.3 |
| 5 | 하루 일정으로만 보고 싶습니다. | SUCCESS | NORMAL | visible | 1074 | 385 | 272 | 3.3 |
| 6 | 이제 친구처럼 편하게 말해줘. 반말로. | SUCCESS | NORMAL | visible | 1111 | 247 | 159 | 2.2 |
| 7 | 거기서 뭘 봐야 돼? | SUCCESS | NORMAL | visible | 1077 | 213 | 153 | 2.0 |
| 8 | 밥 먹을 곳도 하나 넣어줘. | SUCCESS | RUNAWAY | visible | 1112 | 4339 | 618 | 34.0 |
| 9 | 걷는 시간이 너무 길면 힘들어. | SUCCESS | NORMAL | visible | 1383 | 526 | 728 | 4.4 |
| 10 | 처음부터 지금까지 말투가 몇 번 바뀌었는지도 알려 주세요. | REPETITION_LOOP | RUNAWAY | visible | 1564 | 3878 | 4323 | 35.1 |

### MTN-MT-103 (multiturn / reference_tracking)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 무릎 통증 때문에 병원 두 곳 알아봤어요. 정형외과랑 한의원. | SUCCESS | REPETITION_LOOP | visible | 269 | 417 | 72 | 3.6 |
| 2 | 거기 둘 중 70대한테 더 맞는 곳은? | SUCCESS | NORMAL | visible | 380 | 207 | 171 | 1.7 |
| 3 | 정형외과는 검사 장비가 있다고 들었어요. | SUCCESS | NORMAL | visible | 588 | 201 | 104 | 1.7 |
| 4 | 한의원은 침 치료가 가능하대요. | SUCCESS | NORMAL | visible | 671 | 159 | 307 | 1.4 |
| 5 | 그 곳 보험 적용돼요? | SUCCESS | NORMAL | visible | 835 | 295 | 335 | 2.4 |
| 6 | 어느 쪽이 먼저 진단받기에 좋아요? | SUCCESS | NORMAL | visible | 1047 | 440 | 316 | 3.8 |
| 7 | 통증이 오래됐으면 어디가 우선이에요? | SUCCESS | NORMAL | visible | 1154 | 336 | 335 | 2.8 |
| 8 | 걷기 힘든 날에는 대기 시간이 짧은 곳이 좋아요. | SUCCESS | NORMAL | visible | 1264 | 408 | 401 | 3.4 |
| 9 | 약을 많이 먹는 건 부담스러워요. | SUCCESS | NORMAL | visible | 1411 | 374 | 335 | 3.0 |
| 10 | 내 조건 중 나이와 무릎 통증을 포함해서 최종 정리해주세요. | SUCCESS | NORMAL | visible | 1453 | 346 | 335 | 2.8 |

### MTN-MT-104 (multiturn / topic_switch_return)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 회의록 정리하는 법 알려줘. | SUCCESS | NORMAL | visible | 259 | 372 | 194 | 2.9 |
| 2 | 가장 효과적인 방법은? | SUCCESS | NORMAL | visible | 460 | 56 | 109 | 0.5 |
| 3 | 회의 참석자가 8명 정도일 때 기준으로 알려줘. | SUCCESS | NORMAL | visible | 610 | 316 | 192 | 2.6 |
| 4 | 결정사항과 액션아이템을 분리하고 싶어. | SUCCESS | NORMAL | visible | 718 | 413 | 221 | 3.4 |
| 5 | 잠깐, 다른 거 물어봐도 돼? 노션이랑 옵시디언 차이가 뭐야? | SUCCESS | NORMAL | visible | 887 | 580 | 795 | 4.5 |
| 6 | 둘 중 회의록에 더 적합한 건? | SUCCESS | NORMAL | visible | 1146 | 175 | 136 | 1.4 |
| 7 | 가격은 어떻게 돼? | SUCCESS | NORMAL | visible | 1186 | 161 | 107 | 1.4 |
| 8 | 회사 공유용이면 어떤 도구가 나아? | SUCCESS | NORMAL | visible | 1053 | 147 | 141 | 1.2 |
| 9 | 개인 지식관리용이면 어떤 도구가 좋아? | SUCCESS | NORMAL | visible | 1149 | 59 | 116 | 0.5 |
| 10 | 최종적으로 회의록 정리 프로세스만 5단계로 출력해줘. | SUCCESS | NORMAL | visible | 1144 | 241 | 138 | 2.0 |

### MTN-MT-105 (multiturn / constraint_accumulation)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국 정착할 때 신청해야 하는 지원금 알려주세요. | SUCCESS | NORMAL | visible | 265 | 433 | 327 | 3.5 |
| 2 | 정확히 3가지만. | SUCCESS | NORMAL | visible | 538 | 280 | 102 | 2.4 |
| 3 | 각 항목 옆에 신청 기관도 같이. | SUCCESS | NORMAL | visible | 671 | 307 | 140 | 2.7 |
| 4 | 각 항목 30자 이내로 짧게. | SUCCESS | NORMAL | visible | 663 | 262 | 140 | 2.4 |
| 5 | 마지막은 새터민이 가장 먼저 알아야 할 순서로 정렬해주세요. | SUCCESS | NORMAL | visible | 786 | 272 | 140 | 2.4 |
| 6 | 온라인 신청이 필요한지 여부도 표시해주세요. | SUCCESS | NORMAL | visible | 888 | 294 | 182 | 2.6 |
| 7 | 컴퓨터가 약한 사람 기준으로 쉬운 순서를 원해요. | SUCCESS | NORMAL | visible | 1018 | 220 | 88 | 1.8 |
| 8 | 전화 문의가 가능한지도 적어주세요. | SUCCESS | RUNAWAY | visible | 1055 | 4187 | 731 | 33.7 |
| 9 | 금액은 확실하지 않으면 쓰지 마세요. | SUCCESS | NORMAL | visible | 1313 | 224 | 88 | 1.8 |
| 10 | 마지막에 추가 설명은 쓰지 마세요. | ITEM_COUNT_MISMATCH(expected=3,got=0) | NORMAL | visible | 1375 | 275 | 88 | 2.3 |

### FRN-MT-101 (foreigner_lang / beginner_restaurant)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국어 잘 못해요. 천천히 쉽게 말해주세요. | SUCCESS | NORMAL | visible | 275 | 366 | 225 | 3.0 |
| 2 | 식당에서 주문하고 싶어요. 어떻게 말해요? | VOCAB_MISMATCH(long_sentences=2) | NORMAL | visible | 500 | 274 | 187 | 2.5 |
| 3 | "이거 주세요" 무엇이에요? | REPETITION_LOOP | NORMAL | visible | 714 | 2942 | 5882 | 34.3 |
| 4 | 매운 거 싫어요. 어떻게 말해요? | VOCAB_MISMATCH(long_sentences=2) | NORMAL | visible | 950 | 2707 | 169 | 33.9 |
| 5 | 물 주세요는 어떻게 말해요? | REPETITION_LOOP | NORMAL | visible | 1038 | 2940 | 5880 | 34.9 |
| 6 | 계산하고 싶을 때 뭐라고 해요? | REPETITION_LOOP | NORMAL | visible | 1138 | 3194 | 6388 | 34.4 |
| 7 | 고기 안 먹어요. 쉬운 말로 알려주세요. | REPETITION_LOOP | NORMAL | visible | 1406 | 3085 | 6170 | 35.1 |
| 8 | 혼자 먹어도 돼요? 어떻게 물어요? | REPETITION_LOOP | NORMAL | visible | 1511 | 2653 | 5305 | 34.1 |
| 9 | 포장하고 싶어요. 짧게 말해주세요. | REPETITION_LOOP | NORMAL | visible | 1509 | 2650 | 5299 | 34.8 |
| 10 | 지금까지 얘기 다시. 짧게. 쉬운 단어만. | REPETITION_LOOP | NORMAL | visible | 1509 | 2526 | 5052 | 34.7 |

### FRN-MT-102 (foreigner_lang / code_switching)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. I'm learning Korean. | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 276 | 265 | 72 | 2.1 |
| 2 | "처마" 무슨 뜻이에요? Is it about the roof? | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 391 | 234 | 152 | 1.9 |
| 3 | 한옥 설명해주세요. 어려우면 영어 단어 쓰셔도 돼요. | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 596 | 232 | 103 | 1.9 |
| 4 | 기와는 영어로 roof tile 맞아요? | SUCCESS | NORMAL | visible | 687 | 148 | 114 | 1.1 |
| 5 | 마루는 floor랑 같아요? | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 738 | 259 | 183 | 2.0 |
| 6 | 온돌은 heating system이라고 보면 돼요? | SUCCESS | NORMAL | visible | 877 | 241 | 212 | 1.9 |
| 7 | 한옥 보러 가고 싶어요. 어디 가요? | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 1031 | 284 | 278 | 2.2 |
| 8 | 서울에서 가기 쉬운 곳이면 좋아요. | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 1183 | 311 | 230 | 2.4 |
| 9 | 입장료 비싸요? | VOCAB_MISMATCH(no_english_terms) | RUNAWAY | visible | 1283 | 4203 | 312 | 33.9 |
| 10 | 위 내용 다시 정리. Korean first, then English s… | SUCCESS | NORMAL | visible | 1348 | 700 | 497 | 4.4 |

### FRN-MT-103 (foreigner_lang / english_to_korean_teaching)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | Hi! Can you help me practice Korean? | VOCAB_MISMATCH(no_romanization;not_trilingual) | NORMAL | visible | 281 | 341 | 396 | 2.7 |
| 2 | I want to order food in Korean. Teach me… | VOCAB_MISMATCH(no_romanization;not_trilingual) | NORMAL | visible | 616 | 3483 | 472 | 33.8 |
| 3 | How do I say "no spicy please"? | REPETITION_LOOP | RUNAWAY | visible | 996 | 5911 | 11817 | 34.0 |
| 4 | 한국어로 다시 말해주세요. 천천히. | SUCCESS | NORMAL | visible | 1147 | 3448 | 515 | 34.1 |
| 5 | 발음도 알려줘요. 로마자로요. | SUCCESS | NORMAL | visible | 1243 | 347 | 502 | 3.1 |
| 6 | "감사합니다" 발음도 알려주세요. | VOCAB_MISMATCH(no_romanization;not_trilingual) | NORMAL | visible | 1337 | 299 | 479 | 2.8 |
| 7 | Can you include English meaning every ti… | SUCCESS | NORMAL | visible | 1439 | 781 | 552 | 7.0 |
| 8 | I need Korean, romanization, and English… | SUCCESS | NORMAL | visible | 1565 | 880 | 358 | 3.5 |
| 9 | How do I say "water please"? | SUCCESS | NORMAL | visible | 1510 | 1167 | 226 | 5.1 |
| 10 | 마지막에 가장 중요한 표현 2개만 다시 골라주세요. | SUCCESS | NORMAL | visible | 1352 | 325 | 203 | 2.4 |

### FRN-MT-104 (foreigner_lang / avoid_hanja_hospital)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국어 공부해요. 한자어 어려워요. 병원 갈 때 쉬운 말로 알려주세요. | SUCCESS | NORMAL | visible | 282 | 3279 | 211 | 33.9 |
| 2 | "감기" 같은 단어 말고 다른 쉬운 말로 증상 설명하는 법. | SUCCESS | NORMAL | visible | 515 | 330 | 228 | 3.2 |
| 3 | 머리가 아파요를 더 쉬운 말로도 알려주세요. | SUCCESS | RUNAWAY | visible | 759 | 3596 | 352 | 34.0 |
| 4 | 배가 아플 때 말하는 문장 알려주세요. | REPETITION_LOOP | RUNAWAY | visible | 924 | 3517 | 7033 | 33.9 |
| 5 | 열이 나는 것 같아요를 쉬운 말로요. | REPETITION_LOOP | RUNAWAY | visible | 1157 | 3503 | 3436 | 34.8 |
| 6 | 목이 따가워요는 어떻게 말해요? | REPETITION_LOOP | RUNAWAY | visible | 1329 | 3797 | 7594 | 34.3 |
| 7 | 기침이 나와요는 쉬운가요? | REPETITION_LOOP | RUNAWAY | visible | 1426 | 3800 | 7600 | 34.4 |
| 8 | 병원에서 접수하는 법 쉽게 알려주세요. | REPETITION_LOOP | RUNAWAY | visible | 1526 | 3808 | 7615 | 34.8 |
| 9 | 이름을 말할 때 문장 알려주세요. | THINK_RUNAWAY | RUNAWAY | visible | 1517 | 3996 | 802 | 34.7 |
| 10 | 병원에서 처음부터 끝까지 말할 순서만 알려주세요. | REPETITION_LOOP | RUNAWAY | visible | 1516 | 3808 | 7616 | 34.4 |

### FRN-MT-105 (foreigner_lang / register_shift)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국어 책으로 공부했어요. 너무 formal해요. | SUCCESS | NORMAL | visible | 276 | 420 | 441 | 3.7 |
| 2 | 친구한테 쓸 말 알려주세요. 평어/반말로요. | SUCCESS | NORMAL | visible | 613 | 243 | 93 | 2.0 |
| 3 | "안녕하세요" → 친구한테는 어떻게 말해요? "감사합니다"는요? | SUCCESS | NORMAL | visible | 743 | 302 | 95 | 2.7 |
| 4 | 카페에서 음료 주문할 때 일상적인 말투로. | SUCCESS | NORMAL | visible | 646 | 298 | 13 | 2.6 |
| 5 | 친구에게 밥 먹자고 말하는 표현 알려줘. | REPETITION_LOOP | NORMAL | visible | 642 | 2915 | 5827 | 33.6 |
| 6 | 미안해를 자연스럽게 말하는 방법은? | REPETITION_LOOP | NORMAL | visible | 939 | 3152 | 6304 | 33.8 |
| 7 | 괜찮습니다 말고 편한 말로 바꿔줘. | REPETITION_LOOP | NORMAL | visible | 1282 | 2828 | 5655 | 34.2 |
| 8 | 잘 지내세요 말고 친구한테 쓰는 말은? | REPETITION_LOOP | NORMAL | visible | 1383 | 3389 | 6778 | 34.5 |
| 9 | 너무 무례하지 않은 반말이면 좋겠어. | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 1486 | 3120 | 365 | 34.9 |
| 10 | 마지막에는 반말 표현만 번호로 정리해줘. | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 1522 | 3270 | 401 | 34.4 |

### REC-MT-101 (recommendation / multicultural_museum)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국 박물관 가보고 싶어요. 어디가 좋을까요? | SUCCESS | NORMAL | visible | 280 | 266 | 196 | 2.1 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | RUNAWAY | visible | 493 | 4082 | 509 | 33.5 |
| 3 | 한국어는 일상 회화 정도예요. | SUCCESS | RUNAWAY | visible | 864 | 4370 | 246 | 34.3 |
| 4 | 한국 역사 잘 몰라요. | SUCCESS | RUNAWAY | visible | 982 | 4641 | 314 | 33.7 |
| 5 | 그림이나 도자기 좋아해요. | SUCCESS | RUNAWAY | visible | 982 | 4635 | 454 | 34.5 |
| 6 | 8살 딸이랑 같이 가요. | SUCCESS | RUNAWAY | visible | 1184 | 4177 | 412 | 34.6 |
| 7 | 너무 길거나 어려운 곳 말고요. | SUCCESS | RUNAWAY | visible | 1334 | 4358 | 467 | 35.0 |
| 8 | 대중교통으로 가기 쉬운 곳이면 좋겠어요. | SUCCESS | RUNAWAY | visible | 1444 | 4343 | 340 | 34.6 |
| 9 | 아이에게 설명하기 쉬운 전시가 필요해요. | SUCCESS | RUNAWAY | visible | 1411 | 4468 | 326 | 34.3 |
| 10 | 위 정보 다 반영해서 박물관 3곳 추천 + 각각 이유. | RECOMMENDATION_GENERIC(missing=베트남,도자기) | RUNAWAY | visible | 1346 | 4330 | 462 | 34.6 |

### REC-MT-102 (recommendation / defector_settlement_program)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국 정착 프로그램 추천해주세요. | SUCCESS | NORMAL | visible | 276 | 309 | 181 | 2.0 |
| 2 | 50대 여자, 평양 출신이에요. 작년에 한국 왔어요. | SUCCESS | NORMAL | visible | 482 | 446 | 394 | 3.4 |
| 3 | 혼자 살고 있어요. | SUCCESS | NORMAL | visible | 799 | 334 | 399 | 2.5 |
| 4 | 장사 해보고 싶어요. 컴퓨터는 약해요. | SUCCESS | NORMAL | visible | 1007 | 567 | 601 | 4.3 |
| 5 | 서울에 살아요. | SUCCESS | RUNAWAY | visible | 1151 | 4260 | 461 | 33.9 |
| 6 | 너무 빨리 진행되는 건 따라가기 힘들어요. | SUCCESS | NORMAL | visible | 1284 | 337 | 56 | 2.9 |
| 7 | 온라인 신청보다 방문 상담이 편해요. | SUCCESS | RUNAWAY | visible | 1113 | 4336 | 646 | 34.4 |
| 8 | 창업 전에 기초 교육부터 받고 싶어요. | THINK_RUNAWAY | RUNAWAY | visible | 1241 | 4540 | 868 | 34.0 |
| 9 | 소상공인이라는 말도 아직 어려워요. | THINK_RUNAWAY | RUNAWAY | visible | 1563 | 4277 | 1359 | 34.5 |
| 10 | 위 조건 다 반영해서 정착 지원 프로그램 3개 추천 + 이유. | SUCCESS | NORMAL | visible | 1571 | 885 | 704 | 6.8 |

### REC-MT-103 (recommendation / elderly_culture_event)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 우리 동네 문화행사 추천 좀 해주세요. | SUCCESS | REPETITION_LOOP | visible | 278 | 433 | 365 | 3.4 |
| 2 | 75살이에요. 무릎이 안 좋아요. | SUCCESS | REPETITION_LOOP | visible | 571 | 665 | 779 | 5.7 |
| 3 | 큰 글씨, 큰 화면이면 좋아요. | SUCCESS | NORMAL | visible | 940 | 161 | 310 | 1.3 |
| 4 | 가곡이나 옛날 노래 좋아해요. | SUCCESS | RUNAWAY | visible | 1011 | 4257 | 421 | 34.2 |
| 5 | 친구 사귈 수 있는 곳이면 더 좋고요. | SUCCESS | RUNAWAY | visible | 1072 | 4166 | 238 | 34.4 |
| 6 | 오래 서 있는 행사는 어렵습니다. | SUCCESS | NORMAL | visible | 1139 | 602 | 797 | 4.7 |
| 7 | 버스로 갈 수 있는 곳이 좋아요. | SUCCESS | RUNAWAY | visible | 1280 | 4295 | 269 | 34.4 |
| 8 | 계단이 적은 장소를 원해요. | THINK_RUNAWAY | RUNAWAY | visible | 1393 | 4183 | 1174 | 34.4 |
| 9 | 오후 시간이 편합니다. | SUCCESS | RUNAWAY | visible | 1387 | 4244 | 193 | 34.6 |
| 10 | 위 조건 다 반영해서 행사 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=75) | NORMAL | visible | 1350 | 570 | 605 | 4.7 |

### REC-MT-104 (recommendation / office_worker_fitness_diet)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 운동 루틴이랑 식단 추천해줘. | SUCCESS | RUNAWAY | visible | 275 | 4287 | 680 | 33.9 |
| 2 | 32살 사무직, 허리가 자주 아파. | SUCCESS | REPETITION_LOOP | visible | 634 | 726 | 377 | 6.1 |
| 3 | 집에서 할 수 있는 거 위주. | SUCCESS | NORMAL | visible | 940 | 763 | 376 | 6.2 |
| 4 | 평일 저녁 30분. | SUCCESS | REPETITION_LOOP | visible | 975 | 908 | 376 | 8.3 |
| 5 | 요리 잘 못해. | SUCCESS | NORMAL | visible | 1067 | 410 | 375 | 3.5 |
| 6 | 키 175에 몸무게 82kg이야. | SUCCESS | NORMAL | visible | 1164 | 769 | 375 | 6.3 |
| 7 | 헬스장은 당분간 안 갈 생각이야. | SUCCESS | NORMAL | visible | 1269 | 938 | 429 | 7.6 |
| 8 | 요가매트는 있어. | SUCCESS | NORMAL | visible | 1397 | 1024 | 483 | 8.7 |
| 9 | 허리에 부담 가는 윗몸일으키기는 싫어. | SUCCESS | NORMAL | visible | 1549 | 894 | 517 | 7.8 |
| 10 | 위 정보로 1주 운동 + 식단 표로 추천해줘. | RECOMMENDATION_GENERIC(missing=집,30분) | RUNAWAY | visible | 1590 | 3726 | 669 | 34.7 |

### REC-MT-105 (recommendation / student_learning_resource)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 학습 자료 추천해줘. | SUCCESS | REPETITION_LOOP | visible | 273 | 201 | 118 | 1.5 |
| 2 | 정보 부족하면 먼저 질문해줘. | SUCCESS | NORMAL | visible | 416 | 133 | 118 | 1.0 |
| 3 | 컴퓨터공학 전공 3학년이야. | SUCCESS | NORMAL | visible | 571 | 528 | 683 | 4.6 |
| 4 | 머신러닝 기초 공부하고 싶어. | SUCCESS | NORMAL | visible | 864 | 813 | 290 | 6.0 |
| 5 | 한국어 자료가 더 편해. 영어도 가능은 함. | SUCCESS | NORMAL | visible | 1052 | 470 | 612 | 4.0 |
| 6 | 책보단 무료 강의가 좋아. | SUCCESS | NORMAL | visible | 1156 | 529 | 269 | 4.5 |
| 7 | 수학 백그라운드는 미적분/선형대수 학부 수준. | SUCCESS | NORMAL | visible | 1248 | 351 | 315 | 2.9 |
| 8 | 파이썬은 기본 문법 정도 알아. | SUCCESS | NORMAL | visible | 1256 | 425 | 418 | 3.5 |
| 9 | 딥러닝보다 머신러닝 개념부터 하고 싶어. | SUCCESS | NORMAL | visible | 1436 | 324 | 418 | 2.7 |
| 10 | 위 정보로 학습 자료 3개 추천 + 각각 이유. | SUCCESS | NORMAL | visible | 1514 | 732 | 418 | 6.2 |
