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

### Verse 1 (Markende Puran 0.2661)
- **Original**: तगस्ताये
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2662)
- **Original**: नमस्तस्यें वप्तो चप
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2663)
- **Original**: या देवी सर्वंभूतेषु शक्तिरूपेण संस्थिता। नयस्तस्पै
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2664)
- **Original**: नमस्तस्थै
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2665)
- **Original**: नमस्ते तममो वर:
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2666)
- **Original**: # ऋ देंयो सर्वभूतेषु तृष्णारूपेण संस्थिता
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2667)
- **Original**: नगस्ता्थै
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2668)
- **Original**: 35 # भगस्ता्ये
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2669)
- **Original**: गफस्तस्थ नमो तप:
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2670)
- **Original**: 67 # या देखी सर्वभूतेषु क्षान्तिरूपेण संस्थिता। मफातस्यै।। 38
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2671)
- **Original**: नमस्तस्य
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2672)
- **Original**: नपस्तस्ये नमो तम:
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2673)
- **Original**: या देजों सर्वभूतेषु जातिरूपेण संस्थिता। नमस्तस्वे
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2674)
- **Original**: नमस्तस्य
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2675)
- **Original**: नमस्तर्यै नमो नम
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2676)
- **Original**: या देखी स्वभूलेषु लज्जारूपेण संस्थिता। नमसतस्वे।। 44
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2677)
- **Original**: नमस्तस्ये
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2678)
- **Original**: भपस्तस्वै नमो तय:
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2679)
- **Original**: या देवी सर्वभूतेषु शान्तिरूपेण संस्थिता। नप्रस्तायै
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2680)
- **Original**: नमस्तस्ये
- **Translation**: 

---

