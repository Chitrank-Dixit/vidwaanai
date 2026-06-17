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

### Verse 1 (Vishnu Puran 0.7181)
- **Original**: उसे आकाहामें ले जाते समय उर्वशीने
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7182)
- **Original**: आ0 6 ] आब्दमश्यूणोत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7183)
- **Original**: एबमुबाच च ममा- नाथायाः पुत्र: केनापह्ियते कं झरणमुपया- मीति
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7184)
- **Original**: तदाकर्ण्य राजा माँ नर देवी बीक्ष्यतीति न ययौ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7185)
- **Original**: अथान्यमप्युरणक- मादाय गन्धर्वा ययु:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7186)
- **Original**: तस्थाप्यपट्डिय- मराणस्थाकर्ण्य झब्दमाकाशे. पुनरष्यनाथा- राजाप्यमर्षवशादन्धकारमेतदिति खड्गमादाय दुष्ट दुष्ट हतोउसीति व्याहरन्नभ्यधावत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7187)
- **Original**: तावच्च॒ गन्धर्वैरप्पतोवोज्ज्वला. विद्युजजनिता
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7188)
- **Original**: तत्मभया चोर्मशी राजानमपगताम्बरं तत्क्षणादेबापक्रान्ता
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7189)
- **Original**: परित्यज्य तावप्युरणकोौ गन्धर्वास्सुरलोकमुपगता:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7190)
- **Original**: राजापि च तौ मेषावादायातिहष्टमना: स्वशयनपायातो नोर्वज्ञीं ददर्श
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7191)
- **Original**: तां चापश्यन्‌ व्यपगताम्बर एवोन्यत्तरूपो बश्राम
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7192)
- **Original**: कुरुक्षेत्र चाम्भोजसरस्यन्याभि- ज्षतसृभिरप्सरोभिस्समवेतामुर्वशों ददर्श
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7193)
- **Original**: ततश्लोन्यत्तरूपो जाये हे तिष्ठ मनसिधोरे तिष्ठ वचसि कपटिके..तिष्टेत्येबमनेकप्रकारं॑. सुक्त- मवोचत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7194)
- **Original**: आह चोर्वज्ञी
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7195)
- **Original**: महाराजाछमनेना- विवेकचेषप्टतिन
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7196)
- **Original**: अन्तर्वल्यहमब्दान्ते भ्रवतात्रागन्तव्यं कुमारस्ते भविष्यति एकां च॑ निशामहं त्वया सह बत्स्थामीत्युक्तः प्रहाश्स्स्वपुरें जगाम
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7197)
- **Original**: तासां चाप्सरसामुर्वशी कथयामास
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7198)
- **Original**: अयं स पुरुषोत्कृष्ठो येनाहमेतावन्त कालमनुरागा- कृष्टमानसा सहोषितेति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7199)
- **Original**: एशवमुक्तास्ता- श्ाप्सस उल्चु:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7200)
- **Original**: साधु साध्वस्य अब्दे च पूर्ण स॒ राजा तत्राजगाम
- **Translation**: 

---

