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

### Verse 1 (Bramha 0.5621)
- **Original**: ही तप और आप ही जनलोक हैं। आप विजयो पुरुषोंमें श्रेष्ठ! आपकी जय हो। श्रीकृष्ण!
- **Translation**: 

---

### Verse 2 (Bramha 0.5622)
- **Original**: विश्वविजेता, कल्याणमय, शरणागतपालक, अविनाजञी, आप अजित और अख़ण्ड हैं। श्रीनिवास! आपको
- **Translation**: 

---

### Verse 3 (Bramha 0.5623)
- **Original**: शम्भु, स्वयम्भू, ज्येट और परायण (परम आश्रय) नमस्कार है। आप ही बादल और धूम--वर्षा और : हैं। आदित्य, ओंकार, प्राण, अन्धकारनाशक सूर्य,
- **Translation**: 

---

### Verse 4 (Bramha 0.5624)
- **Original**: « कण्डुपुनिका चरित्र और मुनिपर भगवातू पुरुषोत्तपकी कृपा « 271 मेघ, सर्वत्र विख्यात तथा देवताओंके स्वामी ब्रह्म
- **Translation**: 

---

### Verse 5 (Bramha 0.5625)
- **Original**: अन्य वृक्ष हैं। व्यक्त जगत्‌ और प्रजापति भी आप भी आप ही हैं। ऋक्‌, यजुः और साम भी आप
- **Translation**: 

---

### Verse 6 (Bramha 0.5626)
- **Original**: ही हैं। आपकी नाभिसे सुबर्णमय कमल प्रकट ही हैं। आप हो सबके आत्मा माने गये हैं। आप
- **Translation**: 

---

### Verse 7 (Bramha 0.5627)
- **Original**: हुआ है। आप दिव्य शक्तिसे सम्पन्न हैं। आप ही ही अग्नि, आप ही वायु, आप ही जल और आप
- **Translation**: 

---

### Verse 8 (Bramha 0.5628)
- **Original**: चद्धमा और आप ही प्रजापति हैं। आपके ही पृथ्वी हैं। स्रष्टा, भोका, होता, हविष्य,यज्ञ,
- **Translation**: 

---

### Verse 9 (Bramha 0.5629)
- **Original**: स्वरूपका वर्णव नहीं किया जा सकता। आप प्रभु, विभु, श्रेष्ठ, लोकपति और अच्युत भी आप
- **Translation**: 

---

### Verse 10 (Bramha 0.5630)
- **Original**: ही यम और आप ही दैत्योंके नाशक श्रीविष्णु ही हैं। आप सबके द्रष्टा और लक्ष्मीबान्‌ हैं। आप
- **Translation**: 

---

### Verse 11 (Bramha 0.5631)
- **Original**: हैं। आप हो संकर्षण देव हैं। आप ही कर्ता ही सबका दमन करनेवाले और शत्रुओंके नाशक
- **Translation**: 

---

### Verse 12 (Bramha 0.5632)
- **Original**: और आप ही सनातन पुरुष हैं। आप तीनों हैं। आप ही दिन और आप ही रात्रि हैं, विद्वान्‌
- **Translation**: 

---

### Verse 13 (Bramha 0.5633)
- **Original**: गुणोंसे रहित हैं। पुरुष आपको ही वर्ष कहते हैं। आप ही काल, आप ज्येष्ठ, वरिष्ठ और सहिष्णु हैं। लक्ष्मीके हैं। कला, काझ्ठा, मुहूर्त, क्षण और लव-सग
- **Translation**: 

---

### Verse 14 (Bramha 0.5634)
- **Original**: पति हैं। आपके सहस्रों मस्तक हैं। आप अव्यक्त आपके हो स्वरूप हैं। आप ही बालक, आप ही , देवता हैं। आपके सहल्नों नेत्र और सहस्तरों चरण यृद्ध तथा आप ही पुरुष, स्त्री और नपुंसक हैं।
- **Translation**: 

---

### Verse 15 (Bramha 0.5635)
- **Original**: हैं। आप विराट्‌ और देवताओंके स्वामी हैं। आप विश्वको उत्पत्तिके स्थान हैं। आप ही सबके
- **Translation**: 

---

### Verse 16 (Bramha 0.5636)
- **Original**: देवदेव! तथापि आप दस अँगुलके होकर रहते नेत्र हैं। आप हो स्थाणु (स्थिर रहनेवाले) और
- **Translation**: 

---

### Verse 17 (Bramha 0.5637)
- **Original**: हैं। जो भूत है, वह आपका ही स्वरूप बताया आप ही शुचिश्रवा (पवित्र यशवाले) हैं। आप
- **Translation**: 

---

### Verse 18 (Bramha 0.5638)
- **Original**: गया है। आप हो अन्तर्यामी पुरुष, इन्द्र और उत्तम सनातन पुरुष हैं। आपको कोई जीत नहीं सकता।
- **Translation**: 

---

### Verse 19 (Bramha 0.5639)
- **Original**: देवता हैं। जो भविष्य है, वह भी आप ही हैं। आप इन्द्रके छोटे भाई उपेन्द्र और सबसे उत्तम
- **Translation**: 

---

### Verse 20 (Bramha 0.5640)
- **Original**: आप हो ईशान, आप ही अमृत और आप ही मर्त्य हैं। आप सम्पूर्ण विश्वको सुख देनेवाले हैं। वेदोंके
- **Translation**: 

---

