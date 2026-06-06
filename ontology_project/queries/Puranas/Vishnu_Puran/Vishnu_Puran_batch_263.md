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

### Verse 1 (Vishnu Puran 0.5241)
- **Original**: 29 कामः क्रोधस्तथा दर्पमोहत्लोभादयश्र ये । तांस्तु सर्वान्परित्यज्य परित्राड निर्ममो भवेत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5242)
- **Original**: 30 अभय सर्वभूतेभ्यो दत्त्वा यश्वरते मुनिः । तस्यापि सर्वभूतेभ्यो न भर्य विद्यते क्चित्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5243)
- **Original**: 31 शारीरमभं स्वपुखे जुहोति । विप्रस्तु भैक्ष्योपहितैहविर्भि- श्वितापिकानां व्रजति सम लोकान्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5244)
- **Original**: 32 मोक्षाश्रम॑ चश्चरते. यथोक्ते शुचिस्तुख॑ कल्पितबुद्धियुक्त: । अनिन्धनं ज्योतिरिव प्रशान्तः स॒ब्रहालोक॑ अ्रयते ह्विजाति:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5245)
- **Original**: 33 त्यागकर तथा मास्सर्यकों छोड़कर चतुर्थ आश्रममें प्रवे: करे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5246)
- **Original**: हे पृच्ितोपते ! भिक्षुक्रो उचित है कि अर्थ, धर्म और कामरूप त़िवर्गसम्बँ्ची समस्त कमोम्मे छोड़ दे, सतु- सित्रादिगें समान भाव रखे और सभी जीवॉका सुहद्‌ हो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5247)
- **Original**: निरन्तर समाहित एहकर जरायुज, अष्डज और स्वदेज आदि समस्त जीवोंसे मन, जाणी अथया कर्मद्वारा कभो ड्रोह न करे तथा सब प्रकारक्ो आसक्तियॉक्ो त्याग दे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5248)
- **Original**: ग्राममें एक रत और पुरसें पाँच राजितक रहे तथा इतने दिन भी तो इस प्रकार रहे जिससे किसीसे प्रेम अथवा ड्वेष न हो
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5249)
- **Original**: जिस समय षरोंमें अभस्‍्रि झात्त हो जाय और स्त्रेण भोजन कर चुकें उस समय प्राणरक्षाके लिये उत्तम बर्णोमे भिक्षाके लिये जाय
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5250)
- **Original**: परित्राजकव् चाहिये कि काम, क्रोध तथा दर्प, छोभ और मोह आदि समस्त दुर्गुणोंको जोड़कर ममताशून्य होकर रहें
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5251)
- **Original**: जो मुनि समस्त ब्राणियॉक्थरे अभयदान देकर विचरता है उसको भी किसीसे कभी कोई भय नहीं होता
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5252)
- **Original**: जो ब्राह्मण चतुर्थ आश्रममें अपने झरीरमें स्थित प्राणादिसहित जठग्रप्निके उद्देश्यसे अपने मुख्में भिक्षान्नरूप हविसे हजन करता है, वह ऐसा अग्मिहोत्र कस्के अग्रिहोत्रियोंके स्जेकॉको प्राप्त हो जाता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5253)
- **Original**: जो ब्राह्मण [ब्रह्मससे भिन्न सभी मिथ्या है, सम्पूर्ण जगत्‌ भगवानका ही संकल्प है--ऐसे] बुद्धियोगसे युक्त होकर, यथाविधि आचरण करता हुआ इस मोश्षाश्रमका पवित्रता और सुखपूर्वक आचरण करता है, बह निरिन्‍्धन अप्रिके समान शान्त होता है और अन्तमें ब्रह्मल्येक्त प्राप्न करता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5254)
- **Original**: ल्च्च्च्ंल् है -कफं्फन- इति श्रीविष्णुपुराणे तुतीयेंड्शे नवमोउ्ध्यायः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5255)
- **Original**: दसवाँ अध्याय जातकर्म, नामकरण और बिवाह-संस्कारकी विधि सगर उवाच कथित चातुराश्रम्य॑ चातुर्व्यक्रियास्तथा । पुंस: क्रियामह ओ्रोतुमिच्छामि द्विजसत्तम
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5256)
- **Original**: नित्यनैमित्तिका: काप्या: क्रिया: पुंसामशेफ्त: । समाख्याहि भृगु्रेष्ट सर्वज्ञो हासि मे मत:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5257)
- **Original**: 2 ऑर्वउवाच यदेतदुक्त भवता नित्यनैमित्तिकाश्रयम्‌। तदह कथविष्यामि श्ृणुश्बकमना मम
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5258)
- **Original**: 1 ] सगर बोले-- हे द्विजश्रेष्ठ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5259)
- **Original**: आपने चारों आंभ्रम और चारों वर्णोकि कर्मोंक्त्र वर्णन किया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5260)
- **Original**: अब मैं आपके द्वारा मनुष्योंके (घोड़ा संस्काररूप) कर्मोंक्तो सुनना चाहता हूँ। 1
- **Translation**: 

---

