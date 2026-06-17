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

### Verse 1 (Vaivtpuran 13.10502)
- **Original**: पुत्र हुए, जो गन्धवोंमें श्रेष्ठ समझे जाते थे। वे सोते और जागते समय दिन-रात श्रीकृष्णके चरणकमलोॉंका ही चिन्तन करते रहते थे। वे सभी दिव्यरूपधारी पार्षद विमानपर बैठे हुए वहाँ आ [ दुर्वासाके शिष्य थे और श्रीकृष्णकी आराधनामें पहुँचे। उन सबके दो भुजाएँ थीं। वे पीताम्बरधारी,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10503)
- **Original**: लगे रहते थे। प्रतिदिन कमल चढ़ाकर श्रीहरिकी किरीट और कुण्डलसे अलंकृत तथा वनमालासे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10504)
- **Original**: पूजा करनेके पश्चात्‌ ही जल पीते थे। उन चारोंके विभूषित थे। उन्होंने विनोदके लिये हाथमें मुरली
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10505)
- **Original**: नाम इस प्रकार हैं--वसुदेव, सुहोत्र, सुदर्शन और ले रखी थी। उनके पैरोंमें मझ्ीरकी मधुर ध्वनि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10506)
- **Original**: सुपार्श्। वे चारों श्रेष्ठ वैष्णण थे और पुष्करमें हो रही थी। उन पार्षदोंके सभी अड्ढग चन्दनसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10507)
- **Original**: तपस्या करते थे। चिरकालतक तपस्या करनेके चर्चित थे। वे गोपवेष धारण किये बड़े सुन्दर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10508)
- **Original**: पश्चात्‌ उन्होंने मन्त्रकों सिद्ध कर लिया था। उन दिखायी देते थे। उनके प्रसन्नमुखपर मन्द हास्यकी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10509)
- **Original**: चारोंमें जो ज्येष्ठ वसुदेव था, वह दुर्वासासे योग्य छटा छा रही थी। वे श्रीकृष्णभक्तोंपर अनुग्रह
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10510)
- **Original**: शिक्षा पाकर योगियोंमें श्रेष्ठ और सिद्ध हो गया। करनेके लिये कातर जान पड़ते थे। रत्नोंके सार-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10511)
- **Original**: उसने विवाह नहीं किया। वह त्रह्मतेजसे प्रज्वलित तत्त्वसे निर्मित दीप्तिशाली दिव्य रथपर आरूढ़
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10512)
- **Original**: हो तत्काल देह त्यागकर श्रीकृष्णका पार्षद हो हो वे भाण्डीरवनमें उस स्थानपर आये, जहाँ
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10513)
- **Original**: गया। एक दिन वे तीनों भाई चित्रसरोवरके तटपर श्रीहरि विराजमान थे। उसी समय दिव्य वस्त्र
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10514)
- **Original**: गये। बे सूर्योदयकालमें श्रीहरिकी पूजाके लिये पहने तथा रत्नमय अलंकारोंसे विभूषित हुए तीन
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10515)
- **Original**: कमल लेना चाहते थे। मुने! कमलोंका संग्रह
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10516)
- **Original**: + भ्रीकृष्णजन्मखण्ड * 479 ऋऋ######## 55% # कर क्र हक /%#%####% 5555 कक ##4###%## 5555 #############%$#%$ कक कक करके जाते हुए उन वैष्णवॉको जब भगवान्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10517)
- **Original**: उनके कहाँ देह और कहाँ रूप? भक्तोंपर अनुग्रह शंकरके सेवकोंने देखा, तब वे सब उन्हें बाँधकर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10518)
- **Original**: करनेके लिये ही भगवान्‌ शरीर धारण करते हैं। अपने साथ ले गये। शंकरके सेवक शरीरसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10519)
- **Original**: रूप-भेद मायासे ही प्रतीत होता है। प्रभो! आप बलिष्ठ थे; अत: उन दुर्बल वैष्णवोंको पकड़कर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10520)
- **Original**: ये कमल ले लीजिये; क्योंकि आप ही हमारे उन्हें शंकरजीके पास ले गये। भगवान्‌ शंकरको
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10521)
- **Original**: प्रभु हैं। अच्युत! हमारा हृदय जिसके ध्यानसे देखकर उन सब वैष्णवोने भूतलपर माथा टेक
- **Translation**: 

---

