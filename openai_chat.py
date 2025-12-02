import os
import json
import requests


API_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-5-mini"


def get_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("環境変数 OPENAI_API_KEY が設定されていません。")
    return api_key


def call_openai(prompt: str) -> str:
    api_key = get_api_key()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 1,
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(payload), timeout=60)
    response.raise_for_status()

    res_json = response.json()
    return res_json["choices"][0]["message"]["content"]


def main():
    print("OpenAI Chat (Ctrl+C で終了)")
    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not user_input.strip():
            continue

        try:
            reply = call_openai(user_input)
        except Exception as e:
            print(f"[ERROR] {e}")
            continue

        print("Assistant:", reply)


if __name__ == "__main__":
    main()


