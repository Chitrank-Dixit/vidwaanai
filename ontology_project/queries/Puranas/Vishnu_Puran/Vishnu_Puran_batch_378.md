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

### Verse 1 (Vishnu Puran 0.7541)
- **Original**: डसके राज्यमें कोई भी पदार्थ नष्ट नहों होता था
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7542)
- **Original**: इस प्रकार उसने बल, पराक्रम, आरोग्य और सम्पत्तिक्य्रे सर्वथा सुरक्षित रखते हुए पचासी हजार बर्ष राज्य किया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7543)
- **Original**: एक दिन अब वह अतिशय मचद्य- पानसे व्याकुछ हुआ नर्मदा नदीमें जल-क्रीडा कर रहा उसकी राजधानी माहिष्मतीपुरीपर दिग्विजयके किये आये हुए साप्पूर्ण देव, दानव, गन्धर्व और राजाओंके विजय मदसे उन्मत्त रावणने आक्रमण किया, उस समय उसने अनायास ही राबणको पशुके समान बांधकर अपने नगरके एक निर्जन स्थानमें रख दिया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7544)
- **Original**: इस सहस्त्रार्जुनकां पच्चासी हजार वर्ष व्यतीत होनेपर झगवान्‌ नारायणके अंशायतार परणशुरामजीने वध किया था
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7545)
- **Original**: इसके सौ पुजोंगेंसे शूर, शूरसेन, वृषसेन, मध जयध्यज्ञ--ये पाँच प्रधान थे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7546)
- **Original**: जयध्वजका हक ताल्जंघ हुआ और तालजंघके ताल्जैघ नामक सौ पुत्र हुए इनमें सबसे बड़ा वीतिहोत्र तथा दूसरा भरत था
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7547)
- **Original**: 22--24
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7548)
- **Original**: भरतके वृष, वुषके पथु और मधुके वृष्णि आदि सौ पुत्र हुए
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7549)
- **Original**: 27--27
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7550)
- **Original**: अष्णिके कारण यह बैड यूष्णि कहल्याया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7551)
- **Original**: मधघुके कारण इसकी मधु-संज्ञा हुई
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7552)
- **Original**: और यदुके नामानुसार इस चंशके स्त्रेग यादव कहलाये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7553)
- **Original**: 30 । 5 ड््थ हज >-डडडड््अ इति श्रीविष्णुपुराणे चतुर्थेषरो एकादशोउध्यायः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7554)
- **Original**: डक च है 4 अ+-
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7555)
- **Original**: 268 श्रीविष्णुपुराण [ आ 12 बारहवाँ अध्याय यदुपुत्र क्रोौष्ठुका वंश श्रीपरागर उवाय क्रोष्टोस्तु यदुपुत्नस्थात्मजों ध्वजिनीवान्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7556)
- **Original**: ततश्ष स्वातिस्ततो रुशडू. रुशड्डोश्चित्रस्थ:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7557)
- **Original**: . तत्तनयद्शशिबिन्दुअतुर्दशमहारल्ले- शाश्चक्रवर्त्भभवत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7558)
- **Original**: तस्थ च झतसहस्न पत्नीनामभवत्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7559)
- **Original**: दशलक्षसंख्याश्न पुत्रा:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7560)
- **Original**: तेषां च पृथुश्रवा: पृथुकर्मा पृथ्ुकीर्ति: पृथुयज्ञा: पृथुजय: पृथुदान: घट पुत्रा: प्रधाना:
- **Translation**: 

---

