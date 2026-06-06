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

### Verse 1 (Vaivtpuran 16.3594)
- **Original**: पत्नीके रूपमें उसका सतीत्व भज्ज हो गया। यद्यपि पश्चात्‌ बह तुरंत रथपर सवार हो गया और
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3595)
- **Original**: तत्त्वरूपसे तो वह श्रीहरिकी परम प्रेयसी पत्नी भगवान्‌ शिवके साथ युद्ध करने लगा। ब्रह्मन्‌! ही थी।) ठीक इसी समय शंकरने शड्डचूड़पर उस समय शिव और शह्लुचूड़में बहुत लंबे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3596)
- **Original**: चलानेके लिये श्रीहरिका दिया हुआ त्रिशूल कालतक युद्ध होता रहा। कोई किसीसे न जीतते
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3597)
- **Original**: हाथमें उठा लिया। बह त्रिशूल इतना प्रकाशमान थे और न हारते थे। कभी समयानुसार शब्भुचूड़
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3598)
- **Original**: था, मानो ग्रीष्म-ऋतुका मध्याह्कालीन सूर्य हो, शस्त्र रखकर रथपर ही विश्राम कर लेता और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3599)
- **Original**: अथवा प्रलयकालीन प्रचण्ड अग्रि। वह दुर्निवार्य, कभी भगवान्‌ शंकर भी शस्त्र रखकर वृषभपर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3600)
- **Original**: दुर्धर्ष, अव्यर्थ और शत्रुसंहारक्क था। सम्पूर्ण ही आराम कर लेते। शंकरके बाणोंसे असंख्य
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3601)
- **Original**: शस्त्रोंके सारभूत उस त्रिशूलकी तेजमें चक्रके दानबोंका संहार हुआ। इधर संग्राममें देवपक्षके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3602)
- **Original**: साथ तुलना कौ जातो थी। उस भवंकर त्रिशूलको जो-जो योद्धा मरते थे, उनको विभु शंकर पुनः
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3603)
- **Original**: शिव अथवा केशव-ये दो ही उठा सकते थे। जीवित कर देते थे। उसी समय भगवान्‌ श्रीहरि
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3604)
- **Original**: अन्य किसीके मानका बह नहीं था। बह साक्षात्‌ एक अत्यन्त आतुर बूढ़े ब्राह्मणका बेष बनाकर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3605)
- **Original**: सजीव ब्रह्म ही था। उसके रूपका कभी परिवर्तन युद्धभूमिमें आग्रे और दानवराज शह्डुचूड़से
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3606)
- **Original**: नहीं होता और सभी उसे देख भी नहीं पाते कहने लगे। थे। नारद! अखिल ब्रह्माण्डका संहार करनेकी वृद्ध ब्राह्मणके वेषमें पधारे हुए श्रीहरिने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3607)
- **Original**: उस त्रिशूलमें पूर्ण शक्ति थी। भगवान्‌ शंकरने कहा--राजेन्द्र
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3608)
- **Original**: तुम मुझ ब्राह्मणको भिक्षा देनेकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3609)
- **Original**: लीलासे ही उसे उठाकर हाथपर जमाया और कृपा करो। इस समय सम्पूर्ण शक्तियाँ प्रदान
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3610)
- **Original**: शह्लुचूड़पर फेंक दिया। तब उस बुद्धिमान्‌ नरेशने करनेकी तुममें पूर्ण योग्यता है। अत: तुम मेरी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3611)
- **Original**: सारा रहस्य जानकर अपना धनुष धरतीपर फेंक अभिलाषा पूर्ण करो। मैं निरीह, तृषित एवं वृद्ध
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3612)
- **Original**: दिया और वह बुद्धिपूर्वक योगासन लगाकर ब्राह्मण हूँ। पहले तुम देनेके लिये सत्य प्रतिज्ञा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3613)
- **Original**: भक्तिके साथ अनन्य-चित्तसे भगवान्‌ श्रीकृष्णके कर लो, तब मैं तुमसे कहूँगा। चरणकमलका ध्यान करने लगा। त्रिशूल कुछ राजेन्द्र शब्भचचूड़ने अत्यन्त प्रसन्न होकर
- **Translation**: 

---

