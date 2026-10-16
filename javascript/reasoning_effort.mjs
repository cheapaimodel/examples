// Compare DeepSeek V4.1 Flash reasoning effort levels.
//
// Full explanation (costs, caveats, tool-specific setup):
// https://cheapaimodel.ai/blog/deepseek-v4-1-flash-reasoning-effort
//
// reasoning_effort accepts "none", "low", "high" (default) and "max".
// Run:  node reasoning_effort.mjs            # compares low and high
//       node reasoning_effort.mjs none max   # pick your own levels
import { getClient } from "./client.mjs";

const MODEL = "deepseek-v4-1-flash";
const PROMPT =
  "A farmer has 17 sheep. All but 9 run away. How many sheep are left? Answer with one number.";

const client = getClient();
const levels = process.argv.slice(2).length ? process.argv.slice(2) : ["low", "high"];

for (const level of levels) {
  const completion = await client.chat.completions.create({
    model: MODEL,
    reasoning_effort: level,
    messages: [{ role: "user", content: PROMPT }],
    // max_tokens includes reasoning tokens. If you set it too low, the
    // reasoning can use it all up and the answer comes back empty.
  });

  const msg = completion.choices[0].message;
  const reasoningTokens = completion.usage?.completion_tokens_details?.reasoning_tokens ?? 0;

  console.log(`=== reasoning_effort=${level}`);
  console.log(`answer:           ${JSON.stringify(msg.content)}`);
  console.log(`reasoning tokens: ${reasoningTokens}`);
  console.log(`output tokens:    ${completion.usage?.completion_tokens ?? "?"}`);

  // The reasoning text is not in the SDK's types, but the field is there.
  if (msg.reasoning_content) {
    console.log(`reasoning (first 200 chars): ${JSON.stringify(msg.reasoning_content.slice(0, 200))}`);
  }
  console.log();
}
