# Use CheapAIModel with Kilo Code

[Kilo Code](https://github.com/Kilo-Org/kilocode) is an open-source AI coding agent.

## Setup in 3 steps

1. Open **Settings → Providers → Custom provider**.
2. Fill in:
   - **Provider ID:** `cheapaimodel`
   - **Display name:** `CheapAIModel`
   - **Provider API:** OpenAI Compatible
   - **Base URL:** `https://api.cheapaimodel.com/v1`
   - **API key:** your CheapAIModel key
3. Save. Kilo Code loads the available models from `/v1/models` automatically; pick one.

<!-- screenshot: kilo-custom-provider.png -->

Reference: [Kilo Code docs: OpenAI compatible](https://kilo.ai/docs/ai-providers/openai-compatible)
