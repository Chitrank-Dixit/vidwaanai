import json
import glob
import os
from typing import List, Dict, Any

# Configuration
RESPONSE_DIRS = [
    "scripts/responses/perplexity",
    "scripts/responses/gemini",
    "scripts/responses/chatgpt"
]
OUTPUT_FILE = "ontology_project/merged_output/raw_entities.json"

def load_json_files(directories: List[str]) -> List[Dict[str, Any]]:
    all_data = []
    for directory in directories:
        files = glob.glob(os.path.join(directory, "*.json"))
        print(f"Found {len(files)} files in {directory}")
        for filepath in files:
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    # Validate basic structure
                    if "nodes" in data or "relationships" in data or "entities" in data:
                        all_data.append(data)
                    else:
                        print(f"Warning: Skipping {filepath} - Missing 'nodes' or 'relationships' keys.")
            except json.JSONDecodeError as e:
                print(f"Error: Failed to decode {filepath}: {e}")
            except Exception as e:
                print(f"Error: Failed to process {filepath}: {e}")
    return all_data

def merge_data(data_list: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    merged = {
        "nodes": [],
        "relationships": []
    }
    
    seen_nodes = set()
    
    for entry in data_list:
        # Normalize Nodes (entities -> nodes)
        nodes_source = entry.get("nodes", []) + entry.get("entities", [])
        
        for node in nodes_source:
            # Ensure name exists
            if "name" not in node:
                continue
                
            # Create ID if missing
            if "id" not in node:
                node["id"] = node["name"].replace(" ", "_")

            node_id = node.get("id")
            
            if node_id and node_id not in seen_nodes:
                merged["nodes"].append(node)
                seen_nodes.add(node_id)
            elif node_id:
                # Duplicate handling: skip for now
                pass
        
        # Merge Relationships
        for rel in entry.get("relationships", []):
            # Normalize keys (from -> source, to -> target)
            if "from" in rel:
                rel["source"] = rel.pop("from")
            if "to" in rel:
                rel["target"] = rel.pop("to")
                
            merged["relationships"].append(rel)
            
    return merged

def main():
    print("Starting aggregation...")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    raw_data = load_json_files(RESPONSE_DIRS)
    merged_data = merge_data(raw_data)
    
    node_count = len(merged_data["nodes"])
    rel_count = len(merged_data["relationships"])
    
    print(f"Aggregation complete.")
    print(f"Total Nodes: {node_count}")
    print(f"Total Relationships: {rel_count}")
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(merged_data, f, indent=2, ensure_ascii=False)
        
    print(f"Saved merged output to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
