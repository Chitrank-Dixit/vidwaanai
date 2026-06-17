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

### Verse 1 (Markende Puran 0.2721)
- **Original**: रैद्राकों नमस्कार हैं। नित्या, गौरी एवं धात्रीको ब्ारंबार नमस्कार हैं। ज्योत््ामयी, चन्द्ररूपिणी एवं सुखस्वरूपा देवीकों सतत्त प्रणाम हैं
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2722)
- **Original**: शरणागतोंका कल्याण करनेवालों वृद्धि एवं सिद्धिरूप। देवीकों हम बारंबार नमस्कार करते हैं। नैऱ्ती (राक्षसॉंकी लक्ष्मी), राजाओंकी लक्ष्मी तथा शर्नाणी (शिवपत्नी ) -स्वरृपा आप जगदम्ब्राकों बार-बार नमस्कार है
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2723)
- **Original**: दुर्गा, दुर्गपारा (दुर्गम संकटसे पार उतारनेत्रालो), सारा (सबकी सारभूता), सर्वकारिंणी, ख्याति, कृष्णा और पधृश्नादेवीको सवंदा नमस्कार है
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2724)
- **Original**: अत्यन्त सौम्य तथा अत्यन्त रौंद्ररूपा देवीको हम नमस्कार करते हैं, उन्हें हपारा बारंबार प्रणाम है
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2725)
- **Original**: जगत्‌की आधारपूता कृति देवीको बारंभ्ार नमस्कार है
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2726)
- **Original**: जो देवी ; सब प्राणियोंमें विष्णुमायाके नामसे कहां जाती हैं, डनको नमस्कार, ठनकों नमस्कार, उनको बारंबार नमस्कार है
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2727)
- **Original**: 14--16
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2728)
- **Original**: जो देवी सब प्राणियोंमें चेतना कहलाती हैं, ठनकों नमस्कार, उतकों नमस्कार, उनकों बारंबार नमस्कार है
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2729)
- **Original**: 17--19
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2730)
- **Original**: जो देवों सत्र प्राणियोंमें ्रुद्धिरूपसे स्थित हैं, उनको नमस्कार, उनकों नमस्कार, उनको बार॑बार नमस्कार है
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2731)
- **Original**: 20--22
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2732)
- **Original**: जे देवी सब प्राणियोंमें निद्रारूपसे स्थित हैं, उनको उमस्कार, उनक्तों, नमस्कार, उनक्ों बारंबर नमस्कार है
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2733)
- **Original**: जो देवीं सब प्राणियोंमें भ्षुधारूपसे स्थित हैं, उनको नमस्कार, उनको नमस्कार, उनको बारंबार नमस्कार है
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2734)
- **Original**: 26--28
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2735)
- **Original**: जो देवीं सब प्राणियॉंमें छाथारूपसे स्थित हैं, ठनको नमस्कार, उनको नमस्कार, उनको बारंबार नमस्कार हैं
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2736)
- **Original**: 29--315
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2737)
- **Original**: देवी सब प्राणियोंमें मातारूपसे स्थित हैं, उनको जो देवी सब प्राणियोंमें शक्तिरूपसो स्थित हैं, उनको नमस्कार, उतक्तों सपस्कार, उनको बारंबार संक्षिप्त पाकंण्डेयपुराण पुराण + नमस्कार है
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2738)
- **Original**: जो देवी सब प्राणियोंमें तुष्णारूपसे स्थित हैं, ठनंको नमस्कारं, उनको नमस्कार, उनको बारंबार नमस्कार है
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2739)
- **Original**: 35--37
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2740)
- **Original**: जो देवी सब प्राणियॉमें क्षान्ति (क्षेमा)-रूपसे स्थित हैं, ठतकों नमस्कार, उनकों नमस्कार, उनको बारंबांर नमस्कार हैं
- **Translation**: 

---

