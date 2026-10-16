# CheapAIModel Examples

Ready-to-run examples for the CheapAIModel API. Every example uses the official OpenAI SDK — only the base URL and API key change.

## Setup

```bash
export CHEAPAIMODEL_API_KEY="your-key"
# optional: pick a model (default: glm-5.3-flash)
export CHEAPAIMODEL_MODEL="glm-5.3-flash"
```

## Python

```bash
cd python
pip install -r requirements.txt
python chat.py
```

| File | Shows |
| --- | --- |
| [chat.py](python/chat.py) | Basic chat completion |
| [streaming.py](python/streaming.py) | Streaming tokens as they arrive |
| [tool_calling.py](python/tool_calling.py) | Function / tool calling |
| [multi_turn.py](python/multi_turn.py) | Simple chatbot in the terminal |
| [langchain_chat.py](python/langchain_chat.py) | Using CheapAIModel with LangChain |
| [reasoning_effort.py](python/reasoning_effort.py) | Compare DeepSeek V4.1 Flash reasoning effort levels ([blog post](https://cheapaimodel.ai/blog/deepseek-v4-1-flash-reasoning-effort?utm_source=github&utm_medium=examples)) |

## JavaScript / TypeScript

```bash
cd javascript
npm install
node chat.mjs
```

| File | Shows |
| --- | --- |
| [chat.mjs](javascript/chat.mjs) | Basic chat completion |
| [streaming.mjs](javascript/streaming.mjs) | Streaming tokens as they arrive |
| [tool_calling.mjs](javascript/tool_calling.mjs) | Function / tool calling |
| [reasoning_effort.mjs](javascript/reasoning_effort.mjs) | Compare DeepSeek V4.1 Flash reasoning effort levels ([blog post](https://cheapaimodel.ai/blog/deepseek-v4-1-flash-reasoning-effort?utm_source=github&utm_medium=examples)) |

## cURL

See [curl/README.md](curl/README.md).

## Use with other tools

Step-by-step setup guides for Cline, Codex CLI, DeepSeek Harness, Kilo Code, opencode, OpenClaw, Aider, Cherry Studio, LobeHub, SillyTavern, Open WebUI, LibreChat and Chatbox: see [integrations/](integrations/README.md).

## License

MIT
