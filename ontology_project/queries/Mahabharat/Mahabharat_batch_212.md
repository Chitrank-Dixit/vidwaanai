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

### Verse 1 (Mahabharat 0.2111)
- **Original**: दे करके अर्जुनसे कहा--'कुन्तीनन्दन ! हमल्‍्मेश आपकी किस
- **Translation**: 

---

### Verse 2 (Mahabharat 0.2111)
- **Original**: दे करके अर्जुनसे कहा--'कुन्तीनन्दन ! हमल्‍्मेश आपकी किस
- **Translation**: 

---

### Verse 3 (Mahabharat 0.2112)
- **Original**: है आज्ञाका पालन करें ?' ) अर्जुनने कहा--सुमस्लोगोंका कल्याण हो। डरे मत, अपने है. 9» देशको लौट जाओ । मैं संकटमें पड़े हुएको नहीं मारना चाहता ।
- **Translation**: 

---

### Verse 4 (Mahabharat 0.2112)
- **Original**: है आज्ञाका पालन करें ?' ) अर्जुनने कहा--सुमस्लोगोंका कल्याण हो। डरे मत, अपने है. 9» देशको लौट जाओ । मैं संकटमें पड़े हुएको नहीं मारना चाहता ।
- **Translation**: 

---

### Verse 5 (Mahabharat 0.2113)
- **Original**: न इस बातके लिये तुमलोगोंक्रे पूरा विश्वास दिलाता हूँ। वह अभयदानयुक्त वाणी सुनकर वहाँ आये हुए सभी
- **Translation**: 

---

### Verse 6 (Mahabharat 0.2113)
- **Original**: न इस बातके लिये तुमलोगोंक्रे पूरा विश्वास दिलाता हूँ। वह अभयदानयुक्त वाणी सुनकर वहाँ आये हुए सभी
- **Translation**: 

---

### Verse 7 (Mahabharat 0.2114)
- **Original**: अजुतको प्रसन्न किया । उसके बाद अर्जुनने उत्तकको हयसे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.2114)
- **Original**: अजुतको प्रसन्न किया । उसके बाद अर्जुनने उत्तकको हयसे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.2115)
- **Original**: ] (- हि/ह ः लगाकर कहा--तात ! यह तो तुम्हें मालूम ही हो गया है कि
- **Translation**: 

---

### Verse 10 (Mahabharat 0.2115)
- **Original**: ] (- हि/ह ः लगाकर कहा--तात ! यह तो तुम्हें मालूम ही हो गया है कि
- **Translation**: 

---

### Verse 11 (Mahabharat 0.2116)
- **Original**: छड शर0
- **Translation**: 

---

### Verse 12 (Mahabharat 0.2116)
- **Original**: छड शर0
- **Translation**: 

---

### Verse 13 (Mahabharat 0.2117)
- **Original**: 4 2 हे प्रवेश करके तुम पाप्डबोकी प्रशंसा न करना, नहीं तो तुस्हार 2 शक 8
- **Translation**: 

---

### Verse 14 (Mahabharat 0.2117)
- **Original**: 4 2 हे प्रवेश करके तुम पाप्डबोकी प्रशंसा न करना, नहीं तो तुस्हार 2 शक 8
- **Translation**: 

---

### Verse 15 (Mahabharat 0.2118)
- **Original**: पिता डसकर प्राण त्याग देंगे।' उत्तर बोला--'सब्यसाधिन्‌ !
- **Translation**: 

---

### Verse 16 (Mahabharat 0.2118)
- **Original**: पिता डसकर प्राण त्याग देंगे।' उत्तर बोला--'सब्यसाधिन्‌ !
- **Translation**: 

---

### Verse 17 (Mahabharat 0.2119)
- **Original**: £ >> के 6 जबतक आप इस बातकोे प्रकाझित करनेके लिये स्वयं मुझसे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.2119)
- **Original**: £ >> के 6 जबतक आप इस बातकोे प्रकाझित करनेके लिये स्वयं मुझसे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.2120)
- **Original**: ध्वजापर बैठा हुआ अप्निके समान तेजस्वी विशालकाय बानर नहीं कहेंगे, तबतक पिताजीके निकट आपके विषयमें मै कुछ
- **Translation**: 

---

### Verse 20 (Mahabharat 0.2120)
- **Original**: ध्वजापर बैठा हुआ अप्निके समान तेजस्वी विशालकाय बानर नहीं कहेंगे, तबतक पिताजीके निकट आपके विषयमें मै कुछ
- **Translation**: 

---

