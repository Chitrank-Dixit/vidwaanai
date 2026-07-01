import logging
import os
import sys
from typing import Any

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
        id_to_entity = {}

        # Pass 1: Build lookup registry and create all entity nodes
        logger.info("Pass 1: Creating entity nodes...")
        self._collect_and_create_nodes(VEDIC_ONTOLOGY, id_to_entity)

        # Pass 2: Create static relationships using registry
        logger.info("Pass 2: Creating relationship links...")
        self._create_relationships(VEDIC_ONTOLOGY, id_to_entity)

        logger.info("Ontology Seeding Complete.")

    def _collect_and_create_nodes(
        self, obj: Any, id_to_entity: dict[str, dict[str, Any]]
    ):
        if isinstance(obj, dict):
            if "id" in obj and "type" in obj and "name" in obj:
                entity_id = obj["id"]
                name = obj["name"]
                ent_type = obj["type"]

                # Registry lookup
                id_to_entity[entity_id] = {"name": name, "type": ent_type}

                # Prepare attributes
                attributes = {
                    k: v
                    for k, v in obj.items()
                    if k
                    not in [
                        "id",
                        "type",
                        "name",
                        "parent_entity",
                        "relation_types",
                        "relations",
                    ]
                }

                # Create Node
                logger.info(f"Creating Entity: {name} ({ent_type})")
                self.builder.create_entity(name, ent_type, attributes)

            for key, value in obj.items():
                if key not in ["attributes", "relations", "components"]:
                    self._collect_and_create_nodes(value, id_to_entity)
        elif isinstance(obj, list):
            for item in obj:
                self._collect_and_create_nodes(item, id_to_entity)

    def _create_relationships(self, obj: Any, id_to_entity: dict[str, dict[str, Any]]):
        if isinstance(obj, dict):
            if "id" in obj and "name" in obj:
                name = obj["name"]

                # 1. Handle parent_entity relationships (e.g. Manifestation/Avatar)
                if "parent_entity" in obj:
                    parent_id = obj["parent_entity"]
                    if parent_id in id_to_entity:
                        parent_info = id_to_entity[parent_id]
                        parent_name = parent_info["name"]

                        # Determine relation type
                        rel_type = "MANIFESTS_AS"
                        if (
                            "relation_types" in obj
                            and isinstance(obj["relation_types"], list)
                            and obj["relation_types"]
                        ):
                            rel_type = obj["relation_types"][0]

                        logger.info(
                            f"Linking relationship: {name} --[{rel_type}]--> {parent_name}"
                        )
                        self.builder.create_relationship(
                            from_name=name,
                            to_name=parent_name,
                            rel_type=rel_type,
                            attributes={"source": "ontology_static"},
                        )

                # 2. Handle generic relations list (e.g. Atman --[IS_ASPECT_OF]-> Brahman)
                if "relations" in obj and isinstance(obj["relations"], list):
                    for rel_str in obj["relations"]:
                        if ":" in rel_str:
                            rel_type, target_id = rel_str.split(":", 1)
                            if target_id in id_to_entity:
                                target_name = id_to_entity[target_id]["name"]
                                logger.info(
                                    f"Linking relationship: {name} --[{rel_type}]--> {target_name}"
                                )
                                self.builder.create_relationship(
                                    from_name=name,
                                    to_name=target_name,
                                    rel_type=rel_type,
                                    attributes={"source": "ontology_static"},
                                )

            for key, value in obj.items():
                if key not in ["attributes", "relations", "components"]:
                    self._create_relationships(value, id_to_entity)
        elif isinstance(obj, list):
            for item in obj:
                self._create_relationships(item, id_to_entity)


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
