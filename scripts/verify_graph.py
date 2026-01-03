import logging
import sys
import os
from neo4j import GraphDatabase

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def verify_graph():
    logger.info("Connecting to Neo4j...")
    try:
        driver = GraphDatabase.driver(
            settings.NEO4J_URI, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
        )
    except Exception as e:
        logger.error(f"Failed to connect: {e}")
        return

    with driver.session() as session:
        # Count Nodes
        result = session.run("MATCH (n) RETURN count(n) as count")
        node_count = result.single()["count"]
        logger.info(f"Total Nodes: {node_count}")

        # Count Relations
        result = session.run("MATCH ()-[r]->() RETURN count(r) as count")
        rel_count = result.single()["count"]
        logger.info(f"Total Relationships: {rel_count}")

        # Breakdown by Label
        logger.info("--- Node Counts by Label ---")
        result = session.run(
            "MATCH (n) RETURN labels(n) as labels, count(n) as count ORDER BY count DESC"
        )
        for record in result:
            logger.info(f"{record['labels']}: {record['count']}")

        # Show Sample Entities
        logger.info("--- Sample Entities ---")
        result = session.run(
            "MATCH (n) RETURN n.name as name, labels(n) as labels LIMIT 5"
        )
        for record in result:
            logger.info(f"{record['name']} ({record['labels']})")

        # Show Sample Relationships
        logger.info("--- Sample Relationships ---")
        result = session.run(
            "MATCH (a)-[r]->(b) RETURN a.name, type(r), b.name LIMIT 5"
        )
        for record in result:
            logger.info(
                f"{record['a.name']} --[{record['type(r)']}]--> {record['b.name']}"
            )

    driver.close()


if __name__ == "__main__":
    verify_graph()
