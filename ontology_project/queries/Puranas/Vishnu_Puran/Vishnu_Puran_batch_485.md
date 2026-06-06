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

### Verse 1 (Vishnu Puran 0.9681)
- **Original**: 33 आजीवो या: परस्तेषां गाबस्तस्य चर कारणम्‌ । ता गावो वृष्टिवातेन पीड्यन्तां वचनान्मप
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9682)
- **Original**: 4 अहमप्यद्रियूड्ाभं॑ तुड्डमारुह्दा वारणम्‌। साहाय्य॑ व: करिष्यामि वास्वम्बूत्सर्गयोजितम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9683)
- **Original**: 5 औपरादार उवाच जृत्याज्ञप्तास्ततस्तेन मुसुचुस्ते बलाहका: । वातवर्ष महाभीमम्रभावाय गयां द्विज
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9684)
- **Original**: 6 ततः क्षणेन पृथिब्री ककुभो5म्बरमेज च
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9685)
- **Original**: णएकं धारामहासारपूरणेनाभवन्पुने
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9686)
- **Original**: 7 विद्युल्लताकशाघातत्रस्तिरिव. घनैर्घनम्‌ । नादापुरितदिक्चक्रैर्धारासारमपात्यत._
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9687)
- **Original**: 8 अन्धकारीकृते लोके वर्षद्धिरनिशं घन: । अधश्ो््व॑ च॒ तिर्यक्‌ च जगदाप्यमिवाभवत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9688)
- **Original**: 9 गावस्तु लेन पतता वर्षबातेन बेगिना। धूता: प्राणाझ्जहुस्सन्नत्रिकसक्थिहिरोधरा:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9689)
- **Original**: 90 क्रोडेन वत्सानाक्रम्य तस्थुरन्‍्या महामुने
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9690)
- **Original**: गाबो बिवत्साश्न कृता बारिपूरेण चापरा:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9691)
- **Original**: 11 वत्साक्ष दीनवदना वातकम्पितकन्थरा: । अ्ाहि त्राहीत्यल्पशब्दा: कृष्णमूच्रुरिब्रातुरा:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9692)
- **Original**: 12 भ्रीपराशरजी बोले--हे मैत्रेय ! अपने यह्षके रुक जानेसे इच्धने अत्यन्त रोषपूर्वक संवर्तक नामक मेघोंके दलसे इस प्रकार कहा--
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9693)
- **Original**: “रे सेथो ! मेरा यह्र वचन सुनो और मैं जो कुछ कहूँ उसे मेरी आज्ञा सुनते ही, बिना कुछ सोचे-खिचारे तुरन्त पूरा करे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9694)
- **Original**: देखो अन्य गोपोंके सहित दुर्बुद्धि नन्‍्दगोपने कृष्णकी सहायताके बलसें अन्या होकर मेरा यज्ञ भंग कर दिया है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9695)
- **Original**: अतः जो उनकी परम जोविका और उनके गोपत्वका कारण है. उन गौओंको तुम मेरी आज्ञासे वर्षा और वायुके द्वारा पीडित कर दो
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9696)
- **Original**: मैं भी पर्वत-शिख़रके समान अत्यन्त ऊँचे अपने ऐराबत हाथीपर चढ़कर वायु और जल छोड़नेके समय तुम्हारी सहायता करूँगा''
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9697)
- **Original**: श्रीपराह्रजी बरोछे--हे ट्विज ! इच्धकी ऐसी आज्ञा होनेपर गौओंक्यो नष्ट करनेके लिये मेघोंने अति प्रचण्ड वायु और वर्षा छोड़ दी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9698)
- **Original**: है मुन! उस समय एक क्षणमें ही मेघोंकी ब्लोड़ी हुई महान्‌ जलधाराओंसे पृथिबरी, दिदाएँ और आकाश एकरूप हो. गये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9699)
- **Original**: सेबगण मानो. विध्ुल्कतारूप दण्डाघातसे भयभीत होकर महान्‌ शब्दसे दिज्ञाओंकों ज्यात करते हुए घृसलाधार पानी बरसाने छगे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9700)
- **Original**: इस प्रकार मेथोंके अहर्निज्ञ बरसनेसे संसारके अन्धकारपूर्ण हो जानेपर ऊपर-नीचे और सब ओस्से समस्त छोफ जऊूमय-सा हो गया
- **Translation**: 

---

