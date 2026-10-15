"""Basic chat completion."""
from client import MODEL, get_client

client = get_client()

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain what an API is in one sentence."},
    ],
)

print(response.choices[0].message.content)
if response.usage:
    print(f"\nTokens used: {response.usage.total_tokens}")
