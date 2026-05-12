from openai import OpenAI

client = OpenAI(
    ## 엔드포인트트
    base_url="http://172.20.93.80:8001/v1",
    ## API key (인증없음)
    api_key="EMPTY",
)

r = client.chat.completions.create(
    ## 모델 ID
    model="vaetki20b",
    messages=[
        {"role": "user", "content": "안녕하세요. 자기소개 한 줄로."}
    ],
    ## max_model_len: 16384
    max_tokens=200,
    temperature=0.2,
    timeout=60,
)

print(r.choices[0].message.content)