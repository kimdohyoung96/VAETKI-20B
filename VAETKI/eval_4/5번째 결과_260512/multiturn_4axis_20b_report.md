# 4축 평가 결과 (think 모드)

## 1. 전체 요약

- 세션 수: 20
- 총 turn: 123
- 성공 turn: 54 (43.9%)
- 성공 latency 중앙값: 39.7s
- 실패 latency 중앙값: 99.2s

## 2. 트랙별 성공률

| 트랙 | 성공/전체 | 성공률 |
|---|---|---|
| persona | 14/31 | 45.2% |
| multiturn | 21/30 | 70.0% |
| foreigner_lang | 5/27 | 18.5% |
| recommendation | 14/35 | 40.0% |

## 3. Summary Memory / Context 진단

- prompt chars 중앙값: 1335
- prompt chars 최대값: 2501
- memory chars 중앙값: 382
- memory chars 최대값: 1064
- raw output chars 중앙값: 523
- raw output chars 최대값: 1715
- clean output chars 중앙값: 92
- clean output chars 최대값: 1238

## 4. 실패 유형 분포

### 4.1 일반 실패

| 유형 | 개수 |
|---|---|
| EMPTY | 42 |
| REPETITION_LOOP | 7 |
| THINK_RUNAWAY | 5 |

### 4.2 4축 특화 실패 (generic=SUCCESS이지만 트랙 기준 미충족)

| 유형 | 개수 |
|---|---|
| VOCAB_MISMATCH | 10 |
| RECOMMENDATION_GENERIC | 3 |
| PERSONA_RECALL_FAIL | 2 |

## 5. 세션별 turn 결과

### PER-MT-101 (persona / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 박물관 가이드 도움 받고 싶어요. | REPETITION_LOOP | 1637 | 101.0 | 549 | 0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | 197 | 36.9 | 632 | 79 |
| 3 | 한국어는 일상 회화 정도만 가능해요. | SUCCESS | 202 | 46.5 | 1036 | 266 |
| 4 | 한국 역사 잘 몰라요. 조선시대 이런 거 들어본 적 없어요. | EMPTY | 0 | 100.3 | 1430 | 450 |
| 5 | 그림이나 도자기 같은 거 보는 거 좋아해요. | EMPTY | 0 | 100.3 | 1519 | 538 |
| 6 | 8살 딸이랑 같이 가요. 짧게 보고 싶어요. | EMPTY | 0 | 100.2 | 1425 | 617 |
| 7 | 위 정보 종합해서 저랑 딸의 관람 페르소나 한 단락으로 정리해주세요. | PERSONA_RECALL_FAIL(missing=베트남,2년) | 829 | 91.3 | 1522 | 696 |

### PER-MT-102 (persona / defector_settlement)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 도움 받고 싶어서요. | SUCCESS | 100 | 15.3 | 542 | 0 |
| 2 | 작년에 한국 왔어요. 50대 여자입니다. | SUCCESS | 98 | 48.1 | 782 | 139 |
| 3 | 혼자 살고 있어요. 평양 출신이에요. | SUCCESS | 98 | 40.2 | 1044 | 283 |
| 4 | 장사 좀 해보고 싶은데 한국 시스템을 잘 몰라요. 컴퓨터도 약해요. | SUCCESS | 98 | 39.2 | 1205 | 425 |
| 5 | 위 정보로 제 상황 한 단락으로 정리해주세요. | EMPTY | 0 | 110.3 | 1367 | 584 |

### PER-MT-103 (persona / elderly_culture)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 우리 동네 문화센터 어떻게 다닐지 좀 알려줘요. | SUCCESS | 246 | 32.7 | 557 | 0 |
| 2 | 75살이고 무릎이 안 좋아서 멀리는 못 다녀요. | REPETITION_LOOP | 1238 | 110.4 | 1006 | 196 |
| 3 | 글씨 작은 건 잘 안 보여요. 큰 글씨로 부탁해요. | EMPTY | 0 | 110.4 | 1723 | 386 |
| 4 | 옛날에 노래 부르는 거 좋아했어요. 가곡 같은 거. | EMPTY | 0 | 110.3 | 1801 | 469 |
| 5 | 친구 사귀고 싶어요. 혼자 너무 적적해요. | EMPTY | 0 | 110.5 | 1661 | 552 |
| 6 | 위 정보로 제 페르소나 정리해주세요. | EMPTY | 0 | 100.8 | 1733 | 630 |

### PER-MT-104 (persona / office_worker_fitness)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 운동 좀 시작하려고. | SUCCESS | 153 | 40.4 | 535 | 0 |
| 2 | 32살 직장인이고 사무실에서 하루 종일 앉아 있어. | SUCCESS | 393 | 56.0 | 870 | 174 |
| 3 | 키 175, 몸무게 82kg. | EMPTY | 0 | 100.7 | 1468 | 366 |
| 4 | 허리가 자주 아파. | EMPTY | 0 | 100.2 | 1538 | 437 |
| 5 | 헬스장은 부담스럽고 집에서 할 수 있는 거 좋아. | SUCCESS | 423 | 42.8 | 1478 | 502 |
| 6 | 시간은 평일 저녁 30분 정도밖에 못 내. | EMPTY | 0 | 100.2 | 1695 | 693 |
| 7 | 식단도 신경 쓰고 싶은데 요리는 잘 못해. | EMPTY | 0 | 102.2 | 1780 | 771 |
| 8 | 위 정보 다 종합해서 내 페르소나 한 단락으로 정리해줘. | PERSONA_RECALL_FAIL(missing=32,집) | 94 | 37.3 | 1879 | 849 |

### PER-MT-105 (persona / parent_kid_education)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 우리 아이 학습 도움 받고 싶어요. | SUCCESS | 139 | 37.5 | 543 | 0 |
| 2 | 초등학교 3학년 딸이에요. | SUCCESS | 135 | 34.3 | 858 | 181 |
| 3 | 수학을 어려워해요. 특히 분수 부분. | SUCCESS | 215 | 40.4 | 1186 | 354 |
| 4 | 책 읽는 건 좋아하는데 혼자만 하려고 해요. | SUCCESS | 392 | 100.2 | 1451 | 538 |
| 5 | 위 정보로 우리 아이 학습 페르소나 정리해주세요. | EMPTY | 0 | 100.3 | 1907 | 726 |

### MTN-MT-101 (multiturn / intent_repair)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 저녁 메뉴 추천해줘. | SUCCESS | 271 | 49.7 | 495 | 0 |
| 2 | 한식 말고. | SUCCESS | 115 | 7.8 | 919 | 174 |
| 3 | 아 미안, 한식도 괜찮아. 단 너무 매운 건 빼고. | SUCCESS | 263 | 37.4 | 1207 | 319 |
| 4 | 내가 처음에 뭘 부탁했지? | EMPTY | 0 | 98.6 | 1402 | 511 |

### MTN-MT-102 (multiturn / tone_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 한국 여행 정보 부탁드립니다. | SUCCESS | 348 | 38.6 | 507 | 0 |
| 2 | 정중하게 안내해주세요. 저는 외국인이에요. | SUCCESS | 345 | 46.6 | 1042 | 186 |
| 3 | 경주 추천 받고 싶어요. | SUCCESS | 303 | 46.8 | 1587 | 373 |
| 4 | 이제 친구처럼 편하게 말해줘. 반말로. | EMPTY | 0 | 98.6 | 1720 | 550 |
| 5 | 거기서 뭘 봐야 돼? | EMPTY | 0 | 100.2 | 1784 | 626 |
| 6 | 다시 정중하게 돌아가 주세요. 격식체로요. | EMPTY | 0 | 100.2 | 1528 | 692 |
| 7 | 위에서 추천한 곳들 격식체로 한 줄씩 다시 정리해 주세요. | EMPTY | 0 | 100.3 | 1625 | 770 |

### MTN-MT-103 (multiturn / reference_tracking)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 무릎 통증 때문에 병원 두 곳 알아봤어요. 정형외과랑 한의원. | SUCCESS | 324 | 59.5 | 518 | 0 |
| 2 | 거기 둘 중 70대한테 더 맞는 곳은? | SUCCESS | 234 | 51.1 | 1038 | 197 |
| 3 | 그 곳 보험 적용돼요? | SUCCESS | 103 | 29.0 | 1469 | 382 |
| 4 | 거기 가는 길에 약국도 들를 수 있나요? | SUCCESS | 71 | 23.1 | 1378 | 521 |
| 5 | 처음에 비교한 두 군데 이름 다시 말해줘요. | SUCCESS | 13 | 22.4 | 1335 | 638 |

### MTN-MT-104 (multiturn / topic_switch_return)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 회의록 정리하는 법 알려줘. | SUCCESS | 348 | 48.8 | 499 | 0 |
| 2 | 가장 효과적인 방법은? | SUCCESS | 147 | 30.5 | 1016 | 178 |
| 3 | 잠깐, 다른 거 물어봐도 돼? 노션이랑 옵시디언 차이가 뭐야? | SUCCESS | 230 | 58.3 | 1373 | 354 |
| 4 | 둘 중 회의록에 더 적합한 건? | EMPTY | 0 | 100.1 | 1457 | 552 |
| 5 | 가격은 어떻게 돼? | SUCCESS | 386 | 27.1 | 1527 | 624 |
| 6 | 아까 회의록 얘기로 돌아가서, 두 번째로 효과적인 정리 방법은? | SUCCESS | 228 | 38.5 | 1935 | 797 |
| 7 | 그 방법 단점도 알려줘. | EMPTY | 0 | 100.1 | 2128 | 996 |
| 8 | 우리가 회의록 얘기 하다가 잠깐 뭐로 빠졌었지? | SUCCESS | 254 | 15.8 | 2212 | 1064 |

### MTN-MT-105 (multiturn / constraint_accumulation)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 정착할 때 신청해야 하는 지원금 알려주세요. | SUCCESS | 181 | 53.3 | 511 | 0 |
| 2 | 정확히 3가지만. | SUCCESS | 23 | 11.1 | 871 | 190 |
| 3 | 각 항목 옆에 신청 기관도 같이. | THINK_RUNAWAY | 1362 | 100.0 | 968 | 246 |
| 4 | 각 항목 30자 이내로 짧게. | SUCCESS | 39 | 17.6 | 1030 | 319 |
| 5 | 마지막은 새터민이 가장 먼저 알아야 할 순서로 정렬해주세요. | SUCCESS | 39 | 29.7 | 992 | 398 |
| 6 | 위 모든 제약 다 지켜서 최종본만 출력. | EMPTY | 0 | 99.6 | 1108 | 494 |

### FRN-MT-101 (foreigner_lang / beginner_restaurant)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 잘 못해요. 천천히 쉽게 말해주세요. | REPETITION_LOOP | 1530 | 98.7 | 530 | 0 |
| 2 | 식당에서 주문하고 싶어요. 어떻게 말해요? | THINK_RUNAWAY | 1126 | 98.7 | 612 | 78 |
| 3 | "이거 주세요" 무엇이에요? | THINK_RUNAWAY | 1381 | 98.8 | 705 | 156 |
| 4 | 매운 거 싫어요. 어떻게 말해요? | SUCCESS | 92 | 25.2 | 793 | 226 |
| 5 | 지금까지 얘기 다시. 짧게. 쉬운 단어만. | SUCCESS | 92 | 36.3 | 1018 | 360 |

### FRN-MT-102 (foreigner_lang / code_switching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. I'm learning Korean. | VOCAB_MISMATCH(no_english_terms) | 23 | 33.1 | 533 | 0 |
| 2 | "처마" 무슨 뜻이에요? Is it about the roof? | VOCAB_MISMATCH(no_english_terms) | 133 | 17.1 | 645 | 73 |
| 3 | 한옥 설명해주세요. 어려우면 영어 단어 쓰셔도 돼요. | REPETITION_LOOP | 183 | 98.7 | 999 | 265 |
| 4 | 한옥 보러 가고 싶어요. 어디 가요? | VOCAB_MISMATCH(no_english_terms) | 204 | 46.4 | 1345 | 458 |
| 5 | 입장료 비싸요? | EMPTY | 0 | 98.8 | 1573 | 642 |
| 6 | 위 내용 다시 정리. Korean first, then English s… | EMPTY | 0 | 98.8 | 1654 | 705 |

### FRN-MT-103 (foreigner_lang / english_to_korean_teaching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | Hi! Can you help me practice Korean? | VOCAB_MISMATCH(no_romanization;not_trilingual) | 125 | 34.6 | 542 | 0 |
| 2 | I want to order food in Korean. Teach me… | SUCCESS | 401 | 38.5 | 887 | 184 |
| 3 | How do I say "no spicy please"? | EMPTY | 0 | 98.8 | 1536 | 403 |
| 4 | 한국어로 다시 말해주세요. 천천히. | VOCAB_MISMATCH(no_romanization;not_trilingual) | 120 | 46.7 | 1605 | 489 |
| 5 | 발음도 알려줘요. 로마자로요. | EMPTY | 0 | 98.8 | 1724 | 652 |
| 6 | "감사합니다" 발음도 알려주세요. | VOCAB_MISMATCH(no_romanization;not_trilingual) | 103 | 27.4 | 1414 | 723 |
| 7 | 위 표현 5개 정리. 한국어 + 로마자 발음 + 영어 의미 형식으로. | EMPTY | 0 | 98.9 | 1650 | 868 |

### FRN-MT-104 (foreigner_lang / avoid_hanja_hospital)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 공부해요. 한자어 어려워요. 병원 갈 때 쉬운 말로 알려주세요. | THINK_RUNAWAY | 1001 | 98.8 | 545 | 0 |
| 2 | "감기" 같은 단어 말고 다른 쉬운 말로 증상 설명하는 법. | SUCCESS | 197 | 56.9 | 652 | 93 |
| 3 | 병원에서 접수하는 법 쉽게 알려주세요. | SUCCESS | 239 | 38.7 | 1065 | 290 |
| 4 | 지금까지 다 정리해주세요. 한자어 0개로. | EMPTY | 0 | 98.8 | 1471 | 475 |

### FRN-MT-105 (foreigner_lang / register_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 책으로 공부했어요. 너무 formal해요. | VOCAB_MISMATCH(uses_formal_register) | 212 | 46.2 | 533 | 0 |
| 2 | 친구한테 쓸 말 알려주세요. 평어/반말로요. | VOCAB_MISMATCH(uses_formal_register) | 32 | 39.6 | 936 | 189 |
| 3 | "안녕하세요" → 친구한테는 어떻게 말해요? "감사합니다"는요? | THINK_RUNAWAY | 1271 | 98.8 | 1081 | 268 |
| 4 | 카페에서 음료 주문할 때 일상적인 말투로. | VOCAB_MISMATCH(uses_formal_register) | 41 | 24.6 | 1167 | 358 |
| 5 | 위 전부 다시. 친구한테 말하는 말투로. | VOCAB_MISMATCH(uses_formal_register) | 36 | 20.1 | 1085 | 446 |

### REC-MT-101 (recommendation / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 박물관 가보고 싶어요. 어디가 좋을까요? | SUCCESS | 198 | 38.0 | 540 | 0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | 183 | 77.6 | 930 | 188 |
| 3 | 한국어는 일상 회화 정도예요. | SUCCESS | 183 | 44.4 | 1315 | 374 |
| 4 | 한국 역사 잘 몰라요. | EMPTY | 0 | 99.3 | 1466 | 553 |
| 5 | 그림이나 도자기 좋아해요. | SUCCESS | 240 | 16.7 | 1524 | 620 |
| 6 | 8살 딸이랑 같이 가요. | EMPTY | 0 | 99.2 | 1756 | 798 |
| 7 | 너무 길거나 어려운 곳 말고요. | EMPTY | 0 | 99.4 | 1658 | 866 |
| 8 | 위 정보 다 반영해서 박물관 3곳 추천 + 각각 이유. | EMPTY | 0 | 99.3 | 1748 | 938 |

### REC-MT-102 (recommendation / defector_settlement_program)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 정착 프로그램 추천해주세요. | SUCCESS | 198 | 37.6 | 533 | 0 |
| 2 | 50대 여자, 평양 출신이에요. 작년에 한국 왔어요. | REPETITION_LOOP | 995 | 99.3 | 922 | 181 |
| 3 | 혼자 살고 있어요. | EMPTY | 0 | 99.4 | 1624 | 374 |
| 4 | 장사 해보고 싶어요. 컴퓨터는 약해요. | EMPTY | 0 | 99.3 | 1692 | 439 |
| 5 | 서울에 살아요. | EMPTY | 0 | 99.2 | 1578 | 515 |
| 6 | 너무 빨리 진행되는 건 따라가기 힘들어요. | EMPTY | 0 | 99.2 | 1635 | 578 |
| 7 | 위 조건 다 반영해서 정착 지원 프로그램 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=50대,장사,서울) | 260 | 56.6 | 1248 | 656 |

### REC-MT-103 (recommendation / elderly_culture_event)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 우리 동네 문화행사 추천 좀 해주세요. | SUCCESS | 357 | 42.8 | 536 | 0 |
| 2 | 75살이에요. 무릎이 안 좋아요. | SUCCESS | 640 | 79.9 | 1074 | 184 |
| 3 | 큰 글씨, 큰 화면이면 좋아요. | EMPTY | 0 | 99.3 | 1771 | 365 |
| 4 | 가곡이나 옛날 노래 좋아해요. | SUCCESS | 758 | 80.4 | 1838 | 437 |
| 5 | 친구 사귈 수 있는 곳이면 더 좋고요. | EMPTY | 0 | 99.4 | 2165 | 616 |
| 6 | 위 조건 다 반영해서 행사 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=가곡) | 1050 | 92.5 | 1768 | 692 |

### REC-MT-104 (recommendation / office_worker_fitness_diet)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 운동 루틴이랑 식단 추천해줘. | REPETITION_LOOP | 1617 | 99.1 | 531 | 0 |
| 2 | 32살 사무직, 허리가 자주 아파. | SUCCESS | 271 | 48.9 | 601 | 70 |
| 3 | 집에서 할 수 있는 거 위주. | SUCCESS | 245 | 35.4 | 1071 | 253 |
| 4 | 평일 저녁 30분. | EMPTY | 0 | 99.2 | 1490 | 433 |
| 5 | 요리 잘 못해. | REPETITION_LOOP | 1563 | 99.2 | 1544 | 498 |
| 6 | 위 정보로 1주 운동 + 식단 표로 추천해줘. | RECOMMENDATION_GENERIC(missing=허리,집) | 450 | 52.6 | 1361 | 561 |

### REC-MT-105 (recommendation / student_learning_resource)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 학습 자료 추천해줘. | SUCCESS | 500 | 60.8 | 526 | 0 |
| 2 | 정보 부족하면 먼저 질문해줘. | EMPTY | 0 | 99.2 | 1191 | 173 |
| 3 | 컴퓨터공학 전공 3학년이야. | SUCCESS | 633 | 68.5 | 1277 | 244 |
| 4 | 머신러닝 기초 공부하고 싶어. | EMPTY | 0 | 99.4 | 1961 | 423 |
| 5 | 한국어 자료가 더 편해. 영어도 가능은 함. | SUCCESS | 1116 | 99.3 | 1561 | 494 |
| 6 | 책보단 무료 강의가 좋아. | EMPTY | 0 | 99.4 | 2232 | 682 |
| 7 | 수학 백그라운드는 미적분/선형대수 학부 수준. | SUCCESS | 1054 | 99.3 | 1826 | 751 |
| 8 | 위 정보로 학습 자료 3개 추천 + 각각 이유. | EMPTY | 0 | 99.3 | 2501 | 940 |
