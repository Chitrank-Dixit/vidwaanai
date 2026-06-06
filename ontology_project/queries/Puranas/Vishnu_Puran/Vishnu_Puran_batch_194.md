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

### Verse 1 (Vishnu Puran 0.3861)
- **Original**: 112 सीता चालकनन्दा च चक्षूर्भद्रा च संस्थिता
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3862)
- **Original**: एकैव या चतुर्भेदा दिग्भेदगतिलक्षणा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3863)
- **Original**: 113 भेदं चालकनन्दास्यं यस्या: शर्वोंडपि दक्षिणम्‌ । दधार शिस्सा प्रीत्या वर्षाणामघिकं झतम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3864)
- **Original**: 114 अम्भोर्जगकलापाध विनिष्क्रान्तास्थिशर्करा: । प्लावयित्वा दिव निन्‍ये या पापान्सगरात्मजानू
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3865)
- **Original**: 115 ख्नातस्य सलिले यपघ््या: सद्यः पाप॑ प्रणश्यति । अपूर्वपुण्यप्राप्तिश्ष सद्यो मैत्रेय जायते
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3866)
- **Original**: 116 दत्ता: पितृभ्यो यत्रापस्तनयै: श्रद्धयान्वितै: । समाझत॑ प्रयच्छन्ति तृप्ति मैत्रेय दुर्लभाम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3867)
- **Original**: 197 अस्यामिष्ठा महायज्नैर्यज्ञेश पुरुषोत्तमम्‌ । द्विज भूपा: परां सिद्धिमवापुर्दिवि चेह च
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3868)
- **Original**: 118 या पाययति भूतानि कीर्तिता चर दिने दिने
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3869)
- **Original**: 120 गद्ढा गद्ढलेति चैन्नास योजनानां झतेप्रुपि । स्थितैरुश्वारितं हन्ति पाप जन्प्रत्रयार्जितम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3870)
- **Original**: 1219 यत: सा पावनायारं त्रयाणां जगतामपि । समुद्धूता परं॑ तत्तु तृतीयं भगवत्पदम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3871)
- **Original**: 122 होकर चाद्स्‍मण्डल क्षयके अनन्तर पुनः पहलेसे भी अधिक कान्ति धारण करता है, वे श्रीगज्नाजी चन्द्र- मण्डलसे निकलकर मेरुपर्वतके ऊपर गिरती हैं और संसारकों पवित्र करनेके लिये चारों दिशाओंमें जाती हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3872)
- **Original**: 160 --112
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3873)
- **Original**: चारों दिशाओंमें जानेसे ले एक ही सीता, अल्कनन्दा, चक्षु और भद्गा इन चार भेदोंजाली हो जाती हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3874)
- **Original**: जिसके अलकनन्दा नामक दक्षिणीय भरेदको भगवान्‌ दकरने अत्यन्त प्रीतिपूर्वक सौ वर्षसे भी अधिक अपने मस्तकपर घारण किया था, जिसने श्रीश्षूकरके जटाकल्मपसे निकलकर पापी सशयपुप्रोके अस्थिचूर्णको आए्राबित कर उन्हें स्वर्गमें पहुँचा दिया। है मैत्रय ! जिसके जलमे सख्रान करनेसे ज्ञीघ्र ही समस्त पाप नष्ट हो जाते हैं और अपूर्व पुण्यकी प्राप्ति होती है। 114--116
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3875)
- **Original**: जिसके प्रवाहमें पुत्रों्रारा पितरोंके हिये श्रद्धापूर्वक किया हुआ एक दिनका भी तर्पण उन्हें सौ वर्षतक दुर्लभ तृप्ति देता है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3876)
- **Original**: हे ट्विज ! जिसके तटपर राजाओंने महायज्ञोंसे यज्ञेधर भगवान्‌ पुरुषोत्तमका यजन करके इहल्परेक और स्वर्गलोकमें परमसिद्धि छाभ की है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3877)
- **Original**: जिसके जलपें स्नान करनेसे निष्पाप हुए यतिजनोंने भगवान्‌ केशालमें चित्त छगाकर अत्युत्तम निर्वाणपद प्राप्त किया है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3878)
- **Original**: जो अपना श्रवण, इच्छा, दर्शन, स्पर्श, जलपान, स्त्रान तथा यशोगान करनेसे ही नित्यप्रति प्राणियोंकों पवित्र करती रहती है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3879)
- **Original**: तथा जिसका “गक्का, गक्ल' ऐसा नाम सौ योजनको दूरीसे श्री उच्चारण किये जानेपर [
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3880)
- **Original**: जीवके ] तीन जन्मोंके सन्लित पापोंको नष्ट कर देता है
- **Translation**: 

---

