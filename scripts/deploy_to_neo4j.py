import json
import os
import sys
import logging

# Add src to python path to reuse GraphManager
# Add src to python path to reuse GraphManager
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.graph.graph_manager import GraphManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

INPUT_FILE = "ontology_project/merged_output/raw_entities.json"

def deploy_to_neo4j():
    if not os.path.exists(INPUT_FILE):
        logger.error(f"Input file {INPUT_FILE} not found. Run aggregation first.")
        return

    try:
        gm = GraphManager()
    except Exception as e:
        logger.error(f"Failed to connect to Neo4j: {e}")
        return

    with open(INPUT_FILE, 'r') as f:
        data = json.load(f)

    nodes = data.get("nodes", [])
    relationships = data.get("relationships", [])

    logger.info(f"Deploying {len(nodes)} nodes and {len(relationships)} relationships...")

    # 1. Create Nodes
    # We use MERGE to avoid duplicates.
    # Note: efficient batching would be better for massive datasets, 
    # but for 150-query ontology, row-by-row or small batches is fine.
    
    for i, node in enumerate(nodes):
        node_id = node.get("id")
        label = node.get("type", "Entity")
        name = node.get("name", node_id)
        props = node.get("attributes", {})
        
        # Construct content for properties
        # We'll flatten attributes into the node properties for simplicity in Neo4j
        
        # Cypher query
        query = f"""
        MERGE (n:`{label}` {{id: $id}})
        SET n.name = $name
        """
        
        # Add attributes dynamically
        # Note: In a real prod script, we'd handle types more carefully
        params = {"id": node_id, "name": name}
        
        for k, v in props.items():
            if isinstance(v, list):
                # Neo4j supports lists of basic types
                params[k] = v
                query += f", n.`{k}` = ${k}"
            else:
                params[k] = v
                query += f", n.`{k}` = ${k}"

        try:
            gm.execute_query(query, params)
        except Exception as e:
            logger.error(f"Failed to create node {node_id}: {e}")
            
        if i % 50 == 0:
            logger.info(f"Processed {i} nodes...")

    # 2. Create Relationships
    for i, rel in enumerate(relationships):
        source = rel.get("source")
        target = rel.get("target")
        rel_type = rel.get("type", "RELATED_TO")
        
        query = f"""
        MATCH (a {{id: $source}}), (b {{id: $target}})
        MERGE (a)-[r:`{rel_type}`]->(b)
        """
        
        params = {"source": source, "target": target}
        
        # Add relationship properties if any
        if "properties" in rel:
            for k, v in rel["properties"].items():
                 params[k] = v
                 query += f" SET r.`{k}` = ${k}"

        try:
            gm.execute_query(query, params)
        except Exception as e:
            logger.error(f"Failed to create relationship {source} -> {target}: {e}")

        if i % 50 == 0:
            logger.info(f"Processed {i} relationships...")

    logger.info("Deployment complete.")
    gm.close()

if __name__ == "__main__":
    deploy_to_neo4j()
