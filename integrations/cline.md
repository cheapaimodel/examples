# Use CheapAIModel with Cline

[Cline](https://github.com/cline/cline) is an AI coding agent for VS Code.

## Setup in 3 steps

1. Open Cline in VS Code and click the **Settings** (gear) icon.
2. Set **API Provider** to **OpenAI Compatible**.
3. Fill in:
   - **Base URL:** `https://api.cheapaimodel.ai/v1`
   - **API Key:** your CheapAIModel key
   - **Model ID:** for example `glm-5.3-flash` (see the [model list](https://github.com/cheapaimodel/docs/blob/main/models.md))

Click **Done** and start a task.

<!-- screenshot: cline-settings.png -->

## Tips

- Coding agents send long prompts. Pick a model with a large context window.
- If you see `401`, re-check the API key. If you see `404`, re-check the Model ID.

Reference: [Cline docs: OpenAI Compatible](https://docs.cline.bot/provider-config/openai-compatible)
