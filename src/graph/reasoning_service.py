import logging
from typing import Any, Dict, List
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

    def get_entity_details(self, entity_id: str, depth: int = 1) -> Dict[str, Any]:
        """Fetch entity with its neighborhood."""
        # Check if entity exists
        query_node = "MATCH (n) WHERE n.id = $id RETURN n"
        result = self.gm.execute_query(query_node, {"id": entity_id})

        if not result:
            return {}

        entity = result[0]["n"]

        # Determine neighbor query based on Depth
        # For Depth 1 (Immediate neighbors)
        query_neighbors = """
        MATCH (n)-[r]-(m)
        WHERE n.id = $id
        RETURN startNode(r) as source, r, endNode(r) as target
        """
        # If depth > 1 is strictly required, path algorithms are better,
        # but for viewing details, 1-hop is standard.

        rels_result = self.gm.execute_query(query_neighbors, {"id": entity_id})

        outgoing = []
        incoming = []

        for record in rels_result:
            source = record["source"]
            target = record["target"]
            rel = record["r"]

            # Format manually
            rel_data = {
                "id": rel.element_id,  # or rel.id
                "type": rel.type,
                "properties": dict(rel.items()),
                "source": dict(source.items()),
                "target": dict(target.items()),
            }

            # Determine direction relative to central node
            if source["id"] == entity_id:
                outgoing.append(rel_data)
            else:
                incoming.append(rel_data)

        return {
            "entity": dict(entity.items()),
            "outgoing": outgoing,
            "incoming": incoming,
        }

    def find_shortest_path(
        self, start_id: str, end_id: str, max_hops: int = 5
    ) -> Dict[str, Any]:
        """Find Shortest Path between two nodes."""
        query = f"""
        MATCH (start {{id: $start_id}}), (end {{id: $end_id}})
        MATCH p = shortestPath((start)-[*..{max_hops}]-(end))
        RETURN p, length(p) as len
        """

        result = self.gm.execute_query(query, {"start_id": start_id, "end_id": end_id})

        if not result:
            return {"found": False, "path": []}

        path = result[0]["p"]
        length = result[0]["len"]

        # Path object in Neo4j python driver is complex to serialize directly
        # It contains Nodes and Relationships.
        # We need to serialize it.
        nodes = [dict(n.items()) for n in path.nodes]
        rels = [
            {
                "type": r.type,
                "start": r.start_node["name"],  # simplify for display
                "end": r.end_node["name"],
                "properties": dict(r.items()),
            }
            for r in path.relationships
        ]

        return {"found": True, "length": length, "nodes": nodes, "relationships": rels}

    def search_entities(self, name_query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Fuzzy search for entities by name."""
        query = """
        MATCH (n)
        WHERE toLower(n.name) CONTAINS toLower($q)
        RETURN n
        LIMIT $limit
        """
        result = self.gm.execute_query(query, {"q": name_query, "limit": limit})
        return [dict(r["n"].items()) for r in result]

    def reason_about_entity(self, entity_id: str, hops: int = 2) -> Dict[str, Any]:
        """
        Explore implications around an entity.
        Finds nodes connected up to `hops` distance,
        prioritizing causal relations (LEADS_TO, CAUSES, etc).
        """
        # We can filter mainly for implication-heavy relations
        implication_rels = [
            RelationType.CAUSES.value,
            RelationType.LEADS_TO.value,
            RelationType.MANIFESTS_AS.value,
            RelationType.IS_A.value,
        ]
        rel_types_str = "|".join(implication_rels)

        query = f"""
        MATCH (start {{id: $id}})
        MATCH (start)-[r:{rel_types_str}*1..{hops}]->(target)
        RETURN distinct target, r
        LIMIT 20
        """
        # Note: variable length relationship return is a list of relationships in path
        # But here 'r' refers to the path collection? No, syntax is [r...].
        # Let's adjust query to be simpler: just get paths.

        query = f"""
        MATCH p = (start {{id: $id}})-[:{rel_types_str}*1..{hops}]->(target)
        RETURN p
        LIMIT 20
        """

        results = self.gm.execute_query(query, {"id": entity_id})

        paths = []
        for rec in results:
            p = rec["p"]
            # Serialize
            path_str = " -> ".join([f"({n['name']})" for n in p.nodes])
            paths.append(path_str)

        return {"entity_id": entity_id, "implications": paths}

    def get_hierarchy(self, concept_id: str) -> Dict[str, Any]:
        """
        Resolve IS_A / PART_OF hierarchy.
        Find parents (generalization) and children (specialization).
        """
        # Parents: node -> IS_A -> parent
        q_parents = """
        MATCH (n {id: $id})-[:IS_A|PART_OF]->(parent)
        RETURN parent
        """
        # Children: child -> IS_A -> node
        q_children = """
        MATCH (child)-[:IS_A|PART_OF]->(n {id: $id})
        RETURN child
        """

        parents = [
            dict(r["parent"].items())
            for r in self.gm.execute_query(q_parents, {"id": concept_id})
        ]
        children = [
            dict(r["child"].items())
            for r in self.gm.execute_query(q_children, {"id": concept_id})
        ]

        return {"concept_id": concept_id, "parents": parents, "children": children}
