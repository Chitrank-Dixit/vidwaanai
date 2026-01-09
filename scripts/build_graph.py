import logging
import sys
import os

# Ensure src is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.config import settings
from src.db.db_manager import DatabaseManager
from src.graph.graph_builder import GraphBuilder
from src.graph.graph_ingestor import GraphIngestor
from src.graph.entity_extractor import EntityExtractor
from src.llm.openai_client import OpenAIClient

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info("Starting Graph Build Process...")

    # 1. Initialize Components
    db = DatabaseManager(settings.DATABASE_URL)

    # Needs LLM for Entity Extractor
    if settings.OPENAI_API_KEY:
        llm = OpenAIClient(api_key=settings.OPENAI_API_KEY)
    else:
        logger.warning(
            "No OPENAI_API_KEY found. Entity extraction might fail if not using local fallback."
        )
        llm = None  # Or mock/raise

    extractor = EntityExtractor(llm_client=llm)

    builder = GraphBuilder(
        uri=settings.NEO4J_URI,
        user=settings.NEO4J_USER,
        password=settings.NEO4J_PASSWORD,
    )

    ingestor = GraphIngestor(db, builder, extractor)

    # 2. Run Ingestion
    # Start small for testing
    limit = 20
    logger.info(f"Ingesting up to {limit} mantras...")
    stats = ingestor.ingest_all_mantras(batch_size=5, limit=limit)

    logger.info(f"Build Complete. Stats: {stats}")
    builder.close()


if __name__ == "__main__":
    main()
