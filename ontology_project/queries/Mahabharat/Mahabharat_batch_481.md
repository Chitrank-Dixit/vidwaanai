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

### Verse 1 (Mahabharat 0.4801)
- **Original**: “भगवन्‌ ! मैंने जिदमें आकर भाईका अपमानरूप महान्‌ छूटकर प्रसन्नतापूर्वक सूतपुत्र कर्णका वध करना।
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4801)
- **Original**: “भगवन्‌ ! मैंने जिदमें आकर भाईका अपमानरूप महान्‌ छूटकर प्रसन्नतापूर्वक सूतपुत्र कर्णका वध करना।
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4802)
- **Original**: पाप कर डाल्म है, इसलिये अब अपने इस झरीरको ही नए अपने सखा भगवान्‌ श्रीकृष्मका वह बचन सुनकर
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4802)
- **Original**: पाप कर डाल्म है, इसलिये अब अपने इस झरीरको ही नए अपने सखा भगवान्‌ श्रीकृष्मका वह बचन सुनकर
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4803)
- **Original**: कर डालूँगा।' अर्जुनकी बात सुनकर भगवानते अ्जुनने उसकी बड़ी प्रशंसा की, फिर ये हठपूर्वक धर्मराजके
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4803)
- **Original**: कर डालूँगा।' अर्जुनकी बात सुनकर भगवानते अ्जुनने उसकी बड़ी प्रशंसा की, फिर ये हठपूर्वक धर्मराजके
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4804)
- **Original**: कहा--'पार्थ ! राजा युथिप्निस्कों 'तू' मात्र कहकर तुम प्रति ऐसे कटुवचन कहने लगे, जैसे पहले कभी नहीं कहे थे।
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4804)
- **Original**: कहा--'पार्थ ! राजा युथिप्निस्कों 'तू' मात्र कहकर तुम प्रति ऐसे कटुवचन कहने लगे, जैसे पहले कभी नहीं कहे थे।
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4805)
- **Original**: इतने घोर दुःख क्‍यों डूब गये? उफ ! इसीके हछियें वें बोले--'तू चुप रह, न जोल, तू तो खुद ही लड़ाईसे
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4805)
- **Original**: इतने घोर दुःख क्‍यों डूब गये? उफ ! इसीके हछियें वें बोले--'तू चुप रह, न जोल, तू तो खुद ही लड़ाईसे
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4806)
- **Original**: आत्पघात करना चाहते हों ? अर्जुन ! श्रेष्ठ पुरुषोने कभी ऐसा काम नहीं किया है। धर्मका स्वरूप सूक्ष्म है और उसका समझना कठिन। अज्ञानियोंके लिये तो और भी मुश्किल है। यहाँ जो कर्तव्य है, उसे मैं बताता हूँ, सुतरो
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4806)
- **Original**: आत्पघात करना चाहते हों ? अर्जुन ! श्रेष्ठ पुरुषोने कभी ऐसा काम नहीं किया है। धर्मका स्वरूप सूक्ष्म है और उसका समझना कठिन। अज्ञानियोंके लिये तो और भी मुश्किल है। यहाँ जो कर्तव्य है, उसे मैं बताता हूँ, सुतरो
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4807)
- **Original**: भाईका वध करनेसे जिस नरककी प्राप्ति होती है, उससे भी भयानक नस्क तुम्हें आत्मघात कस्तेसे मिलेगा। इसलिये
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4807)
- **Original**: भाईका वध करनेसे जिस नरककी प्राप्ति होती है, उससे भी भयानक नस्क तुम्हें आत्मघात कस्तेसे मिलेगा। इसलिये
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4808)
- **Original**: अब अपने ही मुँहसे अपने गुणोंका बखान करे, ऐसा
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4808)
- **Original**: अब अपने ही मुँहसे अपने गुणोंका बखान करे, ऐसा
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4809)
- **Original**: करनेसे यही समझा 'जायगा कि तुमने अपने ही हाथों
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4809)
- **Original**: करनेसे यही समझा 'जायगा कि तुमने अपने ही हाथों
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4810)
- **Original**: अपनेको मार छिया।' यह सुनकर अर्जुनने श्रीकृष्णकी बातोंका अभिनन्‍दन
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4810)
- **Original**: अपनेको मार छिया।' यह सुनकर अर्जुनने श्रीकृष्णकी बातोंका अभिनन्‍दन
- **Translation**: 

---

