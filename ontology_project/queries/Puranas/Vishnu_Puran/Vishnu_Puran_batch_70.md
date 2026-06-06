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

### Verse 1 (Vishnu Puran 0.1381)
- **Original**: आ* 12 ] यद्धूत॑ यश्व वै भव्यं पुरुषोत्तम तद्धवान्‌। त्कत्तो विराट स्वराद सप्राट्‌ त्वत्तश्ाप्यधिपूरुष:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1382)
- **Original**: 57 अत्यरिच्यत सो5थश्च तिर्यगूर्धष्व तर जै भुजः । त्वत्तो विश्वपिदं जात॑ त्क्‍तो भूतभविष्यती
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1383)
- **Original**: 58 त्वद्रूपधारिणश्चान्तर्भूत॑ सर्वमिदं जगत्‌। त्वत्तो यज्ञ: सर्वहुत: पृषदाज्य पशुर्द्धिधा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1384)
- **Original**: 59 त्वत्त: ऋचो5थ सामानि त्वत्तइहन्दांसि जज़िरे । त्क्तो यजूंष्यजायन्त त्वत्तोड्श्चाश्लैकतों दतः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1385)
- **Original**: 60 गावस्त्वत्त: समुद्धृतास्त्वत्तोजजा अवयो मृगा: । त्वन्पुखादब्राह्मणास्त्वत्तों बाहो: क्षत्रमजायत
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1386)
- **Original**: 61 लैश्यास्तवोरुजा: श्रुद्रास्तव पद्भूयां समुद्गरता: । अध्ष्णो: सू्यो+निल: प्राणाच्न्द्रमा मनसस्तव
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1387)
- **Original**: 62 प्राणो5न्तःसुषिराजातो मुस्वादश्मिरजायत । नाभितो गगन॑ दौश्व शिरसः समवर्तत
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1388)
- **Original**: 83 दिल्ला: श्रोत्रात्क्षिति: पद्भयां त्वत्त: सर्वमभूदिदम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1389)
- **Original**: 64 न्यग्रोध: सुमहानल्पे यथा बीजे व्यवस्थित: । संयम विश्वमस्िलं खीजभूते तथा त्वयि
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1390)
- **Original**: 65 बीजादड्डरसम्भूतो न्‍्यग्रोधस्तु समुत्यित: । विस्तारं चर यथा याति त्वत्त: सृष्टो तथा जगत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1391)
- **Original**: 66 यथा हि कदली नान्या त्वकृपत्रादपि दृश्यते । एवं विश्वस्य नान्यस्त्वं त्वत्त्थायीश्वर दृश्यते
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1392)
- **Original**: 67 हादिनी सच्धिनी संवित्त्वय्येका सर्वसंस्थितो । ह्रादतापकरी मिश्रा त्वयि नो गुणवर्जिते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1393)
- **Original**: 68 पृथग्भूतेकभूताय भूतभूताय ते नमः । व्यक्त प्रधानपुरुषो बिरादसम्राट्स्वराट्तथा । विभाव्यतेउन्तःकरणे पुरुषेष्नक्षयो भवान्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1394)
- **Original**: 70 सर्वास्मिन्‍्सर्वभूतस्त्व॑ सर्ल: सर्वस्वरूपथुक्‌ । सर्व त्वत्तस्ततश्न त्वे नमः सर्वात्पिनेउस्तु ते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1395)
- **Original**: 79 भ्रथम अंबा डर है पुरुषोत्तम ! भूत और भविष्यत्‌ जो कुछ पदार्थ हैं ये सब आप ही हैं तथा विराट, स्वराट, सम्राट और अधिपुरुष (ब्रह्मा) आदि भी सब आपहीसे उत्पन्न हुए हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1396)
- **Original**: ये हो आप इस पृथिवीके नीचे-ऊपर और इधर-उधर सब ओर बढ़े हुए हैं। यह सम्पूर्ण जगत्‌ आपहीसे उत्पन्न हुआ है तथा आपसझेसे भूत और भविष्यत्‌ हुए हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1397)
- **Original**: यह सम्पूर्ण जगत्‌ आपके उअह्याप्डके अन्तर्गत है [
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1398)
- **Original**: फिर आपके अन्तर्गत होनेकी तो बात ही क्या है ] जिसमें सभो पुरोडाशॉक्)ा हसन होता है वह यज्ञ, पृषदाज्य (दधि और दूत) तथा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1399)
- **Original**: आम्य और वन्य ] दो प्रकारके पशु आपहोसे उत्पन्न हुए है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1400)
- **Original**: आपहीसे ऋक्‌, साम और गायत्री आदि छन्द प्रकट हुए हैं, आपल्ीसे यजुर्वेदका प्रादुर्भाव हुआ है और आपहोसे अश्च तथा एक ओर दाँतबाले महिष आदि जीच उत्पन्न हुए हैं
- **Translation**: 

---

