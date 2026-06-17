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

### Verse 1 (Vaivtpuran 67.6095)
- **Original**: किया गया है कि मैं आत्मा हूँ, ब्रह्मा मन हैं, द्वारा सब जान लेनेपर कहना आरम्भ किया।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.6096)
- **Original**: महेश्वर ज्ञानरूप हैं, स्वयं विष्णु पद्मप्राण हैं, श्रीनारायण बोले--सुरगणो! मेंरे सिवा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.6097)
- **Original**: ऐश्वर्यशालिनी प्रकृति बुद्धि है, मेधा, निद्रा आदि ब्रह्मासे लेकर तृणपर्यन्त यह सारा जगत्‌ प्रकृतिसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.6098)
- **Original**: ये सभी प्रकृतिकी कलाएँ हैं और वह प्रकृति उत्पन्न हुआ है-यह सर्वथा सत्य है। विश्वमें सारे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.6099)
- **Original**: ही ये शैलराजकन्या पार्वती हैं। मैं सनातनदेव ही प्राणी जिस शक्तिसे शक्तिमान्‌ हुए हैं, उस
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.6100)
- **Original**: बैकुण्ठका अधिपति हूँ और मैं ही गोलोकका भी शक्तिको मैंने ही प्रकाशित किया है। सृष्टिके स्वामी हूँ। वहाँ गोलोकमें मैं दो भुजाधारी होकर आदिमें मेरी इच्छासे वह प्रकृतिदेवी मुझसे ही
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.6101)
- **Original**: गोप और गोपियोंसे घिरा रहता हूँ तथा यहाँ प्रकट हुई हैं और मेरे सृष्टिका संहार कर लेनेपर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.6102)
- **Original**: वैकुण्ठमें मैं देवेश्वर और लक्ष्मीपतिके रूपमें चार वह अन्तहिंत होकर शयन करती हैं। प्रकृति ही
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.6103)
- **Original**: भुजाएँ धारण करता हूँ और मेरे पार्षद मुझे घेरे सृष्टिकी विधायिका और समस्त प्राणियोंकी परा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.6104)
- **Original**: रहते हैं। वैकुण्ठसे ऊपर पचास करोड़ योजनकी जननी है। वह मेरी माया मेरे समान है, इसी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.6105)
- **Original**: दूरीपर स्थित गोलोकमें मेरा निवास-स्थान है, कारण नारायणी कहलाती है। शम्भुने चिरकालतक
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.6106)
- **Original**: वहाँ मैं “गोपीनाथ” रूपसे रहता हूँ। उन्हीं मेरा ध्यान करते हुए तपस्या कौ है, इसलिये
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.6107)
- **Original**: द्विभुजधारी गोपीनाथकी त्रतद्वारा आराधना को
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.6108)
- **Original**: +* गणपतिखण्ड « 307 अऋकककऋककऋकऋ कक #####
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.6109)
- **Original**: कक ऋकऋकककऊकऊऋऊ$ऊऋ$ कक कक # 6 #########%#$$$%%%%%$%%$%%%########## जाती है और वे ही उसका फल प्रदान करते
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.6110)
- **Original**: कहीं दूसरेकी इच्छासे होता है ? मैं इन दिगम्बरको हैं। जो जिस रूपसे उनका ध्यान करता है, उसे आगे करके तीनों लोकोंमें भ्रमण करूँगा। उस उसी रूपसे उसका फल देते हैं। अतः: शिवे! समय ये बालक-बालिकाओंके समुदायके लिये तुम शिवको दक्षिणारूपमें देकर अपना ब्रत पूर्ण
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.6111)
- **Original**: हँसीके कारण होंगे। करो। फिर समुचित मूल्य देकर अपने स्वामीको
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.6112)
- **Original**: .. मुने! उस देवसभामें यों कहकर ब्रह्माके वापस कर लेना। शुभे! जैसे गौएँ विष्णुकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.6113)
- **Original**: पुत्र तेजस्वी सनत्कुमारने शंकरजीको अपने देहस्वरूपा हैं, उसी प्रकार शिव भी विष्णुके शरीर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.6114)
- **Original**: संनिकट बैठा लिया। इस प्रकार कुमारद्वारा हैं; अत: तुम ब्राह्मणकों गोमूल्य प्रदान करके
- **Translation**: 

---

