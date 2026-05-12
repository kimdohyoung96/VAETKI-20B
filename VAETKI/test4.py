import time
import re
from openai import OpenAI

client = OpenAI(
    base_url="http://172.20.93.80:8001/v1",
    api_key="EMPTY",
)

multi_turn_sessions = [
    {
        "session_id": "MT-001",
        "turns": [
            "안녕하세요. 자기소개 한 줄로.",
            "저는 전통 공연을 좋아합니다. 서울에서 볼 만한 공연을 추천해주세요.",
            "너무 비싼 공연은 제외하고 추천해주세요.",
            "부모님과 함께 가기 좋은 공연으로 다시 정리해주세요.",
            "지금까지 조건을 반영해서 최종 추천을 한 줄로 요약해주세요.",
        ],
    },
    {
        "session_id": "MT-002",
        "turns": [
            "서울에서 40대가 즐길만한 문화 활동 3가지를 추천해주세요.",
            "그중 실내 활동만 골라주세요.",
            "비용이 적게 드는 순서대로 정리해주세요.",
            "각 활동별 추천 이유를 짧게 설명해주세요.",
            "최종적으로 가장 추천하는 1개만 골라주세요.",
        ],
    },
]


def detect_repetition(text):
    lines = text.split("\n")
    repeated_lines = len(lines) - len(set(lines))

    words = text.split()
    unique_ratio = len(set(words)) / max(len(words), 1)

    return repeated_lines > 3 or unique_ratio < 0.3


def remove_think_block(text):
    return re.sub(
        r"<think>.*?</think>",
        "",
        text,
        flags=re.DOTALL
    ).strip()


def parse_response(content):
    has_think = "<think>" in content or "</think>" in content

    think_content = ""
    final_content = content

    think_match = re.search(
        r"<think>(.*?)</think>",
        content,
        re.DOTALL
    )

    if think_match:
        think_content = think_match.group(1).strip()
        final_content = remove_think_block(content)

    return has_think, think_content, final_content


for session in multi_turn_sessions:

    session_id = session["session_id"]
    turns = session["turns"]

    print("=" * 120)
    print(f"[SESSION] {session_id}")

    messages = [
        {
            "role": "system",
            "content": (
                "당신은 사용자와 자연스럽게 대화하는 AI 어시스턴트입니다. "
                "내부 추론 과정, reasoning, chain-of-thought, <think> 블록을 출력하지 마세요. "
                "최종 답변만 간결하고 명확하게 작성하세요. "
                "이전 대화의 조건을 반영하되 같은 문장을 반복하지 마세요."
            )
        }
    ]

    for turn_idx, user_prompt in enumerate(turns, 1):

        print("=" * 120)
        print(f"[{session_id} / TURN-{turn_idx}]")
        print(f"User: {user_prompt}")

        messages.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

        start_time = time.time()

        try:
            r = client.chat.completions.create(
                model="vaetki20b",
                messages=messages,

                max_tokens=1024,
                temperature=0.2,
                top_p=0.9,
                timeout=2000,

                # 핵심: 서버 chat template이 지원하면 thinking 비활성화
                extra_body={
                    "chat_template_kwargs": {
                        "enable_thinking": False
                    }
                },

                # no-think 테스트에서는 </think> stop을 쓰지 않는 것을 추천
                # stop=["<|END|>"]
            )

            latency = time.time() - start_time
            content = r.choices[0].message.content or ""

            has_think, think_content, final_content = parse_response(content)

            is_empty = len(final_content.strip()) == 0
            repetition = detect_repetition(content)

            print(f"Latency: {latency:.2f}s")
            print(f"Has <think>: {has_think}")
            print(f"Empty Response: {is_empty}")
            print(f"Repetition Loop: {repetition}")
            print(f"History Turns: {len(messages)}")
            print(f"History Chars: {sum(len(m['content']) for m in messages)}")

            print("-" * 120)
            print("[FINAL RESPONSE]")
            print(final_content[:2000])

            if has_think:
                print("-" * 120)
                print("[WARNING] <think> was still generated.")
                print("[THINK CONTENT]")
                print(think_content[:2000])

            # 다음 턴 history에는 think 제거한 final response만 누적
            messages.append(
                {
                    "role": "assistant",
                    "content": final_content
                }
            )

            if is_empty or repetition:
                print("-" * 120)
                print(f"[STOP SESSION] {session_id} stopped at TURN-{turn_idx}")
                break

        except Exception as e:
            latency = time.time() - start_time

            print("[FAILED]")
            print(f"Latency: {latency:.2f}s")
            print(f"Error: {e}")
            break