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

### Verse 1 (Mahabharat 0.4271)
- **Original**: ... सज़यने कहा--महाराज ! आप जिन्हें श्रेष्ठ पहारथी मानते
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4271)
- **Original**: ... सज़यने कहा--महाराज ! आप जिन्हें श्रेष्ठ पहारथी मानते
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4272)
- **Original**: है, व्य सबको राजा पाण्ड्य अपने पराक्रमके सामने तुच्छ गिनते
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4272)
- **Original**: है, व्य सबको राजा पाण्ड्य अपने पराक्रमके सामने तुच्छ गिनते
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4273)
- **Original**: थे। अपने साथ भीष्य और ग्रेणकी समानता बतस्प्रना भी उन्‍हें बीचमें उप्रायुधके पुत्रने तीन बाणोंसे अर्जुनको बींघ
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4273)
- **Original**: थे। अपने साथ भीष्य और ग्रेणकी समानता बतस्प्रना भी उन्‍हें बीचमें उप्रायुधके पुत्रने तीन बाणोंसे अर्जुनको बींघ
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4274)
- **Original**: बरदाइत नहीं होता था। श्रीकृष्ण और अर्जुनसे किसी भी बातमें दिया। यह देख अर्जुनने उसका सिर धड़से अलग कर दिया।
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4274)
- **Original**: बरदाइत नहीं होता था। श्रीकृष्ण और अर्जुनसे किसी भी बातमें दिया। यह देख अर्जुनने उसका सिर धड़से अलग कर दिया।
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4275)
- **Original**: वें अपनेको कम नहीं समझते थे। इस प्रकार पाण्डय समस्त उस समय उस्रायुधके समस्त सैनिक क्रोधमें भरकर अर्जुन-
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4275)
- **Original**: वें अपनेको कम नहीं समझते थे। इस प्रकार पाण्डय समस्त उस समय उस्रायुधके समस्त सैनिक क्रोधमें भरकर अर्जुन-
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4276)
- **Original**: राजाओं तथा सम्पूर्ण अखधारियोंमें श्रेष्ठ थे । वे कर्णकी सेनाका पर नाना प्रकारके अख-झख्नोंकी वर्षा करने लगे।
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4276)
- **Original**: राजाओं तथा सम्पूर्ण अखधारियोंमें श्रेष्ठ थे । वे कर्णकी सेनाका पर नाना प्रकारके अख-झख्नोंकी वर्षा करने लगे।
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4277)
- **Original**: संहार कर रहे थे। उन्होंने सम्पूर्ण योद्धाओंको छिन्न-घिन्न कर परंतु अजुँनने अपने अखोंसे झन्रुओंकी अख्वर्षा रोक
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4277)
- **Original**: संहार कर रहे थे। उन्होंने सम्पूर्ण योद्धाओंको छिन्न-घिन्न कर परंतु अजुँनने अपने अखोंसे झन्रुओंकी अख्वर्षा रोक
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4278)
- **Original**: दिया, हाथियों और उनके सवारोंको पताका, ध्वजा और दी और सायकॉकी झड़ी लगाकर बहुतों-से झन्रुओंका वध
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4278)
- **Original**: दिया, हाथियों और उनके सवारोंको पताका, ध्वजा और दी और सायकॉकी झड़ी लगाकर बहुतों-से झन्रुओंका वध
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4279)
- **Original**: अखोंसे होन करके पादरक्षकोंसहित मार डाल्ला। पुलिन्द, कर डाला ।
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4279)
- **Original**: अखोंसे होन करके पादरक्षकोंसहित मार डाल्ला। पुलिन्द, कर डाला ।
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4280)
- **Original**: खस, बाद्लीक, निषाद, आन्ध्र, कुत्तल, दाक्षिणात्य और
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4280)
- **Original**: खस, बाद्लीक, निषाद, आन्ध्र, कुत्तल, दाक्षिणात्य और
- **Translation**: 

---

