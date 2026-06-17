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

### Verse 1 (Vishnu Puran 0.8301)
- **Original**: उसके नामकरणके विषयमें भो यह इत्मेक कहा जाता है---
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8302)
- **Original**: “'पुज्ोत्पत्तिके अनन्तर बृहस्पतिने ममतासे कहा---'हे मूढ़े ! यह पुत्र द्वाज (हम टोनोंसे उत्पन्न हुआ) है तू इसका भरण कर ।' तब ममताने भी कहा---' हे खहस्पते ! यह पुत्र द्वाज (हम दोनोंसे उत्पन्न-हुआ) है अतः तुम इसका भरण करो ।' इस प्रकार परस्पर विदाद करते हुए उसके माता-पिता चले गये, इसलिये उसका नाम भरद्वाज' पड़ा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8303)
- **Original**: पूत्र-जन्म वितथ (विफल) होनेपर मरूदणने राजा भरतको भरद्वाज दिया था, इसलिये उसका नाम 'वितथ' भी हुआ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8304)
- **Original**: वितथका पुत्र मन्‍्यु हुआ और मन्वुके खुहस्क्षत्र, सहावीर्य, नर और गर्ग आदि कई पुत्र हुए
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8305)
- **Original**: पगरका पुत्र संकति और संकृतिके गुरुप्रीति एजे रन्तिदेज नामक दो पुत्र हुए
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8306)
- **Original**: गर्गसे झिनिका जन्म हुआ जिससे कि गार्म्य और शैन्य नामसे विख्यात क्षत्रोपेत ब्राह्मण उत्पन्न हुए
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8307)
- **Original**: महावीर्यका पुत्र दुरुक्षय हुआ
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8308)
- **Original**: उसके त्रय्यारुणि, पुष्करिण्य और कपि नामक तीन पुत्र हुए
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8309)
- **Original**: ये तीनों पुत्र पीछे ब्राह्मण हो गये थे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8310)
- **Original**: बुहत्क्षत्रका पुत्र सुझोत्र, सुहोजका पुत्र हस्ती था जिसने यह हस्तिनापुर नामक नगर बसाया था
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8311)
- **Original**: हस्तीके तोन पुत्र अजमीढ, द्विजमीढ और पुरुमीढ थे । अजमीढके कण्व और कण्बके मेघातिथि नामक पुत्र हुआ जिससे कि काण्वायन ज्राह्मण उत्पन्न हुए
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8312)
- **Original**: 29--32
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8313)
- **Original**: अजमीदका दूसरा पुत्र खहदिषु था
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8314)
- **Original**: उसके वृहद्धनु, बृहद्धलुके बृहत्कर्मा।।बहत्कर्मकि जयद्रथ, जयद्रधके विश्वजित्‌ तथा विश्वजित॒के सेनजित्‌का जन्म हुआ । सेनजित्‌के रुचिएश्च; काज्य; दूढहनु और वत्सहनु नामक चार पुत्र हुए
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8315)
- **Original**: 34--36
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8316)
- **Original**: रुचिराश्चके पृथुसेन, पृथुसेनके पार और पारके नीलका जन्म हुआ । इस नीलके सौ पुत्र थे, जिनमें काम्पिल्यनरेशा समर प्रधान था
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8317)
- **Original**: 37---40
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8318)
- **Original**: समरके पार, सुपार और सदश्न नामक तीन पुत्र थे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8319)
- **Original**: सुपारके पृथु, पृथुके सुकृति, सुकृतिके खिधाज और विभ्राजके अगुह नामक पुत्र हुआ, जिसने शुककत्या कीर्तिसे विवाह किया था
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8320)
- **Original**: अणुहसे ब्रह्मदतका जन्म हुआ। बद्यदत्तसे विष्वक्सेन विध्रक्सेनसे उदक्सेन तथा उदक्सेनसे भल्ल्ाभ नामक पुत्र उत्पन्न हुआ
- **Translation**: 

---

