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

### Verse 1 (Vishnu Puran 0.9741)
- **Original**: 9 साधित॑ कृष्ण देवानापहं मन्ये प्रयोजनम्‌। त्ववायमद्रिप्रवर: करेणैकेन यदधृत:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9742)
- **Original**: 10 गोभिश्व: चोदित: कृष्ण त्वत्सकाझ्मिहागतः । त्वया आ्राताभिरत्यर्थ युष्मत्सल्कारकारणात्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9743)
- **Original**: 11 स लां कृष्णाभिषेक्ष्यामि गवां वाक्यप्रचोदित: । उपेद्धत्वे गवापिन्द्रों गोविन्दस्त्वे भविष्यसि
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9744)
- **Original**: 12 श्रीपराज्षरजी खोलछे--इस प्रकार गोवर्धनपर्वतका धारण और गोकुरूकी रक्षा हो जानेपर देवराज इन्द्रको श्रोकष्णचच्द्रका दर्घन करनेकी इच्छा हुई
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9745)
- **Original**: अतः जात्रुजित्‌ देवराज गजग़ज गेशवतपर चढ़कर गोवर्धनपर्वतपर आये और वहाँ सम्पूर्ण जगतके रक्षक गोपवेषधारी महाबल्यान्‌.श्रीकृष्णचन्रको ग्वाल्यालोके साथ गौएँ चराते देखा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9746)
- **Original**: हे द्विज ! उन्होंने यह भी देखा कि पत्तिश्रेप्ठ गरुड अदुक्ष्यभावसे उनके ऊपर रहकर अपने पह्लेंसे उनको छाया कर रहे हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9747)
- **Original**: तब ये ऐराबत्से उतर पड़े और एकात्तमें श्रीमधुसूदनकी ओर प्रीतिपूर्वक दृष्टि फैलाते हुए मुसकाकर बोले
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9748)
- **Original**: इन्दने कहा--हे श्रीकृष्णचन्द्र ! मैं जिस लिये आपके पास आया हूँ, यह सुनिये--हे महाबाहों ! आप इसे अन्यथा न समझें
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9749)
- **Original**: हे अखित्मधार परमेश्रर आपने पृथिव्रीका भार उतारनेके लिये ही पृथिवीपर अवतार लिया है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9750)
- **Original**: यज्ञभंगसे विरोध सानकर ही मैंने गोकुछकों नष्ट करतेके ल्ल्यि महामेघोंकों आज्ञा दी थी, उन्हींने यह संहार मचाया था
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9751)
- **Original**: किन्तु आपने पर्वतको ठख्ाड़कर गौओंक्य्े यवा लिया। हे वीर ! आपके इस अद्भुत कर्मसे मैं अति प्रसन्न हूँ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9752)
- **Original**: है कृष्ण ! आपने जो अपने एक हाथपर गोवर्धन धारण किया है इससे मैं देवताओंका प्रयोजन [ आपके द्वारा ] सिद्ध हुआ ही समझता हूँ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9753)
- **Original**: [ गोबंहाकी रक्षाद्वार ] आपसे रक्षित [ कामघेनु आदि ] गौओसे प्रेर्ति होकर ही मैं आपका विशेष सत्कार करनेके लिये यहाँ आपके पास आया हूँ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9754)
- **Original**: हे कष्ण ! अब मैं गौओंके वाक्यानुसार ही आफ्का उपेन्द्र-पदपर अभिषेक करूँगा तथा आप गौओंके इन्द्र (स्तामी) हैं इसलिये आपका नाम “गोविन्द! भी होगा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9755)
- **Original**: 342 अश्रीविष्णुपुराण [ अ5 12 अऋपराशर उवाच अथोपवाह्यादादाय घण्टामैरावता दजात्‌ । अभिषेक॑ तया चक्रे पवित्रजल्पूर्णया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9756)
- **Original**: 13 क्रियमाणेअभिषेके तु गाव: कृष्णस्य तत्क्षणात्‌ । प्रश्नवोद्धृतदुग्धाद. सद्यभ्क्कुर्बवसुन्धराम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9757)
- **Original**: 14 अभिषिष्य गवां वाक्यादुपेन्द्रे वै जनार्दनम्‌ । प्रीत्या सप्रश्न्यं वाक्य पुनराह झचीपतिः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9758)
- **Original**: 95 गबामेतत्कृर्त ब्राक्य तथान्यद॒पि मे श्रूणु । भारावतरणेक्तया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9759)
- **Original**: 16 मर्पांश: पुरुषव्याप्र पृथिव्यां पृथिवीधर । अवतीणों्र्जुनो नाम संरक्ष्यो भवता सदा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9760)
- **Original**: 97 भारावतरणे साहा स ते वीर: करिष्यति । संरक्षणीयो भवता यथात्मा मथधुसूदन
- **Translation**: 

---

