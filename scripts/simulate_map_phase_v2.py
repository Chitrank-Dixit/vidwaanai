import os
import json

def generate_mock_data(batch_id, agent):
    # Create valid JSON content for the merged batch
    # We simulate extraction from ~16 files by adding slightly more entities
    return {
        "entities": [
            {
                "name": f"Entity_Batch_{batch_id}_Main",
                "type": "Concept",
                "attributes": {"description": f"Main entity from Merged Batch {batch_id} processed by {agent}"}
            },
            {
                "name": f"Entity_Batch_{batch_id}_Secondary",
                "type": "Character",
                "attributes": {"description": f"Secondary entity from Merged Batch {batch_id}"}
            }
        ],
        "relationships": [
            {
                "source": f"Entity_Batch_{batch_id}_Main",
                "target": f"Entity_Batch_{batch_id}_Secondary",
                "type": "RELATED_TO",
                "attributes": {"context": "Mock relationship from merged batch"}
            }
        ]
    }

def main():
    base_path = "scripts/responses"
    
    # Define batches: (Batch ID, Agent)
    # 1-4 Gemini, 5-8 ChatGPT, 9-12 Perplexity
    batches = [
        (1, "gemini"), (2, "gemini"), (3, "gemini"), (4, "gemini"),
        (5, "chatgpt"), (6, "chatgpt"), (7, "chatgpt"), (8, "chatgpt"),
        (9, "perplexity"), (10, "perplexity"), (11, "perplexity"), (12, "perplexity")
    ]
    
    print("Starting Map Phase Simulation (v2 - Merged Batches)...")
    
    for batch_id, agent in batches:
        dir_path = os.path.join(base_path, agent)
        os.makedirs(dir_path, exist_ok=True)
        
        file_path = os.path.join(dir_path, f"batch_{batch_id}.json")
        
        data = generate_mock_data(batch_id, agent)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
            
        print(f"Created {file_path}")

if __name__ == "__main__":
    main()
