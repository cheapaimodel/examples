# Use CheapAIModel with LibreChat

[LibreChat](https://github.com/danny-avila/LibreChat) supports custom endpoints in `librechat.yaml`.

## Setup in 3 steps

1. Add your key to `.env`:

```bash
CHEAPAIMODEL_API_KEY=your-key
```

2. Add a custom endpoint to `librechat.yaml`:

```yaml
endpoints:
  custom:
    - name: "CheapAIModel"
      apiKey: "${CHEAPAIMODEL_API_KEY}"
      baseURL: "https://api.cheapaimodel.com/v1"
      models:
        default: ["<model-id>"]
        fetch: true
      titleConvo: true
      titleModel: "current_model"
      modelDisplayLabel: "CheapAIModel"
```

3. Restart LibreChat and choose **CheapAIModel** in the endpoint menu.

Reference: [LibreChat docs: custom endpoints](https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints)
