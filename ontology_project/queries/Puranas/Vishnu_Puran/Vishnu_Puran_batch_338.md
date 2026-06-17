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

### Verse 1 (Vishnu Puran 0.6741)
- **Original**: ब्रिशक्लोहरि श्रन्द्रस्तस्माश्व रोहिताश्रस्ततश्न हरितो हरितस्थ चज्ुश्रश्चोर्विजयवसुदेवा.. रुरूको विजयाहुरुकस्य बृकः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6742)
- **Original**: ततो वृकस्य बाहुर्योजइसो हैहयतालजज्लदिभि: पराजितो3- न्तर्वल्या महिष्या सह वन प्रविवेश
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6743)
- **Original**: तस्याश्र सपत्या गर्भस्तम्भनाय गरो द्त्तः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6744)
- **Original**: तेनास्था गर्भस्सप्तवर्षाणि जठर एव तस्थौ
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6745)
- **Original**: सच बाहुर्बृद्धभावादौर्बाश्रम- समीपे ममार
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6746)
- **Original**: सा तस्य भार्या चितां कृत्वा चतुर्थ अंझ 243 अपने झरीरका बक बढ़ जानेसे सम्पूर्ण गन्धवॉकों मार डाला और फिर अपने नगरमें व्त्रैर आया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6747)
- **Original**: उस समय समस्त नागराजोंने नर्मदाकों यह खर दिया कि जो कोई तेरा स्मरण करते हुए तेरा नाम केगा उसको सर्प-बिषसे कोई भय न होगा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6748)
- **Original**: इस विषयमें यह इलोक भी है---
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6749)
- **Original**: 'नर्मदाको प्रातःकाल नमस्कार है और रात्रिकालमें भी नर्मदाकों नमस्कार है। हे नर्मदे ! तुमको बारम्नार नमस्कार है, तुम मेरी खिष और सर्पसे रक्षा करो'
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6750)
- **Original**: इसका उन्नारण करते हुए दिन अथवा रात्रिमें किसी समय भी अन्धकारमें जानेसे सर्प नहीं काटता तथा इसका स्मरण करके भोजन करनेवालेका खाया हुआ विष भी घातक नहीं होता
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6751)
- **Original**: पुरुकुत्सकों नागपतियोंने यह वर दिया कि तुम्हारी सनन्‍्तानकाा कभी अन्त न होगा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6752)
- **Original**: पुरुकुत्सने नर्मदाल्रे त्रसहस्यु नामक पुत्र उत्पन्न किया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6753)
- **Original**: जसदस्युसे अनरण्य हुआ, जिसे दिग्विजयके समय रावणने मारा था
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6754)
- **Original**: अनरण्यके पृषदश्च, पृषदश्के हर्यश्र, हर्यश्रके हस्त, हस्तके सुमना, सुमनाके त्रिधन्या, तिधन्वाके जय्यास्ण और त्रव्यास्णिके सत्यतत नामक पुत्र हुआ, जो पीछे त्रिशंकु कहल्थ्रया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6755)
- **Original**: बह त्रिशंकु चाप्डाल हो गया था
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6756)
- **Original**: एक बार बारह वर्षतक अनावृष्टि रही। उस समय विश्वामित्र मुन्कि स्त्री और बारू-अन्चोके पोषणार्थ तथा अपनी चाप्डालताको छुड़ानेके लिये बह गज़्ाजीके तटपर एक बटके वृक्षपर प्रतिदिन मृगका मास बाँध आता था
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6757)
- **Original**: इससे प्रसन्न होकर बिश्वामित्रजीने उसे सदेह स्वर्ग भेज दिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6758)
- **Original**: वरिदोकुसे हरिक्षत्र, हरिश्द्रसे रोहिताश्व, रोहिताश्से हरित, हरितसे चब्चु, चश्लुसे लिजय और जसुदेव, विजयसे रुकुक और रुरुकसे वृकका जन्म हुआ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6759)
- **Original**: खकके बहू नामक पुत्र हुआ जो हैहय और तालजंघ आदि क्षत्रियोंसे पराजित होकर अपनी गर्भवती पटरानीके सहित वनमें चल्त्र गया था।26
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6760)
- **Original**: पटरानीकी सौतने उसका गर्भ रोकनेकी इच्छझासे उसे विष स्विल्प् दिया
- **Translation**: 

---

