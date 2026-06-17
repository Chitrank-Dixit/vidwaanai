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

### Verse 1 (Vishnu Puran 0.12961)
- **Original**: जो उन्हींके समान गुणोंको भोगनेवाला है, एक होकर भी अनेक रूप है तथा शुद्ध होकर भी विभिन्न रूपॉंके कारण अशुद्ध-(विकारवान्‌-) सा अतीत होता है और जो ज्ञानस्वरूप एवं समस्त भूत तथा विभूतियोंका कर्ता है उस नित्य अव्यय पुरुषको नमस्कार है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12962)
- **Original**: जो ज्ञान (सत्त्व), प्रवृत्ति (सज) और नियमन (तम) की एकतारूप है, पुरुषक्तरे भोग प्रदान करनेमें कुशल है, त्रिगुणात्मक तथा अब्याकृत है, संसास्की उत्पत्तिका कारण है, उस स्वतःसिद्ध तथा जराश्ून्य प्रभुको सर्वदा नमस्कार करता हूँ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12963)
- **Original**: जो आकाश, वायु, अग्नि, जल और पृथिवीरूप है, शब्दादि भोग्य॑ विषयोंकी प्राप्ति करानेमें समर्थ है और पुरुष्का उसकी समस्त इन्द्रियों्राण उपकार करता है उस सुक्ष्म और विद्दरूप व्यक्त परमात्माको नमस्कार करता हूँ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12964)
- **Original**: इस प्रकार जिन नित्य सनातन परमात्माके प्रकृति- पुरुषमय ऐसे अनेक रूप हैं वे भगवान्‌ हरि समस्त पुरुषोंकों जन्म और जरा आदिसे रहित (मुक्तिरूप) हरिरपजन्यजरादिकां स सिद्धिम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12965)
- **Original**: सिद्धि प्रदान करें
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12966)
- **Original**: इति श्रीविष्णुपुराणे चष्ठेंडशो अष्टमोउध्याय:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12967)
- **Original**: अन्‍न्‍नबन्णगण्ा, है. $ अक्‍स+ इति श्रीपराशरमुनिविरचिते श्रीविष्णुपरत्वनिर्णायके श्रीमति णे पष्टोंउझ समाप्त: । इति श्रीकिष्णुमहापुराणं सम्पूर्णम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12968)
- **Original**: श्रीसिष्णवर्षणमस्तु
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12969)
- **Original**: समाप्त
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12970)
- **Original**: श्रीविष्णुपुराणान्तर्गतश्लोकानामकारादिक्रमेणानुक्रम:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12971)
- **Original**: श्रीहरिः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12972)
- **Original**: जज ह् 5 अंज्ञाः अध्या0. इल्लो0 इल्मेकाः अद्ञास्सुतीधापत्यम्‌ 1 डे 8.
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12973)
- **Original**: अचिरादागमिष्यामि 3 12 36
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12974)
- **Original**: अचिक्तयश्ष कौत्तेयः 3 16 62
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12975)
- **Original**: अच्छेनागन्थलेपेन 15 13 50
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12976)
- **Original**: अच्यूतोजपि तहिव्य॑ रलम्‌ 1 26 37 । अच्युतोःप्यतिप्रणतात्तस्मात्‌ 3 16. 7
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12977)
- **Original**: अजयइल्देवस्तम्‌ 4 13 67
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12978)
- **Original**: अजमीदद्विजमोठपुरुमीढाः ड 13 108
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12979)
- **Original**: अजमोदात्कण्व: 5. हैं7 1
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12980)
- **Original**: अजमीठस्पान्यः पुत्र: 5 18 30
- **Translation**: 

---

