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

### Verse 1 (Markende Puran 0.2641)
- **Original**: *देवताओंद्वास देवीको स्तुति * '&+27 7 # 30174 ###क4 & । शैश्षय कमो नित्याये गौये क्षात्ये नमो नमः। ज्योत्त्रायै चेन्ट्रूपिण्य सुखायै सततं चम:
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2642)
- **Original**: 10 छ सह््याण्य प्रणाम वृद्धा सिद्धाँ कुर्मों नमो नम:। नैकत्य भूभुतां लक्ष्य शर्वाण्य ते नमो नमः
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2643)
- **Original**: दुगयि दुर्गपाराये साराये सर्वकारिण्य। ख्यात्य तथैत्र क्ृष्णायै धूप्रामे सतत नमः
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2644)
- **Original**: अतिसौम्यातिरौद्राय॑ नतास्तस्थे नमो नमः। नमो जगत््नतिष्ठाय॑ देव्यै कृत्य नम्मो नमः
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2645)
- **Original**: था देवी सर्वभूतेषु विष्णुमायेति शब्दिता। अपस्तर्य
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2646)
- **Original**: तम्ख्तर्ये
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2647)
- **Original**: नमस्तस्थ नमो छप:
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2648)
- **Original**: आऋ देवों सर्वभूतेषु बेतनेत्यभिधीयते। नप्स्तस्ये
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2649)
- **Original**: नमस्तस्थै
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2650)
- **Original**: नपस्तस्य तम्ने सम:
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2651)
- **Original**: 99 # या देवी सर्वभूतेषु ग्रुद्धिरूुपेण संस्थिता। जमस्तस्यें
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2652)
- **Original**: नमस्तस्वै
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2653)
- **Original**: सपस्तस्थे नमो नम:
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2654)
- **Original**: या देवी सर्वभूतेषु निम्रारपेण संस्थिता। नमस्तस्थै
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2655)
- **Original**: नमस्तस्ये
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2656)
- **Original**: नप्रस्तस्थे नप्तो नम:
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2657)
- **Original**: वा देवी सर्वभूतेषु क्षुआरूपेण संस्थिता। नमस्ते
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2658)
- **Original**: तमसास्थ
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2659)
- **Original**: 27।।नपस्तस्यै नमो नम:
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2660)
- **Original**: या देवी सर्वभूतेषुच्छायारूपेण संस्थिता। नम्स्तस्थै
- **Translation**: 

---

