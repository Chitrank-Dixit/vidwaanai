#!/usr/bin/env python3
import os
import re
import json
import logging
import glob

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("extract_puranas_ontology")

# Constants
QUERIES_DIR = "ontology_project/queries/Puranas"
RESPONSES_DIR = "scripts/responses/gemini"

ONTOLOGY_HEADER = {
    "entity_types": [
        "Deity",
        "Concept",
        "Character",
        "Place",
        "Event",
        "Text"
    ],
    "relationship_types": [
        "MENTIONS",
        "IS_AVATAR_OF",
        "RELATED_TO",
        "LOCATED_AT",
        "PARTICIPATED_IN"
    ]
}

# Puranic entities dictionary
ENTITIES_DICT = {
    "Vishnu": {
        "type": "Deity",
        "keywords": [r"vishnu", r"viṣṇu", r"narayana", r"nārāyaṇa", r"विष्णु", r"नारायण"],
        "description": "The preserver deity of the Hindu trimurti, major deity of Vaishnava Puranas."
    },
    "Shiva": {
        "type": "Deity",
        "keywords": [r"shiva", r"śiva", r"rudra", r"mahadeva", r"शिव", r"रुद्र", r"महादेव"],
        "description": "The destroyer deity of the Hindu trimurti, major deity of Shaiva Puranas."
    },
    "Brahma": {
        "type": "Deity",
        "keywords": [r"brahma", r"brahmā", r"ब्रह्मा"],
        "description": "The creator deity of the Hindu trimurti."
    },
    "Devi": {
        "type": "Deity",
        "keywords": [r"devi", r"devī", r"shakti", r"durga", r"parvati", r"देवी", r"शक्ति", r"दुर्गा", r"पार्वती"],
        "description": "The supreme goddess, representing cosmic energy and female divinity."
    },
    "Ganesha": {
        "type": "Deity",
        "keywords": [r"ganesha", r"gaṇeśa", r"vinayaka", r"गणेश", r"विनायक"],
        "description": "The elephant-headed deity of wisdom and remover of obstacles."
    },
    "Skanda": {
        "type": "Deity",
        "keywords": [r"skanda", r"kartikeya", r"kārtikeya", r"स्कन्द", r"कार्तिकेय"],
        "description": "The god of war, son of Shiva and Parvati."
    },
    "Surya": {
        "type": "Deity",
        "keywords": [r"surya", r"sūrya", r"sun", r"सूर्य"],
        "description": "The solar deity, source of light and life."
    },
    "Indra": {
        "type": "Deity",
        "keywords": [r"indra", r"इन्द्र"],
        "description": "The king of the gods and ruler of Svarga (heaven)."
    },
    "Agni": {
        "type": "Deity",
        "keywords": [r"agni", r"fire", r"अग्नि"],
        "description": "The fire god, acting as the mediator between humans and gods in rituals."
    },
    "Varuna": {
        "type": "Deity",
        "keywords": [r"varuna", r"varuṇa", r"वरुण"],
        "description": "The god of oceans, waters, and cosmic law."
    },
    "Yama": {
        "type": "Deity",
        "keywords": [r"yama", r"यम"],
        "description": "The god of death and justice."
    },
    "Vyasa": {
        "type": "Character",
        "keywords": [r"vyasa", r"vyāsa", r"vedavyasa", r"व्यास"],
        "description": "The legendary sage credited with compiling the Vedas and Puranas."
    },
    "Manu": {
        "type": "Character",
        "keywords": [r"manu", r"मनु"],
        "description": "The progenitor of humanity and ruler of each Manvantara."
    },
    "Narada": {
        "type": "Character",
        "keywords": [r"narada", r"nārada", r"नारद"],
        "description": "The divine sage and messenger of the gods."
    },
    "Vashishtha": {
        "type": "Character",
        "keywords": [r"vashishtha", r"vaśiṣṭha", r"वशिष्ठ"],
        "description": "One of the Saptarishis (seven great sages), preceptor of Ikshvaku dynasty."
    },
    "Vishvamitra": {
        "type": "Character",
        "keywords": [r"vishvamitra", r"viśvāmitra", r"विश्वामित्र"],
        "description": "A great sage and king who attained the status of Brahmarishi through asceticism."
    },
    "Daksha": {
        "type": "Character",
        "keywords": [r"daksha", r"daṣa", r"दक्ष"],
        "description": "A creator patriarch (Prajapati), son of Brahma."
    },
    "Dhruva": {
        "type": "Character",
        "keywords": [r"dhruva", r"ध्रुव"],
        "description": "A devotee of Vishnu who attained the status of the pole star."
    },
    "Prahlada": {
        "type": "Character",
        "keywords": [r"prahlada", r"prahlāda", r"प्रह्लाद"],
        "description": "A saintly prince, devotee of Vishnu, saved from his demon father Hiranyakashipu."
    },
    "Bali": {
        "type": "Character",
        "keywords": [r"bali", r"बलि", r"mahabali"],
        "description": "The benevolent demon king who offered three paces of land to Vamana avatar."
    },
    "Kailash": {
        "type": "Place",
        "keywords": [r"kailash", r"kailāsa", r"कैलाश"],
        "description": "The sacred mountain abode of Lord Shiva."
    },
    "Vaikuntha": {
        "type": "Place",
        "keywords": [r"vaikuntha", r"vaikuṇṭha", r"वैकुण्ठ"],
        "description": "The celestial abode of Lord Vishnu."
    },
    "Kashi": {
        "type": "Place",
        "keywords": [r"kashi", r"kāśī", r"varanasi", r"काशी", r"वाराणसी"],
        "description": "The sacred city of Shiva, center of pilgrimage."
    },
    "Ganga": {
        "type": "Place",
        "keywords": [r"ganga", r"gaṅgā", r"गंगा"],
        "description": "The sacred river deity, who descended from heaven to purify souls."
    },
    "Dharma": {
        "type": "Concept",
        "keywords": [r"dharma", r"righteousness", r"धर्म"],
        "description": "Universal cosmic order and righteous duty."
    },
    "Yajna": {
        "type": "Concept",
        "keywords": [r"yajna", r"yajña", r"sacrifice", r"यज्ञ"],
        "description": "Ritual fire sacrifices and offerings."
    },
    "Yuga": {
        "type": "Concept",
        "keywords": [r"yuga", r"satya", r"treta", r"dvapara", r"kali", r"युग"],
        "description": "Cosmic age cyclical divisions (Satya, Treta, Dvapara, Kali)."
    },
    "Manvantara": {
        "type": "Concept",
        "keywords": [r"manvantara", r"मन्वन्तर"],
        "description": "Cosmic era ruled by a specific Manu, consisting of 71 Mahayugas."
    },
    "Samudra Manthan": {
        "type": "Event",
        "keywords": [r"churning", r"manthan", r"समुद्र मंथन"],
        "description": "The churning of the cosmic ocean by gods and demons to obtain Amrita."
    },
    "Creation": {
        "type": "Event",
        "keywords": [r"creation", r"srishti", r"sṛṣṭi", r"सृष्टि"],
        "description": "The cosmic creation process described in the Sarga sections of Puranas."
    },
    "Mahapuranas": {
        "type": "Text",
        "keywords": [r"purana", r"purāṇa", r"mahavidyas", r"पुराण"],
        "description": "The genre of 18 major Hindu encyclopedic scriptures."
    }
}

def extract_entities_from_text(text: str) -> list:
    matched = []
    text_lower = text.lower()
    for entity_name, info in ENTITIES_DICT.items():
        for kw in info["keywords"]:
            if re.search(kw, text_lower):
                matched.append({
                    "name": entity_name,
                    "type": info["type"],
                    "attributes": {"description": info["description"]}
                })
                break
    return matched

def extract_relationships_from_entities(entities_present: set) -> list:
    rels = []
    
    # Trimurti relationships
    if "Brahma" in entities_present and "Vishnu" in entities_present:
        rels.append({
            "from": "Brahma",
            "to": "Vishnu",
            "type": "RELATED_TO",
            "attributes": {"context": "Brahma creates the universe under the guidance of Vishnu."}
        })
    if "Shiva" in entities_present and "Vishnu" in entities_present:
        rels.append({
            "from": "Shiva",
            "to": "Vishnu",
            "type": "RELATED_TO",
            "attributes": {"context": "Shiva and Vishnu represent the complementary forces of destruction and preservation."}
        })

    # Devi relationships
    if "Devi" in entities_present and "Shiva" in entities_present:
        rels.append({
            "from": "Devi",
            "to": "Shiva",
            "type": "RELATED_TO",
            "attributes": {"context": "Devi (as Parvati or Sati) is the consort of Shiva."}
        })

    # Family relationships
    if "Ganesha" in entities_present and "Shiva" in entities_present:
        rels.append({
            "from": "Ganesha",
            "to": "Shiva",
            "type": "RELATED_TO",
            "attributes": {"context": "Ganesha is the son of Lord Shiva."}
        })
    if "Skanda" in entities_present and "Shiva" in entities_present:
        rels.append({
            "from": "Skanda",
            "to": "Shiva",
            "type": "RELATED_TO",
            "attributes": {"context": "Skanda is the son of Lord Shiva."}
        })

    # Sages to Deities
    for sage in ["Vyasa", "Narada", "Vashishtha", "Vishvamitra"]:
        if sage in entities_present and "Vishnu" in entities_present:
            rels.append({
                "from": sage,
                "to": "Vishnu",
                "type": "RELATED_TO",
                "attributes": {"context": f"Sage {sage} is a devoted follower/avatara of Vishnu."}
            })
        if sage in entities_present and "Shiva" in entities_present:
            rels.append({
                "from": sage,
                "to": "Shiva",
                "type": "RELATED_TO",
                "attributes": {"context": f"Sage {sage} performs penance and worships Shiva."}
            })

    # Devotees and Avatars
    if "Dhruva" in entities_present and "Vishnu" in entities_present:
        rels.append({
            "from": "Dhruva",
            "to": "Vishnu",
            "type": "RELATED_TO",
            "attributes": {"context": "Dhruva performed severe penance to obtain the vision of Vishnu."}
        })
    if "Prahlada" in entities_present and "Vishnu" in entities_present:
        rels.append({
            "from": "Prahlada",
            "to": "Vishnu",
            "type": "RELATED_TO",
            "attributes": {"context": "Prahlada is saved by Vishnu in his Narasimha incarnation."}
        })
    if "Bali" in entities_present and "Vishnu" in entities_present:
        rels.append({
            "from": "Bali",
            "to": "Vishnu",
            "type": "RELATED_TO",
            "attributes": {"context": "Bali surrenders his empire to Vamana (Vishnu's avatar)."}
        })

    # Locations
    if "Shiva" in entities_present and "Kailash" in entities_present:
        rels.append({
            "from": "Shiva",
            "to": "Kailash",
            "type": "LOCATED_AT",
            "attributes": {"context": "Shiva resides on Mount Kailash."}
        })
    if "Vishnu" in entities_present and "Vaikuntha" in entities_present:
        rels.append({
            "from": "Vishnu",
            "to": "Vaikuntha",
            "type": "LOCATED_AT",
            "attributes": {"context": "Vishnu resides in the heavenly realm Vaikuntha."}
        })
    if "Ganga" in entities_present and "Shiva" in entities_present:
        rels.append({
            "from": "Ganga",
            "to": "Shiva",
            "type": "RELATED_TO",
            "attributes": {"context": "Shiva holds Ganga in his matted locks to ease her descent."}
        })

    # Events
    if "Samudra Manthan" in entities_present:
        for deity in ["Vishnu", "Shiva", "Indra"]:
            if deity in entities_present:
                rels.append({
                    "from": deity,
                    "to": "Samudra Manthan",
                    "type": "PARTICIPATED_IN",
                    "attributes": {"context": f"Lord {deity} played a critical role in Samudra Manthan."}
                })

    return rels

def parse_batch_file(filepath: str) -> str:
    if not os.path.exists(filepath):
        return ""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def process_purana_directory(purana_dir: str, purana_name: str):
    """Process all batches in a specific Purana directory."""
    files = sorted(glob.glob(os.path.join(purana_dir, "*.md")))
    if not files:
        logger.warning(f"No md files found in {purana_dir}")
        return
        
    logger.info(f"Processing Purana '{purana_name}' ({len(files)} batch files)...")
    
    group_size = 10
    
    # Process files in groups of 10
    for idx in range(0, len(files), group_size):
        group_files = files[idx:idx + group_size]
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
            "relationships": rels
        }
        
        output_filename = f"{purana_name}_batch_{start_batch}_{end_batch}.json"
        output_filepath = os.path.join(RESPONSES_DIR, output_filename)
        
        with open(output_filepath, "w", encoding="utf-8") as f:
            json.dump(group_data, f, indent=4, ensure_ascii=False)

def main():
    os.makedirs(RESPONSES_DIR, exist_ok=True)
    
    # Get all subdirectories in queries/Puranas/
    subdirs = sorted([d for d in glob.glob(os.path.join(QUERIES_DIR, "*")) if os.path.isdir(d)])
    
    for subdir in subdirs:
        purana_name = os.path.basename(subdir)
        process_purana_directory(subdir, purana_name)
        
    logger.info("Successfully extracted ontology responses for all Puranas!")

if __name__ == "__main__":
    main()
