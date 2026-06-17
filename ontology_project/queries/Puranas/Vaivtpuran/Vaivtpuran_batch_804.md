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

### Verse 1 (Vaivtpuran 543.14394)
- **Original**: वह रलत्नमयी मुद्रिका दे दी। धर्मात्मा वायुपुत्र तब भगवान्‌ श्रीरामने स्वयं ही जाकर वानरराज
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14395)
- **Original**: सीताकी दशा देखकर उनके चरणकमलोंको सुग्रीवके साथ मित्रता की और वालीको बाणोंसे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14396)
- **Original**: पकड़कर रोने लगे। उन्होंने श्रीरामका वह मारकर उनका राज्य सुग्रीवको दे दिया। यह
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14397)
- **Original**: संदेश सुनाया, जो सीताजीके जीवनको रक्षा सब उन्होंने अपने मित्रके प्रति की गयी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14398)
- **Original**: करनेवाला था। प्रतिज्ञा पालन करनेके लिये किया था।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14399)
- **Original**: हनुमानजी बोले--मात: ! समुद्रके उस पार वानरराजने सीताका पता लगानेके लिये समस्त
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14400)
- **Original**: श्रीराम और लक्ष्मण इस राक्षसपुरीपर चढ़ाई दिशाओंमें दूत भेजे और लक्ष्मणसहित श्रीराम
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14401)
- **Original**: करनेके लिये तैयार खड़े हैं। बलवान्‌ बानरराज सुग्रीबके यहाँ रहने लगे। श्रीरामने हनुमानूजीको
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14402)
- **Original**: सुग्रीव श्रीरामके मित्र हो गये हैं। श्रीरामने प्रेमपूर्वक हृदयसे लगाकर उन्हें अपनी परम दुर्लभ
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14403)
- **Original**: बालीका बध करके अपने मित्र सुग्रीबको निष्कण्टक पदधूलि प्रदान की और सीताके लिये पहचानके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14404)
- **Original**: राज्य दिया है। साथ ही उन्हें उनकी पत्नी भी प्राप्त रूपमें श्रेष्ठ एवं सुन्दर रत्नमयी मुद्रिका उनके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14405)
- **Original**: करा दी है, जिसे पहले बालीने हर लिया था। हाथमें देकर अपना शुभ संदेश भी प्रदान किया,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14406)
- **Original**: सुग्रीवने भी धर्मत: तुम्हारे उद्धारकी प्रतिज्ञा की जो सीताको जीवन-रक्षाका कारण बना। यह सब
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14407)
- **Original**: है। उनके समस्त बानर तुम्हें खोजनेके लिये सब करनेके पश्चात्‌ उन्होंने हनुमानूजीकों उत्तम
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14408)
- **Original**: ओर गये हैं। मुझसे तुम्हारा मड्रलमय समाचार पा दक्षिण दिशामें भेजा। हनुमानजी रुद्रकी कलासे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14409)
- **Original**: कमलनयन श्रीराम गहरे सागरपर सेतु बाँधकर प्रकट हुए थे। बे श्रीरामका संदेश ले सीताकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14410)
- **Original**: शीघ्र यहाँ आ पहुँचेंगे और पापी रावणकों उसके खोजके लिये लंकाको गये। वहाँ उन्होंने पुत्र तथा बान्धवोंसहित मारकर अविलम्ब तुम्हारा अशोकवाटिकामें सीताजीको देखा, जो शोकसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14411)
- **Original**: उद्धार करेंगे। आज तुम्हारे प्रसादसे इस रत्रमयी अत्यन्त कृश दिखायी देती थीं। अमावास्याको
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14412)
- **Original**: लंकाको मैं बेखटके जलाकर भस्म कर दूँगा। तुम अत्यन्त क्षीण हुई चन्द्रकलाके समान वे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14413)
- **Original**: मुस्कराती हुई मेरे इस पराक्रमको देखो। सुत्रते! उपवासके कारण बहुत ही दुबली-पतली हो
- **Translation**: 

---

