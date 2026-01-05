import logging
import sys
import os

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.agent.vidwaan_agent import VidwaanAI
from src.core.config import settings

logging.basicConfig(level=logging.INFO)


def test_query():
    print("\n--- Initializing Vidwaan Agent ---")
    agent = VidwaanAI(
        db_url=settings.DATABASE_URL,
        openai_key=settings.OPENAI_API_KEY,
        use_lmstudio=True,
        lmstudio_url=settings.lmstudio_base_url,
    )

    query = "What does Rig Veda say about Agni?"
    print(f"\n--- Query: {query} ---")

    response = agent.query(query)

    print("\n--- Response ---")
    print(response["answer"])

    print("\n--- Retrieved Sources ---")
    for source in response["retrieved_verses"]:
        scripture = source.get("scripture", "Unknown")
        ref = f"{source.get('chapter', '')}:{source.get('verse', '')}"
        text = source.get("translation", source.get("text", ""))
        score = source.get("similarity", 0)
        print(f"- {scripture} ({ref}): {text[:100]}... (Score: {score:.3f})")


if __name__ == "__main__":
    test_query()
