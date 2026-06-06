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

### Verse 1 (Vishnu Puran 0.6301)
- **Original**: तस्थाप्यु- ल्कलगगयविनतार्त्रय: पुत्रा बभूवु:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6302)
- **Original**: सुघुप्नस्तु स्त्रीपूर्वकत्वाद्राज्यभागं न लेभे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6303)
- **Original**: तत्पित्रा तु वसिष्ठवचनात्प्रतिष्ठानं नाम नगर सुच्युम्नाय दत्त तघासौ पुरूरवसे प्रादात्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6304)
- **Original**: तदन्वयाश्ष क्षत्रियास्सवें दिक्षषभवन । पृषध्रस्तु मनुपुत्रो गुरुगोवरधाच्छृद्रत्वमगमत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6305)
- **Original**: मनोः पुत्र: करूष: करूषात्कारूषा: क्षत्रिया महाबल- पराक्रमा बम्मूबु:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6306)
- **Original**: दिु्टपुत्रस्तु नाभागो बैश्यतामगमत्तस्मादलन्धन: पुत्रो3भवत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6307)
- **Original**: बलन्धनादत्सप्रीतिरुदास्कीतत्ति:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6308)
- **Original**: बत्त्प्रीतेः प्रांझुरभवत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6309)
- **Original**: प्रजापतिश्न प्राझ्रोरेको5भवत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6310)
- **Original**: ततश्च॒ खनित्र:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6311)
- **Original**: तस्माचाक्षुष:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6312)
- **Original**: चारक्षुषाश्ाति- खलपराक्रमो. विंशो$भवत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6313)
- **Original**: ततो विविशक:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6314)
- **Original**: तस्माद्च खनिनेत्र:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6315)
- **Original**: ततश्चातिविभूति:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6316)
- **Original**: . अतिविभूतेरति- बलपराक्रम: करन्धमः पुत्नो35भवत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6317)
- **Original**: तस्मादप्यविक्षित्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6318)
- **Original**: अविज्षिततोउप्यति- बलपराक्रम: पुत्रो मरुतो नामाभवत्‌; यस्पेमावद्यापि इलोकौ गीयेते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6319)
- **Original**: मरुत्तस्य यथा यज्ञस्तथा कस्याभवद्भुवि
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6320)
- **Original**: सर्व हिरण्मयं यस्थ॒ यज्ञवस्त्वतिञ्ञोभनम्‌
- **Translation**: 

---

