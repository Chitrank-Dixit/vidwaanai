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

### Verse 1 (Vishnu Puran 0.8361)
- **Original**: उससे दो भागॉमें बैंट जानेके कारण पुत्र और पुत्रीरूप दो सच्चानें उत्पन्न हुईै
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8362)
- **Original**: उन्हें मुगयाके लिये गये हुए राजा जान्तनु कृपावण के आये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8363)
- **Original**: तदनत्तर पुत्रका नाम कृप हुआ और कन्या अश्वस्थामाको माता द्रोणाचार्यकी पत्नी कृपी हुई
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8364)
- **Original**: दिवोदासका पुत्र मित्रायु हुआ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8365)
- **Original**: मित्रायुका पुत्र च्यत्वन नामक राजा हुआ, च्यबनका सुदास, सुदासका सौदास, सौदासका सहदेव, सहदेवका सोमक और सोमकके सौ पृत्र हुए जिनमें जन्तु सबसे बड़ा और पृषत सबसे छोटा था। पृषतका पुत्र ट्रंपद, ड्रपदका धृष्टदयुप्र और घृट्टयुप्तका पुत्र घृष्वकेतु था।
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8366)
- **Original**: 70--73
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8367)
- **Original**: 292 श्रीकिष्णुपुराण [ आ+ 20 अजमीढस्यथान्य ऋशक्षनामा पुत्रो5भवत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8368)
- **Original**: तस्थ संवरण:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8369)
- **Original**: संवरणात्कुरु:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8370)
- **Original**: य॒ डु्द धर्मक्षेत्र कुरुक्षेत्र चकार।
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8371)
- **Original**: सुधनुर्जहपरीक्षित्ममुखा: कुरो: पुत्रा बभूबु:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8372)
- **Original**: सुधनुषः पुमत्रस्सुझोत्रस्तस्माच्व्यवन इच्यवनात्‌ कृतकः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8373)
- **Original**: ततश्लोपरिचरो बसु
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8374)
- **Original**: बृहद्रथप्रत्यग्रकुशाम्बकुचेलमात्य- प्रमुखा ब्सो: पुत्रास्सप्ताजायन्त
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8375)
- **Original**: बृहद्रथात्कुझागः . कुशाआद्बवृषभो. वृषभात्‌ पुष्पवान्‌ तस्मात्सत्यहितस्तस्मात्सुधन्वा तस्य व जतु:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8376)
- **Original**: बृह॒द्रथाशान्यशझकलद्दयजन्पा जरया संहितो जरासन्धनामा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8377)
- **Original**: तस्मात्सहदेव स्सहदेवात्सोमपस्ततश्च श्रुतिअ्रवा:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8378)
- **Original**: इत्येते प्रया मागधा भूपाछा: कथिता:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8379)
- **Original**: अजमीढका ऋश्ष नामक एक पुत्र और था
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8380)
- **Original**: उसका पुत्र संतरण हुआ तथा संवरणका पुत्र कुरू था जिसने क्रि अधर्मक्षेत्र कुरुक्षेत्रीी स्थापना को
- **Translation**: 

---

