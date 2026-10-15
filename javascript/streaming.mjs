import { getClient, MODEL } from "./client.mjs";

const client = getClient();

const stream = await client.chat.completions.create({
  model: MODEL,
  messages: [{ role: "user", content: "Write a short poem about cheap but powerful AI." }],
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
process.stdout.write("\n");
