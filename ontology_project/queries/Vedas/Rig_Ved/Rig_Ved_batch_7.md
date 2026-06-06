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

### Verse 1 (Rig Ved 0.121)
- **Original**: 53. केतुं कृण्वन्नकेतवे पेशो मर्या अपेशसे
- **Translation**: 

---

### Verse 2 (Rig Ved 0.122)
- **Original**: समुषद्धिरजायथा:
- **Translation**: 

---

### Verse 3 (Rig Ved 0.123)
- **Original**: है मनुष्यों ! तुम रात्रि में निद्राभिभूत होकर, संज्ञा शून्य निश्वेष्ट होकर, प्रातः पुन: सचेत एवं सचेष्ट होकर मानों प्रतिदिन ववजीयन प्राप्त करते हो । (प्रति-दिन जन्म लेते हो)
- **Translation**: 

---

### Verse 4 (Rig Ved 0.124)
- **Original**: 54. आदह स्वधामनु पुनर्गर्भत्वमेरिरे । दधाना नाम यज्ञियम्‌
- **Translation**: 

---

### Verse 5 (Rig Ved 0.125)
- **Original**: यज्ञीय नाम वाले,धारण करते में समर्थ मरुत्‌ वास्तव में अन्न की (वृद्धि की) कामना से बार-बार (मेघ आदि) गर्भ को प्राप्त होते हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.126)
- **Original**: [यज़ में वायुभूत पदार्थ ेघ आदि के गर्ध में स्वापित होकर उर्वरता को बढ़ाते हैं।] 55. वील्ठु चिदारुजलुभिर्गुहा चिदिन्द्र वल्लिभि:। अविन्द उस्निया अनु
- **Translation**: 

---

### Verse 7 (Rig Ved 0.127)
- **Original**: हे इद्धदेव ! सुदृढ़ किले बन्दी को ध्वस्त करने में समर्थ, तेजस्वी मरुदूगणों के सहयोग से आपने गुफा में अवरुद्ध गौओं (किरणों) को खोजकर प्राप्त किया
- **Translation**: 

---

### Verse 8 (Rig Ved 0.128)
- **Original**: 56. देवयन्तो यथा मतिमच्छा विद्ठसुं गिर:। महामनूषत श्रुतम्‌
- **Translation**: 

---

### Verse 9 (Rig Ved 0.129)
- **Original**: देवत्व प्राप्ति की कामना वाले ज्ञानी ऋत्विज्‌ , महान्‌ यशस्वी, ऐश्वर्यवान्‌ बौर मरुदगणों की बुद्धिपूर्वक स्तुति करते हैं
- **Translation**: 

---

### Verse 10 (Rig Ved 0.130)
- **Original**: 57. इन्द्रेण सं हि दृक्षसे सब्जग्मानो अबिभ्युधा। मन्दू समानवर्चसा
- **Translation**: 

---

### Verse 11 (Rig Ved 0.131)
- **Original**: सदा प्रसन्‍न रहने वाले, समान तेज वाले मरुदगण निर्भय रहने वाले इन्द्रदेव के साथ (संगठित हुए) अच्छे लगते हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.132)
- **Original**: [ विधिन वर्गों के समान प्रतिभा - सम्पन व्यक्ति परस्पर सहयोग करें, तो समाज सुखी होता है । ] 58. अनवद्यैरभिद्युभि्मख: सहस्वदर्चति । गणैरिव्द्रस्य काम्यैः
- **Translation**: 

---

### Verse 13 (Rig Ved 0.133)
- **Original**: इस यज्ञ में निर्दोष , दीप्तिमान्‌ , इष्ट प्रदायक, सामर्थ्यवान्‌ मरुद्गणों के साथी इन्द्रदेव के सामर्थ्य की पूजा की जाती है
- **Translation**: 

---

### Verse 14 (Rig Ved 0.134)
- **Original**: 59. अतः परिज्मन्ना गहि दिवो वा रोचनादधि
- **Translation**: 

---

### Verse 15 (Rig Ved 0.135)
- **Original**: समस्मिन्नृज्ञते गिर:
- **Translation**: 

---

### Verse 16 (Rig Ved 0.136)
- **Original**: हे सर्वत्र गमनशील मरुद्गणों ! आप अन्तरिक्ष से, आकाश से अथवा प्रकाशमान च्युलोक से यहाँ पर आयें, क्योंकि इस यज्ञ में हमारी वाणियाँ आपकी स्तुति कर रही हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.137)
- **Original**: 60. इतो वा सातिमीमहे दिवो वा पार्थिवादधि
- **Translation**: 

---

### Verse 18 (Rig Ved 0.138)
- **Original**: इन्द्र महो वा रजसः
- **Translation**: 

---

### Verse 19 (Rig Ved 0.139)
- **Original**: इस प्रृथ्वी लोक, अन्तरिक्ष लोक अथवा च्ुलोक से - कहीं से भी प्रभूत धन प्राप्त कराने के लिये, हम इन्द्रदेव की प्रार्थना करते है
- **Translation**: 

---

### Verse 20 (Rig Ved 0.140)
- **Original**: 8 ऋग्वेद संहिता भाग-1 [ सूक्त -7 ] [ऋषि- मधुच्छन्दा वैश्वाभित्र । देवता- इन्द्र
- **Translation**: 

---

