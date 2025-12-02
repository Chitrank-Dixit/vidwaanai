import sys
import os
import time
from typing import Any

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.config import settings
from src.core.logger import get_logger
from src.db.db_manager import DatabaseManager
from src.graph.graph_builder import GraphBuilder
from src.graph.entity_extractor import EntityExtractor
from src.llm.lmstudio_client import LMStudioClient
from src.llm.openai_client import OpenAIClient

logger = get_logger(__name__)


def build_graph() -> None:
    """Build knowledge graph from existing scripture data."""
    logger.info("Starting graph population...")

    # Initialize components
    db = DatabaseManager(settings.DATABASE_URL)

    if not settings.NEO4J_URI:
        logger.error("Neo4j URI not configured.")
        return

    try:
        graph_builder = GraphBuilder(
            settings.NEO4J_URI, settings.NEO4J_USER, settings.NEO4J_PASSWORD
        )
    except Exception as e:
        logger.error(f"Failed to connect to Neo4j: {e}")
        return

    # Initialize LLM for extraction
    llm: Any
    if settings.llm_backend == "lmstudio":
        llm = LMStudioClient(base_url=settings.lmstudio_base_url)
    else:
        llm = OpenAIClient(api_key=str(settings.OPENAI_API_KEY))

    entity_extractor = EntityExtractor(llm)

    # Get all verses
    verses = db.get_all_verses()
    logger.info(f"Found {len(verses)} verses to process")

    for i, verse in enumerate(verses):
        try:
            logger.info(
                f"Processing verse {i + 1}/{len(verses)}: {verse['scripture_name']} {verse['chapter_number']}.{verse['verse_number']}"
            )

            # Extract entities and relationships
            extracted = entity_extractor.extract_entities(
                verse["text"], verse["translation"], verse["scripture_name"]
            )

            # Helper to extract name string
            def get_name_str(entity_name: Any) -> str:
                if isinstance(entity_name, str):
                    return entity_name
                if isinstance(entity_name, dict):
                    return str(entity_name.get("primary", str(entity_name)))
                return str(entity_name)

            # Add to graph
            for entity in extracted.get("entities", []):
                name = get_name_str(entity["name"])
                if entity["type"] == "Person":
                    graph_builder.create_person(name, entity.get("attributes", {}))
                elif entity["type"] == "Concept":
                    graph_builder.create_concept(name, entity.get("attributes", {}))
                elif entity["type"] == "Event":
                    graph_builder.create_event(name, entity.get("attributes", {}))
                elif entity["type"] == "Location":
                    graph_builder.create_location(name, entity.get("attributes", {}))

            for rel in extracted.get("relationships", []):
                if not all(k in rel for k in ("from", "to", "type")):
                    logger.warning(f"Skipping incomplete relationship: {rel}")
                    continue

                from_name = get_name_str(rel["from"])
                to_name = get_name_str(rel["to"])

                graph_builder.create_relationship(
                    from_name, to_name, rel["type"], rel.get("attributes", {})
                )

            # Rate limiting if using OpenAI
            if settings.llm_backend == "openai":
                time.sleep(1)

        except Exception as e:
            logger.error(f"Error processing verse {verse['id']}: {e}")
            continue

    graph_builder.close()
    logger.info("✓ Knowledge graph built successfully!")


if __name__ == "__main__":
    build_graph()
