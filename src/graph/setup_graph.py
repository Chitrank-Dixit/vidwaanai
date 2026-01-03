import logging
import sys
import os

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from src.graph.graph_manager import GraphManager
from src.graph.schema import EntityType

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup_graph_schema():
    """Setup graph schema constraints and indexes."""
    logger.info("Initializing Graph Manager...")
    try:
        graph_manager = GraphManager()
    except Exception as e:
        logger.error(f"Failed to connect to Neo4j: {e}")
        return

    logger.info("Setting up constraints for Entity Types...")

    # Universal constraint on Entity ID
    # We want uniqueness on the 'id' property for ALL nodes labeled 'Entity' (if we use a base label)
    # Or specifically for each sub-label if we don't use a base label.
    # Let's apply for each specific Type.

    for entity_type in EntityType:
        label = entity_type.value
        try:
            # Create constraint: Ensure 'id' is unique for each label
            query = f"CREATE CONSTRAINT {label}_id_unique IF NOT EXISTS FOR (n:{label}) REQUIRE n.id IS UNIQUE"
            graph_manager.execute_query(query)
            logger.info(f"Created constraint for {label}: id IS UNIQUE")

            # Create index on 'name' for fast lookups
            query_index = f"CREATE INDEX {label}_name_index IF NOT EXISTS FOR (n:{label}) ON (n.name)"
            graph_manager.execute_query(query_index)
            logger.info(f"Created index for {label}: name")

        except Exception as e:
            logger.error(f"Failed to setup constraints for {label}: {e}")

    logger.info("Graph schema setup complete.")
    graph_manager.close()


if __name__ == "__main__":
    setup_graph_schema()
