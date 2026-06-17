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

### Verse 1 (Bramha 0.2121)
- **Original**: जैसे स्वामीकी शरणमें आकर अब मुझे जीवन, पक्षी, मनुष्य तथा अन्य स्थावर-जद्जम भूतोंमें
- **Translation**: 

---

### Verse 2 (Bramha 0.2122)
- **Original**: मरण अथवा योगक्षेमके लिये कहीं भी भय नहीं ऐसा कोई स्थान नहीं है, जहाँ मेरा जाता न हुआ
- **Translation**: 

---

### Verse 3 (Bramha 0.2123)
- **Original**: होता। देव! जो नराधम आपकी विधिपूर्वक पूजा हो। जगत्पते! कभी नरकमें और कभी स्वर्गमें
- **Translation**: 

---

### Verse 4 (Bramha 0.2124)
- **Original**: नहीं करते, उनकी इस संसार-बन्धनसे मुक्ति एवं मेरा निवास रहा है। कभी मनुष्यलोकमें और
- **Translation**: 

---

### Verse 5 (Bramha 0.2125)
- **Original**: सद्गति कैसे हो सकती है। जगदाधार भगवान्‌ कभी तिर्यग्योनियोंमें जन्म लेना पड़ा है। सुरश्रेष्ठ!
- **Translation**: 

---

### Verse 6 (Bramha 0.2126)
- **Original**: केशवर्में जिनकी भक्ति नहीं होती, उनके कुल, जैसे रहटमें रस्सीसे बँधी हुई घंटी कभी ऊपर
- **Translation**: 

---

### Verse 7 (Bramha 0.2127)
- **Original**: शील, विद्या और जीवनसे क्‍या लाभ हैं। जो जाती, कभी नीचे आती और कभी बीचमें ठहरी
- **Translation**: 

---

### Verse 8 (Bramha 0.2128)
- **Original**: आसुरी प्रकृतिका आश्रय ले विवेकशून्य हो रहती है, उसी प्रकार मैं कर्मरूपी रज्जुमें बंधकर
- **Translation**: 

---

### Verse 9 (Bramha 0.2129)
- **Original**: आपकी निनन्‍्दा करते हैं, वे बारंबार जन्म लेकर दैवयोगसे ऊपरे, नीचे तथा मध्यवर्ती लोकमें
- **Translation**: 

---

### Verse 10 (Bramha 0.2130)
- **Original**: घोर नरकमें पड़ते हैं तथा उस नरक-समुद्रसे भटकता रहता हूँ। इस प्रकार यह संसार-चक्र
- **Translation**: 

---

### Verse 11 (Bramha 0.2131)
- **Original**: उनका कभी उद्धार नहीं होता। देव ! जो दुराचारी बड़ा ही भयानक एवं रोमाञ्ञकारी है। मैं इसमें
- **Translation**: 

---

### Verse 12 (Bramha 0.2132)
- **Original**: नीच पुरुष आपपर दोषारोपण करते हैं, वे कभी दीर्घकालसे घूम रहा हूँ, किंतु कभी इसका अन्त _ नरकसे छुटकारा नहीं पाते। हरे! अपने कर्मोमें नहीं दिखायी देता। समझमें नहीं आता, अब क्या
- **Translation**: 

---

### Verse 13 (Bramha 0.2133)
- **Original**: बँधे रहनेके कारण मेरा जहाँ कहीं भी जन्म हो, करूँ। हरे! हमारी सम्पूर्ण इन्द्रियाँ व्याकुल हो
- **Translation**: 

---

### Verse 14 (Bramha 0.2134)
- **Original**: वहाँ सर्वदा आपमें मेरी दृढ़ भक्ति बनी रहे। देव! गयी हैं। मैं शोक और तृष्णासे आक्रान्त होकर
- **Translation**: 

---

### Verse 15 (Bramha 0.2135)
- **Original**: आपकी आराधना करके देवता, दैत्य, मनुष्य तथा अब कहाँ जाऊँ। मेरी चेतना लुप्त हो रही है।
- **Translation**: 

---

### Verse 16 (Bramha 0.2136)
- **Original**: अन्य संयमी पुरुषोंने परम सिद्धि प्राप्त की.है; फिर असंतोषाक्ष संतोषा: संचयाप्चया व्यया: । मया प्राह्ठा जगन्नाथ श्षयवृद्धघुदयेतरा:
- **Translation**: 

---

### Verse 17 (Bramha 0.2137)
- **Original**: भायारिमित्रयन्धूनां. वियोगा: संगमास्तथा। पितरो विविधा दृष्टा मातरक्ष तथा मया
- **Translation**: 

---

### Verse 18 (Bramha 0.2138)
- **Original**: दुश्आनि चानुभूतानि यानि सौख्यान्यनेकश:। प्राप्ताश्ष बान्धवा: पुत्रा श्रातरों ज्ञातयस्तथा
- **Translation**: 

---

### Verse 19 (Bramha 0.2139)
- **Original**: मयोपित॑ तथा स्टत्रीणां कोष्टे विण्मूत्नपिच्छले। गर्भवासे महादुःखमनुभूत॑ तथा प्रभो
- **Translation**: 

---

### Verse 20 (Bramha 0.2140)
- **Original**: दुःखानि यान्यनेकानि बाल्ययौयनगोचरे। वार्थके चर हृपीकेश तानि प्राप्तानि वै मया
- **Translation**: 

---

