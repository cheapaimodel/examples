# Use CheapAIModel with Codex CLI

[Codex CLI](https://github.com/openai/codex) is OpenAI's coding agent for the terminal. It talks to custom providers through the **Responses API** (`/v1/responses`).

## Setup in 3 steps

1. Export your key:

```bash
export CHEAPAIMODEL_API_KEY="your-key"
```

2. Add a provider to `~/.codex/config.toml`:

```toml
model_provider = "cheapaimodel"
model = "deepseek-v4-1-flash"

[model_providers.cheapaimodel]
name = "CheapAIModel"
base_url = "https://api.cheapaimodel.ai/v1"
env_key = "CHEAPAIMODEL_API_KEY"
wire_api = "responses"
```

3. Run `codex`.

To try it without changing your defaults, keep only the `[model_providers.cheapaimodel]` table and run:

```bash
codex -c model_provider=cheapaimodel -m deepseek-v4-1-flash
```

## Notes

- `wire_api = "chat"` is no longer supported by Codex. Use `"responses"`.
- The provider IDs `openai`, `ollama` and `lmstudio` are reserved. Keep the ID `cheapaimodel`.
- Coding agents send long prompts and use reasoning. See [reasoning effort](https://cheapaimodel.ai/blog/deepseek-v4-1-flash-reasoning-effort?utm_source=github&utm_medium=examples) for how to tune cost.

Reference: [Codex docs: advanced configuration](https://developers.openai.com/codex/config-advanced)
