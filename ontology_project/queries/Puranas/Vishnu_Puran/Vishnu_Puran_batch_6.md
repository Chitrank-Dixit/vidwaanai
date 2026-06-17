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

### Verse 1 (Vishnu Puran 0.101)
- **Original**: भणवान्‌ विष्णु जो न्यक्त, अव्यक्त, पुरुष और कालरूपसे स्थित होते हैं, इसे उनकी खात्यत्‌ फ्रीडा ही समझो
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.102)
- **Original**: उनमेंसे अव्यक्त कारणको, जो सदसद्रूप (कारण- शक्तिविशिष्ट) और नित्य (सदा एकरस) है, ओष्ठ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.103)
- **Original**: अ*2) अक्षय्थे नान्यदाघारप्भेयमजर ध्रुंवम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.104)
- **Original**: शब्दस्पर्शलिधीय॑. तद्गुपादिभिरसंहितय
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.105)
- **Original**: 20 ब्रिगुणं._ तज्जणद्योनिरनादिप्रभवाप्यसम्‌ । तेनाग्रे सर्वधेयासीदमाप्त वे। प्रल्यादनु
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.106)
- **Original**: 21 लेदखादलिदों विद्वन्नियता ग्रह्मयवादिन: । गठच्ति चेतसेयार्थ प्रधानप्रतिपादकम
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.107)
- **Original**: 22 नाहो न सत्रिन नभो ने धूमि- नसीक्रमोज्योतिरभूश॑नान्यत्‌ । श्रोज्रादितुद्धयानुपलभ्यपेक प्राधानिकं ब्रह्म पुमास्तदार्ीतू
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.108)
- **Original**: 23 ब्िष्णो: स्वरूपात्परतो हि ते द्वे रूपे प्रधान पुरुषक्ष तिप्र । तस्वैद ' तेज्येन धृते . दियुक्ते रूपान्तरं तद॒द्विंज कांल्संज्ञप्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.109)
- **Original**: 24 प्रकृतो संस्थितं व्यक्तमतीतप्रत्त्ये तु यत्‌। तस्माओआकृतसंज्ञोउयमुच्यते. प्रतिसक्षर:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.110)
- **Original**: 27 अनादिभंगवान्कालो नान्तोजत्य द्विव विद्चते। अय्युक्तिप्नासतस्लेते. सर्गस्थित्यन्तुसंयमा:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.111)
- **Original**: 26 शुणसाम्ये ततस्तस्मिन्‍्पृथक्युंसि व्यवस्थित । काल्कस्वरूप . तह्विष्णोपम्रिय.. परियवरत्तते
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.112)
- **Original**: 27 ततस्तु तत्परं ब्रह्म परमात्मा जगन्मयः। सर्थग: सर्वमूतेशः सर्बात्मा परमेश्वर:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.113)
- **Original**: 28 प्रधानपुरुषो सांपि प्रविश्यात्मेच्छया हरि: । क्षोभयामास सम्प्राप्ते सर्गकाले व्ययाव्ययों
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.114)
- **Original**: 29 सथा सन्निधिमात्रेण गन्ध; क्षीभाय जायते । मनसो नोपकर्तृत्वात्तथाइसी परमेश्वर:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.115)
- **Original**: 30 स एव क्षो भको अहान्‌ क्षेभ्यअ पुरुषोत्तम: । स सझ्लोचविकासाभ्या प्रधानस्केषपि चर स्थित्त:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.116)
- **Original**: 39 विकासाणुस्वरूपेश्र ग्रह्मरूपादिभिस्तथा । व्यक्तस्वरूपश्न तथा विध्णः सर्वेश्वरेश्वर:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.117)
- **Original**: 32 प्रथम अंक वे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.118)
- **Original**: मुनिजन प्रधान सथा सुक्ष्म प्रकृति कहते हैं । 69
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.119)
- **Original**: वह क्षयरहित है, डसका कोई अन्य आश्वार भी नहीं है तथा अप्रमेय, अजर, निश्क शाब्ड-स्पर्शीदिशुन्य और रूपादिरशित है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.120)
- **Original**: यह ब्रिगुंणमंथ और जगत्‌का कारण है तथा स्वर्य अनादि एज उत्पत्ति ओर लूयसे रहित है। यह सम्पूर्ण प्रपक्ष प्रलमकालसे केक्तर सृश्टिके आदितक इस्रीसे व्याप्त था
- **Translation**: 

---

