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

### Verse 1 (Bramha 0.1201)
- **Original**: होते हैं। इन्द्र, धाता, पर्जन्य, त्वष्टा, पूषा, अर्यमा, होते ही अपनी किरणोंसे संसारका अन्धकार दूर
- **Translation**: 

---

### Verse 2 (Bramha 0.1202)
- **Original**: भंग, विवस्वानू, विष्णु, अंशुमान्‌ु, वरुण और कर देते हैं। अत: उनसे बढ़कर दूसरा कोई देवता
- **Translation**: 

---

### Verse 3 (Bramha 0.1203)
- **Original**: मित्र--इन बारह मूर्तियोंद्वारा परमात्मा सूर्यने सम्पूर्ण नहीं है। वे आदि-अन्तसे रहित, सनातन पुरुष
- **Translation**: 

---

### Verse 4 (Bramha 0.1204)
- **Original**: जगत्‌को व्याप्त कर रखा है। भगवान्‌ आदित्यको एवं अविनाशी हैं तथा अपनों किरणोंसे प्रचण्ड
- **Translation**: 

---

### Verse 5 (Bramha 0.1205)
- **Original**: जो प्रथम पूर्ति है, उसका नाम इन्द्र है। बह रूप धारणकर तीनों लोकोंको ताप देते हैं। सम्पूर्ण
- **Translation**: 

---

### Verse 6 (Bramha 0.1206)
- **Original**: देवराजके पदपर प्रतिष्ठित हैं। बह देवशत्रुओंका देवता इन्हींके स्वरूप हैं। ये तपनेबालोंमें श्रेष्ठ,
- **Translation**: 

---

### Verse 7 (Bramha 0.1207)
- **Original**: नाश करनेवाली मूर्ति है। भगवान्‌के दूसरे बिग्रहका सम्पूर्ण जगत्‌के स्वामी, साक्षी तथा पालक हैं। ये
- **Translation**: 

---

### Verse 8 (Bramha 0.1208)
- **Original**: नाम धाता है, जो प्रजापतिके पदपर स्थित हो ही बारम्बार जोबॉंकी सृष्टि और संहार करते हैं
- **Translation**: 

---

### Verse 9 (Bramha 0.1209)
- **Original**: नाना प्रकारके प्रजावर्गको सृष्टि करते हैं। सूर्यदेवकी तथा ये ही अपनी किरणोंसे प्रकाशित होते, तपते
- **Translation**: 

---

### Verse 10 (Bramha 0.1210)
- **Original**: तीसरी मूर्ति पर्जन्यके नामसे विख्यात है, जो और वर्षा करते हैं। ये धाता, बिधाता, सम्पूर्ण
- **Translation**: 

---

### Verse 11 (Bramha 0.1211)
- **Original**: बादलॉमें स्थित हो अपनी किरणोंद्वारा वर्षा करती भूतोंके आदि कारण और सब जीबोंको उत्पन्न
- **Translation**: 

---

### Verse 12 (Bramha 0.1212)
- **Original**: है। उनके चतुर्थ विग्रहको त्वष्टा कहते हैं। त्वष्टा करनेवाले हैं। ये कभी क्षीण नहीं होते। इनका
- **Translation**: 

---

### Verse 13 (Bramha 0.1213)
- **Original**: सम्पूर्ण बनस्पतियों और ओषधियोंमें स्थित रहते मण्डल सदा अक्षय बना रहता है। ये पितरोंके भी
- **Translation**: 

---

### Verse 14 (Bramha 0.1214)
- **Original**: हैं। उनकी पाँचवीं मूर्ति पृषाके नामसे प्रसिद्ध है, पिता और देवताओंके भी देवता हैं। इनका स्थान
- **Translation**: 

---

### Verse 15 (Bramha 0.1215)
- **Original**: जो अनमें स्थित हो सर्वदा प्रजाजनोंको पुष्टि ध्रुव माना गया है, जहाँसे फिर नीचे नहीं गिरना , करती है। सूर्यकी जो छठी मूर्ति है, उसका नाम पड़ता। सृष्टिके समय सम्पूर्ण जगतू सूर्यसे ही
- **Translation**: 

---

### Verse 16 (Bramha 0.1216)
- **Original**: अर्यमा बताया गया है। वह वायुके सहारे सम्पूर्ण उत्पन्न होता है और प्रलयके समय अत्यन्त
- **Translation**: 

---

### Verse 17 (Bramha 0.1217)
- **Original**: देवताओंमें स्थित रहती है। भानुका सातवाँ विग्रह तेजस्वी भगवान्‌ भास्करमें ही उसका लय होता
- **Translation**: 

---

### Verse 18 (Bramha 0.1218)
- **Original**: भगके नामसे विख्यात है। वह ऐश्वर्य तथा है। असंख्य योगिजन अपने कलेबरका परित्याग
- **Translation**: 

---

### Verse 19 (Bramha 0.1219)
- **Original**: देहधारियोंके शरीरोंमें स्थित होता है। सूर्यदेवको करके वायुस्वरूप हो तेजोराशि भगवान्‌ सूर्यपें ही
- **Translation**: 

---

### Verse 20 (Bramha 0.1220)
- **Original**: आठवों मूर्ति विवस्थान्‌ कहलाती है, बह अग्रनिमें प्रवेश करते हैं। राजा जनक आदि गृहस्थ योगी,
- **Translation**: 

---

