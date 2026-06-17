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

### Verse 1 (Sama Ved 0.401)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.402)
- **Original**: 135. इह्ेव श्रृण्व एषां कशा हस्तेषु यद्वदान्‌ । नि याम॑ चित्रमूझते
- **Translation**: 

---

### Verse 3 (Sama Ved 0.403)
- **Original**: मरुद्‌गणों के हाथों में स्थित चाबुकों से होने वाली ध्वनियाँ हमें सुनाई देत॑ हैं । जैसे, वे यहीं हो रहो हों । ये श्यनियाँ संघर्ष के समय असामान्य शक्ति प्रदर्शित करती हैं
- **Translation**: 

---

### Verse 4 (Sama Ved 0.404)
- **Original**: 136. इम उ त्वा वि चक्षते सखाय इन्द्र सोमिन: । पुष्टावन्तो यथा पशुम्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.405)
- **Original**: जिस प्रकार पशुपालक हाथ में घास लेकर स्नेहपूर्वक पशुओं की ओर देखता है, उसी प्रकार आपको तृप्त करने के लिए बाजक सोमादि हाथ में लेकर आपकी ओर देखते रहते हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.406)
- **Original**: 137.समस्य मन्यबे विशो विश्वा नमन्त कृष्टयः । समुद्रायेव सिन्धव:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.407)
- **Original**: समस्त प्रजाएँ (असुरों के प्रति) उग्र इद्धदेव के प्रति नमनपूर्वक उसी प्रकार आकर्षित होती हैं, जैसे कि सब नदियाँ समुद्र में मिलने के लिए देग से जाती हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.408)
- **Original**: 138. देवानामिदवो महत्तदा वृणीमहे वयम्‌
- **Translation**: 

---

### Verse 9 (Sama Ved 0.409)
- **Original**: वृष्णामस्मभ्यमूतये
- **Translation**: 

---

### Verse 10 (Sama Ved 0.410)
- **Original**: हे देवगण ! आपका संरक्षण हमारे लिए पूजनीय है । आप सभी कामनाओं को पूर्ण करने वाले हैं । आपके महिमामय संरक्षण को हम स्वीकार करते हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.411)
- **Original**: 139. सोमानां स्वरणं कृणुहि ब्रह्मणस्पते । कक्षीवन्तं य औशिज:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.412)
- **Original**: हे बह्मणस्पते ! सोमयज्ञ कर्ता, उशिज के पुत्र कक्षीवान्‌ को तेजस्विता प्रदान करें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.413)
- **Original**: 140.बोधन्मना इदस्तु नो बृत्रहा भूर्यासुति:। श्रृणोतु शक्र आशिषम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.414)
- **Original**: जिस देव के लिए बहुत से लोग सोमरस तैयार करते हैं, जो हमारी कामनाओं के ज्ञाता हैं, युद्ध क्षेत्र में शत्रुओं को पराजित करने वाले है । वे सामर्थ्यवान्‌ , वृत्र संहारक इ्धदेव हमारी स्तुतियों को ध्यान से सुनें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.415)
- **Original**: 141.अगद्या नो देव सवितः प्रजावत्सावी: सौभगम्‌। परा दुष्वप्यं सुव
- **Translation**: 

---

### Verse 16 (Sama Ved 0.416)
- **Original**: हे सवितादेव ! आप आज हमें पुत्र-पौत्रों सहित पवित्र ऐश्वर्य प्रदान करें । दुःखदायी स्वप्नों की तरह दरिद्रता को हमसे दूर करें ?
- **Translation**: 

---

### Verse 17 (Sama Ved 0.417)
- **Original**: 142. क्‍्य 3सय यृषभो युवा तुविग्रीवो अनानत:। ब्रह्मा कस्तं सपर्यति
- **Translation**: 

---

### Verse 18 (Sama Ved 0.418)
- **Original**: युवा, सशक्त ग्रीवा वाले एवं किसी के सामने न झुकने वाले, वे इन्द्र (परमेश्वर) इस समय कहाँ हैं ? कौन याजक उनका पूजन करता है ?
- **Translation**: 

---

### Verse 19 (Sama Ved 0.419)
- **Original**: र्ड सामवेद-संहिता 143. उपद्वरे गिरीणां सड्रमे च नदीनाम्‌
- **Translation**: 

---

### Verse 20 (Sama Ved 0.420)
- **Original**: धिया विप्रो अजायत
- **Translation**: 

---

