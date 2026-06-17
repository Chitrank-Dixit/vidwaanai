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

### Verse 1 (Vaivtpuran 17.994)
- **Original**: निःस्पृष्ठ हो अपने पाँच मुखोंसे उनके नाम और बालक हो तो भी सूर्यसे बढ़कर तेज धारण करते
- **Translation**: 

---

### Verse 2 (Vaivtpuran 17.995)
- **Original**: गुणोंका कोर्तन एवं गान करता हुआ सर्वत्र घूमता हो। तुम अपने तेजसे देवताओंकों भी तिरस्कृत
- **Translation**: 

---

### Verse 3 (Vaivtpuran 17.996)
- **Original**: रहता हूँ। उनके नाम और गुणोंके कीर्तनका ही करते हो; परंतु सबके हृदयमें अन्तर्यामी आत्मारूपसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 17.997)
- **Original**: यह प्रभाव है कि मृत्यु मुझसे दूर भागती है। विराजमान हमारे स्वामी सर्वेश्वर परमात्मा विष्णुको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 17.998)
- **Original**: निरन्‍्तर भगवन्नामका जप करनेवाले पुरुषको नहीं जानते हो, यह आश्चर्यकी बात है। उन
- **Translation**: 

---

### Verse 6 (Vaivtpuran 17.999)
- **Original**: देखकर मृत्यु पलायन कर जाती है। चिरकालतक परमात्माके ही त्याग देनेपर देहधारियोंका यह
- **Translation**: 

---

### Verse 7 (Vaivtpuran 17.1000)
- **Original**: तपस्थापूर्वक उनके नाम और गुणोंका कीर्तन शरीर गिर जाता है और सभी सूक्ष्म इन्द्रियवर्ग
- **Translation**: 

---

### Verse 8 (Vaivtpuran 17.1001)
- **Original**: करनेसे ही मैं समस्त ब्रह्माण्डोंका संहार करनेमें एवं प्राण उसके पीछे उसी तरह निकल जाते
- **Translation**: 

---

### Verse 9 (Vaivtpuran 17.1002)
- **Original**: समर्थ एवं मृत्युझ्रय हुआ हूँ। समय आनेपर मैं हैं, जैसे राजाके पीछे उसके सेवक जाते हैं।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 17.1003)
- **Original**: उन्हों श्रीहरिमें लोन होता हूँ तथा पुन: उन्हींसे जीव उन्हींका प्रतिबिम्ब है। वह तथा मन, ज्ञान,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 17.1004)
- **Original**: मेरा प्रादुर्भाव होता है। उन्हींकी कृपासे काल चेतना, प्राण, इन्द्रियवर्ग, बुद्धि, मेधा, धृति, स्मृति,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 17.1005)
- **Original**: मेरा संहार नहीं कर सकता और मौत मुझे मार निद्रा, दया, तन्द्रा, क्षुधा, तृष्णा, पुष्टि, श्रद्धा, नहीं सकती। ब्रह्मन्‌! जो श्रीकृष्ण गोलोकधाममें संतुष्टि, इच्छा, क्षमा और लज्जा आदि भाव
- **Translation**: 

---

### Verse 13 (Vaivtpuran 17.1006)
- **Original**: निवास करते हैं, वे ही बैकुण्ठ और श्रेतद्वीपमें उन्हींके अनुगामी माने गये हैं। वे परमात्मा जब
- **Translation**: 

---

### Verse 14 (Vaivtpuran 17.1007)
- **Original**: भी हैं। जैसे आग और उसकी चिनगारियोंमें कोई जानेको उद्यत होते हैं, तब उनकी शक्ति आगे-
- **Translation**: 

---

### Verse 15 (Vaivtpuran 17.1008)
- **Original**: अन्तर नहीं है, उसी प्रकार अंशी और अंशमें आगे जाती है। उपर्युक्त सभी भाव तथा शक्ति
- **Translation**: 

---

### Verse 16 (Vaivtpuran 17.1009)
- **Original**: भेद नहीं होता। इकहत्तर दिव्य युगोंका एक उन्हीं परमात्माके आज्ञापालक हैं। देहमें जबतक मन्वन्तर होता है। (प्रत्येक मन्वन्तरमें दो इन्द्र *कर्मारम्भे च मध्ये वा शेषे विष्णु च यः स्मरेत्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 17.1010)
- **Original**: परिपूर्ण तस्य कर्म वैदिक च भवेद्‌ द्विज
- **Translation**: 

---

### Verse 18 (Vaivtpuran 17.1011)
- **Original**: (ब्रह्मबण्ड 17। 18)
- **Translation**: 

---

### Verse 19 (Vaivtpuran 17.1012)
- **Original**: व्यतीत होते हैं।) अट्टाईसवें * इन्द्रके गत होनेपर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 17.1013)
- **Original**: ब्रह्माजीकी आयुपर्यन्त कुम्भीपाक नरकमें पकाया ब्रह्माजीका एक दिन होता है। इसी संख्यासे जाता है। जहाँ श्रीहरिकी निन्‍दा होती है, वह विशिष्ट सौ वर्षकी आयुवाले ब्रह्माजीका जब पतन
- **Translation**: 

---

