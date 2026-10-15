"""우리 학교 소개 쳇봇 만들기

uv run ex06   (끝낼 때 /bye)
"""

import ollama

MODEL = "qwen3.5:2b"

messages = [
    {"role": "system", "content": "한국어로 짧게 답한다."},
    {"role": "system", "content": "너는 원광대학교를 소개하는 챗봇이다. "
        "원광대학교는 1946년에 설립된 전북특별자치도 익산시에 위치한 사립대학교이다. "
        "확인되지 않은 정보를 사실처럼 지어내지 말고, 정확히 모르는 정보는 모른다고 답하고, "
        "최신 정보나 정확한 통계는 원광대학교 공식 홈페이지에서 확인하도록 안내하자."}
]


def main() ->None:
    while True:
        text = input("나> ").strip()
        if text == "/bye":
            break
        if not text:
            continue
        messages.append({"role": "user", "content": text})
        request = messages  # 기억 끄기 비교: [messages[0], messages[-1]] (규칙과 이번 질문만)
        print(f"(보내는 메시지 {len(request)}개)")
        response = ollama.chat(model=MODEL, messages=request, think=False)
        answer = response.message.content
        print("AI>", answer)
        messages.append({"role": "assistant", "content": answer})  # 답도 쌓아야 다음에 기억한다

