# 4축 평가 결과 (think 모드)

## 1. 전체 요약

- 세션 수: 20
- 총 turn: 123
- 성공 turn: 55 (44.7%)
- 성공 latency 중앙값: 41.3s
- 실패 latency 중앙값: 64.2s

## 2. 트랙별 성공률

| 트랙 | 성공/전체 | 성공률 |
|---|---|---|
| persona | 16/31 | 51.6% |
| multiturn | 16/30 | 53.3% |
| foreigner_lang | 9/27 | 33.3% |
| recommendation | 14/35 | 40.0% |

## 3. Summary Memory / Context 진단

- prompt chars 중앙값: 1341
- prompt chars 최대값: 2075
- memory chars 중앙값: 418
- memory chars 최대값: 911
- raw output chars 중앙값: 395
- raw output chars 최대값: 1090
- clean output chars 중앙값: 80
- clean output chars 최대값: 620

## 4. 실패 유형 분포

### 4.1 일반 실패

| 유형 | 개수 |
|---|---|
| EMPTY | 52 |
| THINK_RUNAWAY | 5 |

### 4.2 4축 특화 실패 (generic=SUCCESS이지만 트랙 기준 미충족)

| 유형 | 개수 |
|---|---|
| VOCAB_MISMATCH | 7 |
| PERSONA_RECALL_FAIL | 2 |
| RECOMMENDATION_GENERIC | 1 |
| CLARIFY_SKIPPED | 1 |

## 5. 세션별 turn 결과

### PER-MT-101 (persona / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 박물관 가이드 도움 받고 싶어요. | SUCCESS | 256 | 32.7 | 549 | 0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | 300 | 45.8 | 985 | 187 |
| 3 | 한국어는 일상 회화 정도만 가능해요. | EMPTY | 0 | 64.1 | 1489 | 373 |
| 4 | 한국 역사 잘 몰라요. 조선시대 이런 거 들어본 적 없어요. | SUCCESS | 250 | 36.0 | 1572 | 448 |
| 5 | 그림이나 도자기 같은 거 보는 거 좋아해요. | SUCCESS | 243 | 15.3 | 1774 | 644 |
| 6 | 8살 딸이랑 같이 가요. 짧게 보고 싶어요. | EMPTY | 0 | 64.1 | 1911 | 832 |
| 7 | 위 정보 종합해서 저랑 딸의 관람 페르소나 한 단락으로 정리해주세요. | EMPTY | 0 | 87.7 | 1995 | 911 |

### PER-MT-102 (persona / defector_settlement)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 도움 받고 싶어서요. | SUCCESS | 95 | 23.2 | 542 | 0 |
| 2 | 작년에 한국 왔어요. 50대 여자입니다. | SUCCESS | 189 | 30.1 | 776 | 136 |
| 3 | 혼자 살고 있어요. 평양 출신이에요. | SUCCESS | 189 | 50.2 | 1171 | 322 |
| 4 | 장사 좀 해보고 싶은데 한국 시스템을 잘 몰라요. 컴퓨터도 약해요. | EMPTY | 0 | 64.1 | 1468 | 506 |
| 5 | 위 정보로 제 상황 한 단락으로 정리해주세요. | SUCCESS | 330 | 20.7 | 1563 | 598 |

### PER-MT-103 (persona / elderly_culture)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 우리 동네 문화센터 어떻게 다닐지 좀 알려줘요. | SUCCESS | 324 | 34.5 | 557 | 0 |
| 2 | 75살이고 무릎이 안 좋아서 멀리는 못 다녀요. | SUCCESS | 347 | 64.2 | 1082 | 196 |
| 3 | 글씨 작은 건 잘 안 보여요. 큰 글씨로 부탁해요. | EMPTY | 0 | 64.3 | 1644 | 386 |
| 4 | 옛날에 노래 부르는 거 좋아했어요. 가곡 같은 거. | EMPTY | 0 | 64.3 | 1722 | 469 |
| 5 | 친구 사귀고 싶어요. 혼자 너무 적적해요. | THINK_RUNAWAY | 1002 | 64.2 | 1506 | 552 |
| 6 | 위 정보로 제 페르소나 정리해주세요. | PERSONA_RECALL_FAIL(missing=가곡,혼자) | 344 | 46.9 | 1578 | 630 |

### PER-MT-104 (persona / office_worker_fitness)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 운동 좀 시작하려고. | SUCCESS | 211 | 46.4 | 535 | 0 |
| 2 | 32살 직장인이고 사무실에서 하루 종일 앉아 있어. | SUCCESS | 522 | 64.2 | 924 | 174 |
| 3 | 키 175, 몸무게 82kg. | EMPTY | 0 | 64.3 | 1632 | 366 |
| 4 | 허리가 자주 아파. | SUCCESS | 401 | 64.2 | 1702 | 437 |
| 5 | 헬스장은 부담스럽고 집에서 할 수 있는 거 좋아. | EMPTY | 0 | 64.3 | 2068 | 611 |
| 6 | 시간은 평일 저녁 30분 정도밖에 못 내. | EMPTY | 0 | 64.1 | 1673 | 693 |
| 7 | 식단도 신경 쓰고 싶은데 요리는 잘 못해. | EMPTY | 0 | 64.2 | 1758 | 771 |
| 8 | 위 정보 다 종합해서 내 페르소나 한 단락으로 정리해줘. | PERSONA_RECALL_FAIL(missing=32) | 516 | 56.2 | 1857 | 849 |

### PER-MT-105 (persona / parent_kid_education)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 우리 아이 학습 도움 받고 싶어요. | SUCCESS | 167 | 33.3 | 543 | 0 |
| 2 | 초등학교 3학년 딸이에요. | SUCCESS | 168 | 28.4 | 886 | 182 |
| 3 | 수학을 어려워해요. 특히 분수 부분. | EMPTY | 0 | 64.2 | 1252 | 360 |
| 4 | 책 읽는 건 좋아하는데 혼자만 하려고 해요. | SUCCESS | 222 | 41.1 | 1332 | 435 |
| 5 | 위 정보로 우리 아이 학습 페르소나 정리해주세요. | EMPTY | 0 | 64.1 | 1589 | 623 |

### MTN-MT-101 (multiturn / intent_repair)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 저녁 메뉴 추천해줘. | SUCCESS | 226 | 41.3 | 495 | 0 |
| 2 | 한식 말고. | SUCCESS | 150 | 9.8 | 878 | 173 |
| 3 | 아 미안, 한식도 괜찮아. 단 너무 매운 건 빼고. | EMPTY | 0 | 64.1 | 1226 | 343 |
| 4 | 내가 처음에 뭘 부탁했지? | EMPTY | 0 | 64.1 | 1312 | 426 |

### MTN-MT-102 (multiturn / tone_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 한국 여행 정보 부탁드립니다. | SUCCESS | 372 | 40.8 | 507 | 0 |
| 2 | 정중하게 안내해주세요. 저는 외국인이에요. | EMPTY | 0 | 64.2 | 1065 | 186 |
| 3 | 경주 추천 받고 싶어요. | SUCCESS | 424 | 54.9 | 1156 | 264 |
| 4 | 이제 친구처럼 편하게 말해줘. 반말로. | EMPTY | 0 | 64.3 | 1753 | 441 |
| 5 | 거기서 뭘 봐야 돼? | EMPTY | 0 | 64.2 | 1472 | 517 |
| 6 | 다시 정중하게 돌아가 주세요. 격식체로요. | SUCCESS | 422 | 62.5 | 1538 | 583 |
| 7 | 위에서 추천한 곳들 격식체로 한 줄씩 다시 정리해 주세요. | SUCCESS | 312 | 54.4 | 1744 | 770 |

### MTN-MT-103 (multiturn / reference_tracking)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 무릎 통증 때문에 병원 두 곳 알아봤어요. 정형외과랑 한의원. | SUCCESS | 373 | 62.9 | 518 | 0 |
| 2 | 거기 둘 중 70대한테 더 맞는 곳은? | SUCCESS | 285 | 47.2 | 1087 | 197 |
| 3 | 그 곳 보험 적용돼요? | EMPTY | 0 | 64.2 | 1568 | 381 |
| 4 | 거기 가는 길에 약국도 들를 수 있나요? | EMPTY | 0 | 64.3 | 1623 | 448 |
| 5 | 처음에 비교한 두 군데 이름 다시 말해줘요. | THINK_RUNAWAY | 1041 | 64.1 | 1354 | 525 |

### MTN-MT-104 (multiturn / topic_switch_return)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 회의록 정리하는 법 알려줘. | SUCCESS | 299 | 33.2 | 499 | 0 |
| 2 | 가장 효과적인 방법은? | SUCCESS | 76 | 21.2 | 969 | 178 |
| 3 | 잠깐, 다른 거 물어봐도 돼? 노션이랑 옵시디언 차이가 뭐야? | SUCCESS | 139 | 45.3 | 1191 | 290 |
| 4 | 둘 중 회의록에 더 적합한 건? | EMPTY | 0 | 64.2 | 1228 | 486 |
| 5 | 가격은 어떻게 돼? | SUCCESS | 364 | 24.3 | 1298 | 558 |
| 6 | 아까 회의록 얘기로 돌아가서, 두 번째로 효과적인 정리 방법은? | THINK_RUNAWAY | 1054 | 64.2 | 1756 | 732 |
| 7 | 그 방법 단점도 알려줘. | EMPTY | 0 | 64.1 | 1721 | 822 |
| 8 | 우리가 회의록 얘기 하다가 잠깐 뭐로 빠졌었지? | SUCCESS | 349 | 63.1 | 1798 | 890 |

### MTN-MT-105 (multiturn / constraint_accumulation)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 정착할 때 신청해야 하는 지원금 알려주세요. | SUCCESS | 415 | 50.8 | 511 | 0 |
| 2 | 정확히 3가지만. | EMPTY | 0 | 64.2 | 1104 | 190 |
| 3 | 각 항목 옆에 신청 기관도 같이. | SUCCESS | 66 | 29.4 | 1186 | 254 |
| 4 | 각 항목 30자 이내로 짧게. | EMPTY | 0 | 64.1 | 1341 | 358 |
| 5 | 마지막은 새터민이 가장 먼저 알아야 할 순서로 정렬해주세요. | SUCCESS | 62 | 34.8 | 1032 | 429 |
| 6 | 위 모든 제약 다 지켜서 최종본만 출력. | EMPTY | 0 | 64.1 | 1208 | 548 |

### FRN-MT-101 (foreigner_lang / beginner_restaurant)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 잘 못해요. 천천히 쉽게 말해주세요. | SUCCESS | 620 | 64.1 | 530 | 0 |
| 2 | 식당에서 주문하고 싶어요. 어떻게 말해요? | SUCCESS | 270 | 42.4 | 1221 | 187 |
| 3 | "이거 주세요" 무엇이에요? | EMPTY | 0 | 64.2 | 1689 | 373 |
| 4 | 매운 거 싫어요. 어떻게 말해요? | EMPTY | 0 | 64.3 | 1753 | 443 |
| 5 | 지금까지 얘기 다시. 짧게. 쉬운 단어만. | SUCCESS | 164 | 11.7 | 1349 | 516 |

### FRN-MT-102 (foreigner_lang / code_switching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. I'm learning Korean. | VOCAB_MISMATCH(no_english_terms) | 274 | 48.0 | 533 | 0 |
| 2 | "처마" 무슨 뜻이에요? Is it about the roof? | VOCAB_MISMATCH(no_english_terms) | 124 | 33.6 | 1009 | 190 |
| 3 | 한옥 설명해주세요. 어려우면 영어 단어 쓰셔도 돼요. | EMPTY | 0 | 64.1 | 1345 | 373 |
| 4 | 한옥 보러 가고 싶어요. 어디 가요? | EMPTY | 0 | 64.1 | 1422 | 457 |
| 5 | 입장료 비싸요? | VOCAB_MISMATCH(no_english_terms) | 126 | 22.3 | 1235 | 532 |
| 6 | 위 내용 다시 정리. Korean first, then English s… | VOCAB_MISMATCH(no_english_terms) | 126 | 33.1 | 1407 | 690 |

### FRN-MT-103 (foreigner_lang / english_to_korean_teaching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | Hi! Can you help me practice Korean? | VOCAB_MISMATCH(no_romanization;not_trilingual) | 222 | 40.3 | 542 | 0 |
| 2 | I want to order food in Korean. Teach me… | VOCAB_MISMATCH(no_romanization;not_trilingual) | 318 | 45.7 | 996 | 199 |
| 3 | How do I say "no spicy please"? | EMPTY | 0 | 64.2 | 1562 | 418 |
| 4 | 한국어로 다시 말해주세요. 천천히. | EMPTY | 0 | 64.1 | 1631 | 504 |
| 5 | 발음도 알려줘요. 로마자로요. | SUCCESS | 181 | 33.2 | 1502 | 578 |
| 6 | "감사합니다" 발음도 알려주세요. | EMPTY | 0 | 64.1 | 1510 | 758 |
| 7 | 위 표현 5개 정리. 한국어 + 로마자 발음 + 영어 의미 형식으로. | SUCCESS | 80 | 23.7 | 1590 | 831 |

### FRN-MT-104 (foreigner_lang / avoid_hanja_hospital)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 공부해요. 한자어 어려워요. 병원 갈 때 쉬운 말로 알려주세요. | SUCCESS | 85 | 31.1 | 545 | 0 |
| 2 | "감기" 같은 단어 말고 다른 쉬운 말로 증상 설명하는 법. | SUCCESS | 228 | 42.9 | 789 | 146 |
| 3 | 병원에서 접수하는 법 쉽게 알려주세요. | SUCCESS | 272 | 40.3 | 1234 | 343 |
| 4 | 지금까지 다 정리해주세요. 한자어 0개로. | EMPTY | 0 | 64.2 | 1588 | 527 |

### FRN-MT-105 (foreigner_lang / register_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 책으로 공부했어요. 너무 formal해요. | VOCAB_MISMATCH(uses_formal_register) | 257 | 46.9 | 533 | 0 |
| 2 | 친구한테 쓸 말 알려주세요. 평어/반말로요. | SUCCESS | 272 | 63.7 | 984 | 190 |
| 3 | "안녕하세요" → 친구한테는 어떻게 말해요? "감사합니다"는요? | EMPTY | 0 | 63.7 | 1435 | 378 |
| 4 | 카페에서 음료 주문할 때 일상적인 말투로. | EMPTY | 0 | 63.7 | 1521 | 468 |
| 5 | 위 전부 다시. 친구한테 말하는 말투로. | EMPTY | 0 | 63.6 | 1365 | 546 |

### REC-MT-101 (recommendation / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 박물관 가보고 싶어요. 어디가 좋을까요? | SUCCESS | 78 | 24.8 | 540 | 0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | 104 | 43.5 | 748 | 126 |
| 3 | 한국어는 일상 회화 정도예요. | THINK_RUNAWAY | 1063 | 63.6 | 1019 | 277 |
| 4 | 한국 역사 잘 몰라요. | SUCCESS | 172 | 27.2 | 1077 | 348 |
| 5 | 그림이나 도자기 좋아해요. | SUCCESS | 101 | 26.8 | 1337 | 523 |
| 6 | 8살 딸이랑 같이 가요. | EMPTY | 0 | 63.6 | 1470 | 662 |
| 7 | 너무 길거나 어려운 곳 말고요. | SUCCESS | 101 | 25.0 | 1543 | 730 |
| 8 | 위 정보 다 반영해서 박물관 3곳 추천 + 각각 이유. | EMPTY | 0 | 63.6 | 1630 | 872 |

### REC-MT-102 (recommendation / defector_settlement_program)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 정착 프로그램 추천해주세요. | SUCCESS | 230 | 39.6 | 533 | 0 |
| 2 | 50대 여자, 평양 출신이에요. 작년에 한국 왔어요. | SUCCESS | 421 | 64.4 | 954 | 181 |
| 3 | 혼자 살고 있어요. | SUCCESS | 563 | 64.5 | 1573 | 373 |
| 4 | 장사 해보고 싶어요. 컴퓨터는 약해요. | EMPTY | 0 | 64.5 | 2020 | 547 |
| 5 | 서울에 살아요. | EMPTY | 0 | 64.8 | 2075 | 623 |
| 6 | 너무 빨리 진행되는 건 따라가기 힘들어요. | EMPTY | 0 | 64.6 | 1744 | 686 |
| 7 | 위 조건 다 반영해서 정착 지원 프로그램 3개 추천 + 이유. | EMPTY | 0 | 64.6 | 1846 | 764 |

### REC-MT-103 (recommendation / elderly_culture_event)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 우리 동네 문화행사 추천 좀 해주세요. | SUCCESS | 411 | 47.1 | 536 | 0 |
| 2 | 75살이에요. 무릎이 안 좋아요. | SUCCESS | 547 | 64.6 | 1125 | 183 |
| 3 | 큰 글씨, 큰 화면이면 좋아요. | EMPTY | 0 | 64.7 | 1823 | 364 |
| 4 | 가곡이나 옛날 노래 좋아해요. | EMPTY | 0 | 64.7 | 1890 | 436 |
| 5 | 친구 사귈 수 있는 곳이면 더 좋고요. | SUCCESS | 599 | 64.6 | 1575 | 507 |
| 6 | 위 조건 다 반영해서 행사 3개 추천 + 이유. | EMPTY | 0 | 64.6 | 1767 | 691 |

### REC-MT-104 (recommendation / office_worker_fitness_diet)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 운동 루틴이랑 식단 추천해줘. | SUCCESS | 367 | 49.5 | 531 | 0 |
| 2 | 32살 사무직, 허리가 자주 아파. | SUCCESS | 542 | 64.6 | 1074 | 179 |
| 3 | 집에서 할 수 있는 거 위주. | EMPTY | 0 | 64.7 | 1773 | 362 |
| 4 | 평일 저녁 30분. | EMPTY | 0 | 64.6 | 1838 | 433 |
| 5 | 요리 잘 못해. | THINK_RUNAWAY | 1089 | 64.6 | 1547 | 498 |
| 6 | 위 정보로 1주 운동 + 식단 표로 추천해줘. | RECOMMENDATION_GENERIC(missing=허리) | 333 | 22.6 | 1616 | 561 |

### REC-MT-105 (recommendation / student_learning_resource)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 학습 자료 추천해줘. | SUCCESS | 206 | 49.7 | 526 | 0 |
| 2 | 정보 부족하면 먼저 질문해줘. | CLARIFY_SKIPPED(no_question_or_dumped_list) | 203 | 37.1 | 900 | 174 |
| 3 | 컴퓨터공학 전공 3학년이야. | EMPTY | 0 | 64.7 | 1298 | 354 |
| 4 | 머신러닝 기초 공부하고 싶어. | EMPTY | 0 | 64.6 | 1373 | 424 |
| 5 | 한국어 자료가 더 편해. 영어도 가능은 함. | EMPTY | 0 | 64.6 | 1265 | 495 |
| 6 | 책보단 무료 강의가 좋아. | EMPTY | 0 | 64.6 | 1342 | 574 |
| 7 | 수학 백그라운드는 미적분/선형대수 학부 수준. | EMPTY | 0 | 64.6 | 1233 | 643 |
| 8 | 위 정보로 학습 자료 3개 추천 + 각각 이유. | EMPTY | 0 | 64.6 | 1324 | 723 |
