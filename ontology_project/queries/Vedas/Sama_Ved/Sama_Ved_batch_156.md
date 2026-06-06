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

### Verse 1 (Sama Ved 0.3101)
- **Original**: पवित्र होकर कलशों में अवस्थित सोमरस में चन्द्रमा के श्रेष्ठ गुणों का संचार होता है
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3102)
- **Original**: 1201. प्र वाचमिन्दुरिष्यति समुद्रस्याधि विष्टपि
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3103)
- **Original**: जिन्वन्कोशं मथुश्चुतम्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3104)
- **Original**: मधुर रस सोम, आकाश (घटाकाश) में प्रवेश कर शब्द करता हुआ कलश को पूरी तरह भर देता है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3105)
- **Original**: 1202. नित्यस्तोत्रो वनस्पतिर्थेनामन्त: सबर्दुघाम्‌ । हिन्वानो मानुषा युजा
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3106)
- **Original**: नित्य स्तुत्य, बन-के स्वामी सोमदेव, श्रेष्ठ मनुष्यों को संगठित होने की प्रेरणा प्रदान करें और मधुरभाषी की हार्दिक स्तुतियों को स्वीकार करें
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3107)
- **Original**: 1203. आ पवमान धारया रवि सहस्लवर्चसम्‌। अस्मे इन्दो स्वाभुवम्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3108)
- **Original**: हे शुद्ध होने वाले सोमदेव ! आप हमें सहस्ल गुण सम्पन्न अपने धाम और ऐश्वर्य का अधिकारी बनाएँ
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3109)
- **Original**: द्र्ड सामवेद-संहिता 1204. अभि प्रिया दिवः कविर्विप्र: स धारया सुतः । सोमो हिन्वे परावति
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3110)
- **Original**: श्रेष्ठ स्थान पर रहने वाले (ज्ञान प्रेरक) ज्ञानी की तरह, चुलोक में रहने वाला सोम, त्रिय स्थानों (यज्ञस्थलों) की ओर श्रेष्ठ प्रेरणाओं का संचार करता है
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3111)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3112)
- **Original**: के के के
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3113)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3114)
- **Original**: 1205. उत्ते शुष्पास ईरते सिन्धोरूमेंरिव स्वनः । वा'गस्य चोदया पविम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3115)
- **Original**: हे सोमदेव ! आपके बेग से प्रवाहित होने से समुद्र की तरंगों जैसी ध्वनियाँ प्रकट होती हैं। आप वाणी से उत्पन्न शब्दों को प्रेरित करें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3116)
- **Original**: 1206. प्रसवे त उदीरते तिस्नो बाचो मखस्युव: । यदव्य एपि सानवि
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3117)
- **Original**: हे सोमदेव ! आपके प्रादुर्भाव के बाद याजकवृन्द ऋकछ-यजु, साम के मंत्रों का गान करते हैं, तब आप उच्च आसीन होकर संस्कारित होने के लिए तत्पर हो जाते हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3118)
- **Original**: 1207. अव्या वार: परिप्रियं हरि हिन्वन्त्यद्रिभि:। पवमानं मधुश्चुतम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3119)
- **Original**: । क््रत्विग्गण पाषाणों से कूटे गये, हरिताभ, सुन्दर मधुर सोमरस को (ऊन से बने) छनने से छानते हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3120)
- **Original**: 1208, आ पवस्व मदिन्तम पवित्र धारया कवे । अर्कस्य योनिमासदम्‌
- **Translation**: 

---

