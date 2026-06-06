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

### Verse 1 (Mahabharat 0.4211)
- **Original**: 7/36 संहार करने छगा। उसकी मार खाकर केकयोंकी सेना ठहर
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4211)
- **Original**: 7/36 संहार करने छगा। उसकी मार खाकर केकयोंकी सेना ठहर
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4212)
- **Original**: ल्विर्व के न सकी। वह अपने प्रबल शत्रुका सामना करना छोड़ सब
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4212)
- **Original**: ल्विर्व के न सकी। वह अपने प्रबल शत्रुका सामना करना छोड़ सब
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4213)
- **Original**: 8 दिल्लाओँमें भाग गयी। । तदनन्तर श्रुतकर्माने क्रोधमें भरकर पत्नास बाणोंसे राजा चित्रसेनको घायल किया। अभिसारनरेश चित्रसेनने भी नो
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4213)
- **Original**: 8 दिल्लाओँमें भाग गयी। । तदनन्तर श्रुतकर्माने क्रोधमें भरकर पत्नास बाणोंसे राजा चित्रसेनको घायल किया। अभिसारनरेश चित्रसेनने भी नो
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4214)
- **Original**: बाणोंसे भ्रुतर्कमांकों बॉंधकर पाँच सायकॉसे उसके
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4214)
- **Original**: बाणोंसे भ्रुतर्कमांकों बॉंधकर पाँच सायकॉसे उसके
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4215)
- **Original**: सारथिको भी पीड़ित किया। तब श्रुतकर्माने चित्रसेनके
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4215)
- **Original**: सारथिको भी पीड़ित किया। तब श्रुतकर्माने चित्रसेनके
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4216)
- **Original**: मर्मस्थानमें तीखे नाराचसे बार किया। उसकी गहरी चोट
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4216)
- **Original**: मर्मस्थानमें तीखे नाराचसे बार किया। उसकी गहरी चोट
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4217)
- **Original**: देरमें जब होझ हुआ तो उसने एक भल्‍्ल मारकर श्रुतकर्माका
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4217)
- **Original**: देरमें जब होझ हुआ तो उसने एक भल्‍्ल मारकर श्रुतकर्माका
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4218)
- **Original**: धनुष काट दिया और फिर सात बाणोंसे उसे भी बींध
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4218)
- **Original**: धनुष काट दिया और फिर सात बाणोंसे उसे भी बींध
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4219)
- **Original**: डाला। श्रुतकर्माको पुनः क्रोथ आया, उसने झन्रुके धनुषके
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4219)
- **Original**: डाला। श्रुतकर्माको पुनः क्रोथ आया, उसने झन्रुके धनुषके
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4220)
- **Original**: उसकी छाती और कब ऐेदता हुआ जमीनमें घुस गया तथा दो दुकड़े कर डाले और तीन सौ बाण मारकर उसे खूब
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4220)
- **Original**: उसकी छाती और कब ऐेदता हुआ जमीनमें घुस गया तथा दो दुकड़े कर डाले और तीन सौ बाण मारकर उसे खूब
- **Translation**: 

---

