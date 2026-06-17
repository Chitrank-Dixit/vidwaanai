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

### Verse 1 (Markende Puran 0.2701)
- **Original**: नमस्तायँ
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2702)
- **Original**: नपस्तस्यै नमो नमः
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2703)
- **Original**: या देवी सर्वभूतेषु मातृरूपेण संस्थिता। नप्रस्तस्यै
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2704)
- **Original**: नमसास्‍्ये
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2705)
- **Original**: नमस्तस्य जयो नमः । 73
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2706)
- **Original**: या देवी सर्वभूतेषु भ्रान्तिरूपेण संस्थिता। नमस्तस्यै
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2707)
- **Original**: नमस्तस्यें
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2708)
- **Original**: नमस्तस्थै नपो नमः
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2709)
- **Original**: इन्द्रियाणामध्िष्ठात्री भूतानां चाखिलैषु या। भूतेषु सतत तस्बे ध्याप्िदेत्ये नमो नमः
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2710)
- **Original**: बितिरूपेण या कुत्स्रमैतद्‌ व्याप्य म्थिता जगत्‌। नमस्तस्थे
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2711)
- **Original**: उमस्तस्ये
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2712)
- **Original**: नपस्तस्थ नमो चम:
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2713)
- **Original**: क्षया सुरेजेण दिनेषुसेविता। करोतु सवा नः शुभहेतुर्ीश्चरी शुभानि भरव्राण्यभिहन्तु चापदः
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2714)
- **Original**: साप्प्रत॑. चोद्धतदैत्यतापित रस्माभिरीिशा च सुरैन॑म्स्यते। या अर स्पमृता तस्क्षणमेब हन्ति न; सर्वापदों भ्रक्तिविनम्रमूर्तिभिः
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2715)
- **Original**: देवता बोले--
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2716)
- **Original**: देवीको नमस्कार हैं, महादेवी शिवाक्नों सबंदा नमस्कार है। प्रकृति एवं दा 2. चुझ्धवे ज्न्जा चह्णतां देवों ज्रति नये: नतिं कुर्गं इत्य्चव:। यद्‌ था ज्रषमत्येति प्रशन्त:, ठेपां ग्रशतासिति फश्लोबह्ुण्चनान्त ओोध्यपू। पते शान्तमव्यां टीकायां स्पष्टप्‌। 'प्रणता:' इति पाठान्तरमू।
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2717)
- **Original**: श्न्च हु हि. 0-00«4% #0
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2718)
- **Original**: 04) 43 ह औ4
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2719)
- **Original**: - / के 48
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2720)
- **Original**: / 9 /+ /./ 4 /:/:/ 7 +43 1? भद्राकों प्रणाम है। हपलोग निय्मपूर्वक जगंदम्बाकी नपस्कार करते हैं
- **Translation**: 

---

