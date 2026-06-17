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

### Verse 1 (Bramha 0.4141)
- **Original**: कार्य देखकर उन्हें बड़ा विस्मय हुआ। नारद! जीत होगी; अतः आप देवबताओंका पक्ष ग्रहण
- **Translation**: 

---

### Verse 2 (Bramha 0.4142)
- **Original**: इस कार्यसे प्रसन्न होकर राजाने कैकेयीकों वर कीजिये, जिससे देवता विजयी हों।' दिये। रानी कैकेयोने भी राजाकी आज्ञा स्वीकार वायुकी यह बात सुनकर राजा दशरथने
- **Translation**: 

---

### Verse 3 (Bramha 0.4143)
- **Original**: करके इस प्रकार कहा--' महाराज ! आपके दिये कहा--' वायुदेव! आप सुखपूर्वक पधारें। मैं अवश्य
- **Translation**: 

---

### Verse 4 (Bramha 0.4144)
- **Original**: हुए ये बर आपके ही पास रहें [ आवश्यकता चलूँगा।' वायुके चले जानेपर दैत्यगण राजाके
- **Translation**: 

---

### Verse 5 (Bramha 0.4145)
- **Original**: पड़नेपर ले लूँगी]
- **Translation**: 

---

### Verse 6 (Bramha 0.4146)
- **Original**: * पास आये और बोले--' भगवन्‌! हमारी सहायता
- **Translation**: 

---

### Verse 7 (Bramha 0.4147)
- **Original**: . राजा दशरथ पुरस्कारमें अनेक आभूषण देकर कीजिये। महाराज ! विजय आपपर ही अवलम्बित
- **Translation**: 

---

### Verse 8 (Bramha 0.4148)
- **Original**: अपनी प्रिया कैकेयीके साथ अपने नगरकों गये। है, अत: आप दैत्यराजकी सहायता करें।' राजा
- **Translation**: 

---

### Verse 9 (Bramha 0.4149)
- **Original**: विजयी होनेसे ये बहुत प्रसन्न थे। तदनन्तर बहुत बोले--' वायुदेवने पहले मुझसे प्रार्थना को है और
- **Translation**: 

---

### Verse 10 (Bramha 0.4150)
- **Original**: समयके बाद मुनोश्वर ऋष्यश्रृड़्की कृपासे देवताओंकी मैंने देवताओंकी सहायता करनेका बचन दे दिया । कार्यसिद्धिके लिये राजा दशरथके चार देवोपम जननी
- **Translation**: 

---

### Verse 11 (Bramha 0.4151)
- **Original**: हि “यम प्रानीय7णदझीडई चनीयखकफडनईजफ ु * स तु मध्ये महाराजों मार्गे वीक्ष्य तदा प्रियाम्‌। कैकेय्या: कर्म तद्‌ दृष्टवा विस्मय परम गतः
- **Translation**: 

---

### Verse 12 (Bramha 0.4152)
- **Original**: ततस्तस्थै बरान्‌ प्रादाल्त्रीस्तु नारद सा अपधि। अनुमान्य नृपप्रोर्क फैकेयी वाक्धमत्रवीतू
- **Translation**: 

---

### Verse 13 (Bramha 0.4153)
- **Original**: त्वयि तिह्ठन्तु राजेद्र त्ववा दत्ता वरा अमी
- **Translation**: 

---

### Verse 14 (Bramha 0.4154)
- **Original**: 290--31)
- **Translation**: 

---

### Verse 15 (Bramha 0.4155)
- **Original**: र0्ड * संक्षिप्त ब्रह्मपुराण * पुत्र हुए। कौसल्यासे राम, कैकेयीसे बुद्धिमानोंमें
- **Translation**: 

---

### Verse 16 (Bramha 0.4156)
- **Original**: श्रीरमके साथ विवाह कर दिया। इसी प्रकार श्रेष्ठ भरत तथा सुमित्रासे लक्ष्मण और शत्रुघ्न हुए।
- **Translation**: 

---

### Verse 17 (Bramha 0.4157)
- **Original**: लक्ष्मण, भरत और शत्रुघ्नका विवाह भी राजा वे सभी पुत्र बुद्धिमानू, प्रिय तथा राजाके आज्ञाकारी
- **Translation**: 

---

### Verse 18 (Bramha 0.4158)
- **Original**: जनकके ही घर हुआ। तदनन्तर दीर्घकाल व्यतीत थे। एक बार महर्षि विश्वामित्र आये और उन्होंने
- **Translation**: 

---

### Verse 19 (Bramha 0.4159)
- **Original**: होनेपर राजा दशरथ समस्त प्रजा और गुरुकी यज्ञकी रक्षाके लिये राजासे राम और लक्ष्मणको
- **Translation**: 

---

### Verse 20 (Bramha 0.4160)
- **Original**: अनुमतिसे श्रीरामकों राज्य देने लगे। उस समय माँगा। विश्वामित्र उनके महत्त्वकों जानते थे।
- **Translation**: 

---

