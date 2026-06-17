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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.201)
- **Original**: ऊँ अं सचद्योजात मुखोद्धवायमनु विश्वब्रह्मसानगात्मने हृदयाय नमः । उँ? क्लीं वामदेवमुखोद्धवायमय विश्वब्रह्म सनात्मने शिरसे स्वाहा
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.202)
- **Original**: ऊँ हीं अधघोरमुख जन्मनेत्वष्ट्र विश्वब्रह्माहभूतात्मने शिखायैवौषट
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.203)
- **Original**: ऊँ अं तत्पुरुष मुख जन्मने शिल्पि विश्वब्रह्मप्रत्ात्मनेकवचायहुं
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.204)
- **Original**: ऊँ? ईशान्मुख जन्मने अर्कब्रह्म सुपणत्मिने नेत्रनयायवौषट्
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.205)
- **Original**: ऊँ? अं कश्यप विश्वकर्म विराटू स्वरूपमित्यस्रायफट्‌
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.206)
- **Original**: भूर्भुवः स्वरोमिविदिग्बंधः । अथ ध्यानमू
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.207)
- **Original**: सहस्त्रवद नोदाहुः सहस्त्राक्ष: सहस्त्र पातू
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.208)
- **Original**: आदिपुरुष ईघानआदि ब्रह्मकुलोद्धवः
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.209)
- **Original**: यस्यस्मृत्या चनामोक्त्याजप- पूजादिकर्मसु
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.210)
- **Original**: न्यूनसं पूर्णतांयाति नमस्तद्विश्व कर्मणे
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.211)
- **Original**: ब्रह्मोवाच
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.212)
- **Original**: देवदेव महादेव भक्तानुग्रह कारक
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.213)
- **Original**: सुचितैकमनों ब्रह्मकवचंकथयस्वमे
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.214)
- **Original**: ईश्वर शी विश्वकर्मा पुराण एवं पूजन पद्धति 27
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.215)
- **Original**: अपातः संप्रवकष्यामिकवचदेव दुर्लभम्‌
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.216)
- **Original**: अप्रकाशपरं गुहयं सर्वाभिष्टस्य सिद्धिदमू
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.217)
- **Original**: विश्वकर्माख्यकवर्च श्रूणुष्वचतुरानन
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.218)
- **Original**: अस्यकवचस्य संप्रोक्ता कऋषयः सानगादय:
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.219)
- **Original**: अनुष्टुप छंद सश्वैवपर ब्रह्मादि दैवतमू
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.220)
- **Original**: धर्मज्ञानार्थसिध्यर्थ विनियोगः प्रकीर्तितः
- **Translation**: 

---

