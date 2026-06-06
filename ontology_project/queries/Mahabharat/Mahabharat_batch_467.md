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

### Verse 1 (Mahabharat 0.4661)
- **Original**: बाण मारे। इससे अर्जुनकों गहरी चोट छूगी और वे व्यखित होकर रथके पिछले भागमें बैठ गये । थोड़ी ही देरमें उम्हें चेत
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4661)
- **Original**: बाण मारे। इससे अर्जुनकों गहरी चोट छूगी और वे व्यखित होकर रथके पिछले भागमें बैठ गये । थोड़ी ही देरमें उम्हें चेत
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4662)
- **Original**: हुआ, फिर तो उन्होंने तुरंत ही ऐड्राख्को प्रकट किया। उससे
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4662)
- **Original**: हुआ, फिर तो उन्होंने तुरंत ही ऐड्राख्को प्रकट किया। उससे
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4663)
- **Original**: हजारों बाण निकल-निकलकर चारों दिज्ञाओंमें छा गये और
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4663)
- **Original**: हजारों बाण निकल-निकलकर चारों दिज्ञाओंमें छा गये और
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4664)
- **Original**: आपकी सेना तथा घोड़े-हाथियोंका विनाश करने लगे। इस
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4664)
- **Original**: आपकी सेना तथा घोड़े-हाथियोंका विनाश करने लगे। इस
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4665)
- **Original**: अरकार सेनाका संहार होता देख संशप्तकों तथा नारायणी
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4665)
- **Original**: अरकार सेनाका संहार होता देख संशप्तकों तथा नारायणी
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4666)
- **Original**: सेनाके ग्वाल्लोंको बड़ा भय हुआ। उस समय वहाँ एक भी
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4666)
- **Original**: सेनाके ग्वाल्लोंको बड़ा भय हुआ। उस समय वहाँ एक भी
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4667)
- **Original**: पुरुष ऐसा नहीं था, जो अर्जुनका सामना कर सके। सब दिया। तदनच्तर, अर्जुनने देखदस तथा आीकृष्णने पाक्चजन्य
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4667)
- **Original**: पुरुष ऐसा नहीं था, जो अर्जुनका सामना कर सके। सब दिया। तदनच्तर, अर्जुनने देखदस तथा आीकृष्णने पाक्चजन्य
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4668)
- **Original**: बीरोंके देखते-देखते आपकी सेना कट रही थी। वह स्वयं नामक शद्बू बजाया। उनकी ध्यनिसे पृथ्वी और आकाझ
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4668)
- **Original**: बीरोंके देखते-देखते आपकी सेना कट रही थी। वह स्वयं नामक शद्बू बजाया। उनकी ध्यनिसे पृथ्वी और आकाझ
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4669)
- **Original**: निश्चेष्ट हो गयी थी, उससे पराक्रम करते नहीं बनता था। यह गैजने-से छगे। शद्बोंकी आवाज सुत्रकर संझप्कॉंकी सेना
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4669)
- **Original**: निश्चेष्ट हो गयी थी, उससे पराक्रम करते नहीं बनता था। यह गैजने-से छगे। शद्बोंकी आवाज सुत्रकर संझप्कॉंकी सेना
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4670)
- **Original**: सब मेरी आँखों-देखी घटना है। अर्जुनने वहाँ दस हजारे भयसे सिहर डठी
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4670)
- **Original**: सब मेरी आँखों-देखी घटना है। अर्जुनने वहाँ दस हजारे भयसे सिहर डठी
- **Translation**: 

---

