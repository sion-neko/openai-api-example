import os
import json
import requests

class OpenAIClient:
    def __init__(self, model: str):
        self.model = model
        self.api_key = self._get_api_key()

    def _get_api_key(self) -> str:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("環境変数 OPENAI_API_KEY が設定されていません。")
        return api_key


    def call_openai(self, prompt: str) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            "temperature": 1,
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(payload), timeout=60)
        response.raise_for_status()

        res_json = response.json()
        return res_json["choices"][0]["message"]["content"]


if __name__ == "__main__":
    client = OpenAIClient(model="gpt-5-mini")
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
            reply = client.call_openai(user_input)
        except Exception as e:
            print(f"[ERROR] {e}")
            continue

        print("Assistant:", reply)


