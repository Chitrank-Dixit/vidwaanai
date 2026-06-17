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

### Verse 1 (Vishnu Puran 0.6341)
- **Original**: *“मरुत्तका जैसा यज्ञ हुआ था वैसा इस पृथिवीपर और किसका हुआ है, जिसकी सभी याज्ञिक बस्तुएँ सुवर्णमय और अति सुन्दर थीं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6342)
- **Original**: उस यज्ञमें इन्द्र सोमरसले और ब्राह्मणणण दक्षिणासे परितृप्त हो गये थे, तथा उसमें मरूद्रण परोसनेवाले और देखगण सदस्य थे!
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6343)
- **Original**: उस चक्रवर्ती मरुत्तके नरिष्यत्त नामक पुत्र हुआ तथा नरिष्यन्तके दम और दमके राजवर्द्धन नामेक पुत्र जेत्पन्न हुआ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6344)
- **Original**: राजवर्दधनसे सुबद्धि, सुबद्धिसे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6345)
- **Original**: आ 1 ] सुवृद्धे: केवल:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6346)
- **Original**: _ केवलात्सुधृति- रभूत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6347)
- **Original**: ततश्न नरः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6348)
- **Original**: तस्माशन्द्रः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6349)
- **Original**: ततः केवलो5भूत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6350)
- **Original**: केवर्ा- इन्धुमान्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6351)
- **Original**: बन्धुघतो वेगवान्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6352)
- **Original**: वेगवतो खुध:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6353)
- **Original**: ततश्च॒तृणबिन्दुः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6354)
- **Original**: तस्वाप्येका कन्या इलखिला नाम
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6355)
- **Original**: ततश्आालम्बुसा नाम वराप्सरा- स्तृणबिन्तुं भेजे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6356)
- **Original**: तस्यामप्यस्थ विशालो जज्ले यः पुरी विशाल्तां निर्ममे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6357)
- **Original**: हेमचनद्रश्ष॒ विशालस्य पुत्रो$भवत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6358)
- **Original**: ततक्चन्द्र:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6359)
- **Original**: तत्तनयो धुृम्नाक्ष:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6360)
- **Original**: तस्यापि सुक्षयो5भूत्‌
- **Translation**: 

---

