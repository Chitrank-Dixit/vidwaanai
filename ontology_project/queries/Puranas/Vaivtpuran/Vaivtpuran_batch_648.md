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

### Verse 1 (Vaivtpuran 66.17923)
- **Original**: स्मृतिर्मेधा च्व॒ बुद्धिवां ज्ञानशक्तिविपशिताम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 66.17924)
- **Original**: शूलिने कृपया सा त्वं यतो मृत्युज्लय: शिव:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 66.17925)
- **Original**: ब्रह्मविष्णुमहेशानां सा त्वमेव नमो5स्तु ते
- **Translation**: 

---

### Verse 4 (Vaivtpuran 66.17926)
- **Original**: स्तुत्वा मुप्रोच् यां देवीं तां मूर्शा प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 66.17927)
- **Original**: बभूव शक्तिमान्‌ स्तुत्वा तां दुर्गा प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 66.17928)
- **Original**: यां तुष्ठ॒वु: सुरा: सर्वे तां दुर्गा प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 66.17929)
- **Original**: जघान त्रिपुरं स्तुत्वा तां दुर्गां प्रणमाप्यहम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 66.17930)
- **Original**: वर्षतीन्रो दहत्यग्रिस्तां दुर्गा प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 66.17931)
- **Original**: मृत्युक्ति जन्लवोधे तां दुर्गा प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 66.17932)
- **Original**: संहर्ता संहरेत्‌ काले तां दुर्गा प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 66.17933)
- **Original**: यया बिना न शक्तश्न सृष्टि कर्तुँ नमामि ताम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 66.17934)
- **Original**: शिशूनामपराथेन कुतों माता हि कुप्यति
- **Translation**: 

---

### Verse 13 (Vaivtpuran 66.17935)
- **Original**: तुष्टा दुर्गा सम्भ्रमेण चाभय॑ च॑ वरें ददौ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 66.17936)
- **Original**: शर्वप्रसादात्‌ सर्वत्र जयोउस्तु तब संततम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 66.17937)
- **Original**: भ्क्तिर्भवतु ते कृष्णे शिवदे चर शिव गुरौ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 66.17938)
- **Original**: त॑ हन्तुं न हि शक्ताश्न रुष्टाश्न सर्वदेबता:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 66.17939)
- **Original**: गुरुपत्लीं स्तौषि यस्मात्‌ कस्त्वां हन्तुमिहेश्वर:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 66.17940)
- **Original**: अन्यदेवेषु ये भक्ता न भक्ता या निरड्भुशा:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.5773)
- **Original**: अस्त्र नहीं बेधता है। अवश्य ही वह जल या
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.5774)
- **Original**: दही, अन्न भोजन करावे और उसे सुवर्ण दान अग्रिमें प्रवेश कर सकता है। वहाँ उसकी मृत्यु
- **Translation**: 

---

