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

### Verse 1 (Vishnu Puran 0.8541)
- **Original**: अयुतायु, अयुतायुके निरमित्र, निरमित्रके सुनेत्र, सुनेत्रके विध्रस्तस्थ चर पुत्रइशुचिनामा भविष्यति
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8542)
- **Original**: बृहत्कर्मा, बृहत्कर्माके सेनजित्‌, सेनजितके भ्रुततय, तस्थापि क्षेम्यस्ततश्चल॒ सुत्रतस्सुव्रताद्धर्मस्तत-
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8543)
- **Original**: श्रुतज्यके तिप्र तथा तिप्रके शुत्षि नामक एक पुत्र होगा स्सुश्रवा:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8544)
- **Original**: . ततो. दृढसेनः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8545)
- **Original**: झुचिके क्षेम्य, क्षेम्यके सुजनत, सुत्रतके धर्म, तस्मात्सुबल:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8546)
- **Original**: सुबलात्सुनीतों भविता
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8547)
- **Original**: घर्मके सुश्रवा, सुश्रवाके दृढसेन, दृढसेनके सुबल,
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8548)
- **Original**: ततस्सत्यजित्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8549)
- **Original**: तस्माद्विश्वजित्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8550)
- **Original**: सुबलके सुनीत, सुनीतके सत्यजित्‌, सत्यजितके विश्वजित्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8551)
- **Original**: तस्यथापि. रिपुझ्जयः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8552)
- **Original**: और विश्वजितके रिपुल्षयका जन्म होगा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8553)
- **Original**: 6-- 12
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8554)
- **Original**: इस इत्येते बार्ईद्रथा भूषतयो वर्षसहस्रमेकक
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8555)
- **Original**: प्रकारसे बृहद्रथवंशीय राजागण एक सहस्तर वर्षपर्यन्त भरविष्यन्ति
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8556)
- **Original**: मगधमें शासन करेंगे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8557)
- **Original**: जा: है ॑ौ-+ इति श्रीविष्णुपुराणे चतुर्थेंडशे त्रयोविशोउध्याय:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8558)
- **Original**: अेाणण चोबीसवाँ अध्याय कलियुगी राजाओं और कल्धमॉँका वर्णन तथा राजवंद-वर्णवका उपसंहार श्रीपराशर उवाच श्रीपराशरजी बोले--बहद्रथर्वदाका.रिपुञ्रय नामक जो अन्तिम राजा होगा उसका सुनिक नामक एक बाहईद्रथो उन्त्यस्तस्थामात्यो किफ0 34330 0घ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8559)
- **Original**: स चैन स्वासिनं मनन्‍््नी होगा । वह अपने स्वामी रिपुझ्यको मारकर अपने हत्वा स्वपुत्रं प्रद्योततामानमभिषेक्ष्यति
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8560)
- **Original**: पुत्र प्रयोत्तका राज्याभिषेक करेगा। उसका पुत्र बछाक तस्यापि बलाकनामा पुत्रो भविता
- **Translation**: 

---

