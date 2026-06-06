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

### Verse 1 (Sama Ved 0.2501)
- **Original**: स नः पवस्व वसुमद्धिरण्यवद्वयं स्थाम भुवनेषु ज'वसे
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2502)
- **Original**: हे शक्तिवर्द्धक पवित्र सोम ! सभी में व्याप्त, साक्षी रूप, आप संस्कारित होते हुए हमारे पास पधारें । आपके अनुग्रह से हम सभी धन-सम्पदा से सम्पन्न होकर सुखी जीवन जिएँ
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2503)
- **Original**: 957.ईशान इमा भुवनानि ईयसे युजान इन्दो हरित: सुपर्ण्य: । तास्ते क्षरन्तु मधुमदघृतं पयस्तव बते सोम तिष्ठन्तु कृष्टयः
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2504)
- **Original**: हरे वर्ण के तीवगामी अश्वों (किरणों) से सभी लोकों में संव्याप्तु जगत्‌ के स्वामी, हे तेजस्वी सूर्यरूप सोम ! मधुर स्निग्ध जलधाराओं में आपका रस (शक्ति) स्थिर रहे । हे दिव्य सोम ! आपको प्रेरणा से याजक गण सत्कर्म में निरत रहें
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2505)
- **Original**: 958,पवमानस्य विश्वविद्य ते सर्गा अस॒क्षत। सूर्यस्थेव न रश्मय:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2506)
- **Original**: हे विश्व के ज्ञाता दिव्य सोम ! पवित्र होती हुई आपकी धाराएँ सूर्य की रश्मियों की भाँति तीव्र वेग से नीचे आ रही हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2507)
- **Original**: 959.केतुं कृण्वन्दिवस्परि विश्वा रूपाभ्यर्षसि । समुद्र: सोम पिन्वसे
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2508)
- **Original**: हे विश्वव्यापी सोम ! अन्तरिक्ष में ज्ञान चेतना (विचार-तरंगों) के रूप में संव्याप्त आप (प्राण-पर्जन्य वर्षा के रूप में) जल के माध्यम से हमें विभिन प्रकार का वैभव प्रदान करते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2509)
- **Original**: 960.जज्ञानों वाचमिष्यसि पवमान विश्चर्मणि क्रन्दन्देवो न सूर्य:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2510)
- **Original**: सूर्य रश्मियों की भाँति प्रकाशित होने वाले हे सोमदेव ! स्तुति-गान के साथ पवित्र होते हुए, आप ध्वनिपूर्वक पात्र में स्थिर हो रहे हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2511)
- **Original**: 9631.प्र सोमासो अधन्विषु: पवमानास इन्दवः। श्रीणाना अप्सु वृज्जते
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2512)
- **Original**: दुग्ध आदि पोषक तत्त्वों से युकत, शीतल सोमरस पवित्र होते समय, जल के साथ नीचे रखे हुए पात्र में एकत्र हो रहा है
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2513)
- **Original**: 6.2 सामवेद-संहिता 962.अभि गावो अधन्विषुरापो न प्रवता यती: । पुनाना इन्द्रमाशत
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2514)
- **Original**: शुद्धता को प्राप्त होने वाला सोमरस अध: पात्र (नीचे के बर्तन) में पहुँच कर स्थिर हो रहा है । देवराज इन्द्र इस पवित्र रस का पान करते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2515)
- **Original**: 963.प्र पवमान धन्वसि सोमेन्भाय मादनः । नृभिर्यतों वि नीयसे
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2516)
- **Original**: इन्द्रदेव का उत्साहवर्द्धन करने वाले, हे पवित्र सोम ! शुद्धिकरण की प्रक्रिया के बाद आप ऋष्विजों (याजकों) द्वारा यज्ञ वेदी पर पहुँचाए जाते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2517)
- **Original**: 964.इन्दो यदद्विभि: सुतः पवित्र परिदीयसे । अरमिन्द्रस्थ धाम्ने
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2518)
- **Original**: हे सोमदेव ! पत्थरों से कुचलकर निकालने के बाद आपको छे द्वारा शुद्ध किया जाता है, तब आप इन्द्रदेव के लिए पीने योग्य होते हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2519)
- **Original**: 965.त्वं सोम नृमादन: पवस्व चर्षणीधृति: । सस्नियों अनुमाद्यः
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2520)
- **Original**: प्रशंसा के योग्य हे संस्कारित सोम ! मानव मात्र के आनन्द को बढ़ाने वाले, याजकों के द्वारा धारण किये गये, आप पवित्रता को प्राप्त करें
- **Translation**: 

---

