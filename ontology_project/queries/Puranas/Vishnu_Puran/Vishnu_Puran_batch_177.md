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

### Verse 1 (Vishnu Puran 0.3521)
- **Original**: 50 विद्याविद्येति मैत्रेय ज्ञानमेवोपधारय
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3522)
- **Original**: 51 एबमेतन्म्रयाख्यातं भवतो मण्डलें भुवः। पातालानि चर सर्वाणि तथैव नरका द्विज
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3523)
- **Original**: 52 सद्बेपात्सर्वमाख्यातं कि भूयः श्रोतुमिच्छसि
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3524)
- **Original**: 53 श्रीकृष्णस्मरण सर्वश्रेष्ठ है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3525)
- **Original**: जिस पुरुषके च्त्तमें पाप-कर्मके अन्तर पश्चालाप होता है उसके लिये ही प्रायक्षित्तोंका विधान है। किंतु यह हरिस्मरण तो एकमात्र स्वये ही परम प्रायश्चित्त है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3526)
- **Original**: ध्रात:काल, सायेकाल, रात्रिमिं अथबा मध्याह्में किसी भो समय श्रोनारायणका स्मरण करनेसे पुरुषके समस्त पाप तत्काल क्षीण हो जाते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3527)
- **Original**: श्रीविष्णुमगवानके स्मरणसे समस्त पापणशिके भस्म हो जानेसे पुरुष मोक्षपद पघाप्त कर छेता है, स्वर्ग-त्वभ तो उसके स्तये विधरूप माना जाता है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3528)
- **Original**: हे मैत्रेय ! जिसका चित्त जप, होम और अर्चनादि करते हुए निरन्तर भगवान्‌ वासूुदेवमें लगा रहता है उसके लिये इन्द्रपद आदि फल तो अन्तराय (विश्न) हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3529)
- **Original**: कहाँ तो पुनर्जन्मके चक्रमें डालनेवाली स्वर्ग-प्राप्ति और कहाँ मोक्षका सर्वोत्तम बीज 'जबासुदेव' नामका जप !
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3530)
- **Original**: इसलिये हे मुने ! श्रीविष्णुभगवानका अहर्निश स्मरण करनेसे सम्पूर्ण पाप क्षीण हो जानेके कारण मनुष्य फिर नरकमें नहीं जाता
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3531)
- **Original**: चित्तको प्रिय छगनेवाल्ता ही स्वर्ग है और उसके बिपरीत ( अप्रिय लगनेबाल्त्र) ही नरक है । हे द्विजोत्तम ! पाप और पुण्यहोके दूसरे नाम नरक और स्वर्ग हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3532)
- **Original**: जब कि एक ही वस्तु सुख और दुःख तथा ईर्ष्य और कोपका कारण हो जाती है तो उसमें बस्तुता (नियतस्वभावत्व) ही कहाँ है 2
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3533)
- **Original**: क्योंकि एक हो वस्तु कभी प्रीतिकी कारण होती है तो बह्ही दूसरे समय दुःखदायिनी हो जाती है और वहों कभी क्रोधको हेतु होती है तो कभी प्रसन्नता देनेवाली हो जाती है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3534)
- **Original**: अतः कोई भी पदार्थ दुःखमय नहीं है और न कोई सुखमय है । ये सुख-दुःख तो मनके ही खिकार हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3535)
- **Original**: [परमार्थतः] ज्ञान हीं परअह्म है और [अविद्याकी उपाधिसे) वही बन्धनका कारण है । यह सम्पूर्ण विश्व ज्ञानमय ही है; ज्ञानसे घिन्न और कोई वस्तु नहीं है। हे मैत्रेय ! विद्या और अविद्याक्तों भी तुम ज्ञान ही समझो
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3536)
- **Original**: है द्विज ! इस प्रक्तार मैंने तुमसे समस्त भूमण्डल, सम्पूर्ण पाताऊलोक और नस्कॉंका वर्णन कर दिया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3537)
- **Original**: समुद्र, पर्वत, द्वीप, वर्ष और नदियाँ --बन सभीकी मैंने संक्षेपसे व्याख्या कर दी; अब, तुम और क्या सुनना चाहते हो 2?
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3538)
- **Original**: वतन औ इति श्रीविष्णुपुराणे द्वितोयें5शे पश्ठोउ्ध्याय:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3539)
- **Original**: क्क्ततन औ पान
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3540)
- **Original**: श्रीविष्णुपुपण सातवाँ अध्याय भूर्भुष: आदि सात ऊर्ध्वलोकॉका वृत्तान्त औमैत्रेय उठाच कथित धूतल॑ ब्रह्मन्म्रमैतदखिलं त्वया। भुवर्लोकादिकॉल्लोकाउप्छेतुमिच्छाम्यहं मुने
- **Translation**: 

---

