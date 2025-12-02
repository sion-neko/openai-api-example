## OpenAI Chat API サンプル（公式Pythonライブラリ不使用）

このプロジェクトは、**OpenAI の公式 Python ライブラリを使わずに** `requests` で直接 HTTP リクエストを送り、
Chat Completions API（GPT-4.1 など）を叩く最小限のサンプルです。

### 1. 準備

- OpenAI API キーを環境変数に設定

**Windows (PowerShell):**

```powershell
$env:OPENAI_API_KEY = "sk-xxxx"
```

**Windows (cmd.exe):**

```bat
set OPENAI_API_KEY=sk-xxxx
```

**Linux / macOS (bash / zsh など):**

```bash
export OPENAI_API_KEY="sk-xxxx"
```

永続的に設定したい場合は、`~/.bashrc` や `~/.zshrc` などのシェル設定ファイルに上記行を追記し、再読み込みしてください。

### 2. 実行方法

```bash
python openai_chat.py
```

コンソール上でプロンプト（質問）を入力すると、OpenAI の返答が表示されます。

### 3. コード概要

- `openai_chat.py`
  - `call_openai(prompt: str) -> str`  
    OpenAI Chat Completions API にリクエストを送り、アシスタントの返答テキストを返します。
  - `MODEL` 定数で使用するモデル（例: `gpt-4.1-mini`）を変更できます。


