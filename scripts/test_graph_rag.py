import logging
import sys
import os

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.core.config import settings
from src.agent.vidwaan_agent import VidwaanAI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_graph_rag():
    logger.info("Initializing Agent with Graph RAG...")
    
    agent = VidwaanAI(
        db_url=settings.DATABASE_URL,
        openai_key="lm-studio", # Placeholder for local
        use_lmstudio=True,
        lmstudio_url=settings.lmstudio_base_url,
        enable_graph_rag=True,
        neo4j_uri=settings.NEO4J_URI,
        neo4j_user=settings.NEO4J_USER,
        neo4j_password=settings.NEO4J_PASSWORD
    )

    query = "How is Krishna related to Arjuna?"
    logger.info(f"Querying: {query}")
    
    result = agent.query(query, verbose=True)
    
    print("\n\n=== AGENT RESPONSE ===")
    print(result['answer'])
    print("======================\n")
    
    # Check logs for "Graph RAG: Retrieved ..." to verify internal logic

if __name__ == "__main__":
    test_graph_rag()
