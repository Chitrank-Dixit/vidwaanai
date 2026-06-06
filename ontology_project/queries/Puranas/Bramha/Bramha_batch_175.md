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

### Verse 1 (Bramha 0.3481)
- **Original**: 'मुनिश्रेश ! बताइये, कौन मेरा गुरु हो सकता है? जो धर्मात्मा ऋषि हुए हैं। इन दोनोंके दो-दो पुत्र हुए,
- **Translation**: 

---

### Verse 2 (Bramha 0.3482)
- **Original**: तीनों लोकोंका गुरु हो, उसीके पास मैं जाऊँगा।' जो बड़े ही विद्वान्‌ और रूप तथा बुद्धिसे
- **Translation**: 

---

### Verse 3 (Bramha 0.3483)
- **Original**: । गौतमने कहा--जगदुरु भगवान्‌ शंकर ही गुरु सुशोभित थे। अब्विराके पुत्रका नाम था जीव
- **Translation**: 

---

### Verse 4 (Bramha 0.3484)
- **Original**: होने योग्य हैं। और भृगुके पुत्रका नाम था कवि। ये दोनों
- **Translation**: 

---

### Verse 5 (Bramha 0.3485)
- **Original**: शुक्रगे पूछ--मैं कहाँ रहकर शझ्डूरजीको अपने माता-पिताके अधीन रहते थे। जब दोनोंका
- **Translation**: 

---

### Verse 6 (Bramha 0.3486)
- **Original**: आराधना करूँ? यज्ञोपवीत-संस्कार हो गया, तब उनके पिता
- **Translation**: 

---

### Verse 7 (Bramha 0.3487)
- **Original**: । गौतम बोले-गौतमी गज्जामें स्नान करके परस्पर कहने लगे--'हम दोनॉमेंसे एक ही इन
- **Translation**: 

---

### Verse 8 (Bramha 0.3488)
- **Original**: पवित्र हो स्तोत्रोंद्राय भगवान्‌ शंकरको संतुष्ट करो। दोनों पुत्नॉंका शिक्षक हो। इससे एक ही शासन
- **Translation**: 

---

### Verse 9 (Bramha 0.3489)
- **Original**: संतुष्ट होनेपर वे जगदीश्वर तुम्हें विद्या प्रदान करेंगे। करेगा और दूसरा सुखसे बैठा रहेगा।!' यह
- **Translation**: 

---

### Verse 10 (Bramha 0.3490)
- **Original**: गौतमके कहनेसे शुक्र गोदायरोके तटपर गये सुनकर अज्लिराने कहा-'मैं कविकों भी अपने
- **Translation**: 

---

### Verse 11 (Bramha 0.3491)
- **Original**: और वहाँ स्नान करके पवित्र हो भगवान्‌ शिवकी पुत्रके समान ही पढ़ाऊँगा। वह सुखपूर्वक मेरे
- **Translation**: 

---

### Verse 12 (Bramha 0.3492)
- **Original**: स्तुति करने लगे। यहाँ रहे।' शुक्र बोले--प्रभो ! मैं बालक हूँ। मेरी बुद्धि अड्लिराकी बात सुनकर भूगुने कहा-'ठीक
- **Translation**: 

---

### Verse 13 (Bramha 0.3493)
- **Original**: बालककी ही है और आप बालचन्द्रमाको है” और उन्होंने अपने पुत्र शुक्रको अड्भिराकी
- **Translation**: 

---

### Verse 14 (Bramha 0.3494)
- **Original**: मस्तकपर धारण करनेवाले हैं। मुझे आपको स्तुति सेवार्में सौंप दिया। परन्तु अश्लिरा उन दोनों
- **Translation**: 

---

### Verse 15 (Bramha 0.3495)
- **Original**: करनेका कुछ भी ज्ञान नहीं है। केवल आपको बालकॉमें विषम बुद्धि रखते थे। इसलिये दोनोंको
- **Translation**: 

---

### Verse 16 (Bramha 0.3496)
- **Original**: नमस्कार करता हूँ। गुरुने मुझे त्याग दिया है। मेरा पृथक्‌-पृथक्‌ पढ़ाते थे। बहुत दिनोतक किसी
- **Translation**: 

---

### Verse 17 (Bramha 0.3497)
- **Original**: कोई सुददद्‌ अथवा सखा नहीं है। आए हो सब प्रकार चलता रहा, तब एक दिन शुक्रने कहा--
- **Translation**: 

---

### Verse 18 (Bramha 0.3498)
- **Original**: प्रकारसे मेरे प्रभु हैं। जगन्नाथ! आपको नमस्कार
- **Translation**: 

---

### Verse 19 (Bramha 0.3499)
- **Original**: 268 * संक्षिप्त अह्यपुराण * है। आप गुरुवालोंके भी गुरु और बड़ोंके भी बड़े
- **Translation**: 

---

### Verse 20 (Bramha 0.3500)
- **Original**: लौकिकी, बैदिकी तथा अन्यान्य विद्याएँ भी दीं। हैं। मैं छोटा बच्चा हूँ। मुझपर कृपा कीजिये।
- **Translation**: 

---

