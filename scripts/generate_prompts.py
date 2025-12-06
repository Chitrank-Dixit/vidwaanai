#!/usr/bin/env python3
import json
import os
from datetime import datetime

# Sample data extracted from user request
SAMPLES = {
    "en": [
        {
            "id": "en_ramayana_001",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "Who was Ram's father in the Ramayana?",
            "prompt_english": "Who was Ram's father in the Ramayana?",
            "expected_answer_keywords": ["Dasharatha", "King Dasharatha"],
            "context": "Ramayana - Balakanda",
            "tags": ["characters", "family", "ayodhya"],
        },
        {
            "id": "en_ramayana_002",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "In which city was Ram born?",
            "prompt_english": "In which city was Ram born?",
            "expected_answer_keywords": ["Ayodhya"],
            "context": "Ramayana - Balakanda",
            "tags": ["locations", "birth", "ayodhya"],
        },
        {
            "id": "en_ramayana_003",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "Who was Ram's wife?",
            "prompt_english": "Who was Ram's wife?",
            "expected_answer_keywords": ["Sita", "Janaki"],
            "context": "Ramayana - Balakanda",
            "tags": ["characters", "family", "marriage"],
        },
        {
            "id": "en_ramayana_004",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "Who abducted Sita?",
            "prompt_english": "Who abducted Sita?",
            "expected_answer_keywords": ["Ravana"],
            "context": "Ramayana - Aranyakanda",
            "tags": ["major_events", "conflict", "lanka"],
        },
        {
            "id": "en_ramayana_005",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "Who was Ram's best friend?",
            "prompt_english": "Who was Ram's best friend?",
            "expected_answer_keywords": ["Hanuman", "Sugriva"],
            "context": "Ramayana - Kishkindhakanda",
            "tags": ["characters", "relationships", "monkeys"],
        },
        {
            "id": "en_ramayana_006",
            "category": "ramayana",
            "difficulty": "medium",
            "prompt": "Why was Ram exiled from Ayodhya?",
            "prompt_english": "Why was Ram exiled from Ayodhya?",
            "expected_answer_keywords": ["mother's wish", "Kaikeyi", "boon", "kingdom"],
            "context": "Ramayana - Ayodhyakanda",
            "tags": ["plot_points", "exile", "family"],
        },
        {
            "id": "en_ramayana_007",
            "category": "ramayana",
            "difficulty": "medium",
            "prompt": "What was the purpose of Ram's journey to Lanka?",
            "prompt_english": "What was the purpose of Ram's journey to Lanka?",
            "expected_answer_keywords": ["rescue Sita", "defeat Ravana", "dharma"],
            "context": "Ramayana - Yuddhakanda",
            "tags": ["plot_points", "war", "dharma"],
        },
        {
            "id": "en_ramayana_008",
            "category": "ramayana",
            "difficulty": "medium",
            "prompt": "What challenges did Ram face in the forest?",
            "prompt_english": "What challenges did Ram face in the forest?",
            "expected_answer_keywords": ["demons", "separation from Sita", "hardship"],
            "context": "Ramayana - Aranyakanda",
            "tags": ["plot_points", "challenges", "forest"],
        },
        {
            "id": "en_ramayana_009",
            "category": "ramayana",
            "difficulty": "hard",
            "prompt": "What does Ram's exile teach us about duty and dharma in Hindu philosophy?",
            "prompt_english": "What does Ram's exile teach us about duty and dharma in Hindu philosophy?",
            "expected_answer_keywords": [
                "duty",
                "sacrifice",
                "righteousness",
                "familial obligation",
                "karma",
            ],
            "context": "Ramayana - Philosophy",
            "tags": ["philosophy", "dharma", "ethics"],
        },
        {
            "id": "en_ramayana_010",
            "category": "ramayana",
            "difficulty": "hard",
            "prompt": "How did Ram balance his personal desires with his duties as a son and king?",
            "prompt_english": "How did Ram balance his personal desires with his duties as a son and king?",
            "expected_answer_keywords": [
                "dharma",
                "personal vs public",
                "sacrifice",
                "principles",
                "morality",
            ],
            "context": "Ramayana - Philosophy",
            "tags": ["philosophy", "leadership", "dilemma"],
        },
        # Add a few more from samples to ensure good coverage
        {
            "id": "en_gita_001",
            "category": "bhagavad_gita",
            "difficulty": "easy",
            "prompt": "What is the setting of the Bhagavad Gita?",
            "prompt_english": "What is the setting of the Bhagavad Gita?",
            "expected_answer_keywords": ["Kurukshetra", "battlefield", "war"],
            "context": "Bhagavad Gita - Chapter 1",
            "tags": ["setting", "context"],
        },
        {
            "id": "en_hinduism_001",
            "category": "hinduism",
            "difficulty": "easy",
            "prompt": "Name the major Hindu festival associated with victory of good over evil.",
            "prompt_english": "Name the major Hindu festival associated with victory of good over evil.",
            "expected_answer_keywords": ["Diwali", "Deepavali", "lights"],
            "context": "Hinduism - Festivals",
            "tags": ["culture", "festivals"],
        },
    ],
    "hi": [
        {
            "id": "hi_ramayana_001",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "रामायण में राम के पिता का नाम क्या था?",
            "prompt_english": "What was the name of Ram's father in the Ramayana?",
            "expected_answer_keywords": ["दशरथ", "राजा दशरथ"],
            "context": "Ramayana - Balakanda",
            "tags": ["characters", "family", "ayodhya"],
        },
        {
            "id": "hi_ramayana_002",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "राम का जन्म किस नगर में हुआ?",
            "prompt_english": "In which city was Ram born?",
            "expected_answer_keywords": ["अयोध्या"],
            "context": "Ramayana - Balakanda",
            "tags": ["locations", "birth", "ayodhya"],
        },
        {
            "id": "hi_ramayana_003",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "राम की पत्नी कौन थी?",
            "prompt_english": "Who was Ram's wife?",
            "expected_answer_keywords": ["सीता", "जानकी"],
            "context": "Ramayana - Balakanda",
            "tags": ["characters", "family", "marriage"],
        },
        {
            "id": "hi_ramayana_004",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "सीता का हरण किसने किया?",
            "prompt_english": "Who abducted Sita?",
            "expected_answer_keywords": ["रावण"],
            "context": "Ramayana - Aranyakanda",
            "tags": ["major_events", "conflict", "lanka"],
        },
        {
            "id": "hi_ramayana_005",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "राम का सबसे अच्छा दोस्त कौन था?",
            "prompt_english": "Who was Ram's best friend?",
            "expected_answer_keywords": ["हनुमान"],
            "context": "Ramayana - Kishkindhakanda",
            "tags": ["characters", "relationships", "monkeys"],
        },
    ],
    "ta": [
        {
            "id": "ta_ramayana_001",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "இராமாயணத்தில் இராமனின் தந்தையின் பெயர் என்ன?",
            "prompt_english": "What was the name of Ram's father in the Ramayana?",
            "expected_answer_keywords": ["தசரதன்", "அரசன் தசரதன்"],
            "context": "Ramayana - Balakanda",
            "tags": ["characters", "family", "ayodhya"],
        },
        {
            "id": "ta_ramayana_002",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "ராமன் எந்த நகரில் பிறந்தான்?",
            "prompt_english": "In which city was Ram born?",
            "expected_answer_keywords": ["அயோத்தி"],
            "context": "Ramayana - Balakanda",
            "tags": ["locations", "birth", "ayodhya"],
        },
        {
            "id": "ta_ramayana_003",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "சீதை யாரால் கடத்தப்பட்டாள்?",
            "prompt_english": "Who abducted Sita?",
            "expected_answer_keywords": ["இரணியன்"],
            "context": "Ramayana - Aranyakanda",
            "tags": ["major_events", "conflict", "lanka"],
        },
        {
            "id": "ta_ramayana_004",
            "category": "ramayana",
            "difficulty": "hard",
            "prompt": "ராமாயணம் நமக்கு கர்தவ்யம் மற்றும் தர்மமைப் பற்றி என்ன கற்பிக்கிறது?",
            "prompt_english": "What does Ramayana teach us about duty and dharma?",
            "expected_answer_keywords": [
                "கர்தவ்யம்",
                "தியாகம்",
                "நீதி",
                "குடும்ப கர்தவ்யம்",
                "கர்மா",
            ],
            "context": "Ramayana - Philosophy",
            "tags": ["philosophy", "dharma", "ethics"],
        },
    ],
    "bho": [
        {
            "id": "bho_ramayana_001",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "रामायनमा राम के बाप के नाम का बा काहे?",
            "prompt_english": "What was the name of Ram's father in the Ramayana?",
            "expected_answer_keywords": ["दशरथ", "राजा दशरथ"],
            "context": "Ramayana - Balakanda",
            "tags": ["characters", "family", "ayodhya"],
        },
        {
            "id": "bho_ramayana_002",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "राम का जन्म कउन नगर मा हुअल?",
            "prompt_english": "In which city was Ram born?",
            "expected_answer_keywords": ["अयोध्या"],
            "context": "Ramayana - Balakanda",
            "tags": ["locations", "birth", "ayodhya"],
        },
        {
            "id": "bho_ramayana_003",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "सीता के पति कउन हलें?",
            "prompt_english": "Who was Sita's husband?",
            "expected_answer_keywords": ["राम"],
            "context": "Ramayana - Balakanda",
            "tags": ["characters", "family", "marriage"],
        },
        {
            "id": "bho_ramayana_004",
            "category": "ramayana",
            "difficulty": "hard",
            "prompt": "रामायण से हमार धर्म अउर कर्तव्य के बारे मा का सिखाई?",
            "prompt_english": "What does Ramayana teach us about our dharma and duty?",
            "expected_answer_keywords": ["धर्म", "कर्तव्य", "त्याग", "न्याय", "कर्म"],
            "context": "Ramayana - Philosophy",
            "tags": ["philosophy", "dharma", "ethics"],
        },
    ],
    "mai": [
        {
            "id": "mai_ramayana_001",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "रामायणमे रामक पिता केर नाम की छल?",
            "prompt_english": "What was the name of Ram's father in the Ramayana?",
            "expected_answer_keywords": ["दशरथ"],
            "context": "Ramayana - Balakanda",
            "tags": ["characters", "family", "ayodhya"],
        },
        {
            "id": "mai_ramayana_002",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "राम केर जन्मक समय कि नाम रखल गेल?",
            "prompt_english": "What name was given to Ram at birth?",
            "expected_answer_keywords": ["राम"],
            "context": "Ramayana - Balakanda",
            "tags": ["characters", "birth"],
        },
    ],
    "raj": [
        {
            "id": "raj_ramayana_001",
            "category": "ramayana",
            "difficulty": "easy",
            "prompt": "रामायण मांय राम के पिता को नाम काय हो?",
            "prompt_english": "What was the name of Ram's father in the Ramayana?",
            "expected_answer_keywords": ["दशरथ"],
            "context": "Ramayana - Balakanda",
            "tags": ["characters", "family", "ayodhya"],
        }
    ],
}

LANGUAGES = [
    {"code": "en", "name": "English"},
    {"code": "hi", "name": "Hindi"},
    {"code": "sa", "name": "Sanskrit"},
    {"code": "bn", "name": "Bengali"},
    {"code": "gu", "name": "Gujarati"},
    {"code": "kn", "name": "Kannada"},
    {"code": "ml", "name": "Malayalam"},
    {"code": "mr", "name": "Marathi"},
    {"code": "ta", "name": "Tamil"},
    {"code": "te", "name": "Telugu"},
    {"code": "bho", "name": "Bhojpuri"},
    {"code": "mai", "name": "Maithili"},
    {"code": "raj", "name": "Rajasthani"},
    {"code": "bgc", "name": "Haryanvi"},
    {"code": "hne", "name": "Chhattisgarhi"},
    {"code": "doi", "name": "Dogri"},
    {"code": "kok", "name": "Konkani"},
]


def generate_prompts():
    output_dir = "tests/prompt_suite"
    os.makedirs(output_dir, exist_ok=True)

    for lang in LANGUAGES:
        code = lang["code"]
        name = lang["name"]
        filename = os.path.join(output_dir, f"{code}_prompts.json")

        # Get samples or empty list
        prompts = SAMPLES.get(code, [])

        # If no samples, add a placeholder TODO prompt to avoid empty file issues
        if not prompts:
            prompts = [
                {
                    "id": f"{code}_ramayana_001",
                    "category": "ramayana",
                    "difficulty": "easy",
                    "prompt": f"[TODO: Add {name} prompt here]",
                    "prompt_english": "Placeholder prompt",
                    "expected_answer_keywords": [],
                    "context": "Placeholder",
                    "tags": ["todo"],
                }
            ]

        data = {
            "metadata": {
                "language_code": code,
                "language_name": name,
                "total_prompts": len(prompts),
                "generation_date": datetime.now().strftime("%Y-%m-%d"),
                "version": "1.0",
            },
            "prompts": prompts,
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"Generated {filename} with {len(prompts)} prompts")


if __name__ == "__main__":
    generate_prompts()
