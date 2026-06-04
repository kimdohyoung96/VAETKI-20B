# 평가 결과

## 1. 전체 요약

- 세션 수: 20
- 총 turn: 200
- 성공 turn: 138 (69.0%)
- 성공 latency 중앙값: 3.3s
- 실패 latency 중앙값: 34.2s

## 1-1. Summary Memory / Recent-Turn 진단

- prompt token 중앙값: 1098
- prompt token 최대값: 1597
- memory token 중앙값: 432
- memory token 최대값: 800
- reply token 중앙값: 534
- reply token 최대값: 8725
- clean source 분포: visible=200
- debug status 분포: NORMAL=130, RUNAWAY=67, REPETITION_LOOP=3

## 2. 트랙별 성공률

| 트랙 | 성공/전체 | 성공률 |
|---|---|---|
| persona | 34/50 | 68.0% |
| multiturn | 48/50 | 96.0% |
| foreigner_lang | 17/50 | 34.0% |
| recommendation | 39/50 | 78.0% |

## 3. 실패 유형 분포

### 3.1 일반 실패

| 유형 | 개수 |
|---|---|
| REPETITION_LOOP | 38 |
| THINK_RUNAWAY | 4 |

### 3.2 4축 특화 실패 (generic=SUCCESS이지만 트랙 기준 미충족)

| 유형 | 개수 |
|---|---|
| VOCAB_MISMATCH | 14 |
| RECOMMENDATION_GENERIC | 4 |
| PERSONA_RECALL_FAIL | 1 |
| ITEM_COUNT_MISMATCH | 1 |

## 4. 세션별 turn 결과

### PER-MT-101 (persona / multicultural_museum)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 박물관 가이드 도움 받고 싶어요. | SUCCESS | NORMAL | visible | 283 | 175 | 151 | 2.0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | NORMAL | visible | 466 | 370 | 198 | 3.0 |
| 3 | 한국어는 일상 회화 정도만 가능해요. | SUCCESS | NORMAL | visible | 688 | 304 | 193 | 2.4 |
| 4 | 한국 역사 잘 몰라요. 조선시대 이런 거 들어본 적 없어요. | SUCCESS | NORMAL | visible | 816 | 274 | 168 | 2.2 |
| 5 | 그림이나 도자기 같은 거 보는 거 좋아해요. | SUCCESS | NORMAL | visible | 910 | 271 | 236 | 2.2 |
| 6 | 8살 딸이랑 같이 가요. 짧게 보고 싶어요. | SUCCESS | NORMAL | visible | 1038 | 577 | 452 | 4.8 |
| 7 | 딸은 오래 걷는 걸 싫어해서 이동이 적었으면 해요. | SUCCESS | NORMAL | visible | 1281 | 399 | 275 | 3.5 |
| 8 | 저는 쉬운 한국어 설명이 있으면 좋아요. | SUCCESS | NORMAL | visible | 1405 | 341 | 272 | 3.0 |
| 9 | 영어 안내가 있으면 도움은 되지만 꼭 필요하진 않아요. | SUCCESS | RUNAWAY | visible | 1322 | 4234 | 240 | 34.1 |
| 10 | 위 정보를 모두 반영해서 저와 딸의 관람 페르소나를 한 단락으로 정리해주… | REPETITION_LOOP | RUNAWAY | visible | 1316 | 4718 | 9436 | 34.4 |

### PER-MT-102 (persona / defector_settlement)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 도움 받고 싶어서요. | REPETITION_LOOP | RUNAWAY | visible | 279 | 4496 | 3996 | 33.5 |
| 2 | 작년에 한국 왔어요. 50대 여자입니다. | REPETITION_LOOP | RUNAWAY | visible | 641 | 4354 | 8707 | 33.5 |
| 3 | 혼자 살고 있어요. 평양 출신이에요. | REPETITION_LOOP | RUNAWAY | visible | 1012 | 4355 | 8709 | 33.9 |
| 4 | 장사 좀 해보고 싶은데 한국 시스템을 잘 몰라요. 컴퓨터도 약해요. | REPETITION_LOOP | RUNAWAY | visible | 1124 | 4355 | 8709 | 34.3 |
| 5 | 스마트폰은 전화랑 문자 정도만 익숙해요. | REPETITION_LOOP | RUNAWAY | visible | 1235 | 4357 | 8713 | 34.2 |
| 6 | 온라인 신청이라는 말이 나오면 긴장이 돼요. | REPETITION_LOOP | RUNAWAY | visible | 1340 | 4359 | 8717 | 34.2 |
| 7 | 가게를 바로 크게 시작할 생각은 없어요. | REPETITION_LOOP | RUNAWAY | visible | 1436 | 4356 | 8711 | 34.5 |
| 8 | 먼저 배워보고 천천히 준비하고 싶어요. | REPETITION_LOOP | RUNAWAY | visible | 1538 | 4359 | 8717 | 34.5 |
| 9 | 서울에 살지만 동네 밖으로 멀리 가는 건 부담돼요. | REPETITION_LOOP | RUNAWAY | visible | 1542 | 4355 | 8709 | 34.1 |
| 10 | 위 정보로 제 상황을 한 단락 페르소나로 정리해주세요. | REPETITION_LOOP | RUNAWAY | visible | 1549 | 4354 | 8707 | 34.2 |

### PER-MT-103 (persona / elderly_culture)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 우리 동네 문화센터 어떻게 다닐지 좀 알려줘요. | SUCCESS | NORMAL | visible | 287 | 280 | 351 | 2.2 |
| 2 | 75살이고 무릎이 안 좋아서 멀리는 못 다녀요. | SUCCESS | REPETITION_LOOP | visible | 583 | 370 | 279 | 3.1 |
| 3 | 글씨 작은 건 잘 안 보여요. 큰 글씨로 부탁해요. | SUCCESS | NORMAL | visible | 851 | 344 | 279 | 2.9 |
| 4 | 옛날에 노래 부르는 거 좋아했어요. 가곡 같은 거. | SUCCESS | NORMAL | visible | 919 | 337 | 279 | 2.8 |
| 5 | 친구 사귀고 싶어요. 혼자 너무 적적해요. | SUCCESS | NORMAL | visible | 1023 | 337 | 334 | 3.0 |
| 6 | 계단이 많은 곳은 피하고 싶어요. | SUCCESS | NORMAL | visible | 1149 | 150 | 299 | 1.3 |
| 7 | 버스로 한 번에 갈 수 있으면 좋겠어요. | REPETITION_LOOP | RUNAWAY | visible | 1257 | 3731 | 5388 | 34.2 |
| 8 | 오전보다는 오후 시간이 편해요. | REPETITION_LOOP | RUNAWAY | visible | 1440 | 4198 | 8395 | 34.5 |
| 9 | 수업 시간이 너무 길면 힘들어요. | REPETITION_LOOP | RUNAWAY | visible | 1533 | 4198 | 8395 | 34.8 |
| 10 | 위 정보로 제 문화센터 이용 페르소나를 정리해주세요. | REPETITION_LOOP | RUNAWAY | visible | 1531 | 3901 | 7611 | 34.7 |

### PER-MT-104 (persona / office_worker_fitness)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 운동 좀 시작하려고. | SUCCESS | NORMAL | visible | 276 | 370 | 347 | 2.9 |
| 2 | 32살 직장인이고 사무실에서 하루 종일 앉아 있어. | SUCCESS | NORMAL | visible | 560 | 662 | 286 | 5.6 |
| 3 | 키 175, 몸무게 82kg. | SUCCESS | NORMAL | visible | 824 | 548 | 594 | 4.6 |
| 4 | 허리가 자주 아파. | SUCCESS | NORMAL | visible | 1000 | 460 | 258 | 3.8 |
| 5 | 헬스장은 부담스럽고 집에서 할 수 있는 거 좋아. | SUCCESS | NORMAL | visible | 1085 | 468 | 464 | 3.9 |
| 6 | 시간은 평일 저녁 30분 정도밖에 못 내. | SUCCESS | NORMAL | visible | 1176 | 407 | 437 | 3.3 |
| 7 | 식단도 신경 쓰고 싶은데 요리는 잘 못해. | SUCCESS | NORMAL | visible | 1376 | 567 | 672 | 4.8 |
| 8 | 아침은 자주 거르고 점심은 회사 근처에서 먹어. | SUCCESS | NORMAL | visible | 1496 | 543 | 568 | 4.6 |
| 9 | 퇴근하면 피곤해서 강도 높은 운동은 자신 없어. | SUCCESS | NORMAL | visible | 1537 | 445 | 564 | 3.7 |
| 10 | 위 정보 다 종합해서 내 운동 페르소나를 한 단락으로 정리해줘. | PERSONA_RECALL_FAIL(missing=32,집) | NORMAL | visible | 1542 | 534 | 414 | 4.2 |

### PER-MT-105 (persona / parent_kid_education)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 우리 아이 학습 도움 받고 싶어요. | SUCCESS | NORMAL | visible | 280 | 309 | 307 | 2.3 |
| 2 | 초등학교 3학년 딸이에요. | SUCCESS | NORMAL | visible | 541 | 337 | 281 | 2.6 |
| 3 | 수학을 어려워해요. 특히 분수 부분. | SUCCESS | NORMAL | visible | 800 | 420 | 424 | 3.3 |
| 4 | 책 읽는 건 좋아하는데 혼자만 하려고 해요. | SUCCESS | NORMAL | visible | 963 | 425 | 413 | 3.4 |
| 5 | 문제집을 오래 붙잡고 있으면 금방 지쳐요. | SUCCESS | NORMAL | visible | 1137 | 392 | 370 | 3.4 |
| 6 | 그림이 있는 설명은 잘 보는 편이에요. | SUCCESS | NORMAL | visible | 1214 | 368 | 366 | 3.1 |
| 7 | 말로 설명하면 중간에 딴생각을 해요. | SUCCESS | NORMAL | visible | 1291 | 295 | 371 | 2.4 |
| 8 | 분모와 분자를 자꾸 헷갈려요. | SUCCESS | NORMAL | visible | 1389 | 415 | 467 | 3.7 |
| 9 | 학교 숙제는 미루다가 밤에 하는 편이에요. | SUCCESS | NORMAL | visible | 1439 | 375 | 369 | 3.0 |
| 10 | 위 정보로 우리 아이 학습 페르소나를 정리해주세요. | SUCCESS | NORMAL | visible | 1447 | 355 | 706 | 2.9 |

### MTN-MT-101 (multiturn / intent_repair)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 저녁 메뉴 추천해줘. | SUCCESS | NORMAL | visible | 257 | 344 | 229 | 2.8 |
| 2 | 한식 말고. | SUCCESS | RUNAWAY | visible | 470 | 4025 | 237 | 34.3 |
| 3 | 아 미안, 한식도 괜찮아. 단 너무 매운 건 빼고. | SUCCESS | RUNAWAY | visible | 706 | 4411 | 288 | 34.4 |
| 4 | 고기는 가능하지만 튀김은 싫어. | SUCCESS | RUNAWAY | visible | 847 | 4418 | 247 | 33.5 |
| 5 | 조리 시간은 20분 안쪽이면 좋겠어. | SUCCESS | RUNAWAY | visible | 959 | 3884 | 229 | 34.0 |
| 6 | 집에 계란이랑 두부가 있어. | SUCCESS | RUNAWAY | visible | 1025 | 4417 | 191 | 34.1 |
| 7 | 밥은 이미 해놨어. | SUCCESS | RUNAWAY | visible | 1093 | 4421 | 201 | 33.8 |
| 8 | 국물 요리는 오늘은 별로야. | SUCCESS | NORMAL | visible | 1173 | 108 | 214 | 0.9 |
| 9 | 냉장고에 애호박도 조금 있어. | SUCCESS | NORMAL | visible | 1285 | 89 | 177 | 0.8 |
| 10 | 최종 저녁 메뉴와 이유를 짧게 다시 말해줘. | SUCCESS | NORMAL | visible | 1282 | 85 | 167 | 0.7 |

### MTN-MT-102 (multiturn / tone_shift)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. 한국 여행 정보 부탁드립니다. | SUCCESS | REPETITION_LOOP | visible | 263 | 449 | 499 | 3.6 |
| 2 | 정중하게 안내해주세요. 저는 외국인이에요. | SUCCESS | NORMAL | visible | 627 | 528 | 499 | 4.2 |
| 3 | 경주 추천 받고 싶어요. | SUCCESS | NORMAL | visible | 996 | 531 | 581 | 4.2 |
| 4 | 역사 설명은 너무 어렵지 않게 부탁드립니다. | SUCCESS | NORMAL | visible | 1096 | 534 | 500 | 4.4 |
| 5 | 하루 일정으로만 보고 싶습니다. | SUCCESS | NORMAL | visible | 1197 | 453 | 258 | 3.6 |
| 6 | 이제 친구처럼 편하게 말해줘. 반말로. | SUCCESS | NORMAL | visible | 1177 | 290 | 278 | 2.3 |
| 7 | 거기서 뭘 봐야 돼? | SUCCESS | NORMAL | visible | 1162 | 142 | 281 | 1.3 |
| 8 | 밥 먹을 곳도 하나 넣어줘. | SUCCESS | NORMAL | visible | 1274 | 354 | 467 | 3.0 |
| 9 | 걷는 시간이 너무 길면 힘들어. | SUCCESS | NORMAL | visible | 1362 | 124 | 246 | 1.1 |
| 10 | 처음부터 지금까지 말투가 몇 번 바뀌었는지도 알려 주세요. | SUCCESS | NORMAL | visible | 1351 | 427 | 186 | 3.5 |

### MTN-MT-103 (multiturn / reference_tracking)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 무릎 통증 때문에 병원 두 곳 알아봤어요. 정형외과랑 한의원. | SUCCESS | NORMAL | visible | 269 | 492 | 270 | 3.9 |
| 2 | 거기 둘 중 70대한테 더 맞는 곳은? | SUCCESS | NORMAL | visible | 522 | 241 | 215 | 2.0 |
| 3 | 정형외과는 검사 장비가 있다고 들었어요. | SUCCESS | NORMAL | visible | 753 | 288 | 166 | 2.2 |
| 4 | 한의원은 침 치료가 가능하대요. | SUCCESS | NORMAL | visible | 795 | 268 | 166 | 2.0 |
| 5 | 그 곳 보험 적용돼요? | SUCCESS | NORMAL | visible | 866 | 444 | 166 | 3.5 |
| 6 | 어느 쪽이 먼저 진단받기에 좋아요? | SUCCESS | NORMAL | visible | 962 | 424 | 197 | 3.5 |
| 7 | 통증이 오래됐으면 어디가 우선이에요? | SUCCESS | NORMAL | visible | 1080 | 289 | 197 | 2.3 |
| 8 | 걷기 힘든 날에는 대기 시간이 짧은 곳이 좋아요. | THINK_RUNAWAY | RUNAWAY | visible | 1204 | 8725 | 824 | 33.9 |
| 9 | 약을 많이 먹는 건 부담스러워요. | SUCCESS | RUNAWAY | visible | 1352 | 4096 | 413 | 33.9 |
| 10 | 내 조건 중 나이와 무릎 통증을 포함해서 최종 정리해주세요. | SUCCESS | RUNAWAY | visible | 1465 | 4246 | 437 | 34.5 |

### MTN-MT-104 (multiturn / topic_switch_return)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 회의록 정리하는 법 알려줘. | SUCCESS | NORMAL | visible | 259 | 289 | 155 | 2.1 |
| 2 | 가장 효과적인 방법은? | SUCCESS | NORMAL | visible | 439 | 278 | 155 | 2.0 |
| 3 | 회의 참석자가 8명 정도일 때 기준으로 알려줘. | SUCCESS | NORMAL | visible | 635 | 368 | 155 | 2.7 |
| 4 | 결정사항과 액션아이템을 분리하고 싶어. | SUCCESS | NORMAL | visible | 740 | 358 | 312 | 2.9 |
| 5 | 잠깐, 다른 거 물어봐도 돼? 노션이랑 옵시디언 차이가 뭐야? | SUCCESS | RUNAWAY | visible | 931 | 4021 | 459 | 34.1 |
| 6 | 둘 중 회의록에 더 적합한 건? | SUCCESS | NORMAL | visible | 1186 | 288 | 157 | 2.3 |
| 7 | 가격은 어떻게 돼? | SUCCESS | NORMAL | visible | 1203 | 203 | 157 | 1.8 |
| 8 | 회사 공유용이면 어떤 도구가 나아? | SUCCESS | NORMAL | visible | 1142 | 265 | 158 | 2.2 |
| 9 | 개인 지식관리용이면 어떤 도구가 좋아? | SUCCESS | NORMAL | visible | 1148 | 184 | 147 | 1.5 |
| 10 | 최종적으로 회의록 정리 프로세스만 5단계로 출력해줘. | SUCCESS | NORMAL | visible | 1248 | 230 | 85 | 1.9 |

### MTN-MT-105 (multiturn / constraint_accumulation)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국 정착할 때 신청해야 하는 지원금 알려주세요. | SUCCESS | NORMAL | visible | 265 | 411 | 434 | 3.3 |
| 2 | 정확히 3가지만. | SUCCESS | NORMAL | visible | 592 | 139 | 273 | 1.2 |
| 3 | 각 항목 옆에 신청 기관도 같이. | SUCCESS | NORMAL | visible | 843 | 266 | 212 | 2.3 |
| 4 | 각 항목 30자 이내로 짧게. | SUCCESS | NORMAL | visible | 827 | 208 | 152 | 2.0 |
| 5 | 마지막은 새터민이 가장 먼저 알아야 할 순서로 정렬해주세요. | SUCCESS | NORMAL | visible | 875 | 225 | 439 | 1.9 |
| 6 | 온라인 신청이 필요한지 여부도 표시해주세요. | SUCCESS | NORMAL | visible | 1100 | 184 | 24 | 1.6 |
| 7 | 컴퓨터가 약한 사람 기준으로 쉬운 순서를 원해요. | SUCCESS | NORMAL | visible | 1078 | 273 | 545 | 2.3 |
| 8 | 전화 문의가 가능한지도 적어주세요. | SUCCESS | NORMAL | visible | 1207 | 251 | 500 | 2.0 |
| 9 | 금액은 확실하지 않으면 쓰지 마세요. | SUCCESS | NORMAL | visible | 1544 | 251 | 500 | 2.1 |
| 10 | 마지막에 추가 설명은 쓰지 마세요. | ITEM_COUNT_MISMATCH(expected=3,got=0) | NORMAL | visible | 1537 | 251 | 500 | 2.1 |

### FRN-MT-101 (foreigner_lang / beginner_restaurant)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국어 잘 못해요. 천천히 쉽게 말해주세요. | SUCCESS | NORMAL | visible | 275 | 215 | 110 | 1.8 |
| 2 | 식당에서 주문하고 싶어요. 어떻게 말해요? | SUCCESS | NORMAL | visible | 414 | 235 | 123 | 2.1 |
| 3 | "이거 주세요" 무엇이에요? | VOCAB_MISMATCH(long_sentences=3) | NORMAL | visible | 577 | 281 | 154 | 2.4 |
| 4 | 매운 거 싫어요. 어떻게 말해요? | SUCCESS | NORMAL | visible | 696 | 229 | 54 | 2.1 |
| 5 | 물 주세요는 어떻게 말해요? | VOCAB_MISMATCH(long_sentences=2) | NORMAL | visible | 705 | 228 | 127 | 2.1 |
| 6 | 계산하고 싶을 때 뭐라고 해요? | REPETITION_LOOP | NORMAL | visible | 776 | 2790 | 5579 | 34.2 |
| 7 | 고기 안 먹어요. 쉬운 말로 알려주세요. | REPETITION_LOOP | NORMAL | visible | 1101 | 2844 | 5687 | 33.8 |
| 8 | 혼자 먹어도 돼요? 어떻게 물어요? | REPETITION_LOOP | RUNAWAY | visible | 1393 | 3501 | 7001 | 34.2 |
| 9 | 포장하고 싶어요. 짧게 말해주세요. | REPETITION_LOOP | NORMAL | visible | 1495 | 3016 | 6032 | 34.3 |
| 10 | 지금까지 얘기 다시. 짧게. 쉬운 단어만. | SUCCESS | NORMAL | visible | 1597 | 287 | 22 | 2.4 |

### FRN-MT-102 (foreigner_lang / code_switching)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 안녕하세요. I'm learning Korean. | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 276 | 356 | 441 | 3.0 |
| 2 | "처마" 무슨 뜻이에요? Is it about the roof? | VOCAB_MISMATCH(no_english_terms) | NORMAL | visible | 619 | 452 | 520 | 3.7 |
| 3 | 한옥 설명해주세요. 어려우면 영어 단어 쓰셔도 돼요. | SUCCESS | NORMAL | visible | 1003 | 449 | 392 | 3.6 |
| 4 | 기와는 영어로 roof tile 맞아요? | SUCCESS | NORMAL | visible | 1082 | 314 | 329 | 2.5 |
| 5 | 마루는 floor랑 같아요? | REPETITION_LOOP | RUNAWAY | visible | 1090 | 4128 | 5055 | 34.4 |
| 6 | 온돌은 heating system이라고 보면 돼요? | SUCCESS | RUNAWAY | visible | 1243 | 3962 | 441 | 34.2 |
| 7 | 한옥 보러 가고 싶어요. 어디 가요? | VOCAB_MISMATCH(no_english_terms) | RUNAWAY | visible | 1404 | 4031 | 457 | 34.4 |
| 8 | 서울에서 가기 쉬운 곳이면 좋아요. | VOCAB_MISMATCH(no_english_terms) | RUNAWAY | visible | 1486 | 4037 | 269 | 34.8 |
| 9 | 입장료 비싸요? | VOCAB_MISMATCH(no_english_terms) | RUNAWAY | visible | 1386 | 4038 | 276 | 33.9 |
| 10 | 위 내용 다시 정리. Korean first, then English s… | VOCAB_MISMATCH(no_english_terms) | RUNAWAY | visible | 1296 | 4037 | 273 | 34.4 |

### FRN-MT-103 (foreigner_lang / english_to_korean_teaching)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | Hi! Can you help me practice Korean? | VOCAB_MISMATCH(no_romanization;not_trilingual) | RUNAWAY | visible | 281 | 4135 | 245 | 33.3 |
| 2 | I want to order food in Korean. Teach me… | VOCAB_MISMATCH(no_romanization;not_trilingual) | NORMAL | visible | 540 | 349 | 373 | 3.1 |
| 3 | How do I say "no spicy please"? | SUCCESS | RUNAWAY | visible | 863 | 3801 | 596 | 33.5 |
| 4 | 한국어로 다시 말해주세요. 천천히. | REPETITION_LOOP | RUNAWAY | visible | 1090 | 4094 | 8188 | 33.8 |
| 5 | 발음도 알려줘요. 로마자로요. | REPETITION_LOOP | RUNAWAY | visible | 1243 | 4098 | 8196 | 33.9 |
| 6 | "감사합니다" 발음도 알려주세요. | REPETITION_LOOP | NORMAL | visible | 1337 | 3334 | 6668 | 34.4 |
| 7 | Can you include English meaning every ti… | REPETITION_LOOP | RUNAWAY | visible | 1450 | 4111 | 8220 | 34.4 |
| 8 | I need Korean, romanization, and English… | REPETITION_LOOP | RUNAWAY | visible | 1575 | 4101 | 8202 | 34.0 |
| 9 | How do I say "water please"? | REPETITION_LOOP | NORMAL | visible | 1583 | 3343 | 6686 | 34.2 |
| 10 | 마지막에 가장 중요한 표현 2개만 다시 골라주세요. | REPETITION_LOOP | RUNAWAY | visible | 1562 | 4093 | 8186 | 34.5 |

### FRN-MT-104 (foreigner_lang / avoid_hanja_hospital)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국어 공부해요. 한자어 어려워요. 병원 갈 때 쉬운 말로 알려주세요. | SUCCESS | NORMAL | visible | 282 | 390 | 343 | 3.2 |
| 2 | "감기" 같은 단어 말고 다른 쉬운 말로 증상 설명하는 법. | SUCCESS | NORMAL | visible | 580 | 490 | 478 | 4.3 |
| 3 | 머리가 아파요를 더 쉬운 말로도 알려주세요. | REPETITION_LOOP | RUNAWAY | visible | 948 | 3656 | 7311 | 34.5 |
| 4 | 배가 아플 때 말하는 문장 알려주세요. | REPETITION_LOOP | NORMAL | visible | 1122 | 3408 | 6816 | 34.3 |
| 5 | 열이 나는 것 같아요를 쉬운 말로요. | REPETITION_LOOP | NORMAL | visible | 1230 | 3410 | 3462 | 34.2 |
| 6 | 목이 따가워요는 어떻게 말해요? | REPETITION_LOOP | NORMAL | visible | 1328 | 3481 | 6962 | 34.2 |
| 7 | 기침이 나와요는 쉬운가요? | REPETITION_LOOP | NORMAL | visible | 1425 | 3412 | 6823 | 34.3 |
| 8 | 병원에서 접수하는 법 쉽게 알려주세요. | REPETITION_LOOP | RUNAWAY | visible | 1524 | 3852 | 2229 | 34.7 |
| 9 | 이름을 말할 때 문장 알려주세요. | SUCCESS | NORMAL | visible | 1516 | 3416 | 331 | 34.8 |
| 10 | 병원에서 처음부터 끝까지 말할 순서만 알려주세요. | REPETITION_LOOP | RUNAWAY | visible | 1431 | 3653 | 7306 | 34.3 |

### FRN-MT-105 (foreigner_lang / register_shift)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국어 책으로 공부했어요. 너무 formal해요. | SUCCESS | RUNAWAY | visible | 276 | 3728 | 488 | 33.9 |
| 2 | 친구한테 쓸 말 알려주세요. 평어/반말로요. | SUCCESS | RUNAWAY | visible | 637 | 3805 | 191 | 33.8 |
| 3 | "안녕하세요" → 친구한테는 어떻게 말해요? "감사합니다"는요? | VOCAB_MISMATCH(uses_formal_register) | RUNAWAY | visible | 864 | 3870 | 278 | 34.2 |
| 4 | 카페에서 음료 주문할 때 일상적인 말투로. | SUCCESS | RUNAWAY | visible | 866 | 3896 | 257 | 33.8 |
| 5 | 친구에게 밥 먹자고 말하는 표현 알려줘. | SUCCESS | RUNAWAY | visible | 1001 | 3942 | 248 | 34.1 |
| 6 | 미안해를 자연스럽게 말하는 방법은? | SUCCESS | RUNAWAY | visible | 1082 | 4092 | 175 | 33.9 |
| 7 | 괜찮습니다 말고 편한 말로 바꿔줘. | VOCAB_MISMATCH(uses_formal_register) | RUNAWAY | visible | 1140 | 4092 | 176 | 34.4 |
| 8 | 잘 지내세요 말고 친구한테 쓰는 말은? | VOCAB_MISMATCH(uses_formal_register) | RUNAWAY | visible | 1205 | 4093 | 177 | 34.4 |
| 9 | 너무 무례하지 않은 반말이면 좋겠어. | SUCCESS | RUNAWAY | visible | 1204 | 4090 | 171 | 33.8 |
| 10 | 마지막에는 반말 표현만 번호로 정리해줘. | VOCAB_MISMATCH(uses_formal_register) | NORMAL | visible | 1201 | 206 | 81 | 1.9 |

### REC-MT-101 (recommendation / multicultural_museum)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국 박물관 가보고 싶어요. 어디가 좋을까요? | SUCCESS | NORMAL | visible | 280 | 378 | 236 | 2.9 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | RUNAWAY | visible | 513 | 3996 | 742 | 33.7 |
| 3 | 한국어는 일상 회화 정도예요. | SUCCESS | NORMAL | visible | 884 | 427 | 236 | 3.5 |
| 4 | 한국 역사 잘 몰라요. | SUCCESS | NORMAL | visible | 977 | 399 | 350 | 3.3 |
| 5 | 그림이나 도자기 좋아해요. | THINK_RUNAWAY | RUNAWAY | visible | 996 | 3906 | 812 | 34.1 |
| 6 | 8살 딸이랑 같이 가요. | SUCCESS | NORMAL | visible | 1225 | 719 | 350 | 6.1 |
| 7 | 너무 길거나 어려운 곳 말고요. | SUCCESS | NORMAL | visible | 1325 | 189 | 179 | 1.7 |
| 8 | 대중교통으로 가기 쉬운 곳이면 좋겠어요. | SUCCESS | NORMAL | visible | 1269 | 215 | 193 | 1.8 |
| 9 | 아이에게 설명하기 쉬운 전시가 필요해요. | SUCCESS | NORMAL | visible | 1194 | 102 | 203 | 0.9 |
| 10 | 위 정보 다 반영해서 박물관 3곳 추천 + 각각 이유. | RECOMMENDATION_GENERIC(missing=베트남,딸,도자기) | NORMAL | visible | 1212 | 361 | 266 | 2.9 |

### REC-MT-102 (recommendation / defector_settlement_program)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 한국 정착 프로그램 추천해주세요. | SUCCESS | NORMAL | visible | 276 | 423 | 495 | 3.1 |
| 2 | 50대 여자, 평양 출신이에요. 작년에 한국 왔어요. | SUCCESS | NORMAL | visible | 638 | 478 | 455 | 3.9 |
| 3 | 혼자 살고 있어요. | SUCCESS | RUNAWAY | visible | 986 | 4016 | 324 | 34.5 |
| 4 | 장사 해보고 싶어요. 컴퓨터는 약해요. | SUCCESS | NORMAL | visible | 1000 | 923 | 400 | 6.8 |
| 5 | 서울에 살아요. | REPETITION_LOOP | RUNAWAY | visible | 1064 | 4525 | 2947 | 34.6 |
| 6 | 너무 빨리 진행되는 건 따라가기 힘들어요. | SUCCESS | NORMAL | visible | 1254 | 317 | 264 | 2.8 |
| 7 | 온라인 신청보다 방문 상담이 편해요. | REPETITION_LOOP | RUNAWAY | visible | 1289 | 4556 | 9112 | 34.6 |
| 8 | 창업 전에 기초 교육부터 받고 싶어요. | SUCCESS | RUNAWAY | visible | 1397 | 4490 | 535 | 35.0 |
| 9 | 소상공인이라는 말도 아직 어려워요. | SUCCESS | NORMAL | visible | 1515 | 451 | 442 | 3.6 |
| 10 | 위 조건 다 반영해서 정착 지원 프로그램 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=50대,장사) | NORMAL | visible | 1488 | 661 | 277 | 5.0 |

### REC-MT-103 (recommendation / elderly_culture_event)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 우리 동네 문화행사 추천 좀 해주세요. | SUCCESS | NORMAL | visible | 278 | 378 | 308 | 3.0 |
| 2 | 75살이에요. 무릎이 안 좋아요. | SUCCESS | NORMAL | visible | 542 | 657 | 483 | 5.4 |
| 3 | 큰 글씨, 큰 화면이면 좋아요. | SUCCESS | NORMAL | visible | 901 | 287 | 413 | 2.4 |
| 4 | 가곡이나 옛날 노래 좋아해요. | SUCCESS | NORMAL | visible | 1051 | 558 | 326 | 4.5 |
| 5 | 친구 사귈 수 있는 곳이면 더 좋고요. | SUCCESS | NORMAL | visible | 1075 | 530 | 446 | 4.2 |
| 6 | 오래 서 있는 행사는 어렵습니다. | SUCCESS | RUNAWAY | visible | 1195 | 4276 | 787 | 34.3 |
| 7 | 버스로 갈 수 있는 곳이 좋아요. | SUCCESS | RUNAWAY | visible | 1384 | 4362 | 556 | 34.4 |
| 8 | 계단이 적은 장소를 원해요. | SUCCESS | RUNAWAY | visible | 1509 | 4366 | 541 | 34.4 |
| 9 | 오후 시간이 편합니다. | SUCCESS | RUNAWAY | visible | 1503 | 4439 | 720 | 34.5 |
| 10 | 위 조건 다 반영해서 행사 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=75,가곡) | NORMAL | visible | 1504 | 577 | 493 | 4.4 |

### REC-MT-104 (recommendation / office_worker_fitness_diet)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 운동 루틴이랑 식단 추천해줘. | SUCCESS | NORMAL | visible | 275 | 399 | 486 | 3.2 |
| 2 | 32살 사무직, 허리가 자주 아파. | SUCCESS | REPETITION_LOOP | visible | 627 | 1111 | 363 | 9.5 |
| 3 | 집에서 할 수 있는 거 위주. | SUCCESS | NORMAL | visible | 925 | 539 | 780 | 4.3 |
| 4 | 평일 저녁 30분. | THINK_RUNAWAY | NORMAL | visible | 1029 | 743 | 950 | 6.5 |
| 5 | 요리 잘 못해. | SUCCESS | NORMAL | visible | 1191 | 556 | 784 | 4.8 |
| 6 | 키 175에 몸무게 82kg이야. | SUCCESS | NORMAL | visible | 1288 | 604 | 383 | 5.1 |
| 7 | 헬스장은 당분간 안 갈 생각이야. | THINK_RUNAWAY | NORMAL | visible | 1332 | 775 | 921 | 6.8 |
| 8 | 요가매트는 있어. | SUCCESS | NORMAL | visible | 1433 | 566 | 535 | 4.8 |
| 9 | 허리에 부담 가는 윗몸일으키기는 싫어. | SUCCESS | NORMAL | visible | 1591 | 742 | 665 | 6.3 |
| 10 | 위 정보로 1주 운동 + 식단 표로 추천해줘. | REPETITION_LOOP | RUNAWAY | visible | 1597 | 4184 | 7895 | 34.7 |

### REC-MT-105 (recommendation / student_learning_resource)

| Turn | User (요약) | 분류 | Debug | Source | Prompt tok | Reply tok | 답 길이 | latency(s) |
|---|---|---|---|---|---:|---:|---:|---:|
| 1 | 학습 자료 추천해줘. | SUCCESS | NORMAL | visible | 273 | 438 | 431 | 3.5 |
| 2 | 정보 부족하면 먼저 질문해줘. | SUCCESS | NORMAL | visible | 591 | 362 | 428 | 2.8 |
| 3 | 컴퓨터공학 전공 3학년이야. | SUCCESS | NORMAL | visible | 922 | 1182 | 381 | 9.2 |
| 4 | 머신러닝 기초 공부하고 싶어. | SUCCESS | NORMAL | visible | 999 | 955 | 390 | 7.5 |
| 5 | 한국어 자료가 더 편해. 영어도 가능은 함. | SUCCESS | NORMAL | visible | 1082 | 952 | 362 | 7.2 |
| 6 | 책보단 무료 강의가 좋아. | SUCCESS | RUNAWAY | visible | 1177 | 4498 | 374 | 34.2 |
| 7 | 수학 백그라운드는 미적분/선형대수 학부 수준. | SUCCESS | RUNAWAY | visible | 1273 | 4657 | 417 | 33.8 |
| 8 | 파이썬은 기본 문법 정도 알아. | SUCCESS | NORMAL | visible | 1401 | 196 | 390 | 1.5 |
| 9 | 딥러닝보다 머신러닝 개념부터 하고 싶어. | REPETITION_LOOP | RUNAWAY | visible | 1417 | 4243 | 4242 | 34.1 |
| 10 | 위 정보로 학습 자료 3개 추천 + 각각 이유. | RECOMMENDATION_GENERIC(missing=3학년) | RUNAWAY | visible | 1463 | 5525 | 266 | 34.7 |
