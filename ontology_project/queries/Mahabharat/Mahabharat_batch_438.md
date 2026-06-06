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

### Verse 1 (Mahabharat 0.4371)
- **Original**: . डुरयोधनकी यह बात सुनकर झल्य एकदम क्रोधमें भर
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4371)
- **Original**: . डुरयोधनकी यह बात सुनकर झल्य एकदम क्रोधमें भर
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4372)
- **Original**: गये। उनकी भौंहोंमें बल पड़ गये तथा हाथ बार-बार काँपने लूगे। उन्हें अपने कुछ, ऐश्वर्य, विद्या और बलका बड़ा गर्व
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4372)
- **Original**: गये। उनकी भौंहोंमें बल पड़ गये तथा हाथ बार-बार काँपने लूगे। उन्हें अपने कुछ, ऐश्वर्य, विद्या और बलका बड़ा गर्व
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4373)
- **Original**: था। इसलिये उन्होंने क्रोधसे आँखें लाल कस्के कहा,
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4373)
- **Original**: था। इसलिये उन्होंने क्रोधसे आँखें लाल कस्के कहा,
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4374)
- **Original**: 'दुरबोधन ! अवश्य ही तुम या तो मेरा अपमान कर रहें हो
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4374)
- **Original**: 'दुरबोधन ! अवश्य ही तुम या तो मेरा अपमान कर रहें हो
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4375)
- **Original**: था तुरहें मेरे प्रति संदेह है। इसीसे तुप्त मुझे सारथिका काम ।
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4375)
- **Original**: था तुरहें मेरे प्रति संदेह है। इसीसे तुप्त मुझे सारथिका काम ।
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4376)
- **Original**: करनेकी आजा दे रहे हो। तुम कर्णको हपारी अपेक्षा भी श्रेष्ठ समझकर उसकी प्रजलसा करते हो। किंतु मैं उसे 4
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4376)
- **Original**: करनेकी आजा दे रहे हो। तुम कर्णको हपारी अपेक्षा भी श्रेष्ठ समझकर उसकी प्रजलसा करते हो। किंतु मैं उसे 4
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4377)
- **Original**: संज्रापमें अपने समान नहीं समझता। तुय जो बड़े-से-बड़ हि प्र बीर हो, ख्से मेरे हिस्सेमें कर दो; मैं उसे संग्रापमें जीतकर च्न्स््
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4377)
- **Original**: संज्रापमें अपने समान नहीं समझता। तुय जो बड़े-से-बड़ हि प्र बीर हो, ख्से मेरे हिस्सेमें कर दो; मैं उसे संग्रापमें जीतकर च्न्स््
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4378)
- **Original**: अपने घर चला जाऊँगा। अथवा आज मैं अकेल्ता हों युद्ध ड्रंउचे श्लिज््ट2ग «>>य्ती
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4378)
- **Original**: अपने घर चला जाऊँगा। अथवा आज मैं अकेल्ता हों युद्ध ड्रंउचे श्लिज््ट2ग «>>य्ती
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4379)
- **Original**: करूँगा। तब तुम झत्नुओंका संहार करते समय मेरा पराक्रम :.
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4379)
- **Original**: करूँगा। तब तुम झत्नुओंका संहार करते समय मेरा पराक्रम :.
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4380)
- **Original**: पलक थ्च््य्य्न्
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4380)
- **Original**: पलक थ्च््य्य्न्
- **Translation**: 

---

