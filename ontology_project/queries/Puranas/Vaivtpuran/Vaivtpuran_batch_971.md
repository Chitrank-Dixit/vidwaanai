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

### Verse 1 (Vaivtpuran 1216.17733)
- **Original**: ऐशान्यामेकदन्तक्ष हेरम्थः पातु चोर्ध्यत: । अधो गणाधिप: पातु सर्वपूज्यश्च सर्वतः
- **Translation**: 

---

### Verse 2 (Vaivtpuran 1216.17734)
- **Original**: स्वप्ने जागरणे चैव पातु मां योगिनां गुरु:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 1216.17735)
- **Original**: इति ते कथित वत्स सर्वमनत्रौधविग्नहम्‌ । संसारमोहनं नाम कवच परमाद्भुतम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 1216.17736)
- **Original**: श्रीकृष्णेण पुरा दत्त गोलोके रासमण्डले । वृन्दावने विनीताय महां दिनकरात्मज:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 1216.17737)
- **Original**: मया दत्त च तुथ्यं च यस्मै कस्मै न दास्यसि । पर॑ वरें सर्वपूज्य॑ सर्वसक्कुटतारणम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 1216.17738)
- **Original**: गुरुमभ्यर्चव्थविश्विवत्‌ कवच धारयेत्तु यः । कण्ठे वा दक्षिणे बराहौँ सो5पि विष्णुर्न संशय:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 1216.17739)
- **Original**: अश्वमेध्रसहस्राणि खाजपेयशतानि च॒ । ग्रहेद्धकवचस्यास्य कलां नाईन्ति षोड़शीम्‌।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 1216.17740)
- **Original**: डइदे कबचमज़ात्वा यो भजेच्छंकरात्मजम्‌ । शतलक्षप्रजप्तोषपि न मन्त्र: सिद्धिदायकः
- **Translation**: 

---

### Verse 9 (Vaivtpuran 1216.17741)
- **Original**: इति अीग्रह्मवँवर्ते शनै्वर प्रति विष्णुनोप्रदिर्ट संसारमोहत॑ गणेशकवर्च सम्पूर्णम्‌। (गणपतिखण्ड 13। 78-96) >+>रशय 00000
- **Translation**: 

---

