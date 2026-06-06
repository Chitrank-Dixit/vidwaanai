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

### Verse 1 (Vaivtpuran 39.8259)
- **Original**: चाहिये, पर परशुरामजी हठ करते ही रहे। उन्होंने करनेके लिये अन्तःपुरमें जाऊँगा और भक्तिपूर्वक
- **Translation**: 

---

### Verse 2 (Vaivtpuran 39.8260)
- **Original**: अनेकों युक्तियोंद्वार अपना अंदर जाना निर्दोष माता पार्वतीको नमस्कार करके तुरंत ही घरकों
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.8261)
- **Original**: बतलाया। यों परस्पर दोनोंमें वाद-विवाद होता लौट जाऊँगा। जो सगुण-निर्गुण, भक्तोंके लिये
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.8262)
- **Original**: रहा। गणेशजी विनयपूर्वक ही परशुरामको रोकते अनुग्रहके मूर्तरूप, सत्य, सत्यस्वरूप, ब्रह्मज्योति,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 39.8263)
- **Original**: रहे, पर जब परशुरामने बलपूर्वक जाना चाहा सनातन, स्वेच्छामय, दयासिन्धु, दीनबन्धु, मुनियोंके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 39.8264)
- **Original**: तो गणेशजीने रोक दिया। तब परस्परमें वाग्युद्ध ईश्वर, आत्मामें रमण करनेवाले, पूर्णकाम, व्यक्त-
- **Translation**: 

---

### Verse 7 (Vaivtpuran 39.8265)
- **Original**: और करताड़न होने लगा। अन्तमें परशुरामने अव्यक्त, परात्पर, पर-अपरके रचयिता, इन्द्रस्वरूप,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 39.8266)
- **Original**: गणेशजीपर अपना फरसा उठा लिया। तब सम्मानित, पुरातन, परमात्मा, ईशान, सबके आदि,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 39.8267)
- **Original**: कार्तिकेयने बीचमें आकर उन्हें समझाया। परशुरामने अविनाशी, समस्त मड्जलोंके मड्रलस्वरूप, सम्पूर्ण गणेशजीको धक्का दे दिया, वे गिर पड़े। फिर मड्लोंके कारण, सभी मड्जलोंके दाता, शान्त,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 39.8268)
- **Original**: उठकर उन्होंने परशुरामको फटकारा। इसपर समस्त ऐश्वर्यॉंको प्रदान करनेवाले, परमोत्कृष्ट,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 39.8269)
- **Original**: परशुरामने पुनः कुठार उठा लिया। तब गणेशजीने शौघ्र ही संतुष्ट होनेवाले, प्रसन्न मुखवाले, शरणमें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 39.8270)
- **Original**: अपनी सूँड़को बहुत लंबा कर लिया और उसमें आये हुएकी रक्षा करनेवाले, भक्तोंक लिये
- **Translation**: 

---

### Verse 13 (Vaivtpuran 39.8271)
- **Original**: परशुरामको लपेटकर बे घुमाने लगे। जैसे छोटेसे अभयप्रद, भक्तवत्सल और समदर्शी हैं, जिनसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 39.8272)
- **Original**: साँपको गरुड़ ऊपर उठा लेता है, बैसे ही अपने मैंने नाना प्रकारकी विद्याओं और अनेक प्रकारके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 39.8273)
- **Original**: योगबलसे शिवपुत्र गणेशने उनको उठाकर परम दुर्लभ शस्त्रोंको प्राप्त किया है; उन जगदीश्वर [स्तम्भित कर दिया और सप्तद्वीप, सप्तपर्वत, गुरुके इस समय मैं दर्शन करना चाहता हूँ। यों
- **Translation**: 

---

### Verse 16 (Vaivtpuran 39.8274)
- **Original**: सप्तसागर, भूलोंक, भुवर्लोक, स्वलोक, जनलोक, कहकर परशुराम गणपतिके आगे खड़े हो गये।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 39.8275)
- **Original**: तपोलोक, ध्रुवलोक, गौरीलोक, शम्भुलोक उनको इसपर श्रीगणेशजीने उनको बहुत तरहसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 39.8276)
- **Original**: दिखा दिये। तदनन्तर उन्हें गम्भीर समुद्रमें फेंक समझाया कि इस समय भगवान्‌ शंकर और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 39.8277)
- **Original**: दिया। जब वे तैरने लगे तो पुनः पकड़कर उठा माताजी अन्तःपुरमें हैं। आपको वहाँ नहीं जाना
- **Translation**: 

---

### Verse 20 (Vaivtpuran 39.8278)
- **Original**: लिया और घुमाते हुए बैकुण्ठ दिखलाकर फिर
- **Translation**: 

---

