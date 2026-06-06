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

### Verse 1 (Vaivtpuran 16.3494)
- **Original**: करनेमें तो हमें क्या बड़ी लज्जा होगी और नहीं माना जा सकता; तथापि कुछ मेरी भी प्रार्थना
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3495)
- **Original**: हारनेपर हमारी क्या भारी अपकीर्ति होगी? इसके है, उसे यथार्थतः सुननेकी कृपा करें। इस समय
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3496)
- **Original**: पहले मधु और कैटभके साथ श्रीहरिका भी तो
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3497)
- **Original**: 158 + संक्षिप्त ब्रह्मवैवर्तपुराण
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3498)
- **Original**: &%&#4$£ ££ #$ $ $# $ 4 4 $ 4 %$ 4 % 6 $ $ 555 55 % 6 5 56 4 4 4 5 5 4 4 4 5 6 4 5 4 % $ 5 4 5 5 $ 5 % 4 $ 6 54 # $ 5 5 # $ 4 # $ 5 % 4 5 % 555 55% £ युद्ध हो चुका है। राजन्‌! एक बार वे हिरण्याक्षसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3499)
- **Original**: साथ युद्ध करनेमें मुझे क्या लज्जा है? देवता लड़े थे और पुनः दूसरी बार हिरण्यकशिपुसे।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3500)
- **Original**: भगवान्‌ श्रीहरिकी शरणमें गये हैं। तभी उन्होंने स्वयं मैं भी इससे पूर्व त्रिपुर नामक दैत्योंके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3501)
- **Original**: मुझे तुम्हारे पास भेजा है। अत: देवताओंका राज्य साथ युद्ध कर चुका हूँ। यही नहीं, किंतु प्राचीन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3502)
- **Original**: तुम लौटा दो। बस, मेरे कहनेका इतना ही समयमें जो सर्वेश्वरी एवं प्रकृति नामसे प्रसिद्ध
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3503)
- **Original**: अभिप्राय है। अथवा मेरे साथ प्रसन्नतासे लड़नेके भगवती जगदम्बा हैं, उनका शुम्भ आदि असुरोंके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3504)
- **Original**: लिये तैयार हो जाओ। अब अधिक शब्दोंके साथ अत्यन्त अद्भुत युद्ध हुआ था। तुम तो स्वयं
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3505)
- **Original**: अपव्ययसे क्‍या प्रयोजन है? परमात्मा श्रीकृष्णके अंश और उनके पार्षद हो।। नारद! जब इस प्रकार कहकर भगवान्‌ शंकर जो-जो दैत्य मारे गये हैं, उनमेंसे कोई भी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3506)
- **Original**: चुप हो गये, तब शब्बुचूड़ भी अपने मन्त्रियोंके तुम्हारे-जैसे बलवान्‌ नहीं थे। फिर राजन्‌! तुम्हारे । साथ तुरंत उठकर खड़ा हो गया। (अध्याय 18) “>> ्यरकञ..> न भगवान्‌ शंकर और शद्जचूड़के पक्षोंमें युद्ध, भद्रकालीका घोर युद्ध है और आकाशवाणी सुनकर कालीका शब्डुचूड़पर पाशुपतास्त्र न चलाना भगवान्‌ नारायण कहते हैं--मुने ! प्रतापी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3507)
- **Original**: स्कन्‍्दके भयंकर एवं दुर्वह धनुषको काट दिया। “दानवराज शब्बुचूड़ सिर झुका भगवान्‌ शिवको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3508)
- **Original**: दिव्य रथके टुकड़े-टुकड़े कर डाले तथा रथके प्रणाम करके अपने मन्त्रियोंक साथ तत्काल
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3509)
- **Original**: घोड़ोंको भी मार गिराया। उनके मोरको दिव्यास्त्रसे विमानपर जा बैठा। दोनों दलोंमें युद्ध आरम्भ हो
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3510)
- **Original**: मार-मारकर छलनी कर दिया। इसके बाद गया। दानव स्कन्दकी शक्तिसे निरन्तर पीड़ित
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3511)
- **Original**: दानवेन्द्रने उनके बक्षःस्थलपर सूर्यके समान होने लगे। उनमें हलचल मच गयी। इधर स्वर्गमें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3512)
- **Original**: जाज्वल्यमान प्राणघातक शक्ति चलायी। उस देवताओंकी दुन्दुभियाँ बज उठीं। उस भयंकर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3513)
- **Original**: शक्तिके आघातसे एक क्षणतक मूर्च्छित होनेके समराद्भणमें ही स्कन्दके ऊपर फूलोंको वर्षा होने
- **Translation**: 

---

