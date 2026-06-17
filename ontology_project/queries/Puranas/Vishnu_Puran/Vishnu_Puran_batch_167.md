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

### Verse 1 (Vishnu Puran 0.3321)
- **Original**: 73 एकश्षात्र महाभाग प्रख्यातो वर्षपर्वतः । मानसोत्तरसंज्ञो बे मध्यतो बलयाकृति:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3322)
- **Original**: 74 दिये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3323)
- **Original**: बे स्रात पुत्र जलद, कुमार, सुकुमार, मरीचक, कुसुमोद, मौदाकि और महाद्वुम थे। उन्हींके नामानुसार वहाँ क्रमद्ाः सात वर्ष हैं और वहाँ भी बषोंका विभाग करनेवाले सात ही पर्वत हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3324)
- **Original**: हे द्विज! वहाँ पहला पर्वत उदवाचल है और दूसरा जल्मधार; तथा अन्य पर्वत रैवतक, इयाम, अस्तायल्ड, आम्निकिय और अति सुरम्य गिरिश्रेष्ठ केसरी हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3325)
- **Original**: वहाँ सिद्ध और गन्धवोंसे सेवित एक अति महान्‌ शाकवृक्ष है, जिसके वायुका स्पर्श करनेसे हृदयमें परम आह्वाद उत्पन्न होता है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3326)
- **Original**: वहाँ चारतुर्वर्ण्यसे युक्त अति पणित्र देश और समस्त पाप तथा भयको दूर करनेबाली सुकुमारी, कुमारी, नलिनी, घेनुका, इक्षु, खेणुका और गभस्ती--ये स्रात महापवित्र नदियाँ हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3327)
- **Original**: है महामुने ! इनके सिखा उस द्वीपमें और भी सैकड़ों छोटी-छोटी नदियाँ और सैकड़ों-हजारों पर्वत हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3328)
- **Original**: स्वर्ग-भोगके अनन्तर जिन्होंने पृथिवी-तल्पर आकर जल्द आदि वर्षो जन्म ग्रहण किया है ये क्जोग प्रसन्न होकर उनका जल पान करते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3329)
- **Original**: उन सातों वर्षोंमें घर्मका ह्वास पारस्परिक संघर्ष (कलह) अथवा मर्यादाका उल्लंघन कभी नहीं होता
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3330)
- **Original**: बहाँ बंग, मसागघ, मानस और मनन्‍्दग--ये चार वर्ण हैं। इनमें नंग सर्वश्रेष्ठ ब्राह्मण हैं, मागध क्षत्रिय हैं, मानस लैश्य हैं तथा मन्दग शूद्र हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3331)
- **Original**: हे मुने ! शाकद्दीपमें आख्नानुकूल कर्म करनेवाले पूर्वोक्त चारों वर्णाद्वारा संयत चित्तसे विधिपूर्वक सूर्यरूपधारी भगवान्‌ विष्णुकी उपासना की जाती है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3332)
- **Original**: हे मैत्रेय ! यह शाकट्ठरीप अपने हो बग़बर विस्तारवाे मष्डलाकार दुग्धके समुद्रसे घिरा हुआ है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3333)
- **Original**: ओर हे ब्रह्मनू ! वह क्षीर-समुद्र शाकद्वीपसे दूने परिमाणवाले पुष्करदीपसे परिवेष्टित है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3334)
- **Original**: पुष्करद्वीपर्मं लहाँके अधिपति महाराज सवनके महावीर और धातकिनामक दो पुत्र हुए। अतः उन दोनोंके नामानुसार उसमें महावीर-खण्ड और चातकी-खण्डनामक दो वर्ष हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3335)
- **Original**: हे महाभाग ! इसमें मानसोत्तनामक एक ही वर्ष-पर्वत कहा जाता है जो इसके मध्यमें बलयाकार स्थित है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3336)
- **Original**: अबन्ड ] योजनानां सहल्लाणि ऊर्ध्व पञ्चाशदुच्छित: । तावदेव च विस्तीर्ण: सर्वतः परिमण्डलः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3337)
- **Original**: 75 पुष्करद्यीपववलयं मध्येन विभजन्निव । स्थितो सौ तेन विच्छिन्न॑ जाते तद्गर्षकद्वयम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3338)
- **Original**: । 76 वलयाकारमेकैक तयोर्वर्ष॑ तथा गिरिः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3339)
- **Original**: 77 दछ्वर्षसहस्त्राणि तत्र जीवन्ति मानवा: । निरामया विशोकाश्व रागद्वेषादिवर्जिता:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3340)
- **Original**: 78 अधमोत्तमौ न तेघ्वास्तां न वध्यवधको द्विज । नेर्ष्यासूया भयं द्वेषो दोषो छोभादिको न ्ञ ।। 79 महावीर॑ बयहिर्वर्ष॑ धात्तकीखण्डमन्तत: । मानसोत्तरशैलस्थ देवदैत्यादिसेवितम्‌
- **Translation**: 

---

