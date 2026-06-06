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

### Verse 1 (Vishnu Puran 0.8281)
- **Original**: अजमीढद्विजमीढपुरुमीढाखयो हस्तिनस्तनया:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8282)
- **Original**: अजमीढात्कण्व:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8283)
- **Original**: कण्वान- मेधातिथि:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8284)
- **Original**: यतः काण्वायना द्विजाः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8285)
- **Original**: अजसमीढस्थान्य: पुत्रों बृहदिषुः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8286)
- **Original**: बृहदिषोर्व॑हद्नुर्वृहद्धनुषक्ष बृहत्कर्मा ततश्न जयद्रथस्तस्मादपि व्श्वजित्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8287)
- **Original**: ततश्च सेनजित्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8288)
- **Original**: रुचिराश्चकाइयदृढहनुवत्सहनु- संज्ञास्सेनजित: पुत्रा:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8289)
- **Original**: रुचिराश्चपुत्रः पृथुसेनः पुथुसेनात्पार:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8290)
- **Original**: पाराज्नील
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8291)
- **Original**: तस्वैकझत॑ पुत्राणाम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8292)
- **Original**: तेषां प्रधान: काम्पिल्याधिपतिस्समर:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8293)
- **Original**: समरस्थापि पारसुपारसदक्चास्रय: पुत्रा:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8294)
- **Original**: सुपारात्युथु: पृथोस्ससुकृतिस्ततो विभ्राज:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8295)
- **Original**: तस्माश्चाणुह:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8296)
- **Original**: यहश्ुकदुहितरं कीर्ति नामोपयेमे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8297)
- **Original**: अणुहादब्नह्मद्त:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8298)
- **Original**: ततश्न विषृक्सेनस्तस्मादुदक्सेन:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8299)
- **Original**: भ्ललाभस्तस्य चात्मज:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8300)
- **Original**: श्रीविष्णुपुराण [ अ" 19 गर्भमें स्थित दीर्घतमा मुनिके पाद-प्रहारसे स्खरित हुए. युहस्पतिजीके वीर्यसे उत्पन्न हुआ था
- **Translation**: 

---

