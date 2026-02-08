import json

INPUT_FILE = "ontology_project/merged_output/raw_entities.json"

def check_structure(data):
    issues = []
    nodes = {n["id"]: n for n in data.get("nodes", [])}
    
    # 1. Avatar Consistency
    # Rule: If type is 'Avatar', it should ideally be linked to a 'Deity' via 'IS_AVATAR_OF'
    avatars = [n for n in data.get("nodes", []) if n.get("type") == "Avatar"]
    for av in avatars:
        av_id = av["id"]
        # Check if there is a relationship
        has_link = False
        for rel in data.get("relationships", []):
            if rel["source"] == av_id and rel["type"] == "IS_AVATAR_OF":
                target_id = rel["target"]
                target_node = nodes.get(target_id)
                if target_node and target_node.get("type") == "Deity":
                    has_link = True
                elif target_node:
                    issues.append(f"Logic Warning: Avatar '{av_id}' is avatar of '{target_id}' which is type '{target_node.get('type')}', expected 'Deity'.")
                else:
                    issues.append(f"Broken Link: Avatar '{av_id}' links to missing node '{target_id}'.")
        
        if not has_link:
            issues.append(f"Logic Warning: Avatar '{av_id}' has no 'IS_AVATAR_OF' relationship to a Deity.")

    # 2. Symmetric Relationships
    # Rule: 'CONSORT_OF' should be symmetric
    for rel in data.get("relationships", []):
        if rel["type"] == "CONSORT_OF":
            source = rel["source"]
            target = rel["target"]
            # Look for reverse
            reverse_found = False
            for r2 in data.get("relationships", []):
                if r2["source"] == target and r2["target"] == source and r2["type"] == "CONSORT_OF":
                    reverse_found = True
                    break
            if not reverse_found:
                issues.append(f"Symmetry Warning: '{source}' is CONSORT_OF '{target}', but reverse is missing.")

    return issues

def main():
    try:
        with open(INPUT_FILE, "r") as f:
            data = json.load(f)
            
        print("Running Consistency Checks...")
        issues = check_structure(data)
        
        if issues:
            print(f"Found {len(issues)} consistency issues:")
            for i, issue in enumerate(issues, 1):
                print(f"{i}. {issue}")
        else:
            print("No logical consistency issues found (based on current rules).")
            
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")

if __name__ == "__main__":
    main()
