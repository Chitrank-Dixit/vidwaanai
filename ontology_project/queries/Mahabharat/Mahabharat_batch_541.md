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

### Verse 1 (Mahabharat 0.5401)
- **Original**: डाल्म। अब सत्यसेनने पृथक्‌-पृथक्‌ दो बाण मारकर नकुछका चित्रसेनपर आक्रमण किया
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5401)
- **Original**: डाल्म। अब सत्यसेनने पृथक्‌-पृथक्‌ दो बाण मारकर नकुछका चित्रसेनपर आक्रमण किया
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5402)
- **Original**: उस समय चित्रसेन उसके ऊपर . धनुष और उसके रथका हरसा काट डाल्म । तब नकुछने रधझक्ति बाणोंकी बौछार करने लूगा। किंतु नकुल विचित्र प्रकारसे
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5402)
- **Original**: उस समय चित्रसेन उसके ऊपर . धनुष और उसके रथका हरसा काट डाल्म । तब नकुछने रधझक्ति बाणोंकी बौछार करने लूगा। किंतु नकुल विचित्र प्रकारसे
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5403)
- **Original**: हाथमें ली और बहुत ऊँचे उठाकर सत्बसेनपर दे मारी
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5403)
- **Original**: हाथमें ली और बहुत ऊँचे उठाकर सत्बसेनपर दे मारी
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5404)
- **Original**: युद्ध करनेवाला था, उसने चित्रसेनके बाणोंकरो'ढालपर ही
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5404)
- **Original**: युद्ध करनेवाला था, उसने चित्रसेनके बाणोंकरो'ढालपर ही
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5405)
- **Original**: उसकी चोटसे सत्यसेनकी छातीके सैकड़ों टुकड़े हो गये सेककर नष्टकर दिया तथा सम्पूर्ण सेनाके सामने ही
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5405)
- **Original**: उसकी चोटसे सत्यसेनकी छातीके सैकड़ों टुकड़े हो गये सेककर नष्टकर दिया तथा सम्पूर्ण सेनाके सामने ही
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5406)
- **Original**: और वह प्राणहीन होकर जमीनपर जा पढ़ा। बिंत्रसेनके रथ्षपर चढ़कर उसने उसके कुण्डल और मुकुटसे .. भाईको मरा देख सुषेण क्रोधमें धरं गया और नकुलके सुझोधित मस्तकको घड़से अलग कर दिया। किप्रसेनका
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5406)
- **Original**: और वह प्राणहीन होकर जमीनपर जा पढ़ा। बिंत्रसेनके रथ्षपर चढ़कर उसने उसके कुण्डल और मुकुटसे .. भाईको मरा देख सुषेण क्रोधमें धरं गया और नकुलके सुझोधित मस्तकको घड़से अलग कर दिया। किप्रसेनका
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5407)
- **Original**: ऊपर बाणोंकी वृष्टि करने छूगा। उसने चार सायकोसे मस्तक रथके पीछे भागमें गिर पड़ा।
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5407)
- **Original**: ऊपर बाणोंकी वृष्टि करने छूगा। उसने चार सायकोसे मस्तक रथके पीछे भागमें गिर पड़ा।
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5408)
- **Original**: नकुलके चारों घोड़ोंकों मार डाला, पाँचसे रथकी ध्वजा काट उसको मरा हुआ देख पाण्डव-महारथी सिंहनाद करने
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5408)
- **Original**: नकुलके चारों घोड़ोंकों मार डाला, पाँचसे रथकी ध्वजा काट उसको मरा हुआ देख पाण्डव-महारथी सिंहनाद करने
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5409)
- **Original**: दी और तीनसे सारथिकों भी यमत्मेक पठा दिया। नकुलूको लंगे। किंतु कर्णके महारथी पुत्र सुषेण और संत्यसेन तौखे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5409)
- **Original**: दी और तीनसे सारथिकों भी यमत्मेक पठा दिया। नकुलूको लंगे। किंतु कर्णके महारथी पुत्र सुषेण और संत्यसेन तौखे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5410)
- **Original**: रथहीन देख द्रोपदीकुमार सुतसोम दौड़कर यहाँ आ पहुँचा। बाणोंकी वर्षा करते हुए नकुलपर टूट पड़ें। उनके बाणोंसे
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5410)
- **Original**: रथहीन देख द्रोपदीकुमार सुतसोम दौड़कर यहाँ आ पहुँचा। बाणोंकी वर्षा करते हुए नकुलपर टूट पड़ें। उनके बाणोंसे
- **Translation**: 

---

