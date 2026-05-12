# 4축 평가 결과 (think 모드)

## 1. 전체 요약

- 세션 수: 20
- 총 turn: 123
- 성공 turn: 59 (48.0%)
- 성공 latency 중앙값: 43.6s
- 실패 latency 중앙값: 98.7s

## 2. 트랙별 성공률

| 트랙 | 성공/전체 | 성공률 |
|---|---|---|
| persona | 18/31 | 58.1% |
| multiturn | 16/30 | 53.3% |
| foreigner_lang | 9/27 | 33.3% |
| recommendation | 16/35 | 45.7% |

## 3. Summary Memory / Context 진단

- prompt chars 중앙값: 1365
- prompt chars 최대값: 2292
- memory chars 중앙값: 381
- memory chars 최대값: 1116
- raw output chars 중앙값: 481
- raw output chars 최대값: 1598
- clean output chars 중앙값: 103
- clean output chars 최대값: 1096

## 4. 실패 유형 분포

### 4.1 일반 실패

| 유형 | 개수 |
|---|---|
| EMPTY | 51 |
| REPETITION_LOOP | 2 |

### 4.2 4축 특화 실패 (generic=SUCCESS이지만 트랙 기준 미충족)

| 유형 | 개수 |
|---|---|
| VOCAB_MISMATCH | 7 |
| RECOMMENDATION_GENERIC | 2 |
| ITEM_COUNT_MISMATCH | 1 |
| CLARIFY_SKIPPED | 1 |

## 5. 세션별 turn 결과

### PER-MT-101 (persona / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 박물관 가이드 도움 받고 싶어요. | SUCCESS | 138 | 28.7 | 549 | 0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | 138 | 30.5 | 877 | 186 |
| 3 | 한국어는 일상 회화 정도만 가능해요. | SUCCESS | 278 | 33.8 | 1220 | 371 |
| 4 | 한국 역사 잘 몰라요. 조선시대 이런 거 들어본 적 없어요. | EMPTY | 0 | 99.1 | 1550 | 554 |
| 5 | 그림이나 도자기 같은 거 보는 거 좋아해요. | SUCCESS | 557 | 57.9 | 1639 | 642 |
| 6 | 8살 딸이랑 같이 가요. 짧게 보고 싶어요. | EMPTY | 0 | 98.7 | 2192 | 829 |
| 7 | 위 정보 종합해서 저랑 딸의 관람 페르소나 한 단락으로 정리해주세요. | EMPTY | 0 | 98.8 | 2032 | 908 |

### PER-MT-102 (persona / defector_settlement)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 도움 받고 싶어서요. | SUCCESS | 105 | 15.6 | 542 | 0 |
| 2 | 작년에 한국 왔어요. 50대 여자입니다. | SUCCESS | 103 | 32.0 | 792 | 144 |
| 3 | 혼자 살고 있어요. 평양 출신이에요. | REPETITION_LOOP | 1576 | 98.7 | 1064 | 293 |
| 4 | 장사 좀 해보고 싶은데 한국 시스템을 잘 몰라요. 컴퓨터도 약해요. | SUCCESS | 103 | 42.9 | 1158 | 368 |
| 5 | 위 정보로 제 상황 한 단락으로 정리해주세요. | EMPTY | 0 | 98.6 | 1325 | 532 |

### PER-MT-103 (persona / elderly_culture)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 우리 동네 문화센터 어떻게 다닐지 좀 알려줘요. | SUCCESS | 254 | 30.1 | 557 | 0 |
| 2 | 75살이고 무릎이 안 좋아서 멀리는 못 다녀요. | SUCCESS | 497 | 61.0 | 1014 | 196 |
| 3 | 글씨 작은 건 잘 안 보여요. 큰 글씨로 부탁해요. | EMPTY | 0 | 98.8 | 1725 | 386 |
| 4 | 옛날에 노래 부르는 거 좋아했어요. 가곡 같은 거. | SUCCESS | 395 | 49.1 | 1803 | 469 |
| 5 | 친구 사귀고 싶어요. 혼자 너무 적적해요. | EMPTY | 0 | 98.7 | 2130 | 660 |
| 6 | 위 정보로 제 페르소나 정리해주세요. | EMPTY | 0 | 98.7 | 1735 | 738 |

### PER-MT-104 (persona / office_worker_fitness)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 운동 좀 시작하려고. | SUCCESS | 60 | 33.8 | 535 | 0 |
| 2 | 32살 직장인이고 사무실에서 하루 종일 앉아 있어. | SUCCESS | 334 | 43.6 | 698 | 94 |
| 3 | 키 175, 몸무게 82kg. | SUCCESS | 147 | 10.1 | 1238 | 286 |
| 4 | 허리가 자주 아파. | SUCCESS | 571 | 76.5 | 1504 | 466 |
| 5 | 헬스장은 부담스럽고 집에서 할 수 있는 거 좋아. | EMPTY | 0 | 98.7 | 1845 | 640 |
| 6 | 시간은 평일 저녁 30분 정도밖에 못 내. | SUCCESS | 306 | 21.4 | 1934 | 722 |
| 7 | 식단도 신경 쓰고 싶은데 요리는 잘 못해. | EMPTY | 0 | 98.9 | 2292 | 908 |
| 8 | 위 정보 다 종합해서 내 페르소나 한 단락으로 정리해줘. | EMPTY | 0 | 98.8 | 1901 | 986 |

### PER-MT-105 (persona / parent_kid_education)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 우리 아이 학습 도움 받고 싶어요. | SUCCESS | 186 | 42.0 | 543 | 0 |
| 2 | 초등학교 3학년 딸이에요. | SUCCESS | 234 | 28.7 | 906 | 182 |
| 3 | 수학을 어려워해요. 특히 분수 부분. | SUCCESS | 489 | 83.4 | 1337 | 359 |
| 4 | 책 읽는 건 좋아하는데 혼자만 하려고 해요. | EMPTY | 0 | 98.9 | 1825 | 542 |
| 5 | 위 정보로 우리 아이 학습 페르소나 정리해주세요. | EMPTY | 0 | 99.7 | 1917 | 621 |

### MTN-MT-101 (multiturn / intent_repair)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 저녁 메뉴 추천해줘. | SUCCESS | 347 | 41.8 | 495 | 0 |
| 2 | 한식 말고. | SUCCESS | 252 | 43.7 | 1001 | 174 |
| 3 | 아 미안, 한식도 괜찮아. 단 너무 매운 건 빼고. | EMPTY | 0 | 100.5 | 1451 | 344 |
| 4 | 내가 처음에 뭘 부탁했지? | EMPTY | 0 | 100.5 | 1537 | 427 |

### MTN-MT-102 (multiturn / tone_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 한국 여행 정보 부탁드립니다. | SUCCESS | 362 | 42.6 | 507 | 0 |
| 2 | 정중하게 안내해주세요. 저는 외국인이에요. | SUCCESS | 366 | 31.8 | 1053 | 186 |
| 3 | 경주 추천 받고 싶어요. | EMPTY | 0 | 100.4 | 1609 | 373 |
| 4 | 이제 친구처럼 편하게 말해줘. 반말로. | EMPTY | 0 | 100.3 | 1675 | 441 |
| 5 | 거기서 뭘 봐야 돼? | EMPTY | 0 | 100.3 | 1406 | 517 |
| 6 | 다시 정중하게 돌아가 주세요. 격식체로요. | SUCCESS | 324 | 58.7 | 1472 | 583 |
| 7 | 위에서 추천한 곳들 격식체로 한 줄씩 다시 정리해 주세요. | EMPTY | 0 | 100.4 | 1646 | 770 |

### MTN-MT-103 (multiturn / reference_tracking)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 무릎 통증 때문에 병원 두 곳 알아봤어요. 정형외과랑 한의원. | SUCCESS | 381 | 63.3 | 518 | 0 |
| 2 | 거기 둘 중 70대한테 더 맞는 곳은? | SUCCESS | 265 | 36.5 | 1095 | 197 |
| 3 | 그 곳 보험 적용돼요? | SUCCESS | 167 | 40.3 | 1556 | 381 |
| 4 | 거기 가는 길에 약국도 들를 수 있나요? | SUCCESS | 81 | 48.2 | 1509 | 557 |
| 5 | 처음에 비교한 두 군데 이름 다시 말해줘요. | EMPTY | 0 | 100.2 | 1455 | 684 |

### MTN-MT-104 (multiturn / topic_switch_return)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 회의록 정리하는 법 알려줘. | SUCCESS | 485 | 61.1 | 499 | 0 |
| 2 | 가장 효과적인 방법은? | SUCCESS | 133 | 36.2 | 1149 | 177 |
| 3 | 잠깐, 다른 거 물어봐도 돼? 노션이랑 옵시디언 차이가 뭐야? | SUCCESS | 651 | 68.2 | 1485 | 346 |
| 4 | 둘 중 회의록에 더 적합한 건? | SUCCESS | 302 | 50.5 | 1704 | 543 |
| 5 | 가격은 어떻게 돼? | SUCCESS | 91 | 18.2 | 2050 | 724 |
| 6 | 아까 회의록 얘기로 돌아가서, 두 번째로 효과적인 정리 방법은? | EMPTY | 0 | 98.7 | 1767 | 849 |
| 7 | 그 방법 단점도 알려줘. | REPETITION_LOOP | 1096 | 98.7 | 1853 | 939 |
| 8 | 우리가 회의록 얘기 하다가 잠깐 뭐로 빠졌었지? | EMPTY | 0 | 99.0 | 2246 | 1116 |

### MTN-MT-105 (multiturn / constraint_accumulation)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 정착할 때 신청해야 하는 지원금 알려주세요. | SUCCESS | 311 | 62.6 | 511 | 0 |
| 2 | 정확히 3가지만. | SUCCESS | 126 | 30.8 | 1000 | 190 |
| 3 | 각 항목 옆에 신청 기관도 같이. | EMPTY | 0 | 98.6 | 1303 | 349 |
| 4 | 각 항목 30자 이내로 짧게. | EMPTY | 0 | 98.6 | 1365 | 422 |
| 5 | 마지막은 새터민이 가장 먼저 알아야 할 순서로 정렬해주세요. | EMPTY | 0 | 98.7 | 1160 | 493 |
| 6 | 위 모든 제약 다 지켜서 최종본만 출력. | ITEM_COUNT_MISMATCH(expected=3,got=0) | 126 | 51.6 | 1261 | 581 |

### FRN-MT-101 (foreigner_lang / beginner_restaurant)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 잘 못해요. 천천히 쉽게 말해주세요. | SUCCESS | 161 | 35.0 | 530 | 0 |
| 2 | 식당에서 주문하고 싶어요. 어떻게 말해요? | SUCCESS | 171 | 34.3 | 880 | 187 |
| 3 | "이거 주세요" 무엇이에요? | EMPTY | 0 | 98.6 | 1253 | 374 |
| 4 | 매운 거 싫어요. 어떻게 말해요? | EMPTY | 0 | 98.6 | 1317 | 444 |
| 5 | 지금까지 얘기 다시. 짧게. 쉬운 단어만. | SUCCESS | 210 | 40.7 | 1254 | 517 |

### FRN-MT-102 (foreigner_lang / code_switching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. I'm learning Korean. | SUCCESS | 246 | 45.5 | 533 | 0 |
| 2 | "처마" 무슨 뜻이에요? Is it about the roof? | VOCAB_MISMATCH(no_english_terms) | 154 | 35.1 | 983 | 190 |
| 3 | 한옥 설명해주세요. 어려우면 영어 단어 쓰셔도 돼요. | EMPTY | 0 | 98.6 | 1365 | 389 |
| 4 | 한옥 보러 가고 싶어요. 어디 가요? | VOCAB_MISMATCH(no_english_terms) | 225 | 42.1 | 1442 | 473 |
| 5 | 입장료 비싸요? | VOCAB_MISMATCH(no_english_terms) | 218 | 41.2 | 1580 | 657 |
| 6 | 위 내용 다시 정리. Korean first, then English s… | EMPTY | 0 | 98.7 | 1834 | 829 |

### FRN-MT-103 (foreigner_lang / english_to_korean_teaching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | Hi! Can you help me practice Korean? | VOCAB_MISMATCH(no_romanization;not_trilingual) | 67 | 35.9 | 542 | 0 |
| 2 | I want to order food in Korean. Teach me… | VOCAB_MISMATCH(no_romanization;not_trilingual) | 316 | 43.7 | 769 | 125 |
| 3 | How do I say "no spicy please"? | SUCCESS | 276 | 37.9 | 1333 | 344 |
| 4 | 한국어로 다시 말해주세요. 천천히. | EMPTY | 0 | 98.6 | 1716 | 538 |
| 5 | 발음도 알려줘요. 로마자로요. | EMPTY | 0 | 98.6 | 1751 | 612 |
| 6 | "감사합니다" 발음도 알려주세요. | VOCAB_MISMATCH(not_trilingual) | 160 | 11.2 | 1526 | 683 |
| 7 | 위 표현 5개 정리. 한국어 + 로마자 발음 + 영어 의미 형식으로. | SUCCESS | 48 | 21.2 | 1603 | 865 |

### FRN-MT-104 (foreigner_lang / avoid_hanja_hospital)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 공부해요. 한자어 어려워요. 병원 갈 때 쉬운 말로 알려주세요. | SUCCESS | 980 | 98.5 | 545 | 0 |
| 2 | "감기" 같은 단어 말고 다른 쉬운 말로 증상 설명하는 법. | EMPTY | 0 | 98.7 | 1260 | 201 |
| 3 | 병원에서 접수하는 법 쉽게 알려주세요. | EMPTY | 0 | 98.7 | 1369 | 289 |
| 4 | 지금까지 다 정리해주세요. 한자어 0개로. | EMPTY | 0 | 98.7 | 1468 | 365 |

### FRN-MT-105 (foreigner_lang / register_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 책으로 공부했어요. 너무 formal해요. | VOCAB_MISMATCH(uses_formal_register) | 62 | 40.4 | 533 | 0 |
| 2 | 친구한테 쓸 말 알려주세요. 평어/반말로요. | SUCCESS | 194 | 39.3 | 712 | 112 |
| 3 | "안녕하세요" → 친구한테는 어떻게 말해요? "감사합니다"는요? | SUCCESS | 980 | 98.8 | 1120 | 299 |
| 4 | 카페에서 음료 주문할 때 일상적인 말투로. | EMPTY | 0 | 99.8 | 1752 | 497 |
| 5 | 위 전부 다시. 친구한테 말하는 말투로. | EMPTY | 0 | 99.7 | 1828 | 575 |

### REC-MT-101 (recommendation / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 박물관 가보고 싶어요. 어디가 좋을까요? | SUCCESS | 115 | 38.3 | 540 | 0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | 115 | 58.2 | 822 | 163 |
| 3 | 한국어는 일상 회화 정도예요. | EMPTY | 0 | 99.5 | 1115 | 325 |
| 4 | 한국 역사 잘 몰라요. | EMPTY | 0 | 99.0 | 1173 | 396 |
| 5 | 그림이나 도자기 좋아해요. | SUCCESS | 180 | 47.9 | 1139 | 463 |
| 6 | 8살 딸이랑 같이 가요. | EMPTY | 0 | 99.0 | 1372 | 641 |
| 7 | 너무 길거나 어려운 곳 말고요. | SUCCESS | 180 | 46.1 | 1441 | 709 |
| 8 | 위 정보 다 반영해서 박물관 3곳 추천 + 각각 이유. | EMPTY | 0 | 99.2 | 1806 | 890 |

### REC-MT-102 (recommendation / defector_settlement_program)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 정착 프로그램 추천해주세요. | SUCCESS | 193 | 36.1 | 533 | 0 |
| 2 | 50대 여자, 평양 출신이에요. 작년에 한국 왔어요. | SUCCESS | 350 | 53.1 | 916 | 180 |
| 3 | 혼자 살고 있어요. | EMPTY | 0 | 99.2 | 1467 | 373 |
| 4 | 장사 해보고 싶어요. 컴퓨터는 약해요. | EMPTY | 0 | 99.3 | 1535 | 438 |
| 5 | 서울에 살아요. | SUCCESS | 358 | 50.0 | 1426 | 514 |
| 6 | 너무 빨리 진행되는 건 따라가기 힘들어요. | EMPTY | 0 | 99.2 | 1601 | 685 |
| 7 | 위 조건 다 반영해서 정착 지원 프로그램 3개 추천 + 이유. | EMPTY | 0 | 99.3 | 1703 | 763 |

### REC-MT-103 (recommendation / elderly_culture_event)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 우리 동네 문화행사 추천 좀 해주세요. | SUCCESS | 671 | 73.1 | 536 | 0 |
| 2 | 75살이에요. 무릎이 안 좋아요. | SUCCESS | 631 | 93.8 | 1219 | 184 |
| 3 | 큰 글씨, 큰 화면이면 좋아요. | SUCCESS | 221 | 46.7 | 1918 | 366 |
| 4 | 가곡이나 옛날 노래 좋아해요. | SUCCESS | 509 | 59.6 | 1807 | 547 |
| 5 | 친구 사귈 수 있는 곳이면 더 좋고요. | EMPTY | 0 | 99.3 | 1989 | 726 |
| 6 | 위 조건 다 반영해서 행사 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=가곡) | 531 | 79.3 | 2074 | 802 |

### REC-MT-104 (recommendation / office_worker_fitness_diet)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 운동 루틴이랑 식단 추천해줘. | SUCCESS | 352 | 48.3 | 531 | 0 |
| 2 | 32살 사무직, 허리가 자주 아파. | EMPTY | 0 | 98.7 | 1059 | 179 |
| 3 | 집에서 할 수 있는 거 위주. | EMPTY | 0 | 98.7 | 1149 | 253 |
| 4 | 평일 저녁 30분. | SUCCESS | 673 | 80.9 | 1230 | 324 |
| 5 | 요리 잘 못해. | EMPTY | 0 | 98.7 | 1547 | 498 |
| 6 | 위 정보로 1주 운동 + 식단 표로 추천해줘. | EMPTY | 0 | 98.7 | 1616 | 561 |

### REC-MT-105 (recommendation / student_learning_resource)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 학습 자료 추천해줘. | SUCCESS | 63 | 31.5 | 526 | 0 |
| 2 | 정보 부족하면 먼저 질문해줘. | CLARIFY_SKIPPED(no_question_or_dumped_list) | 63 | 29.6 | 683 | 97 |
| 3 | 컴퓨터공학 전공 3학년이야. | SUCCESS | 416 | 58.9 | 864 | 200 |
| 4 | 머신러닝 기초 공부하고 싶어. | EMPTY | 0 | 98.7 | 1399 | 379 |
| 5 | 한국어 자료가 더 편해. 영어도 가능은 함. | SUCCESS | 574 | 45.1 | 1478 | 450 |
| 6 | 책보단 무료 강의가 좋아. | EMPTY | 0 | 98.7 | 2102 | 638 |
| 7 | 수학 백그라운드는 미적분/선형대수 학부 수준. | EMPTY | 0 | 98.8 | 1782 | 707 |
| 8 | 위 정보로 학습 자료 3개 추천 + 각각 이유. | RECOMMENDATION_GENERIC(missing=3학년) | 189 | 39.2 | 1872 | 787 |
