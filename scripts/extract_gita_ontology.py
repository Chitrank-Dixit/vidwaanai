#!/usr/bin/env python3
import json
import logging
import os
import re

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("extract_gita_ontology")

# Constants
QUERIES_DIR = "ontology_project/queries/Bhagwat_Geeta"
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

# Entity dictionary for keyword matching in Gita verses (supports English and Devanagari)
ENTITIES_DICT = {
    "Krishna": {
        "type": "Deity",
        "keywords": [
            r"krishna",
            r"kṛṣṇa",
            r"vasudeva",
            r"madhusudana",
            r"hrishikesha",
            r"keshava",
            r"govinda",
            r"achyuta",
            r"madhava",
            r"कृष्ण",
            r"केशव",
            r"गोविन्द",
            r"माधव",
            r"वासुदेव",
            r"ऋषिकेश",
        ],
        "description": "Avatara of Vishnu, chariot driver and teacher of Arjuna in the Bhagavad Gita.",
    },
    "Arjuna": {
        "type": "Character",
        "keywords": [
            r"arjuna",
            r"partha",
            r"kaunteya",
            r"dhananjaya",
            r"savyasachin",
            r"gudakesha",
            r"अर्जुन",
            r"पार्थ",
            r"कौन्तेय",
            r"धनंजय",
        ],
        "description": "Third Pandava prince, the archer disciple of Sri Krishna on the battlefield of Kurukshetra.",
    },
    "Dhritarashtra": {
        "type": "Character",
        "keywords": [r"dhritarashtra", r"dhṛtarāṣṭra", r"धृतराष्ट्र"],
        "description": "The blind king of Hastinapura, father of the Kauravas.",
    },
    "Sanjaya": {
        "type": "Character",
        "keywords": [r"sanjaya", r"sañjaya", r"संजय"],
        "description": "Charioteer and advisor to Dhritarashtra, endowed with divine vision to narrate the war.",
    },
    "Duryodhana": {
        "type": "Character",
        "keywords": [r"duryodhana", r"durjodhana", r"दुर्योधन"],
        "description": "The eldest son of Dhritarashtra and leader of the Kaurava faction.",
    },
    "Bhishma": {
        "type": "Character",
        "keywords": [r"bhishma", r"bhīṣma", r"grandsire", r"भीष्म"],
        "description": "The grand patriarch of the Kuru dynasty, commander of the Kaurava army.",
    },
    "Drona": {
        "type": "Character",
        "keywords": [r"drona", r"droṇa", r"dronacharya", r"द्रोण", r"द्रोणाचार्य"],
        "description": "The royal preceptor and teacher of military arts to both Pandavas and Kauravas.",
    },
    "Karna": {
        "type": "Character",
        "keywords": [r"karna", r"karṇa", r"radheya", r"कर्ण"],
        "description": "Great warrior and ally of Duryodhana, son of Surya and Kunti.",
    },
    "Yudhishthira": {
        "type": "Character",
        "keywords": [r"yudhishthira", r"yudhiṣṭhira", r"dharmaraja", r"युधिष्ठिर"],
        "description": "Eldest Pandava prince, known for his adherence to truth and righteousness.",
    },
    "Bhima": {
        "type": "Character",
        "keywords": [r"bhima", r"bhīma", r"vrikodara", r"भीम"],
        "description": "Second Pandava brother, known for his colossal physical strength.",
    },
    "Kurukshetra": {
        "type": "Place",
        "keywords": [
            r"kurukshetra",
            r"kuru-kshetra",
            r"dharmakshetra",
            r"कुरुक्षेत्र",
            r"धर्मक्षेत्र",
        ],
        "description": "The sacred battlefield where the Mahabharata war and Gita dialogue occur.",
    },
    "Dharma": {
        "type": "Concept",
        "keywords": [r"dharma", r"righteousness", r"duty", r"धर्म"],
        "description": "Universal cosmic order and righteous duty.",
    },
    "Karma": {
        "type": "Concept",
        "keywords": [r"karma", r"action", r"कर्म"],
        "description": "Action and its corresponding consequences.",
    },
    "Atman": {
        "type": "Concept",
        "keywords": [r"atman", r"soul", r"self", r"आत्म", r"आत्मा"],
        "description": "The individual soul or self, which is immortal and distinct from the body.",
    },
    "Brahman": {
        "type": "Concept",
        "keywords": [r"brahman", r"absolute", r"supreme reality", r"ब्रह्म"],
        "description": "The ultimate impersonal reality or supreme cosmic spirit.",
    },
    "Svadharma": {
        "type": "Concept",
        "keywords": [r"svadharma", r"own duty", r"personal duty", r"स्वधर्म"],
        "description": "Personal duty or right action aligned with one's nature and social position.",
    },
    "Karma Yoga": {
        "type": "Concept",
        "keywords": [r"karma yoga", r"yoga of action", r"कर्मयोग"],
        "description": "The spiritual path of action performed without attachment to results.",
    },
    "Nishkama Karma": {
        "type": "Concept",
        "keywords": [r"nishkama", r"niṣkāma", r"desireless action", r"निष्काम"],
        "description": "Selfless or desireless action performed as an offering to the Divine.",
    },
    "Bhakti Yoga": {
        "type": "Concept",
        "keywords": [r"bhakti", r"devotion", r"भक्ति"],
        "description": "The spiritual path of love, devotion, and surrender to the Supreme Lord.",
    },
    "Jnana Yoga": {
        "type": "Concept",
        "keywords": [r"jnana", r"jñāna", r"yoga of knowledge", r"wisdom", r"ज्ञान"],
        "description": "The spiritual path of knowledge and discrimination between the real and unreal.",
    },
    "Gunas": {
        "type": "Concept",
        "keywords": [r"guna", r"sattva", r"rajas", r"tamas", r"गुण"],
        "description": "The three qualities of nature: Sattva (purity), Rajas (activity), and Tamas (inertia).",
    },
    "Samsara": {
        "type": "Concept",
        "keywords": [r"samsara", r"saṃsāra", r"rebirth", r"संसार"],
        "description": "The cycle of birth, death, and rebirth.",
    },
    "Moksha": {
        "type": "Concept",
        "keywords": [r"moksha", r"liberation", r"release", r"मोक्ष"],
        "description": "Liberation from the cycle of samsara.",
    },
    "Vishwarupa": {
        "type": "Concept",
        "keywords": [
            r"vishwarupa",
            r"viśvarūpa",
            r"cosmic form",
            r"universal form",
            r"विश्वरूप",
        ],
        "description": "The cosmic form of Lord Krishna containing the entire universe revealed to Arjuna.",
    },
    "Bhagavad Gita": {
        "type": "Text",
        "keywords": [r"bhagavad gita", r"gita", r"gītā", r"गीता"],
        "description": "The sacred 700-verse philosophical dialogue from the Bhishma Parva of Mahabharata.",
    },
}


def extract_entities_from_text(text: str) -> list:
    """Scan text for keywords and return matched entities."""
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
    """Generate valid relationships based on present entities in the batch."""
    rels = []

    if "Krishna" in entities_present and "Arjuna" in entities_present:
        rels.append(
            {
                "from": "Krishna",
                "to": "Arjuna",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "Krishna acts as Arjuna's preceptor and charioteer on the battlefield."
                },
            }
        )

    if "Arjuna" in entities_present and "Kurukshetra" in entities_present:
        rels.append(
            {
                "from": "Arjuna",
                "to": "Kurukshetra",
                "type": "LOCATED_AT",
                "attributes": {
                    "context": "Arjuna stands ready to fight at Kurukshetra."
                },
            }
        )

    if "Krishna" in entities_present and "Kurukshetra" in entities_present:
        rels.append(
            {
                "from": "Krishna",
                "to": "Kurukshetra",
                "type": "LOCATED_AT",
                "attributes": {
                    "context": "Krishna drives Arjuna's chariot at Kurukshetra."
                },
            }
        )

    if "Duryodhana" in entities_present and "Dhritarashtra" in entities_present:
        rels.append(
            {
                "from": "Duryodhana",
                "to": "Dhritarashtra",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "Duryodhana is the eldest son of Dhritarashtra."
                },
            }
        )

    if "Sanjaya" in entities_present and "Dhritarashtra" in entities_present:
        rels.append(
            {
                "from": "Sanjaya",
                "to": "Dhritarashtra",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "Sanjaya narrates the battle of Kurukshetra to the blind king Dhritarashtra."
                },
            }
        )

    if "Svadharma" in entities_present and "Dharma" in entities_present:
        rels.append(
            {
                "from": "Svadharma",
                "to": "Dharma",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "Svadharma is an individual's personal duty aligned with universal Dharma."
                },
            }
        )

    if "Karma Yoga" in entities_present and "Karma" in entities_present:
        rels.append(
            {
                "from": "Karma Yoga",
                "to": "Karma",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "Karma Yoga is practiced by performing actions (Karma) selflessly."
                },
            }
        )

    if "Atman" in entities_present and "Brahman" in entities_present:
        rels.append(
            {
                "from": "Atman",
                "to": "Brahman",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "The individual soul (Atman) is realized as non-different from the universal Brahman."
                },
            }
        )

    if "Moksha" in entities_present and "Samsara" in entities_present:
        rels.append(
            {
                "from": "Moksha",
                "to": "Samsara",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "Moksha is liberation from the cycle of rebirth (Samsara)."
                },
            }
        )

    if "Krishna" in entities_present and "Vishwarupa" in entities_present:
        rels.append(
            {
                "from": "Krishna",
                "to": "Vishwarupa",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "Krishna manifests his Vishwarupa form to Arjuna."
                },
            }
        )

    return rels


def parse_batch_file(filepath: str) -> str:
    """Read file and return combined raw text."""
    if not os.path.exists(filepath):
        return ""
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def process_batches(start: int, end: int) -> dict:
    """Process a range of batches, merge entities and relationships."""
    batch_entities = []
    seen_entities = set()
    seen_entity_names = set()

    for b_id in range(start, end + 1):
        filename = f"Bhagwat_Geeta_batch_{b_id}.md"
        filepath = os.path.join(QUERIES_DIR, filename)
        if not os.path.exists(filepath):
            continue

        content = parse_batch_file(filepath)
        matches = extract_entities_from_text(content)

        for m in matches:
            seen_entities.add(m["name"])
            if m["name"] not in seen_entity_names:
                batch_entities.append(m)
                seen_entity_names.add(m["name"])

    rels = extract_relationships_from_entities(seen_entities)

    return {
        "ontology": ONTOLOGY_HEADER,
        "entities": batch_entities,
        "relationships": rels,
    }


def main():
    os.makedirs(RESPONSES_DIR, exist_ok=True)

    # Range of batches is 1 to 84
    start_batch = 1
    end_batch = 84
    group_size = 10

    for i in range(start_batch, end_batch + 1, group_size):
        group_end = min(i + group_size - 1, end_batch)

        logger.info(f"Processing group: Bhagavad Gita batches {i} to {group_end}...")
        group_data = process_batches(i, group_end)

        output_filename = f"Bhagwat_Geeta_batch_{i}_{group_end}.json"
        output_filepath = os.path.join(RESPONSES_DIR, output_filename)

        with open(output_filepath, "w", encoding="utf-8") as f:
            json.dump(group_data, f, indent=4, ensure_ascii=False)

        logger.info(f"✓ Saved response to: {output_filepath}")


if __name__ == "__main__":
    main()
