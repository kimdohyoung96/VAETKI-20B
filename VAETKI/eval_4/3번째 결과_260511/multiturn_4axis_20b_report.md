# 4축 평가 결과

## 1. 전체 요약

- 세션 수: 20
- 총 turn: 123
- 성공 turn: 66 (53.7%)
- 성공 latency 중앙값: 43.1s
- 실패 latency 중앙값: 95.2s

## 2. 트랙별 성공률

| 트랙 | 성공/전체 | 성공률 |
|---|---|---|
| persona | 20/31 | 64.5% |
| multiturn | 18/30 | 60.0% |
| foreigner_lang | 12/27 | 44.4% |
| recommendation | 16/35 | 45.7% |

## 3. Summary Memory / Context 진단

- prompt chars 중앙값: 1420
- prompt chars 최대값: 2315
- memory chars 중앙값: 409
- memory chars 최대값: 1016
- raw output chars 중앙값: 574
- raw output chars 최대값: 1587
- clean output chars 중앙값: 161
- clean output chars 최대값: 919

## 4. 실패 유형 분포

### 4.1 일반 실패

| 유형 | 개수 |
|---|---|
| EMPTY | 40 |
| THINK_RUNAWAY | 4 |
| REPETITION_LOOP | 2 |

### 4.2 4축 특화 실패 (generic=SUCCESS이지만 트랙 기준 미충족)

| 유형 | 개수 |
|---|---|
| VOCAB_MISMATCH | 7 |
| RECOMMENDATION_GENERIC | 2 |
| PERSONA_RECALL_FAIL | 1 |
| CLARIFY_SKIPPED | 1 |

## 5. 세션별 turn 결과

### PER-MT-101 (persona / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 박물관 가이드 도움 받고 싶어요. | SUCCESS | 77 | 28.2 | 549 | 0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | 101 | 20.7 | 755 | 125 |
| 3 | 한국어는 일상 회화 정도만 가능해요. | SUCCESS | 92 | 23.8 | 1024 | 273 |
| 4 | 한국 역사 잘 몰라요. 조선시대 이런 거 들어본 적 없어요. | SUCCESS | 106 | 35.2 | 1183 | 409 |
| 5 | 그림이나 도자기 같은 거 보는 거 좋아해요. | SUCCESS | 603 | 66.8 | 1352 | 572 |
| 6 | 8살 딸이랑 같이 가요. 짧게 보고 싶어요. | EMPTY | 0 | 95.2 | 1951 | 759 |
| 7 | 위 정보 종합해서 저랑 딸의 관람 페르소나 한 단락으로 정리해주세요. | EMPTY | 0 | 95.2 | 2035 | 838 |

### PER-MT-102 (persona / defector_settlement)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 도움 받고 싶어서요. | SUCCESS | 72 | 15.2 | 542 | 0 |
| 2 | 작년에 한국 왔어요. 50대 여자입니다. | SUCCESS | 176 | 28.4 | 730 | 113 |
| 3 | 혼자 살고 있어요. 평양 출신이에요. | SUCCESS | 191 | 33.4 | 1112 | 299 |
| 4 | 장사 좀 해보고 싶은데 한국 시스템을 잘 몰라요. 컴퓨터도 약해요. | SUCCESS | 176 | 50.3 | 1433 | 482 |
| 5 | 위 정보로 제 상황 한 단락으로 정리해주세요. | SUCCESS | 191 | 34.8 | 1637 | 683 |

### PER-MT-103 (persona / elderly_culture)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 우리 동네 문화센터 어떻게 다닐지 좀 알려줘요. | SUCCESS | 309 | 42.0 | 557 | 0 |
| 2 | 75살이고 무릎이 안 좋아서 멀리는 못 다녀요. | SUCCESS | 919 | 90.5 | 1065 | 196 |
| 3 | 글씨 작은 건 잘 안 보여요. 큰 글씨로 부탁해요. | EMPTY | 0 | 95.1 | 1783 | 386 |
| 4 | 옛날에 노래 부르는 거 좋아했어요. 가곡 같은 거. | EMPTY | 0 | 95.2 | 1861 | 469 |
| 5 | 친구 사귀고 싶어요. 혼자 너무 적적해요. | EMPTY | 0 | 94.9 | 1662 | 552 |
| 6 | 위 정보로 제 페르소나 정리해주세요. | PERSONA_RECALL_FAIL(missing=가곡,혼자) | 484 | 66.1 | 1734 | 630 |

### PER-MT-104 (persona / office_worker_fitness)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 운동 좀 시작하려고. | SUCCESS | 244 | 32.0 | 535 | 0 |
| 2 | 32살 직장인이고 사무실에서 하루 종일 앉아 있어. | SUCCESS | 431 | 57.3 | 958 | 173 |
| 3 | 키 175, 몸무게 82kg. | SUCCESS | 476 | 61.3 | 1594 | 365 |
| 4 | 허리가 자주 아파. | EMPTY | 0 | 94.9 | 2003 | 544 |
| 5 | 헬스장은 부담스럽고 집에서 할 수 있는 거 좋아. | SUCCESS | 482 | 65.9 | 2067 | 609 |
| 6 | 시간은 평일 저녁 30분 정도밖에 못 내. | EMPTY | 0 | 95.1 | 2315 | 800 |
| 7 | 식단도 신경 쓰고 싶은데 요리는 잘 못해. | EMPTY | 0 | 94.9 | 1944 | 878 |
| 8 | 위 정보 다 종합해서 내 페르소나 한 단락으로 정리해줘. | EMPTY | 0 | 94.9 | 2043 | 956 |

### PER-MT-105 (persona / parent_kid_education)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 우리 아이 학습 도움 받고 싶어요. | SUCCESS | 167 | 26.6 | 543 | 0 |
| 2 | 초등학교 3학년 딸이에요. | SUCCESS | 272 | 46.8 | 886 | 182 |
| 3 | 수학을 어려워해요. 특히 분수 부분. | SUCCESS | 375 | 70.4 | 1354 | 360 |
| 4 | 책 읽는 건 좋아하는데 혼자만 하려고 해요. | SUCCESS | 272 | 40.4 | 1748 | 543 |
| 5 | 위 정보로 우리 아이 학습 페르소나 정리해주세요. | EMPTY | 0 | 95.3 | 1950 | 730 |

### MTN-MT-101 (multiturn / intent_repair)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 저녁 메뉴 추천해줘. | SUCCESS | 180 | 30.5 | 495 | 0 |
| 2 | 한식 말고. | REPETITION_LOOP | 1518 | 95.2 | 835 | 174 |
| 3 | 아 미안, 한식도 괜찮아. 단 너무 매운 건 빼고. | THINK_RUNAWAY | 1477 | 95.1 | 924 | 235 |
| 4 | 내가 처음에 뭘 부탁했지? | SUCCESS | 179 | 46.5 | 1021 | 318 |

### MTN-MT-102 (multiturn / tone_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 한국 여행 정보 부탁드립니다. | SUCCESS | 234 | 32.3 | 507 | 0 |
| 2 | 정중하게 안내해주세요. 저는 외국인이에요. | SUCCESS | 362 | 43.8 | 927 | 185 |
| 3 | 경주 추천 받고 싶어요. | SUCCESS | 385 | 57.1 | 1486 | 372 |
| 4 | 이제 친구처럼 편하게 말해줘. 반말로. | EMPTY | 0 | 95.1 | 1813 | 549 |
| 5 | 거기서 뭘 봐야 돼? | EMPTY | 0 | 95.3 | 1877 | 625 |
| 6 | 다시 정중하게 돌아가 주세요. 격식체로요. | SUCCESS | 383 | 51.7 | 1607 | 691 |
| 7 | 위에서 추천한 곳들 격식체로 한 줄씩 다시 정리해 주세요. | EMPTY | 0 | 95.2 | 1813 | 878 |

### MTN-MT-103 (multiturn / reference_tracking)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 무릎 통증 때문에 병원 두 곳 알아봤어요. 정형외과랑 한의원. | SUCCESS | 301 | 54.4 | 518 | 0 |
| 2 | 거기 둘 중 70대한테 더 맞는 곳은? | SUCCESS | 299 | 42.6 | 1016 | 197 |
| 3 | 그 곳 보험 적용돼요? | SUCCESS | 472 | 53.3 | 1512 | 382 |
| 4 | 거기 가는 길에 약국도 들를 수 있나요? | EMPTY | 0 | 95.3 | 1848 | 558 |
| 5 | 처음에 비교한 두 군데 이름 다시 말해줘요. | EMPTY | 0 | 95.4 | 1928 | 635 |

### MTN-MT-104 (multiturn / topic_switch_return)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 회의록 정리하는 법 알려줘. | SUCCESS | 347 | 49.2 | 499 | 0 |
| 2 | 가장 효과적인 방법은? | SUCCESS | 109 | 24.7 | 1015 | 178 |
| 3 | 잠깐, 다른 거 물어봐도 돼? 노션이랑 옵시디언 차이가 뭐야? | SUCCESS | 381 | 46.2 | 1303 | 323 |
| 4 | 둘 중 회의록에 더 적합한 건? | SUCCESS | 123 | 28.4 | 1536 | 521 |
| 5 | 가격은 어떻게 돼? | EMPTY | 0 | 95.1 | 1712 | 685 |
| 6 | 아까 회의록 얘기로 돌아가서, 두 번째로 효과적인 정리 방법은? | EMPTY | 0 | 114.1 | 1778 | 750 |
| 7 | 그 방법 단점도 알려줘. | SUCCESS | 183 | 43.6 | 1503 | 840 |
| 8 | 우리가 회의록 얘기 하다가 잠깐 뭐로 빠졌었지? | EMPTY | 0 | 95.1 | 1748 | 1016 |

### MTN-MT-105 (multiturn / constraint_accumulation)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 정착할 때 신청해야 하는 지원금 알려주세요. | SUCCESS | 356 | 62.3 | 511 | 0 |
| 2 | 정확히 3가지만. | SUCCESS | 143 | 31.4 | 1032 | 190 |
| 3 | 각 항목 옆에 신청 기관도 같이. | SUCCESS | 87 | 26.6 | 1366 | 363 |
| 4 | 각 항목 30자 이내로 짧게. | SUCCESS | 87 | 28.2 | 1230 | 492 |
| 5 | 마지막은 새터민이 가장 먼저 알아야 할 순서로 정렬해주세요. | EMPTY | 0 | 95.2 | 1325 | 619 |
| 6 | 위 모든 제약 다 지켜서 최종본만 출력. | EMPTY | 0 | 95.2 | 1417 | 707 |

### FRN-MT-101 (foreigner_lang / beginner_restaurant)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 잘 못해요. 천천히 쉽게 말해주세요. | SUCCESS | 250 | 38.2 | 530 | 0 |
| 2 | 식당에서 주문하고 싶어요. 어떻게 말해요? | SUCCESS | 199 | 34.3 | 969 | 187 |
| 3 | "이거 주세요" 무엇이에요? | VOCAB_MISMATCH(long_sentences=2) | 185 | 42.2 | 1370 | 374 |
| 4 | 매운 거 싫어요. 어떻게 말해요? | SUCCESS | 193 | 45.6 | 1478 | 553 |
| 5 | 지금까지 얘기 다시. 짧게. 쉬운 단어만. | EMPTY | 0 | 95.2 | 1645 | 734 |

### FRN-MT-102 (foreigner_lang / code_switching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. I'm learning Korean. | SUCCESS | 268 | 36.9 | 533 | 0 |
| 2 | "처마" 무슨 뜻이에요? Is it about the roof? | VOCAB_MISMATCH(no_english_terms) | 320 | 57.2 | 1001 | 190 |
| 3 | 한옥 설명해주세요. 어려우면 영어 단어 쓰셔도 돼요. | VOCAB_MISMATCH(no_english_terms) | 195 | 39.4 | 1546 | 389 |
| 4 | 한옥 보러 가고 싶어요. 어디 가요? | EMPTY | 0 | 95.2 | 1664 | 581 |
| 5 | 입장료 비싸요? | EMPTY | 0 | 95.2 | 1712 | 656 |
| 6 | 위 내용 다시 정리. Korean first, then English s… | VOCAB_MISMATCH(no_english_terms) | 652 | 85.3 | 1505 | 719 |

### FRN-MT-103 (foreigner_lang / english_to_korean_teaching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | Hi! Can you help me practice Korean? | VOCAB_MISMATCH(no_romanization;not_trilingual) | 291 | 38.5 | 542 | 0 |
| 2 | I want to order food in Korean. Teach me… | SUCCESS | 295 | 40.5 | 1067 | 199 |
| 3 | How do I say "no spicy please"? | THINK_RUNAWAY | 1368 | 95.3 | 1610 | 418 |
| 4 | 한국어로 다시 말해주세요. 천천히. | SUCCESS | 316 | 44.9 | 1679 | 504 |
| 5 | 발음도 알려줘요. 로마자로요. | THINK_RUNAWAY | 1515 | 95.3 | 1843 | 687 |
| 6 | "감사합니다" 발음도 알려주세요. | EMPTY | 0 | 95.3 | 1639 | 758 |
| 7 | 위 표현 5개 정리. 한국어 + 로마자 발음 + 영어 의미 형식으로. | SUCCESS | 325 | 38.2 | 1719 | 831 |

### FRN-MT-104 (foreigner_lang / avoid_hanja_hospital)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 공부해요. 한자어 어려워요. 병원 갈 때 쉬운 말로 알려주세요. | SUCCESS | 173 | 37.2 | 545 | 0 |
| 2 | "감기" 같은 단어 말고 다른 쉬운 말로 증상 설명하는 법. | SUCCESS | 76 | 45.3 | 933 | 202 |
| 3 | 병원에서 접수하는 법 쉽게 알려주세요. | SUCCESS | 161 | 39.7 | 1163 | 335 |
| 4 | 지금까지 다 정리해주세요. 한자어 0개로. | SUCCESS | 161 | 35.8 | 1320 | 519 |

### FRN-MT-105 (foreigner_lang / register_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 책으로 공부했어요. 너무 formal해요. | SUCCESS | 225 | 54.4 | 533 | 0 |
| 2 | 친구한테 쓸 말 알려주세요. 평어/반말로요. | REPETITION_LOOP | 1586 | 96.0 | 948 | 189 |
| 3 | "안녕하세요" → 친구한테는 어떻게 말해요? "감사합니다"는요? | VOCAB_MISMATCH(uses_formal_register) | 264 | 55.5 | 1062 | 268 |
| 4 | 카페에서 음료 주문할 때 일상적인 말투로. | EMPTY | 0 | 96.1 | 1520 | 467 |
| 5 | 위 전부 다시. 친구한테 말하는 말투로. | VOCAB_MISMATCH(uses_formal_register) | 263 | 44.1 | 1399 | 545 |

### REC-MT-101 (recommendation / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 박물관 가보고 싶어요. 어디가 좋을까요? | SUCCESS | 107 | 32.9 | 540 | 0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | 107 | 30.6 | 806 | 155 |
| 3 | 한국어는 일상 회화 정도예요. | EMPTY | 0 | 96.0 | 1083 | 309 |
| 4 | 한국 역사 잘 몰라요. | EMPTY | 0 | 95.9 | 1141 | 380 |
| 5 | 그림이나 도자기 좋아해요. | EMPTY | 0 | 95.9 | 1115 | 447 |
| 6 | 8살 딸이랑 같이 가요. | SUCCESS | 223 | 45.1 | 1174 | 516 |
| 7 | 너무 길거나 어려운 곳 말고요. | SUCCESS | 125 | 20.4 | 1468 | 693 |
| 8 | 위 정보 다 반영해서 박물관 3곳 추천 + 각각 이유. | EMPTY | 0 | 96.0 | 1763 | 859 |

### REC-MT-102 (recommendation / defector_settlement_program)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 정착 프로그램 추천해주세요. | SUCCESS | 238 | 48.8 | 533 | 0 |
| 2 | 50대 여자, 평양 출신이에요. 작년에 한국 왔어요. | SUCCESS | 256 | 48.6 | 961 | 180 |
| 3 | 혼자 살고 있어요. | EMPTY | 0 | 95.9 | 1420 | 373 |
| 4 | 장사 해보고 싶어요. 컴퓨터는 약해요. | SUCCESS | 559 | 58.5 | 1488 | 438 |
| 5 | 서울에 살아요. | SUCCESS | 206 | 23.4 | 1914 | 623 |
| 6 | 너무 빨리 진행되는 건 따라가기 힘들어요. | EMPTY | 0 | 95.9 | 2049 | 795 |
| 7 | 위 조건 다 반영해서 정착 지원 프로그램 3개 추천 + 이유. | EMPTY | 0 | 95.9 | 2140 | 873 |

### REC-MT-103 (recommendation / elderly_culture_event)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 우리 동네 문화행사 추천 좀 해주세요. | SUCCESS | 301 | 46.0 | 536 | 0 |
| 2 | 75살이에요. 무릎이 안 좋아요. | SUCCESS | 443 | 70.0 | 1015 | 183 |
| 3 | 큰 글씨, 큰 화면이면 좋아요. | EMPTY | 0 | 96.1 | 1652 | 364 |
| 4 | 가곡이나 옛날 노래 좋아해요. | SUCCESS | 329 | 47.1 | 1719 | 436 |
| 5 | 친구 사귈 수 있는 곳이면 더 좋고요. | EMPTY | 0 | 96.1 | 1934 | 616 |
| 6 | 위 조건 다 반영해서 행사 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=75) | 350 | 52.2 | 1597 | 692 |

### REC-MT-104 (recommendation / office_worker_fitness_diet)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 운동 루틴이랑 식단 추천해줘. | SUCCESS | 323 | 39.2 | 531 | 0 |
| 2 | 32살 사무직, 허리가 자주 아파. | SUCCESS | 388 | 58.7 | 1028 | 179 |
| 3 | 집에서 할 수 있는 거 위주. | EMPTY | 0 | 96.1 | 1613 | 362 |
| 4 | 평일 저녁 30분. | SUCCESS | 515 | 66.8 | 1678 | 433 |
| 5 | 요리 잘 못해. | EMPTY | 0 | 96.1 | 1999 | 606 |
| 6 | 위 정보로 1주 운동 + 식단 표로 추천해줘. | RECOMMENDATION_GENERIC(missing=30분) | 752 | 91.1 | 1701 | 669 |

### REC-MT-105 (recommendation / student_learning_resource)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 학습 자료 추천해줘. | SUCCESS | 530 | 75.5 | 526 | 0 |
| 2 | 정보 부족하면 먼저 질문해줘. | CLARIFY_SKIPPED(no_question_or_dumped_list) | 421 | 60.8 | 1196 | 173 |
| 3 | 컴퓨터공학 전공 3학년이야. | THINK_RUNAWAY | 1448 | 96.2 | 1812 | 353 |
| 4 | 머신러닝 기초 공부하고 싶어. | EMPTY | 0 | 96.2 | 1887 | 423 |
| 5 | 한국어 자료가 더 편해. 영어도 가능은 함. | SUCCESS | 662 | 67.4 | 1482 | 494 |
| 6 | 책보단 무료 강의가 좋아. | EMPTY | 0 | 96.1 | 1747 | 682 |
| 7 | 수학 백그라운드는 미적분/선형대수 학부 수준. | EMPTY | 0 | 96.1 | 1826 | 751 |
| 8 | 위 정보로 학습 자료 3개 추천 + 각각 이유. | EMPTY | 0 | 96.2 | 1916 | 831 |
