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

### Verse 1 (Vishnu Puran 0.3341)
- **Original**: 80 सत्यानृते न तत्नास्तां द्वीपे पुष्करसंज्ञिते । न तत्र नद्: दशैला वा दीपे वर्षहयान्विते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3342)
- **Original**: 81 तुल्यवेषास्तु मनुजा देबास्तत्रैकरूपिण: । वर्णाश्रमाचारहीन॑.. धर्माचरणवर्जितम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3343)
- **Original**: 82 त्रयी वार्ता दण्डनीतिशुश्रूषारहितश्ल यत्‌। वर्षद््यं तु मैत्रेय भौम: स्वगोंठयमुत्तम:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3344)
- **Original**: 83 सर्वर्तुसुखद: कालो जरारोगादिवर्जित: । धातकीखण्डसंज्ञेटथ महावीरे च ये मुने
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3345)
- **Original**: 84 न्यप्रोधः पुष्करद्वीपे ब्रह्मण: स्थानमुत्तमम्‌ । तस्मिन्निबसति ब्रह्मा पूज्यमानः सुरासुरैः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3346)
- **Original**: 85 स्वादूदकेनोदधिना पुष्कर: परिवेष्टित: । समेन पुष्करस्येव विस्ताराषण्डलं तथा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3347)
- **Original**: 86 एवं द्वीपा: समुद्रैश्न सप्त सप्तभिरावृताः । द्वीपश्लैव समुद्रश्त समानौ द्विगुणो परो
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3348)
- **Original**: 87 पयांसि सर्वदा सर्वसपुद्रेषु समानि वै। न्यूनातिरिक्तता तेषां कदाचित्रेव जायते
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3349)
- **Original**: 88 स्थालीस्थमभिसंयोगादुद्रेकि सत्ठिले यथा । तथेन्दुवृद्ों सलिलमण्भोधौ पुनिसत्तम
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3350)
- **Original**: 89 अन्यूनानतिरिक्ता्ष वर्थन्त्यापो हसन्ति च । उदयास्तमनेष्विन्दो: पक्षयो: शुक्लकृष्णयो:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3351)
- **Original**: 90 द्वितीय अंधा 119 तथा पचास सहस्त्र योजन ऊँचा और इतना ही सब ओर गोलाकार फैला हुआ है।
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3352)
- **Original**: यह पर्वत पुष्करद्वीपरूप गोलेको मानो बीचमेंसे विभक्त कर रहा है और इससे विभक्त होनेसे उसमें दो वर्ष हो गये हैं; उनमेंसे प्रत्येक वर्ष और बह पर्वत बलयाकार हो है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3353)
- **Original**: 36-77।
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3354)
- **Original**: वहाँकि मनुष्य य्ेग, ज्ञोक और रागद्रेषादिसे रहित हुए दस सहस्त्र वर्षतक जीखित रहते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3355)
- **Original**: हे द्विज ! उनमें उत्तम-अधम अथवा वध्य- बधक आदि (विरोधी) भाव नहीं हैं और न उनमें ईर्ष्या, असूया, भय, द्रेष और ल्त्रेभादि दोष ही हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3356)
- **Original**: महावीरवर्ष मानसोत्तर पर्शतके बाहरकी ओर है और धातकी-खण्ड भीतरकी ओर। इनमें देव और दैल्य आदि निवास करते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3357)
- **Original**: दो खण्डोंसे युक्त डस पृष्करद्वीपमें सत्य और मिथ्याक्ता व्यवहार नहीं है और न उसमें पर्वत तथा नदियाँ हो हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3358)
- **Original**: वहाँक्े मनुष्य और देवगण समान वेष और समान रूपयाले होते हैं। है सैत्रेय ! वर्णाश्रमाचारसे हीम, क्म्य कर्मोंसे रहित तथा वेदत्रयी, कृषि, दण्डनीति और शुझ्रूषा आदिसे झून्य वे दोनों वर्ष तो मानों अल्युत्तम भौष (पृथिवीके) स्वर्ग हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3359)
- **Original**: है मूने ? उन सहालीर और धातकी-खण्डनामक वर्षों काल (समय) समस्त ऋतुओमें सुखदायक और जरा तथा गेगादिसे रहित रहता है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3360)
- **Original**: पुष्करद्वीपमें ब्रह्माजीका उत्तम निवासस्थान एक न्यग्रोष (बट) का वृक्ष है, जहां देवता और दानबादिसे पूजित श्रीश्रह्माजी विशजते हैं
- **Translation**: 

---

