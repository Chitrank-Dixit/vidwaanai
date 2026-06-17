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

### Verse 1 (Vishnu Puran 0.2901)
- **Original**: कालस्वरूपो भगवानपापो हरिरव्ययः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2902)
- **Original**: 79 भूलोंकोउथ भुवरलोंक: स्लोंको मुनिम्तत्तम । महर्जनस्तप: सत्यं सप्त छोका इसे विभु:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2903)
- **Original**: 80 ल्लेकात्मपूर्त्ति: सर्वेषां पूर्वेषामपि पूर्वजः । आधार: सर्वविद्यानाँ स्क्यमेव हरि: स्थित:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2904)
- **Original**: 89 देवमानुषपश्चादिस्वरूपैबहुसि:. स्थित: । ततः सर्वेश्वरोडनन्तो भूतमूर्तिसमूर्त्तिमान्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2905)
- **Original**: 82 ऋचो यजूंषि सामानि तथेवाधर्वणानि ये । इतिहासोपवेदाश्व॒ वेदान्तेषु_ तथोक्तय:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2906)
- **Original**: 83 वेदाड्रानि समस्तानि मन्वादिगदितानि च । शास्रराण्यशेषाण्यास्यानान्यनुवाकाश्च ये क्चित्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2907)
- **Original**: 84 काव्यालापाश्च ये केचिद्रीतकान्यखिलानि
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2908)
- **Original**: अब्दमूर्तिधरस्यैतद्रपुर्विष्णोर्महात्मन:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2909)
- **Original**: 85 यानि मूर््तन्यपूर्त्तानि यान्यत्रान्यश्न वा क्रचित्‌ । सन्ति बे बस्तुजातानि तानि सर्वाणि तद्पु:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2910)
- **Original**: 86 अहं हरि: सर्वपिद॑ जनार्दनो नान्यत्ततः कारणकार्यजातम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2911)
- **Original**: सन चाट कद जद 4 यस्य न तस्य भूयो >अयब, परजत्मब थे हत इन्द्रदा भवन्ति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2912)
- **Original**: 87 यथाबवत्कथितो पापै: प्रमुच्यते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2913)
- **Original**: 88 कार्ततिक्यां पुष्करस्राने द्वादशाब्देन यत्फलम्‌ तदस्य श्रवणास्सव॑ मैत्रेयाप्रनोति मानजः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2914)
- **Original**: 89 देवर्षिपितृगन्धर्वयक्षादीनां च सम्मवम्‌ । और अविद्या सभो श्रीड्षषीकेशमें आश्रित हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2915)
- **Original**: श्रीहरि रूपरहित होकर भी मायामयरूपसे प्राणियोंके कल्याणके लिये इन सबको अख्ब और भूषणरूपसे धारण करते हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2916)
- **Original**: इस प्रकार वे कमलनयन परमेश्वर सबिकार प्रधान [ निर्विकार ], पुरुष तथा सम्पूर्ण जगत्‌को धारण करते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2917)
- **Original**: जो कुछ भो विद्या- अविद्या, सत्‌- असत्‌ तथा अव्ययरूप है, हे मैत्रेय ! कह सब सर्जभूतेश्वर श्रोमधुसूदनमें हो स्थित है।
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2918)
- **Original**: कला, काष्टा, निमेष, दिन, ऋतु, अयन और यर्षरूपसे वे कालूस्वरूप निष्पाप अय्यय श्रीहरि ही विराजमान हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2919)
- **Original**: हे मनिश्रेष्ठ ! भूलॉक, भुबर््मेक और स्वलॉक तथा मह, जन, तप और सत्य आदि सातों लोक भी सर्वव्यापक भगलान्‌ ही हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2920)
- **Original**: रूभौ पूर्वजोंके पूर्वज तथा समस्त विद्याओँके आधार श्रीहरि हो स्वयं लोकमयस्थरूपसे स्थित हैं
- **Translation**: 

---

