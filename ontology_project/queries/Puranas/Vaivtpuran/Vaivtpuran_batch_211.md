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

### Verse 1 (Vaivtpuran 13.10362)
- **Original**: पूर्वकालमें पुष्करतीर्थमें सूर्यके प्रकाशमें बैठकर वहाँ गोलोकमें जो निश्चय किया था, उसका
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10363)
- **Original**: परसात्मा श्रीकृष्णकी प्रसन्नताके लिये साठ हजार खण्डन नहीं होना चाहिये। प्रिये! तुम क्षणभर वर्षोंतक तपस्या की। तब वरदाता श्रीहरि मुझे ठहरो। मैं तुम्हारा मड्गल करूँगा। तुम्हारे वर देनेके लिये स्वयं पधारे। उनके “वर माँगो मनोरथकी पूर्तिका समय स्वयं आ पहुँचा है।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10364)
- **Original**: ऐसा कहनेपर मैंने प्रसन्नतापूर्वक अभीष्ट वर माँगते राधे! पहले मैंने जिसके लिये जो कुछ लिख
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10365)
- **Original**: हुए कहा--' हे गुणातीत परमेश्वर! जो सबके लिये दिया है और जिस समय उस मनोरथकी प्राप्तिका
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10366)
- **Original**: परम दुर्लभ है, उन राधिकाके चरण-कमलका निश्चय कर दिया है; उस पूर्व-निश्चयका खण्डन
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10367)
- **Original**: मुझे इसी समय शीघ्र दर्शन कराइये।' मेरी यह मैं स्वयं ही नहीं कर सकता। फिर विधाताकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10368)
- **Original**: बात सुनकर ये श्रीहरि मुझ तपस्वीसे बोले--' वत्स ! क्या विसात है, जो उसे मिटा सके ? मैं विधाताका
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10369)
- **Original**: इस समय क्षमा करो। उपयुक्त समय आनेपर भी विधाता हूँ। मैंने जिनके लिये जो कुछ विधान
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10370)
- **Original**: मैं. तुम्हें श्रीरधाके चरणारविन्दोंके दर्शन कर दिया है, उसका ब्रह्मा आदि देवता भी कदापि
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10371)
- **Original**: कराऊँगा।' ईश्वरकी आज्ञा निष्फल नहीं होती; खण्डन नहीं कर सकते। इसीलिये मुझे तुम्हारे चरणकमलोंके दर्शन प्राप्त इसी बीचमें ब्रह्मा श्रीहरिके सामने आये।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10372)
- **Original**: हुए हैं। माता! तुम्हारे ये चरण गोलोकमें तथा उनके हाथोंमें माला और कमण्डलु शोभा पा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10373)
- **Original**: इस समय भारतमें भी सबकी मनोवाजञ्छाके विषय रहे थे। चारों मुखोंपर मन्द मुस्कान खेल रही
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10374)
- **Original**: हैं। सब देवियाँ प्रकृतिकी अंशभूता हैं; अत: वे थी। निकट जाकर उन्होंने श्रीकृष्णजो नमस्कार
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10375)
- **Original**: निश्चय ही जन्य और प्राकृतिक हैं। तुम श्रीकृष्णके किया और आगमके अनुसार उनकी स्तुति कौ।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10376)
- **Original**: आधे अज्गसे प्रकट हुई हो; अतः सभी दृष्टियोंसे उस समय उनके नेन्रोंसे आँसू झर रहे थे। सम्पूर्ण
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10377)
- **Original**: श्रीकृष्णके समान हो। तुम स्वयं श्रीकृष्ण हो और अज्जोंमें रोमाझ हो आया था और भक्तिभावसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10378)
- **Original**: ये श्रीकृष्ण राधा हैं, अथवा तुम राधा हो और उनका मस्तक झुका हुआ था। स्तुति और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10379)
- **Original**: ये स्वयं श्रीकृष्ण हैं। इस बातका किसीने निरूपण नमस्कार करके जगद्धाता ब्रह्मा श्रीहरिक और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10380)
- **Original**: किया हो, ऐसा मैंने वेदोंमें नहीं देखा है। निकट गये। उन्होंने अपने प्रभुको भक्तिभावसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10381)
- **Original**: अम्बिके! जैसे गोलोक ब्रह्माण्डसे बाहर और पुनः प्रणाम किया। फिर वे श्रीराधिकाके समीप
- **Translation**: 

---

