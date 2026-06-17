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

### Verse 1 (Markende Puran 0.2061)
- **Original**: वैश्य उद्बाच
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2062)
- **Original**: 20 # सह्दी नगर आज मुझसे रहित है। पक्ष नहों, मेरे
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2063)
- **Original**: समाधिनाम बैश्वो5हमुत्पन्नो धनिर्ना कुल्े
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2064)
- **Original**: दुयाचारी भ्रत्यगण उसको धर्मपूर्वक रक्षा करते हैँ
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2065)
- **Original**: पुत्रदारैनिरस्तश. अनलोभादसाथुभि:। या उहों। जो सदा मदकी वर्षा करनेबाला और
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2066)
- **Original**: विहीनअभ्ष थनैदीरै: पुतरैरादाय मे धनम्‌
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2067)
- **Original**: शूरबीर था, बह मेरा प्रधान हाथी अब शत्रुओंके
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2068)
- **Original**: वनमभ्यागतों' दुःखोी निरस्तश्राप्तवन्धधिः। अधीन होकर न जाने किन भोगेंक्रो भोगतत होगा ?
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2069)
- **Original**: सो5ह न केब्ि पुत्राणां कुशलाकुशलात्मिकापू
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2070)
- **Original**: जो लोग मेरी कृपा, धत और भोजन पानेसे सदा
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2071)
- **Original**: प्रवृत्ति स्कनानां च दारणां चात्र संस्थित:। मेरे पीछे-पीछे चलते थे, वे निश्रय ही अब्न दूसरे शराजाओंका अनुसरण करते हॉंगे। उन अपव्ययी लोगोंके द्वारा सदा खर्च होते रहनेके क्रारण अत्पन्त कष्टसे जमा किया हुआ मेयर वह खज़ाना खाली हो जावगा।' ये तभा और भी कई बातें राजां सुंस्थ निरन्तर सोचते रहते थे। एक दिन उन्होंने वहाँ बिग्रवर मेधाके आश्रमके निकट एक लैश्यकों देखा कि नु तेषां गृहे क्षेम्रमक्षेमं किं नु साध्प्रतम्‌
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2072)
- **Original**: कं ते कि नु सदवृत्ता दुर्वत्ता: कि नु मे सुता:
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2073)
- **Original**: सैश्य बोला--
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2074)
- **Original**: राजन्‌ ! में धरन्ियोक्त कुलमें उत्पन्न एक वैश्य हूँ। मेरा नाम समाधि है
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2075)
- **Original**: मेरे दुष्ट स्त्रो-पुच्नोने धनके लोभसे मुझे अरसे बाहर निकाल दिया है। मेँ इस समय धन, सत्रों और प्रुजसे चच्नित हूँ। मेरे विश्वसनीय और' उससे पूछा-भाई! तुम कौन हो? यहाँ
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2076)
- **Original**: बन्धुओंने मेश डी धन लेकर मुझे दूर कर दिया तुम्हारे आनेका क्या कारण है? तुम क्‍यों शोकग्रस्त
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2077)
- **Original**: है, इसलिये दुखी होकर मैं वनपें चला आया हूँ। और अनमने-से दिखायी देते हो 7' राजा सुरक्षका
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2078)
- **Original**: यहाँ रहकर मैं इस बातकों नहीं जानता कि मेरे यह प्रमपूर्वक कहा हुआ वचन सुनकर वैश्सने
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2079)
- **Original**: पुत्रॉको, स्त्रीकों और स्वजनोंकी कुशल हैं या विनीत-भावसे उन्हें फ़्गाप करके कहा--
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2080)
- **Original**: 12--19
- **Translation**: 

---

