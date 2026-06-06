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

### Verse 1 (Vishnu Puran 0.801)
- **Original**: 9 मदान्धकारिताक्षोउसौ गन्थाकृष्टेन वारण: । करेणाप्राय चिक्षेप तां स्त्र्ज धरणीतले
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.802)
- **Original**: 10 ततश्लुक़्ोध भगबान्दुर्वासा मुनिसत्तम: । मैत्रेय देवराज॑ त॑ क्ुद्धक्षैतदुवाच है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.803)
- **Original**: 11 ऐश्वर्यमददुष्टात्मन्नतिस्तव्योडसि._ वासव । श्रियो धाम स्र॒जं यस्त्वे महत्ता नाभिनन्द्सि
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.804)
- **Original**: 12 प्रसाद ड़ति नोक्ते ते प्रणिपातपुरःसरम्‌। हर्षोत्फुल्लकपोलेन न च्रापि शिरसा धृता
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.805)
- **Original**: 13 मया दत्तामिमरां सालां यस्मान्न बहु मन्‍यसे । त्रैल्ोक्यश्रीरतोी मृढ विनाशमुपयास्यति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.806)
- **Original**: 14 श्रीपराशरजी बोलछे--हे मैत्रेय ! तुमने इस समय मुझसे जिसके विषयमें पूछा है यह श्रीसम्बन्ध (लूक्मीजीका इतिहास) मैंने भी मरीचि ऋषिसे सुना था, यह मैं तुम्हें सुनाता हूँ, (सावधान होकर] सुनो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.807)
- **Original**: एक बार शंकरके अदशाखतार श्रदुर्यासाजी पृथिवीततलमें विचर रहे थे। घूमते-घूमते उन्होंने एक लिद्याधरीके हारथोंमें सन्‍्तानक पुष्पोंको एक दिव्य माला देखी। है बह्मन्‌ ! उसकी गन्धसे सुवासित होकर वह वन वनवासियोंके लिये अति सेवनीय हो रहा था
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.808)
- **Original**: तब उन उत्मत- यृत्तिवाले विप्रवरने वह सुन्दर माल्य देखकर उसे उस विधाधर-सुन्दरीसे माँगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.809)
- **Original**: उनके माँगनेपर उस बड़े-यड़े नेत्रॉंचाली क॒ुआंगी विद्याधरीने उन्हें आदरपूर्वक प्रणाम कर वह माला दे दी
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.810)
- **Original**: हे मैत्रेय ! उन उच्तत्तवेषधारी थिप्रवरने उसे लेकर अपने मस्तकपर डाल लिया और पृथिवापर बिचरने छगे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.811)
- **Original**: इसी समय उन्होंने उन्मत्त ऐराखतपर चढ़कर देवताओंके साथ आते हुए. त्रैल्लेक्याधिपति ज्चौपति इन्दकों देखा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.812)
- **Original**: उन्हें देखकर मुनिवर दुर्वासाने उन्मत्तके समान बह मतबाले भौंणेंसे गुझ्लायमान माला अपने सिरपरसे उताए्कर देवराज इन्द्रक ऊपर फेंक दी
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.813)
- **Original**: देवराजने उसे लेकर ऐरावतके मस्तकपर डाल दी; उस समय बह ऐसी सुशोभित हुई मानों कैलास पर्वतके शिखरपर श्रीगड्जाजी विराजमान हों
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.814)
- **Original**: उस मदोन्‍्मत्त हाथीने भो उसको गन्धसे आकर्षित हो उसे सूँडसे सुँघकर पृथिवीपर फेंक दिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.815)
- **Original**: हे मैत्रेय ! यह देखकर मुनिश्रेष्ठ भगवान्‌ दुर्वासाजी अति क्रोधित हुए और देवराज इच्द्रसे इस प्रकार बोले
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.816)
- **Original**: दुर्वासाजीने कहा-- अरे ऐश्वर्यके मदसे दूषितचित्त इन्द्र ! लू बड़ा छौठ है, तूने मेरी दी हुई सम्पूर्ण शोभावती घाम मालाका कुछ भी आदर नहीं किया !
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.817)
- **Original**: अरे ! तूने न तो प्रणाम करके “बड़ी कृपा की' ऐसा ही कहा और न हर्षसे प्रसन्नवदन होकर उसे अपने सिरपर ही रखा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.818)
- **Original**: रे मृढ़ ! तूने मेरी दी हुई मालाका कुछ भी मूल्य नहीं किया, इसल्लये तेरा त्रिस्जेव्रिका लैभव नष्ट हो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.819)
- **Original**: 30 श्रीखिष्णुपुराण ( अ0 9 मां मन्यसे त्वं॑ सदृश नून॑ झक्रेतरद्विजैः । अतो5बमानमस्मासु मानिना भवता कृतम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.820)
- **Original**: 15 महत्ता भवता यस्मात्क्षिप्ता माला महीतले । तस्मात्रणए्लक्ष्मीकं त्रैल्लोक्यं ते भविष्यति
- **Translation**: 

---

