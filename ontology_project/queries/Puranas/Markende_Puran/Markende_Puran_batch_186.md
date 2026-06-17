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

### Verse 1 (Markende Puran 0.3701)
- **Original**: अत्यन्त मनोहर पतली प्राप्त होगी और उसके गर्भसे एकाग्रचित्त होकर प्रणाम करता हूँ। उन्हें ऋप्रंजर
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3702)
- **Original**: युम्हें 'मनु' संज्ञक उत्तम पुतकी प्राप्ति होगी। वह
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3703)
- **Original**: 248 संक्षिप्त मार्कण्डेयपुरण + 9048 $ 0++5 77 _ / 7 । 5 # 0 ।।5 0
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3704)
- **Original**: हम 4. 3... &.).. है, ह,+ ह & & «, &,। 7 4 ,। । »,। 6 &.
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3705)
- **Original**: बुद्धिमात्‌ पुत्र मन्तरन्तरका स्वामी होगा और तुम्हारे
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3706)
- **Original**: होता है तथा ग्रोष्म-ऋतुमें पढ़े जानेपर भो यह उतने हो नामपर तीनों लोकॉंगें 'रौच्य' के नापसे उसकी
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3707)
- **Original**: ही वर्षोतक तृततिका साभ्रक होता है। रुचे! कर्षा- ख्याति होगी। उराके भी महाबलवान्‌ और पराक्रमी
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3708)
- **Original**: ऋतुमें किया हुआ श्राद्ध यदि किसी अज्जसे घिकल बहुत-रे महात्मा पुत्र होंगे, रो इस 1शवीका पालन दो तो भी इस स्तोह़के भाठसे पूर्ण होता हैं और कोंगे। धमंत्! तुभ शी प्रजापति होऋर चार उस श्राद्धसें हमें अक्षय तृप्ति होती है। शस्त्कालर्मे प्रकारकी प्रजा उत्पक्ष करोगे और फिर अपना भी श्राइ़्फके अवसरण यदि इसका पाठ हो तो यह अधिकार क्षीण होनेपर सिद्धिकों प्रत्रा होओगे। जो
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3709)
- **Original**: हें पंद्रह वर्ोत्कक्रे लिये तृप्ति प्रदान करता हैं। पनुष्ठ इस स्तेत्रसे भांक्तिपर्चक टमारो स्तुति करेगा,
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3710)
- **Original**: लिस परमें यह स्तोत्र सदा लिखकर रखा जाता उसके ऊपर रसतुष्ट होकर हमलोग उसे मनोवाज्छित
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3711)
- **Original**: है, कहाँ त्राद्ध करमेपर हमारी निश्चय हों उपस्थिति धोष तथा उत्तम आत्मज्ञन प्रदात करेंगे; जो नोरेग
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3712)
- **Original**: होती है; अतः महाध्वग! श्राद्धमें भोजन करनेवाले शरीर, धन और पुन्र-पौत आदिकों इच्छा करता हो,
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3713)
- **Original**: ब्राह्मणेके सामने सुम्हें यह स्तोष्न अलश्य सुनाना वह सदा एस स्तोत्ले हपलोगोंकों स्तुति करें। वह चाहिये; क्योंकि यह हमारों पृष्टि करनेबाला है। स्तोत्र हमलेगोंकी प्रसन्नता बढ़ानेबाल्ता है। जो श्राद्यमे.. मार्कण्डेयजी कहते हैं --ऋश्किजी
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3714)
- **Original**: तदनत्तर पोजन कलबाले श्रेष्ठ ब्राह्मणोंके सामने खड़ा हो। रुचिके समीप उस तदीके भीतरसे छरहरे अख्जोंवालों भक्तिपूर्ताक् इस स्तोन्रका पाट करेगा, उसके वहाँ
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3715)
- **Original**: मनोहर अप्सता ग्म्लोचा प्रकट हुई और महात्मा स्तेत्रश्नच्रणके प्रेमसे हम निश्रथ ही उपस्थित होंगे प और हमारे लिप किया हुआ श्राद्ध भों नि:सच्देह अक्षय ह
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3716)
- **Original**: !। अट्टे श्रोषियन द्राहाणसे रहित श्राद्ध हो, अहे बच्च क्रिसों दोषसे दूषित हो गया हो ऊरथवा अन्यायपरार्मित धगसे किया गया हो अथवा श्राद्धके लिये अयोग्य दूषित सामग्रियोंसे उसका अनुष्ठात हुआ हो. अनुचति क्षय या अयेग्य देशपें हुआ हो या उनमें विधिका उल्लफूलड किया गया हो अथया लोगोंगे बिता श्रद्धांफे या दिखावेके लिये किया हो तो भो बह श्राद्ध इस स्तोन्नके पप्टसे हपारी तुप्त हमें समर्थ होहा है। हपें सुख देनेवाल। यह स्त्ीत्र जहाँ श्राद्धपेँ पढ़ा जात' है, कहाँ हमलोगोंको बाज वर्णेतक बनो 2हनेजालों तृप्ति ग्राप होती यह स्तोन्न हेन्न्ल-ऋलुवें श्राउके अवसरपर सुनानेसे
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3717)
- **Original**: . हमें
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3718)
- **Original**: % कर्षोके लिये तुप्ति प्रदान कस्ता है। इसी
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3719)
- **Original**: ध्पटेा - > 52222. प्रकोर शिशिर ऋतुमें गढ़ ऋत्ण
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3720)
- **Original**: ।5 स्तोत्र हमें
- **Translation**: 

---

