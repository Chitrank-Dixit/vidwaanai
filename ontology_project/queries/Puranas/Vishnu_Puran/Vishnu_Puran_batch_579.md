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

### Verse 1 (Vishnu Puran 0.11561)
- **Original**: 32 राम राम महाबाहो क्षम्यतां क्षम्यतां त्वया । उपसंह्वियतां कोप: प्रसीद मुसलायुध
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11562)
- **Original**: 33 एप साम्बस्सपत्नीकस्तव निर्यातितों बल । अविज्ञातप्रभावाणां क्षम्यतामपराधिनाम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11563)
- **Original**: 34 श्रीपराजर उताच ततो निर्यातयामासुस्साम्ब पत्नीसमन्वितम्‌। निष्क्रम्य स्वपुरात्तूण कौरवा मुनिपुड्व
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11564)
- **Original**: 35 भीष्मद्रोणकृपादीनां प्रणम्य बदतां प्रियम्‌। क्षात्तमेव मयेत्याह बलो बलवतां बर:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11565)
- **Original**: 36 अद्याप्याघूर्णिताकारं लक्ष्यते तत्पुरं द्विज । एप प्रभावों रामस्थ बलज्ञौयोंपलक्षण:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11566)
- **Original**: 37 ततस्तु कौरवास्साम्ब॑ सम्पूज्य हलिना सह । प्रेषयामासुरुद्वाहधनभार्यासमन्वितम्‌. _
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11567)
- **Original**: 38 पश्षम अंश 407 कौरवोंको धिक्तार है जिन्हें सैकड़ों मनुष्योंके उच्छिष् राजसिंहासनमें इतनी तुष्टि है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11568)
- **Original**: जिनके सेवकोंकी स्याँ भी पारिजात-वृक्षकी पुष्प-मज्जरी धारण करती हैं यह भी इन कौरवोंके महाराज नहीं है ? [यह कैसा आश्चर्य है ?]
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11569)
- **Original**: बे उम्रसेन ही सम्पूर्ण राजाओंके महाराज बनकर रहें। आज मैं अकेल्प ही पृथिवीको कौरवहीन कस्के उनकी द्वास्कापुरीको जाकँगा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11570)
- **Original**: आज कर्ण, दुर्योधन, द्रोण, भीष्म, बराढ़िक, दुश्झासनादि, भूरि, भूरिश्रवा, सोमदत्त, दाल, भीम, अर्जुन, युधिष्ठिर, नकुल और सहदेव तथा अन्यान्य समस्त कौरवॉको उनके हाथी- घोड़े और रथके सहित मारकर तथा नववधूके साथ वीरवर साम्बको लेकर ही मैं ट्वारकापुरीमें जाकर उम्रसेन आदि अपने बन्धु-बान्धवॉको देखूगा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11571)
- **Original**: 27--29
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11572)
- **Original**: अथवा समस्त कौरवोंके सहित उनके निवासस्थान इस हस्तिनापुर नगरको ही अभी गद्जाजीमें फेंके देता हूँ"
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11573)
- **Original**: श्रीपराझ्रजी बोलछे--ऐसा कहकर मदसे अरुणनयन मुसल्तयुध श्रीबलभद्रजीने हलकी नॉकको हस्तिनापुरके खाई और दुर्गसे युक्त प्राकारके मूलमें लगाकर खींचा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11574)
- **Original**: उस समय सम्पूर्ण हस्तिनापुर सहसा डगमगाता देख समस्त कौरवगण क्षुब्धचित्त होकर भयभीत हो गये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11575)
- **Original**: [और कहने ऊगे--] “हे राम ! हे राम ! हे महायाहो ! क्षमा करो, क्षमा करो
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11576)
- **Original**: हे मुसलायुध ! अपना कोप झान्त करके प्रसन्न होइये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11577)
- **Original**: हे बलराम ! हम आपको पत्नीके सहित इस साम्बकों सौंपते हैं। हम आपका प्रभाव नहीं जानते थे, इसीसे आपका अपराध किया; कृपया क्षमा कीजिये"
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11578)
- **Original**: श्रीपराशरजी बोले--हे मुनिश्रेष्ठ ! तदनन्तर कौरवोने तुरत्त ही अपने नगरसे बाहर आकर पत्नीसहित साम्बको श्रीबलरामजीके अर्पण कर दिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11579)
- **Original**: तब प्रणामपूर्वक प्रिय वाक्य बोलते हुए भोष्म, द्रोण, कृप आदिसे बीस्वर बलरामजीने कह्ा-- अच्छा मैंने क्षमा किया"
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11580)
- **Original**: है द्विज ! इस समय भी हस्तिनापुर [ गज़्ाकी ओर ] कुछ झुका हुआ-सा दिखायो देता है, यह श्रीबलरामजीके नल ओर शुरवीरताका परिचय देनेवाल्य उनका प्रभाव ही है
- **Translation**: 

---

