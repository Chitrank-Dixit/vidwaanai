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

### Verse 1 (Vishnu Puran 0.12441)
- **Original**: 37 हिरण्यधान्यतनयभार्या भृत्यगृहादिषु । एते कर्थ भविष्यन्तीत्यतीब ममताकुछः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12442)
- **Original**: 38 मर्मभिद्धिर्महारोगैः क्रकचैरिब दारुणैः । शरैरिवान्तकस्योग्रैश्छिद्ममानासुबधन:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12443)
- **Original**: 39 परिवर्तितताराक्षो हस्तपादं मुहुः क्षिपन्‌। संशुष्यमाणताल्वोष्ठ पुटो घुरघुरायते
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12444)
- **Original**: 40 निरुद्धकण्ठो. दोषौघैरुदानश्रासपीडितः । तापेन महता व्याप्तस्तृषा चार्त्तस्तथा क्षुधा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12445)
- **Original**: 49 क्लेशादुत्क्रान्तिमाप्रोति यमकिड्भूरपीडित: । ततश्च॒ यातनादेहँ क्लेशेन प्रतिपदाते
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12446)
- **Original**: 42 एतान्यन्यानि चोआणि दुःखानि मरणे नृणाम्‌ । श्रृणुष्न नरके यानि प्राप्यन्ते पुरुषैर्मतैः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12447)
- **Original**: 43 याम्यकिड्भूरपाशादिग्रहणं॑._ दण्डताडनम्‌ । यमस्य दर्शन चोम्रमुग्रमार्गबिलोकनम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12448)
- **Original**: 44 चष्ठ अंश 439 अनुभव किये हुए समस्त पदार्थोकों भी भूल जाता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12449)
- **Original**: उसे एक वाक्य उच्चारण करनेमें भी महान पस्श्रिम होता है तथा श्वास और खाँसी आदिके महान कष्टके कारण वह [ दिन-णत ] जागता रहता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12450)
- **Original**: वृद्ध पुरुष औरोंकी सहायतासे ही ठठता तथा ओऔरोंके बिठानेसे ही बैठ सकता है, अतः वह अपने सेक्‍्क और खी-पुत्रादिके छिये सदा अनादरक् पात्र बना रहता है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12451)
- **Original**: उसका समस्त शौचाचार नष्ट हो जाता है तथा भोग और भोजनकी लालसा बढ जाती है; उसके परिजन भी उसकी हैंसी ठड़ाते हैं और बन्धुजन उससे उदासीन हो जाते हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12452)
- **Original**: अपनी युवावस्थाकी चेष्टाओंक्ो अन्य जतञ्में अनुभव की हुई-सी स्मरण करके वह अत्यन्त सत्तापवज्ञ दीर्घ निःधास छोड़ता रहता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12453)
- **Original**: इस प्रकार वृद्धावस्थामें ऐसे ही अनेकों दुःशन अनुभव कर उसे मरणकालमें जो कष्ट भोगने पड़ते हैं वे भी सुनो
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12454)
- **Original**: कण्ठ और हाथ-पैर शिथिल पड़ जाते तथा शरीरमें अत्यन्त कम्प छा जाता है। बार-बार उसे ग्लानि होती और कभी कुछ चेतना भी आ जाती है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12455)
- **Original**: उस समय बह अपने हिरण्य (सोना), घन-धान्य, पुज्-स्त्री, भृत्य और गृह आदिके प्रति 'इन सबका क्या होगा ?' इस प्रकार अत्यन्त ममतासे व्याकुल हो जाता है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12456)
- **Original**: उस समय मर्मभेटी क्रकाच (आरे) तथा यमराजफे विकराल खाणके समान महाभयड्जभूर रोगोंसे उसके प्राण-बन्धन कटने लगते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12457)
- **Original**: उसकी आँखोंके तारे चढ़ जाते हैं, वह अत्यन्त पीड़ासे बारम्बार हाथ-पैर पटकता है तथा उसके तालु और ओऑठ सूखने लगते हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12458)
- **Original**: फिर क्रमशः दोष-समूहसे उसका कण्ठ रुक जाता है अतः वह “घरघर' शब्द करने लगता है; तथा ऊर्ष्वश्राससे पीड़ित और महान्‌ तपसे व्याप्त होकर श्षुघा-तृष्णासे व्याकुल्ठ हो उठता है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12459)
- **Original**: ऐसी अवस्थामें भी यमदूतोंसे पीड़ित होता हुआ वह बड़े फ्लेझसे दारीर छोड़ता है और अत्यन्त कष्टसे कर्मफल भोगनेके लिये यातना-देह़ प्राप्त करता है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12460)
- **Original**: मरणकालमें मनुष्योंको ये और ऐसे ही अन्य भयानक कष्ट भोगने पड़ते हैं; अब, मरणोपरान्त उन्हें नस्कमें जो यातनाएँ भोगनी पड़ती हैं उह सुनो---
- **Translation**: 

---

