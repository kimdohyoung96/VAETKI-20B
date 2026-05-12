# 4축 평가 결과

## 1. 전체 요약

- 세션 수: 20
- 총 turn: 123
- 성공 turn: 47 (38.2%)
- 성공 latency 중앙값: 74.3s
- 실패 latency 중앙값: 99.0s

## 2. 트랙별 성공률

| 트랙 | 성공/전체 | 성공률 |
|---|---|---|
| persona | 13/31 | 41.9% |
| multiturn | 12/30 | 40.0% |
| foreigner_lang | 10/27 | 37.0% |
| recommendation | 12/35 | 34.3% |

## 3. 실패 유형 분포

### 3.1 일반 실패

| 유형 | 개수 |
|---|---|
| EMPTY | 62 |
| THINK_RUNAWAY | 3 |
| REPETITION_LOOP | 1 |

### 3.2 4축 특화 실패 (generic=SUCCESS이지만 트랙 기준 미충족)

| 유형 | 개수 |
|---|---|
| VOCAB_MISMATCH | 8 |
| CONTEXT_LOSS | 1 |
| CLARIFY_SKIPPED | 1 |

## 4. 세션별 turn 결과

### PER-MT-101 (persona / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 안녕하세요. 박물관 가이드 도움 받고 싶어요. | SUCCESS | 831 | 99.8 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | THINK_RUNAWAY | 1511 | 99.1 |
| 3 | 한국어는 일상 회화 정도만 가능해요. | SUCCESS | 629 | 92.8 |
| 4 | 한국 역사 잘 몰라요. 조선시대 이런 거 들어본 적 없어요. | EMPTY | 0 | 99.2 |
| 5 | 그림이나 도자기 같은 거 보는 거 좋아해요. | EMPTY | 0 | 99.1 |
| 6 | 8살 딸이랑 같이 가요. 짧게 보고 싶어요. | EMPTY | 0 | 106.8 |
| 7 | 위 정보 종합해서 저랑 딸의 관람 페르소나 한 단락으로 정리해주세요. | EMPTY | 0 | 109.8 |

### PER-MT-102 (persona / defector_settlement)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 안녕하세요. 도움 받고 싶어서요. | SUCCESS | 203 | 61.7 |
| 2 | 작년에 한국 왔어요. 50대 여자입니다. | SUCCESS | 296 | 69.5 |
| 3 | 혼자 살고 있어요. 평양 출신이에요. | SUCCESS | 298 | 49.9 |
| 4 | 장사 좀 해보고 싶은데 한국 시스템을 잘 몰라요. 컴퓨터도 약해요. | SUCCESS | 499 | 78.4 |
| 5 | 위 정보로 제 상황 한 단락으로 정리해주세요. | EMPTY | 0 | 109.7 |

### PER-MT-103 (persona / elderly_culture)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 안녕하세요. 우리 동네 문화센터 어떻게 다닐지 좀 알려줘요. | SUCCESS | 810 | 97.4 |
| 2 | 75살이고 무릎이 안 좋아서 멀리는 못 다녀요. | SUCCESS | 878 | 109.9 |
| 3 | 글씨 작은 건 잘 안 보여요. 큰 글씨로 부탁해요. | EMPTY | 0 | 109.9 |
| 4 | 옛날에 노래 부르는 거 좋아했어요. 가곡 같은 거. | EMPTY | 0 | 109.6 |
| 5 | 친구 사귀고 싶어요. 혼자 너무 적적해요. | EMPTY | 0 | 109.7 |
| 6 | 위 정보로 제 페르소나 정리해주세요. | EMPTY | 0 | 109.7 |

### PER-MT-104 (persona / office_worker_fitness)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 운동 좀 시작하려고. | SUCCESS | 561 | 84.8 |
| 2 | 32살 직장인이고 사무실에서 하루 종일 앉아 있어. | SUCCESS | 445 | 67.8 |
| 3 | 키 175, 몸무게 82kg. | EMPTY | 0 | 105.1 |
| 4 | 허리가 자주 아파. | EMPTY | 0 | 99.3 |
| 5 | 헬스장은 부담스럽고 집에서 할 수 있는 거 좋아. | EMPTY | 0 | 99.1 |
| 6 | 시간은 평일 저녁 30분 정도밖에 못 내. | EMPTY | 0 | 99.1 |
| 7 | 식단도 신경 쓰고 싶은데 요리는 잘 못해. | EMPTY | 0 | 99.2 |
| 8 | 위 정보 다 종합해서 내 페르소나 한 단락으로 정리해줘. | EMPTY | 0 | 99.1 |

### PER-MT-105 (persona / parent_kid_education)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 우리 아이 학습 도움 받고 싶어요. | SUCCESS | 704 | 83.6 |
| 2 | 초등학교 3학년 딸이에요. | SUCCESS | 100 | 56.5 |
| 3 | 수학을 어려워해요. 특히 분수 부분. | SUCCESS | 768 | 86.6 |
| 4 | 책 읽는 건 좋아하는데 혼자만 하려고 해요. | EMPTY | 0 | 99.2 |
| 5 | 위 정보로 우리 아이 학습 페르소나 정리해주세요. | EMPTY | 0 | 99.1 |

### MTN-MT-101 (multiturn / intent_repair)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 저녁 메뉴 추천해줘. | SUCCESS | 180 | 48.7 |
| 2 | 한식 말고. | SUCCESS | 504 | 74.7 |
| 3 | 아 미안, 한식도 괜찮아. 단 너무 매운 건 빼고. | SUCCESS | 404 | 58.1 |
| 4 | 내가 처음에 뭘 부탁했지? | CONTEXT_LOSS(missing=저녁) | 48 | 37.7 |

### MTN-MT-102 (multiturn / tone_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 안녕하세요. 한국 여행 정보 부탁드립니다. | REPETITION_LOOP | 1517 | 116.2 |
| 2 | 정중하게 안내해주세요. 저는 외국인이에요. | SUCCESS | 649 | 61.4 |
| 3 | 경주 추천 받고 싶어요. | SUCCESS | 434 | 60.3 |
| 4 | 이제 친구처럼 편하게 말해줘. 반말로. | EMPTY | 0 | 105.0 |
| 5 | 거기서 뭘 봐야 돼? | EMPTY | 0 | 116.5 |
| 6 | 다시 정중하게 돌아가 주세요. 격식체로요. | EMPTY | 0 | 104.5 |
| 7 | 위에서 추천한 곳들 격식체로 한 줄씩 다시 정리해 주세요. | EMPTY | 0 | 105.5 |

### MTN-MT-103 (multiturn / reference_tracking)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 무릎 통증 때문에 병원 두 곳 알아봤어요. 정형외과랑 한의원. | THINK_RUNAWAY | 1481 | 110.2 |
| 2 | 거기 둘 중 70대한테 더 맞는 곳은? | SUCCESS | 956 | 110.1 |
| 3 | 그 곳 보험 적용돼요? | SUCCESS | 895 | 110.6 |
| 4 | 거기 가는 길에 약국도 들를 수 있나요? | EMPTY | 0 | 109.9 |
| 5 | 처음에 비교한 두 군데 이름 다시 말해줘요. | EMPTY | 0 | 105.1 |

### MTN-MT-104 (multiturn / topic_switch_return)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 회의록 정리하는 법 알려줘. | SUCCESS | 726 | 78.9 |
| 2 | 가장 효과적인 방법은? | SUCCESS | 513 | 71.9 |
| 3 | 잠깐, 다른 거 물어봐도 돼? 노션이랑 옵시디언 차이가 뭐야? | EMPTY | 0 | 105.0 |
| 4 | 둘 중 회의록에 더 적합한 건? | EMPTY | 0 | 104.7 |
| 5 | 가격은 어떻게 돼? | EMPTY | 0 | 104.6 |
| 6 | 아까 회의록 얘기로 돌아가서, 두 번째로 효과적인 정리 방법은? | EMPTY | 0 | 104.6 |
| 7 | 그 방법 단점도 알려줘. | EMPTY | 0 | 104.6 |
| 8 | 우리가 회의록 얘기 하다가 잠깐 뭐로 빠졌었지? | EMPTY | 0 | 99.7 |

### MTN-MT-105 (multiturn / constraint_accumulation)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 한국 정착할 때 신청해야 하는 지원금 알려주세요. | SUCCESS | 839 | 95.4 |
| 2 | 정확히 3가지만. | SUCCESS | 207 | 34.7 |
| 3 | 각 항목 옆에 신청 기관도 같이. | SUCCESS | 307 | 44.5 |
| 4 | 각 항목 30자 이내로 짧게. | EMPTY | 0 | 98.0 |
| 5 | 마지막은 새터민이 가장 먼저 알아야 할 순서로 정렬해주세요. | EMPTY | 0 | 97.6 |
| 6 | 위 모든 제약 다 지켜서 최종본만 출력. | EMPTY | 0 | 98.5 |

### FRN-MT-101 (foreigner_lang / beginner_restaurant)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 한국어 잘 못해요. 천천히 쉽게 말해주세요. | SUCCESS | 212 | 71.1 |
| 2 | 식당에서 주문하고 싶어요. 어떻게 말해요? | SUCCESS | 249 | 48.2 |
| 3 | "이거 주세요" 무엇이에요? | SUCCESS | 206 | 33.7 |
| 4 | 매운 거 싫어요. 어떻게 말해요? | SUCCESS | 221 | 42.0 |
| 5 | 지금까지 얘기 다시. 짧게. 쉬운 단어만. | EMPTY | 0 | 97.8 |

### FRN-MT-102 (foreigner_lang / code_switching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 안녕하세요. I'm learning Korean. | SUCCESS | 379 | 59.4 |
| 2 | "처마" 무슨 뜻이에요? Is it about the roof? | VOCAB_MISMATCH(no_english_terms) | 205 | 39.8 |
| 3 | 한옥 설명해주세요. 어려우면 영어 단어 쓰셔도 돼요. | VOCAB_MISMATCH(no_english_terms) | 305 | 49.2 |
| 4 | 한옥 보러 가고 싶어요. 어디 가요? | VOCAB_MISMATCH(no_english_terms) | 346 | 48.5 |
| 5 | 입장료 비싸요? | VOCAB_MISMATCH(no_english_terms) | 237 | 47.0 |
| 6 | 위 내용 다시 정리. Korean first, then English s… | EMPTY | 0 | 96.0 |

### FRN-MT-103 (foreigner_lang / english_to_korean_teaching)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | Hi! Can you help me practice Korean? | SUCCESS | 865 | 95.8 |
| 2 | I want to order food in Korean. Teach me… | EMPTY | 0 | 98.9 |
| 3 | How do I say "no spicy please"? | EMPTY | 0 | 98.2 |
| 4 | 한국어로 다시 말해주세요. 천천히. | EMPTY | 0 | 95.0 |
| 5 | 발음도 알려줘요. 로마자로요. | EMPTY | 0 | 94.5 |
| 6 | "감사합니다" 발음도 알려주세요. | EMPTY | 0 | 108.9 |
| 7 | 위 표현 5개 정리. 한국어 + 로마자 발음 + 영어 의미 형식으로. | EMPTY | 0 | 99.0 |

### FRN-MT-104 (foreigner_lang / avoid_hanja_hospital)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 한국어 공부해요. 한자어 어려워요. 병원 갈 때 쉬운 말로 알려주세요. | SUCCESS | 102 | 66.0 |
| 2 | "감기" 같은 단어 말고 다른 쉬운 말로 증상 설명하는 법. | SUCCESS | 165 | 55.6 |
| 3 | 병원에서 접수하는 법 쉽게 알려주세요. | SUCCESS | 238 | 46.0 |
| 4 | 지금까지 다 정리해주세요. 한자어 0개로. | SUCCESS | 238 | 43.2 |

### FRN-MT-105 (foreigner_lang / register_shift)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 한국어 책으로 공부했어요. 너무 formal해요. | VOCAB_MISMATCH(uses_formal_register) | 264 | 65.9 |
| 2 | 친구한테 쓸 말 알려주세요. 평어/반말로요. | THINK_RUNAWAY | 1312 | 104.8 |
| 3 | "안녕하세요" → 친구한테는 어떻게 말해요? "감사합니다"는요? | VOCAB_MISMATCH(uses_formal_register) | 22 | 28.8 |
| 4 | 카페에서 음료 주문할 때 일상적인 말투로. | VOCAB_MISMATCH(uses_formal_register) | 300 | 65.1 |
| 5 | 위 전부 다시. 친구한테 말하는 말투로. | VOCAB_MISMATCH(uses_formal_register) | 300 | 62.2 |

### REC-MT-101 (recommendation / multicultural_museum)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 한국 박물관 가보고 싶어요. 어디가 좋을까요? | SUCCESS | 447 | 97.4 |
| 2 | 베트남에서 왔고 한국 온 지 2년 됐어요. | SUCCESS | 918 | 101.7 |
| 3 | 한국어는 일상 회화 정도예요. | EMPTY | 0 | 104.8 |
| 4 | 한국 역사 잘 몰라요. | EMPTY | 0 | 104.2 |
| 5 | 그림이나 도자기 좋아해요. | EMPTY | 0 | 104.4 |
| 6 | 8살 딸이랑 같이 가요. | EMPTY | 0 | 96.7 |
| 7 | 너무 길거나 어려운 곳 말고요. | EMPTY | 0 | 96.8 |
| 8 | 위 정보 다 반영해서 박물관 3곳 추천 + 각각 이유. | EMPTY | 0 | 96.3 |

### REC-MT-102 (recommendation / defector_settlement_program)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 한국 정착 프로그램 추천해주세요. | SUCCESS | 776 | 96.4 |
| 2 | 50대 여자, 평양 출신이에요. 작년에 한국 왔어요. | SUCCESS | 277 | 55.6 |
| 3 | 혼자 살고 있어요. | SUCCESS | 311 | 50.9 |
| 4 | 장사 해보고 싶어요. 컴퓨터는 약해요. | EMPTY | 0 | 95.6 |
| 5 | 서울에 살아요. | EMPTY | 0 | 95.4 |
| 6 | 너무 빨리 진행되는 건 따라가기 힘들어요. | EMPTY | 0 | 95.4 |
| 7 | 위 조건 다 반영해서 정착 지원 프로그램 3개 추천 + 이유. | EMPTY | 0 | 95.5 |

### REC-MT-103 (recommendation / elderly_culture_event)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 우리 동네 문화행사 추천 좀 해주세요. | SUCCESS | 879 | 95.5 |
| 2 | 75살이에요. 무릎이 안 좋아요. | SUCCESS | 810 | 83.5 |
| 3 | 큰 글씨, 큰 화면이면 좋아요. | EMPTY | 0 | 95.6 |
| 4 | 가곡이나 옛날 노래 좋아해요. | EMPTY | 0 | 95.5 |
| 5 | 친구 사귈 수 있는 곳이면 더 좋고요. | EMPTY | 0 | 96.0 |
| 6 | 위 조건 다 반영해서 행사 3개 추천 + 이유. | EMPTY | 0 | 96.5 |

### REC-MT-104 (recommendation / office_worker_fitness_diet)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 운동 루틴이랑 식단 추천해줘. | SUCCESS | 664 | 84.3 |
| 2 | 32살 사무직, 허리가 자주 아파. | SUCCESS | 735 | 74.3 |
| 3 | 집에서 할 수 있는 거 위주. | SUCCESS | 669 | 96.4 |
| 4 | 평일 저녁 30분. | EMPTY | 0 | 96.3 |
| 5 | 요리 잘 못해. | EMPTY | 0 | 96.4 |
| 6 | 위 정보로 1주 운동 + 식단 표로 추천해줘. | EMPTY | 0 | 96.2 |

### REC-MT-105 (recommendation / student_learning_resource)

| Turn | User (요약) | 분류 | 답 길이 | latency(s) |
|---|---|---|---|---|
| 1 | 학습 자료 추천해줘. | SUCCESS | 739 | 81.6 |
| 2 | 정보 부족하면 먼저 질문해줘. | CLARIFY_SKIPPED(no_question_or_dumped_list) | 644 | 65.8 |
| 3 | 컴퓨터공학 전공 3학년이야. | SUCCESS | 800 | 112.8 |
| 4 | 머신러닝 기초 공부하고 싶어. | EMPTY | 0 | 96.2 |
| 5 | 한국어 자료가 더 편해. 영어도 가능은 함. | EMPTY | 0 | 96.0 |
| 6 | 책보단 무료 강의가 좋아. | EMPTY | 0 | 96.0 |
| 7 | 수학 백그라운드는 미적분/선형대수 학부 수준. | EMPTY | 0 | 96.0 |
| 8 | 위 정보로 학습 자료 3개 추천 + 각각 이유. | EMPTY | 0 | 96.0 |
