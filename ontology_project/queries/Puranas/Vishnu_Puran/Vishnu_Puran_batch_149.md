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

### Verse 1 (Vishnu Puran 0.2961)
- **Original**: 19 इल्लाबृताय प्रददो मेरु्त्र तु मध्यम: । नीलाचलाश्रितं वर्ष रम्याय प्रददौ पिता
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2962)
- **Original**: 20 श्वेत तदुत्तरं वर्ष पिन्ना दत्त हिरण्बते
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2963)
- **Original**: 21 यदुत्तर श्रूड़बतो वर्ष तत्कुरवे ददो। मेरोः पूर्वेण यह भद्गाश्चाय प्रदत्ततान्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2964)
- **Original**: 22 गन्धमादनवर्ष तु केतुमालाय दत्तवान्‌। इत्येतानि ददौ तेभ्य: पुत्रेध्य: स नरेश्वर:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2965)
- **Original**: 23 वर्षेध्रेतेषु तान्युन्नानभिषिच्य स भूमिपः । झालग्रार्म महापुण्य॑ मैत्रेय तपसे ययौ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2966)
- **Original**: 24 यानि किप्पुरुषादीनि वर्षाण्यष्टो महामुने । तेषां स्वाभाविकी सिद्धि: सुखप्राया हायत्नत:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2967)
- **Original**: 25 श्रीविष्णुपुराण [ अ* 1 राज्य आदि भोगोंमें अपना छित्त नहीं लगाया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2968)
- **Original**: है मुने ! वे निर्म्चित्त और कर्म-फल्की इच्छासे रहित थे तथा समस्त विषयोंमें सदा न्यायानुकूल ही प्रकततत होते थे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2969)
- **Original**: हे मुनिश्रेष्ठ ! राजा प्रियत्नरतने अपने शोष सात महात्मा पुत्रोंको सात द्वीप बाँट दिये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2970)
- **Original**: है महाभाग ! पिता प्रियक्रतने आम्रीध्रको जम्बूद्वीप और प्रेधातिथिको प्लक्ष नामक दूसरा द्वीप दिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2971)
- **Original**: उन्होंने शाल्मलद्ठीपमें वपुष्मानकों अभिषिक्त किया; ज्योतिष्मान्को कुशद्टीपका राजा चबनाया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2972)
- **Original**: झ्ुतिमानको ऋश्षद्धीपके आसनपर नियुक्त किया, भव्यको प्रियत्नतने शकद्वीफ्का स्वामी बनाया और सयनको पुष्करद्वीपका अधिपति किया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2973)
- **Original**: है मुनिसत्तम ! उनमें जो जम्यूदोपके अधीधर राजा आग्रीध्न थे उनके प्रजापतिके समान नौ पुत्र हूए।। ये नाभि, किम्पुरुष, हरिवर्ष, इल्त्रवृत; रम्य, हिरण्यान, कुरु, भव्राश्व और सत्कर्मशील राजा केतुमाल थे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2974)
- **Original**: .15---17
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2975)
- **Original**: हे विप्र ! अब उनके जम्बूद्वीपके विभाग सुनो। पिता आप्रीच्नने दक्षिणती ओरका हिमबर्ष [जिसे अब भारतवर्ष कहते हैं] नाभिकों दिया। 18
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2976)
- **Original**: इसी प्रकार किम्पुल्षको हेमकूटवर्ष तथा हरिवर्षको तीसरा नैषधवर्ष दिया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2977)
- **Original**: जिसके मध्यमें मेरुपर्चत है लह इत्माव॒तवर्ष उन्होंने इस्म्रवृतकों दिया तथा नीस्माथरूसे रूगा हुआ चर्ष रम्यकों दिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2978)
- **Original**: पिता आम्रीधने_ उसका उत्तरवर्ती श्वेतवर्ष हिरण्वानकों दिया तथा जो वर्ष थरृगवानपर्चतके उत्तरमें स्थित है वह कुरुकों और जो मेरूके पूर्वमें स्थित है कह भद्गाश्रक्रे दिया तथा केतुमालकों गन्धमादनबर्ष दिया। इस प्रकार राजा आम्रीधने अपने पुत्रोंकों ये वर्ष दिये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2979)
- **Original**: है मैत्रेय ! अपने पुत्रोंको इन बर्षोर्मे अभिषिक्त कर थे तपस्याके लिये झालमाप्त- नामक मह़ापविय्र क्षेत्रकों चले गये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2980)
- **Original**: है महामुने ! किः्पुरुष आदि जो आठ वर्ष:-है उनमें सुरक्को बहुलता है और बिना यल्लके-स्व॒भावसे
- **Translation**: 

---

