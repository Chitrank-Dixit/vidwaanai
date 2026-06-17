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

### Verse 1 (Vaivtpuran 23.1582)
- **Original**: लम्बा-चौड़ा सुन्दर मण्डल बनाकर उसमें हाथ श्रेष्ठ साधक गुरु, इष्टदेव, सूर्य, ब्रह्मा, महादेव,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1583)
- **Original**: दे ती्थोंका आबाहन करे। जो-जो तीर्थ हैं, उन विष्णु, माया, लक्ष्मी और सरस्वतीको प्रणाम करे।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1584)
- **Original**: सबका वर्णन कर रहा हूँ। तत्पश्चात्‌ गुड़, घी, दर्पण, मधु और सुवर्णका स्पर्श
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1585)
- **Original**: गड्ढे च॒ यमुने चैव गोदावरि सरस्वति। करके समयानुसार स्नान आदि करे। जब पोखरी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1586)
- **Original**: नर्मदे सिन्धु काबेरि जलेउस्मिन्‌ संनिर्धिं कुरु
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1587)
- **Original**: या बावड़ीमें स्नान करे, तब धर्मात्मा एवं विद्वान “हे गड्ढे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1588)
- **Original**: यमुने ! गोदाबरि ! सरस्वति! नर्मदे! पुरुष पहले उसमेंसे पाँच पिण्ड मिट्टी निकालकर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1589)
- **Original**: सिन्धु! और कावेरि! तुम सब लोग इस जलमें बाहर फेंक दे। नदी, नद, गुफा अथवा तीर्थमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1590)
- **Original**: निवास करो! (इस प्रकार आवाहन करनेसे सब सत्रान करना चाहिये। पहले जलमें गोता लगाकर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1591)
- **Original**: तीर्थ जलमें आ जाते हैं)। तदनन्तर नलिनी, पुन: स्नानके लिये संकल्प करे। वैष्णव महात्माओंका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1592)
- **Original**: नन्दिनी, सीता, मालिनी, महापथा, भगवान्‌ स्रानविषयक संकल्प श्रीकृष्णकी प्रीतिके लिये
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1593)
- **Original**: विष्णुके पादार्ध्यसे प्रकट हुई त्रिपथगामिनी गड्जा, होता है और गृहस्थोंका वह संकल्प किये हुए
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1594)
- **Original**: पद्मावती, भोगवती, स्वर्णरेखा, - कौशिकी, दक्षा, पापोंके नाशके उद्देश्यसे होता है। ब्राह्मण संकल्प
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1595)
- **Original**: पृथ्वी, सुभगा, विश्वकाया, शिवामृता, विद्याधरी, करके अपने शरीरमें मिट्टी पोते। उस समय
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1596)
- **Original**: सुप्रसन्ना, लोकप्रसाधिनी, क्षेमा, वैष्णवी, शान्ता, निम्नांकित वेद-मन्त्रका पाठ करे। मिट्टी लगानेका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1597)
- **Original**: शान्तिदा, गोमती, सती, सावित्री, तुलसी, दुर्गा, उद्देश्य शरीरकी शुद्धि ही है। महालक्ष्मी, सरस्वती, श्रीकृष्णप्राणाधिका राधिका, शरीरमें मृत्तिका-लेपनका मन्त्र लोपामुद्रा, दिति, रति, अहल्या, अदिति, संज्ञा, अश्वक्रान्ते रथक़ान्ते विष्णुक्रान्ते वसुन्धर।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1598)
- **Original**: स्वधा, स्वाहा, अरुन्धती, शतरूपा तथा देवहूति मृत्तिके हर में पाप यन्मया दुष्कृतं कृतम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1599)
- **Original**: इत्यादि देवियोंका शुद्ध बुद्धिवाला बुद्धिमान्‌ पुरुष वसुन्धरे! तुम्हारे ऊपर अश्व चलते हैं, रथ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1600)
- **Original**: स्मरण करे। इनके स्मरणसे स्नान कर अथवा दौड़ते हैं और भगवान्‌ विष्णुने अपने चरणोंसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1601)
- **Original**: बिना स्नान किये ही मनुष्य परम पवित्र हो जाता तुम्हें आक्रान्त किया है (अथवा अवतारकालमें
- **Translation**: 

---

