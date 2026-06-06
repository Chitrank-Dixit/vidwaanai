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

### Verse 1 (Vishnu Puran 0.4981)
- **Original**: तदनन्तर, पुराणार्थविद्ासद व्यासजीने आख्यान,
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4982)
- **Original**: संहिताकी रचना की
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4983)
- **Original**: रोमहर्पण सूत व्यासजीके प्रसिद्ध शिष्य थे। महामति व्यासजीने उन्हें पुराण- पुराणसंहितां तस्मै ददौ व्यासो महामति:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4984)
- **Original**: संहिताका अध्ययन कराया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4985)
- **Original**: उन सूतजीके सुमतिश्चाभ्रिवर्चाश्च॒मित्रायुइशांसपायन: । सुमति, अम्रिवर्चा, मित्रायु, शांसपायन, अफृतद्रण अकृतब्रणसावर्णी षट्‌ शिष्यास्तस्य चाभवन्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4986)
- **Original**: और सावार्णि--ये छः शिष्य थे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4987)
- **Original**: काइयप काझ्यप: संहिताकर्ता सावर्णिश्शांसपायन:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4988)
- **Original**: रोमहर्षणिका चान्या तिसृर्णों मूलसंहिता
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4989)
- **Original**: 18 गोत्रीय अकृतत्रण, सार्वार्ण और झ्ांसपायन--ये तीनों संहिताकर्ता हैं। उन तीनों संहिताओँक्यी आधार एक रोमहर्षणजीकी संहिता है। है मुने! इन चारों चतुष्टयेन भेदेन संहितानापरिद॑ मुने
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4990)
- **Original**: संहिताओंकी सारभूत मैंने यह तिष्णुपुराणसंहिता ननायी आइ्यव॑ सर्वपुराणानां पुराणं ब्राह्ममुच्यते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4991)
- **Original**: पुराणज्ञ पुरुष कुछ अठारह पुणण अष्टादशपुराणानि पुराणज्ञा: प्रचक्षते
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4992)
- **Original**: बतलाते हैं; उन सब्रमें प्राचीनतम ब्रह्मपुराण है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4993)
- **Original**: 178 ब्राह्म॑ पाद्म॑ वैष्णवं च॒ दौव भागवत तथा । श्रीविष्णुपुराण [आ* 6 प्रधम पुराण ज्राह्म है, दूसरा पाद्य, तीसरा वैष्णव, तथान्य नास्दीय॑ च मार्कण्डेयं च सप्तमम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4994)
- **Original**: चौथा तौव, पाँचवाँ भागवत, छटा नारदीय और सातकाँ आश्नेयमष्टम॑ चेत्र भविष्यज्नवर्म स्पृतम्‌। दक्षमं ब्रह्मवैवर्त लैड्मेकादर्श स्मृतम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4995)
- **Original**: 22 वाराहं ड्वादहं चैब स्कान्दं चात्र त्रयोदशम्‌। चतुर्दश बामन च कोर्म पल्लद्श तथा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4996)
- **Original**: 23 मात्य च गारुडे चैव ब्रह्माण्ड च तत: परम्‌ । महापुराणान्येतानि ह्ाष्टाश्य महामुने
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4997)
- **Original**: 24 तथा चोपपुराणानि मुनिर्भि:ः कधितानि च । सर्गश्ष॒प्रतिसर्गश्॒ वंशमन्वन्तराणि च। सर्वेश्ेतेषु कथ्यन्ते बंशानुचरितें च यत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4998)
- **Original**: 25 यदेतत्तव मैत्रेय पुराणं कथ्यते माया। एतद्वैष्णवर्सज्न॑वै पाड़ास्य समनन्तरम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4999)
- **Original**: 26 सर्गे चर प्रतिसगें च वंशमन्वन्तरादिषु । कथ्यते भगवान्तिष्णुरेषेश्वेव सत्तम
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5000)
- **Original**: 27 अड्ञनि वेदाश्षत्वारो मीमांसा न्यायविस्तरः। पुराणं धर्मशास्त्र च विद्या होताश्षतुर्दशा
- **Translation**: 

---

