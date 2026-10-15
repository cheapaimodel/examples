"""Use CheapAIModel as the LLM in LangChain."""
import os

from langchain_openai import ChatOpenAI

from client import BASE_URL, MODEL

api_key = os.getenv("CHEAPAIMODEL_API_KEY")
if not api_key:
    raise SystemExit("Set CHEAPAIMODEL_API_KEY first")

llm = ChatOpenAI(model=MODEL, base_url=BASE_URL, api_key=api_key)

print(llm.invoke("Give me three startup ideas using AI.").content)
