# Use CheapAIModel with OpenClaw

[OpenClaw](https://github.com/openclaw/openclaw) supports custom OpenAI-compatible providers through its config.

## Setup in 3 steps

1. Export your key:

```bash
export CHEAPAIMODEL_API_KEY="your-key"
```

2. Add a custom provider under `models.providers` in your OpenClaw config:

```json
{
  "models": {
    "providers": {
      "cheapaimodel": {
        "baseUrl": "https://api.cheapaimodel.ai/v1",
        "apiKey": "${CHEAPAIMODEL_API_KEY}",
        "api": "openai-completions",
        "models": [
          { "id": "glm-5.3-flash", "name": "GLM 5.3 Flash" }
        ]
      }
    }
  }
}
```

3. Restart OpenClaw and select `cheapaimodel/glm-5.3-flash` as your model.

Reference: OpenClaw docs, `concepts/model-providers/custom-providers`.
