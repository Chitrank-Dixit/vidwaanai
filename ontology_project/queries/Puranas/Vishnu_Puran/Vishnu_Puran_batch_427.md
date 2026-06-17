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

### Verse 1 (Vishnu Puran 0.8521)
- **Original**: तत्पुत्रश्च सुमित्र:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8522)
- **Original**: इलत्येते . चेक्ष्वाकवो बृहद्वलान्वया:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8523)
- **Original**: अ्नानुवंशइल्मेक:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8524)
- **Original**: इक्ष्वाकृणामयं वंशस्सुमित्रान्तों भविष्यति । यतस्त॑ प्राप्य राजान॑ संस्था प्राप्यति वै कल्लो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8525)
- **Original**: 13 श्रीपराशरजी बोत्दे---अब मैं भविष्यमें होनेबाले इश्ष्याकुलशीय राजाओंका चर्णन करता हूँ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8526)
- **Original**: बहद्डलका पुत्र बुहत्दाण होगा, उसका उरुक्षय, उरुक्षयका वत्सव्यूह, बत्सन्यूहका प्रतिव्योम, प्रतिव्योमका दिवाकर, दिव्राकस्का सहदेव, सहदेवका बुहदश्थ, बृहदश्चका भानुरथ, भानुरथका प्रतीताश्च, प्रतीताश्रका सुप्रतीक, सुप्रतीकका मरुदेय, मल्देवका सुनक्षत्र, सुनक्षत्रका किन्नर, किन्रक्ता अन्तरिक्ष, अन्तरिक्षका सुपर्ण, सुपर्णको अमिन्नजित, अमित्रजितका बूहद्राज, बृहद्राजका धर्मी, चर्मीका कृत्य, कृतअयका रणञ्जय, रणञ़्यका सञ्अय, सञयफका दाक्‍्य, शाक्यका झुद्धोदन, शुद्धोदनका राहुल, राहुछका प्रसेनजित्‌, प्रसेनजितका क्षुद्रक, श्षुद्रकका कुष्डक, कुप्डकका सुरथ और सुरथका सुमित्र नामक पुत्र होगा। ये सब इक्ष्जाकुक्े वंदामें बृरद्वककी सनन्‍्तान होंगे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8527)
- **Original**: 2--611
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8528)
- **Original**: इस अंशके है---
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8529)
- **Original**: यह इक्बाकुवंश राजा सुमित्रतक रहेगा, क्योंकि कल्लियुगर्में राजा सुमित्र्के होनेपर फिर यह समाप्त हो जायगा'
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8530)
- **Original**: सम्बश्में यह इल्मेक प्रसिद्ध कण औ पा इति श्रीविष्णुपुराणे चतुर्थे 5शे द्वातिशोउ्ध्यायः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8531)
- **Original**: आर 23, 24 ] चतुर्थ अंश 297 तेईसवाँ अध्याय मगधवंशका वर्णन ऑीफराशर उकाच श्रीपराशरजी बोले--अब मैं मगधदेशीय मागधानां बार्ईद्रथानां भाविनामनुक्रमं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8532)
- **Original**: बृहद्रधको भाषी सन्तानका अनुक्रमसे वर्णन करूँगा कथयिष्यामि
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8533)
- **Original**: अन्न हि तंशे महालल-
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8534)
- **Original**: इस बंशमें महानलवान्‌ और पराक्रमी जरासन्थ पराक्रमा जरासन्धप्रधाना बभूवु:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8535)
- **Original**: । आदि राजागण प्रधान थे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8536)
- **Original**: जरासन्धस्य पुत्र: सहदेखः:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8537)
- **Original**: सहदेवा- त्सोमापिस्तस्य श्रुतभ्रवास्तस्पाप्ययुतायुस्तत श्र जरासन्धका पुत्र सहदेव है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8538)
- **Original**: सहदेवके सोमापि निरमित्रस्तत्तनयस्मुनेत्रस्तस्मादपि. बृहत्कर्मा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8539)
- **Original**: तामक पुत्र होगा, सरोमापिके श्रुतश्रा, श्रुतश्रवाके
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8540)
- **Original**: ततश्न सेनजित्ततश्न॒श्रुतझयस्ततो
- **Translation**: 

---

