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

### Verse 1 (Vishnu Puran 0.3261)
- **Original**: जाल्मलद्बीपमें कपिछ, अरुण, पीत और कृष्ण--ये चार वर्ण निवास करते हैं जो पृथक्‌-पृथक्क्‌ क्रमशः ब्राह्मण, क्षत्रिय, वैश्य और शूद्र हैं। ये यजनशील लोग सबके आत्मा, अव्यय और यशके आश्रय वायुरूप विष्णु- भगतान्का ओष्ठ यज्ञोंद्ारा यजन करते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3262)
- **Original**: इस अत्यन्त मनोहर ट्वीपमें देवगण सदा विराजमान रहते हैं। इसमें झाल्णल (सेमल) का एक महान्‌ वृक्ष है जो अपने नामसे ही अत्यन्त शान्तिदायक है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3263)
- **Original**: यह द्वीप अपने समान ही विस्तारवाले एक मदिराके समुद्रसे सत्च ओरसे पूर्णतया घिरा हुआ है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3264)
- **Original**: और यह सरासमुद्र शाल्मलद्बौपसे दुने विस्तास्वाले कुशद्वीपद़्ास सब ओरसे परिवेष्टित है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3265)
- **Original**: कुशद्वीपमें (वहाँके अधिपति] ज्योतिष्यानके सात पुत्र थे, उनके नाम सुनो! के उद्धिद, वेणुमान्‌, वैरथ, हप्बन, धृति, प्रभाकर और कपिल थे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3266)
- **Original**: उनके नामानुसार ही वहाँके वर्षोके नाम पड़े
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3267)
- **Original**: उसमें दैत्य और दानबॉके सहित मनुष्य तथा देव, गन्धर्व, यक्ष और किन्नर आदि निवास वरते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3268)
- **Original**: हे महामुने ! वहाँ भी अपने-अपने करमोमें तत्यर दमी, झुष्मी, स्लेह और मन्देहनामक चार ही वर्ण हैं, जो क्रमशः ब्राह्मण, क्षत्रिय, वैज्य और शुद्र ही हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3269)
- **Original**: अपने प्रारव्यक्षयके निमित्त शास्नानुकुछ कर्म करते हुए बहाँ कुशह्वीपमें ही ये बऋह्मरूप जनार्दनकी उपासनाद्वारा अपने प्रासब्धफलके देनेवाले अत्युप्र अहंकारका क्षय करते हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3270)
- **Original**: हे महामुने ! उस द्रीपमें विद्वुम, हेमदौल्ल, चयुतिमान्‌, पुष्पवान्‌, कुशेशय, हरि और सातवाँ मन्दराचछ---यथे सात बर्षपर्बत हैं। तथा उसमें सात ही नदियां हैं, उनके नाम क्रमशः सुनो --
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3271)
- **Original**: जे धूतपापा, शिवा, पवित्रा, सम्मति, विद्युत, अम्भा और मही हैं। ये सम्पूर्ण पापोंक्तो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3272)
- **Original**: अण्ड ] अन्या: सहस्नशस्तत्र क्षुद्रनद्यस्तथाचला: । कुशहीपे कुद्ास्तम्बः संज्ञया तस्य तत्स्मृतम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3273)
- **Original**: 44 तत्यमाणेन स॒॒ द्वीपो समावृतः । घृतोदक्ष समुद्रो तै संबृतः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3274)
- **Original**: 45 क्रौअद्वीपो महाभाग श्रूयताज्लापरो महान्‌। कुशद्वीपस्य विस्ताराद द्विगुणो यस्य विस्तर:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3275)
- **Original**: 46 क्रौक्चद्वीपे द्युतिमत: पुत्रास्तस्य महात्मनः । तन्नामानि च वर्षाणि तेषां चक्रे महीपतिः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3276)
- **Original**: 47 कुशल्त्रे मन्दगश्नोष्णः पीवबरो5थान्धकारकः । मुनिश्च दुन्दुभिशैव सप्तैते तत्सुता मुने
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3277)
- **Original**: 48 तत्नापि देवगन्धर्वसेविताः सुमनोहरा: । वर्षाचला महाबुद्धे तेषां नामानि में श्रूणु
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3278)
- **Original**: 49 क्रौक्शश्न॒ वामनश्चैव तृतीयश्चान्धकारकः । चतुथों रत्नहौलअ स्वाहिनी हयसबन्निभ:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3279)
- **Original**: 50 दिवादृत्पद्चमश्षात्र तथान्य: पुण्डरीकवान्‌ । दुन्दुभिश्ष महाशैलो द्विगुणास्ते परस्परम्‌। ड्वीपा द्वीपेषु ये चौला यथा द्वीपेषु ते तथा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3280)
- **Original**: 59 वर्षेध्रेतिषु. रम्येषु तथा चौलवरेषु चा। निवसन्ति निरातड्लाः सह देवगणै: प्रजा:
- **Translation**: 

---

