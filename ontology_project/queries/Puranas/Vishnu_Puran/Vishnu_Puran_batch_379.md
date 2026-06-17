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

### Verse 1 (Vishnu Puran 0.7561)
- **Original**: पृथुश्रवसश्च पुत्र: पृथुतमः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7562)
- **Original**: तस्मादुशना यो वाजिमेधानां शतमाजहार
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7563)
- **Original**: तस्थ च शितपुर्नाम पुत्रो5भवत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7564)
- **Original**: तस्यापि रुक्मकवचस्तत: परावृत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7565)
- **Original**: परावृतो रुकमेषु: पृथुज्यामघबलितहरितर्ज्ञास्तस्थ.. पद्चात्मजा खभूयु:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7566)
- **Original**: तस्थायमद्यापि ज्यामघस्य इलोको गीयते
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7567)
- **Original**: भार्यावद्यास्तु ये केचिद्धविष्यन्यथ वा पृता: । त्ेषां तु ज्यामघः श्रेष्ठहशैव्यापतिरभून्रप:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7568)
- **Original**: 13 अपुत्ना तस्य सा पत्नी जैव्या नाम तथाप्यसौ । अपतयामो5पि.भयान्नान्यां. भार्यामविन्द्त
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7569)
- **Original**: 14 स त्वेकदा प्रभूतरथतुरगगजसम्मर्दातिदारुणे महाहवे युद्धयमान: सकलमेवारिचिक्रमजयत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7570)
- **Original**: श्रीपराहरजी बोले--यदुपुत्र क्रोहके ध्वजिनीवान्‌ नामक पुत्र हुआ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7571)
- **Original**: उसके स्वाति, स्वातिके रुजंकु, रुशकुके चित्ररथ और चित्ररथके झशिनिन्दु नामक पुत्र हुआ जो चौदहों महारत्नोंकाँ स्वामी तथा चक्रचरतों सम्रादू था
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7572)
- **Original**: दादिव्न्दुके एक लाख सख्तरियाँ और दस ह्म्स्त पुत्र थे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7573)
- **Original**: उनमें पृथुअबा, पृथुकर्मा, पृथुकीर्ति, पृथुयशा, पृथुजय और पृथुदान--ये छः पुत्र प्रधान थे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7574)
- **Original**: पृथुश्रवाका पुत्र पृधुतम और उसका पुत्र उग़ना हुआ जिसने सौ अश्वमेघ-यज्ञ किया था
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7575)
- **Original**: उशनाके शितपु नामक पुत्र हुआ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7576)
- **Original**: शितपुके रुक्‍ममकलच, रुक्मकबचके परावुत्‌ तथा परावृत्के रुक्मेषु, पृथु, ज्यामध, वलित और हरित नामक पाँच पुत्र हुए। 10-11
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7577)
- **Original**: इनमेंसे ज्यामघके विषयमें अब भी यह इलोक गाया जाता है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7578)
- **Original**: रंसारमें स्वीके बशीभृत जो-जो लोग होंगे और जो जो पहले हो चुके हैं उनमें हौव्याका पति राजा ज्यामघ ही सर्वश्रेष्ठ है। 13
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7579)
- **Original**: उसकी स्ती दौव्या यह्यपि निःसन्तान थी तथापि सनन्‍्तानकी इच्छा रहते हुए भी उसने उसके भयसे दूसरी स्न्रीसे विवाह नहीं किया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7580)
- **Original**: एक दिन बहुत से रथ, घोड़े और हाथियोंके संघड्टसे अत्यन्त भयानक महायुद्धमें लड़ते हुए उसने अपने समस्त * चर्मसंडितामें चौदह रत्रोंका उल्लेख इस प्रकार किया है-- “चक्र रथो मणिः ख्डड़्श्चर्म सले च पञ्रमम्‌। केतुर्निधिश्व॒ सप्तेवः प्राणहीनानि चक्षते
- **Translation**: 

---

