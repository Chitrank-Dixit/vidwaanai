#!/usr/bin/env python3
import os
import re
import json
import logging
import glob

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("extract_vedas_ontology")

# Constants
QUERIES_DIR = "ontology_project/queries/Vedas"
RESPONSES_DIR = "scripts/responses/gemini"

ONTOLOGY_HEADER = {
    "entity_types": ["Deity", "Concept", "Character", "Place", "Event", "Text"],
    "relationship_types": [
        "MENTIONS",
        "IS_AVATAR_OF",
        "RELATED_TO",
        "LOCATED_AT",
        "PARTICIPATED_IN",
    ],
}

# Vedic entities dictionary (Pantheon, Concepts, Texts)
ENTITIES_DICT = {
    "Agni": {
        "type": "Deity",
        "keywords": [r"agni", r"अग्नि"],
        "description": "The Vedic fire deity, messenger of the gods, and chief priest of the yajna.",
    },
    "Indra": {
        "type": "Deity",
        "keywords": [r"indra", r"इन्द्र"],
        "description": "The king of the Vedic gods, deity of thunder, rain, and war, slayer of Vritra.",
    },
    "Soma": {
        "type": "Deity",
        "keywords": [r"soma", r"सोम"],
        "description": "The deified sacred plant and drink of immortality offered in Vedic rituals.",
    },
    "Varuna": {
        "type": "Deity",
        "keywords": [r"varuna", r"varuṇa", r"वरुण"],
        "description": "The guardian of cosmic order (Rta), deity of the sky, oceans, and moral law.",
    },
    "Mitra": {
        "type": "Deity",
        "keywords": [r"mitra", r"मित्र"],
        "description": "Vedic solar deity of friendship, contracts, and alliances, closely associated with Varuna.",
    },
    "Rudra": {
        "type": "Deity",
        "keywords": [r"rudra", r"रुद्र"],
        "description": "The fierce storm and wind deity, early form of Lord Shiva.",
    },
    "Vishnu": {
        "type": "Deity",
        "keywords": [r"vishnu", r"viṣṇu", r"विष्णु"],
        "description": "Vedic deity known for taking three giant strides (Trivikrama) to span the universe.",
    },
    "Savitr": {
        "type": "Deity",
        "keywords": [r"savitr", r"savitṛ", r"सविता", r"सविट"],
        "description": "Vedic solar deity representing the morning sun, associated with the Gayatri mantra.",
    },
    "Ushas": {
        "type": "Deity",
        "keywords": [r"ushas", r"uṣas", r"उषा"],
        "description": "The goddess of dawn, bringing light and life to the world.",
    },
    "Maruts": {
        "type": "Deity",
        "keywords": [r"marut", r"मरुत्"],
        "description": "The storm deities, companions of Indra and sons of Rudra.",
    },
    "Ashvins": {
        "type": "Deity",
        "keywords": [r"ashvin", r"aśvin", r"अश्विन"],
        "description": "The twin horsemen, divine physicians who rescue and heal.",
    },
    "Prithvi": {
        "type": "Deity",
        "keywords": [r"prithvi", r"pṛthivī", r"पृथ्वी"],
        "description": "The earth goddess, consort of Dyaus Pita.",
    },
    "Dyaus": {
        "type": "Deity",
        "keywords": [r"dyaus", r"द्यौ"],
        "description": "The sky father deity, oldest deity of the Vedic pantheon.",
    },
    "Rta": {
        "type": "Concept",
        "keywords": [r"rta", r"ṛta", r"ऋत", r"cosmic order"],
        "description": "The physical and moral order of the universe that gods and humans must follow.",
    },
    "Yajna": {
        "type": "Concept",
        "keywords": [r"yajna", r"yajña", r"yagya", r"यज्ञ", r"sacrifice"],
        "description": "The central Vedic ritual of fire offering accompanied by mantras.",
    },
    "Purusha": {
        "type": "Concept",
        "keywords": [r"purusha", r"puruṣa", r"पुरुष"],
        "description": "The cosmic giant or primeval being from whose sacrifice the universe was created.",
    },
    "Rigveda": {
        "type": "Text",
        "keywords": [r"rigveda", r"ṛgveda", r"ऋग्वेद"],
        "description": "The oldest of the four Vedas, containing hymns to the deities.",
    },
    "Yajurveda": {
        "type": "Text",
        "keywords": [r"yajurveda", r"यजुर्वेद"],
        "description": "The Veda of prose mantras and ritual formulas.",
    },
    "Samaveda": {
        "type": "Text",
        "keywords": [r"samaveda", r"सामवेद"],
        "description": "The Veda of melodies and chants chanted by Udgatri priests.",
    },
    "Atharvaveda": {
        "type": "Text",
        "keywords": [r"atharvaveda", r"अथर्ववेद"],
        "description": "The Veda of spells, charms, and everyday procedures.",
    },
}


def extract_entities_from_text(text: str) -> list:
    matched = []
    text_lower = text.lower()
    for entity_name, info in ENTITIES_DICT.items():
        for kw in info["keywords"]:
            if re.search(kw, text_lower):
                matched.append(
                    {
                        "name": entity_name,
                        "type": info["type"],
                        "attributes": {"description": info["description"]},
                    }
                )
                break
    return matched


def extract_relationships_from_entities(entities_present: set) -> list:
    rels = []

    # Agni & Yajna
    if "Agni" in entities_present and "Yajna" in entities_present:
        rels.append(
            {
                "from": "Agni",
                "to": "Yajna",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "Agni is the fire medium and priest through whom offerings are made in Yajna."
                },
            }
        )

    # Soma & Yajna
    if "Soma" in entities_present and "Yajna" in entities_present:
        rels.append(
            {
                "from": "Soma",
                "to": "Yajna",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "Soma juice libation is a key offering in Vedic Yajna."
                },
            }
        )

    # Indra & Soma
    if "Indra" in entities_present and "Soma" in entities_present:
        rels.append(
            {
                "from": "Indra",
                "to": "Soma",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "Indra consumes Soma juice to gain divine strength for battles."
                },
            }
        )

    # Mitra & Varuna
    if "Mitra" in entities_present and "Varuna" in entities_present:
        rels.append(
            {
                "from": "Mitra",
                "to": "Varuna",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "Mitra and Varuna are dual deities (Mitra-Varuna) who uphold moral law."
                },
            }
        )

    # Purusha & Yajna
    if "Purusha" in entities_present and "Yajna" in entities_present:
        rels.append(
            {
                "from": "Purusha",
                "to": "Yajna",
                "type": "PARTICIPATED_IN",
                "attributes": {
                    "context": "The primeval Purusha is sacrificed in the cosmic Yajna to create manifestation."
                },
            }
        )

    # Deities and Rta
    deities = ["Agni", "Indra", "Varuna", "Mitra", "Soma"]
    for d in deities:
        if d in entities_present and "Rta" in entities_present:
            rels.append(
                {
                    "from": d,
                    "to": "Rta",
                    "type": "RELATED_TO",
                    "attributes": {
                        "context": f"Lord {d} is a guardian and upholder of the cosmic order Rta."
                    },
                }
            )

    return rels


def parse_batch_file(filepath: str) -> str:
    if not os.path.exists(filepath):
        return ""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def process_veda_directory(veda_dir: str, veda_name: str):
    """Process all batches in a specific Veda directory."""
    files = sorted(glob.glob(os.path.join(veda_dir, "*.md")))
    if not files:
        logger.warning(f"No md files found in {veda_dir}")
        return

    logger.info(f"Processing Veda '{veda_name}' ({len(files)} batch files)...")

    group_size = 10

    for idx in range(0, len(files), group_size):
        group_files = files[idx : idx + group_size]
        start_batch = idx + 1
        end_batch = idx + len(group_files)

        batch_entities = []
        seen_entities = set()
        seen_entity_names = set()

        for filepath in group_files:
            content = parse_batch_file(filepath)
            matches = extract_entities_from_text(content)

            for m in matches:
                seen_entities.add(m["name"])
                if m["name"] not in seen_entity_names:
                    batch_entities.append(m)
                    seen_entity_names.add(m["name"])

        rels = extract_relationships_from_entities(seen_entities)

        group_data = {
            "ontology": ONTOLOGY_HEADER,
            "entities": batch_entities,
            "relationships": rels,
        }

        output_filename = f"{veda_name}_batch_{start_batch}_{end_batch}.json"
        output_filepath = os.path.join(RESPONSES_DIR, output_filename)

        with open(output_filepath, "w", encoding="utf-8") as f:
            json.dump(group_data, f, indent=4, ensure_ascii=False)


def main():
    os.makedirs(RESPONSES_DIR, exist_ok=True)

    # Get all subdirectories in queries/Vedas/
    subdirs = sorted(
        [d for d in glob.glob(os.path.join(QUERIES_DIR, "*")) if os.path.isdir(d)]
    )

    for subdir in subdirs:
        veda_name = os.path.basename(subdir)
        process_veda_directory(subdir, veda_name)

    logger.info("Successfully extracted ontology responses for all Vedas!")


if __name__ == "__main__":
    main()
