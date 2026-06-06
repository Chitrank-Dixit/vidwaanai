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

### Verse 1 (Vishnu Puran 0.9841)
- **Original**: 28 घेनुकोउ्य मया क्षिप्तो विचरत्तु यथेच्छया । गावो ब्रवीति चैवान्या कृष्णलीलानुसारिणी
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9842)
- **Original**: 29 एवं नानाप्रकारासु कृष्णचेष्टासु तास्तदा । गोष्यो व्यग्रा: सम चेरू रम्य वृन्दावनान्तरम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9843)
- **Original**: 30 वित्तेक्यैका भुव॑ प्राह गोपी गोपवराड्रना । पुलकाशितसर्वाड्री विकासिनबनोत्पछा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9844)
- **Original**: 31 ध्वजवज्ाडुशाब्जाडूरेखावन्यालि पश्यत । पदान्येतानि कृष्णस्य लीलालल्तिगामिन:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9845)
- **Original**: 32 कापि तेन समायाता कृतपुण्या मदालसा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9846)
- **Original**: पदानि तस्थाक्षैतानि घनान्यल्पतनूनि च
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9847)
- **Original**: 33 पुष्पापचयमत्रोचैश्क्रे दामोदरों ध्रुवम्‌। ओनाग्राक्रान्तमात्राणि पदान्यत्र महात्मनः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9848)
- **Original**: 34 अन्नोपविश्य बै तेन काचित्युष्पैरलडुतता । अन्यजन्मनि सर्वात्मा विष्णुरभ्यर्चितस्तया ।। 35 पुष्पवन्धनसम्मानकृतमानामपास्थय ताम्‌ । नन्‍्दगोपसुतो यातो मार्गेणानेन पशुयत
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9849)
- **Original**: 36 अनुयातैनमत्रान्या नितम्बभरमन्धरा । या गन्तव्ये दूत याति निम्नपादाग्रसंस्थिति:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9850)
- **Original**: 37 हस्तन्यस्ताअहस्तेय॑ तेन याति तथा सखी । अनाचत्तपदन्यासा लक्ष्तते पदपद्धति:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9851)
- **Original**: 38 हस्तसंस्पर्शमात्रेण धुर्तेनेषा विमानिता । नैराश्यान्मन्दगामिन्या निवृत्त लक्ष्यते पदम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9852)
- **Original**: 39 पश्षम अंझ 3457 गति तो देखो ।'* दूसरी कहती-- कृष्ण तो मैं हूँ, अहा ! मेरा गाना तो सुनो"
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9853)
- **Original**: कोई अन्य गोपी भुजाएँ डॉककर बोछ उठती--“आरे दुष्ट काल्किय ! मैं कृष्ण हूँ तनिक ठहर तो जा" ऐसा कहकर यह कृष्णके सारे चरित्रोंका ल्त्ेल्मपूर्वक अनुकरण करने लूगती
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9854)
- **Original**: कोई और गोपी कहने ऊंगतो--''अरे गोपगण ! मैंने गोवर्धन घारण कर लिया है, तुम बर्षासे मत डरो, निउ्ंक होकर इसके नीचे आकर बैठ जाओ”
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9855)
- **Original**: कोई दूसरी गोपी कृष्णलीलाओंका अनुकरण करती हुई बोलने लूगती--“मैंने घेनुकासुरक्त मार दिया है, अब यहाँ गौएँ. स्वच्चछप्द होकर खिचरें'”
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9856)
- **Original**: इस प्रकार समस्त गोपियाँ श्रीकृष्णचन्भधकी नाना प्रकारकी चेष्टाओंमें ज्यप्न होकर साथ-साथ अति सुरम्ब वुन्दावनके अन्दर विचरने छर्ीं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9857)
- **Original**: खिले हुए पुल्ककित हो पृथिवीक्ते ओर देखकर कहने लूगी--
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9858)
- **Original**: अरे आली ! ये लोलाललितगामो कृष्णचन्द्रके ध्वजा, वच्र, अंकुदा और कमल आदिकी रेखाओंसे सुशोभित पदचिह्न तो देखो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9859)
- **Original**: और देखो, उनके साथ कोई पुण्यबती मदमाती युवती भी आ गयी है, उसके ये घने छोटे-छोटे और पतले चरणचिह्न दिखायी दे रहे हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9860)
- **Original**: यहाँ निश्चय ही दामोदरने ऊँचे होकर पुष्पचयन किये हैं; इसी कारण यहाँ उन महात्माके चरणोंकि केबल अग्रभाग हो अज्लित्त हुए हैं
- **Translation**: 

---

