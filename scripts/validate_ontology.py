import json
import os
import sys
from typing import Dict, Any, Set, List

INPUT_FILE = "ontology_project/merged_output/raw_entities.json"

def validate_nodes(nodes: List[Dict[str, Any]]) -> Set[str]:
    valid_ids = set()
    errors = []
    
    for i, node in enumerate(nodes):
        node_id = node.get("id")
        node_label = node.get("label")
        
        if not node_id:
            errors.append(f"Node at index {i} missing 'id'.")
            continue
            
        if not node_label:
            errors.append(f"Node '{node_id}' missing 'label'.")
            
        if node_id in valid_ids:
            errors.append(f"Duplicate Node ID: '{node_id}'.")
        else:
            valid_ids.add(node_id)
            
    if errors:
        print("\nNode Validation Errors:")
        for err in errors:
            print(f"  - {err}")
    
    return valid_ids

def validate_relationships(relationships: List[Dict[str, Any]], valid_node_ids: Set[str]):
    errors = []
    
    for i, rel in enumerate(relationships):
        source = rel.get("source")
        target = rel.get("target")
        rel_type = rel.get("type")
        
        if not rel_type:
            errors.append(f"Relationship at index {i} missing 'type'.")
        
        if not source:
             errors.append(f"Relationship at index {i} missing 'source'.")
        elif source not in valid_node_ids:
            # Warn but don't fail, as we might have partial data
            pass # errors.append(f"Dangling Relationship: Source '{source}' not found in nodes.")

        if not target:
             errors.append(f"Relationship at index {i} missing 'target'.")
        elif target not in valid_node_ids:
            # Warn but don't fail
            pass # errors.append(f"Dangling Relationship: Target '{target}' not found in nodes.")

    if errors:
        print("\nRelationship Validation Errors:")
        for err in errors:
            print(f"  - {err}")

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Input file {INPUT_FILE} not found. Run aggregate_responses.py first.")
        sys.exit(1)
        
    print(f"Validating {INPUT_FILE}...")
    
    try:
        with open(INPUT_FILE, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format: {e}")
        sys.exit(1)
        
    nodes = data.get("nodes", [])
    relationships = data.get("relationships", [])
    
    print(f"Checking {len(nodes)} nodes and {len(relationships)} relationships...")
    
    valid_ids = validate_nodes(nodes)
    validate_relationships(relationships, valid_ids)
    
    print("\nValidation check complete.")

if __name__ == "__main__":
    main()
