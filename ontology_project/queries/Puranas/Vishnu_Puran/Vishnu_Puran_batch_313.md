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

### Verse 1 (Vishnu Puran 0.6241)
- **Original**: फिर दूसरे जञअमें काक-योनिको प्राप्त होनेपर घी अपने पतिको योगवलसे पाकर उस सुन्दरीने कहा---
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6242)
- **Original**: “हे प्रधो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6243)
- **Original**: जिनके लशोधूत होकर सम्पूर्ण सामन्तगण नाना प्रकारकी वस्तुएँ भेंट करते थे वही आप आज काक- योनिको प्राप्त होकर अलिभोजी हुए हैं”
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6244)
- **Original**: इसी प्रकार काक-योनिमें भी पूर्वजच्पका स्मरण कराये जानेपर राजाने अपने प्राण छोड़ दिये और फिर मयूर-योनिमें जन्म ह्या
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6245)
- **Original**: भी काशिराजकी कन्या उसे क्षण- क्षणमें अति सुन्दर मयूरोचित आहार देती हुई उसकी टहल करने लगी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6246)
- **Original**: उस समय राजा जनकने अश्रवमेध नामक महायज्ञका अनुष्ठान किया; उस यज्ञमें अवभूथ-खानके समय उस मयूरकों स्नान कराया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6247)
- **Original**: तब उस सुत्दरीने स्वयं भी स्त्रान कर राजाकों यह स्मरण कराया कि किस प्रकार उसने श्वान और श्रृगाल आदि योनियाँ ग्रहण की थीं। 86
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6248)
- **Original**: अपनी जन्म-परम्पराका स्मरण होनेपर उसने अपना जारीर त्याग दिया और फिर महात्वा जनकजोके यहां ही पुत्ररूपसे जन्म लिया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6249)
- **Original**: तब उस सुन्दरीने अपने पिताकों विवाहरके लिये प्रेरित किया । उसकी प्रेरणासे गजाने उसके स्वयँखरका आयोजन किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6250)
- **Original**: स्वयेघर होनेपर उस राजकन्याने स्वयंवरमें आये हुए अपने उस पतिको फिर पतिभावसे वरण कर लिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6251)
- **Original**: उस ण्जकुमारने कादियाजसुताके साथ नाना प्रकारके भोग भोगे और फिर पिताके परस्लोकवासी होनेपर विदेहनगरका राज्य किया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6252)
- **Original**: उसने बहुत-से यज्ञ किये, याचकॉगत्रे नाना प्रकारसे दान दिये, बल्रत-से पुत्र उत्पन्न किये और शलब्रुओंके साथ अनेव्यें युद्ध किये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6253)
- **Original**: इस प्रकार उस राजाने पृथिवीका न्यायानुकूछ पालन करते हुए राज्य- भोग किया और अत्तमें अपने प्रिय प्राणोंकों धर्मयुझमें
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6254)
- **Original**: आ 18 ] ततश्चितास्थं त॑ भूयो भरत्तरिं सा शुभेक्षणा । अन्वारुरोह विधिवद्मथापूर्व मुदान्यिता
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6255)
- **Original**: एप पाषण्डसप्भाषाददेषः प्रोक्तो मया द्विज । तथाअश्चमेधावभूथरन्नानमाहात्प्यमेज 98 किं पुनर्यस्तु सन्त्यक्ता त्रयी सर्वात्मिना द्विज । पाषण्डभोजिभि: पापैजेंदबादविरोधिभि:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6256)
- **Original**: 99 50 येषां सम्भाषणात्पुंसां दिनपुण्य प्रणश्यति
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6257)
- **Original**: 103 एसे पाषण्डिन: पापा न होतानाल्पेद बुध: । पुण्य नश्यति सम्भाषादेतेषां तद्दिनोद्धलप्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6258)
- **Original**: 104 पुंसां जयधरणमौण्ड्यवता वृथैव मोघाशिनामखिलशौचनिराकृतानाम्‌ । सुतीय अंश रेर5 छोड़ा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6259)
- **Original**: तब्र उस सुल्मेचनाने पहलेके समान फिर चितारूद पतिक्य विधिपूर्वक प्रसन्न-मनसे अनुगमन किया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6260)
- **Original**: इससे वह राजा उस ग़जकत्याके सहित इन्द्रलोकसे भी उत्कृष्ट अक्षय लोकोंका प्राप्त हुआ
- **Translation**: 

---

