# Manual Entity Extraction Prompt

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

### Verse 1 (Vishnu Puran 0.2561)
- **Original**: 75 सर्वभूतेषु सर्वात्मन्या शक्तिरपरा तव। गुणाश्रया नमस्तस्थ शञाप्नताये सुरेश्वर
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2562)
- **Original**: 76 यातीतगोचरा बात्नां मनसां चाविशेषणा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2563)
- **Original**: ज्ञानिज्ञानपरिच्छेद्ा ता वन्‍्दे स्वेश्वरीं पराम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2564)
- **Original**: 77 34 नमो बासुदेवाय तस्मै भगवते सदा। व्यतिस्क्ति न यस्यास्ति व्यतिरिक्तोडखिलस्य यः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2565)
- **Original**: 78 नमस्तस्मै नमस्तस्मै नमस्तस्मे महात्मने । नाम रूप न यस्थैको योउस्तित्वेनोपलभ्यते
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2566)
- **Original**: 79 यस्थावताररूपाणि समर्चन्ति दिवोकसः । अपश्यन्त: पर रूप नमस्तस्मे महात्मने
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2567)
- **Original**: 80 योउन्तस्तिप्नन्नशेषस्य पश्यतीश: शुभाशुभम। ते सर्वसाक्षिण विश्व नपस्थे परेश्वरम
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2568)
- **Original**: 89 नमोस्तु विष्णवे तस्मै यस्याभिन्नमिदं जगत्‌ । ध्येय: स जगतामाद्यः स प्रसीदतु मेउव्यय:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2569)
- **Original**: 82 अत्रोतमेतत्ओतं विश्वमक्षरमव्ययम्‌ आधारभूत: सर्वस्य स प्रसीदतु मे हरि:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2570)
- **Original**: 83 मे सब व स्व थे सब सका
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2571)
- **Original**: 84 एवाहमवस्थित: । ग्त्त: सर्वपह सर्व मयि सर्वे सनातने
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2572)
- **Original**: 85 अहमेवाक्षयो नित्य: परमात्मात्मसंभ्रय: । ब्रह्मसंज्ञोहहमेवाश्रे तथान्ते चर पर: पुमान्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2573)
- **Original**: 86 आपको नमस्कार है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2574)
- **Original**: हे सर्वात्मन्‌ ! समस्त भूतोंमें आपकी जो गुणाश्रया पग़दाक्ति है, हे सुरेश्वर! उस नित्यस्वरूपिणीको नमस्कार है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2575)
- **Original**: जो वाणी और मनके परे है, विश्ोषणरहित तथा ज्ञानियोके ज्ञानसे परिच्छेद्य है उस स्वतन्त्रा पराहक्तिकी मैं वन्‍्दना करता हैँ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2576)
- **Original**: 3% उन भगवान्‌ वासुदेक्कों सदा नमस्कार है, जिनसे अतिरिक्त और कोई वस्तु नहीं है तथा जो स्वयं सबसे अतिरिक्त (असम) हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2577)
- **Original**: जिनका कोई भी नाम अथवा रूप नहीं है और जो अपनी सत्तामात्रसे ही उपलब्ध होते है उन महात्माकों नमस्कार है, नमस्कार है, नमस्कार है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2578)
- **Original**: जिनके पर-स्वरूपको न जानते हुए ही देवतागण उनके अवतार-जरीरोंका सम्यक्‌ अर्चन करते हैं उन महात्माकों नमस्कार है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2579)
- **Original**: जो ईश्वर सबके अन्तःकरणोमें स्थित होकर उनके शुभाशुभ कर्मोंको देखते हैं उन सर्वसाक्षी विश्रकप परमेश्वरकों मैं नमस्कार करता हूँ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2580)
- **Original**: जिनसे यह जगत्‌ सर्वथा अभिन्न है उन श्रीविष्णु- भगवान्‌कों नमस्कार है वे जगतके आदिकारण और पोगियोंके ध्येय अव्यय हरि मुझपर प्रसन्न हों
- **Translation**: 

---

