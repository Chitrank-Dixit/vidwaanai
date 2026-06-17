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

### Verse 1 (Rig Ved 0.11681)
- **Original**: 6 हे धाक्ोा।ए 7990करा
- **Translation**: 

---

### Verse 2 (Rig Ved 0.11682)
- **Original**: 2ट3र्0ए ;07 (6
- **Translation**: 

---

### Verse 3 (Rig Ved 0.11683)
- **Original**: 979 407 डआ7! पट धरा आरत फतह 6 5 । #3/97 8602€- 4949ए4734 #0
- **Translation**: 

---

### Verse 4 (Rig Ved 0.11684)
- **Original**: 97 78: (ग्रंग्रा05 > 20 [80।95 ?म्ररुएहांग्राज0 (सा) शिवपाल ;
- **Translation**: 

---

### Verse 5 (Rig Ved 0.11685)
- **Original**: 0095 (वह 9395 0 ण 8) 05 ।
- **Translation**: 

---

### Verse 6 (Rig Ved 0.11686)
- **Original**: पिताड्षाड 507
- **Translation**: 

---

### Verse 7 (Rig Ved 0.11687)
- **Original**: 57 (#एएॉ€ 5
- **Translation**: 

---

### Verse 8 (Rig Ved 0.11688)
- **Original**: 3945 #ए
- **Translation**: 

---

### Verse 9 (Rig Ved 0.11689)
- **Original**: / 77एठाफराए
- **Translation**: 

---

### Verse 10 (Rig Ved 0.11690)
- **Original**: पाफशा 57995, एंड" (9: 45
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11691)
- **Original**: 'मोध <एात(टिकाल €4 609407 90
- **Translation**: 

---

### Verse 12 (Rig Ved 0.11692)
- **Original**: % 948] €
- **Translation**: 

---

### Verse 13 (Rig Ved 0.11693)
- **Original**: 3 0 27065 ण॑ 37(4
- **Translation**: 

---

### Verse 14 (Rig Ved 0.11694)
- **Original**: 70075 437 0 (6 9 1404! 7 3001 30
- **Translation**: 

---

### Verse 15 (Rig Ved 0.11695)
- **Original**: तए/छ [द
- **Translation**: 

---

### Verse 16 (Rig Ved 0.11696)
- **Original**: 50700 47
- **Translation**: 

---

### Verse 17 (Rig Ved 0.11697)
- **Original**: 5 सडः <
- **Translation**: 

---

### Verse 18 (Rig Ved 0.11698)
- **Original**: ञातठं छछ 400
- **Translation**: 

---

### Verse 19 (Rig Ved 0.11699)
- **Original**: 6 3 ।: * हा >#0णा (4 099 $
- **Translation**: 

---

### Verse 20 (Rig Ved 0.11700)
- **Original**: 0आ6< 0285-49
- **Translation**: 

---

