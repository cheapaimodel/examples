# Use CheapAIModel with opencode

[opencode](https://opencode.ai) is an AI coding agent for the terminal.

## Setup in 3 steps

1. Run `/connect`, choose **Other**, enter the provider ID `cheapaimodel` and paste your API key.
2. Add the provider to `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "cheapaimodel": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "CheapAIModel",
      "options": {
        "baseURL": "https://api.cheapaimodel.ai/v1"
      },
      "models": {
        "glm-5.3-flash": { "name": "GLM 5.3 Flash" }
      }
    }
  }
}
```

3. Run `/models` and pick a CheapAIModel model.

Reference: [opencode docs: custom provider](https://opencode.ai/docs/providers#custom-provider)
