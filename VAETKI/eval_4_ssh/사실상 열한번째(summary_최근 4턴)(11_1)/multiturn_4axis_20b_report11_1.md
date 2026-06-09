# 4축 평가 결과 (think 모드)

## 1. 전체 요약

- 세션 수: 20
- 총 turn: 200
- 성공 turn: 150 (75.0%)
- 성공 latency 중앙값: 3.4s
- 실패 latency 중앙값: 6.5s

## 1-1. Summary Memory / Recent-Turn 진단

- prompt token 중앙값: 1259
- prompt token 최대값: 2136
- memory token 중앙값: 406
- memory token 최대값: 799
- reply token 중앙값: 449
- reply token 최대값: 9322
- clean source 분포: visible=200
- debug status 분포: NORMAL=165, RUNAWAY=30, REPETITION_LOOP=5

## 2. 트랙별 성공률

| 트랙 | 성공/전체 | 성공률 |
|---|---|---|
| persona | 40/50 | 80.0% |
| multiturn | 46/50 | 92.0% |
| foreigner_lang | 27/50 | 54.0% |
| recommendation | 37/50 | 74.0% |

## 3. 실패 유형 분포

### 3.1 일반 실패

| 유형 | 개수 |
|---|---|
| THINK_RUNAWAY | 14 |
| REPETITION_LOOP | 7 |

### 3.2 4축 특화 실패 (generic=SUCCESS이지만 트랙 기준 미충족)

| 유형 | 개수 |
|---|---|
| VOCAB_MISMATCH | 20 |
| PERSONA_RECALL_FAIL | 5 |
| RECOMMENDATION_GENERIC | 3 |
| ITEM_COUNT_MISMATCH | 1 |

## 4. 세션별 turn 결과

### PER-MT-101 (persona / multicultural_museum)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 박물관 가이드 도움 받고 싶어요. | SUCCESS | NORMAL | visible | 283 | 224 | 103 | 2.3 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | NORMAL | visible | 421 | 269 | 193 | 2.2 |
| 3 | 한국어는 일상 회화 정도만 가능해요. | SUCCESS | NORMAL | visible | 641 | 227 | 129 | 1.8 |
| 4 | 한국 역사 잘 몰라요. 조선시대 이런 거 들어본 적 없어요. | SUCCESS | NORMAL | visible | 818 | 243 | 186 | 2.0 |
| 5 | 그림이나 도자기 같은 거 보는 거 좋아해요. | SUCCESS | NORMAL | visible | 1040 | 491 | 515 | 4.1 |
| 6 | 8살 딸이랑 같이 가요. 짧게 보고 싶어요. | SUCCESS | NORMAL | visible | 1342 | 707 | 472 | 6.0 |
| 7 | 딸은 오래 걷는 걸 싫어해서 이동이 적었으면 해요. | SUCCESS | NORMAL | visible | 1587 | 509 | 353 | 4.5 |
| 8 | 저는 쉬운 한국어 설명이 있으면 좋아요. | SUCCESS | NORMAL | visible | 1805 | 416 | 352 | 3.5 |
| 9 | 영어 안내가 있으면 도움은 되지만 꼭 필요하진 않아요. | SUCCESS | NORMAL | visible | 1990 | 259 | 205 | 2.2 |
| 10 | 위 정보를 모두 반영해서 저와 딸의 관람 페르소나를 한 단락으로 정리해주… | PERSONA_RECALL_FAIL(missing=베트남,2년,일상 회화,조선) | NORMAL | visible | 1777 | 481 | 289 | 4.0 |

### PER-MT-102 (persona / defector_settlement)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 도움 받고 싶어서요. | SUCCESS | NORMAL | visible | 279 | 301 | 79 | 2.4 |
| 2 | 작년에 한국 왔어요. 50대 여자입니다. | SUCCESS | NORMAL | visible | 389 | 147 | 78 | 1.3 |
| 3 | 혼자 살고 있어요. 평양 출신이에요. | SUCCESS | NORMAL | visible | 509 | 383 | 78 | 3.0 |
| 4 | 장사 좀 해보고 싶은데 한국 시스템을 잘 몰라요. 컴퓨터도 약해요. | REPETITION_LOOP | RUNAWAY | visible | 637 | 9322 | 2710 | 34.0 |
| 5 | 스마트폰은 전화랑 문자 정도만 익숙해요. | SUCCESS | RUNAWAY | visible | 1018 | 4566 | 480 | 34.0 |
| 6 | 온라인 신청이라는 말이 나오면 긴장이 돼요. | SUCCESS | RUNAWAY | visible | 1325 | 4372 | 389 | 34.7 |
| 7 | 가게를 바로 크게 시작할 생각은 없어요. | SUCCESS | RUNAWAY | visible | 1584 | 4539 | 413 | 34.3 |
| 8 | 먼저 배워보고 천천히 준비하고 싶어요. | SUCCESS | RUNAWAY | visible | 1855 | 4533 | 723 | 34.7 |
| 9 | 서울에 살지만 동네 밖으로 멀리 가는 건 부담돼요. | SUCCESS | RUNAWAY | visible | 1953 | 4548 | 412 | 34.8 |
| 10 | 위 정보로 제 상황을 한 단락 페르소나로 정리해주세요. | PERSONA_RECALL_FAIL(missing=50대) | RUNAWAY | visible | 1969 | 4548 | 564 | 34.8 |

### PER-MT-103 (persona / elderly_culture)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 우리 동네 문화센터 어떻게 다닐지 좀 알려줘요. | SUCCESS | NORMAL | visible | 287 | 271 | 329 | 2.2 |
| 2 | 75살이고 무릎이 안 좋아서 멀리는 못 다녀요. | SUCCESS | REPETITION_LOOP | visible | 572 | 374 | 364 | 3.2 |
| 3 | 글씨 작은 건 잘 안 보여요. 큰 글씨로 부탁해요. | SUCCESS | NORMAL | visible | 883 | 323 | 364 | 2.7 |
| 4 | 옛날에 노래 부르는 거 좋아했어요. 가곡 같은 거. | SUCCESS | NORMAL | visible | 1194 | 317 | 159 | 2.6 |
| 5 | 친구 사귀고 싶어요. 혼자 너무 적적해요. | SUCCESS | NORMAL | visible | 1400 | 482 | 398 | 4.0 |
| 6 | 계단이 많은 곳은 피하고 싶어요. | SUCCESS | NORMAL | visible | 1531 | 383 | 509 | 3.2 |
| 7 | 버스로 한 번에 갈 수 있으면 좋겠어요. | SUCCESS | NORMAL | visible | 1698 | 615 | 405 | 5.1 |
| 8 | 오전보다는 오후 시간이 편해요. | THINK_RUNAWAY | RUNAWAY | visible | 1816 | 4148 | 1316 | 34.3 |
| 9 | 수업 시간이 너무 길면 힘들어요. | SUCCESS | NORMAL | visible | 1973 | 423 | 358 | 3.3 |
| 10 | 위 정보로 제 문화센터 이용 페르소나를 정리해주세요. | PERSONA_RECALL_FAIL(missing=가곡,혼자) | NORMAL | visible | 1951 | 450 | 405 | 3.9 |

### PER-MT-104 (persona / office_worker_fitness)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 운동 좀 시작하려고. | SUCCESS | NORMAL | visible | 276 | 380 | 247 | 3.2 |
| 2 | 32살 직장인이고 사무실에서 하루 종일 앉아 있어. | SUCCESS | NORMAL | visible | 507 | 369 | 311 | 3.0 |
| 3 | 키 175, 몸무게 82kg. | SUCCESS | NORMAL | visible | 785 | 407 | 398 | 3.2 |
| 4 | 허리가 자주 아파. | SUCCESS | NORMAL | visible | 1099 | 553 | 433 | 4.5 |
| 5 | 헬스장은 부담스럽고 집에서 할 수 있는 거 좋아. | THINK_RUNAWAY | NORMAL | visible | 1435 | 750 | 910 | 6.5 |
| 6 | 시간은 평일 저녁 30분 정도밖에 못 내. | SUCCESS | RUNAWAY | visible | 1676 | 4352 | 735 | 34.8 |
| 7 | 식단도 신경 쓰고 싶은데 요리는 잘 못해. | THINK_RUNAWAY | NORMAL | visible | 1872 | 730 | 903 | 6.4 |
| 8 | 아침은 자주 거르고 점심은 회사 근처에서 먹어. | SUCCESS | NORMAL | visible | 2031 | 617 | 661 | 5.1 |
| 9 | 퇴근하면 피곤해서 강도 높은 운동은 자신 없어. | SUCCESS | NORMAL | visible | 2081 | 963 | 474 | 7.7 |
| 10 | 위 정보 다 종합해서 내 운동 페르소나를 한 단락으로 정리해줘. | PERSONA_RECALL_FAIL(missing=32,허리,집,30분) | NORMAL | visible | 2071 | 925 | 263 | 7.8 |

### PER-MT-105 (persona / parent_kid_education)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 우리 아이 학습 도움 받고 싶어요. | SUCCESS | NORMAL | visible | 280 | 233 | 61 | 1.8 |
| 2 | 초등학교 3학년 딸이에요. | SUCCESS | NORMAL | visible | 369 | 118 | 234 | 1.1 |
| 3 | 수학을 어려워해요. 특히 분수 부분. | SUCCESS | NORMAL | visible | 603 | 468 | 582 | 3.7 |
| 4 | 책 읽는 건 좋아하는데 혼자만 하려고 해요. | SUCCESS | NORMAL | visible | 976 | 415 | 373 | 3.4 |
| 5 | 문제집을 오래 붙잡고 있으면 금방 지쳐요. | SUCCESS | NORMAL | visible | 1287 | 561 | 535 | 4.6 |
| 6 | 그림이 있는 설명은 잘 보는 편이에요. | SUCCESS | NORMAL | visible | 1610 | 628 | 453 | 5.2 |
| 7 | 말로 설명하면 중간에 딴생각을 해요. | SUCCESS | NORMAL | visible | 1827 | 355 | 361 | 2.8 |
| 8 | 분모와 분자를 자꾸 헷갈려요. | REPETITION_LOOP | RUNAWAY | visible | 1857 | 4093 | 7969 | 34.9 |
| 9 | 학교 숙제는 미루다가 밤에 하는 편이에요. | SUCCESS | NORMAL | visible | 2021 | 513 | 498 | 4.3 |
| 10 | 위 정보로 우리 아이 학습 페르소나를 정리해주세요. | PERSONA_RECALL_FAIL(missing=분수) | NORMAL | visible | 1975 | 514 | 367 | 4.1 |

### MTN-MT-101 (multiturn / intent_repair)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 저녁 메뉴 추천해줘. | SUCCESS | REPETITION_LOOP | visible | 257 | 336 | 365 | 2.8 |
| 2 | 한식 말고. | SUCCESS | NORMAL | visible | 539 | 310 | 277 | 2.6 |
| 3 | 아 미안, 한식도 괜찮아. 단 너무 매운 건 빼고. | SUCCESS | NORMAL | visible | 796 | 274 | 28 | 2.3 |
| 4 | 고기는 가능하지만 튀김은 싫어. | SUCCESS | NORMAL | visible | 868 | 351 | 182 | 3.1 |
| 5 | 조리 시간은 20분 안쪽이면 좋겠어. | SUCCESS | NORMAL | visible | 1078 | 115 | 228 | 1.1 |
| 6 | 집에 계란이랑 두부가 있어. | SUCCESS | NORMAL | visible | 1114 | 239 | 153 | 2.0 |
| 7 | 밥은 이미 해놨어. | SUCCESS | NORMAL | visible | 1150 | 61 | 119 | 0.6 |
| 8 | 국물 요리는 오늘은 별로야. | SUCCESS | NORMAL | visible | 1265 | 201 | 181 | 1.6 |
| 9 | 냉장고에 애호박도 조금 있어. | SUCCESS | NORMAL | visible | 1364 | 216 | 198 | 2.0 |
| 10 | 최종 저녁 메뉴와 이유를 짧게 다시 말해줘. | SUCCESS | NORMAL | visible | 1354 | 244 | 190 | 2.1 |

### MTN-MT-102 (multiturn / tone_shift)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 한국 여행 정보 부탁드립니다. | SUCCESS | REPETITION_LOOP | visible | 263 | 462 | 560 | 3.8 |
| 2 | 정중하게 안내해주세요. 저는 외국인이에요. | SUCCESS | NORMAL | visible | 627 | 528 | 499 | 4.4 |
| 3 | 경주 추천 받고 싶어요. | SUCCESS | NORMAL | visible | 995 | 359 | 284 | 3.0 |
| 4 | 역사 설명은 너무 어렵지 않게 부탁드립니다. | SUCCESS | NORMAL | visible | 1257 | 299 | 284 | 2.4 |
| 5 | 하루 일정으로만 보고 싶습니다. | SUCCESS | NORMAL | visible | 1520 | 584 | 619 | 5.1 |
| 6 | 이제 친구처럼 편하게 말해줘. 반말로. | SUCCESS | NORMAL | visible | 1620 | 600 | 733 | 5.4 |
| 7 | 거기서 뭘 봐야 돼? | THINK_RUNAWAY | NORMAL | visible | 1717 | 659 | 868 | 5.8 |
| 8 | 밥 먹을 곳도 하나 넣어줘. | THINK_RUNAWAY | NORMAL | visible | 1923 | 706 | 868 | 6.5 |
| 9 | 걷는 시간이 너무 길면 힘들어. | SUCCESS | NORMAL | visible | 2023 | 740 | 723 | 6.5 |
| 10 | 처음부터 지금까지 말투가 몇 번 바뀌었는지도 알려 주세요. | SUCCESS | NORMAL | visible | 2028 | 396 | 523 | 3.4 |

### MTN-MT-103 (multiturn / reference_tracking)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 무릎 통증 때문에 병원 두 곳 알아봤어요. 정형외과랑 한의원. | SUCCESS | REPETITION_LOOP | visible | 269 | 355 | 192 | 2.8 |
| 2 | 거기 둘 중 70대한테 더 맞는 곳은? | SUCCESS | NORMAL | visible | 484 | 316 | 222 | 2.6 |
| 3 | 정형외과는 검사 장비가 있다고 들었어요. | SUCCESS | NORMAL | visible | 717 | 274 | 84 | 2.2 |
| 4 | 한의원은 침 치료가 가능하대요. | SUCCESS | NORMAL | visible | 842 | 77 | 151 | 0.7 |
| 5 | 그 곳 보험 적용돼요? | SUCCESS | NORMAL | visible | 1029 | 318 | 107 | 2.5 |
| 6 | 어느 쪽이 먼저 진단받기에 좋아요? | SUCCESS | NORMAL | visible | 1051 | 348 | 222 | 2.8 |
| 7 | 통증이 오래됐으면 어디가 우선이에요? | SUCCESS | NORMAL | visible | 1151 | 320 | 222 | 2.7 |
| 8 | 걷기 힘든 날에는 대기 시간이 짧은 곳이 좋아요. | SUCCESS | RUNAWAY | visible | 1324 | 4044 | 596 | 34.3 |
| 9 | 약을 많이 먹는 건 부담스러워요. | SUCCESS | NORMAL | visible | 1605 | 222 | 442 | 1.8 |
| 10 | 내 조건 중 나이와 무릎 통증을 포함해서 최종 정리해주세요. | REPETITION_LOOP | RUNAWAY | visible | 1775 | 3861 | 1755 | 34.6 |

### MTN-MT-104 (multiturn / topic_switch_return)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 회의록 정리하는 법 알려줘. | SUCCESS | NORMAL | visible | 259 | 376 | 307 | 2.7 |
| 2 | 가장 효과적인 방법은? | SUCCESS | RUNAWAY | visible | 517 | 4132 | 799 | 33.6 |
| 3 | 회의 참석자가 8명 정도일 때 기준으로 알려줘. | SUCCESS | NORMAL | visible | 888 | 330 | 147 | 2.6 |
| 4 | 결정사항과 액션아이템을 분리하고 싶어. | SUCCESS | NORMAL | visible | 1080 | 259 | 517 | 2.0 |
| 5 | 잠깐, 다른 거 물어봐도 돼? 노션이랑 옵시디언 차이가 뭐야? | SUCCESS | NORMAL | visible | 1458 | 589 | 621 | 4.8 |
| 6 | 둘 중 회의록에 더 적합한 건? | SUCCESS | NORMAL | visible | 1665 | 273 | 232 | 2.2 |
| 7 | 가격은 어떻게 돼? | SUCCESS | NORMAL | visible | 1631 | 237 | 217 | 2.1 |
| 8 | 회사 공유용이면 어떤 도구가 나아? | SUCCESS | NORMAL | visible | 1759 | 106 | 211 | 0.9 |
| 9 | 개인 지식관리용이면 어떤 도구가 좋아? | SUCCESS | NORMAL | visible | 1616 | 219 | 169 | 1.9 |
| 10 | 최종적으로 회의록 정리 프로세스만 5단계로 출력해줘. | SUCCESS | NORMAL | visible | 1453 | 482 | 473 | 3.7 |

### MTN-MT-105 (multiturn / constraint_accumulation)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국 정착할 때 신청해야 하는 지원금 알려주세요. | SUCCESS | NORMAL | visible | 265 | 587 | 532 | 4.6 |
| 2 | 정확히 3가지만. | SUCCESS | NORMAL | visible | 624 | 216 | 71 | 1.9 |
| 3 | 각 항목 옆에 신청 기관도 같이. | SUCCESS | NORMAL | visible | 726 | 404 | 240 | 3.5 |
| 4 | 각 항목 30자 이내로 짧게. | SUCCESS | RUNAWAY | visible | 965 | 3505 | 348 | 33.9 |
| 5 | 마지막은 새터민이 가장 먼저 알아야 할 순서로 정렬해주세요. | SUCCESS | NORMAL | visible | 1262 | 578 | 240 | 5.3 |
| 6 | 온라인 신청이 필요한지 여부도 표시해주세요. | SUCCESS | NORMAL | visible | 1240 | 555 | 387 | 4.5 |
| 7 | 컴퓨터가 약한 사람 기준으로 쉬운 순서를 원해요. | SUCCESS | RUNAWAY | visible | 1513 | 3643 | 356 | 35.0 |
| 8 | 전화 문의가 가능한지도 적어주세요. | SUCCESS | RUNAWAY | visible | 1677 | 4000 | 504 | 34.9 |
| 9 | 금액은 확실하지 않으면 쓰지 마세요. | SUCCESS | RUNAWAY | visible | 1859 | 3958 | 551 | 34.9 |
| 10 | 마지막에 추가 설명은 쓰지 마세요. | ITEM_COUNT_MISMATCH(expected=3,got=0) | NORMAL | visible | 1978 | 424 | 387 | 3.5 |

### FRN-MT-101 (foreigner_lang / beginner_restaurant)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국어 잘 못해요. 천천히 쉽게 말해주세요. | SUCCESS | NORMAL | visible | 275 | 253 | 167 | 2.1 |
| 2 | 식당에서 주문하고 싶어요. 어떻게 말해요? | SUCCESS | NORMAL | visible | 472 | 227 | 137 | 2.0 |
| 3 | "이거 주세요" 무엇이에요? | SUCCESS | NORMAL | visible | 650 | 304 | 222 | 2.8 |
| 4 | 매운 거 싫어요. 어떻게 말해요? | SUCCESS | NORMAL | visible | 878 | 310 | 210 | 2.8 |
| 5 | 물 주세요는 어떻게 말해요? | THINK_RUNAWAY | NORMAL | visible | 1101 | 2996 | 5637 | 33.7 |
| 6 | 계산하고 싶을 때 뭐라고 해요? | SUCCESS | NORMAL | visible | 1364 | 3056 | 482 | 34.1 |
| 7 | 고기 안 먹어요. 쉬운 말로 알려주세요. | SUCCESS | NORMAL | visible | 1635 | 3058 | 490 | 34.8 |
| 8 | 혼자 먹어도 돼요? 어떻게 물어요? | SUCCESS | NORMAL | visible | 1867 | 430 | 508 | 4.8 |
| 9 | 포장하고 싶어요. 짧게 말해주세요. | SUCCESS | NORMAL | visible | 2114 | 3056 | 428 | 35.5 |
| 10 | 지금까지 얘기 다시. 짧게. 쉬운 단어만. | SUCCESS | NORMAL | visible | 2079 | 448 | 231 | 4.1 |

### FRN-MT-102 (foreigner_lang / code_switching)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. I'm learning Korean. | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 276 | 200 | 149 | 1.6 |
| 2 | "처마" 무슨 뜻이에요? Is it about the roof? | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 465 | 203 | 133 | 1.6 |
| 3 | 한옥 설명해주세요. 어려우면 영어 단어 쓰셔도 돼요. | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 651 | 264 | 136 | 2.1 |
| 4 | 기와는 영어로 roof tile 맞아요? | SUCCESS | NORMAL | visible | 834 | 110 | 23 | 0.9 |
| 5 | 마루는 floor랑 같아요? | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 897 | 225 | 97 | 1.9 |
| 6 | 온돌은 heating system이라고 보면 돼요? | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 941 | 212 | 92 | 1.7 |
| 7 | 한옥 보러 가고 싶어요. 어디 가요? | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 985 | 269 | 132 | 2.3 |
| 8 | 서울에서 가기 쉬운 곳이면 좋아요. | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 1066 | 324 | 225 | 2.6 |
| 9 | 입장료 비싸요? | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 1261 | 253 | 120 | 2.1 |
| 10 | 위 내용 다시 정리. Korean first, then English s… | SUCCESS | RUNAWAY | visible | 1365 | 4264 | 545 | 34.4 |

### FRN-MT-103 (foreigner_lang / english_to_korean_teaching)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | Hi! Can you help me practice Korean? | VOCAB_MISMATCH(no_romanization;not_trilingual) | NORMAL | visible | 281 | 185 | 81 | 1.5 |
| 2 | I want to order food in Korean. Teach me… | VOCAB_MISMATCH(no_romanization;not_trilingual) | NORMAL | visible | 419 | 247 | 221 | 2.2 |
| 3 | How do I say "no spicy please"? | SUCCESS | NORMAL | visible | 673 | 233 | 158 | 1.8 |
| 4 | 한국어로 다시 말해주세요. 천천히. | SUCCESS | NORMAL | visible | 875 | 130 | 156 | 1.0 |
| 5 | 발음도 알려줘요. 로마자로요. | SUCCESS | NORMAL | visible | 1070 | 285 | 140 | 2.6 |
| 6 | "감사합니다" 발음도 알려주세요. | VOCAB_MISMATCH(not_trilingual) | NORMAL | visible | 1181 | 245 | 125 | 2.0 |
| 7 | Can you include English meaning every ti… | SUCCESS | NORMAL | visible | 1211 | 644 | 156 | 5.1 |
| 8 | I need Korean, romanization, and English… | SUCCESS | NORMAL | visible | 1328 | 424 | 228 | 3.4 |
| 9 | How do I say "water please"? | VOCAB_MISMATCH(not_trilingual) | NORMAL | visible | 1480 | 233 | 119 | 2.0 |
| 10 | 마지막에 가장 중요한 표현 2개만 다시 골라주세요. | SUCCESS | NORMAL | visible | 1371 | 225 | 220 | 1.9 |

### FRN-MT-104 (foreigner_lang / avoid_hanja_hospital)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국어 공부해요. 한자어 어려워요. 병원 갈 때 쉬운 말로 알려주세요. | REPETITION_LOOP | NORMAL | visible | 282 | 2827 | 1581 | 33.7 |
| 2 | "감기" 같은 단어 말고 다른 쉬운 말로 증상 설명하는 법. | SUCCESS | NORMAL | visible | 660 | 385 | 366 | 3.6 |
| 3 | 머리가 아파요를 더 쉬운 말로도 알려주세요. | SUCCESS | NORMAL | visible | 972 | 222 | 20 | 2.1 |
| 4 | 배가 아플 때 말하는 문장 알려주세요. | REPETITION_LOOP | NORMAL | visible | 1036 | 3186 | 6370 | 34.5 |
| 5 | 열이 나는 것 같아요를 쉬운 말로요. | SUCCESS | RUNAWAY | visible | 1407 | 3526 | 282 | 34.8 |
| 6 | 목이 따가워요는 어떻게 말해요? | SUCCESS | NORMAL | visible | 1389 | 3271 | 229 | 34.8 |
| 7 | 기침이 나와요는 쉬운가요? | SUCCESS | NORMAL | visible | 1412 | 3458 | 248 | 34.6 |
| 8 | 병원에서 접수하는 법 쉽게 알려주세요. | SUCCESS | NORMAL | visible | 1623 | 422 | 493 | 3.9 |
| 9 | 이름을 말할 때 문장 알려주세요. | SUCCESS | NORMAL | visible | 1712 | 3383 | 239 | 34.7 |
| 10 | 병원에서 처음부터 끝까지 말할 순서만 알려주세요. | SUCCESS | NORMAL | visible | 1684 | 406 | 362 | 3.5 |

### FRN-MT-105 (foreigner_lang / register_shift)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국어 책으로 공부했어요. 너무 formal해요. | SUCCESS | NORMAL | visible | 276 | 372 | 247 | 3.2 |
| 2 | 친구한테 쓸 말 알려주세요. 평어/반말로요. | SUCCESS | NORMAL | visible | 515 | 376 | 228 | 3.8 |
| 3 | "안녕하세요" → 친구한테는 어떻게 말해요? "감사합니다"는요? | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 736 | 363 | 22 | 3.5 |
| 4 | 카페에서 음료 주문할 때 일상적인 말투로. | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 808 | 277 | 80 | 2.3 |
| 5 | 친구에게 밥 먹자고 말하는 표현 알려줘. | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 932 | 2916 | 382 | 34.0 |
| 6 | 미안해를 자연스럽게 말하는 방법은? | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 1100 | 3216 | 133 | 34.7 |
| 7 | 괜찮습니다 말고 편한 말로 바꿔줘. | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 1162 | 3021 | 159 | 34.3 |
| 8 | 잘 지내세요 말고 친구한테 쓰는 말은? | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 1325 | 3488 | 312 | 34.4 |
| 9 | 너무 무례하지 않은 반말이면 좋겠어. | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 1542 | 2927 | 265 | 35.1 |
| 10 | 마지막에는 반말 표현만 번호로 정리해줘. | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 1480 | 2929 | 270 | 34.6 |

### REC-MT-101 (recommendation / multicultural_museum)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국 박물관 가보고 싶어요. 어디가 좋을까요? | SUCCESS | NORMAL | visible | 280 | 242 | 126 | 2.0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | NORMAL | visible | 441 | 653 | 622 | 5.3 |
| 3 | 한국어는 일상 회화 정도예요. | SUCCESS | NORMAL | visible | 812 | 319 | 126 | 2.6 |
| 4 | 한국 역사 잘 몰라요. | SUCCESS | NORMAL | visible | 974 | 545 | 126 | 4.6 |
| 5 | 그림이나 도자기 좋아해요. | SUCCESS | NORMAL | visible | 1134 | 331 | 109 | 2.6 |
| 6 | 8살 딸이랑 같이 가요. | SUCCESS | NORMAL | visible | 1193 | 526 | 523 | 4.3 |
| 7 | 너무 길거나 어려운 곳 말고요. | SUCCESS | NORMAL | visible | 1289 | 484 | 345 | 4.2 |
| 8 | 대중교통으로 가기 쉬운 곳이면 좋겠어요. | SUCCESS | RUNAWAY | visible | 1498 | 4293 | 309 | 34.9 |
| 9 | 아이에게 설명하기 쉬운 전시가 필요해요. | SUCCESS | NORMAL | visible | 1697 | 356 | 387 | 3.0 |
| 10 | 위 정보 다 반영해서 박물관 3곳 추천 + 각각 이유. | SUCCESS | NORMAL | visible | 1859 | 589 | 653 | 5.1 |

### REC-MT-102 (recommendation / defector_settlement_program)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국 정착 프로그램 추천해주세요. | SUCCESS | NORMAL | visible | 276 | 533 | 264 | 3.8 |
| 2 | 50대 여자, 평양 출신이에요. 작년에 한국 왔어요. | SUCCESS | NORMAL | visible | 523 | 552 | 582 | 4.2 |
| 3 | 혼자 살고 있어요. | SUCCESS | NORMAL | visible | 894 | 440 | 566 | 3.4 |
| 4 | 장사 해보고 싶어요. 컴퓨터는 약해요. | SUCCESS | RUNAWAY | visible | 1261 | 6425 | 337 | 34.1 |
| 5 | 서울에 살아요. | SUCCESS | NORMAL | visible | 1546 | 278 | 278 | 2.0 |
| 6 | 너무 빨리 진행되는 건 따라가기 힘들어요. | SUCCESS | NORMAL | visible | 1651 | 261 | 133 | 2.1 |
| 7 | 온라인 신청보다 방문 상담이 편해요. | SUCCESS | NORMAL | visible | 1547 | 358 | 371 | 2.9 |
| 8 | 창업 전에 기초 교육부터 받고 싶어요. | SUCCESS | RUNAWAY | visible | 1590 | 5126 | 326 | 34.6 |
| 9 | 소상공인이라는 말도 아직 어려워요. | SUCCESS | RUNAWAY | visible | 1686 | 4413 | 290 | 34.7 |
| 10 | 위 조건 다 반영해서 정착 지원 프로그램 3개 추천 + 이유. | REPETITION_LOOP | RUNAWAY | visible | 1705 | 5597 | 7611 | 35.1 |

### REC-MT-103 (recommendation / elderly_culture_event)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 우리 동네 문화행사 추천 좀 해주세요. | SUCCESS | NORMAL | visible | 278 | 339 | 291 | 2.6 |
| 2 | 75살이에요. 무릎이 안 좋아요. | SUCCESS | NORMAL | visible | 534 | 502 | 342 | 4.2 |
| 3 | 큰 글씨, 큰 화면이면 좋아요. | SUCCESS | NORMAL | visible | 824 | 258 | 346 | 2.2 |
| 4 | 가곡이나 옛날 노래 좋아해요. | SUCCESS | NORMAL | visible | 1114 | 517 | 593 | 4.3 |
| 5 | 친구 사귈 수 있는 곳이면 더 좋고요. | SUCCESS | NORMAL | visible | 1483 | 631 | 530 | 5.1 |
| 6 | 오래 서 있는 행사는 어렵습니다. | SUCCESS | NORMAL | visible | 1689 | 317 | 346 | 2.6 |
| 7 | 버스로 갈 수 있는 곳이 좋아요. | SUCCESS | NORMAL | visible | 1792 | 502 | 667 | 4.2 |
| 8 | 계단이 적은 장소를 원해요. | SUCCESS | RUNAWAY | visible | 1969 | 3952 | 413 | 34.9 |
| 9 | 오후 시간이 편합니다. | REPETITION_LOOP | RUNAWAY | visible | 1921 | 3805 | 3060 | 35.4 |
| 10 | 위 조건 다 반영해서 행사 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=가곡) | NORMAL | visible | 1920 | 816 | 625 | 6.9 |

### REC-MT-104 (recommendation / office_worker_fitness_diet)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 운동 루틴이랑 식단 추천해줘. | SUCCESS | NORMAL | visible | 275 | 477 | 536 | 3.9 |
| 2 | 32살 사무직, 허리가 자주 아파. | THINK_RUNAWAY | NORMAL | visible | 634 | 1095 | 832 | 9.1 |
| 3 | 집에서 할 수 있는 거 위주. | THINK_RUNAWAY | NORMAL | visible | 1003 | 854 | 1163 | 7.3 |
| 4 | 평일 저녁 30분. | THINK_RUNAWAY | NORMAL | visible | 1367 | 668 | 856 | 5.7 |
| 5 | 요리 잘 못해. | THINK_RUNAWAY | REPETITION_LOOP | visible | 1727 | 740 | 842 | 6.5 |
| 6 | 키 175에 몸무게 82kg이야. | THINK_RUNAWAY | NORMAL | visible | 1825 | 716 | 946 | 6.4 |
| 7 | 헬스장은 당분간 안 갈 생각이야. | SUCCESS | NORMAL | visible | 1925 | 775 | 538 | 6.5 |
| 8 | 요가매트는 있어. | THINK_RUNAWAY | NORMAL | visible | 2023 | 668 | 853 | 5.7 |
| 9 | 허리에 부담 가는 윗몸일으키기는 싫어. | THINK_RUNAWAY | NORMAL | visible | 2125 | 714 | 1066 | 6.3 |
| 10 | 위 정보로 1주 운동 + 식단 표로 추천해줘. | RECOMMENDATION_GENERIC(missing=집,30분) | NORMAL | visible | 2136 | 1101 | 676 | 9.6 |

### REC-MT-105 (recommendation / student_learning_resource)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 학습 자료 추천해줘. | SUCCESS | NORMAL | visible | 273 | 366 | 127 | 2.7 |
| 2 | 정보 부족하면 먼저 질문해줘. | SUCCESS | NORMAL | visible | 425 | 176 | 127 | 1.4 |
| 3 | 컴퓨터공학 전공 3학년이야. | SUCCESS | NORMAL | visible | 589 | 598 | 597 | 4.3 |
| 4 | 머신러닝 기초 공부하고 싶어. | SUCCESS | NORMAL | visible | 956 | 652 | 624 | 4.4 |
| 5 | 한국어 자료가 더 편해. 영어도 가능은 함. | SUCCESS | NORMAL | visible | 1327 | 445 | 497 | 3.3 |
| 6 | 책보단 무료 강의가 좋아. | SUCCESS | NORMAL | visible | 1609 | 428 | 480 | 3.2 |
| 7 | 수학 백그라운드는 미적분/선형대수 학부 수준. | THINK_RUNAWAY | RUNAWAY | visible | 1889 | 3854 | 918 | 34.6 |
| 8 | 파이썬은 기본 문법 정도 알아. | SUCCESS | RUNAWAY | visible | 1994 | 4459 | 450 | 34.7 |
| 9 | 딥러닝보다 머신러닝 개념부터 하고 싶어. | SUCCESS | RUNAWAY | visible | 2073 | 4401 | 424 | 34.7 |
| 10 | 위 정보로 학습 자료 3개 추천 + 각각 이유. | RECOMMENDATION_GENERIC(missing=3학년) | RUNAWAY | visible | 2067 | 4396 | 625 | 35.0 |
