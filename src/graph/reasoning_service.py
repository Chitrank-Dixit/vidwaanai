import logging
from typing import Any

from src.graph.graph_manager import GraphManager
from src.graph.schema import RelationType

logger = logging.getLogger(__name__)


class GraphReasoningService:
    """
    Advanced Logic for Knowledge Graph:
    - Path Finding
    - Multi-hop Reasoning
    - Hierarchy Resolution
    """

    def __init__(self, graph_manager: GraphManager) -> None:
        self.gm = graph_manager

    def get_entity_details(self, entity_id: str, depth: int = 1) -> dict[str, Any]:
        """Fetch entity with its neighborhood."""
        # Check if entity exists
        query_node = "MATCH (n) WHERE n.id = $id RETURN properties(n) as entity"
        result = self.gm.execute_query(query_node, {"id": entity_id})

        if not result:
            return {}

        entity = result[0]["entity"]

        # Determine neighbor query based on Depth
        query_neighbors = """
        MATCH (n)-[r]-(m)
        WHERE n.id = $id
        RETURN 
          properties(startNode(r)) as source,
          type(r) as rel_type,
          properties(r) as rel_properties,
          properties(endNode(r)) as target,
          elementId(r) as rel_id
        """

        rels_result = self.gm.execute_query(query_neighbors, {"id": entity_id})

        outgoing = []
        incoming = []

        for record in rels_result:
            source = record["source"]
            target = record["target"]
            rel_type = record["rel_type"]
            rel_properties = record["rel_properties"]
            rel_id = record["rel_id"]

            # Format manually
            rel_data = {
                "id": rel_id,
                "type": rel_type,
                "properties": rel_properties,
                "source": source,
                "target": target,
            }

            # Determine direction relative to central node
            if source["id"] == entity_id:
                outgoing.append(rel_data)
            else:
                incoming.append(rel_data)

        return {
            "entity": entity,
            "outgoing": outgoing,
            "incoming": incoming,
        }

    def find_shortest_path(
        self, start_id: str, end_id: str, max_hops: int = 5
    ) -> dict[str, Any]:
        """Find Shortest Path between two nodes."""
        query = f"""
        MATCH (start {{id: $start_id}}), (end {{id: $end_id}})
        MATCH p = shortestPath((start)-[*..{max_hops}]-(end))
        RETURN 
          [n in nodes(p) | properties(n)] as path_nodes,
          [r in relationships(p) | {{
             type: type(r),
             start: startNode(r).name,
             end: endNode(r).name,
             properties: properties(r)
          }}] as path_rels,
          length(p) as len
        """

        result = self.gm.execute_query(query, {"start_id": start_id, "end_id": end_id})

        if not result:
            return {"found": False, "path": []}

        nodes = result[0]["path_nodes"]
        rels = result[0]["path_rels"]
        length = result[0]["len"]

        return {"found": True, "length": length, "nodes": nodes, "relationships": rels}

    def search_entities(self, name_query: str, limit: int = 10) -> list[dict[str, Any]]:
        """Fuzzy search for entities by name."""
        query = """
        MATCH (n)
        WHERE toLower(n.name) CONTAINS toLower($q)
        RETURN properties(n) as node
        LIMIT $limit
        """
        result = self.gm.execute_query(query, {"q": name_query, "limit": limit})
        return [r["node"] for r in result]

    def reason_about_entity(self, entity_id: str, hops: int = 2) -> dict[str, Any]:
        """
        Explore implications around an entity.
        Finds nodes connected up to `hops` distance,
        prioritizing causal relations (LEADS_TO, CAUSES, etc).
        """
        implication_rels = [
            RelationType.CAUSES.value,
            RelationType.LEADS_TO.value,
            RelationType.MANIFESTS_AS.value,
            RelationType.IS_A.value,
        ]
        rel_types_str = "|".join(implication_rels)

        query = f"""
        MATCH p = (start {{id: $id}})-[:{rel_types_str}*1..{hops}]->(target)
        RETURN [n in nodes(p) | n.name] as names
        LIMIT 20
        """

        results = self.gm.execute_query(query, {"id": entity_id})

        paths = []
        for rec in results:
            names = rec["names"]
            path_str = " -> ".join([f"({name})" for name in names])
            paths.append(path_str)

        return {"entity_id": entity_id, "implications": paths}

    def get_hierarchy(self, concept_id: str) -> dict[str, Any]:
        """
        Resolve IS_A / PART_OF hierarchy.
        Find parents (generalization) and children (specialization).
        """
        # Parents: node -> IS_A -> parent
        q_parents = """
        MATCH (n {id: $id})-[:IS_A|PART_OF]->(parent)
        RETURN properties(parent) as parent
        """
        # Children: child -> IS_A -> node
        q_children = """
        MATCH (child)-[:IS_A|PART_OF]->(n {id: $id})
        RETURN properties(child) as child
        """

        parents = [
            r["parent"] for r in self.gm.execute_query(q_parents, {"id": concept_id})
        ]
        children = [
            r["child"] for r in self.gm.execute_query(q_children, {"id": concept_id})
        ]

        return {"concept_id": concept_id, "parents": parents, "children": children}
