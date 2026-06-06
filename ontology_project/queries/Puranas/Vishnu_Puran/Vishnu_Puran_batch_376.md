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

### Verse 1 (Vishnu Puran 0.7501)
- **Original**: यत्रावतीर्ण कृष्णाख्य परं ब्रह्म निराकृति
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7502)
- **Original**: 4 सहस्नजिक्रोष्टनलनहुषसंज़ाश्वत्वारो .यदुपुत्रा बभूबु;
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7503)
- **Original**: सहस्त्जित्पुत्रशशतजित्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7504)
- **Original**: तस्य हैहयहेहयवेणुहयासत्रय: पुत्रा बभूवु:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7505)
- **Original**: हैहयपुत्रो श्र्मस्तस्थापि धर्मनेत्रस्ततः कुन्तिः कुन्तेः सहजित्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7506)
- **Original**: तत्तनयों महिष्मान्‌ योझइसौ माहिष्मती पुरी निवास- यामास
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7507)
- **Original**: तस्माउक्््रेण्यस्ततो दुर्दमस्त- स्माउइनको. घनकस्प कृतवीर्यकृताभ्रि- श्रीपराशरजी बोलछे--अब मैं ययातिके प्रथम पुत्र यदुके बंदाका वर्णन करता हूँ, जिसमें कि मनुष्य, सिद्ध, गन्धर्त, यक्ष, राक्षस, गुहाक, किंपुरुष, अप्सरा, सर्प, पक्षी, दैत्य, दानव, आदित्प, रुद्र, बसु, अश्विनीकुमार मरुद्गरण, देवार्षि, सुसुक्षु तथा घर्म, अर्थ, काम और सोक्षके अख्विलल्ेक-विश्राम आद्यन्तहोन भगवान्‌ विष्णुने अपने अपरिमित महत्वशास्त्रे अंडासे अवतार ल्थिया था। इस विषयमें यह इलोक प्रसिद्ध है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7508)
- **Original**: जिसमें श्रीकृष्ण नामक निराकार परनह्मने अवतार लिया था उस यदुरवंशका श्रवण करनेसे मनुष्य सम्पूर्ण पापोंसे मुक्त हो जाता है'
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7509)
- **Original**: यदुके सहस्नजित, ब्रत्रेष्ट, नल और नहुष नामक चार पुत्र हुए। सहस्नजितके शतजित्‌ और शतजितके-हैहय, हेहय तथा चेणुहय नामक तीन पुत्र हुए
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7510)
- **Original**: हैइयका पुत्र धर्य, धर्यक्ता धर्मनेन्न, धर्मनेत्नका कुत्ति, कुन्तिका सहजित्‌ तथा सहजितका पुत्र महिष्पान्‌ हुआ, जिसने माहिष्मतीपुरंको ऋस्राया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7511)
- **Original**: महिष्पान्‌के भद्धश्रेण्य, भद्रज्नेण्यके दूर्दम, दुर्दमके घनक तथा घनकके
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7512)
- **Original**: अए? 15 ] चतुर्थ अंझ 267 कृवधर्मकृतौजसश्चत्वारः पुत्रा बभूव॒ु:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7513)
- **Original**: पे मुसकना 270 ुंध07-306 »-.- हि जज्ञे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7514)
- **Original**: योउ्सो द्तात्रेयाख्यमाराध्य बाहुसहस््रमधर्मसेवा निवारण स्वधर्मसेवित्यं रणे पृथिवीजयं धर्मतश्ानु- पालनमरातिभ्योडपराजयमखिलजगठ्मस्यात- पुरुषाध मृत्युमित्येतान्वरानभिलषितवाँल्लेभे च
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7515)
- **Original**: तेनेयमशेषद्वीपवती पृथिवी सम्यक्‌ परिपाल्िता
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7516)
- **Original**: दहयज्ञसहस्रा ए्यसावयजत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7517)
- **Original**: तस्यथ च इल्कोकोउद्यापि गीयते
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7518)
- **Original**: ननून॑ कार्तवीर्यस्य गति यास्यन्ति पार्थिवा: । यज्ञैदनिस्तपोभियां प्रश्रयेण श्रुतेन च
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7519)
- **Original**: 16 अनष्टद्रव्यता च तस्य राज्येअभवत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7520)
- **Original**: पञ्ञाशीतिवर्षसहस्राण्यव्याहतारोग्य- एवं च पछ्नलाशी श्रीवलपराक्रमो राज्यमकरोत्‌
- **Translation**: 

---

