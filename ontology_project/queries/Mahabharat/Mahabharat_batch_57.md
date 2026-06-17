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

### Verse 1 (Mahabharat 0.561)
- **Original**: जिस समय देवाथिदेव महादेव तुमपर प्रसन्न होंगे, है। उन्होंने मय दानवको मार डालनेके लिये चक्र उठाया।
- **Translation**: 

---

### Verse 2 (Mahabharat 0.561)
- **Original**: जिस समय देवाथिदेव महादेव तुमपर प्रसन्न होंगे, है। उन्होंने मय दानवको मार डालनेके लिये चक्र उठाया।
- **Translation**: 

---

### Verse 3 (Mahabharat 0.562)
- **Original**: उस समय तुम्हारे तपके प्रभावसे मैं तुप्हें अपने सारे अख् दे आगे चक्र और पीछे धधकती आगको देखकर पहले तो मय
- **Translation**: 

---

### Verse 4 (Mahabharat 0.562)
- **Original**: उस समय तुम्हारे तपके प्रभावसे मैं तुप्हें अपने सारे अख् दे आगे चक्र और पीछे धधकती आगको देखकर पहले तो मय
- **Translation**: 

---

### Verse 5 (Mahabharat 0.563)
- **Original**: दूँगा। मैं जानता हूँ कि वह समय कब आयेगा।' भगवान्‌ दानव किंकर्त॑व्यविमूढ हो गया, पीछे उसने कुछ सोचकर
- **Translation**: 

---

### Verse 6 (Mahabharat 0.563)
- **Original**: दूँगा। मैं जानता हूँ कि वह समय कब आयेगा।' भगवान्‌ दानव किंकर्त॑व्यविमूढ हो गया, पीछे उसने कुछ सोचकर
- **Translation**: 

---

### Verse 7 (Mahabharat 0.564)
- **Original**: अ्रीकृष्णने कहा, 'देवराज ! आप मुझे यह वर दीजिये कि पुकारा--'वीर अजुन ! मैं तुम्हारी शरणमें हूँ। केवल तुष्हीं
- **Translation**: 

---

### Verse 8 (Mahabharat 0.564)
- **Original**: अ्रीकृष्णने कहा, 'देवराज ! आप मुझे यह वर दीजिये कि पुकारा--'वीर अजुन ! मैं तुम्हारी शरणमें हूँ। केवल तुष्हीं
- **Translation**: 

---

### Verse 9 (Mahabharat 0.565)
- **Original**: मेरी और अर्जुनकी मित्रता क्षण-क्षण बढ़ती जाय और कभी मेरी रक्षां कर सकते हो।' अर्जुनने कहा, 'डरो मत।'
- **Translation**: 

---

### Verse 10 (Mahabharat 0.565)
- **Original**: मेरी और अर्जुनकी मित्रता क्षण-क्षण बढ़ती जाय और कभी मेरी रक्षां कर सकते हो।' अर्जुनने कहा, 'डरो मत।'
- **Translation**: 

---

### Verse 11 (Mahabharat 0.566)
- **Original**: न टूटे।' इखले प्रसन्न होकर कहा, 'एवमस्तु'। देवताओंके अ्जुनको अभयदान करते देखकर भगवान्‌ श्रीकृष्णने चक्र
- **Translation**: 

---

### Verse 12 (Mahabharat 0.566)
- **Original**: न टूटे।' इखले प्रसन्न होकर कहा, 'एवमस्तु'। देवताओंके अ्जुनको अभयदान करते देखकर भगवान्‌ श्रीकृष्णने चक्र
- **Translation**: 

---

### Verse 13 (Mahabharat 0.567)
- **Original**: जानेके बाद अग्निदेव श्रीकृष्ण और अर्जुनका अभिनन्दन गेक लिया और अभ्निने भी उसे भर्म नहीं किया। मय
- **Translation**: 

---

### Verse 14 (Mahabharat 0.567)
- **Original**: जानेके बाद अग्निदेव श्रीकृष्ण और अर्जुनका अभिनन्दन गेक लिया और अभ्निने भी उसे भर्म नहीं किया। मय
- **Translation**: 

---

### Verse 15 (Mahabharat 0.568)
- **Original**: करके चले गये। भगवान्‌ श्रीकृष्ण, अर्जुन और मय दानव दानवकी रक्षा हो गयी। वह बन पंद्रह दिनतक जलता रहा।
- **Translation**: 

---

### Verse 16 (Mahabharat 0.568)
- **Original**: करके चले गये। भगवान्‌ श्रीकृष्ण, अर्जुन और मय दानव दानवकी रक्षा हो गयी। वह बन पंद्रह दिनतक जलता रहा।
- **Translation**: 

---

### Verse 17 (Mahabharat 0.569)
- **Original**: यमुनाके पाजन पुलिनपर आकर बैठ गये। >-++<34040+-- आदिपर्व समाप्त
- **Translation**: 

---

### Verse 18 (Mahabharat 0.569)
- **Original**: यमुनाके पाजन पुलिनपर आकर बैठ गये। >-++<34040+-- आदिपर्व समाप्त
- **Translation**: 

---

### Verse 19 (Mahabharat 0.570)
- **Original**: मयासुरकी प्रार्थना-स्वीकृति एवं भगवान्‌ श्रीकृष्णका द्वारका-गमन नारायण समस्कृत्य नें चैव नरोत्मम्‌। देवीं सरखतीं व्यास ततो जयमुदीरयेतू
- **Translation**: 

---

### Verse 20 (Mahabharat 0.570)
- **Original**: मयासुरकी प्रार्थना-स्वीकृति एवं भगवान्‌ श्रीकृष्णका द्वारका-गमन नारायण समस्कृत्य नें चैव नरोत्मम्‌। देवीं सरखतीं व्यास ततो जयमुदीरयेतू
- **Translation**: 

---

