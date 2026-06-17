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

### Verse 1 (Bramha 0.8421)
- **Original**: भूत निवास करते हैं तथा बे भी सर्वात्मारूपसे शास्त्र-जन्य ज्ञान शब्दब्रह्मकमा और विवेक-जन्य
- **Translation**: 

---

### Verse 2 (Bramha 0.8422)
- **Original**: सब भूतोंमें स्थित हैं। अत: वे “बासुदेव' कहे ज्ञान परब्रह्मका स्वरूप है। अज्ञान गाढ अन्धकारके
- **Translation**: 

---

### Verse 3 (Bramha 0.8423)
- **Original**: गये हैं। पूर्वकालमें महर्षियोंके पूछनेपर स्वयं समान“है। उसको नष्ट करनेके लिये शास्त्र-जन्य
- **Translation**: 

---

### Verse 4 (Bramha 0.8424)
- **Original**: प्रजापति ब्रह्माने अनन्त भगवान्‌ वासुदेवके ज्ञान दीपकके समान और विवेक-जन्य ज्ञान
- **Translation**: 

---

### Verse 5 (Bramha 0.8425)
- **Original**: नामकी यह यथार्थ व्याख्या बतलायी थी। साक्षात्‌ सूर्यके सदृश माना गया है। सम्पूर्ण जगत्‌के धाता और विधाता भगवान्‌ मुनिवरो! मनुजीने वेदार्थका स्मरण करके
- **Translation**: 

---

### Verse 6 (Bramha 0.8426)
- **Original**: श्रीहरि सम्पूर्ण भूतोंमें वास करते हैं और इसके विषयमें जो विचार प्रकट किया है, उसे
- **Translation**: 

---

### Verse 7 (Bramha 0.8427)
- **Original**: सम्पूर्ण भूत उनमें वास करते हैं; इसलिये बताता हूँ; सुनो। ब्रह्मके दो स्वरूप जानने योग्य
- **Translation**: 

---

### Verse 8 (Bramha 0.8428)
- **Original**: उनका नाम 'वासुदेव' है। वे परमात्मा निर्गुण, हैं--शब्दब्रह्म और परब्रह्म
- **Translation**: 

---

### Verse 9 (Bramha 0.8429)
- **Original**: जो शब्दब्रह्ममें पारंगत
- **Translation**: 

---

### Verse 10 (Bramha 0.8430)
- **Original**: समस्त आवरणोंसे परे और सबके आत्मा हैं। है, बह परन्रह्मकों प्राप्त कर लेता है। अथर्ववेदकी
- **Translation**: 

---

### Verse 11 (Bramha 0.8431)
- **Original**: सम्पूर्ण धूतोंकी, प्रकृति तथा उसके गुण और श्रुति कहती है कि परा और अपरा-ये दो
- **Translation**: 

---

### Verse 12 (Bramha 0.8432)
- **Original**: दोषोंकी पहुँचके बाहर हैं। सम्पूर्ण भुवनोंके विद्याएँ जानने योग्य हैं। परा विद्यासे अक्षरब्रह्मकी
- **Translation**: 

---

### Verse 13 (Bramha 0.8433)
- **Original**: बीचमें जो कुछ भी स्थित है, बह सब उनके प्राप्ति होती है तथा ऋग्वेदादि शास्त्र ही अपरा
- **Translation**: 

---

### Verse 14 (Bramha 0.8434)
- **Original**: द्वारा व्याप्त है। समस्त कल्याणमय गुण उनके विद्या हैं। वह जो अव्यक्त, जरावस्थासे रहित,
- **Translation**: 

---

### Verse 15 (Bramha 0.8435)
- **Original**: स्वरूप हैं। उन्होंने अपनी मायाशक्तिके लेशमात्रसे अचिन्त्य, अजन्मां, अविनाशी, अनिर्देश्य, अरूप,
- **Translation**: 

---

### Verse 16 (Bramha 0.8436)
- **Original**: सम्पूर्ण प्राणियोंकी सृष्टि की है। वे अपनी हस्त-पादादिसे रहित, सर्वव्यापक, नित्य, सब
- **Translation**: 

---

### Verse 17 (Bramha 0.8437)
- **Original**: इच्छासे मनके अनुरूप अनेक शरीर धारण भूतोंका कारण तथा स्वयं कारणरहित है, जिससे
- **Translation**: 

---

### Verse 18 (Bramha 0.8438)
- **Original**: करते हैं तथा उन्हींके द्वारा सम्पूर्ण जगत्‌के सम्पूर्ण व्याप्य वस्तु व्याप्त है, जिसे ज्ञानी पुरुष
- **Translation**: 

---

### Verse 19 (Bramha 0.8439)
- **Original**: कल्याणका साधन होता है। वे तेज, बल और ही ज्ञानदृष्टिसे देखते हैं, वही परब्रह्म और वही
- **Translation**: 

---

### Verse 20 (Bramha 0.8440)
- **Original**: ऐश्वर्यक महान्‌ भंडार हैं। पराक्रम और शक्ति परमधाम है। मोक्षकी अभिलाषा रखनेवाले
- **Translation**: 

---

