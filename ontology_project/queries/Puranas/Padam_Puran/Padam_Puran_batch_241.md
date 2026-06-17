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

### Verse 1 (Padam Puran 7.4801)
- **Original**: नित्य॑त्रयीनाथायथ ते नमः
- **Translation**: 

---

### Verse 2 (Padam Puran 7.4802)
- **Original**: नमो. ब्रह्मण्यदेयाय नागपर्यडूआयिते । जमः
- **Translation**: 

---

### Verse 3 (Padam Puran 7.4803)
- **Original**: सायया मोहिताः सर्वे देवाक्ष ऋष्यस्तव ।
- **Translation**: 

---

### Verse 4 (Padam Puran 7.4804)
- **Original**: । जानन्ति पहात्पाने सर्यल्लेकेश्वर प्रभों । त्वो न जानन्ति भगवन्सर्ववेदविदोअपि हिं।
- **Translation**: 

---

### Verse 5 (Padam Puran 7.4805)
- **Original**: 7007-82)
- **Translation**: 

---

