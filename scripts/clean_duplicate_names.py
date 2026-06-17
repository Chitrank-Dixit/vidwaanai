#!/usr/bin/env python3
import glob
import json
import logging
import os

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("clean_duplicate_names")

RESPONSE_DIRS = [
    "scripts/responses/perplexity",
    "scripts/responses/gemini",
    "scripts/responses/chatgpt",
]

# Case-insensitive normalization mapping (lowercase variation -> canonical name)
NORMALIZATION_MAP = {
    # Ramayana Characters
    "ram": "Rama",
    "rama": "Rama",
    "ráma": "Rama",
    "râma": "Rama",
    "ramacandra": "Rama",
    "ramachandra": "Rama",
    "sita": "Sita",
    "sītā": "Sita",
    "seetha": "Sita",
    "janaki": "Sita",
    "lakshman": "Lakshmana",
    "lakshmana": "Lakshmana",
    "lakṣmaṇa": "Lakshmana",
    "lakshmag": "Lakshmana",
    "ravan": "Ravana",
    "ravana": "Ravana",
    "rāvaṇa": "Ravana",
    "rávag": "Ravana",
    "hanuman": "Hanuman",
    "hanumān": "Hanuman",
    "anthaneya": "Hanuman",
    "dasharatha": "Dasharatha",
    "dasaratha": "Dasharatha",
    "daśaratha": "Dasharatha",
    "vashishtha": "Vashishtha",
    "vasishtha": "Vashishtha",
    "vaśiṣṭha": "Vashishtha",
    "va[ishmha": "Vashishtha",
    "vishvamitra": "Vishvamitra",
    "visvamitra": "Vishvamitra",
    "viśvāmitra": "Vishvamitra",
    # Mahabharata & Gita Characters / Deities
    "krishna": "Krishna",
    "krsna": "Krishna",
    "kṛṣṇa": "Krishna",
    "yudhishthira": "Yudhishthira",
    "yudhisthira": "Yudhishthira",
    "yudhiṣṭhira": "Yudhishthira",
    "bhima": "Bhima",
    "bhīma": "Bhima",
    "nakula": "Nakula",
    "sahadeva": "Sahadeva",
    "draupadi": "Draupadi",
    "draupadī": "Draupadi",
    "karna": "Karna",
    "karṇa": "Karna",
    "duryodhana": "Duryodhana",
    "dhritarashtra": "Dhritarashtra",
    "dhṛtarāṣṭra": "Dhritarashtra",
    "gandhari": "Gandhari",
    "gāndhārī": "Gandhari",
    "kunti": "Kunti",
    "kuntī": "Kunti",
    "vidura": "Vidura",
    "bhishma": "Bhishma",
    "bhīṣma": "Bhishma",
    "drona": "Drona",
    "droṇa": "Drona",
    "shakuni": "Shakuni",
    "satyavati": "Satyavati",
    "vyasa": "Vyasa",
    "vyāsa": "Vyasa",
    "vedavyasa": "Vyasa",
    "pandu": "Pandu",
    "pāṇḍu": "Pandu",
    # Places
    "hastinapura": "Hastinapura",
    "hastināpura": "Hastinapura",
    "indraprastha": "Indraprastha",
    "kurukshetra": "Kurukshetra",
    "ayodhya": "Ayodhya",
    "ayodhyā": "Ayodhya",
    # Concepts
    "dharma": "Dharma",
    "karma": "Karma",
    "atman": "Atman",
    "brahman": "Brahman",
    "moksha": "Moksha",
    "samsara": "Samsara",
    "yajna": "Yajna",
    "rta": "Rta",
}


def clean_name(name: str) -> str:
    """Standardize name based on normalization map."""
    if not name:
        return ""
    name_stripped = name.strip()
    name_lower = name_stripped.lower()

    # Check direct match
    if name_lower in NORMALIZATION_MAP:
        return NORMALIZATION_MAP[name_lower]

    # Check substring or partial match for common accented forms
    # e.g., 'Rāma' or 'Ráma' with extra spaces
    cleaned = (
        name_lower.replace("á", "a")
        .replace("ā", "a")
        .replace("ś", "sh")
        .replace("ṣ", "sh")
    )
    if cleaned in NORMALIZATION_MAP:
        return NORMALIZATION_MAP[cleaned]

    return name_stripped


def clean_file(filepath: str) -> bool:
    """Read a JSON file, normalize names and keys, and write back."""
    try:
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)

        modified = False

        # 1. Normalize Nodes/Entities
        nodes_key = (
            "nodes" if "nodes" in data else ("entities" if "entities" in data else None)
        )
        if nodes_key:
            for node in data[nodes_key]:
                if "name" in node:
                    old_name = node["name"]
                    new_name = clean_name(old_name)
                    if old_name != new_name:
                        node["name"] = new_name
                        modified = True

                # Standardize ID if present
                if "id" in node:
                    old_id = node["id"]
                    # Clean the ID by replacing spaces with underscores in standardized name
                    new_id = node.get("name", old_id).replace(" ", "_")
                    if old_id != new_id:
                        node["id"] = new_id
                        modified = True

        # 2. Normalize Relationships
        if "relationships" in data:
            for rel in data["relationships"]:
                for key in ["from", "to", "source", "target"]:
                    if key in rel:
                        old_val = rel[key]
                        new_val = clean_name(old_val)
                        if old_val != new_val:
                            rel[key] = new_val
                            modified = True

        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True

    except Exception as e:
        logger.error(f"Failed to clean file {filepath}: {e}")

    return False


def main():
    cleaned_count = 0
    total_files = 0

    for r_dir in RESPONSE_DIRS:
        files = glob.glob(os.path.join(r_dir, "*.json"))
        total_files += len(files)
        logger.info(f"Scanning {len(files)} files in {r_dir}...")

        for filepath in files:
            if clean_file(filepath):
                cleaned_count += 1

    logger.info(
        f"Scan complete. Standardized duplicate spellings in {cleaned_count} out of {total_files} JSON files."
    )


if __name__ == "__main__":
    main()
