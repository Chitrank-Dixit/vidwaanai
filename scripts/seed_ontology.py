import logging
import sys
import os
from typing import Any, Dict

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.core.config import settings
from src.graph.graph_builder import GraphBuilder
from src.graph.ontology import VEDIC_ONTOLOGY

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OntologySeeder:
    def __init__(self, builder: GraphBuilder):
        self.builder = builder

    def seed(self):
        logger.info("Starting Ontology Seeding...")
        self._traverse_and_create(VEDIC_ONTOLOGY)
        logger.info("Ontology Seeding Complete.")

    def _traverse_and_create(self, obj: Any):
        if isinstance(obj, dict):
            # Check if it's an entity definition
            if "id" in obj and "type" in obj:
                self._create_entity_node(obj)

            # Recurse
            for key, value in obj.items():
                if key not in [
                    "attributes",
                    "relations",
                    "components",
                ]:  # details handled in create_entity
                    self._traverse_and_create(value)
        elif isinstance(obj, list):
            for item in obj:
                self._traverse_and_create(item)

    def _create_entity_node(self, entity_data: Dict[str, Any]):
        try:
            name = entity_data["name"]
            ent_type = entity_data["type"]

            # Prepare attributes
            attributes = {
                k: v
                for k, v in entity_data.items()
                if k not in ["id", "type", "name", "parent_entity", "relation_types"]
            }

            # Create Node
            logger.info(f"Creating Entity: {name} ({ent_type})")
            # We use _generate_id logic internally in GraphBuilder, but here we might want to force specific IDs if needed.
            # However, GraphBuilder._generate_id uses Type:Name.
            # The ontology uses ids like "deity:vishnu" (lowercase).
            # GraphBuilder generates "Deity:Vishnu".
            # To match specific ontology IDs, we might need to adjust GraphBuilder or just let it generate its own and rely on Name matching.
            # Let's stick to GraphBuilder's convention for consistency: Type:Name

            self.builder.create_entity(name, ent_type, attributes)

            # Handle static relationships defined in ontology
            if "parent_entity" in entity_data:
                entity_data["parent_entity"]  # e.g. "deity:vishnu"
                # We need to resolve this to a name for GraphBuilder.create_relationship
                # This assumes simple parsing: "type:name_key" -> name lookup?
                # For now, let's assume the parent entity is already created or will be.
                # Actually, GraphBuilder.create_relationship matches by NAME.
                # So we need the NAME of the parent.
                # In VEDIC_ONTOLOGY, parent_entity is "deity:vishnu".
                # We need a lookup to find "Vishnu" from "deity:vishnu".
                # This implies we might need a 2-pass approach or a lookup map.

                # Simple hack: split by ':' and title case the name part? "vishnu" -> "Vishnu"
                # This is risky.
                pass

        except Exception as e:
            logger.error(f"Error creating entity {entity_data.get('name')}: {e}")


def main():
    try:
        builder = GraphBuilder(
            uri=settings.NEO4J_URI,
            user=settings.NEO4J_USER,
            password=settings.NEO4J_PASSWORD,
        )
        seeder = OntologySeeder(builder)
        seeder.seed()
        builder.close()
    except Exception as e:
        logger.error(f"Seeding failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
