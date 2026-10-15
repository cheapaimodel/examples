"""A tiny terminal chatbot that remembers the conversation."""
from client import MODEL, get_client

client = get_client()
history = [{"role": "system", "content": "You are a friendly assistant."}]

print(f"Chatting with {MODEL}. Type 'exit' to quit.\n")
while True:
    user = input("You: ").strip()
    if user.lower() in {"exit", "quit"}:
        break
    if not user:
        continue
    history.append({"role": "user", "content": user})

    print("AI: ", end="", flush=True)
    reply = ""
    for chunk in client.chat.completions.create(model=MODEL, messages=history, stream=True):
        if chunk.choices and chunk.choices[0].delta.content:
            piece = chunk.choices[0].delta.content
            reply += piece
            print(piece, end="", flush=True)
    print("\n")
    history.append({"role": "assistant", "content": reply})
