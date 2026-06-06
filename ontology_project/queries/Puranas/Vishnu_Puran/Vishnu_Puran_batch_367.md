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

### Verse 1 (Vishnu Puran 0.7321)
- **Original**: तन्माता चर विश्वामित्र जनयामास
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7322)
- **Original**: सत्यवत्यपि कौजिकी नाम नद्यमबत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7323)
- **Original**: जमदग्रिरिक्ष्वाकुवंशोद्धलवस्थ. रेणोस्तनयां रेणुकामुपयेमे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7324)
- **Original**: तस्यां चाहोषक्षत्रहन्तारं परशुरामसंज्ञ भगवतस्सकललोकग्रोरनारायण- स्थांश॑ं जमदपग्रिस्जीजनत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7325)
- **Original**: विश्वामित्र- पुत्रस्तु भार्गव एवं शुनइशोपो देवेर्दत्त: ततश् देवरातनामाभवत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7326)
- **Original**: ततश्ान्ये मधुच्छन्दो- धनअञ्जयकृतदेबाष्टककच्छपहारीतकारूया विश्वामित्रपुत्रा अभूतुः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7327)
- **Original**: तेषां अल बहूनि कौशिकगोत्राणि ऋष्यत्तरेषु विवाह्या न्‍्यूभवन्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7328)
- **Original**: चतुर्थ अंझ 2691 तदनन्तर उसने जमदप्रिको जन्म दिया और उसकी साताने विश्वामित्रको उत्पन्न क्रिया तथा ससत्यवती कौडिकी नामकी नदी हो गयी
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7329)
- **Original**: 32--34
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7330)
- **Original**: खिताह किया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7331)
- **Original**: उससे जमदग्रिके सम्पूर्ण क्षत्रियोंका लैस करनेवाछे भगवान्‌ परशुयामजी उत्पन्न हूए जो सकल स्लेक-गुरु भगयान्‌ नारायणके ओऔद्या थे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7332)
- **Original**: देवताओंने विधामित्रजीको भृगुवंशीय शुनःझेप पुत्ररूपसे दिया था
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7333)
- **Original**: उसके पीछे उनके देवरात नामक एक पुत्र हुआ और फिर मधुच्छन्द, धनझ्य, कृतदेव, अष'्टक, कच्छप एज़े हारोतक नामक और भी पुत्र हुए
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7334)
- **Original**: उनसे अन्यान्य ऋषिवंद्ञॉ्में विवाहने योग्य बहुत-से कौशिक- गोत्रीय पुत्र-पौत्रादि हुए
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7335)
- **Original**: कि है न+-+-_5 इति श्रीविष्णुपुराणे चतुर्थेडशे सप्तमोउघ्यायः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7336)
- **Original**: ननन-+ जैर विलनन आठवाँ अध्याय कादयवंशका वर्णन औपयशर उवाच पुरूरवसो ज्येष्ठः पुत्रो यस्त्वायुर्नामा स राहो- दुड्धितरमुपयेमे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7337)
- **Original**: तस्यां च पश्ञ पुत्रानुत्पादया- मास
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7338)
- **Original**: नहुषक्षत्रवृद्धरम्भरजिसंज्ञास्तथै- खानेना: पदश्चमः पुत्रोउभूत्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7339)
- **Original**: क्षत्रवृद्धा- त्सुहोत्र: पुत्रो$भवत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7340)
- **Original**: काइयकाशगृत्स- मरदाखयस्तस्य पुत्रा बधूतु:
- **Translation**: 

---

