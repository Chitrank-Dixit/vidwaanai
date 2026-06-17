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

### Verse 1 (Vaivtpuran 8.2845)
- **Original**: विभाजन किया और उसमेंसे कुछ-कुछ अंश उसका शरीर परम ख्िग्ध तेज बन गया। आपने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 8.2846)
- **Original**: विष्णुको, वैष्णवोंको, धार्मिक पुरुषोंकों, धर्मको, उस तेजको टुकड़े-टुकड़े करके बितरण कर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 8.2847)
- **Original**: दुर्बलॉको, तपस्वियोंको, देवताओं और पण्डितोंको दिया। रल्न, सुवर्ण, श्रेष्ठ मणि, स्त्रियोंक मुखकमल,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 8.2848)
- **Original**: दे दिया। प्रभो! इतनी सब बातें तो मैं सुना चुकी । राजा, पुष्पोंकी कलियाँ, पके हुए फल, लहलहाती
- **Translation**: 

---

### Verse 5 (Vaivtpuran 8.2849)
- **Original**: आपके ऐसे-ऐसे बहुत-से गुण हैं। आप सदा खेतियाँ, राजाओंके सजे-धजे महल, नवीन पात्र
- **Translation**: 

---

### Verse 6 (Vaivtpuran 8.2850)
- **Original**: ही उच्च सुन्दरी देवियोंसे प्रेम किया करते हैं। और दूध-ये सब आपके द्वारा उस शोभाके इस प्रकार रक्त कमलके समान नेत्रोंबाली कुछ-कुछ भाग पा गये। मैंने आपको “प्रभा'के
- **Translation**: 

---

### Verse 7 (Vaivtpuran 8.2851)
- **Original**: राधाने भगवान्‌ श्रीकृष्णससे कहकर साध्वी गड्ढासे साथ प्रेम करते देखा। वह भी शरीर त्यागकर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 8.2852)
- **Original**: कुछ कहना चाहां। गड्जा योगमें परमप्रवीण थीं। सूर्यमण्डलमें प्रवेश कर गयो। उस समय उसका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 8.2853)
- **Original**: योगके प्रभावसे राधाका मनोभाव उन्हें ज्ञात हो शरीर अत्यन्त तेजोमय बन गया था। उस
- **Translation**: 

---

### Verse 10 (Vaivtpuran 8.2854)
- **Original**: गया। अत: बीच सभामें ही अन्तर्धान होकर वे तेजोमयी प्रभाकों आपने विभाजन करके जगह-
- **Translation**: 

---

### Verse 11 (Vaivtpuran 8.2855)
- **Original**: अपने जलमें प्रविष्ट हो गर्वीं। तब सिद्धयोगिनों
- **Translation**: 

---

### Verse 12 (Vaivtpuran 8.2856)
- **Original**: श्32 * संक्षिम जहावैलेतपुराण « कक $%5$%%5$%$%$%%%%$%%%$%%$%%$%$%%$%%%%क%%क$%%$%%$%%$%%%$%$%$%%%%%क%$%%%$%$%%%$%%$%%%$%$%$% 54% $%#6 # राधाने योगद्वारा इस रहस्यको जानकर सर्वत्र
- **Translation**: 

---

### Verse 13 (Vaivtpuran 8.2857)
- **Original**: ज्योतिर्मय है। सम्पूर्ण कारणोंक भी ये कारण विद्यमान उन जलस्वरूपिणोी गज्जाकों अज्ललिसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 8.2858)
- **Original**: हैं। ये उस समय अमूल्य रक्नोंसे निर्मित दिव्य उठाकर पीना आरम्भ कर दिया। ऐसी स्थितिमें
- **Translation**: 

---

### Verse 15 (Vaivtpuran 8.2859)
- **Original**: सिंहासनपर विराजमान थे। गोपाल इनकी सेवामें राधाका अभिप्राय पूर्ण योगसिद्धा गड्जासे छिपा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 8.2860)
- **Original**: संलग्र होकर श्वेत चँँवर डुला रहे थे। गोपियोंके नहीं रह सका। अतः वे भगवान्‌ श्रीकृष्णकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 8.2861)
- **Original**: नृत्यको देखकर प्रसन्नताके कारण इनका मुखमण्डल शरणमें जाकर उनके चरणकमलोंमें लीन हो गयीं।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 8.2862)
- **Original**: मुस्कानसे भरा था। प्राणोंसे भी अधिक प्रिय तब राधाने गोलोक, बैकुण्ठलोक तथा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 8.2863)
- **Original**: श्रीराधा इनके वक्ष:स्थलपर शोभा पा रही थीं। ब्रह्मतोक आदि सम्पूर्ण स्थानोंमें गड़ाको खोजा;
- **Translation**: 

---

### Verse 20 (Vaivtpuran 8.2864)
- **Original**: उनके दिये हुए सुवासित पान ये चबा रहे थे। परंतु कहीं भी वह दिखायी नहीं दीं। उस समय
- **Translation**: 

---

