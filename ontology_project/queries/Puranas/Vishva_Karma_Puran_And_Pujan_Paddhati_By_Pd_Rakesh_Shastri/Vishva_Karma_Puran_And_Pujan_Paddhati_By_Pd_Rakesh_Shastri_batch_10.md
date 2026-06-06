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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.181)
- **Original**: अथध्यानम्‌
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.182)
- **Original**: सहस्त्रवददनोदाहुः सहस्नाक्ष: सहस्त्रपात्‌
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.183)
- **Original**: आदिपुरुष ईशान आदिब्रह्मकुलोद्भव
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.184)
- **Original**: विश्वकर्मा सदाध्येयोनील मेघो परिस्थितः
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.185)
- **Original**: सर्वाभरणसंयुक्तो रत्नसिंह सनस्थितः
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.186)
- **Original**: इति ध्यात्वा
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.187)
- **Original**: मानसोपचार संपूजयेत
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.188)
- **Original**: तच्चेयम्‌
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.189)
- **Original**: लं॑ पृथ्वीतत्वात्मेनगंधत न्माञ्रप्रकृत्यानंदात्मने श्री गुरु विश्व कर्म पर ब्रह्मणेनमः
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.190)
- **Original**: गंघसमर्पयामि
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.191)
- **Original**: हूं आकाशतत्वात्मने शब्द तन्मान्रप्रकृत्यानंदात्मने श्री गुरु विश्वकर्म परब्रह्मणे नमः
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.192)
- **Original**: दीपंदरश्यामि
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.193)
- **Original**: यं आपतत्वात्मनेरस तन्माञप्रत्यानंदात्मने श्री गुरु विश्वकर्म परब्रह्मणे नमः
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.194)
- **Original**: अमृतनैद्य॑ समर्पयामि सं सर्वततत्वात्मने सर्वतत्वात्मने प्रकृत्यानंदात्मने श्री गुरु विश्वकर्म परब्रह्मणे नमः
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.195)
- **Original**: मर्वो पवाशन्‌ समर्पयामि
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.196)
- **Original**: अथमूल मंत्र:
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.197)
- **Original**: ऊँ ऊँ क्लीं हीं विश्वकर्म ब्रह्मोविशक्ति:
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.198)
- **Original**: सर्वकार्यमेव शंकूस हुं फट स्वाहा
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.199)
- **Original**: वैदलक्षपुरश्चरणनासिद्धि:
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.200)
- **Original**: 400000 उतरन्यासः
- **Translation**: 

---

