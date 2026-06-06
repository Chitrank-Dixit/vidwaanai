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

### Verse 1 (Vaivtpuran 9.2256)
- **Original**: 3*हीं-स्वरूपिणी देवीके लिये श्रद्धाकी आहुति हैं। अखिल तत्त्वपरिज्ञानपूर्वक सम्पूर्ण अर्थके दी जाती है, वे अग्रिकोणमें रक्षा करें। साधन तथा समस्त कविताओंके प्रणयन एवं
- **Translation**: 

---

### Verse 2 (Vaivtpuran 9.2257)
- **Original**: “ ऐं हीं श्रीं क्लीं सरस्वत्य बुधजनन्यै स्वाहा।' विवेचनमें इसका 'प्रयोग किया जाता है। इसको मन्त्रराज कहते हैं। यह इसी रूपमें श्रीं-हीं-स्वरूपिणी भगवती सरस्वतीके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 9.2258)
- **Original**: सदा विराजमान रहता है। यह निरन्तर मेरे दक्षिण लिये श्रद्धाकी आहुति दी जाती है, वे सब ओरसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 9.2259)
- **Original**: भागकी रक्षा करे। ऐं हीं श्रीं-यह त््यक्षरमन्त्र मेरे सिरकी रक्षा करें। 3 श्रीं बाग्देबताके लिये
- **Translation**: 

---

### Verse 5 (Vaivtpuran 9.2260)
- **Original**: नैर्ऋत्यकोणमें सदा मेरी रक्षा करें। कविकी श्रद्धाकी आहुति दी जाती है, वे सदा मेरे ललाटकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 9.2261)
- **Original**: जिह्वाके अग्रभागपर रहनेबाली 3#-स्वरूपिणी रक्षा करें। 3» हीं भगवती सरस्वतीके लिये
- **Translation**: 

---

### Verse 7 (Vaivtpuran 9.2262)
- **Original**: देवीके लिये श्रद्धाकी आहुति दी जाती है, वे श्रद्धाकी आहुति दी जाती है, वे निरन्तर कानोंकी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 9.2263)
- **Original**: पश्चिम दिशामें मेरी रक्षा करें। 3%-स्वरूपिणी रक्षा करें। 30 श्रीं-हों भारतीके लिये श्रद्धाकी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 9.2264)
- **Original**: भगवती सर्वाम्बिकाके लिये श्रद्धाकी आहुति दी आहुति दी जाती है, वे सदा दोनों नेत्रोंकी रक्षा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 9.2265)
- **Original**: जाती है, वे वायव्यकोणमें सदा मेरी रक्षा करें। करें। ऐं-हों-स्वरूपिणी वाग्वादिनीके लिये श्रद्धाकी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 9.2266)
- **Original**: गद्य-पद्यमें निवास करनेवाली 35ऐ. श्रींमयी आहुति दी जाती है, वे सब ओरसे मेरी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 9.2267)
- **Original**: देवीके लिये श्रद्धाकी आहुति दी जाती है, वे नासिकाकी रक्षा करें। 3» हीं विद्याकी अधिष्ठात्री
- **Translation**: 

---

### Verse 13 (Vaivtpuran 9.2268)
- **Original**: उत्तर दिशामें मेरी रक्षा करें। सम्पूर्ण शास्त्रोंमें देवीके लिये श्रद्धाकी आहुति दी जाती है, बे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 9.2269)
- **Original**: विराजनेबाली ऐं-स्वरूपिणी देवीके लिये श्रद्धाकी होठकी रक्षा करें। 3 श्रीं-हीं भगवती ब्राह्मीके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 9.2270)
- **Original**: आहुति दी जाती है, वे ईशानकोणमें सदा मेरी लिये श्रद्धाकी आहुति दी जाती है, वे दन्त-
- **Translation**: 

---

### Verse 16 (Vaivtpuran 9.2271)
- **Original**: रक्षा करें। 5» हॉं-स्वरूपिणी सर्वपूजिता देवीके पड्कक्तिकौ निरन्तर रक्षा करें। 'ऐं” यह देवी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 9.2272)
- **Original**: लिये श्रद्धाका आहुति दी जाती है, वे ऊपरसे सरस्वतीका एकाक्षर-मन्त्र मेरे कण्ठको सदा रक्षा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 9.2273)
- **Original**: मेरी रक्षा करें। पुस्तकमें निवास करनेवाली ऐं- करे। 3* श्रीं हीं मेरे गलेकी तथा श्रीं मेरे कंधोंकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 9.2274)
- **Original**: हीं-स्वरूपिणी देवीके लिये श्रद्धाकी आहुति दी सदा रक्षा करे। 35% श्रीं विद्याकी अधिष्ठात्री देवीके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 9.2275)
- **Original**: जाती है, वे मेरे निम्नभागकी रक्षा करें। लिये श्रद्धाकी आहुति दी जाती है, बे सदा
- **Translation**: 

---

