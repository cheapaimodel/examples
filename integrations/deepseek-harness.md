# Use CheapAIModel with DeepSeek Harness (dsh)

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) is an open-source coding agent with a web UI (`dsh web`).

## Option A: in the web UI (3 steps)

1. Start it with `npx @deepseek-ai/dsh web` and open **Settings → Models → Add model provider → Custom model API**.
2. Fill in:
   - **Provider ID:** `cheapaimodel` (lowercase; it can't be changed later)
   - **Base URL:** `https://api.cheapaimodel.ai/v1`
   - **Protocol:** `openai-completions`
   - **API key:** your CheapAIModel key
3. Click **Fetch available models**, enable `deepseek-v4-1-flash` (or another model) and pick it in the model picker.

## Option B: config file

Export your key, then add this to `~/.dsh/profiles/web/cordis.patch.yml`:

```bash
export CHEAPAIMODEL_API_KEY="your-key"
```

```yaml
- id: llm-pi-ai
  config:
    providers:
      cheapaimodel:
        displayName: CheapAIModel
        apiKeyEnv: CHEAPAIMODEL_API_KEY
        api: openai-completions
        baseURL: https://api.cheapaimodel.ai/v1
        compat:
          supportsDeveloperRole: false
          maxTokensField: max_tokens
        models:
          - id: deepseek-v4-1-flash
            compat:
              thinkingFormat: deepseek
```

Changes apply on the next request; no restart needed.

## Troubleshooting

- `MISSING_CREDENTIAL`: the `CHEAPAIMODEL_API_KEY` variable isn't visible to the dsh process. Export it in the same terminal before starting dsh.
- This patch replaces the whole `llm-pi-ai` entry. If you already configured other providers there, keep them in the same file.

Reference: DeepSeek Harness docs, `docs/user/guide/providers.md` and `docs/config-catalog.md`.
