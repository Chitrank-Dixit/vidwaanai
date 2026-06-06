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

### Verse 1 (Vishnu Puran 0.11901)
- **Original**: ऐसी अबस्थामें मेरा श्रीहीन होना कोई आश्चर्यवी बात नहीं है; हे पितामह ! आश्चर्य तो यह है कि नीच प्रुषोंद्राय अपमान-पंकर्में सनकर भी मैं निर्लज्ज अभी जीवित हो हूँ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11902)
- **Original**: श्रीव्यासजी बोले--हे पार्थ ! तुम्हारी रज्जा व्यर्थ है, तुम्हें शोक करना उचित नहीं है। तुम सम्पूर्ण भूतोंमें कालकी ऐसी ही गति जानो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11903)
- **Original**: हे पाण्डव ! प्राणियोंकी उन्नति और अवनतिका कारण काल ही है,
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11904)
- **Original**: आ0 38 ] पतञ्चम अंझ 419 नहद्य: समुद्रा गिरयस्सकला च वसुन्धरा। देवा मनुष्या: पशवस्तरवअ्॒ सरीसृषपा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11905)
- **Original**: 56 सृष्टाः कालेन कालेन पुनर्वास्यन्ति संक्षयम्‌ । कालात्मकमिद सर्व ज्ञात्वा शममवाघुहि
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11906)
- **Original**: 57 कालस्वरूपी भगवान्कृष्ण: कमलल्तोचन: । यचात्थ कृष्णमाहात्यय॑ तत्तथैव धनझय
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11907)
- **Original**: 58 भारावतारकार्यार्थमवतीर्णस्स मेदिनीम्‌ । भाराक़ान्ता धरा याता देवानां समिति पुरा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11908)
- **Original**: 59 तदर्थमबतीणो3सौ कालरूपी जनार्दन: । तत्च निष्पादित॑ कार्यमशेषा भूभुजो हता:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11909)
- **Original**: 60 वृष्ण्यन्धककुलं सर्व तथा पार्थोपसंहतम्‌। न किल्निदन्यत्कर्तव्यं तस्य भूमितले प्रभो:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11910)
- **Original**: 619 अतो गतस्स भगवान्कृतकृत्यो बथेच्छया । सृष्टिं सर्गे करोत्येष देवदेव: स्थितौ स्थितिम्‌ । अन्तें5न्ताय समर्थो5यं साम्प्रतं वै यथा गत:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11911)
- **Original**: 62 तस्मात्पार्थ न सन्तापस्त्वया कार्य: पराभवे । भवन्ति भावा: कालेषु पुरुषाणां यत्: स्तुति:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11912)
- **Original**: 63 त्वयैकेन हता भीष्पद्रोणकर्णादयो रणे। तेषामर्जुन कालोत्थ: कि न्यूनाभिभवो न सः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11913)
- **Original**: 64 बिष्णोस्तस्य प्रभावेण यथा तेषां पराभव: । कृतस्तथैव भवतो दस्पुभ्यस्स पराभव:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11914)
- **Original**: 65 स देवेशइशरीराणि समाविश्य जगत्स्थितिम्‌ । करोति सर्वभूतानां नाशमन्ते जगत्पतिः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11915)
- **Original**: 686 अभगोदये ते कौन्तेय सहायो5भूजनार्दन: । तथात्ते तद्ठिपक्षास्ते केशवेन विल्लोकिता:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11916)
- **Original**: 67 कइश्रदृध्यात्सगाड़ेयान्हन्यास्त्व॑कौरवानिति । आभीरिभ्यक्ष भवत: कः श्रद्दध्यात्पाभवम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11917)
- **Original**: 68 अतः हे अर्जुन
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11918)
- **Original**: ! इन जय-पराजयॉको कालके अधीन समझकर तुम स्थिरता धारण करो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11919)
- **Original**: नदियों, समुद्र, गिरिगण, सम्पूर्ण पृथिवी, देव, मनुष्य, पशु, वृक्ष और सरीसृप आदि सम्पूर्ण पदार्थ कालके ही रचे हुए हैं और फिर कालहीसे ये क्षोण हो जाते हैं, अतः इस सारे प्रपक्षको काल्प्रत्मक जानकर झान्त होओ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11920)
- **Original**: हे धनक्षय ! तुमने कृष्णचन्द्रका जैसा माहात्य बतलाया है वह सब सत्य ही है; क्योंकि कमलनयन भगवान्‌ कृष्ण साक्षात्‌ कलस्वरूप ही हैं
- **Translation**: 

---

