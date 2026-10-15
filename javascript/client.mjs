import OpenAI from "openai";

export const BASE_URL = process.env.CHEAPAIMODEL_BASE_URL ?? "https://api.cheapaimodel.ai/v1";
export const MODEL = process.env.CHEAPAIMODEL_MODEL ?? "glm-5.3-flash";

export function getClient() {
  const apiKey = process.env.CHEAPAIMODEL_API_KEY;
  if (!apiKey) {
    console.error("Set CHEAPAIMODEL_API_KEY first: export CHEAPAIMODEL_API_KEY=your-key");
    process.exit(1);
  }
  return new OpenAI({ baseURL: BASE_URL, apiKey });
}
