import os
import sys
import argparse
import json

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.core.config import settings
from src.db.db_manager import DatabaseManager

OUTPUT_FILE = "ontology_project/queries/batch_from_db.md"

PROMPT_TEMPLATE = """# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

"""

def generate_prompts(limit=20, offset=0, scripture_filter=None):
    print(f"Connecting to database: {settings.DATABASE_URL}")
    db = DatabaseManager(settings.DATABASE_URL)
    
    print("Fetching verses...")
    verses = db.get_all_verses()
    
    # Filter by scripture if provided
    if scripture_filter:
        print(f"Filtering for scripture: {scripture_filter}")
        target_verses = [v for v in verses if scripture_filter.lower() in v.get("scripture_name", "").lower()]
        
        if not target_verses:
            print(f"No verses found for scripture: {scripture_filter}")
            return

        # Prepare directory
        clean_name = scripture_filter.replace(" ", "_")
        scripture_dir = os.path.join(os.path.dirname(OUTPUT_FILE), clean_name)
        os.makedirs(scripture_dir, exist_ok=True)
        
        # Batch processing
        total_verses = len(target_verses)
        num_batches = (total_verses + limit - 1) // limit
        print(f"Found {total_verses} verses. Generating {num_batches} batches of size {limit}.")
        
        for i in range(num_batches):
            batch_start = i * limit
            batch_end = batch_start + limit
            batch = target_verses[batch_start:batch_end]
            
            filename = os.path.join(scripture_dir, f"{clean_name}_batch_{i+1}.md")
            write_batch_file(filename, batch)
            
    else:
        # Default single batch behavior
        batch = verses[offset : offset + limit]
        print(f"Fetched {len(batch)} verses (Offset: {offset}, Limit: {limit})")
        
        if not batch:
            print("No verses found.")
            return

        write_batch_file(OUTPUT_FILE, batch)

def write_batch_file(filename, batch):
    with open(filename, "w") as f:
        f.write(PROMPT_TEMPLATE)
        
        for i, verse in enumerate(batch):
            text = verse.get("text", "").replace("\n", " ").strip()
            trans = verse.get("translation", "").replace("\n", " ").strip()
            scripture = verse.get("scripture_name", "Unknown")
            chapter = verse.get("chapter_number", "?")
            v_num = verse.get("verse_number", "?")
            
            f.write(f"### Verse {i+1} ({scripture} {chapter}.{v_num})\n")
            f.write(f"- **Original**: {text}\n")
            f.write(f"- **Translation**: {trans}\n\n")
            f.write("---\n\n")
            
    print(f"Generated prompt file: {filename}")

def main():
    parser = argparse.ArgumentParser(description="Generate LLM prompts from DB verses")
    parser.add_argument("--limit", type=int, default=20, help="Number of verses to fetch")
    parser.add_argument("--offset", type=int, default=0, help="Offset for fetching")
    parser.add_argument("--scripture", type=str, help="Filter by scripture name (e.g. 'Ramayan')")
    args = parser.parse_args()
    
    generate_prompts(args.limit, args.offset, args.scripture)

if __name__ == "__main__":
    main()
