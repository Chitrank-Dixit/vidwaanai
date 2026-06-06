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

### Verse 1 (Vishnu Puran 0.13141)
- **Original**: किमिरद देवदेव: 3 8 (157 23
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13142)
- **Original**: किमिदमेकदैव 0 36390 664 6. 35
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13143)
- **Original**: किमेठदिहि सिद्धानाम्‌ है70/
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13144)
- **Original**: 4ह0/ 19 ह3 इड
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13145)
- **Original**: किसुव्यामबगोपात्मः च््फड 9 115 84
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13146)
- **Original**: ज्टोटफु्डसपस्प्‌ 56 बेड जुट 17 26
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13147)
- **Original**: किशेटसरकेपूर द्ध 0छ 75 द्ड सर 316
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13148)
- **Original**: किफगोमोति त़न्सर्थीन्‌ 31 71344 4737 13 531 (सीडन
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13149)
- **Original**: - 244 लश्एट8 जूस ह्ड 56 ता 7774539239.7.2 हट प्र &- धन 3 स्ष्ल्र्न्ः 2 1152
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13150)
- **Original**: किंदेवेःकि ट्िजैगेंदेः ना. है क्ाश्ाका पर छू 40...
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13151)
- **Original**: कि देवे: किमनत्तेत *-.. #लाणर्‌ट र 38 8 «5
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13152)
- **Original**: ऊिनपदयमि दुल्पेत ना. 5 उ>रणऋाचछ 28 हट
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13153)
- **Original**: भमिगद्होआ्मर्फठ: “+.. 7जशइव्म्ब्अड 312 19
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13154)
- **Original**: किनबेतिप्पहेशव व्योहत<9 ते ट्र5 10. 7
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13155)
- **Original**: फिनयेटिनृइसोध्यम्‌ 5 हट 20 22 485
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13156)
- **Original**: फिपुनस्तु संत्यक्त का आ्ट्ध 7 हर इंड 26 किममार विभेदधीतिं 4;काए0जलू2 दंड 37... किवदामिसुगायस्थ 2 हर 7 उह7 13 1620
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13157)
- **Original**: किलासर्वजगारूष्ट ध + 07202. 23 116
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13158)
- **Original**: के त्रकेमशिणे व्यापैः नतः.. रेजरएु
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13159)
- **Original**: ज्यरड 8 4120.
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13160)
- **Original**: कि बश्नक्तोझाल्पमश्यलन्‌ >*.. रााशइ्तगाइर 23 1157
- **Translation**: 

---

