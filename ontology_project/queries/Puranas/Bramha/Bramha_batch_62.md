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

### Verse 1 (Bramha 0.1221)
- **Original**: स्थित हो जीवोके खाये हुए अन्नको पचाती है। बालखिल्य आदि ब्रह्मबादी मंहर्षि, व्यास आदि
- **Translation**: 

---

### Verse 2 (Bramha 0.1222)
- **Original**: उनकी चर्बी मूर्ति विष्णुके नामसे विख्यात है, जो -स्‍ 4 नतनततती-----.. -__*-230«-»न---न--नन0णणननननना 3 धत जिनननणओओ««ं-«णन«म»»--
- **Translation**: 

---

### Verse 3 (Bramha 0.1223)
- **Original**: 62 » संक्षिप्त स्रह्मपुराण * सदा देवशत्रुओंका नाश करनेके लिये अवतार
- **Translation**: 

---

### Verse 4 (Bramha 0.1224)
- **Original**: रहे हैं और करेंगे?” इस प्रकार मन-ही-मन लेती है। सूर्यकी दसवीं मूर्तिका नाम अंशुमान्‌
- **Translation**: 

---

### Verse 5 (Bramha 0.1225)
- **Original**: विचार करके नारदजी मित्र देवतासे योले--' भगवन्‌! है, जो बायुमें प्रतिष्ठित होकर समस्त प्रजाको
- **Translation**: 

---

### Verse 6 (Bramha 0.1226)
- **Original**: अज्जोपाब्रोंसहित सम्पूर्ण वेदों एवं पुराणोंमें आपकी आनन्द प्रदान करती है। सूर्यका ग्यारहवाँ स्वरूप
- **Translation**: 

---

### Verse 7 (Bramha 0.1227)
- **Original**: महिमाका गान किया जाता है। आप अजन्मा, वरुणके नामसे प्रसिद्ध है, जो सदा जलमें स्थित
- **Translation**: 

---

### Verse 8 (Bramha 0.1228)
- **Original**: सनातन, धाता तथा उत्तम अधिष्ठान हैं। भूत, होकर प्रजाका पोषण करता है। भानुके बारहवें
- **Translation**: 

---

### Verse 9 (Bramha 0.1229)
- **Original**: भविष्य और वर्तमान-सत्र कुछ आपमें ही विग्रहका नाम मित्र है, जिसने सम्पूर्ण लोकोंका
- **Translation**: 

---

### Verse 10 (Bramha 0.1230)
- **Original**: प्रतिष्ठित है। गृहस्थ आदि चारों आश्रम प्रतिदिन हित करनेके लिये चन्द्र नदीके तटपर स्थित
- **Translation**: 

---

### Verse 11 (Bramha 0.1231)
- **Original**: आपका ही यजन करते हैं। आप ही सबके पिता, होकर तपस्या की। परमात्मा सूर्यदेवने इन बारह
- **Translation**: 

---

### Verse 12 (Bramha 0.1232)
- **Original**: माता और सनातन देवता हैं। फिर भी आप किस मूर्तियोंके द्वारा सम्पूर्ण जगत्‌को व्याप्त कर रखा
- **Translation**: 

---

### Verse 13 (Bramha 0.1233)
- **Original**: देवता अथवा पितरकी आठाधना करते हैं, यह है। इसलिये भक्त पुरुषोंको उचित है कि वे
- **Translation**: 

---

### Verse 14 (Bramha 0.1234)
- **Original**: हमारी समझनमें नहीं आता।' भगवान्‌ सूर्यपें मन लगाकर पूर्वोक्त बारह मूर्तियोंमें
- **Translation**: 

---

### Verse 15 (Bramha 0.1235)
- **Original**: . भिन्रने कहा--ब्रह्मन! यह परम गोपनीय उनका ध्यान और नमस्कार करें। इस प्रकार [सनातन रहस्य कहने योग्य तो नहीं है; परंतु आप मनुष्य बारह आदित्योंको नमस्कार करके उनके
- **Translation**: 

---

### Verse 16 (Bramha 0.1236)
- **Original**: भक्त हैं, इसलिये आपके सामने मैं उसका यथावत्‌ नामोंका प्रतिदिन पाठ और श्रवण करनेसे सूर्यलोकमें
- **Translation**: 

---

### Verse 17 (Bramha 0.1237)
- **Original**: वर्णन करता हूँ। वह जो सूक्ष्म, अविज्लेय, प्रतिष्ठित होता है। अव्यक्त, अचल, ध्रुव, इन्द्रियरहित, इन्द्रियोंके घुनियोंने पूछा--यदि ये सूर्य सनातन आदिदेव
- **Translation**: 

---

### Verse 18 (Bramha 0.1238)
- **Original**: विषयोंसे रहित तथा सम्पूर्ण भूतोंसे पृथक्‌ है, हैं तो इन्होंने बर पानेकी इच्छासे प्राकृत मनुष्योंकी
- **Translation**: 

---

### Verse 19 (Bramha 0.1239)
- **Original**: वही समस्त जीवोंका अन्तरात्मा है; उसीको क्षेत्रज् भाँति तपस्या क्‍यों की? भी कहते हैं। वह तीनों गुणोंसे भिन्न पुरुष कहा भ्रह्माजी बोले--ब्राह्मणो! यह सूर्यका परम
- **Translation**: 

---

### Verse 20 (Bramha 0.1240)
- **Original**: गया है, उसीका नाम भगवान्‌ हिरण्यगर्भ है। वह गोपनीय रहस्य है। पूर्वकालमें मित्र देवताने
- **Translation**: 

---

