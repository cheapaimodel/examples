"""Stream tokens as they are generated."""
from client import MODEL, get_client

client = get_client()

stream = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Write a short poem about cheap but powerful AI."}],
    stream=True,
)

for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
