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

### Verse 1 (Garuda1 0.1321)
- **Original**: ), नगण (
- **Translation**: 

---

### Verse 2 (Garuda1 0.1322)
- **Original**: ।।), नगण (
- **Translation**: 

---

### Verse 3 (Garuda1 0.1323)
- **Original**: ), नगण (।
- **Translation**: 

---

### Verse 4 (Garuda1 0.1324)
- **Original**: ), एक गुरु (5) होता है और पाँच-पाँच, आठ तथा सात वर्णोंपर यति होती है। यह पच्चीस वर्णोंवाले अतिकृति छन्दके अन्तर्गत है। अब छब्बीस वर्णोंवाले उत्कृति वर्गके छन्दको कहा जा रहा है, आप उसे सुनें- जिस छन्दके प्रत्येक चरणमें मगण (555), मगण (555), तगण (55
- **Translation**: 

---

### Verse 5 (Garuda1 0.1325)
- **Original**: ), नगण (
- **Translation**: 

---

### Verse 6 (Garuda1 0.1326)
- **Original**: ।।), नगण (
- **Translation**: 

---

### Verse 7 (Garuda1 0.1327)
- **Original**: ), नगाण (
- **Translation**: 

---

### Verse 8 (Garuda1 0.1328)
- **Original**: ), रगण (5।5) तथा सगण (
- **Translation**: 

---

### Verse 9 (Garuda1 0.1329)
- **Original**: ।5) हों और आठ, ग्यारह एवं सात वर्णोंपर यति होती है, उसे भुजड्भविजृम्भित कहते हैं। यह छब्बीस वर्णवाले उत्कृति छन्‍्द-वर्गका एक भेद है। जिस छन्‍्दके प्रत्येक चरणमें एक मगण (555), छः: नगण (
- **Translation**: 

---

### Verse 10 (Garuda1 0.1330)
- **Original**: ), एक सगण (
- **Translation**: 

---

### Verse 11 (Garuda1 0.1331)
- **Original**: ।5) और दो गुरु (55) हों, साथ ही नौ, छ:-छ: तथा पाँच वर्णोंपर यति हो तो उसको अपहाब कहते हैं। यह उत्कृति वर्गका हो दूसरा भेद है। जिसके फ्रत्येक चरणमें दो नगण (
- **Translation**: 

---

### Verse 12 (Garuda1 0.1332)
- **Original**: ) और सात साण (55, 55, 55, $।5, 5।5, 5।5, 5।5) हों तो उसका नाम चण्डवृत्तिप्रपात छन्द है। उसे दण्डक' भी कहा जाता है। यदि इस छन्दमें दो नगणकों छोड़कर शेष रगण वर्णोंके साथ क्रमशः एक और दो अन्य रगण पदोँकी वृद्धि हो तो उसीसे व्याल और जीमूत आदि नामवाले दण्डक छन्द बनते हैं। (अध्याय 209) >>ाऊशग्कमक छन्द-विधान ( अर्द्धसमवृत्त लक्षण ) श्रीसूतजीने कहा--यदि छनन्‍्दके विषमपादमें तीन सगण (
- **Translation**: 

---

### Verse 13 (Garuda1 0.1333)
- **Original**: । 5), एक लघु (।) और एक गुरु (5) वर्ण-- इस प्रकार ग्यारह अक्षर हों एवं समपादमें तीन भगण (5
- **Translation**: 

---

### Verse 14 (Garuda1 0.1334)
- **Original**: ) और दो गुरु (55) हों तो ठसे उपचित्रक कहते हैं। जिस छन्‍्दके विषमपादमें तीन भगण (5
- **Translation**: 

---

### Verse 15 (Garuda1 0.1335)
- **Original**: ।), दो गुरु (55) हों और उसके समपादमें एक नगण (
- **Translation**: 

---

### Verse 16 (Garuda1 0.1336)
- **Original**: ।), दो जगण (।5।) और एक यगण (। 55) हो, उसे द्रुतमध्या नामक छन्‍्द माना गया है। जिस छन्दके विषम-पादमें तीन सगण (।। 5), एक गुरु और समपादमें तीन भगण (5
- **Translation**: 

---

### Verse 17 (Garuda1 0.1337)
- **Original**: ।) छन्दके विषमपादमें एक तगण (55
- **Translation**: 

---

### Verse 18 (Garuda1 0.1338)
- **Original**: ), एक जगण (।5। ), एक रगण (5।5), एक गुरु (5), हो और समपादमें एक मगण (555), एक सगण (
- **Translation**: 

---

### Verse 19 (Garuda1 0.1339)
- **Original**: ।5), एक जगण (।5।) तथा दो गुरु (55)हों, वह भद्रविऱाद्‌ नामक छन्द होता है। यदि विषमपादमें सगण (।
- **Translation**: 

---

### Verse 20 (Garuda1 0.1340)
- **Original**: 5), जगण (
- **Translation**: 

---

