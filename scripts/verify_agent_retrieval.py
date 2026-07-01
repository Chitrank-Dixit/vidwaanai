import os
import sys

# Add src to python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent.vidwaan_agent import VidwaanAI
from src.core.config import settings


def main():
    print("Initializing VidwaanAI Agent for retrieval verification...")

    # Initialize the real agent with local DB and Neo4j connections
    agent = VidwaanAI(
        db_url=settings.DATABASE_URL,
        openai_key=settings.OPENAI_API_KEY or "dummy",
        neo4j_uri=settings.NEO4J_URI,
        neo4j_user=settings.NEO4J_USER,
        neo4j_password=settings.NEO4J_PASSWORD,
        enable_graph_rag=True,
    )

    # Mock the LLM generate call to inspect the synthesized context
    def mock_generate(prompt, max_tokens=500, temperature=0.3):
        if "Extract key entities" in prompt:
            if "Rama" in prompt or "Vishnu" in prompt:
                return '[{"name": "Rama", "type": "Person"}, {"name": "Vishnu", "type": "Deity"}]'
            elif "Dharma" in prompt:
                return '[{"name": "Dharma", "type": "Concept"}]'
            return "[]"
        else:
            print("\n" + "=" * 80)
            print("SYNTHESIZED RAG PROMPT SENT TO LLM:")
            print("=" * 80)
            print(prompt)
            print("=" * 80 + "\n")
            return "Rama is the avatar of Lord Vishnu, representing cosmic righteousness (Dharma)."

    agent.llm.generate = mock_generate

    print("\n--- Running Query 1: How is Rama related to Vishnu? ---")
    res1 = agent.query("How is Rama related to Vishnu?", verbose=True)
    print("Answer Returned:", res1["answer"])

    print("\n--- Running Query 2: What is the concept of Dharma? ---")
    res2 = agent.query("What is the concept of Dharma?", verbose=True)
    print("Answer Returned:", res2["answer"])

    agent.close()


if __name__ == "__main__":
    main()
