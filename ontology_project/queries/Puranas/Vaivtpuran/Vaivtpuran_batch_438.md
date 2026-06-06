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

### Verse 1 (Vaivtpuran 23.1722)
- **Original**: योगीजनोंको ही वह चन्द्रमण्डलके समान सुखपूर्वक उत्तर दिया, वह सुनो; मैं तुम्हें बताता हूँ। बह । दिखायी देता है। योगीलोग उसे सनातन परल्रह्म ज्ञान तत्त्वोंका सारभूत तत्त्व है, अज्ञानान्‍्धकारसे [कहते हैं और दिन-रात उस सर्वमग्ललमय अन्धे हुए लोगोंके लिये नेत्ररूप है तथा दुविधा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1723)
- **Original**: सत्यस्वरूप परमात्माका ध्यान करते रहते हैं। वह अथवा द्वैत नामक भ्रमरूपी अन्धकारका नाश
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1724)
- **Original**: परमात्मा निरीह, निराकार तथा सबका ईश्वर है।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1725)
- **Original**: 80 +* संक्षिप्त ब्रह्मवैचर्तपुराण + अऊ
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1726)
- **Original**: 4444 464 48% ##$ #% $ 44 45 4 444 $ 4 % 4 4 4 #% 4 4 4 45 4 5 % 4 5 # 5 444 4 % 4 4 5 4 4 84% 5 हक 45 # 54 4 44 8 55 84 4 % उसका स्वरूप उसकी इच्छाके अनुसार है। वह
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1727)
- **Original**: सिद्ध होता है। यही बात दृष्टिमें रखकर कुछ लोग स्वतन्त्र तथा समस्त कारणोंका भी कारण है।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1728)
- **Original**: प्रकृति और ब्रह्म दोनोंकी ही निश्चितरूपसे नित्यताका परमानन्दस्वरूप तथा परमानन्दकी प्राप्तिका हेतु
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1729)
- **Original**: प्रतिपादन करते हैं। कुछ विद्वानोंका कथन है कि है। सबसे उत्कृष्ट, प्रधान पुरुष (पुरुषोत्तम),
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1730)
- **Original**: ब्रह्म स्वयं ही प्रकृति और पुरुषरूपमें प्रकट है। प्राकृत गुणोंसे रहित तथा प्रकृतिसे परे है।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1731)
- **Original**: कुछ लोग यह भी कहते हैं कि प्रकृति ब्रह्मसे प्रलयके समय उसीमें सर्वबीजस्वसरूपपिणी प्रकृति
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1732)
- **Original**: अतिरिक्त (भिन्न) है। वह ब्रह्म परमधाम-स्वरूप लीन होती है। ठीक उसी तरह, जैसे अग्रिमें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1733)
- **Original**: तथा समस्त कारणोंका भी कारण है। ब्रह्मन्‌! उस उसकी दाहिका शक्ति, सूर्यमें प्रभा, दुग्धमें ब्रह्मका लक्षण श्रुतिमें कुछ इस प्रकारका सुना गया धबलता और जलमें शीतलता लीन रहती है।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1734)
- **Original**: है-ब्रह्म सबका आत्मा है। बह सबसे निर्लिप्त मुने! जैसे आकाशमें शब्द और पृथ्वीमें गन्ध सदा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1735)
- **Original**: और सबका साक्षी है। सर्वत्र व्यापक और सबका विद्यमान है, उसी तरह निर्गुण ब्रह्ममें निर्गुण
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1736)
- **Original**: आदिकारण है। सर्वबीजस्वरूपिणी प्रकृति उस प्रकृति सर्वदा स्थित है। जब ब्रह्म सृष्टिके लिये
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1737)
- **Original**: ब्रह्मफी शक्ति है। जिससे वह ब्रह्म शक्तिमान्‌ है, उन्मुख होता है, तब अपने अंशसे पुरुष कहलाता
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1738)
- **Original**: अत: शक्ति और शक्तिमान्‌ दोनों अभिन्न हैं। है। वत्स! वही गुणों-विषयोंसे सम्बन्ध स्थापित
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1739)
- **Original**: योगीलोग सदा तेज:स्वरूपमें ही ब्रह्मका ध्यान करनेपर प्राकृत एवं विषयी कहा गया है। त्रिगुणा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1740)
- **Original**: करते हैं; परंतु सूक्ष्म बुद्धिवाले मेरे भक्त--वैष्णवजन प्रकृति उस परमात्मामें ही उत्कृष्ट छायारूपिणी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1741)
- **Original**: ऐसा नहीं मानते। वे वैष्णलजन उस आश्चर्यमय मानी गयी है। मुने! जैसे कुम्हार मिट्टीसे घड़ा
- **Translation**: 

---

