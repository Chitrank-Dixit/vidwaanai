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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.161)
- **Original**: गायत्रीछंद:
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.162)
- **Original**: सदा शिवो देवता
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.163)
- **Original**: ऊँ अंबीनमू
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.164)
- **Original**: विश्वकर्म ब्रह्मशक्तिः
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.165)
- **Original**: प्रपंचाक्षरंकीलकम्‌
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.166)
- **Original**: श्रीमद्विश्वि कर्मपरब्रह्म मूलमंत्र जपे विनियोग:
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.167)
- **Original**: ऊँ अंगुष्ठाभ्यां नम:
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.168)
- **Original**: ऊँ? क्लीं तर्जनीभ्याम नमः
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.169)
- **Original**: ऊँ हीं मध्यमाभ्यां नमः
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.170)
- **Original**: ऊँ अं अनामिकाभ्यां नमः
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.171)
- **Original**: ऊँ कलीं कनिष्ठिकाश्यां नमः
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.172)
- **Original**: ऊँ ही करतलकर पृष्ठाभ्यां नमः
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.173)
- **Original**: एवं हृदयादिषडंगन्यासः
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.174)
- **Original**: ऊँ? अं सचद्यो जात मुखोदूभवायंमनु विश्वव्रह्म सान मात्यने हृदयाय नमः
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.175)
- **Original**: ऊँ? क्लीं वामदेव मुखोद्धवायमय विश्व ब्रह्म सनातनात्मने: शिरसे स्वाहा
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.176)
- **Original**: ऊँ हीं अधघोरमुखजन्मनेत्वष्ट्र विश्वब्रह्माहमूनात्मने शिरषा यैवषटू
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.177)
- **Original**: उँ0 कलीं तत्पुरुषमुख जन्मनेशिल्पि विश्व्रह्म प्रत्नात्मनेकवचायहुं
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.178)
- **Original**: ऊँ हीं ईशानमुख जन्मने अर्क विश्वव्रह्सपूर्णात्मने नेननयायवौषटू
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.179)
- **Original**: ऊँ? अं कश्यप विश्वकर्म विराटस्वरूपमित्यस्राय फट
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.180)
- **Original**: भूर्भुवः स्वरोमितिदिग्बंध:
- **Translation**: 

---

