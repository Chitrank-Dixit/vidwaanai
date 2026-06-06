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

### Verse 1 (Vishnu Puran 0.5121)
- **Original**: अन्योद्वेगकर वापषि तोष्यते तेन केशवः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5122)
- **Original**: 13 परदारपरद्रव्यपरहिंसास यो रतिम । न करोति पुमान्भूष तोष्यते तेन केशव:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5123)
- **Original**: 14 न ताडयति नो हन्ति प्राणिनोःन्यांश्र देहिन: । यो मनुष्यों मनुष्येन्द्र तोष्यते लेन केशवः शा 5 कर नल नजन
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5124)
- **Original**: 15 देवद्विजगुरूणां चल तोच्यते तेन गोविन्दः पुरुषेण नरेश्वर
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5125)
- **Original**: 16 इलकाय सजप उस कक अप च् हक न यस्तथा । सुखम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5126)
- **Original**: 27 ककककाल कन्‍्कसक गन सकत रागादिदोषेण न दुए्ट नृप मानसम्‌।
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5127)
- **Original**: 18 पक कण नयबाय बाबा ये धर्माइशास्रोक्ता नृपसत्तम । तेषु तिष्ठन्नरो नान्यथा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5128)
- **Original**: 19 स्रगर उकाच तदह श्रोतुमिच्छामि वर्णधर्मानशेषतः । तथैवाश्रम्रधर्माश्ष द्विजवर्य ब्रवीहि तान्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5129)
- **Original**: 20 ऑर्वउवाच ब्राह्मणक्षत्रियविज्ञां शुद्राणां च यथाक्रमम्‌ । त्वमेकाग्रमतिर्भूत्वा श्रृणु धर्मान्ययोदितान्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5130)
- **Original**: 21 दान॑ द्य्ाचजेददेवान्यजैस्स्वाध्यायतत्यर: । नित्योदकी भवेद्विप्र: कुर्याचचाप्निपरिप्रहम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5131)
- **Original**: 22 आढ्णि रल्ले चर पारक्ये समबुद्धिर्भवेद द्विज: । ऋतावभिगम: पत्यां शस्यते चास्य पार्थिव ।। 25 अतः सदाचासयुक्त पुरुष अपने वर्णके लिये विहित
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5132)
- **Original**: धर्मका आचरण करते हुए श्रीजनार्दनहीकी उपासना करता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5133)
- **Original**: हे पृथिवीपते ! ब्रह्मण, क्षत्रिय, वैश्य और अपने-अपने धर्मका पालन करते हुए ही विष्णुकी आराधना करते हैं अन्य प्रकारसे नहीं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5134)
- **Original**: जो पुरुष दूसरोंकों निन्‍दा, चुगली अथवा मिथ्याभाषण नहीं करता तथा ऐसा बचन भी नहीं बोलता जिससे दूसरोंको खेट हो, उससे निश्चय ही भगवान्‌ केशव प्रसन्न रहते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5135)
- **Original**: हे राजन्‌ ! जो पुरुष दूसरोंकी स्त्री, घन और हिंसामें रुचि नहीं करता उससे सर्वदा ही भगवान्‌ केदाव सन्तुष्ट रहते हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5136)
- **Original**: हे केन्द्र ! जो मनुष्य ! किसी प्राणी अथवा [ वृद्षादि ] अन्य देहघारियोंको पीड़ित अथवा नष्ट नहीं करता उससे श्रीकेदाव सन्तुष्ट रहते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5137)
- **Original**: जो पुरुष देवता, ब्राह्मण और गुरुजनोंकी सेवामें सदा तत्पर रहता है, हे नरेश्वर
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5138)
- **Original**: उससे गोजिन्द सदा प्रसन्न रहते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5139)
- **Original**: जो व्यक्ति स्वये अपने और अपने पुत्रोकि समान ही समस्त प्राणियाँका भी हित-चित्तक होता है वह सुगमतासे ही श्रीहरिकों प्रसन्न कर लेता है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5140)
- **Original**: हे नृप ! जिसका चित्त रागादि दोषोंसे दूषित नहीं है उस विशुद्ध-चित्त पुरुषसे भगवान्‌ किष्णु सदा सन्तुष्ट रहते हैं
- **Translation**: 

---

