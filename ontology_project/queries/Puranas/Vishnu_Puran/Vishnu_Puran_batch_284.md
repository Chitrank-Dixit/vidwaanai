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

### Verse 1 (Vishnu Puran 0.5661)
- **Original**: अतः प्राज् पुरुषको वही सत्य कहना चाहिये जो टूसरोंकी प्रसक्नताका कारण हो। यदि किसी सत्य वाक्यके कहनेसे दूसरोंको 'ख होता जाने तो मौन रहे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5662)
- **Original**: यदि प्रिय वाक्यको भो अहितकर समझे तो उसे न कहे; उस अबस्थामें तो हितकर वाक्य ही कहना अच्छा है, भले ही वह अस्यन्त अप्रिय क्‍यों न हो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5663)
- **Original**: जो कार्य इहस्ज्रेक और परलेकमें आ्राणियोँंके हितका साधक हो मतिमान्‌ पुरुष मन, बचन और कर्मसे उसीका आचरण करे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5664)
- **Original**: कै कतततताः इति श्रीविष्णुपुराणे तृतीयेंठशे द्वादशोउध्याय:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5665)
- **Original**: कज-++ और ततततन+ तेरहवाँ अध्याय आभ्युदयिक श्आद्ध, प्रेतकर्म तथा श्राद्धादिका विचार अर्थ उवाच सचैलस्य पितु: स्त्रान॑ जाते पुत्रे विधीयते । जातकर्म तदा कुर्याच्छुद्धमभ्युदये खच यत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5666)
- **Original**: 91 गग्पालेबांश्व पित्रयांश्व सम्यवसब्यक्रमाद द्विजान्‌ । पूजयेद्धोजयेशैवतन्मना नान्यमानस:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5667)
- **Original**: 2 दघ्यक्षतैस्सबदौ: प्राडमुखोदडमुखोउपि वा। देवतीर्थेन वै पिण्डान्दद्यात्कायेन वा नृप
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5668)
- **Original**: 3 नान्‍्दीमुखः पितृगणस्तेन श्राद्धेन पार्थिव । प्रीयते तत्तु कर्त्तव्य॑ पुस्षैस्सर्ववृद्धिपु
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5669)
- **Original**: 4 कन्यापुत्रतिवाहेषु प्रवेशिषु च्॒ वेइमन: । नामकर्मणि बालानां चूडाकर्मादिके तथा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5670)
- **Original**: 5 सीमत्तोन्नयने चैव पुत्रादिमुखदर्शने । नान्दीमुर्ख पितृगर्ण पूजयेट्ययतो गृही
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5671)
- **Original**: & पितृपूजाक्रम: प्रोक्तो वृद्धावेष सनातन: । श्रूयतामवनीपाल प्रेतकर्मक्रियाविधि: ।। 7 प्रेतदेह शुभै: स्त्रानेस्स्नापितं स्रम्बिभूषितम्‌ । दग्ध्वा ग्रामाइहि: स््रात्वा सचैलस्सलिलाशये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5672)
- **Original**: 8 31. अंगुल्क्ियोंके आप्रभाग
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5673)
- **Original**: 2. कनिष्ठिकाका मूछ॒भाग
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5674)
- **Original**: और्य ओले--पृत्र्के उत्पन्न होनेपर पिताको सचैल (यस्नरोंसहित) स्नान करना चाहिये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5675)
- **Original**: उसके पश्चात्‌ जात- कर्म-संस्कार और आध्युदयिक श्राद्ध करने चाहिये 4 1
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5676)
- **Original**: फिर तन्मयभावसे अनन्यचित्त होकर देवता और पितुगणके किये क्रम: दायीं और आयीं ओर बिठाकर दो-दो ब्राह्मणोंका पूजन करे और उन्हें भोजन करावे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5677)
- **Original**: हैं राजन्‌ ! पूर्व अथवा उत्तरकी ओर मुख करके दक्चि, अक्षत और बदरीफलसे बने हुए पिण्डॉको देवतीर्थ' या प्रजापतितोर्थसे' दान करें
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5678)
- **Original**: है पृथिवीनाथ ! इस आधभ्युदयिक आद्धसे नान्‍दीमुख नामक पितृगण प्रसतन्र होते हैं, अतः सब प्रकारकी अधिवद्धिके समय पुरुषोंको इसका अनुष्ठान करना चाहिये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5679)
- **Original**: कन्या और पुक््के विवाहसें, गृहप्रवेदमें, बाल्कोंके नामकरण तथा चूडाकर्म आदि संस्कारोमें, सीमन्तोन्नयन-संस्कारमें और पुत्र आदिके मुस्त् देखनेके समय गृहस्थ पुरुष एकाग्रचित्तसे ना-दीमुख नामक पितृगणका पूजन करें
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5680)
- **Original**: हे पृथिवीपाल ! आशभ्युदबिक श्राद्धमें पितुपूजाका यह सनातन क्रम तुमको सुनाया, अब प्रेतक्रियाकी विधि सुनो
- **Translation**: 

---

