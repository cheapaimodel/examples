import { getClient, MODEL } from "./client.mjs";

const client = getClient();

const res = await client.chat.completions.create({
  model: MODEL,
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "Explain what an API is in one sentence." },
  ],
});

console.log(res.choices[0].message.content);
