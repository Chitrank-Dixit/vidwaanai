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

### Verse 1 (Vishnu Puran 0.241)
- **Original**: देवताओंके खारह हजार चर्षोकि सतयुग, त्रेता, द्वापर और कलियुग नामक चार युग होते हैं। उनका अलग-अलग परिमाण मैं तुम्हें सुनाता हूँ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.242)
- **Original**: पुरातत््वके जाननेवाले सतयुग आदिक्ा परिमाण क्रमग्ः चार, तीन, दो और एक हजार दिव्य वर्ष बतल्त्रते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.243)
- **Original**: प्रत्येक युगके पूर्व उतने ही सौ वर्षकी सम्ध्या खतायी जाती है और युगके पीछे उतने ही परिमाणवाले रच्यांदा होते हैं [ अर्थात्‌ सतयुग आदिके पूर्व क्रमशः चार, तीन, दो और एक सौ दिव्य बर्षकी सथ्याएँ और इतने हो वर्षके समध्याज्ञ होते है]
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.244)
- **Original**: हे मुनिश्रेष्ठ ! इन सन्ध्या और सब्ध्याशॉंके बीचका जितना काल होता है, डसे ही सतयुग आदि नामबाले युग जानना चाहिये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.245)
- **Original**: हे मुने ! सतयुग, त्रेता, द्वापर और कि ये मिलकर चतुर्युग कहलाते हैं; ऐसे हजार चतुर्युगका ब्रह्माका एक दिन होता है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.246)
- **Original**: हे ब्रह्मन्‌ ! ब्रह्माके एक दिनमें चौदह मनु होते हैं। उनका कालकृत परिमाण सुनो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.247)
- **Original**: सप्तर्षि, देवगण, इन्द्र, सनु और मनुके पुत्र राजालोग [ पूर्व- कल्पानुसार ] एक ही कालमें रचे जाते हैं और एक ही
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.248)
- **Original**: 10 अ्रीविष्णुपुराण ( अब्ड चतुर्युगाणां संख्याता साधिका होकसप्तति: । म्रन्वन्तर मनो: काल: सुरादीनां च सत्तम
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.249)
- **Original**: 18 अष्टो झत सहल्लाणि दिव्यवा संख्यया स्मृतम्‌ । द्विपश्लाज्ञत्तथान्यानि सहस्लाण्यधिकानि तु
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.250)
- **Original**: 19 प्रिश्त्कोट्यस्तु सम्पूर्णा: संख्याता; संख्यया द्विज । सप्रपष्टिस्तथान्यानि नियुतानि महामुने
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.251)
- **Original**: 20 विंशतिस्तु सहत्नाणि काल्लोइ्यमधिकं बिना । मन्वन्तरस्थ सद्भूयेय॑ मानुषैर्वत्सैर्टिज
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.252)
- **Original**: 21 चतुर्दशगुणो होष काल ब्राह्ममहः स्पृतम्‌। ब्राह्मो नेपित्तिको नाम तस्थान्ते प्रतिसज्चर:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.253)
- **Original**: 22 तदा हि दहाते सर्व त्रैल्म्रेक्य भूर्भुवादिकम । जन॑ प्रयान्ति तापाता महर््तेकनिवासिन:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.254)
- **Original**: 23 एकार्णवे तु त्रैल्लोक्ये ब्रह्मा नारायणात्मक: । भोगिशय्यां गत: शेते औैलोक्यग्रासबृंहित:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.255)
- **Original**: 24 जनस्थैयोंगिभिदेंवश्चिन्यमानो ब्जसम्भव: । तत्पमाणां हि तां रात्रिं तदन्ते सुजते पुन:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.256)
- **Original**: 25 एबं तु क्ह्मणो वर्षपेज वर्षझतं चर यत्‌। झतं हि तस्य वर्षाणां परमायुर्महात्ममः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.257)
- **Original**: 26 एकमस्य व्यतीतं तु परारीु ब्रह्मणोइनघ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.258)
- **Original**: तस्वात्ते3भून्महाकल्प: पाद्य इत्यभिविश्वुत:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.259)
- **Original**: 27 ब्वितीवस्य परार्दस्य वर्तमानस्य ले द्विज । वाराह इति कल्पोउ्य॑ प्रथम: परिकीर्तित:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.260)
- **Original**: 28 काल्में उनका संहार किया जाता है
- **Translation**: 

---

