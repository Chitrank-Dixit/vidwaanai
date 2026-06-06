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

### Verse 1 (Bramha 0.8721)
- **Original**: भागी होकर देवलोकमें जाते हैं। केवल पापसे किया। अक्षरतत््व पच्चोसवाँ तत्त्व है। वह नित्य
- **Translation**: 

---

### Verse 2 (Bramha 0.8722)
- **Original**: (पापकी प्रधानतासे) पशु-पक्षियोंको योनिमें एवं निराकार है। उसको प्राप्त कर लेनेपर इस
- **Translation**: 

---

### Verse 3 (Bramha 0.8723)
- **Original**: जाना पड़ता है। पुण्य और पाप दोनोंका मेल संसारमें लौटना नहीं होता। जो अव्यक्ततत्त्व इस
- **Translation**: 

---

### Verse 4 (Bramha 0.8724)
- **Original**: होनेसे मनुष्यलोककी प्राप्ति होती है तथा केवल व्यक्त जगत्‌की सृष्टि करता है, वह प्रत्येक शरीरमें
- **Translation**: 

---

### Verse 5 (Bramha 0.8725)
- **Original**: पुण्यसे (पुण्यकी प्रधानतासे) जोव देवताका साक्षीरूपसे निवास करता है। चौब्रीस तत्त्वोंका ' स्वरूप प्राप्त करता है। अव्यक्त परमात्मामें जो समुदाय तो व्यक्त है, किंतु उनका साक्षी पच्चीसवाँ
- **Translation**: 

---

### Verse 6 (Bramha 0.8726)
- **Original**: स्थिति होती है, उसीको मनीषी पुरुष मोक्ष तत्त्व परमात्मा निराकार होनेके कारण अव्यक्त है।
- **Translation**: 

---

### Verse 7 (Bramha 0.8727)
- **Original**: कहते हैं। वे परमात्मा ही पत्चीसवाँ तत्त्व हैं। वही सम्पूर्ण देहधारियोंके हृदयमें निवास करता ज्ञानसे ही उनकी प्राप्ति होती है। #34/0 97000
- **Translation**: 

---

### Verse 8 (Bramha 0.8728)
- **Original**: 318 *+ सॉखिपत ख्रह्मपुणाण « क्षर-अक्षर तथा योग और सांख्यका वर्णन जनकने कहा--मुनिश्रेष्! क्षः और अक्षर
- **Translation**: 

---

### Verse 9 (Bramha 0.8729)
- **Original**: करते हैं, सांख्यके विद्वान्‌ भी उसीका ज्ञान प्राप्त (प्रकृति और पुरुष) दोनोंका सम्बन्ध तो पत्ली
- **Translation**: 

---

### Verse 10 (Bramha 0.8730)
- **Original**: करते हैं। जो सांख्य और योगकों एक समझता है, और पतिके सम्बन्धकी भाँति स्थिर जान पड़ता
- **Translation**: 

---

### Verse 11 (Bramha 0.8731)
- **Original**: यहो बुद्धिमान्‌ है। जैसे बीजसे यीजकी उत्पत्ति है। जैसे पुरुषके बिना स्त्री तथा स्त्रीके बिना पुरुष
- **Translation**: 

---

### Verse 12 (Bramha 0.8732)
- **Original**: होती है, उसी प्रकार द्रव्यसे द्रव्य, इन्द्रियसे इन्द्रिय संतान नहीं उत्पन्न कर सकते, उसी प्रकार प्रकृति
- **Translation**: 

---

### Verse 13 (Bramha 0.8733)
- **Original**: और देहसे देहकी प्राप्ति होती है। परंतु परमात्मा और पुरुष भी सदा एक-दूसरेसे संयुक्त होकर ही
- **Translation**: 

---

### Verse 14 (Bramha 0.8734)
- **Original**: तो इन्द्रिय, बीज, द्रव्य और देहसे रहित तथा सृष्टि करते हैं। ऐसी दशामें पुरुषका मोक्ष असम्भव
- **Translation**: 

---

### Verse 15 (Bramha 0.8735)
- **Original**: निर्गुण है; अतः उसमें गुण कैसे हो सकते हैं। जान पड़ता है। यदि मोक्षके निकट पहुँचनेवाला
- **Translation**: 

---

### Verse 16 (Bramha 0.8736)
- **Original**: जैसे आकाश आदि गुण सत्त्यादि गुणोंसे उत्पन्न (उसके स्वरूपका स्पष्ट बोध करानेवाला) कोई
- **Translation**: 

---

### Verse 17 (Bramha 0.8737)
- **Original**: होते और उन्हींमें लीन हो जाते हैं, उसी प्रकार दृष्टान्त हो तो बताइये; क्योंकि आपको सब कुछ सत्त्वादि गुण भी प्रकृतिसे उत्पन्न होकर उसीमें प्रत्यक्ष है। हमारे मनमें भी मोक्षकी अभिलाषा है।
- **Translation**: 

---

### Verse 18 (Bramha 0.8738)
- **Original**: लीन होते हैं। आत्मा तो जन्म-मृत्युसे रहित, हम भी उस पदको प्राप्त करना चाहते हैं, जो
- **Translation**: 

---

### Verse 19 (Bramha 0.8739)
- **Original**: अनन्त, सबका द्रष्टा एवं अद्वितोय है। बह अनामय, अजेय, युढ़ापेसे रहित, नित्य, इन्द्रियातीत
- **Translation**: 

---

### Verse 20 (Bramha 0.8740)
- **Original**: सत्त्वादि गुणोंमें केबल आत्माभिमान करनेके कारण एवं परम स्वतन्त्र है।
- **Translation**: 

---

