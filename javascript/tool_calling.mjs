import { getClient, MODEL } from "./client.mjs";

const client = getClient();

function getWeather({ city }) {
  // Replace with a real weather API call.
  return { city, temperature_c: 31, condition: "sunny" };
}

const tools = [
  {
    type: "function",
    function: {
      name: "get_weather",
      description: "Get the current weather for a city",
      parameters: {
        type: "object",
        properties: { city: { type: "string" } },
        required: ["city"],
      },
    },
  },
];

const messages = [{ role: "user", content: "What's the weather in Ho Chi Minh City?" }];

const first = await client.chat.completions.create({ model: MODEL, messages, tools });
const msg = first.choices[0].message;

if (!msg.tool_calls?.length) {
  console.log(msg.content);
  process.exit(0);
}

messages.push(msg);
for (const call of msg.tool_calls) {
  const result = getWeather(JSON.parse(call.function.arguments));
  messages.push({ role: "tool", tool_call_id: call.id, content: JSON.stringify(result) });
}

const final = await client.chat.completions.create({ model: MODEL, messages, tools });
console.log(final.choices[0].message.content);
