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

### Verse 1 (Agni Puran 0.6301)
- **Original**: दो सगण हों और शेष चरण ज्यों-के-त्यों रहें लबली' छन्द होता है और जब प्रथम पादके
- **Translation**: 

---

### Verse 2 (Agni Puran 0.6302)
- **Original**: तो उसकी “ललित'' संज्ञा होती है। जिसके स्थानमें चतुर्थ पाद और चतुर्थ पादके स्थानमें
- **Translation**: 

---

### Verse 3 (Agni Puran 0.6303)
- **Original**: प्रथम चरणमें यगण, सगण, जगण, भगण और 1. तस्या: कराक्षविक्षेप: रुक्षकद्ट इसमें शुरु-लथुका विभाग नहीं होता। 2. कुसुमितसहकारे 3. चित्त मम रमयति, कारक वतमिदमुपगिरिनदि। कूृजतधुकरकसरथकृतजनधूति, 4. जनयति महतों प्रीतिं हृदये, कामिनां चूतमझरों। कम्पिततनुकुटिलैरतिदीर्थ: क्षतचैतन्य:, पदचतुरूध्य॑ न चलति पुरुष: पतति सहसैय # विकसितकमलसरसि मधुसमये5 स्मिन्‌, प्रवसससि पचिकहतक यदि भवाति तव विफत्ति:
- **Translation**: 

---

### Verse 4 (Agni Puran 0.6304)
- **Original**: + अध्याय 333 * 685 4 ##%##ऋऋकऋकक कक कक कब क तर अं कक करू छ कक छ छ 8&>&#ऋऊऊ ##%ऋछऊऋ 7447» कक के कक कफ कफ ऋ कक ऋ कक क क अत तक ते तक रू रु रूढ कक र ढ ढक छ कब दो गुरु (अठारह अक्षर) हों, द्वितीय चरणमें
- **Translation**: 

---

### Verse 5 (Agni Puran 0.6305)
- **Original**: क्रमशः दो नगण, एक सगण, फिर दो नगण सगण, नगण, जगण, रगण और एक गुरु (तेरह
- **Translation**: 

---

### Verse 6 (Agni Puran 0.6306)
- **Original**: और एक सगण (अठारह अक्षर) हों तो बह अक्षर) हों, तृतीय चरणमें दो नगण और एक
- **Translation**: 

---

### Verse 7 (Agni Puran 0.6307)
- **Original**: “वर्धमान'' छन्‍्द नाम धारण करता है। उसी सगण (नौ अक्षर) हों तथा चतुर्थ चरणमें तीन
- **Translation**: 

---

### Verse 8 (Agni Puran 0.6308)
- **Original**: छन्दमें तृतीय चरणके स्थानमें जब तगण, जगण नगण, एक जगण और एक भगण (पंद्रह
- **Translation**: 

---

### Verse 9 (Agni Puran 0.6309)
- **Original**: और रगण (ये नौ अक्षर) हों तो वह 'शुद्ध अक्षर) हों, वह उपस्थित “प्रचुपित'' नामक
- **Translation**: 

---

### Verse 10 (Agni Puran 0.6310)
- **Original**: विराषभ” छन्द कहलाता है। अब अर्धसमवृत्तका छन्द होता है। उक्त उन्द्रके तृतीय चरणमें जब
- **Translation**: 

---

### Verse 11 (Agni Puran 0.6311)
- **Original**: वर्णन करूँगा
- **Translation**: 

---

### Verse 12 (Agni Puran 0.6312)
- **Original**: इस प्रकार आदि आग्रेय महापुराणमें 'विफ्मवृत्तका वर्णन” नागक तीन साँ बत्तीसवाँ अध्याय पूरा हुआ# 3320 3 तीन सौ तैंतीसवाँ अध्याय अर्धसमवृत्तोंका वर्णन अग्निदेव कहते हैं--जिसके प्रथम चरणमें
- **Translation**: 

---

### Verse 13 (Agni Puran 0.6313)
- **Original**: है।] जिसके प्रथम चरणमें तीन सगण और एक तीन सगण, एक लघु और एक गुरु (कुल ग्यारह
- **Translation**: 

---

### Verse 14 (Agni Puran 0.6314)
- **Original**: गुरु तथा द्वितीय चरणमें तीन भगण एवं दो गुरु अक्षर) हों, दूसरे चरणमें तीन भगण एवं दो गुरु
- **Translation**: 

---

### Verse 15 (Agni Puran 0.6315)
- **Original**: हों, उस छन्दका नाम “वेगवती" है। जिसके हों तथा पूर्वार्धक समान ही उत्तरार्ध भी हो, वह
- **Translation**: 

---

### Verse 16 (Agni Puran 0.6316)
- **Original**: पहले पादमें तगण (55 ।), जगण (।5।), रगण “उपचित्रक " नामक छन्द है। जिसके प्रथम पादमें
- **Translation**: 

---

### Verse 17 (Agni Puran 0.6317)
- **Original**: (5।5) और एक गुरु तथा दूसरे चरणमें मगण तीन भगण एवं दो गुरु हों और द्वितीय पादमें
- **Translation**: 

---

### Verse 18 (Agni Puran 0.6318)
- **Original**: (555), सगण (
- **Translation**: 

---

### Verse 19 (Agni Puran 0.6319)
- **Original**: 5), जगण (
- **Translation**: 

---

### Verse 20 (Agni Puran 0.6320)
- **Original**: 5।) एवं दो एक नगण (
- **Translation**: 

---

