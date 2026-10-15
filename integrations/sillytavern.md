# Use CheapAIModel with SillyTavern

[SillyTavern](https://github.com/SillyTavern/SillyTavern) is a popular chat and roleplay frontend.

## Setup in 3 steps

1. Open **API Connections** (the plug icon) and set **API** to **Chat Completion**.
2. Set **Chat Completion Source** to **Custom (OpenAI-compatible)**, then fill in:
   - **Custom Endpoint (Base URL):** `https://api.cheapaimodel.com/v1`
   - **Custom API Key:** your CheapAIModel key
   - **Model ID:** `<model-id>` (or click to load available models)
3. Click **Connect**. The status light turns green when it works.

<!-- screenshot: sillytavern-connection.png -->

Reference: [SillyTavern docs: API connections](https://docs.sillytavern.app/usage/api-connections/)
