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

### Verse 1 (Vaivtpuran 543.13334)
- **Original**: . (415। 49)
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13335)
- **Original**: 580 + संक्षिप्त ब्रह्मवैवर्तपुराण * 9 7])7]77:7:]77477+04]]]।।40 0 0800 3) 3) 8)
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13336)
- **Original**: । । . । 0
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13337)
- **Original**: । । 3 8.
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13338)
- **Original**: %करक## ## जो भगवान्‌ ध्रूभड्की लीलामात्से सृष्टिका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13339)
- **Original**: प्रकारकी मूर्ति धारण की। इसके सिवा सृष्टि- निर्माण एवं संहार करनेमें समर्थ हैं; जो ईश
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13340)
- **Original**: संचालनके लिये लीलापूर्वक अपने अंश और प्रकृतिसे परे, निर्गुण, पैरमात्मा एवं सर्वेश्वर हैं;
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13341)
- **Original**: कलाद्वारा उन्होंने और भी बहुतसे रूप धारण जो समस्त जन्तुओंसे निर्लित और उनमें लिप्त
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13342)
- **Original**: किये। श्रीकृष्णके वामाड्भसे प्रकट हुई प्रकृतिदेवी भी हैं; जो अकेले ही समस्त सृष्टिके संहारकर्म
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13343)
- **Original**: स्वयं तो रासेश्वरी राधाके रूपमें प्रतिष्ठित हैं। वे तथा सृष्टिकर्ममें भी समर्थ हैं एवं सर्वरूप हैं;
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13344)
- **Original**: ही स्वयं श्रीकृष्णेक मुखसे प्रकट हो वाणी निराकार, साकार, सर्वव्यापी और स्वेच्छामय हैं;
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13345)
- **Original**: सरस्वती कहलायीं, जो राग-रागिनियोंकी अधिष्ठात्री जो ईश्वर स्वयं सृष्टिकार्यका सम्पादन करनेके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13346)
- **Original**: देवी हैं। श्रीकृष्णके वक्षःस्थलसे प्रकट हुई वे लिये तीन रूप धारण करते हैं तथा सृष्टिकर्ता
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13347)
- **Original**: सर्वसम्पत्स्वरूपिणी लक्ष्मीके नामसे प्रसिद्ध हुईं *ब्रह्मा', पालनकर्ता 'विष्णु' एबं संहारकर्ता
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13348)
- **Original**: तथा सम्पूर्ण देवताओंके तेजमें उन्होंने अपने- *शिव '-नामसे प्रसिद्ध होते हैं; जो ' ब्रह्मा '-रूपसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13349)
- **Original**: आपको ही शिवारूपसे अभिव्यक्त किया और ब्रह्मलोकमें, “विष्णु'-रूपसे क्षीरसागरमें तथा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13350)
- **Original**: समस्त दानवॉका वध करके उन्होंने देवताओंको 'शिव '-रूपसे कैलासमें वास करते हैं; वे परब्रह्म राज्यलक्ष्मी प्रदान की। तत्पश्चात्‌ कल्पान्तरमें परमेश्वर ही 'श्रीकृष्ण' कहे गये हैं। ब्रह्म आदि
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13351)
- **Original**: दक्षपत्रीके गर्भसे जन्म ले वे ही सती नामसे सब रूप उन्हींकी विभूतियाँ हैं। श्रीकृष्णके दो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13352)
- **Original**: प्रसिद्ध हुईं और शिवकी पत्नी बनीं। दक्षने स्वयं रूप हैं-द्विभुज और चतुर्भुज। चतुर्भुज-रूपसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13353)
- **Original**: ही सतीकों शिवके हाथमें दिया; परंतु पिताके तो वे वैकुण्ठमें निवास करते हैं और स्वयं
- **Translation**: 

---

