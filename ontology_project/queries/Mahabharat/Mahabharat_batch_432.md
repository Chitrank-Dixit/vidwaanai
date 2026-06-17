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

### Verse 1 (Mahabharat 0.4311)
- **Original**: बाणोंकी झड़ी लगा दी और हजातं तोमरोंका वार किया । उनकी
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4311)
- **Original**: बाणोंकी झड़ी लगा दी और हजातं तोमरोंका वार किया । उनकी
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4312)
- **Original**: भाससे हाथियोंके कुम्भस्थल फूट गये, मर्मस्थानोंमें घाव हो गया,
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4312)
- **Original**: भाससे हाथियोंके कुम्भस्थल फूट गये, मर्मस्थानोंमें घाव हो गया,
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4313)
- **Original**: दौत दूट गये और उनकी सारी सजावट बिगड़ गयी । उनमेंसे आठ । बड़े-बड़े गजराजोंको सहदेवने चौंसठ बाण मारे, जिनकी चोटसे
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4313)
- **Original**: दौत दूट गये और उनकी सारी सजावट बिगड़ गयी । उनमेंसे आठ । बड़े-बड़े गजराजोंको सहदेवने चौंसठ बाण मारे, जिनकी चोटसे
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4314)
- **Original**: पीड़ित हो वे हाथी अपने सवारोसहित गिरकर मर गये।
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4314)
- **Original**: पीड़ित हो वे हाथी अपने सवारोसहित गिरकर मर गये।
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4315)
- **Original**: प्रहाराज ! सहदेव जब क्रोधमें भरकर आपकी सेनाको 4 । भस्पसात्‌ कर रहा था , उसी समय दुःशासन उसके मुकाबलेमें आ गया । आते ही उसने सहदेवकी छातीमें तीन बाण मारे । तब
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4315)
- **Original**: प्रहाराज ! सहदेव जब क्रोधमें भरकर आपकी सेनाको 4 । भस्पसात्‌ कर रहा था , उसी समय दुःशासन उसके मुकाबलेमें आ गया । आते ही उसने सहदेवकी छातीमें तीन बाण मारे । तब
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4316)
- **Original**: सहदेवने स्तर नाराचोंसे दुःझासनको तथा तीनसे उसके
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4316)
- **Original**: सहदेवने स्तर नाराचोंसे दुःझासनको तथा तीनसे उसके
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4317)
- **Original**: सारधिको बींध डाला
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4317)
- **Original**: सारधिको बींध डाला
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4318)
- **Original**: यह देख दुःशासनने सहदेवका धनुष तब स्लेब्छोंने अपये हाथियोंको झत्ुओंकी ओर ग्रेरित
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4318)
- **Original**: यह देख दुःशासनने सहदेवका धनुष तब स्लेब्छोंने अपये हाथियोंको झत्ुओंकी ओर ग्रेरित
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4319)
- **Original**: काटकर उसकी छाती और भुजाओंमें तिहत्तर बाण मारे। अब किया। बे हाथी अत्यत्त क्रोधमें भरे हुए थे; इसलिये रथों,
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4319)
- **Original**: काटकर उसकी छाती और भुजाओंमें तिहत्तर बाण मारे। अब किया। बे हाथी अत्यत्त क्रोधमें भरे हुए थे; इसलिये रथों,
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4320)
- **Original**: तो सहदेवके क्रोथकी सीमा न रही, उसने बड़ी फुर्तासि [57] ] सं0 म0 ( खण्ड--दो ) 29
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4320)
- **Original**: तो सहदेवके क्रोथकी सीमा न रही, उसने बड़ी फुर्तासि [57] ] सं0 म0 ( खण्ड--दो ) 29
- **Translation**: 

---

