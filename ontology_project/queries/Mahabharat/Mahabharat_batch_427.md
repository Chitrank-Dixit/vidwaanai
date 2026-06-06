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

### Verse 1 (Mahabharat 0.4261)
- **Original**: आवाज सुनायी दी। तब श्रीकृष्णने घोड़ोंकों बढ़ाया और वहाँ
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4261)
- **Original**: आवाज सुनायी दी। तब श्रीकृष्णने घोड़ोंकों बढ़ाया और वहाँ
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4262)
- **Original**: पुँचकर देखा कि राजा पाण्डयके द्वारा दुर्योधनकी सेनाका (न
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4262)
- **Original**: पुँचकर देखा कि राजा पाण्डयके द्वारा दुर्योधनकी सेनाका (न
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4263)
- **Original**: चिकट विष्वंस हुआ है। यह देख उन्हें बड़ा विस्मय हुआ । राजा बिंदी
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4263)
- **Original**: चिकट विष्वंस हुआ है। यह देख उन्हें बड़ा विस्मय हुआ । राजा बिंदी
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4264)
- **Original**: . पाण्का अखविद्या तथा धुर्विद्यामें प्रवीण थे। उन्होंने अनेकों 5.
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4264)
- **Original**: . पाण्का अखविद्या तथा धुर्विद्यामें प्रवीण थे। उन्होंने अनेकों 5.
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4265)
- **Original**: प्रकारके बाण मारकर शत्रु-समुदायका नाश कर डाला था। 8
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4265)
- **Original**: प्रकारके बाण मारकर शत्रु-समुदायका नाश कर डाला था। 8
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4266)
- **Original**: झन्नुओंके प्रधान-प्रधान बीरोने उनपर जो-जो अख छोड़े थे; उन जल छ'
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4266)
- **Original**: झन्नुओंके प्रधान-प्रधान बीरोने उनपर जो-जो अख छोड़े थे; उन जल छ'
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4267)
- **Original**: सबको अपने सायकोंसे काटकर वे उन बीरोंको यमल्मोक भेज
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4267)
- **Original**: सबको अपने सायकोंसे काटकर वे उन बीरोंको यमल्मोक भेज
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4268)
- **Original**: चुके थे। 2.8
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4268)
- **Original**: चुके थे। 2.8
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4269)
- **Original**: धृताफूने कहा--सस्रय ! अब तुम मुझसे राजा पाण्डय्के कण
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4269)
- **Original**: धृताफूने कहा--सस्रय ! अब तुम मुझसे राजा पाण्डय्के कण
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4270)
- **Original**: पराक्रम, अखशिक्षा, प्रभाव और बलका वर्णन करो ।
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4270)
- **Original**: पराक्रम, अखशिक्षा, प्रभाव और बलका वर्णन करो ।
- **Translation**: 

---

