import time
import re
from openai import OpenAI

client = OpenAI(
    base_url="http://172.20.93.80:8001/v1",
    api_key="EMPTY",
)

##
# 단일턴 테스트
##

test_prompts = [
    "안녕하세요. 자기소개 한 줄로.",
    "서울에서 40대가 즐길만한 문화 활동 3가지를 추천해주세요.",
    "두 수의 합이 20이고 차가 4일 때 두 수를 구하세요.",
    "오늘 날씨가 좋아서 산책을 했다 문장을 자연스럽게 바꿔줘.",
]

def detect_repetition(text):
    """
    간단한 반복 루프 탐지
    """
    lines = text.split("\n")

    # 동일 line 반복 체크
    repeated_lines = len(lines) - len(set(lines))

    # 동일 phrase 반복 체크
    words = text.split()
    unique_ratio = len(set(words)) / max(len(words), 1)

    return repeated_lines > 3 or unique_ratio < 0.3


for idx, prompt in enumerate(test_prompts, 1):

    print("=" * 100)
    print(f"[TEST-{idx}]")
    print(f"Prompt: {prompt}")

    start_time = time.time()

    try:
        r = client.chat.completions.create(
            model="vaetki20b",
            messages=[
                {"role": "user", "content": prompt}
            ],

            # generation setting
            max_tokens=1024,
            temperature=0.2,
            top_p=0.9,

            # timeout
            timeout=120,
        )

        latency = time.time() - start_time

        content = r.choices[0].message.content

        # think block 체크
        has_think = (
            "<think>" in content and "</think>" in content
        )

        # think 내용 추출
        think_content = ""
        final_content = content

        think_match = re.search(
            r"<think>(.*?)</think>",
            content,
            re.DOTALL
        )

        if think_match:
            think_content = think_match.group(1).strip()
            final_content = re.sub(
                r"<think>.*?</think>",
                "",
                content,
                flags=re.DOTALL
            ).strip()

        # 빈 응답 체크
        is_empty = len(final_content.strip()) == 0

        # 반복 루프 체크
        repetition = detect_repetition(content)

        # 출력
        print(f"Latency: {latency:.2f}s")
        print(f"Has <think>: {has_think}")
        print(f"Empty Response: {is_empty}")
        print(f"Repetition Loop: {repetition}")

        print("-" * 100)
        print("[FINAL RESPONSE]")
        print(final_content[:2000])

        if has_think:
            print("-" * 100)
            print("[THINK CONTENT]")
            print(think_content[:2000])

    except Exception as e:

        latency = time.time() - start_time

        print(f"[FAILED]")
        print(f"Latency: {latency:.2f}s")
        print(f"Error: {e}")