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

### Verse 1 (Markende Puran 0.1401)
- **Original**: क्रमशः दक्षिणायग और उत्तरायग है। हर प्रकार निश्चित्त सोते हैं। इस प्रकार सूर्रि, पालन और
- **Translation**: 

---

### Verse 2 (Markende Puran 0.1402)
- **Original**: मनुष्योंका एक वर्ष देखताओंका एन दिन रात संहार--इने तीनों कालों्म तोत रशर्णों से वक्त होकर
- **Translation**: 

---

### Verse 3 (Markende Puran 0.1403)
- **Original**: हैं। ठक्षम दिन तो उत्तरायण और राह दक्षिणाथन भो वे परमेश्वर बाक्ष्तमें नि[[/ ही हैं। जैसे
- **Translation**: 

---

### Verse 4 (Markende Puran 0.1404)
- **Original**: है। देवताआओंके बारह हजार वर्धोकों एक चतुर्जुगी खेतिहर पहले बीजको बोता, #र पौँधेकी रक्षा
- **Translation**: 

---

### Verse 5 (Markende Puran 0.1405)
- **Original**: होठों है, जिसे सत्ययूग, त्रेता आदि कहते हैं। ऋरता और अन्तपें खेती पक जानेपर ठसे काटता
- **Translation**: 

---

### Verse 6 (Markende Puran 0.1406)
- **Original**: अब इनका विभाग सुनों। चार हज़ार दिव्य है तथा इन कार्योक्के अनुसा! षोनेवाला, रक्षा
- **Translation**: 

---

### Verse 7 (Markende Puran 0.1407)
- **Original**: वर्षो सत्ययुग होता है, लार सरौ दिव्य भर्षोंकी करनेबाला और क्ारनेवाला-वें तौन नाप धारण
- **Translation**: 

---

### Verse 8 (Markende Puran 0.1408)
- **Original**: उसकी सर्या और उतने हीं वर्षो सन्ध्मांण करता है, उसी प्रकार एक ही परगेश्वर भिन्न-
- **Translation**: 

---

### Verse 9 (Markende Puran 0.1409)
- **Original**: होता हैं। हीन इजार दिव्य वर्षोका प्रेतायुग है। फिन्न कार्वोक्ते अनुसार ब्रह्मा, विष्णु ज़था रुद्र नाप
- **Translation**: 

---

### Verse 10 (Markende Puran 0.1410)
- **Original**: उसकी सब्ध्या और सब्ध्यांशका त्मय तीन-तोन धारण करते हैं। ब्रह।! होकर संसूरक्ती सृर्टि करते
- **Translation**: 

---

### Verse 11 (Markende Puran 0.1411)
- **Original**: सौ दिव्य वर्षोका हैं। दो हजार दिल्ल्य बर्षोका और रुद् होकर उसक्रा संहार करे ई तथा
- **Translation**: 

---

### Verse 12 (Markende Puran 0.1412)
- **Original**: झापरयुग होता हैं और दो-दो सी दिल्य ऋर्ष विप्णुरूपमें इन दोनों कार्योंसे उदासीन रहकर
- **Translation**: 

---

### Verse 13 (Markende Puran 0.1413)
- **Original**: उसको सच्ध्या तथा समन्ध्यांशके होते हैं। द्विजओष्ठ ! सबका पालन करते हैं; इस तरह स्ववम्भू
- **Translation**: 

---

### Verse 14 (Markende Puran 0.1414)
- **Original**: एक हजार दिव्य ब्र्मोका कलियुग होता है तथ' परमात्पाकी त्तीन अबस्थाएँ होते हैं। रजोगुणप्रधान
- **Translation**: 

---

### Verse 15 (Markende Puran 0.1415)
- **Original**: सौ सौ दिव्य वर्ष उसकी सन्ध्या एवं सन्ध्यांशके बअच्या, तमोगुणप्रधार रूद्र और स्वप्रथान दिश्ववालक
- **Translation**: 

---

### Verse 16 (Markende Puran 0.1416)
- **Original**: जताये गये हैं। इस प्रकार दिद्वानोंने बारह हजार विष्ण! हैँ। ये हो तीग देवता हैं और ये ही तोन
- **Translation**: 

---

### Verse 17 (Markende Puran 0.1417)
- **Original**: दिव्य नर्पोंक्ती एक चतुसुंगी बतायो है। एक हजार गुण हैं। ये परक््पर एक-दूसरेके आश्रित और
- **Translation**: 

---

### Verse 18 (Markende Puran 0.1418)
- **Original**: चतुर्युगों बीतनेपर ब्रह्माका एक दिन होता है। एक-दूसरेसे पिले रहते हैं। इननें एक का भी , ब्रह्म! ब्रह्माजीके एक दिनमें बारो श्रागैसे चौंदह बियोग नहीं होता। थे एक-दूस्रेका कणों त्यार
- **Translation**: 

---

### Verse 19 (Markende Puran 0.1419)
- **Original**: मनु होते हैं! देवता, सप्तर्षि, इत्र, मनु और नहीं करते। भनुपूत्र- थे सब्र लोग एक ही साथ उत्पन्न होते इस प्रकार जगशके आदिकारण देवाधिदेव
- **Translation**: 

---

### Verse 20 (Markende Puran 0.1420)
- **Original**: हैं और एक ही साथ इनका संहार भी होता है। चनुर्मुख बह्मजी रजोगुणका आक्रथ लेकर सृट्टिक
- **Translation**: 

---

