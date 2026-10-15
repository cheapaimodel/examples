# Use CheapAIModel with Open WebUI

[Open WebUI](https://github.com/open-webui/open-webui) is a self-hosted AI chat interface.

## Setup in 3 steps

1. Go to **Admin Settings → Connections → Manage OpenAI API Connections** and click **➕ Add Connection**.
2. Fill in:
   - **URL:** `https://api.cheapaimodel.ai/v1`
   - **API Key:** your CheapAIModel key
   - **Model IDs:** leave empty to load all models, or add the ones you want
3. Click **Verify Connection**, save, and pick a model in a new chat.

<!-- screenshot: open-webui-connection.png -->

Reference: [Open WebUI docs: OpenAI-compatible providers](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible)
