# Use CheapAIModel with Aider

[Aider](https://github.com/Aider-AI/aider) is AI pair programming in your terminal.

## Setup in 3 steps

1. Set the base URL and key:

```bash
export OPENAI_API_BASE="https://api.cheapaimodel.com/v1"
export OPENAI_API_KEY="your-cheapaimodel-key"
```

On Windows (PowerShell):

```powershell
setx OPENAI_API_BASE https://api.cheapaimodel.com/v1
setx OPENAI_API_KEY your-cheapaimodel-key
```

2. Start Aider with the `openai/` prefix in front of the model ID:

```bash
aider --model openai/<model-id>
```

3. Start coding.

Reference: [Aider docs: OpenAI compatible APIs](https://aider.chat/docs/llms/openai-compat.html)
