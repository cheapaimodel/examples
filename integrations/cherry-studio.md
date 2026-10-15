# Use CheapAIModel with Cherry Studio

[Cherry Studio](https://github.com/CherryHQ/cherry-studio) is a desktop AI chat client.

## Setup in 3 steps

1. Open **Settings → Model Services** and click **+ Add** at the bottom of the provider list.
2. Name it `CheapAIModel`, choose provider type **OpenAI**, then fill in:
   - **API Key:** your CheapAIModel key
   - **API Address:** `https://api.cheapaimodel.ai`
3. Click **Manage** (or "Get model list") to load models, add the ones you want, and turn the provider on.

<!-- screenshot: cherry-studio-provider.png -->

## Tip

Cherry Studio adds `/v1` to the API address automatically. If requests fail, try entering the address with `/v1` at the end instead.

Reference: [Cherry Studio docs: custom provider](https://docs.cherryai.com.cn/docs/en-us/pre-basic/providers/zi-ding-yi-fu-wu-shang)
