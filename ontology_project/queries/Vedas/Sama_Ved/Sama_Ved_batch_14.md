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

### Verse 1 (Sama Ved 0.261)
- **Original**: बीर पुत्र की प्राप्ति के लिए मनुष्य अग्नि को प्रदीप्त करे और संदा हवनीय पदार्थों का प्रयोग करके, दिव्य सुख प्राप्त करने का मार्ग प्रशस्त करे
- **Translation**: 

---

### Verse 2 (Sama Ved 0.262)
- **Original**: 83.त्वेषस्ते धूम ऋण्वति दिवि सउ्छुक्र आततः
- **Translation**: 

---

### Verse 3 (Sama Ved 0.263)
- **Original**: सूरो न हि दुता त्वं कृपा पावक रोचसे
- **Translation**: 

---

### Verse 4 (Sama Ved 0.264)
- **Original**: प्रदीष्त होने के पश्चात्‌ अग्नि का धवल धूम, अंतरिक्ष में फैलता हुआ अनुभव होता है । हे पावन अग्ने ! सूर्य के समान, स्तुति के प्रभाव से आप प्रकाशित होते हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.265)
- **Original**: 84 .त्वं हि क्षैतवद्यशो5ग्ने मित्रो न पत्यसे । त्वं विचर्षणे श्रवो वसो पुष्टिं न पुष्यसि
- **Translation**: 

---

### Verse 6 (Sama Ved 0.266)
- **Original**: सर्वद्रषशठ, सभी को आश्रय प्रदान करने वाले, सूर्य के समान (तेजस्वी) अग्निदेव, आप सम्रिधारूप अन्न को ग्रहण करके, उसे प्रचुर मात्रा में परिपुष्ट करते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.267)
- **Original**: 85. प्रातरम्नि: पुरुप्रियो विश स्तवेतातिथि: । विश्वे यस्मिन्नमर्त्यें हव्यं मर्तास इन्धते
- **Translation**: 

---

### Verse 8 (Sama Ved 0.268)
- **Original**: परम प्रिय लगने वाले, सभी मनुष्यों के घरों में अतिथि स्वरूप, प्रात: स्मरणीय, अमरणशील अग्नि में सभी लोग हविष्यानों से आहति प्रदान करते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.269)
- **Original**: 86. यद्वाहिष्ठ॑ तदग्नये बृहदर्च विभावसो। महिषीव त्वद्रयिस्त्वद्वाजा उदीरते
- **Translation**: 

---

### Verse 10 (Sama Ved 0.270)
- **Original**: अभ्निदेव की शाघ्र प्रभावकारी स्तोत्रों से स्तुति की जाती है। वे दीप्तिमान्‌ अग्निदेव, हमें अपरिमित घन-धान्य एवं अन्न प्रदान करने की कृपा करें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.271)
- **Original**: 87, विशोविशो वो अतिर्थि वाजयन्त: पुरुप्रियम्‌। अर्मिन वो दुर्य॑ वचः स्तुषे शूघस्य मन्मभि:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.272)
- **Original**: अनन एवं बल चाहने वाले, हे मनुष्यो ! सर्वप्रिय एवं सर्वपूज्य अग्निदेव की स्तुति करो । हम (ऋ्रत्विग्गण) भी इन (गृहपति) अग्निदेव की सुखदायक स्तोत्रों से स्तुति करते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.273)
- **Original**: 8<. बृहद्वयो हि भानवे3र्चा देवायाग्नये । य॑ मित्र॑ न प्रशस्तये मर्तासो दधिरे पर:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.274)
- **Original**: पूर्वार्चिक आस्नेयपर्वणि प्रधमो5ष्याय: 1.13 याजकगण मित्र के समान, तेजस्वी अग्निदेव को, स्तुति के लिए अपने सम्मुछ स्थापित करके, उससें प्रचुर मात्रा में हविष्यान्न की आहुति प्रदान करते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.275)
- **Original**: 89. अगन्म वृत्रहन्तम॑ ज्येष्ठमग्निमानवम्‌ । यः सम श्रुतर्वन्नाक्षे बृहदनीक इथ्यते
- **Translation**: 

---

### Verse 16 (Sama Ved 0.276)
- **Original**: ऋक्षपुत्र श्रुतर्वा के (संहार के) लिए , प्रचण्ड ज्वालाओं वाली, वृत्र संहारक, श्रेष्ठ मनुष्यों के लिए हितकारी, अभ्निदेव का हम वरण (उपासना) करते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.277)
- **Original**: 90, जात: परेण धर्मणा यत्सवृद्धि: सहाभुवः । पिता यत्कश्यपस्याग्नि: श्रद्धा माता मनु: कवि:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.278)
- **Original**: जिन अग्निदेव के पिता कश्यप, माता श्रद्धा एवं स्तोता 'मनु' हैं, वे उत्तम कर्मों के द्वारा प्रारम्भ किये गये यज्ञ में प्रकट होते हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.279)
- **Original**: इति नव: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.280)
- **Original**: दशम: खण्ड:
- **Translation**: 

---

