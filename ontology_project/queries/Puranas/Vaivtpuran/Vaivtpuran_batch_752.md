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

### Verse 1 (Vaivtpuran 543.13354)
- **Original**: यज्ञ्में पतिकी निन्‍दा सुनकर सतीने योगसे अपने द्विभुज-रूपसे गोलोकमें विराजमान हैं। ब्रह्मा, (शरीरकों त्याग दिया। पितरोंकी मानसी कन्या विष्णु और महेश्वर उन भगवान्‌ श्रीकृष्णके अंश
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13355)
- **Original**: मेनका तुम्हारी पत्नी हैं। उनके गर्भसे उन्हीं हैं। कोई देवता उनकी कला है और कोई
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13356)
- **Original**: जगदम्बिका सतीने जन्म ग्रहण किया है। कलांश। श्रीकृष्णने सृष्टिके लिये उन्मुख होकर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13357)
- **Original**: शैलराज! यह शिवा जन्म-जन्ममें और कल्प- स्वयं अपनी प्रकृति (शक्तिस्वरूपा श्रीराधा)-कों
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13358)
- **Original**: कल्पमें शिवकी पत्नी रही हैं। यह पराशक्ति प्रकट किया और उनमें अपने तेजोमय वीर्यकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13359)
- **Original**: जगदम्बा ज्ञानियोंकी बुद्धिरूपा है। इसे पूर्वजन्मकी स्थापना की। उस गर्भसे एक डिम्बका प्रादुर्भाव
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13360)
- **Original**: बातॉँका स्मरण बना रहता है। यह सर्वज्ञा, हुआ, जिसके भीतरसे महाविराद्‌ (नारायण)
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13361)
- **Original**: सिद्धिदायिनी और सिद्धिरूपिणी है। इसकी अस्थि प्रकट हुए। उन्हींकों महाविष्णु जानना चाहिये।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13362)
- **Original**: और चिताभस्मकों भगवान्‌ शिव स्वयं भक्तिपूर्वक वे श्रीकृष्फे सोलहवें अंश हैं। वे ही जब
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13363)
- **Original**: धारण करते हैं। कल्याणस्वरूप गिरिराज! तुम एकार्णवके जलमें शयन करते थे, उस समय
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13364)
- **Original**: स्वेच्छासे अपनी कन्या शिवको दे दो, दे दो। उनके नाभिकमलसे ब्रह्माका प्रादुर्भाव हुआ।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13365)
- **Original**: नहीं तो, वह स्वयं अपने प्राणवल्लभके स्थानको सृष्टिकर्ता ब्रह्मके भाल-देशसे चन्द्रशेखर शंकर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13366)
- **Original**: चली जायगी और तुम देखते रह जाओगे। प्रकट हुए हैं। महाविष्णुके वामपार्श्बसे विष्णु
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13367)
- **Original**: पूर्वजन्मसे जो जिसकी पत्नी है, दूसरे जन्ममें वह (लघु विराट्‌)-का प्राकट्य हुआ। शैलराज! इस
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13368)
- **Original**: अपने उस प्रियतमको अवश्य पाती है। प्रजापतिके प्रकार प्रकृतिसे उत्पन्न होनेके कारण ब्रह्मा, विष्णु
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13369)
- **Original**: इस नियमका कोई भी खण्डन नहीं कर सकता। और शिव आदि प्राकृतिक कहे गये हैं।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13370)
- **Original**: भगवान्‌ शिव स्वात्माराम और तत्त्वज्ञ हैं; अतः श्रीकृष्णसे प्रकट हुई प्रकृतिने मुख्यतः चार
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13371)
- **Original**: विवाहके लिये उत्सुक नहीं हैं। तारकासुरसे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13372)
- **Original**: * भ्रीकृष्णजन्मखण्ड * 5<89 ऋं###% # कक कक # # # ###ऋऊ#ऋऊ%%%#######%%%%%% +[(460:4.])]
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13373)
- **Original**: 22820 84 6 4
- **Translation**: 

---

