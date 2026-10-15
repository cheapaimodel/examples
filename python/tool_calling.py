"""Let the model call a Python function."""
import json

from client import MODEL, get_client

client = get_client()


def get_weather(city: str) -> dict:
    # Replace with a real weather API call.
    return {"city": city, "temperature_c": 31, "condition": "sunny"}


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        },
    }
]

messages = [{"role": "user", "content": "What's the weather in Hanoi?"}]

first = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)
msg = first.choices[0].message

if not msg.tool_calls:
    print(msg.content)
    raise SystemExit

messages.append(msg)
for call in msg.tool_calls:
    args = json.loads(call.function.arguments)
    result = get_weather(**args)
    messages.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(result)})

final = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)
print(final.choices[0].message.content)
