"""Shared client setup for all Python examples."""
import os

from openai import OpenAI

BASE_URL = os.getenv("CHEAPAIMODEL_BASE_URL", "https://api.cheapaimodel.com/v1")
MODEL = os.getenv("CHEAPAIMODEL_MODEL", "gpt-4o-mini")


def get_client() -> OpenAI:
    api_key = os.getenv("CHEAPAIMODEL_API_KEY")
    if not api_key:
        raise SystemExit("Set CHEAPAIMODEL_API_KEY first: export CHEAPAIMODEL_API_KEY=your-key")
    return OpenAI(base_url=BASE_URL, api_key=api_key)
