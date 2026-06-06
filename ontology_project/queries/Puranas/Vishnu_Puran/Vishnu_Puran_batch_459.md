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

### Verse 1 (Vishnu Puran 0.9161)
- **Original**: 15 नखाह्लुरविनिर्भिन्नवैरिवक्षस्स्थलो विभु: । नृसिंहरूपी सर्वत्र रक्षतु त्वां जनार्दन:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9162)
- **Original**: 16 बामनो रक्षतु सदा भवन्ते यः क्षणादभूत्‌ । त्रिविक्रम: क्रमाक्रान्तत्रैल्लेक्य: स्फुरदायुध:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9163)
- **Original**: 17 झिरस्ते पातु गोविन्द: कण्ठं रक्षतु केशल: । गुहां च॒ जठर॑ बिष्णुर्जद्े पादो जनार्दन:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9164)
- **Original**: 18 मुर्ख बाहू प्रबाहू च मन: सर्वेन्द्रियाणि च । रक्षत्वव्याहतैश्वर्यस्तव नारायणो5व्यय:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9165)
- **Original**: 19 झाईचक्रगदापाणेह्शद्भुनादहता: . क्षयम्‌ । गछछन्तु प्रेतकृष्माण्डराक्षसा ये तवाहिता:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9166)
- **Original**: 20 1. घुटनेके नीचेका भाग । क्रोधपूर्वक उसके स्तनको अपने हाथोंसे खूब दबाकर पकड़ लिया और उसे उसके प्राणोंके सहित पीने लगे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9167)
- **Original**: तब ज्ायु-बन्बनोंके झिधिल हो जानेसे पूतना घोर शब्द करती हुई मरते समय महाभयद्भुर रूप घारणकर पृथिवीपर गिर पड़ी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9168)
- **Original**: उसके घोर नादको सुनकर भयभीत हुए ब्रजवासीगण जाग उठे और देखा कि कृष्ण पूतनाकी गोदमें हैं और यह मारी गयो है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9169)
- **Original**: है ट्विजोत्तम ! तब भयभीता यशोदाने कृष्णको गोदमें लेकर उन्हें गौकी एूँछसे झाड़कर बालकका ग्रह-दोष निवारण किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9170)
- **Original**: नन्‍्दगोपने भी आगेके वाक्य कहकर विधिपूर्वक रक्षा करते हूए कृष्णके मस्तकपर गोबरका चूर्ण लगाया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9171)
- **Original**: नन्‍्दगोप बोले--जिनकी नाभिसे प्रकट हुए कमछमसे सम्पूर्ण जगत्‌ उत्पन्न हुआ है वे सम्पूर्ण भूतोकि आदिस्थान श्रीहटरि तेरी रक्षा करें
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9172)
- **Original**: जिगकी दाढ़ोंकि अग्रभागपर स्थापित होकर भूमि सम्पूर्ण जगत॒कों धारण करती है वे वराह-रूप-धारी श्रीकेशव तेरी रक्षा करें
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9173)
- **Original**: जिन विभुने अपने नख्वाओ्रोंसे अत्रुके वक्ष-स्थलको विदीर्ण कर दिया था वे नृसिंहरूपी जनार्दन तेरी सर्वत्र रक्षा करें
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9174)
- **Original**: जिन्होंने क्षणमात्रयें सास त्राप लिया था ये वामनभगवान्‌ तेरी सर्वदा रक्षा करें
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9175)
- **Original**: गोबिन्द तेरे सिर्की, केशव कण्ठकी, विष्णु गुह्ास्थान और जठरकी तथा जनार्दन जैधा और चरणोंकी रक्षा करें
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9176)
- **Original**: तेरे मुख, बाहु, प्रबाहु,, मन और सम्पूर्ण इन्द्रियोंकी अखण्ड-ऐश्वर्यसे सम्पन्न अविनाशी श्रीनारायण रक्षा करें
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9177)
- **Original**: तेरे अनिष्ट करनेवाले जो प्रेत, कृष्पाण्ड और राक्षस हों वे दा धनुष, चक्र और गदा धारण करनेणाले विष्णुभगवान्‌को गज्भु-ध्यनिसे नष्ट
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9178)
- **Original**: आ* 6 ] सं पातु दिक्षु वैकुण्ठो विदिक्षु मधुसूदनः । हृषीकेझोम्बरे भूमों रक्षतु त्वां महीधरः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9179)
- **Original**: 21 श्रीपरादार उत्नाच एवं कृतस्वस्व्ययनो नन्‍्दगोपेन बात्ककः । झायितइ॒दकटस्याधो बालपर्यश्धूकातले
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9180)
- **Original**: 22 ते च गोषा महृददुष्ठा पूतताया: कलेवरम्‌। __ पक्रम अंझ 329 हो जायें
- **Translation**: 

---

