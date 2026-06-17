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

### Verse 1 (Vaivtpuran 28.4206)
- **Original**: यज्जन्म ब्रह्मणो वंशे ज्वलन्तं ब्रत्मयतेजसा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.4207)
- **Original**: यो ध्यायति परं ब्रह्म ब्रह्मवंशं नमाम्यहम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.4208)
- **Original**: (प्रकृतिखण्ड 28
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.4209)
- **Original**: नारदजीने पूछा--मुने! दक्षिणाहीन कर्मके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.4210)
- **Original**: जा रहा था। कुछ कार्यान्तर उपस्थित हो जानेके फलको कौन भोगता है? साथ ही यज्ञपुरुषने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.4211)
- **Original**: कारण तुम भगवान्‌ श्रीकृष्णके दक्षिण कंधेसे भगवती दक्षिणाकी किस प्रकार पूजा की थी;
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.4212)
- **Original**: प्रकट हुई थीं। अतएव तुम्हारा नाम 'दक्षिणा' पड़ यह भी बतलाइये। गया। शोभने! तुम इससे पहले परम शीलवती भगवान्‌ नारायण कहते हैं--मुने ! दक्षिणाहीन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.4213)
- **Original**: होनेके कारण 'सुशीला' कहलाती थीं। तुम ऐसी कर्ममें फल हो कैसे लग सकता है; क्योंकि
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.4214)
- **Original**: सुयोग्या देवी श्रीराधाके शापसे गोलोकसे च्युत फल प्रसव करनेकी योग्यता तो दक्षिणावाले
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.4215)
- **Original**: होकर दक्षिणा नामसे सम्पन्न हो मुझे सौभाग्यवश कर्ममें ही है। मुने! बिना दक्षिणाका कर्म तो
- **Translation**: 

---

### Verse 11 (Vaivtpuran 28.4216)
- **Original**: प्राप्त हुई हो। सुभगे! तुम मुझे अपना स्वामी बलिके पेटमें चला जाता है। पूर्वसमयमें भगवान्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.4217)
- **Original**: बनानेकी कृपा करो! तुम्हीं यज्ञशाली पुरुषोंके वामन बलिके लिये आहाररूपमें इसे अर्पण कर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.4218)
- **Original**: कर्मका फल प्रदान करनेवाली आदरणीया देवी चुके हैं। नारद! अश्रोत्रिय और श्रद्धाहीन व्यक्तिके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.4219)
- **Original**: हो। तुम्हारे बिना सम्पूर्ण प्राणियोंके सभी कर्म द्वारा श्राद्धमें दी हुई वस्तुकों बलि भोजनरूपसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.4220)
- **Original**: निष्फल हो जाते हैं। तुम्हारी अनुपस्थितिमें प्राप्त करते हैं। शूद्रोंसे सम्बन्ध रखनेवाले ब्राह्मणोंके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.4221)
- **Original**: कर्मियोंका कर्म भी शोभा नहीं पाता। ब्रह्मा पूजासम्बन्धी द्रव्य, निषिद्ध एवं आचरणहीन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.4222)
- **Original**: विष्णु, महेश तथा दिक्‍्पाल प्रभृति सभी देवता ब्राह्मणोंद्रारा किया हुआ पूजन तथा गुरुमें भक्ति तुम्हारे न रहनेसे कर्मोंका फल देनेमें असमर्थ न रखनेवाले पुरुषका कर्म-ये सब बलिके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.4223)
- **Original**: रहते हैं। ब्रह्मा स्वयं कर्मरूप हैं। शंकरको आहार हो जाते हैं, इसमें कोई संशय नहीं है।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.4224)
- **Original**: फलरूप बतलाया गया है। मैं विष्णु स्वयं मुने! भगवती दक्षिणाके ध्यान, स्तोत्र और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.4225)
- **Original**: यज्ञरूपसे प्रकट हूँ। इन सबमें साररूपा तुम्हीं हो। पूजाकी विधिके क्रम कण्वशाखामें वर्णित हैं।
- **Translation**: 

---

