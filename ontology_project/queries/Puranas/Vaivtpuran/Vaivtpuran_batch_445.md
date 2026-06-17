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

### Verse 1 (Vaivtpuran 23.1862)
- **Original**: पश्नदेवीरूपा प्रकृतिका तथा उनके अंश, कला एवं कलांशका विशद वर्णन भगवान्‌ नारायण कहते हैं--नारद! [ ब्रह्ममय देखते हैं। भगवान्‌ श्रीकृष्ण स्वेच्छामय, गणेशजननी दुर्गा, लक्ष्मी, सरस्वती, सावित्री और
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1863)
- **Original**: सर्वतन्त्र-स्वतन्त्र परम पुरुष हैं। उनके मनमें राधा-ये पाँच देवियाँ प्रकृति कहलाती हैं।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1864)
- **Original**: सृष्टिकी इच्छा उत्पन्न होते ही सहसा 'मूल इन्हींपर सृष्टि निर्भर है। . प्रकृति' परमेश्वरी प्रकट हो गयीं। तदनन्तर नारदजीने पूछा--ज्ञानियोंमें प्रमुख स्थान
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1865)
- **Original**: परमेश्वरकी आज्ञाके अनुसार सृष्टि-रचनाके लिये प्राप्त करनेवाले साधो! वह प्रकृति कहाँसे प्रकट
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1866)
- **Original**: इनके पाँच रूप हो गये। भगवती प्रकृति भक्तोंके हुई है, उसका कैसा स्वरूप है, कैसे लक्षण हैं
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1867)
- **Original**: अनुरोधसे अथवा उनपर कृपा करनेके लिये तथा क्‍यों बह पाँच प्रकारकी हो गयी ? उन समस्त
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1868)
- **Original**: बिविध रूप धारण करती हैं। देवियोंके चरित्र, उनके पूजाके विधान, उनके गुण। जो गणेशकी माता ' भगवती दुर्गा” हैं, उन्हें और वे किसके यहाँ कैसे प्रकट हुईं-ये सभी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1869)
- **Original**: शिवस्व॒रूपा' कहा जाता है। ये भगवान्‌ शंकरकी प्रसडज़॒ आप मुझे बतानेकी कृपा करें। प्रेयसी भार्या हैं। नारायणी, विष्णुमाया और पूर्ण भगवान्‌ नारायणने कहा--वत्स ! 'प्र' का
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1870)
- **Original**: ब्रह्मस्वरूपिणी नामसे ये प्रसिद्ध हैं। ब्रह्मादि अर्थ है 'प्रकृष्' और “कृति' से सृष्टिके अर्थका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1871)
- **Original**: देवता, मुनिगण तथा मनु प्रभूति-सभी इनकी बोध होता है, अत: सृष्टि करनेमें जो प्रकृष्ट (परम
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1872)
- **Original**: पूजा करते हैं। ये सबकी अधिष्ठात्री देवी हैं, प्रवीण) है, उसे देवी ' प्रकृति' कहते हैं। सर्वोत्तम
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1873)
- **Original**: सनातन ब्रह्मस्वरूपा हैं। यश, मद्गल, धर्म, श्री, सत्त्वगुणके अर्थमें 'प्र' शब्द, मध्यम रजोगुणके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1874)
- **Original**: सुख, मोक्ष और हर्ष प्रदान करना इनका अर्थमें 'कृ' शब्द और तमोगुणके अर्थमें 'ति'
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1875)
- **Original**: स्वाभाविक गुण है। दुःख, शोक और उद्बेगको शब्द है। जो त्रिगुणात्मकस्वरूपा है, वही
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1876)
- **Original**: ये दूर कर देती हैं। शरणमें आये हुए दीनों सर्वशक्तिसे सम्पन्न होकर सृष्टिविषयक कार्यमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1877)
- **Original**: एवं पीड़ितोंकी रक्षामें सदा संलग्न रहती हैं। ये प्रधान है, इसलिये 'प्रधान' या 'प्रकृति' कहलाती
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1878)
- **Original**: तेज:स्वरूपा हैं। इनक़ा विग्रह परम तेजस्वी है। 'प्र' प्रथम अर्थमें और 'कृति' सृष्टि-अर्थमें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1879)
- **Original**: है। इन्हें तेजकी अधिष्ठात्री देवी कहा जाता है। है। अत: जो देवी सृष्टिकी आदिकारणरूपा है,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1880)
- **Original**: ये सर्वशक्तिस्वरूपा हैं और भगवान्‌ शंकरको उसे प्रकृति कहते हैं। सृष्टिके अवसरपर परत्नह्म
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1881)
- **Original**: निरन्तर शक्तिशाली बनाये रखती हैं। सिद्धेश्वरी, परमात्मा स्वयं दो रूपोंमें प्रकट हुए--प्रकृति और
- **Translation**: 

---

