#!/usr/bin/env python3
import json
import logging
import os
import re

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("extract_mahabharat_ontology")

# Constants
QUERIES_DIR = "ontology_project/queries/Mahabharat"
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

# Entity dictionary for keyword matching in Mahabharata verses
ENTITIES_DICT = {
    "Krishna": {
        "type": "Deity",
        "keywords": [
            r"krishna",
            r"kṛṣṇa",
            r"vasudeva",
            r"keshava",
            r"govinda",
            r"madhava",
            r"कृष्ण",
            r"वासुदेव",
            r"केशव",
        ],
        "description": "Avatara of Vishnu, supreme deity, ally of the Pandavas, and teacher of Arjuna.",
    },
    "Vishnu": {
        "type": "Deity",
        "keywords": [r"vishnu", r"viṣṇu", r"विष्णु"],
        "description": "The protector deity of the universe, of whom Krishna is an incarnation.",
    },
    "Shiva": {
        "type": "Deity",
        "keywords": [r"shiva", r"śiva", r"rudra", r"शिव", r"रुद्र"],
        "description": "The destroyer deity, who bestows weapons like the Pashupatastra upon Arjuna.",
    },
    "Ganesha": {
        "type": "Deity",
        "keywords": [r"ganesha", r"gaṇeśa", r"गणेश"],
        "description": "The elephant-headed scribe deity who wrote down the epic dictated by Vyasa.",
    },
    "Indra": {
        "type": "Deity",
        "keywords": [r"indra", r"इन्द्र"],
        "description": "King of the gods, father of Arjuna, who grants celestial weapons.",
    },
    "Arjuna": {
        "type": "Character",
        "keywords": [
            r"arjuna",
            r"partha",
            r"kaunteya",
            r"dhananjaya",
            r"अर्जुन",
            r"पार्थ",
            r"कौन्तेय",
            r"धनंजय",
        ],
        "description": "Third Pandava prince, the archer disciple of Sri Krishna on the battlefield of Kurukshetra.",
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
    "Nakula": {
        "type": "Character",
        "keywords": [r"nakula", r"नकुल"],
        "description": "Fourth Pandava prince, twin of Sahadeva, known for his beauty and expertise with swords.",
    },
    "Sahadeva": {
        "type": "Character",
        "keywords": [r"sahadeva", r"सहदेव"],
        "description": "Fifth Pandava prince, twin of Nakula, renowned for his wisdom and astrological skills.",
    },
    "Draupadi": {
        "type": "Character",
        "keywords": [
            r"draupadi",
            r"draupadī",
            r"krishnaa",
            r"panchali",
            r"द्रौपदी",
            r"पांचाली",
        ],
        "description": "The princess of Panchala, common wife of the five Pandava brothers.",
    },
    "Karna": {
        "type": "Character",
        "keywords": [r"karna", r"karṇa", r"radheya", r"कर्ण"],
        "description": "Great warrior and ally of Duryodhana, son of Surya and Kunti.",
    },
    "Duryodhana": {
        "type": "Character",
        "keywords": [r"duryodhana", r"durjodhana", r"दुर्योधन"],
        "description": "The eldest son of Dhritarashtra and leader of the Kaurava faction.",
    },
    "Dhritarashtra": {
        "type": "Character",
        "keywords": [r"dhritarashtra", r"dhṛtarāṣṭra", r"धृतराष्ट्र"],
        "description": "The blind king of Hastinapura, father of the Kauravas.",
    },
    "Gandhari": {
        "type": "Character",
        "keywords": [r"gandhari", r"gāndhārī", r"गांधारी"],
        "description": "The queen of Hastinapura, wife of Dhritarashtra, who blindfolded herself.",
    },
    "Kunti": {
        "type": "Character",
        "keywords": [r"kunti", r"kuntī", r"कुंती"],
        "description": "Mother of Yudhishthira, Bhima, Arjuna, and Karna.",
    },
    "Vidura": {
        "type": "Character",
        "keywords": [r"vidura", r"विदुर"],
        "description": "Half-brother of Dhritarashtra and Pandu, prime minister of Hastinapura, famous for his wisdom.",
    },
    "Bhishma": {
        "type": "Character",
        "keywords": [r"bhishma", r"bhīṣma", r"devavrata", r"भीष्म"],
        "description": "The grand patriarch of the Kuru dynasty, commander of the Kaurava army.",
    },
    "Drona": {
        "type": "Character",
        "keywords": [r"drona", r"droṇa", r"dronacharya", r"द्रोण", r"द्रोणाचार्य"],
        "description": "The royal preceptor and teacher of military arts to both Pandavas and Kauravas.",
    },
    "Kripa": {
        "type": "Character",
        "keywords": [r"kripa", r"kṛpa", r"kripacharya", r"कृप"],
        "description": "A family preceptor of the Kurus who fought on the Kaurava side.",
    },
    "Dhrishtadyumna": {
        "type": "Character",
        "keywords": [r"dhrishtadyumna", r"dhṛṣṭadyumna", r"धृष्टद्युम्न"],
        "description": "Commander of the Pandava army, brother of Draupadi, destined to slay Drona.",
    },
    "Ashwatthama": {
        "type": "Character",
        "keywords": [r"ashwatthama", r"aśvatthāmā", r"अश्वत्थामा"],
        "description": "Son of Dronacharya, powerful warrior and survivor of the Kurukshetra War.",
    },
    "Shakuni": {
        "type": "Character",
        "keywords": [r"shakuni", r"शकुनि"],
        "description": "Prince of Gandhara, maternal uncle of Duryodhana, architect of the game of dice.",
    },
    "Satyavati": {
        "type": "Character",
        "keywords": [r"satyavati", r"सत्यवती"],
        "description": "Matriarch of the Kuru dynasty, wife of King Shantanu, mother of Vyasa.",
    },
    "Vyasa": {
        "type": "Character",
        "keywords": [r"vyasa", r"vyāsa", r"vedavyasa", r"व्यास", r"वेदव्यास"],
        "description": "Sage who fathered Pandu, Dhritarashtra, and Vidura, and authored the Mahabharata.",
    },
    "Pandu": {
        "type": "Character",
        "keywords": [r"pandu", r"pāṇḍu", r"पाण्डु"],
        "description": "King of Hastinapura, younger brother of Dhritarashtra, father of the Pandavas.",
    },
    "Hastinapura": {
        "type": "Place",
        "keywords": [r"hastinapura", r"hastināpura", r"हस्तिनापुर"],
        "description": "The capital city of the Kuru kingdom, over which the war is fought.",
    },
    "Indraprastha": {
        "type": "Place",
        "keywords": [r"indraprastha", r"इन्द्रप्रस्थ"],
        "description": "The capital city built by the Pandavas in the forest of Khandavaprastha.",
    },
    "Kurukshetra": {
        "type": "Place",
        "keywords": [r"kurukshetra", r"कुरुक्षेत्र"],
        "description": "The sacred battlefield where the Mahabharata war and Gita dialogue occur.",
    },
    "Dwarka": {
        "type": "Place",
        "keywords": [r"dwarka", r"dvārakā", r"द्वारका"],
        "description": "The island city ruled by Krishna.",
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
    "Bhakti": {
        "type": "Concept",
        "keywords": [r"bhakti", r"devotion", r"भक्ति"],
        "description": "The spiritual path of love, devotion, and surrender to the Divine.",
    },
    "Moksha": {
        "type": "Concept",
        "keywords": [r"moksha", r"liberation", r"मोक्ष"],
        "description": "Liberation from the cycle of samsara.",
    },
    "Kurukshetra War": {
        "type": "Event",
        "keywords": [r"war", r"battle", r"yuddha", r"युद्ध", r"संग्राम"],
        "description": "The great 18-day battle between the Pandavas and Kauravas.",
    },
    "Game of Dice": {
        "type": "Event",
        "keywords": [r"dice", r"game", r"dyuta", r"द्यूत"],
        "description": "The gambling match between Yudhishthira and Shakuni which led to the exile.",
    },
    "Mahabharata": {
        "type": "Text",
        "keywords": [r"mahabharata", r"mahabharat", r"महाभारत"],
        "description": "The monumental Sanskrit epic detailing the history of the Kuru dynasty.",
    },
    "Bhagavad Gita": {
        "type": "Text",
        "keywords": [r"bhagavad gita", r"gita", r"gītā", r"गीता"],
        "description": "The sacred dialogue spoken by Krishna to Arjuna before the Kurukshetra War.",
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

    pandavas = ["Yudhishthira", "Bhima", "Arjuna", "Nakula", "Sahadeva"]

    # 1. Pandavas relationship to each other
    for p1 in pandavas:
        for p2 in pandavas:
            if p1 != p2 and p1 in entities_present and p2 in entities_present:
                rels.append(
                    {
                        "from": p1,
                        "to": p2,
                        "type": "RELATED_TO",
                        "attributes": {
                            "context": f"{p1} and {p2} are brothers (the Pandavas)."
                        },
                    }
                )

    # 2. Pandavas to Draupadi
    for p in pandavas:
        if p in entities_present and "Draupadi" in entities_present:
            rels.append(
                {
                    "from": p,
                    "to": "Draupadi",
                    "type": "RELATED_TO",
                    "attributes": {"context": f"{p} is married to Draupadi."},
                }
            )

    # 3. Pandavas to Kunti
    for p in pandavas:
        if p in entities_present and "Kunti" in entities_present:
            rels.append(
                {
                    "from": p,
                    "to": "Kunti",
                    "type": "RELATED_TO",
                    "attributes": {"context": f"{p} is a son of Kunti."},
                }
            )

    # 4. Duryodhana & Dhritarashtra / Gandhari
    if "Duryodhana" in entities_present:
        if "Dhritarashtra" in entities_present:
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
        if "Gandhari" in entities_present:
            rels.append(
                {
                    "from": "Duryodhana",
                    "to": "Gandhari",
                    "type": "RELATED_TO",
                    "attributes": {"context": "Duryodhana is a son of Gandhari."},
                }
            )
        if "Shakuni" in entities_present:
            rels.append(
                {
                    "from": "Duryodhana",
                    "to": "Shakuni",
                    "type": "RELATED_TO",
                    "attributes": {
                        "context": "Shakuni is Duryodhana's maternal uncle and close advisor."
                    },
                }
            )
        if "Karna" in entities_present:
            rels.append(
                {
                    "from": "Duryodhana",
                    "to": "Karna",
                    "type": "RELATED_TO",
                    "attributes": {
                        "context": "Karna is Duryodhana's closest friend and key ally."
                    },
                }
            )

    # 5. Pandavas/Kauravas to Bhishma
    for p in pandavas + ["Duryodhana"]:
        if p in entities_present and "Bhishma" in entities_present:
            rels.append(
                {
                    "from": p,
                    "to": "Bhishma",
                    "type": "RELATED_TO",
                    "attributes": {"context": f"Bhishma is the grandsire of {p}."},
                }
            )

    # 6. Pandavas/Kauravas to Drona
    for p in pandavas + ["Duryodhana"]:
        if p in entities_present and "Drona" in entities_present:
            rels.append(
                {
                    "from": p,
                    "to": "Drona",
                    "type": "RELATED_TO",
                    "attributes": {"context": f"Drona is the teacher of {p}."},
                }
            )

    # 7. Arjuna and Krishna
    if "Arjuna" in entities_present and "Krishna" in entities_present:
        rels.append(
            {
                "from": "Krishna",
                "to": "Arjuna",
                "type": "RELATED_TO",
                "attributes": {
                    "context": "Krishna acts as Arjuna's charioteer, guide, and spiritual teacher."
                },
            }
        )

    # 8. Participation in Kurukshetra War
    all_warriors = pandavas + [
        "Duryodhana",
        "Bhishma",
        "Drona",
        "Karna",
        "Ashwatthama",
        "Dhrishtadyumna",
    ]
    for w in all_warriors:
        if w in entities_present and "Kurukshetra War" in entities_present:
            rels.append(
                {
                    "from": w,
                    "to": "Kurukshetra War",
                    "type": "PARTICIPATED_IN",
                    "attributes": {
                        "context": f"{w} participated as a major combatant in the Kurukshetra War."
                    },
                }
            )

    # 9. Participation in Game of Dice
    for actor in ["Yudhishthira", "Duryodhana", "Shakuni"]:
        if actor in entities_present and "Game of Dice" in entities_present:
            rels.append(
                {
                    "from": actor,
                    "to": "Game of Dice",
                    "type": "PARTICIPATED_IN",
                    "attributes": {
                        "context": f"{actor} participated in the fateful Game of Dice."
                    },
                }
            )

    # 10. Places locations
    for p in pandavas + ["Duryodhana", "Dhritarashtra", "Bhishma"]:
        if p in entities_present and "Hastinapura" in entities_present:
            rels.append(
                {
                    "from": p,
                    "to": "Hastinapura",
                    "type": "LOCATED_AT",
                    "attributes": {
                        "context": f"{p} resided at or ruled from Hastinapura."
                    },
                }
            )

    for p in pandavas:
        if p in entities_present and "Indraprastha" in entities_present:
            rels.append(
                {
                    "from": p,
                    "to": "Indraprastha",
                    "type": "LOCATED_AT",
                    "attributes": {
                        "context": f"{p} founded and ruled from Indraprastha."
                    },
                }
            )

    return rels


def parse_batch_file(filepath: str) -> str:
    if not os.path.exists(filepath):
        return ""
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def process_batches(start: int, end: int) -> dict:
    batch_entities = []
    seen_entities = set()
    seen_entity_names = set()

    for b_id in range(start, end + 1):
        filename = f"Mahabharat_batch_{b_id}.md"
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

    start_batch = 1
    end_batch = 844
    group_size = 10

    for i in range(start_batch, end_batch + 1, group_size):
        group_end = min(i + group_size - 1, end_batch)

        logger.info(f"Processing group: Mahabharata batches {i} to {group_end}...")
        group_data = process_batches(i, group_end)

        output_filename = f"Mahabharat_batch_{i}_{group_end}.json"
        output_filepath = os.path.join(RESPONSES_DIR, output_filename)

        with open(output_filepath, "w", encoding="utf-8") as f:
            json.dump(group_data, f, indent=4, ensure_ascii=False)

        logger.info(f"✓ Saved response to: {output_filepath}")


if __name__ == "__main__":
    main()
