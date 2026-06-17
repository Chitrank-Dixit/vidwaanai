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

### Verse 1 (Bramha 0.4441)
- **Original**: उन्हीं दोनोंके सहयोगसे होते हैं। उसमें भी जो कहकर दैत्यराज महाशनिने ऐरावतसहित इन्द्रको
- **Translation**: 

---

### Verse 2 (Bramha 0.4442)
- **Original**: तीर्थभूमि हो, वहीं आप चलें। उस स्थानपर लौटा दिया और उनसे यह बात कही--'इन्द्र!
- **Translation**: 

---

### Verse 3 (Bramha 0.4443)
- **Original**: भगवान्‌ विष्णु तथा शिवकी पूजा करके सम्पूर्ण आजसे तुम शिष्य हुए और मेरे श्वशुर वरुणजी
- **Translation**: 

---

### Verse 4 (Bramha 0.4444)
- **Original**: अभीष्ट वस्तुएँ प्राप्त कर लेंगे। मैंने यह भी सुना तुम्होरे गुरु हुए; क्‍योंकि इन्होंने तुम्हें मुक्ति
- **Translation**: 

---

### Verse 5 (Bramha 0.4445)
- **Original**: है कि जो स्त्रियाँ पतिव्रता हैं, वे ही सब कुछ दिलायी है। अब तुम बरुणके प्रति स्वामिभाव
- **Translation**: 

---

### Verse 6 (Bramha 0.4446)
- **Original**: जानती हैं। उन्होंने ही चराचर जगत्‌कों धारण * जासाध्यमस्ति तपसों नासाध्यं यज्ञकर्मण:। नासाध्यं लोकनाथल्य विष्णोर्भक्त्या हरस्थ च
- **Translation**: 

---

### Verse 7 (Bramha 0.4447)
- **Original**: ] सं0 ब्र0 पु0--8 (129। 50)
- **Translation**: 

---

### Verse 8 (Bramha 0.4448)
- **Original**: 218 + संक्षिप्त ब्रह्मपुराण « कर रखा है।* पृथ्वीपर सबसे सारभूत स्थान है
- **Translation**: 

---

### Verse 9 (Bramha 0.4449)
- **Original**: “अच्छा, ऐसा ही करूँगा” यों कहकर अपने दण्डकवन। वहाँ जगज्जननी गज्जा बहती हैं। वहीं
- **Translation**: 

---

### Verse 10 (Bramha 0.4450)
- **Original**: गुरु बृहस्पति और पत्नी शचीको साथ ले इन्द्र चलकर आप दीन-दु:खियोंकी पीड़ा दूर करनेवाले
- **Translation**: 

---

### Verse 11 (Bramha 0.4451)
- **Original**: जगज्जननी गौतमीके तटपर गये। दण्डकारण्यके जगदीश्वर श्रीविष्णु अथवा शिवकी आराधना करें।
- **Translation**: 

---

### Verse 12 (Bramha 0.4452)
- **Original**: भीतर उनकी पावन धाराका दर्शन करके इन्द्रको दुःखके समुद्रमें डूबनेवाले अनाथ मनुष्योंको श्रीशिव
- **Translation**: 

---

### Verse 13 (Bramha 0.4453)
- **Original**: बढ़ी प्रसन्नता हुई। उन्होंने देवाधिदेव शिवको तथा श्रीविष्णु अथवा गद्गाके सिवा दूसरा कोई
- **Translation**: 

---

### Verse 14 (Bramha 0.4454)
- **Original**: प्रसन्नताके लिये तपस्या करनेका विचार किया। कहीं भी शरण देनेवाला नहीं है। अत: एकाग्रचित्त
- **Translation**: 

---

### Verse 15 (Bramha 0.4455)
- **Original**: पहले गड्जामें स्नान करके उन्होंने हाथ जोड़कर होकर पूर्ण प्रयत्न करके आप इनको संतुष्ट करें।
- **Translation**: 

---

### Verse 16 (Bramha 0.4456)
- **Original**: प्रणाम किया तथा एकमात्र भगवान्‌ शिवके शरण मेरे साथ रहकर भक्ति, स्तोत्र तथा तपस्याके द्वारा
- **Translation**: 

---

### Verse 17 (Bramha 0.4457)
- **Original**: होकर उनका स्तवन आरम्भ किया। इनकी आराधना करें। तत्पश्चात्‌ भगवान्‌ शिव और
- **Translation**: 

---

### Verse 18 (Bramha 0.4458)
- **Original**: इद्ध बोले--जो अपनी मायासे सम्पूर्ण चराचर विष्णुके प्रसादसे आप कल्याणके भागी होंगे। जगतूकी सृष्टि, रक्षा और संहार करते हैं, किंतु बिना जाने किया हुआ कर्म कर्मनिष्ठ पुरुषको ' उसमें आसक्त नहीं होते, जो एक, स्वतन्त्र तथा एकगुना फल देता है। उसके विधि-विधान और
- **Translation**: 

---

### Verse 19 (Bramha 0.4459)
- **Original**: अद्ठैत चिदानन्दस्वरूप हैं, वे पिनाकधारी भगवान्‌ तत्वको अच्छी प्रकार जानकर करनेसे सौ-गुना
- **Translation**: 

---

### Verse 20 (Bramha 0.4460)
- **Original**: शंकर हमपर प्रसन्न हों। वेदान्तके रहस्थोंको फल मिलता है और पत्नीके साथ उसका अनुष्ठान
- **Translation**: 

---

