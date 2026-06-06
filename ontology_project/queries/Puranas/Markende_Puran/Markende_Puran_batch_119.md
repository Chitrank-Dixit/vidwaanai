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

### Verse 1 (Markende Puran 0.2361)
- **Original**: शोषिततषा महातद्य: सद्यस्तत्र प्रसुस्तुव॒:। मध्ये चासुरसैन्यस्थ वारणासुरवाशिनाम्‌
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2362)
- **Original**: क्षणेन त्तन्महासैन्यमसुराणां तथाम्बिका। निन्ये क्षयं यथ्वा बहिस्तृणद्वारुमहात्रयम्‌।
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2363)
- **Original**: स॒ चर 'िंहों महानादमुत्सुजन्धुतक्रेसर:। झरीरिभ्योउभरारीणामसूनिव_ विचिन्यति
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2364)
- **Original**: देव्या गणश्न भैस्तत्र कु युद्ध महांसुर:। यथैयां सुतुषुर्देवा: पुष्पवृष्टिमुचो दिवि
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2365)
- **Original**: देबोका वाहन बह सिंह भी क्रोधमें भरकर गर्दनके बालोको हिलाता हुआ अम्ुरोंको सेनामें इस प्रकार छिचरने लगा, मानों वनोंसें दावानल फैल रहा हों! रणभूमिमें दैत्पोंके साथ युद्ध करतों हुई अध्विका टेबीने जितने निःश्वास छोड़े, वे सभी तत्काल सैकड़ों- हजारों गणोंके रूपमें प्रकर हो गये और परशु, भिन्दिपाल, ख्ढ तथा पट़्रिश आदि अ्षस्त्रोंद्ार असुरोक्ा सापरा करने लगे
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2366)
- **Original**: 49--73
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2367)
- **Original**: देवोकी शक्तिसे बढ़ें हुए वे गण असुरोंका नाश करते हुए नगाड़। और शक आदि ब्राजे बजाने लगे
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2368)
- **Original**: उस संग्राम- 6. पा0-शरबरश्टिपि:। 2. 50-सेगर0. रा्यगु0। हलागूस्। 3, फिसे किम्नी प्रस्नणे इसके व्गठ *सधरधापिलुआाद्र): झूंगामे लौध्टर्णणे। रतनता घर अधिक हैं. 5, पा0-यग्रैनों। 5. पा00-टष्टछर्केग! ।
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2369)
- **Original**: श्र » संक्षिप्त मार्कएडेसपुराण « अऑ5#4:#6400017776.7545646।:#07 1 204.2.3,44:4:54: 4600 9:104733
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2370)
- **Original**: 4 644 6440 750 0720/664644 640 7750 77354 पहोत्सवमें कितने हों गण मृदज्ञ वजा रहे थे। यद्के हो रूपमें अच्छे-अच्छे हथियार हाथपें ले तददन्तर टेंचौने त्रिशूलसे, गदासे, शक्तिकी वर्षासे
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2371)
- **Original**: देवीके साथ युद्ध करने लगते थे। दूसरे ऋबन्ध और खज़ आदिसे क्षेकड़ों पत्तादैत्योंका संहार कर
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2372)
- **Original**: बुद्धेके ब्राजोक्रों लबपर नाचते थे
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2373)
- **Original**: 60--63
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2374)
- **Original**: डाला। कितनोंको घंटेके' भयड्भर भादसे मुर्ष्छित' कितने हो बिता सिसके भ्रड़ हाथोंसें खड़, शक्ति ऋर्के भार गिराया
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2375)
- **Original**: बहुतेरे दैत्योक्नो, और कष्ट लिये दौड़ते थे तथा दूसरे-दूसरे आाशसे जाँबकर धसतीपर घसोटा। कितने ही दैत्व
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2376)
- **Original**: महादँत्थ ठहरो! ठहरों !!' यह कहते हुए देवोकों उनकी तीखी तलबास्की मारसे दो-दो टुकड़े हो
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2377)
- **Original**: चुद्धक लिये ललकारते थे। जहाँ वह घोर संग्राम शु.ये
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2378)
- **Original**: कितने ही गदाक्ी चोटसे घायल हो हुआ था, बहाँकी धरती देवीके गिराये हुए रथ, धरतीपर सो गये। कित्नने ही मृक्षलकों मारसे
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2379)
- **Original**: हाथी, छोड़े और असुरॉकी लाशोसि ऐसी पट गयी अत्यन्त आहत होकर रक वमन करते लगे। कुछ
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2380)
- **Original**: थी दि वहाँ चलना-फिरना असम्भव हो गया दत्य शूलसे छातो फट जानेके कारण पृथ्वीपर ढेर था
- **Translation**: 

---

