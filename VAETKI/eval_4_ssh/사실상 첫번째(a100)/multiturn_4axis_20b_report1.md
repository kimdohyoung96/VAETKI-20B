# 4축 평가 결과 (think 모드)

## 1. 전체 요약

- 세션 수: 20
- 총 turn: 123
- 성공 turn: 85 (69.1%)
- 성공 latency 중앙값: 25.6s
- 실패 latency 중앙값: 26.2s

## 2. 트랙별 성공률

| 트랙 | 성공/전체 | 성공률 |
|---|---|---|
| persona | 25/31 | 80.6% |
| multiturn | 25/30 | 83.3% |
| foreigner_lang | 7/27 | 25.9% |
| recommendation | 28/35 | 80.0% |

## 3. Summary Memory / Context 진단

- prompt chars 중앙값: 1473
- prompt chars 최대값: 2686
- memory chars 중앙값: 399
- memory chars 최대값: 1144
- raw output chars 중앙값: 746
- raw output chars 최대값: 9440
- clean output chars 중앙값: 250
- clean output chars 최대값: 7340

## 4. 실패 유형 분포

### 4.1 일반 실패

| 유형 | 개수 |
|---|---|
| REPETITION_LOOP | 8 |

### 4.2 4축 특화 실패 (generic=SUCCESS이지만 트랙 기준 미충족)

| 유형 | 개수 |
|---|---|
| VOCAB_MISMATCH | 18 |
| RECOMMENDATION_GENERIC | 5 |
| PERSONA_RECALL_FAIL | 4 |
| CONTEXT_LOSS | 2 |
| ITEM_COUNT_MISMATCH | 1 |

## 5. 세션별 turn 결과

### PER-MT-101 (persona / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 박물관 가이드 도움 받고 싶어요. | SUCCESS | 78 | 21.1 | 549 | 0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | REPETITION_LOOP | 8049 | 317.8 | 757 | 126 |
| 3 | 한국어는 일상 회화 정도만 가능해요. | SUCCESS | 243 | 23.0 | 855 | 204 |
| 4 | 한국 역사 잘 몰라요. 조선시대 이런 거 들어본 적 없어요. | SUCCESS | 283 | 28.6 | 1290 | 388 |
| 5 | 그림이나 도자기 같은 거 보는 거 좋아해요. | SUCCESS | 301 | 23.1 | 1693 | 585 |
| 6 | 8살 딸이랑 같이 가요. 짧게 보고 싶어요. | SUCCESS | 290 | 28.8 | 1942 | 772 |
| 7 | 위 정보 종합해서 저랑 딸의 관람 페르소나 한 단락으로 정리해주세요. | PERSONA_RECALL_FAIL(missing=베트남,일상 회화,딸,조선) | 250 | 33.3 | 2142 | 960 |

### PER-MT-102 (persona / defector_settlement)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 도움 받고 싶어서요. | SUCCESS | 76 | 12.2 | 542 | 0 |
| 2 | 작년에 한국 왔어요. 50대 여자입니다. | SUCCESS | 74 | 3.0 | 736 | 116 |
| 3 | 혼자 살고 있어요. 평양 출신이에요. | SUCCESS | 72 | 2.8 | 950 | 236 |
| 4 | 장사 좀 해보고 싶은데 한국 시스템을 잘 몰라요. 컴퓨터도 약해요. | SUCCESS | 464 | 34.3 | 1082 | 352 |
| 5 | 위 정보로 제 상황 한 단락으로 정리해주세요. | SUCCESS | 475 | 29.9 | 1672 | 553 |

### PER-MT-103 (persona / elderly_culture)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 우리 동네 문화센터 어떻게 다닐지 좀 알려줘요. | SUCCESS | 332 | 19.6 | 557 | 0 |
| 2 | 75살이고 무릎이 안 좋아서 멀리는 못 다녀요. | SUCCESS | 614 | 48.3 | 1090 | 196 |
| 3 | 글씨 작은 건 잘 안 보여요. 큰 글씨로 부탁해요. | SUCCESS | 500 | 27.3 | 1808 | 386 |
| 4 | 옛날에 노래 부르는 거 좋아했어요. 가곡 같은 거. | REPETITION_LOOP | 8429 | 289.6 | 2165 | 578 |
| 5 | 친구 사귀고 싶어요. 혼자 너무 적적해요. | SUCCESS | 945 | 51.1 | 2245 | 661 |
| 6 | 위 정보로 제 페르소나 정리해주세요. | PERSONA_RECALL_FAIL(missing=가곡,혼자) | 500 | 33.2 | 2424 | 848 |

### PER-MT-104 (persona / office_worker_fitness)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 운동 좀 시작하려고. | SUCCESS | 393 | 25.6 | 535 | 0 |
| 2 | 32살 직장인이고 사무실에서 하루 종일 앉아 있어. | SUCCESS | 595 | 44.1 | 1107 | 174 |
| 3 | 키 175, 몸무게 82kg. | SUCCESS | 491 | 47.1 | 1815 | 366 |
| 4 | 허리가 자주 아파. | SUCCESS | 573 | 41.0 | 2093 | 546 |
| 5 | 헬스장은 부담스럽고 집에서 할 수 있는 거 좋아. | SUCCESS | 519 | 38.6 | 2265 | 720 |
| 6 | 시간은 평일 저녁 30분 정도밖에 못 내. | SUCCESS | 498 | 41.7 | 2475 | 911 |
| 7 | 식단도 신경 쓰고 싶은데 요리는 잘 못해. | SUCCESS | 638 | 38.1 | 2670 | 1098 |
| 8 | 위 정보 다 종합해서 내 페르소나 한 단락으로 정리해줘. | PERSONA_RECALL_FAIL(missing=30분) | 188 | 36.1 | 2686 | 1110 |

### PER-MT-105 (persona / parent_kid_education)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 우리 아이 학습 도움 받고 싶어요. | SUCCESS | 383 | 31.9 | 543 | 0 |
| 2 | 초등학교 3학년 딸이에요. | SUCCESS | 215 | 18.9 | 1100 | 182 |
| 3 | 수학을 어려워해요. 특히 분수 부분. | SUCCESS | 387 | 32.8 | 1512 | 359 |
| 4 | 책 읽는 건 좋아하는데 혼자만 하려고 해요. | SUCCESS | 383 | 34.2 | 1704 | 543 |
| 5 | 위 정보로 우리 아이 학습 페르소나 정리해주세요. | PERSONA_RECALL_FAIL(missing=초등,3학년) | 251 | 25.4 | 2071 | 731 |

### MTN-MT-101 (multiturn / intent_repair)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 저녁 메뉴 추천해줘. | SUCCESS | 199 | 19.4 | 495 | 0 |
| 2 | 한식 말고. | SUCCESS | 181 | 27.9 | 847 | 174 |
| 3 | 아 미안, 한식도 괜찮아. 단 너무 매운 건 빼고. | SUCCESS | 183 | 24.4 | 1225 | 343 |
| 4 | 내가 처음에 뭘 부탁했지? | CONTEXT_LOSS(missing=저녁) | 15 | 13.6 | 1411 | 535 |

### MTN-MT-102 (multiturn / tone_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. 한국 여행 정보 부탁드립니다. | SUCCESS | 374 | 23.2 | 507 | 0 |
| 2 | 정중하게 안내해주세요. 저는 외국인이에요. | SUCCESS | 370 | 28.6 | 1067 | 186 |
| 3 | 경주 추천 받고 싶어요. | SUCCESS | 223 | 21.5 | 1637 | 373 |
| 4 | 이제 친구처럼 편하게 말해줘. 반말로. | SUCCESS | 244 | 24.8 | 1665 | 550 |
| 5 | 거기서 뭘 봐야 돼? | SUCCESS | 208 | 22.9 | 1712 | 735 |
| 6 | 다시 정중하게 돌아가 주세요. 격식체로요. | SUCCESS | 228 | 26.2 | 1882 | 910 |
| 7 | 위에서 추천한 곳들 격식체로 한 줄씩 다시 정리해 주세요. | SUCCESS | 204 | 20.6 | 2064 | 1097 |

### MTN-MT-103 (multiturn / reference_tracking)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 무릎 통증 때문에 병원 두 곳 알아봤어요. 정형외과랑 한의원. | SUCCESS | 248 | 24.1 | 518 | 0 |
| 2 | 거기 둘 중 70대한테 더 맞는 곳은? | SUCCESS | 309 | 28.6 | 965 | 197 |
| 3 | 그 곳 보험 적용돼요? | SUCCESS | 309 | 31.3 | 1471 | 382 |
| 4 | 거기 가는 길에 약국도 들를 수 있나요? | REPETITION_LOOP | 8372 | 281.2 | 1696 | 558 |
| 5 | 처음에 비교한 두 군데 이름 다시 말해줘요. | SUCCESS | 309 | 25.8 | 1776 | 635 |

### MTN-MT-104 (multiturn / topic_switch_return)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 회의록 정리하는 법 알려줘. | SUCCESS | 286 | 18.5 | 499 | 0 |
| 2 | 가장 효과적인 방법은? | SUCCESS | 173 | 17.1 | 956 | 178 |
| 3 | 잠깐, 다른 거 물어봐도 돼? 노션이랑 옵시디언 차이가 뭐야? | SUCCESS | 826 | 40.8 | 1339 | 354 |
| 4 | 둘 중 회의록에 더 적합한 건? | SUCCESS | 101 | 16.1 | 1753 | 552 |
| 5 | 가격은 어떻게 돼? | SUCCESS | 116 | 17.2 | 1821 | 694 |
| 6 | 아까 회의록 얘기로 돌아가서, 두 번째로 효과적인 정리 방법은? | CONTEXT_LOSS(missing=회의록,노션) | 64 | 16.4 | 1588 | 844 |
| 7 | 그 방법 단점도 알려줘. | SUCCESS | 151 | 17.6 | 1670 | 967 |
| 8 | 우리가 회의록 얘기 하다가 잠깐 뭐로 빠졌었지? | REPETITION_LOOP | 9439 | 289.1 | 1898 | 1144 |

### MTN-MT-105 (multiturn / constraint_accumulation)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 정착할 때 신청해야 하는 지원금 알려주세요. | SUCCESS | 342 | 25.6 | 511 | 0 |
| 2 | 정확히 3가지만. | SUCCESS | 144 | 15.8 | 1031 | 190 |
| 3 | 각 항목 옆에 신청 기관도 같이. | SUCCESS | 138 | 16.6 | 1365 | 362 |
| 4 | 각 항목 30자 이내로 짧게. | SUCCESS | 144 | 14.4 | 1332 | 542 |
| 5 | 마지막은 새터민이 가장 먼저 알아야 할 순서로 정렬해주세요. | SUCCESS | 144 | 21.0 | 1535 | 721 |
| 6 | 위 모든 제약 다 지켜서 최종본만 출력. | ITEM_COUNT_MISMATCH(expected=3,got=0) | 144 | 19.2 | 1741 | 917 |

### FRN-MT-101 (foreigner_lang / beginner_restaurant)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 잘 못해요. 천천히 쉽게 말해주세요. | SUCCESS | 230 | 23.8 | 530 | 0 |
| 2 | 식당에서 주문하고 싶어요. 어떻게 말해요? | SUCCESS | 214 | 19.3 | 949 | 187 |
| 3 | "이거 주세요" 무엇이에요? | VOCAB_MISMATCH(long_sentences=2) | 170 | 23.3 | 1362 | 374 |
| 4 | 매운 거 싫어요. 어떻게 말해요? | SUCCESS | 165 | 18.4 | 1477 | 553 |
| 5 | 지금까지 얘기 다시. 짧게. 쉬운 단어만. | VOCAB_MISMATCH(long_sentences=2) | 170 | 19.6 | 1606 | 734 |

### FRN-MT-102 (foreigner_lang / code_switching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 안녕하세요. I'm learning Korean. | VOCAB_MISMATCH(no_english_terms) | 126 | 16.7 | 533 | 0 |
| 2 | "처마" 무슨 뜻이에요? Is it about the roof? | VOCAB_MISMATCH(no_english_terms) | 115 | 20.5 | 843 | 172 |
| 3 | 한옥 설명해주세요. 어려우면 영어 단어 쓰셔도 돼요. | VOCAB_MISMATCH(no_english_terms) | 249 | 21.4 | 1161 | 346 |
| 4 | 한옥 보러 가고 싶어요. 어디 가요? | VOCAB_MISMATCH(no_english_terms) | 313 | 23.8 | 1473 | 538 |
| 5 | 입장료 비싸요? | VOCAB_MISMATCH(no_english_terms) | 333 | 24.3 | 1828 | 722 |
| 6 | 위 내용 다시 정리. Korean first, then English s… | VOCAB_MISMATCH(no_english_terms) | 76 | 32.3 | 2101 | 894 |

### FRN-MT-103 (foreigner_lang / english_to_korean_teaching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | Hi! Can you help me practice Korean? | VOCAB_MISMATCH(no_romanization;not_trilingual) | 92 | 31.4 | 542 | 0 |
| 2 | I want to order food in Korean. Teach me… | VOCAB_MISMATCH(no_romanization;not_trilingual) | 224 | 22.1 | 813 | 147 |
| 3 | How do I say "no spicy please"? | VOCAB_MISMATCH(not_trilingual) | 131 | 18.8 | 1285 | 366 |
| 4 | 한국어로 다시 말해주세요. 천천히. | VOCAB_MISMATCH(not_trilingual) | 90 | 3.3 | 1493 | 550 |
| 5 | 발음도 알려줘요. 로마자로요. | SUCCESS | 98 | 17.8 | 1455 | 683 |
| 6 | "감사합니다" 발음도 알려주세요. | VOCAB_MISMATCH(not_trilingual) | 84 | 10.4 | 1549 | 821 |
| 7 | 위 표현 5개 정리. 한국어 + 로마자 발음 + 영어 의미 형식으로. | VOCAB_MISMATCH(no_romanization;not_trilingual) | 87 | 29.9 | 1688 | 947 |

### FRN-MT-104 (foreigner_lang / avoid_hanja_hospital)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 공부해요. 한자어 어려워요. 병원 갈 때 쉬운 말로 알려주세요. | REPETITION_LOOP | 7340 | 284.4 | 545 | 0 |
| 2 | "감기" 같은 단어 말고 다른 쉬운 말로 증상 설명하는 법. | SUCCESS | 424 | 30.1 | 1261 | 202 |
| 3 | 병원에서 접수하는 법 쉽게 알려주세요. | REPETITION_LOOP | 7206 | 284.8 | 1899 | 399 |
| 4 | 지금까지 다 정리해주세요. 한자어 0개로. | SUCCESS | 276 | 37.3 | 1959 | 475 |

### FRN-MT-105 (foreigner_lang / register_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국어 책으로 공부했어요. 너무 formal해요. | VOCAB_MISMATCH(uses_formal_register) | 323 | 38.6 | 533 | 0 |
| 2 | 친구한테 쓸 말 알려주세요. 평어/반말로요. | SUCCESS | 337 | 29.1 | 1045 | 189 |
| 3 | "안녕하세요" → 친구한테는 어떻게 말해요? "감사합니다"는요? | VOCAB_MISMATCH(uses_formal_register) | 34 | 20.0 | 1566 | 376 |
| 4 | 카페에서 음료 주문할 때 일상적인 말투로. | VOCAB_MISMATCH(uses_formal_register) | 133 | 21.7 | 1371 | 469 |
| 5 | 위 전부 다시. 친구한테 말하는 말투로. | VOCAB_MISMATCH(uses_formal_register) | 34 | 11.8 | 1381 | 648 |

### REC-MT-101 (recommendation / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 박물관 가보고 싶어요. 어디가 좋을까요? | SUCCESS | 205 | 22.8 | 540 | 0 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | 205 | 31.2 | 937 | 188 |
| 3 | 한국어는 일상 회화 정도예요. | SUCCESS | 205 | 23.4 | 1345 | 375 |
| 4 | 한국 역사 잘 몰라요. | SUCCESS | 205 | 18.4 | 1512 | 555 |
| 5 | 그림이나 도자기 좋아해요. | SUCCESS | 252 | 28.5 | 1679 | 731 |
| 6 | 8살 딸이랑 같이 가요. | SUCCESS | 257 | 28.9 | 1901 | 909 |
| 7 | 너무 길거나 어려운 곳 말고요. | SUCCESS | 266 | 10.1 | 2135 | 1086 |
| 8 | 위 정보 다 반영해서 박물관 3곳 추천 + 각각 이유. | RECOMMENDATION_GENERIC(missing=베트남,딸) | 202 | 20.3 | 2157 | 1078 |

### REC-MT-102 (recommendation / defector_settlement_program)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 한국 정착 프로그램 추천해주세요. | SUCCESS | 81 | 13.7 | 533 | 0 |
| 2 | 50대 여자, 평양 출신이에요. 작년에 한국 왔어요. | SUCCESS | 92 | 23.0 | 746 | 122 |
| 3 | 혼자 살고 있어요. | SUCCESS | 180 | 6.9 | 993 | 267 |
| 4 | 장사 해보고 싶어요. 컴퓨터는 약해요. | REPETITION_LOOP | 8982 | 289.7 | 1266 | 441 |
| 5 | 서울에 살아요. | REPETITION_LOOP | 8291 | 290.2 | 1321 | 517 |
| 6 | 너무 빨리 진행되는 건 따라가기 힘들어요. | SUCCESS | 403 | 40.8 | 1315 | 580 |
| 7 | 위 조건 다 반영해서 정착 지원 프로그램 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=50대,장사,혼자) | 586 | 33.6 | 1748 | 766 |

### REC-MT-103 (recommendation / elderly_culture_event)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 우리 동네 문화행사 추천 좀 해주세요. | SUCCESS | 470 | 31.1 | 536 | 0 |
| 2 | 75살이에요. 무릎이 안 좋아요. | SUCCESS | 900 | 47.6 | 1185 | 184 |
| 3 | 큰 글씨, 큰 화면이면 좋아요. | SUCCESS | 311 | 21.2 | 1884 | 366 |
| 4 | 가곡이나 옛날 노래 좋아해요. | SUCCESS | 316 | 23.1 | 1903 | 547 |
| 5 | 친구 사귈 수 있는 곳이면 더 좋고요. | SUCCESS | 477 | 31.7 | 1899 | 727 |
| 6 | 위 조건 다 반영해서 행사 3개 추천 + 이유. | RECOMMENDATION_GENERIC(missing=75) | 504 | 31.2 | 2258 | 912 |

### REC-MT-104 (recommendation / office_worker_fitness_diet)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 운동 루틴이랑 식단 추천해줘. | SUCCESS | 298 | 28.6 | 531 | 0 |
| 2 | 32살 사무직, 허리가 자주 아파. | SUCCESS | 310 | 29.0 | 1006 | 179 |
| 3 | 집에서 할 수 있는 거 위주. | SUCCESS | 529 | 30.1 | 1513 | 362 |
| 4 | 평일 저녁 30분. | SUCCESS | 577 | 35.4 | 1890 | 541 |
| 5 | 요리 잘 못해. | SUCCESS | 600 | 38.1 | 2244 | 714 |
| 6 | 위 정보로 1주 운동 + 식단 표로 추천해줘. | RECOMMENDATION_GENERIC(missing=집) | 1141 | 57.8 | 2424 | 886 |

### REC-MT-105 (recommendation / student_learning_resource)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) | prompt chars | memory chars |
|---|---|---|---|---|---:|---:|
| 1 | 학습 자료 추천해줘. | SUCCESS | 341 | 23.8 | 526 | 0 |
| 2 | 정보 부족하면 먼저 질문해줘. | SUCCESS | 415 | 26.7 | 1037 | 174 |
| 3 | 컴퓨터공학 전공 3학년이야. | SUCCESS | 699 | 33.0 | 1646 | 354 |
| 4 | 머신러닝 기초 공부하고 싶어. | SUCCESS | 670 | 39.3 | 1989 | 532 |
| 5 | 한국어 자료가 더 편해. 영어도 가능은 함. | SUCCESS | 360 | 25.4 | 2263 | 712 |
| 6 | 책보단 무료 강의가 좋아. | SUCCESS | 358 | 27.6 | 2308 | 900 |
| 7 | 수학 백그라운드는 미적분/선형대수 학부 수준. | SUCCESS | 361 | 24.4 | 2353 | 1078 |
| 8 | 위 정보로 학습 자료 3개 추천 + 각각 이유. | RECOMMENDATION_GENERIC(missing=머신러닝,3학년) | 358 | 27.1 | 2369 | 1092 |
