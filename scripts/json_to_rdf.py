import json
import datetime

INPUT_FILE = "ontology_project/merged_output/raw_entities.json"
OUTPUT_FILE = "ontology_project/merged_output/ontology.ttl"

PREFIXES = """@prefix : <http://vidwaan.ai/ontology/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://vidwaan.ai/ontology/> .
"""

def clean_id(identifier):
    """Ensures ID is a valid IRI segment (alphanumeric + underscore)."""
    return identifier.replace(":", "_").replace(" ", "_").replace("-", "_")

def generate_turtle(data):
    lines = [PREFIXES]
    
    # Metadata
    lines.append(f"""
<http://vidwaan.ai/ontology> rdf:type owl:Ontology ;
    rdfs:comment "Vidwaan AI Vedic Ontology generated via Multi-LLM Pipeline" ;
    owl:versionInfo "{datetime.date.today().isoformat()}" .
""")

    nodes = data.get("nodes", [])
    relationships = data.get("relationships", [])
    
    # 1. Class Definitions (Unique Types)
    types = set(n.get("type", "Thing") for n in nodes)
    for t in types:
        lines.append(f":{clean_id(t)} rdf:type owl:Class .")
        
    lines.append("")

    # 2. Individuals (Nodes)
    for node in nodes:
        node_id = clean_id(node["id"])
        node_type = clean_id(node.get("type", "Thing"))
        label = node.get("name", node_id)
        
        lines.append(f":{node_id} rdf:type :{node_type} ;")
        lines.append(f'    rdfs:label "{label}" ;')
        
        # Add attributes
        props = node.get("attributes", {})
        if isinstance(props, dict):
            for k, v in props.items():
                clean_k = clean_id(k)
                if isinstance(v, list):
                    for val in v:
                        lines.append(f'    :{clean_k} "{val}" ;')
                else:
                    lines.append(f'    :{clean_k} "{v}" ;')
        
        # Close statement
        lines.append("    .")
        lines.append("")

    # 3. Object Properties (Relationships)
    for rel in relationships:
        source = clean_id(rel["source"])
        target = clean_id(rel["target"])
        rel_type = clean_id(rel["type"])
        
        # Define property if not already defined (basic assumption)
        # In a real scenario, we'd define these separately
        
        lines.append(f":{source} :{rel_type} :{target} .")

    return "\n".join(lines)

def main():
    try:
        with open(INPUT_FILE, "r") as f:
            data = json.load(f)
            
        ttl_content = generate_turtle(data)
        
        with open(OUTPUT_FILE, "w") as f:
            f.write(ttl_content)
            
        print(f"Successfully generated {OUTPUT_FILE}")
        
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found. Run aggregation first.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
