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

### Verse 1 (Vishnu Puran 0.9241)
- **Original**: 32 काकपक्षधरो बालौ कुमाराबिव पावकी । हसन्तौ च रमन्तौ च चेरतु: सम घहावनम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9242)
- **Original**: 33 क्रचिद्वहन्तावन्योन्य क्रीडमानों तथा परैः । शोपपुप्रैस्सम॑ वत्सांश्नारयन्ती विचेरतु:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9243)
- **Original**: 34 कालेन गच्छता तौ तु सप्तवर्षों महाव्जे । सर्वस्य जगत: पात्मे वत्सपालो बभूवतु:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9244)
- **Original**: 35 ब्रावृदकालस्ततो5तीवमेघोघस्थगिताम्जर: । बभूव वारिधाराभिरैक्य कुर्वन्दिशामिव
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9245)
- **Original**: 36 प्ररूढनवद्ाष्पात्या शक्रगोपाचितामही । तथा मारकतीवासीत्यद्रागविभूषिता
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9246)
- **Original**: 37 ऊहुरुन्पार्गवाहीनि निम्नगाम्भांसि सर्वतः। मनांसि दुर्विनीतानां प्राप्य लक्ष्मी नवामिव
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9247)
- **Original**: 38 न रेजेकन्तरितश्रद्यों निर्मलो मलिनर्घनेः । सद्ठादिवादो मूर्खाणां प्रगल्भाभिरिवोक्तिभि:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9248)
- **Original**: 39 पञश्चम अंश 323 ही चलो, देरी मत करो'
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9249)
- **Original**: तन ये तव्रजवासी वत्सपाछ दल्त याँधकर एक क्षणमें ही छकड़ों और गौओंके साथ उन्हें हाँकते हुए चल दिये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9250)
- **Original**: हे ट्विज ! वस्तुओकि अवदधिष्टीशॉंसे युक्त वह ब्रजभूमि क्षणभरमें ही काक तथा भास आदि पश्षियोंसे व्याप्त हो गयी
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9251)
- **Original**: तब लील्छाविहारी भगवान्‌ कृष्णने गौओंकी अभिवद्धिकी इक्ासे अपने शुद्धचित्तसे वृ्धावन (नित्य- बुन्दाबनधाम) का चिन्तन किया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9252)
- **Original**: इससे, डे द्विजोतम ! अत्यत्त रूज्ष ग्रीष्मकालगें भी वहाँ वर्षाझतुके समान सब ओर नवीन दूब उत्पन्न हो गयी
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9253)
- **Original**: तब समस्त व्रजवासी वृन्दावनमें रहने लूगो
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9254)
- **Original**: - तदनन्तर राम और कृष्ण थी बछड़ोंके रक्षक हो गये और एक स्थानपर रहकर गोप्ठमें बाऊलीला करते हुए दिचरने लछगे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9255)
- **Original**: ये काकपक्षधारी दोनों बालक सिरपर मयूर-पिच्छका मुकुट धारणकर तथा वन्यपुष्पोंके कर्णभूषण पहन म्वालोचित बंेशी आदिसे सब प्रकारके बाजोंकी ध्वनि करते तथा पत्तोंके बाजेसे ही नाना प्रकारकी ध्वनि निकालते, स्कन्दके अंदधापभृत शाख्त-विज्ञास्तर कुमारोंके समान हँसते और खेल्ख्ते हुए उस महावममें विचरने छगे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9256)
- **Original**: कभी एक-दूसरेकों अपने पोठपर छे जाते तथा कभी अन्य ग्वालबालोंके साथ खेलते हुए ये बछड़ोंको चराते साथ-साथ घूमते रहते
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9257)
- **Original**: इस प्रकार उस महाश्रजमें रहते रहते कुछ समय बीतनेपर ले निम्लिललोकपालक वत्सपाल सात यर्षके हो गये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9258)
- **Original**: तब मेघसमूहसे आकाशकों आच्छादित करता हुआ तथा अतिशय यारिधाराओँसे दिशाओको एकरूप करता हुआ बर्षाकाल आया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9259)
- **Original**: उस समय नवीन दूर्वाके बढ़ जाने और बीरबहूटियोंसे* व्याप्त हो जानेके कारण पृथिवी पद्मग़गविभूषिता मरफतमयी-सी जान पड़ने लगी
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9260)
- **Original**: जिस प्रकार नया धन पाकर दुष्ट पुरुषोंका चित्त उच्छुल्लुलल हो जाता है उसी प्रकार नदियोंका जल सब ओर अपना निर्दिष्ट मार्ग छोड़कर बहने छगा
- **Translation**: 

---

