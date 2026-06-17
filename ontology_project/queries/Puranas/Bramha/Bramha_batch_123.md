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

### Verse 1 (Bramha 0.2441)
- **Original**: 118 न + संक्षिप्त ब्रह्मपुराण * और देवाधिदेव भगवानूसे उत्तरकी ओर एक सुन्दर
- **Translation**: 

---

### Verse 2 (Bramha 0.2442)
- **Original**: स्नान करनेसे सब पापोंका नाश हो जायगा।' तीर्थ (सरोवर) का निर्माण करो। वह तीर्थ मनुष्य-
- **Translation**: 

---

### Verse 3 (Bramha 0.2443)
- **Original**: मार्कण्डेय मुनिसे यों कहकर सर्वव्यापी जनार्दन लोकमें मार्कण्डेयह्दके नामसे विख्यात होगा। उसमें
- **Translation**: 

---

### Verse 4 (Bramha 0.2444)
- **Original**: वहीं अन्तर्धान हो गये। # शॉप मार्कण्डेयेश्वर शिव, बटवृक्ष, श्रीकृष्ण, बलभद्र एवं सुभद्राके दर्शन-पूजनका माहात्म्य ब्रह्माजी कहते हैं--ब्राह्मणो! अब मैं पदञ्नतीर्थकी ; उन्हें प्रसन्न करे-- विधि बतलाऊँगा तथा स्नान, दान और देव-दर्शनसे
- **Translation**: 

---

### Verse 5 (Bramha 0.2445)
- **Original**: ब्रिलोचन नमस्तेउस्तु नमस्ते शशिभूषण। जो फल होता है, उसका वर्णन करूँगा। मार्कण्डेयद्टदमें
- **Translation**: 

---

### Verse 6 (Bramha 0.2446)
- **Original**: त्ाहि मां त्वं विरूपाक्ष महादेव नमोउस्तु ते
- **Translation**: 

---

### Verse 7 (Bramha 0.2447)
- **Original**: जाकर मनुष्य उत्तराभिमुख हो तीन बार डुबकी
- **Translation**: 

---

### Verse 8 (Bramha 0.2448)
- **Original**: “तीन नेत्रोंवाले शंकर! आपको नमस्कार है, लगाये और निप्नाद्धित मन्त्रका उच्चारण करे--
- **Translation**: 

---

### Verse 9 (Bramha 0.2449)
- **Original**: [ चन्द्रमाको भूषणरूपमें धारण करनेवाले! आपको संसारसागर. मग्न॑. पापग्रस्तमचेतनम्‌।
- **Translation**: 

---

### Verse 10 (Bramha 0.2450)
- **Original**: नमस्कार है। विकट नेत्रोंवाले शिवजी ! आप मेरी ज्राहि मां भगनेत्रश्न ब्रिपुयरे नमोउस्तु ते
- **Translation**: 

---

### Verse 11 (Bramha 0.2451)
- **Original**: रक्षा कोजिये। महादेव! आपको नमस्कार है।' नम्र: शिवाय शान्ताय सर्वपापहराय च। इस प्रकार मार्कण्डेयहदमें स्नान करके भगवान्‌ खान॑ करोमि देवेश मम नश्यतु पाठतकम्‌
- **Translation**: 

---

### Verse 12 (Bramha 0.2452)
- **Original**: शंकरका दर्शन करनेसे मनुष्य सब पापोंसे मुक्त हो *भगके नेत्रोंका नाश करनेवाले त्रिपुरशत्रु भगवान्‌
- **Translation**: 

---

### Verse 13 (Bramha 0.2453)
- **Original**: शिवके लोकमें जाता है। शिव! मैं संसार-सागरमें निमग्र, पापग्रस्त एवं
- **Translation**: 

---

### Verse 14 (Bramha 0.2454)
- **Original**: -वहाँसे कल्पान्तस्थायी वटवृक्षके पास जाकर अचेतन हूँ। आप मेरी रक्षा कौजिये। आपको
- **Translation**: 

---

### Verse 15 (Bramha 0.2455)
- **Original**: उसकी तीन परिक्रमा करे। फिर निग्नाद्धित मन्त्रद्वारा नमस्कार है। समस्त पाषोंको दूर करनेवाले शान्तस्वरूप
- **Translation**: 

---

### Verse 16 (Bramha 0.2456)
- **Original**: बड़ी भक्तिके साथ उस बटकी पूजा करे-- शिवको नमस्कार है। देवेश्वर! मैं यहाँ स्नान करता
- **Translation**: 

---

### Verse 17 (Bramha 0.2457)
- **Original**: 4» नमोउव्यक्तरूपाथ महाप्रलयकारिणे। हूँ। मेश सागर पातक नष्ट हो जाय।' भहद्गस्रोपविष्टाय न्यग्रोधाय नमोउस्तु ते
- **Translation**: 

---

### Verse 18 (Bramha 0.2458)
- **Original**: यों कहकर बुद्धिमान्‌ पुरुष नाभिके बराबर
- **Translation**: 

---

### Verse 19 (Bramha 0.2459)
- **Original**: अपरस्त्व॑ सदा कल्पे हरेश्चायतन वंट। जलमें सत्रान करनेके पश्चात्‌ देवताओं और
- **Translation**: 

---

### Verse 20 (Bramha 0.2460)
- **Original**: न्यग्नोध हर में पापं कल्पबृक्ष नमोउस्तु ते
- **Translation**: 

---

