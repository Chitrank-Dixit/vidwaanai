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

### Verse 1 (Vishnu Puran 0.881)
- **Original**: जिस शुद्धस्ररूप भगवान्‌की शक्ति (विभूति) कल्त-
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.882)
- **Original**: क्र श्रीविष्णुपुराण [अ9 अल थे विजन 4 पदानाम, परमेशो हि यः : अ्सीदतु स नो बिष्णुरात्मा यः स्वदिहिनाम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.883)
- **Original**: 46 य: कारणं च कार्य च कारणस्यापि कारणम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.884)
- **Original**: कार्यस्यापि च यः कार्य प्रसीदतु स नो हरि:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.885)
- **Original**: 47 कार्यकार्यत्य यत्कार्य तत्कार्यस्यापि यः स्वयम्‌ । तत्कारयकार्यभूतो यस्ततक्ष प्रणता: सम तम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.886)
- **Original**: 48 कारणं कारणस्यापि तस्य कारणकारणम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.887)
- **Original**: तत्कारणानां हेतु ते प्रणता: सम परेश्वरम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.888)
- **Original**: 49 न निशमट न मम भोग्यभूतं च सख्रष्टारं ते ग्रणताः सम पर पदम
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.889)
- **Original**: 50 ++्नन्त्न्न्र
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.890)
- **Original**: अव्यक्तमविकारे : परम पदम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.891)
- **Original**: 51 नस्‍्थूलं न च सूक्ष्म यन्न विशेषणगोचरम्‌ । तत्पद परम विष्णो: प्रणमामः सदाउमलम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.892)
- **Original**: 52 परब्रह्मस्वरूपं यदत्मणमामस्तमव्ययम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.893)
- **Original**: 53 यदोगिन: सदोश्युक्ता: पुण्यपापक्षये5क्षयम्‌। पह्यन्ति प्रणवे चित्त्य तद्विष्णो: परम पदम
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.894)
- **Original**: 54 जप जाल कक पड हे देवा न हे नचाहंन च शक्बर:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.895)
- **Original**: : परम पदम
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.896)
- **Original**: 55 झक्तयो यस्थ देवस्य ब्रह्मतिष्णुशिवात्पिका: । अवत्त्यभूतपूर्वस्थ तद्विष्णो: परम पदम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.897)
- **Original**: 56 अप छत जन ने कक सर्वाश्नयाच्युत । प्रसीद विष्णो भक्ताना क्रज
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.898)
- **Original**: 57 श्रीपराज्र उकाच इत्युदीरितमाकर्ण्य. ब्रह्मणस्तरिदशास्ततः । प्रणम्योचु: प्रसीदेति त्रज नो दृष्टिगोच्ररम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.899)
- **Original**: 58 यन्नाययं भगवान्‌ ब्रह्मा जानाति परम पदम्‌। तन्नता: सम जगद्धाप तब सर्वगताच्युत
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.900)
- **Original**: 59 काष्ठा और मुहर्स आदि काल-क्रमका विषय नहीं हैं, वें भगवान्‌ विष्णु हमपर प्रसन्न हों
- **Translation**: 

---

