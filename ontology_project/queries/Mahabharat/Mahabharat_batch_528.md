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

### Verse 1 (Mahabharat 0.5271)
- **Original**: के ल्कौंटे। अश्वत्थामा भी पाण्डबोंकी विजय देखकर बारंबार
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5271)
- **Original**: के ल्कौंटे। अश्वत्थामा भी पाण्डबोंकी विजय देखकर बारंबार
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5272)
- **Original**: ? उद्छवास लेता हुआ छावनीकी ओर ही चल दिया। बचे
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5272)
- **Original**: ? उद्छवास लेता हुआ छावनीकी ओर ही चल दिया। बचे
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5273)
- **Original**: हुए संझ्प्तकॉंसहित सुझर्मा और दूटी ध्वजावाले रथके
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5273)
- **Original**: हुए संझ्प्तकॉंसहित सुझर्मा और दूटी ध्वजावाले रथके
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5274)
- **Original**: साथ राजा झल्य भी डरते एवं लूजाते हुए छावनीकी ओर
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5274)
- **Original**: साथ राजा झल्य भी डरते एवं लूजाते हुए छावनीकी ओर
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5275)
- **Original**: चले। कर्णकी मृत्यु देखकर समस्त कौरब भयसे व्याकुल
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5275)
- **Original**: चले। कर्णकी मृत्यु देखकर समस्त कौरब भयसे व्याकुल
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5276)
- **Original**: होकर काँप रहे थे, उनके झरीरसे खूनकी धारा बह रही
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5276)
- **Original**: होकर काँप रहे थे, उनके झरीरसे खूनकी धारा बह रही
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5277)
- **Original**: (65/ थी; अतः सब-के-सब उद्ठिप्र होकर भाग गये। अब उन्हें
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5277)
- **Original**: (65/ थी; अतः सब-के-सब उद्ठिप्र होकर भाग गये। अब उन्हें
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5278)
- **Original**: शव अपने जीवन और राज्यकी आश्ञा न रही। दुर्योधन दुःख
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5278)
- **Original**: शव अपने जीवन और राज्यकी आश्ञा न रही। दुर्योधन दुःख
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5279)
- **Original**: और झोकमें डूब रहा था, वह बड़े यत्रसे सबको एकत्र करके छाबनीमें ले आया। राजाकी आज्ञा मान सभी
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5279)
- **Original**: और झोकमें डूब रहा था, वह बड़े यत्रसे सबको एकत्र करके छाबनीमें ले आया। राजाकी आज्ञा मान सभी
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5280)
- **Original**: सैनिकोने झिविरमें आकर विश्राम किया। उस समय
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5280)
- **Original**: सैनिकोने झिविरमें आकर विश्राम किया। उस समय
- **Translation**: 

---

