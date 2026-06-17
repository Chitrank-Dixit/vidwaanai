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

### Verse 1 (Vishnu Puran 0.8161)
- **Original**: इस प्रकार सैकड़ों हजार पुरुषोंकी संख्यावाले यदुकुलको सन्तानोन्गे गणना सौ बर्षमें भी नहीं कौ जा सकती
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8162)
- **Original**: क्योंकि इस विधयपमें ये दो उल्प्रेक चरितार्थ है---
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8163)
- **Original**: जो गृहाचार्य यादवकुमाशेक््रे धनुर्विद्याकी शिक्षा देनेमें तत्पर रहते थे उनकी संख्या तीन करोड़ अद्ठासी लाख थी, फिर उन महात्मा यादबॉकी गणना तो कर ही कौन सकता है ? जहाँ हजारों और लाखोंकी संख्यामें सर्वदा यदुग़ाज डग्रसेन रहते थे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8164)
- **Original**: देबासुर-संग्राममें जो महाबल्त्रै दैल्वगण मारे गये थे जे मनुष्यल्तेकमें उपद्रव करनेवाले राजालोग होकर उत्पन्न हुए
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8165)
- **Original**: उनका नाश करनेके लिये देवताओंने यदुवज्ञमें जन्म लिया जिसमें कि एक सौ एक कुछ थे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8166)
- **Original**: उनका नियन्लण और स्वामित्न भगवान्‌ किष्णुने हो किया। वे समस्त यादबगण उनकी आज्ञातुसार ही वृद्धिको प्राप्त दुए
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8167)
- **Original**: इस प्रकार जो पुरुष इस वृष्णिवंशकी उत्पत्तिके विवरणकों सुनता है यह सम्पूर्ण पाषोंसे मुक्त होकर विष्णुलोकक्े प्राप्त कर लेता है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8168)
- **Original**: न औ -चततस इति श्रीविष्णुपुराणे चतुर्येघद्ो पह्रद्योध्यायः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8169)
- **Original**: अ0 16, 17, 18 ] चतुर्थ अंश 287 सोलहवाँ अध्याय तुर्वसुके ब॑ंशका वर्णन श्रीपयशर उवाच श्रीपराशरजी बोले-- इस प्रकार मैंने तुमसे संक्षेपसे इत्येष समासतस्ते यदोर्वश: कथित:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8170)
- **Original**: यदुके बंशका वर्णन किया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8171)
- **Original**: अब तुर्वसुके यंशका अथ तुर्वसोर्यवशमवधारय
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8172)
- **Original**: तुर्वसोर्वह्नि-
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8173)
- **Original**: वर्णन सुनों
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8174)
- **Original**: तुर्वसुका पुत्र वह्तिं था, यहिक्त भार्ग, रात्मजः,.. वह्लेर्भार्गो भार्गद्धानुस्ततश्ल
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8175)
- **Original**: भार्गका भानु, भानुका त्रयौसानु, जरयीसानुका करदम और त्रयीसानुस्तस्माध्च करन्दमस्तस्थापि मरुत्त:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8176)
- **Original**: कर्दमका पुत्र सरुत था
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8177)
- **Original**: मरुत्त निस्सत्तान सोअनपत्यो3भकत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8178)
- **Original**: ततश्च पौरवं दुष्यन्त
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8179)
- **Original**: इसल्ल्यि उसने पुरुवंशीय दुष्यन्तको पुत्ररूपसे पुत्रमकल्पयत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8180)
- **Original**: एवं ययातिशापात्तदूँदा:
- **Translation**: 

---

