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

### Verse 1 (Mahabharat 0.4771)
- **Original**: हो गया तो उसका वध करनेके लिये मैंने तुम्हारा ही स्मरण समान था। ऐसे महाबली कर्णको तुम दोनोंने युद्धमें मार
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4771)
- **Original**: हो गया तो उसका वध करनेके लिये मैंने तुम्हारा ही स्मरण समान था। ऐसे महाबली कर्णको तुम दोनोंने युद्धमें मार
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4772)
- **Original**: किया था, इस समय कर्णका वध करके तुपने मेरे उस डाला--यह बड़े आनन्दकी बात हुई। भैया श्रीकृष्ण और
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4772)
- **Original**: किया था, इस समय कर्णका वध करके तुपने मेरे उस डाला--यह बड़े आनन्दकी बात हुई। भैया श्रीकृष्ण और
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4773)
- **Original**: स्मरणकों सफल बना दिया न ? बताओ तो सूतपुत्रको तुमने अर्जुन ! आज कर्णने मेरे साथ भयंकर युद्ध किया था। उसने
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4773)
- **Original**: स्मरणकों सफल बना दिया न ? बताओ तो सूतपुत्रको तुमने अर्जुन ! आज कर्णने मेरे साथ भयंकर युद्ध किया था। उसने
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4774)
- **Original**: किस तरह मारा ?' आग
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4774)
- **Original**: किस तरह मारा ?' आग
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4775)
- **Original**: कर्णपर्व ] युपिश्िसका अर्जुसकों धिक्कारता, युधिष्ठिकके वधके लिये उद्चत हुए अर्जुनकों भगवानड्ाग उपदेश 1 49 अर्जुनकी बातसे कर्णके जीवित रहनेका पता पाकर युधिष्टिरका उन्हें धिक्कारना तथा युथ्चिष्टिका वध करनेके लिये उद्यत हुए अर्जुनको भगवानद्वारा धर्मका तत्त्व समझाया जाना सजय कहते हैं--महाराज ! धर्मात्मा राजा युश्रिष्ठिककी
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4775)
- **Original**: कर्णपर्व ] युपिश्िसका अर्जुसकों धिक्कारता, युधिष्ठिकके वधके लिये उद्चत हुए अर्जुनकों भगवानड्ाग उपदेश 1 49 अर्जुनकी बातसे कर्णके जीवित रहनेका पता पाकर युधिष्टिरका उन्हें धिक्कारना तथा युथ्चिष्टिका वध करनेके लिये उद्यत हुए अर्जुनको भगवानद्वारा धर्मका तत्त्व समझाया जाना सजय कहते हैं--महाराज ! धर्मात्मा राजा युश्रिष्ठिककी
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4776)
- **Original**: यह बात सुनकर अतिरथी वीर अजुन इस प्रकार
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4776)
- **Original**: यह बात सुनकर अतिरथी वीर अजुन इस प्रकार
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4777)
- **Original**: बोले--“राजन्‌ ! आज जब मैं संशमकोंके साथ युद्ध कर रहा
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4777)
- **Original**: बोले--“राजन्‌ ! आज जब मैं संशमकोंके साथ युद्ध कर रहा
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4778)
- **Original**: था, उस समय अश्वत्थामा बाणोंकी वर्षा करता हुआ सहसा
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4778)
- **Original**: था, उस समय अश्वत्थामा बाणोंकी वर्षा करता हुआ सहसा
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4779)
- **Original**: मेरे सामने आ धमका। मेरा रथ देखते ही उसकी सारी
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4779)
- **Original**: मेरे सामने आ धमका। मेरा रथ देखते ही उसकी सारी
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4780)
- **Original**: सेना मेरे साथ युद्ध करनेके लिये खड़ी हो गयी। तब मैं उस
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4780)
- **Original**: सेना मेरे साथ युद्ध करनेके लिये खड़ी हो गयी। तब मैं उस
- **Translation**: 

---

