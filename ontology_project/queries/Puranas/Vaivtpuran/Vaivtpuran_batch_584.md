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

### Verse 1 (Vaivtpuran 45.4541)
- **Original**: और प्रसार कर रहा हूँ। सुरेश्वरि! जो पुरुष पूजा को थी। '$ हीं श्री मनसादेव्य स्वाहा।'
- **Translation**: 

---

### Verse 2 (Vaivtpuran 45.4542)
- **Original**: आषाढ़ मासकी संक्रान्तिक समय, मनसासंज्ञक इस दशाक्षर मूलमन्त्रका उच्चारण करके यथोचित
- **Translation**: 

---

### Verse 3 (Vaivtpuran 45.4543)
- **Original**: पञ्ममी (नागपञ्षमी )-कों अथवा आपषादसे रूपसे पूजनकी सभी सामग्री देवीको अर्पण की।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 45.4544)
- **Original**: आश्विनतक प्रतिदिन भक्तिके साथ तुम्हारी पूजा इस तरह सोलह प्रकारकी दुर्लभ वस्तुएँ देवराज
- **Translation**: 

---

### Verse 5 (Vaivtpuran 45.4545)
- **Original**: करेंगे, उनके यहाँ पुत्र-पौत्र आदिकी और धनकी इन्द्रके द्वारा साध्वी मनसाकी सेवामें अर्पित हुईं।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 45.4546)
- **Original**: वृद्धि होगी--यह निश्चित है। साथ ही वे यशस्वी, भगवान्‌ विष्णुकी प्रेरणासे इन्द्र प्रसन्नतापूर्वक
- **Translation**: 

---

### Verse 7 (Vaivtpuran 45.4547)
- **Original**: कीर्तिमान, विद्वान्‌ू और गुणी होंगे। जो व्यक्ति भक्तिसहित पूजामें लगे रहे। उस समय उन्होंने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 45.4548)
- **Original**: अज्ञानके कारण तुम्हारी पूजासे विमुख होकर नाना प्रकारके बाजे बजवाये। देवी मनसाके ऊपर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 45.4549)
- **Original**: निन्दा करेंगे, उनके यहाँ लक्ष्मी नहीं ठहरेगी और पुष्पोंकी वर्षा होने लगी। तदनन्तर ब्रह्मा, विष्णु
- **Translation**: 

---

### Verse 10 (Vaivtpuran 45.4550)
- **Original**: उन्हें सर्पोसि सदा भय बना रहेगा। तुम स्वयं और शिवकी आज्ञासे पुलकित-शरीर होकर नेत्रोंमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 45.4551)
- **Original**: स्वर्गमें स्वर्गलक्ष्मी हो। बैकुण्ठमें कमलाकी कला अश्रु भरे हुए इन्धने देवी मनसाकौ स्तुति की।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 45.4552)
- **Original**: हो। ये मुनिवर जरत्कारु भगवान्‌ नारायणके इन्द्र बोले--देवि ! तुम साध्वी पतिब्रताओंमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 45.4553)
- **Original**: साक्षात्‌ अंश हैं। पिताजीने हम सबकी रक्षाके परम श्रेष्ठ तथा परात्पर देवी हो। इस समय मैं लिये ही तपस्या और तेजके प्रभावसे मनके द्वारा तुम्हारी स्तुति करना चाहता हूँ; किंतु यह महत्त्वपूर्ण [तुम्हारी सृष्टि की है। अतएव तुम मनसादेवी कार्य मेरी शक्तिके बाहर है। देवी प्रकृते! वेदोमें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 45.4554)
- **Original**: कहलाती हो। देवि ! तुम सिद्धयोगिनी हो, अतः स्तोत्रोंका लक्षण यह बताया गया है कि स्तुत्यके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 45.4555)
- **Original**: स्वतः मनसे देवन (सर्वत्र गमन) करनेकी शक्ति स्वभावका प्रतिपादन किया जाय; परंतु सुव्रते! मैं
- **Translation**: 

---

### Verse 16 (Vaivtpuran 45.4556)
- **Original**: रखती हो; इसलिये जगत्‌में मनसादेवीके नामसे तुम्हारे स्वभावका वर्णन करनेमें असमर्थ हूँ। तुम
- **Translation**: 

---

### Verse 17 (Vaivtpuran 45.4557)
- **Original**: पूजित और वन्दिता होती हो। देवता भक्तिपूर्वक शुद्ध-सत्त्वस्वरूपा हो, तुममें कोप और हिंसाका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 45.4558)
- **Original**: निरन्तर मनसे तुम्हारी पूजा करते हैं, इसीसे नितान्त अभाव है। यही कारण है कि जरत्कारु
- **Translation**: 

---

### Verse 19 (Vaivtpuran 45.4559)
- **Original**: विद्वान्‌ पुरुष तुम्हें मनसादेवी कहते हैं। देवि! तुम मुनिके द्वारा परित्यक्त होनेपर भी तुमने उन
- **Translation**: 

---

### Verse 20 (Vaivtpuran 45.4560)
- **Original**: सदा सत्त्वका सेवन करनेसे सत्त्वस्वरूपा हो। जो मुनिको शाप नहीं दिया। साध्वि! मैंने माता पुरुष जिस वस्तुका निरन्तर चिन्तन करते हैं, वे अदितिके समान मानकर तुम्हारा पूजन किया है।
- **Translation**: 

---

