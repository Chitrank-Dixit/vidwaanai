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

### Verse 1 (Vishnu Puran 0.10681)
- **Original**: आप ही समुद्र है, आप हो पर्यत है, आप ही नदियाँ हैं और आप ही यन हैं तथा आप ही पृथिवी, आकाश, वायु, जल, अप्रि और मन है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10682)
- **Original**: आप ही बुद्धि, अब्याकुत, प्राण और प्राणोंक्र अधिष्ठाता पुरुष हैं; तथा प्रुष्से भी परे जो व्याफ्क और जन्प तथा विकारसे शुन्य तत्त्त है वह भी आप ही हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10683)
- **Original**: जो झब्दादिसे रहित, अजर, अमेय, अक्षय और नाज तथा वृद्धिसे रहित है वह
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10684)
- **Original**: 376 त्वत्तोईमरास्सपितरो. यक्षगन्धर्वकिन्नरा: । मनुष्या: पश्षव: खगा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10685)
- **Original**: 35 सरीसूपा मृगास्सवें त्वत्तस्सवें महीरुहा: । य्व भूर्त भविष्य चर किझ्निदत्र चराचरम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10686)
- **Original**: 36 मूर्तामूत तथा चापि स्थूल्॑ सुक्ष्मतर॑ तथा । तत्सवे ते जगत्कतो नास्ति कि ख़ित्तया बिना
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10687)
- **Original**: 37 प्रया संसारचक्रेउस्मिन्ध्रमता भगवन्‌ सदा । तापत्रयाभिभूतेन न प्राप्ता निर्वेत्ति: क्रचित्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10688)
- **Original**: 38 “न 23 &--+++ जलाशवा। मया नाथ गृहीतानि तानि तापाय मे5भवन्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10689)
- **Original**: 39 राज्यपुर्वी बले कोशो मित्रपक्षस्तथात्मजा: । आया भृत्यजनो ये च शब्दाद्या विषया: प्रभो
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10690)
- **Original**: 40 सुखबुद्धया मया सर्व गृहीतमिदमव्ययम्‌ । परिणाम तदेवेश तापात्मकमभून्मम
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10691)
- **Original**: 49 देवलोकगर्ति त्राप्तो नाथ देवगणो5पि हि। म्त्तस्साहाव्वकामोभूच्छाश्नती कुत्र निर्वेति:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10692)
- **Original**: 42 त्वामनाराध्य जगता सर्व्धा प्रभवास्पदम । ज्ञाश्वती प्राप्यते केन परमेश्वर निर्वेति:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10693)
- **Original**: 43 त्वन्मायामूढमनसो जम्ममृत्युजरादिकान्‌ । अवाप्य तापान्यइ्यन्ति प्रेतराजमनन्तरम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10694)
- **Original**: 44 ततो निजक्रियासूति नरकेष्बतिदारुणम्‌। अ्राधुवन्ति नरा दुःखमस्वरूपविदस्तब
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10695)
- **Original**: 45 अहमत्यन्तविषयी प्रोहितस्ततव पमायया । ममत्वगर्वगर्त्तान्तर्थ्रमामि परमेश्वर
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10696)
- **Original**: 46 सो5हं॑ त्वां. शरणमपारमप्रमेय॑ सम्प्राप्त: परमपद यतो न किश्लित्‌ । संसारध्रमपरितापतप्नचेता निर्वाणे परिणतधाप्रि साभिलाष:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10697)
- **Original**: 47 श्रीविष्ण॒ुपुराण [ अ*« 23 आद्यन्तहीन बच्य भी आप ही हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10698)
- **Original**: आपडीसे देवता, पितृगण, यक्ष, गन्धर्व, किन्नर, सिद्ध और अप्सपगण उत्पन्न हुए हैं। आपहीसे मनुष्य, पत्ञु, पक्षी, सरोसृप और मृष आदि हुए हैं तथा आपहीसे सम्पूर्ण वृक्ष और जो कुछ भी भूत-भविष्यत्‌ चराचर जगत्‌ है वह सब हुआ है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10699)
- **Original**: हे प्रभो ! मूर्त-अमूर्त, स्थूछ-सूक्ष्म तथा और भी जो कुछ है वह सब आप जगत्‌कर्ता हो हैं, आपसे भिन्न और कुछ भी नहीं है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10700)
- **Original**: है भगवन्‌! तापत्रयसे अभिभूत होकर सर्वदा इस संसार-चक्रमें भ्रमण करते हुए मुझे कभी शान्ति प्राप्त नहीं हुई
- **Translation**: 

---

