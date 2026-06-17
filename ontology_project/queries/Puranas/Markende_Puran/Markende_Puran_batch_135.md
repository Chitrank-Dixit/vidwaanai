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

### Verse 1 (Markende Puran 0.2681)
- **Original**: समस्तस्थै नबो सम:
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2682)
- **Original**: ड्ण्प 14097 # 15 4 +. 4 +-+68 #-#प4 458 5 2 7:78 या देवी सर्वभूतेषु श्रद्धारूपेण संस्थिता। नमस्तस्यें
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2683)
- **Original**: भमस्तस्वे
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2684)
- **Original**: 59 # तपस्तस्य तम्रो नम:
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2685)
- **Original**: या देसी सर्वभूतेषु कान्तिरूपेण संस्थिता। नपस्तस्थै
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2686)
- **Original**: नमस्तस्थे
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2687)
- **Original**: नमस्तस्सै नमो नम:
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2688)
- **Original**: या देवी सर्वभूतेषु लक्ष्मीरूपेण संस्थिता। नपस्तस्थे
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2689)
- **Original**: तमस्तस्वै
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2690)
- **Original**: नपस्तस्ये नप्ो नमः
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2691)
- **Original**: या देवी सर्वभूतेषु वृत्तिरूपेण संस्थिता। नमस्तस्मे।।59
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2692)
- **Original**: नमस्तस्वै
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2693)
- **Original**: नमस्तस्सै नमो नम;
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2694)
- **Original**: या देवी सर्वंभूतेषु स्मृतिरूपेण संस्थिता। नप्स्तस्वे
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2695)
- **Original**: गमस्तस्थ
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2696)
- **Original**: पस्तस्यै नमो तय:
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2697)
- **Original**: वा देको सर्वधूतेषु दवारूपेण संस्थिता। नपमातस्वे
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2698)
- **Original**: नपस्तस्थे
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2699)
- **Original**: नपस्तस्यै नपो नम:
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2700)
- **Original**: 67 8 या देंकी सर्वभूतेयु तुष्टिरपेण संस्थिता। नमस्तस्यै
- **Translation**: 

---

