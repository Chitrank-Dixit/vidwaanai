import logging
from typing import Any, Dict, List, Optional

from neo4j import GraphDatabase, Driver
from src.core.config import settings

logger = logging.getLogger(__name__)


class GraphManager:
    """Manages Neo4j graph database connections and operations."""

    def __init__(self) -> None:
        """Initialize graph manager with settings."""
        self.uri = settings.NEO4J_URI
        self.user = settings.NEO4J_USER
        self.password = settings.NEO4J_PASSWORD
        self.driver: Optional[Driver] = None

        try:
            self.driver = GraphDatabase.driver(
                self.uri, auth=(self.user, self.password)
            )
            # Verify connection
            self.verify_connection()
            logger.info("Graph manager initialized and connected to Neo4j")
        except Exception as e:
            logger.error(f"Failed to initialize Neo4j driver: {str(e)}")
            raise

    def verify_connection(self) -> None:
        """Verify connectivity to Neo4j."""
        try:
            if self.driver:
                self.driver.verify_connectivity()
        except Exception as e:
            logger.error(f"Neo4j connectivity check failed: {str(e)}")
            raise

    def close(self) -> None:
        """Close Neo4j driver."""
        if self.driver:
            self.driver.close()
            logger.info("Neo4j driver closed")

    def execute_query(
        self, query: str, parameters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Execute a Cypher query and return results as a list of dictionaries."""
        if not self.driver:
            raise Exception("Neo4j driver is not initialized")

        try:
            # Type guard for mypy
            driver = self.driver
            if not driver:
                raise Exception("Neo4j driver is not initialized")

            with driver.session() as session:
                result = session.run(query, parameters or {})
                return [record.data() for record in result]
        except Exception as e:
            logger.error(f"Error executing graph query: {str(e)}")
            raise

    def create_indexes(self) -> None:
        """Create constraints and indexes for the schema."""
        if not self.driver:
            raise Exception("Neo4j driver is not initialized")

        # We will implement index creation logic here or in a separate setup script calling this
        # For now, just a placeholder or basic constraints
        pass
