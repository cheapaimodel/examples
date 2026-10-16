"""Compare DeepSeek V4.1 Flash reasoning effort levels.

Full explanation (costs, caveats, tool-specific setup):
https://cheapaimodel.ai/blog/deepseek-v4-1-flash-reasoning-effort

reasoning_effort accepts "none", "low", "high" (default) and "max".
Run:  python reasoning_effort.py            # compares low and high
      python reasoning_effort.py none max   # pick your own levels
"""
import sys

from client import get_client

MODEL = "deepseek-v4-1-flash"
PROMPT = "A farmer has 17 sheep. All but 9 run away. How many sheep are left? Answer with one number."

client = get_client()
levels = sys.argv[1:] or ["low", "high"]

for level in levels:
    completion = client.chat.completions.create(
        model=MODEL,
        reasoning_effort=level,
        messages=[{"role": "user", "content": PROMPT}],
        # max_tokens includes reasoning tokens. If you set it too low, the
        # reasoning can use it all up and the answer comes back empty.
    )
    msg = completion.choices[0].message
    details = completion.usage.completion_tokens_details if completion.usage else None
    reasoning_tokens = getattr(details, "reasoning_tokens", 0) or 0

    print(f"=== reasoning_effort={level}")
    print(f"answer:           {msg.content!r}")
    print(f"reasoning tokens: {reasoning_tokens}")
    print(f"output tokens:    {completion.usage.completion_tokens if completion.usage else '?'}")

    # The reasoning text is not in the SDK's types, but the field is there.
    reasoning = getattr(msg, "reasoning_content", None)
    if reasoning:
        print(f"reasoning (first 200 chars): {reasoning[:200]!r}")
    print()

# Turning thinking off: use reasoning_effort="none" OR DeepSeek's own switch,
# never both at once:
#
#   client.chat.completions.create(
#       model=MODEL,
#       messages=[...],
#       extra_body={"thinking": {"type": "disabled"}},
#   )
