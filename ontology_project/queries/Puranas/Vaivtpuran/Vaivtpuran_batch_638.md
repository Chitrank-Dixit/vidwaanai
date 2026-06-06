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

### Verse 1 (Vaivtpuran 65.5640)
- **Original**: निर्गुणा परादेवी तेजोमण्डलके मध्यभागमें स्थित वर्षोतककी की हुई पूजाका फल पा लेता है। मूल
- **Translation**: 

---

### Verse 2 (Vaivtpuran 65.5641)
- **Original**: हो अत्यन्त कमनीय जान पड़ती थीं। भक्तोंपर नक्षत्रमें देवीका प्रवेश होनेपर यज्ञका फल प्राप्त
- **Translation**: 

---

### Verse 3 (Vaivtpuran 65.5642)
- **Original**: अनुग्रहके लिये कातर हुई उन कृपारूपा स्वेच्छामयी होता है। उत्तराषाढ़में पूजन करनेपर बाजपेय-
- **Translation**: 

---

### Verse 4 (Vaivtpuran 65.5643)
- **Original**: देवीको देखकर राजेन्द्र सुरथने भक्तिसे गर्दन नीची यज्ञके फलकी प्राप्ति होती है। श्रवण नक्षत्रमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 65.5644)
- **Original**: करके पुनः उनकी स्तुति की। उस स्तुतिसे संतुष्ट देवीका विसर्जन करके मनुष्य लक्ष्मी तथा पुत्र-
- **Translation**: 

---

### Verse 6 (Vaivtpuran 65.5645)
- **Original**: हो जगदम्बाने मन्‍्द मुस्कराहटके साथ राजेन्द्रको पौत्रोंको पाता है, इसमें संशय नहीं है। देवीकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 65.5646)
- **Original**: सम्बोधित करके कृपापूर्वक यह सत्य बात कही। पूजासे मनुष्यको पृथ्वीकी परिक्रमाका पुण्य प्रात
- **Translation**: 

---

### Verse 8 (Vaivtpuran 65.5647)
- **Original**: प्रकृति बोली--राजन्‌! तुम साक्षात्‌ मुझको होता है। यदि तिथिके साथ आर्द्रां नक्षत्रका योग
- **Translation**: 

---

### Verse 9 (Vaivtpuran 65.5648)
- **Original**: पाकर उत्तम वैभव माँग रहे हो। इस समय तुम्हें न मिले तो केवल नवमीमें पार्वतीका बोधन करके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 65.5649)
- **Original**: यही अभीष्ट है, इसलिये मैं बैभव ही दे रही मनुष्य एक पक्षतक पूजन करे तो उसे अश्वमेधयज्ञका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 65.5650)
- **Original**: हूँ। महाराज! तुम अपने समस्त शत्रुओंको फल प्राप्त होता है। उस दशामें नवमीकों पूजन
- **Translation**: 

---

### Verse 12 (Vaivtpuran 65.5651)
- **Original**: जीतकर निष्कण्टक राज्य पाओ। फिर दूसरे करके दशमीको विसर्जन कर दे। सप्तमीको पूजन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 65.5652)
- **Original**: जन्ममें तुम सावर्णि नामक आठवें मनु होओगे। करके विद्वान्‌ पुरुष बलि अर्पण करे, अष्टमीको
- **Translation**: 

---

### Verse 14 (Vaivtpuran 65.5653)
- **Original**: नरेश्वर! मैं परिणाममें (अन्ततोगत्वा) तुम्हें ज्ञान बलिरहित पूजन उत्तम माना गया है। अष्टमीको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 65.5654)
- **Original**: दूँगी। साथ ही परमात्मा श्रीकृष्णमें भक्ति एवं बलि देनेसे मनुष्योंपर विपत्ति आती है। विद्वान्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 65.5655)
- **Original**: दास्यभाव प्रदान करूँगी। जो मन्दबुद्धि मानव पुरुष नवमी तिथिकों भक्तिभावसे विधिवत्‌ बलि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 65.5656)
- **Original**: साक्षात्‌ मुझको पाकर वैभवकी याचना करता है, दे। विप्रवर! उस बलिसे मनुष्योंपर दुर्गाजी प्रसन्न
- **Translation**: 

---

### Verse 18 (Vaivtpuran 65.5657)
- **Original**: वह मायासे ठगा गया है; इसलिये विष खाता होती हैं। परंतु यह बलि हिंसात्मक नहीं होनी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 65.5658)
- **Original**: है और अमृतका त्याग करता है। ब्रह्मा आदिसे *हिंसाजन्य॑च पाप॑ च लभते नात्र संशय:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 65.5659)
- **Original**: यो य॑ हन्ति स त॑ हन्ति चेति वेदोक्तमेव च। (प्रकृतिखण्ड 65। 10, 12)
- **Translation**: 

---

