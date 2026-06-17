#!/usr/bin/env python3
import logging
import os
import sys

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.core.config import settings
from src.db.db_manager import DatabaseManager

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("generate_all_scripture_queries")

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


def get_target_directory(scripture_name: str) -> str:
    """Determine target directory under ontology_project/queries/ based on scripture name."""
    name_lower = scripture_name.lower()

    # 1. Gita
    if name_lower in ["bhagwat_geeta", "bhagavad gita"]:
        return "ontology_project/queries/Bhagwat_Geeta"

    # 2. Mahabharat
    if name_lower == "mahabharat":
        return "ontology_project/queries/Mahabharat"

    # 3. Vedas
    if name_lower == "rig ved":
        return "ontology_project/queries/Vedas/Rig_Ved"
    if name_lower == "yajur ved":
        return "ontology_project/queries/Vedas/Yajur_Ved"
    if name_lower == "sama ved":
        return "ontology_project/queries/Vedas/Sama_Ved"
    if name_lower == "atharva ved":
        return "ontology_project/queries/Vedas/Atharva_Ved"

    # 4. Puranas (all other database entries)
    # Standardize spaces/dashes to underscores
    clean_name = scripture_name.replace(" ", "_").replace("-", "_")
    return f"ontology_project/queries/Puranas/{clean_name}"


def write_batch_file(filepath: str, batch: list):
    """Write prompt batch to markdown file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(PROMPT_TEMPLATE)
        for i, verse in enumerate(batch):
            text = (verse.get("text") or "").replace("\n", " ").strip()
            trans = (verse.get("translation") or "").replace("\n", " ").strip()
            scripture = verse.get("scripture_name", "Unknown")
            chapter = verse.get("chapter_number", "?")
            v_num = verse.get("verse_number", "?")

            f.write(f"### Verse {i + 1} ({scripture} {chapter}.{v_num})\n")
            f.write(f"- **Original**: {text}\n")
            f.write(f"- **Translation**: {trans}\n\n")
            f.write("---\n\n")


def main():
    logger.info(f"Connecting to database: {settings.DATABASE_URL}")
    db = DatabaseManager(settings.DATABASE_URL)

    logger.info("Fetching all verses from database...")
    all_verses = db.get_all_verses()
    logger.info(f"Total verses fetched: {len(all_verses)}")

    # Group verses by target scripture name
    scriptures_data = {}
    ignored_count = 0

    for verse in all_verses:
        name = verse.get("scripture_name")
        if not name:
            continue

        name_lower = name.lower()

        # Filter out Ramayan and Ramayana
        if "ramayan" in name_lower:
            ignored_count += 1
            continue

        # Ignore Bhagavad Gita to avoid duplicate processing with Bhagwat_Geeta
        if name_lower == "bhagavad gita":
            ignored_count += 1
            continue

        if name not in scriptures_data:
            scriptures_data[name] = []
        scriptures_data[name].append(verse)

    logger.info(
        f"Filtered out {ignored_count} verses (Ramayana / Bhagavad Gita duplicates)"
    )

    # Process each scripture and generate batches of size 20
    batch_size = 20

    for scripture_name, verses in scriptures_data.items():
        total_verses = len(verses)
        target_dir = get_target_directory(scripture_name)
        clean_name = scripture_name.replace(" ", "_").replace("-", "_")

        num_batches = (total_verses + batch_size - 1) // batch_size
        logger.info(
            f"Processing '{scripture_name}': {total_verses} verses -> {num_batches} batches under {target_dir}"
        )

        for i in range(num_batches):
            batch_start = i * batch_size
            batch_end = batch_start + batch_size
            batch = verses[batch_start:batch_end]

            filename = f"{clean_name}_batch_{i + 1}.md"
            filepath = os.path.join(target_dir, filename)
            write_batch_file(filepath, batch)

    logger.info("Successfully generated all scripture batch query files!")


if __name__ == "__main__":
    main()
