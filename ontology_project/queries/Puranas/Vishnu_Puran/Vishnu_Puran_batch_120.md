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

### Verse 1 (Vishnu Puran 0.2381)
- **Original**: 39 सकते हैं। और मुझे तो बिचार भी बहुत ही कम है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2382)
- **Original**: इस विषयमें अधिक क्या कहा जाय ? [ मेरे विचारसे तो ) सबके अन्तःकरणोमें स्थित एकमात्र वे ही संसारके स्वामी तथा उसके रचयिता, पार्क और संहारक हैं। 27
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2383)
- **Original**: से ही भोक्ता और भोज्य तथा ये ही एकमात्र जगदीश्वर हैं। हे गुरुणण ! मैंने वाल्यभावसे यदि कुछ अनुचित कहा हो तो आप क्षमा करें”
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2384)
- **Original**: पुरोहितगण बोले-- अरे बालक ! हमने तो यह समझकर कि तू फिर ऐसी बात न कहेगा तुझे अग्रिमें जलनेसे बचाया है। हम यह नहीं जानते थे कि तू ऐसा बुद्धिहीन है ?
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2385)
- **Original**: रे दुर्मते ! यदि तू हमारे कहनेसे अपने इस मोहमय आग्रहको नहीं छोड़ेगा तो हम तुझे नष्ट करनेके लिये कृत्या उत्पन्न करेंगे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2386)
- **Original**: प्रह्मदजी बोले--कौन जीव किससे मारा जाता है और कौन किससे रक्षित होता है ? जुम और अशुभ आचरणोंके द्वारा आत्मा स्वयं ही अपनी रक्षा और नाहा करता है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2387)
- **Original**: कमेकि कारण ही सब उत्पन्न होते हैं और कर्म ही उनको झुभाझुभ गतियोंके साधन हैं। इसलिये प्रयत्रपूर्वक्ष शुभकर्मोंक्रा ही आचरण करना चाहिये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2388)
- **Original**: श्रीपराशरजी ज्ोछे--उनके ऐसा कहनेपर उन दैत्यगजके पुरोहितोंने क्रोघित होकर अप्नरिशिखाके समान प्रज्यल्ित आरीरवाली कृत्या उत्पन्न कर दी
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2389)
- **Original**: उस अति भयंकरीने अपने पादाघातसे पृथित्रीको कम्पित करते हुए वहाँ प्रकट होकर बड़े क्रोधसे प्रह्लादजीकी ख्तीमें क्रिशुलसे प्रहर किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2390)
- **Original**: किन्तु उस बालकके बक्ष/स्थलमें छणते ही वह तेजोमय त्रिशूल टूटकर पृथिवीपर गिर पड़ा और वहाँ गिरनेसे भी उसके सैकड़ों टुकड़े हो गये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2391)
- **Original**: जिस हृदयमें निरन्तर अक्षुण्णभावसे श्रीहरिंभगवान्‌ विराजते हैं उसमें लगनेसे तो वजके भी टूक- टूक हो जाते हैं, त्रिशुलकी तो बात ही क्या है 7
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2392)
- **Original**: उन पापी पुरोहितोने उस निष्पाप आालकपर कत्याका प्रयोग किया था; इसल्ब्ये तुरन्त हो उसने उनपर बार किया और स्वयं भी नष्ट हो गयी
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2393)
- **Original**: अपने गुरुओंको कृत्याद्यारा जलाये जाते देख महामति प्रह्माद 'हे कृष्ण ! रक्षा करो
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2394)
- **Original**: हे अनन्त ! बचाओ !' ऐसा कहते हुए उनकी ओर दौड़े
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2395)
- **Original**: अ्रह्लादजी कहने लूगे--हे सर्वव्यापी, थिश्ररूप, विश्वस्नष्टा जाार्दन ! इन ब्राह्मणोंकी इस मन्त्राग्ररूप
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2396)
- **Original**: <6 यथा सर्वेषु भूतेषु सर्वव्यापी जगदगुरु: । विष्णुरेज तथा सर्वे जीवन्तवेते पुरोहिता:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2397)
- **Original**: 40 यथा सर्वंग्त विष्णुं मन्यमानोउनपायिनम्‌ । चिन्तयाम्यरिपक्षेपि जीवन्ल्वेते पुरोहिता:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2398)
- **Original**: 49 ये हन्तुमागता दत्त यैर्जिषं यैहताशनः । चैर्दिमाजैरह॑ क्षुण्णो दष्ट: सर्पैश्न यैरपि
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2399)
- **Original**: 42 तेब्ूह॑ मिज्रभावेन सम: पापो5स्सि न क्चित्‌। यथा तेनाद्य सत्येन जीवन्स्वसुरयाजका:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2400)
- **Original**: 43 श्रीपराद्ार उवाच इत्युक्तास्तेन ते सर्वे संस्पृष्टाअ निरापया: । समुत्तस्थुद्दिजा भूयस्तमूचु: प्रश्रयान्वितम्‌
- **Translation**: 

---

