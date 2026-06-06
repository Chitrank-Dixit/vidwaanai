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

### Verse 1 (Vishnu Puran 0.9421)
- **Original**: 70 पश्चषम अंझ 329 अखिलभुवनाश्रय आप ? [ इसके साथ आपका द्वेष कैसा ? ]
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9422)
- **Original**: अत: ' है जगत्स्वामिन्‌ ! इस दीनपर दया कीजिये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9423)
- **Original**: हे प्रभो
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9424)
- **Original**: अब यह नाग अपने प्राण छोड़ने ही चाहता है; कृपया हमें पतिकी भिक्षा दीजिये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9425)
- **Original**: हे भुवनेश्वर ! हे जगन्नाथ ! हे महापुरुष ! हे पूर्वज ! यह नाग अब अपने प्राण छो्ठना ही चाहता हैं; कृपया आप हमें पतिकी भिक्षा दीजिये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9426)
- **Original**: हे वेदात्तवेद्य- देखेश्वर
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9427)
- **Original**: है दुष्ट-दैत्य-दलन !! अब यह नाग अपने प्राण छोड़ना ही चाहता है; आप हमें पतिकी घिक्षा दीजिये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9428)
- **Original**: श्रीपराइरजी खोले--नागपत्रियोंके ऐसा कहनेपर थका-माँदा होनेपर भी नागराज कुछ ढाँडस बाँघकर ध्धरि- धरे कहने लगा “हे देवदेव ! प्रसन्न होइये''
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9429)
- **Original**: काल्ियनाग बोल्मम--हे नाथ ! आपका स्वाभाविक अष्टगुण विशिष्ट परम ऐश्वर्य निरतिद्ाय है [ अर्थात्‌ आपसे बढ़कर किसोंका भी ऐश्रर्य नहीं है], अत: मैं किस प्रकार आपकी स्तुत्ति कर सकूँगा ?
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9430)
- **Original**: आप पर हैं, आप पर (मूलप्रकृति) के भी आदिकारण हैं, हे परात्मक ! परकी प्रयत्ति भी आपहीसे हुई है,अतः आप परसे भी पर हैं फिर मैं किस प्रकार आपकी स्तुति कर सकूँगा 2?
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9431)
- **Original**: जिनसे बह्मया, रुद्र, चन्द्र, इन्द्र, मरुद्रण, अश्रिनीकुमार, बसुगण और आदित्य आदि सभी उत्पन्न हुए हैं उन आपकी मैं किस प्रकार स्तुति कर सकूँगा ?
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9432)
- **Original**: यह अवयर्वाशमात्र है, उन आपकी मैं किस प्रकार स्तुति कर सकूँगा ?
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9433)
- **Original**: जित सदसत्‌ (कार्य कारण) स्वरूफ्के खास्तजिक रूपको ब्रह्मा आदिदेवेध्रगण भी नहीं जानते उन आएकी मैं किस प्रकार स्तुति कर सकूँगा?
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9434)
- **Original**: जिनकी पूजा ब्रह्मा आदि देवगण नन्दनबनके पुष्प, गन्ध और अनुल्पन आदिसे करते हैं उन आपकी मैं किस प्रकार पूजा कर सकता हूँ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9435)
- **Original**: देवराज इन्द्र जिनके अवताररूपॉकी सर्वदा पूजा करते हैं तथापि यथार्थ रूपको नहीं जान पाते, उन आपकी मैं किस प्रकार पूजा कर सकता हूँ?
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9436)
- **Original**: योगिगण अपनी समस्त इन्द्रियोंकी उनके विषयोसे स्लींचकर जिनका ध्यानद्वारा पूजन करते हैं उन आपकी मैं किस प्रकार पूजा कर सकता हूँ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9437)
- **Original**: जिन प्रभुके स्वरूपकी चित्तमें भावना करके योगिजन भावमय पुष्प आदिसे ध्यानद्वार उपासना करते हैं उत आपको मैं किस प्रकार पूजा कर सकता हूँ ?
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9438)
- **Original**: हे देवेशर ! आपकी पूजा अथवा स्तृति करनेमें मैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9439)
- **Original**: 330 श्रीविष्णुपुराण [ अ0 7 सर्पजातिरियं क्रूरा यस्यां जातो5स्मि केशव । तत्स्वभावो5यमत्नास्ति नापराधो ममाच्युत
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9440)
- **Original**: 71 सृज्यते भक्‍ता सर्व तथा संडियते जगत्‌। जातिरूपस्वभावाश्च सृज्यन्ते सृजता त्वया
- **Translation**: 

---

