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

### Verse 1 (Nard Puran 0.801)
- **Original**: “विस्कभिते विस्कभिते' आदि स्थलोंमें 'तिरोविराम ' उपलक्षण मानना चाहिये)। है। 'हि इन्द्र गिर्वण: '*' हीन्द्र0 ' इत्यादिमें ' प्रश्लिष्ट जात्य, क्षैप्र, अभिनिहित, तैरव्यज्जन, तिरोविराम,
- **Translation**: 

---

### Verse 2 (Nard Puran 0.802)
- **Original**: सवार है। 'क ईम्‌ कईं बेद' इत्यादिमें “पादवृत्त' प्रश्लिष्ट तथा सातवाँ पादवृत्त-ये सात सवार हैं।
- **Translation**: 

---

### Verse 3 (Nard Puran 0.803)
- **Original**: नामक सवार है। इस प्रकार ये सब सात सवार हैं। अब मैं इन सब स्वारोंका पृथकू-पृथक्‌ लक्षण
- **Translation**: 

---

### Verse 4 (Nard Puran 0.804)
- **Original**: जात्य स्वरोंकों छोड़कर एक पूर्व॑वर्ती उदात्त बतलाता हूँ। लक्षण कहकर उन सबके यथायोग्य
- **Translation**: 

---

### Verse 5 (Nard Puran 0.805)
- **Original**: अक्षरसे परे जो भी अक्षर हो, उसकी स्वरित संज्ञा उदाहरण भी बताऊँगा। जो अक्षर 'य' कार और
- **Translation**: 

---

### Verse 6 (Nard Puran 0.806)
- **Original**: होती है। यह स्वरितिका सामान्य लक्षण बताया 'ब' कारके साथ स्वरित होता है तथा जिसके
- **Translation**: 

---

### Verse 7 (Nard Puran 0.807)
- **Original**: जाता है। पूर्वोक्त चार सवार उदात्त अथवा एक आगे उदात्त नहीं होता, वह “जात्य' सवार कहलाता
- **Translation**: 

---

### Verse 8 (Nard Puran 0.808)
- **Original**: अनुदात्त परे रहनेपर शास्त्रत: “कम्प' उत्पन्न करते है। जब उदात्त 'इ' वर्ण और “उ' वर्ण कहों
- **Translation**: 

---

### Verse 9 (Nard Puran 0.809)
- **Original**: हैं। (जिसका स्वरूप चल हो, उस स्वारका नाम पदादि अनुदात्त अकार परे रहते सन्धि होनेपर 'य'
- **Translation**: 

---

### Verse 10 (Nard Puran 0.810)
- **Original**: कम्प है) इसका उदाहरण है 'जुड्डग्मि:।' 'उप 'व' के रूपमें परिणत हो स्वरित होते हैं, तो वहाँ
- **Translation**: 

---

### Verse 11 (Nard Puran 0.811)
- **Original**: त्वा जुहू', “उप त्वा जुद्ढों मम' इत्यादि। सदा “क्षैप्र' स्वारका लक्षण समझना चाहिये। 'ए'
- **Translation**: 

---

### Verse 12 (Nard Puran 0.812)
- **Original**: पूर्वपद 'इ'कारान्त हो और परे “उ'कारकी और 'ओ' इन दो उदात्त स्वरोंसे परे जो वकारसहित
- **Translation**: 

---

### Verse 13 (Nard Puran 0.813)
- **Original**: स्थिति हो तो मेधावी पुरुष बहाँ 'हस्व कम्प' अकार निहित (अनुदात्तरूपमें निपातित) हो और
- **Translation**: 

---

### Verse 14 (Nard Puran 0.814)
- **Original**: जाने--इसमें संशय नहीं है । यदि 'उ 'कारद्वययुक्त उसका जहाँ लोप ('ए'कार या 'उ'कार में अनुप्रवेश)
- **Translation**: 

---

### Verse 15 (Nard Puran 0.815)
- **Original**: पद परे हो तो इकारान्त पदमें दीर्घ कम्प होता है, उसे 'अभिनिहित' सवार माना जाता है।
- **Translation**: 

---

### Verse 16 (Nard Puran 0.816)
- **Original**: जानना चाहिये। इसका दृष्टान्त है--' शबग्ध्यूषू छन्दमें जहाँ कहों या जो कोई भी ऐसा स्वरित
- **Translation**: 

---

### Verse 17 (Nard Puran 0.817)
- **Original**: इत्यादि। तीन दीर्घ कम्प जानने चाहिये, जो होता है, जिसके पूर्वमें उदात्त हो, तो वह सर्व
- **Translation**: 

---

### Verse 18 (Nard Puran 0.818)
- **Original**: संध्यक्षरोंमें होते हैं। उनके क्रमश: उदाहरण ये बहुस्वार-( सर्वत्र बहुलतासे होनेबाला स्वर)
- **Translation**: 

---

### Verse 19 (Nard Puran 0.819)
- **Original**: हैं--मन्या। पथ्या। न इन्द्राभ्याम्‌। शेष हस्व कहे 'तैरव्यज्षन' कहलाता है। मदि उदात्त अवग्रह हो
- **Translation**: 

---

### Verse 20 (Nard Puran 0.820)
- **Original**: गये हैं। जब अनेक उदात्तोंक बाद कोई अनुदात्त और अवग्रहसे परे अनन्तर स्वरित हो तो उसे
- **Translation**: 

---

