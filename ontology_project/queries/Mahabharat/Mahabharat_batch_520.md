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

### Verse 1 (Mahabharat 0.5191)
- **Original**: तुम रथपर हो और मैं जमीनपर
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5191)
- **Original**: तुम रथपर हो और मैं जमीनपर
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5192)
- **Original**: साथ ही मैं बहुत घबराया हुआ हूँ, इसलिये मेरे ऊपर प्रहार करना उचित नहीं है।' कर्णकी बात सुनकर रथपर बैठे हुए भगवान्‌ श्रीकृष्णने
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5192)
- **Original**: साथ ही मैं बहुत घबराया हुआ हूँ, इसलिये मेरे ऊपर प्रहार करना उचित नहीं है।' कर्णकी बात सुनकर रथपर बैठे हुए भगवान्‌ श्रीकृष्णने
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5193)
- **Original**: उ्ससे कहा--“राधानन्दन ! सौभाग्यकी बात है कि इस समय तुम्हें धर्मकी याद आ रही है। प्रायः ऐसा देखनेमें आता है कि नीच मनुष्य विपत्तिमें फैसनेपर प्रारब्धकी ही
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5193)
- **Original**: उ्ससे कहा--“राधानन्दन ! सौभाग्यकी बात है कि इस समय तुम्हें धर्मकी याद आ रही है। प्रायः ऐसा देखनेमें आता है कि नीच मनुष्य विपत्तिमें फैसनेपर प्रारब्धकी ही
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5194)
- **Original**: किदा करते हैं, अपने किये हुए कुकमॉकी नहीं। कर्ण !
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5194)
- **Original**: किदा करते हैं, अपने किये हुए कुकमॉकी नहीं। कर्ण !
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5195)
- **Original**: पाष्डवोंके बनवासका तेरहवाँ वर्ष बीत जानेपर भी जब तुमने
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5195)
- **Original**: पाष्डवोंके बनवासका तेरहवाँ वर्ष बीत जानेपर भी जब तुमने
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5196)
- **Original**: उनका राज्य नहीं स्मैटाने दिया, उस समय तुम्हारा धर्म कहाँ लिये ठहर जाओ। तुम्हें नीच पुरक्ोंके मार्गपर न्रहीं चलना
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5196)
- **Original**: उनका राज्य नहीं स्मैटाने दिया, उस समय तुम्हारा धर्म कहाँ लिये ठहर जाओ। तुम्हें नीच पुरक्ोंके मार्गपर न्रहीं चलना
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5197)
- **Original**: चत्प् गया था ? तुम्हारी ही सल्मह लेकर जब राजा दुर्धोधनने चाहिये। तुम्हारे लिये तो श्रेष्ठ आचरण ही उचित है। जिसके
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5197)
- **Original**: चत्प् गया था ? तुम्हारी ही सल्मह लेकर जब राजा दुर्धोधनने चाहिये। तुम्हारे लिये तो श्रेष्ठ आचरण ही उचित है। जिसके
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5198)
- **Original**: भीमसेनको जहर मिलाया हुआ भोजन कराया और उल्हें सिस्‍्के बाल बिखर गये हों, जो पीठ दिखाकर भागा जाता
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5198)
- **Original**: भीमसेनको जहर मिलाया हुआ भोजन कराया और उल्हें सिस्‍्के बाल बिखर गये हों, जो पीठ दिखाकर भागा जाता
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5199)
- **Original**: साँपोंसे डैसवाया, उस समय तुम्हारा धर्म कहाँ गया था ? हो, ब्राह्मण हो, हाथ जोड़ रहा हो, झरणमें आया हो और
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5199)
- **Original**: साँपोंसे डैसवाया, उस समय तुम्हारा धर्म कहाँ गया था ? हो, ब्राह्मण हो, हाथ जोड़ रहा हो, झरणमें आया हो और
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5200)
- **Original**: वारणाबत नगरपें ल्क्षाभवनके भीतर सोये हुए पाण्डवोंको रक्षाके लिये प्रार्थना कर रहा हो, जिसने अपने हधियार
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5200)
- **Original**: वारणाबत नगरपें ल्क्षाभवनके भीतर सोये हुए पाण्डवोंको रक्षाके लिये प्रार्थना कर रहा हो, जिसने अपने हधियार
- **Translation**: 

---

