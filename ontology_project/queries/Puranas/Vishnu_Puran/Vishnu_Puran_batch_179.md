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

### Verse 1 (Vishnu Puran 0.3561)
- **Original**: हे द्विजोत्तम ! बृहस्पतिजीसे दो लाख योजन ऊपर दानि हैं और शनिसे एक लक्ष योजनके अत्तरपर सप्तर्पिमण्डल है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3562)
- **Original**: तथा सप्तर्षियोंसे भी सौ हजार योजन ऊपर समस्त ज्योतिश्क्रकी नाभिरूप घ्रुवमप्डल स्थित है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3563)
- **Original**: है महामुने ! मैंने हुमसे यह त्रिलोकीकी ठक्षताके विषयमें वर्णन किया। यह त्रित्लेकी यज्ञ़फलकी भोग-भूमि है और यज्ञानुष्ठानकी स्थिति इस भारतवर्षमें ही है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3564)
- **Original**: धुबसे एक करोड़ योजन ऊपर महर्तगरेंक है, जहाँ कल्पान्त-पर्यन्त रहनेवाले भूगु आदि सिद्धगण रहते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3565)
- **Original**: हे मैत्रेय ! उससे भी दो करोड़ योजन ऊपर जनलोक है जिसमें ब्रह्माजीके प्रख्यात पुत्र निर्मलचित्त सनकादि रहते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3566)
- **Original**: जनलोकसे चौगुना अर्थात्‌ आठ करोड़ थयोजन ऊपर तपलोक है; बहाँ वैराज नामक देवगणोंका निवास है जिनका कभी दाह नहीं होता
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3567)
- **Original**: आ07 ] क्वितीय अंझ 127 घड्गुणेन तपोत्छोकात्सत्यकोको बिराजते । अपुनर्मारिका यत्र ब्रह्मलोको हि स स्मृतः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3568)
- **Original**: 95 पादगम्बन्तु यत्किल्निहृस्त्वस्ति पृथिवीमयम्‌ । स भूलोंक: समाख्यातो विस्तरोउस्य मयोदित:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3569)
- **Original**: 16 भूमिसूर्यान्‍्तरं यश्च सिद्धादिमुनिसेबितम्‌। ध्रुवर्लेकस्तु सो5प्युक्तो द्वितीयो मुनिसत्तम
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3570)
- **Original**: 17 धुवसूर्यान्‍तर॑यध ॒नियुतानि चतुर्दश । खलोंक: सो5पि गदितो लोकसंत्थानचिन्तकैः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3571)
- **Original**: 18 कृतकाकृतयोर्मध्ये महलोंक इति स्मृतः । शुन्यों भवति कल्पान्ते योउत्यन्त॑ न विनश्यति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3572)
- **Original**: 20 एते सप्त मया छोका मैत्रेय कथितास्तव । पातालानि च सप्तैव ब्रहह्माण्डस्यैष विस्तर:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3573)
- **Original**: 29 एतदण्डकटाहेन तिर्यक्‌ चओध्बपभ्रस्तथा । कपिवत्थस्य यथा बीज सर्बतो बै समावृतम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3574)
- **Original**: 22 दशोत्तरेण पयसा मैत्रेयाण्डं च तद्गृतम्‌। सर्वोष्म्युपरिधानोउसौ वह्निना वेष्टितो बहि:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3575)
- **Original**: 23 वहिश्न बायुना वायुप्रैत्नेय नभसा वृतः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3576)
- **Original**: भूतादिना नभः सो5पि महता परिवेष्टित: । दघ्चोत्तराण्यशेषाणि मैत्रेयेतानि सप्त वै
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3577)
- **Original**: 24 महान्ते च समावृत्य प्रधानं समवस्थितम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3578)
- **Original**: अनन्तस्प न तस्थान्त: संख्यान॑ चापि विद्यते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3579)
- **Original**: 25 तदनन्तमसंख्यातप्रमाणं चाषि वै यतः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3580)
- **Original**: तपलेकसे छःगुना अर्थात्‌ बारह करोड़ योजनके अत्तरपर सत्यस््रेक सुशोभित है जो ब्रह्मलोक भी कहलाता है और जिसमें फिर न मरनेबाले अमरगण निवास करते हैं
- **Translation**: 

---

