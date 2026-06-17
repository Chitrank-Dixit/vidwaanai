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

### Verse 1 (Mahabharat 0.3161)
- **Original**: उपदेशको तूने एकाग्र चित्तसे भ्रवण किया ? और धनक्षय !
- **Translation**: 

---

### Verse 2 (Mahabharat 0.3161)
- **Original**: उपदेशको तूने एकाग्र चित्तसे भ्रवण किया ? और धनक्षय !
- **Translation**: 

---

### Verse 3 (Mahabharat 0.3162)
- **Original**: 6, 4 हल बट जया तेरा अज्ञानजनित मोह नष्ट हो गया ?
- **Translation**: 

---

### Verse 4 (Mahabharat 0.3162)
- **Original**: 6, 4 हल बट जया तेरा अज्ञानजनित मोह नष्ट हो गया ?
- **Translation**: 

---

### Verse 5 (Mahabharat 0.3163)
- **Original**: 67--72
- **Translation**: 

---

### Verse 6 (Mahabharat 0.3163)
- **Original**: 67--72
- **Translation**: 

---

### Verse 7 (Mahabharat 0.3164)
- **Original**: 343232220222000 अर्जु बोले--अच्युत ! आपकी कृपासे पैरा मोह नष्ट हो (7 88% ड- गया और मैंने स्मृति प्राप्त कर ल्‍ही है; अब मैं संझायरहित होकर स्थित हूँ, अत: आपकी आज्ञाका पालन करूँगा
- **Translation**: 

---

### Verse 8 (Mahabharat 0.3164)
- **Original**: 343232220222000 अर्जु बोले--अच्युत ! आपकी कृपासे पैरा मोह नष्ट हो (7 88% ड- गया और मैंने स्मृति प्राप्त कर ल्‍ही है; अब मैं संझायरहित होकर स्थित हूँ, अत: आपकी आज्ञाका पालन करूँगा
- **Translation**: 

---

### Verse 9 (Mahabharat 0.3165)
- **Original**: सज्य ओले--इस प्रकार मैंने शरवासुदेवके और महात्पा अजुनके इस अद्भुत रहस्ययुक्त, रोमाज्लकारक संवादकों सुनो। श्रीव्यासजीकी कृपासे दिव्य दृष्टि पाकर मैंने इस परम 9) गोपनीय योगको अर्जुनके प्रति कहते हुए स्वयं योगेश्वर
- **Translation**: 

---

### Verse 10 (Mahabharat 0.3165)
- **Original**: सज्य ओले--इस प्रकार मैंने शरवासुदेवके और महात्पा अजुनके इस अद्भुत रहस्ययुक्त, रोमाज्लकारक संवादकों सुनो। श्रीव्यासजीकी कृपासे दिव्य दृष्टि पाकर मैंने इस परम 9) गोपनीय योगको अर्जुनके प्रति कहते हुए स्वयं योगेश्वर
- **Translation**: 

---

### Verse 11 (Mahabharat 0.3166)
- **Original**: भी पुनः-पुनः स्परण करके मेरे चित्तमें महान्‌ आश्चर्य होता भगवान्‌ श्रीकृष्णसे प्रत्यक्ष सुना हैं। राजन्‌! भगवान्‌
- **Translation**: 

---

### Verse 12 (Mahabharat 0.3166)
- **Original**: भी पुनः-पुनः स्परण करके मेरे चित्तमें महान्‌ आश्चर्य होता भगवान्‌ श्रीकृष्णसे प्रत्यक्ष सुना हैं। राजन्‌! भगवान्‌
- **Translation**: 

---

### Verse 13 (Mahabharat 0.3167)
- **Original**: है और मैं बारम्बार हर्षित हो रहा हूँ। राजन! जहाँ श्रीकृष्ण और अर्जुनके इस रहस्ययुक्त, कल्याणकारक और
- **Translation**: 

---

### Verse 14 (Mahabharat 0.3167)
- **Original**: है और मैं बारम्बार हर्षित हो रहा हूँ। राजन! जहाँ श्रीकृष्ण और अर्जुनके इस रहस्ययुक्त, कल्याणकारक और
- **Translation**: 

---

### Verse 15 (Mahabharat 0.3168)
- **Original**: योगेश्वर श्रीकृष्ण भगवान्‌ हैं और जहाँ गाण्डीव धनुषधारी अदूधुत संवादको पुन:-पुनः स्मरण करके मैं बारप्यार हर्षित
- **Translation**: 

---

### Verse 16 (Mahabharat 0.3168)
- **Original**: योगेश्वर श्रीकृष्ण भगवान्‌ हैं और जहाँ गाण्डीव धनुषधारी अदूधुत संवादको पुन:-पुनः स्मरण करके मैं बारप्यार हर्षित
- **Translation**: 

---

### Verse 17 (Mahabharat 0.3169)
- **Original**: अर्जुन हैं, वहींपर श्री, विजय, विभूति और अचल नीति है-- हो रहा' हैँ।"राजन्‌ ! श्रीहरिके उस अत्यन्त विलक्षण रूपको
- **Translation**: 

---

### Verse 18 (Mahabharat 0.3169)
- **Original**: अर्जुन हैं, वहींपर श्री, विजय, विभूति और अचल नीति है-- हो रहा' हैँ।"राजन्‌ ! श्रीहरिके उस अत्यन्त विलक्षण रूपको
- **Translation**: 

---

### Verse 19 (Mahabharat 0.3170)
- **Original**: ऐसा मेरा मत है
- **Translation**: 

---

### Verse 20 (Mahabharat 0.3170)
- **Original**: ऐसा मेरा मत है
- **Translation**: 

---

