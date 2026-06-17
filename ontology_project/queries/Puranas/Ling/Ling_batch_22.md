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

### Verse 1 (Ling 0.421)
- **Original**: 32 महः ईश्वराय नमः
- **Translation**: 

---

### Verse 2 (Ling 0.422)
- **Original**: 3» महः ईश्वराय स्वाहा
- **Translation**: 

---

### Verse 3 (Ling 0.423)
- **Original**: 300 जनः प्रकृतये नमः
- **Translation**: 

---

### Verse 4 (Ling 0.424)
- **Original**: 3» जनः प्रकृत्ये स्वाहा
- **Translation**: 

---

### Verse 5 (Ling 0.425)
- **Original**: 34 तपः मुद्गलाय नमः
- **Translation**: 

---

### Verse 6 (Ling 0.426)
- **Original**: 3» मुग्दलाय स्वाहा
- **Translation**: 

---

### Verse 7 (Ling 0.427)
- **Original**: 34 ऋत॑ पुरुषाय नमः
- **Translation**: 

---

### Verse 8 (Ling 0.428)
- **Original**: 340 ऋतं पुरुषाय स्वाहा
- **Translation**: 

---

### Verse 9 (Ling 0.429)
- **Original**: 30 सत्य शिवाय नमः:
- **Translation**: 

---

### Verse 10 (Ling 0.430)
- **Original**: 3» सत्यं शिवाय स्वाहा
- **Translation**: 

---

### Verse 11 (Ling 0.431)
- **Original**: 3 शर्व! थराँ मे गोपाय प्राणे गन्धं शर्वय देवाय भूर्नमः
- **Translation**: 

---

### Verse 12 (Ling 0.432)
- **Original**: 3» शर्व! धराँ मे गोपाय प्राणे गन्धं शर्वय भू: स्वाहा
- **Translation**: 

---

### Verse 13 (Ling 0.433)
- **Original**: 3» शर्व! धराँ मे गोधाय प्राणे गन्धं शर्वस्य देवस्य पत्चयै भूर्नमः
- **Translation**: 

---

### Verse 14 (Ling 0.434)
- **Original**: 3» शर्व! थराँ मे गोपाय प्राणे गर्न्‍्ध शर्य पत्ये भू स्वाहा
- **Translation**: 

---

### Verse 15 (Ling 0.435)
- **Original**: 3» भव! जल मे गोपाय जिट्लायां रसम्भवाय देवाय “भुवा नमः
- **Translation**: 

---

### Verse 16 (Ling 0.436)
- **Original**: 3» भव! जल मे गोपाय जिद्नायां रसम्भवाय देवाय भुवः स्वाहा
- **Translation**: 

---

### Verse 17 (Ling 0.437)
- **Original**: 3» भव! जल॑ मे गोपाय जिड्नायां रसम्भवस्य देवस्य पल्ये भुवो नमः
- **Translation**: 

---

### Verse 18 (Ling 0.438)
- **Original**: 30 भव! जल॑ मे गोपाय जिड्लायां रसम्भवस्य पत्नये
- **Translation**: 

---

### Verse 19 (Ling 0.439)
- **Original**: # श्री लिंग पुराण & 371 भुवः स्वाहा
- **Translation**: 

---

### Verse 20 (Ling 0.440)
- **Original**: 3» रुद्रार्नि मे गोपाय नेत्रे रूप॑ रुद्राय स्व॒रो नमः
- **Translation**: 

---

