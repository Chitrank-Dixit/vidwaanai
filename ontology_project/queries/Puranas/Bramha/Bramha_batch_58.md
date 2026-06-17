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

### Verse 1 (Bramha 0.1141)
- **Original**: तथा अश्वमेध-यज्ञॉका फल पाते और परम नमस्कार, स्तोत्र, गीत और मनोहर वाह्योद्वारा
- **Translation**: 

---

### Verse 2 (Bramha 0.1142)
- **Original**: सिद्धिको प्राप्त होते हैं। हा ्आ भगवान्‌ सूर्यकी महिमा मुनियोंने कहा--सुरश्रेष्ट! आपने भोग और
- **Translation**: 

---

### Verse 3 (Bramha 0.1143)
- **Original**: समाधि, स्तुति और मनसे जो नियम किया जाता मोक्ष प्रदान करनेवाले भगवान्‌ भास्करके उत्तम
- **Translation**: 

---

### Verse 4 (Bramha 0.1144)
- **Original**: और जो ब्राह्मणको दान दिया जाता है, उसे क्षेत्रका जो वर्णन किया है, वह सब हम लोगोंने
- **Translation**: 

---

### Verse 5 (Bramha 0.1145)
- **Original**: देवता, मनुष्य और पितर--सभी ग्रहण करते हैं। सुना। अब यह यताइये कि उनकी भक्ति कैसे की
- **Translation**: 

---

### Verse 6 (Bramha 0.1146)
- **Original**: पत्र, पुष्प, फल और जल--जो कुछ भी भक्तिपूर्वक जाती है और बे किस प्रकार प्रसन्न होते हैं? इस
- **Translation**: 

---

### Verse 7 (Bramha 0.1147)
- **Original**: अर्पण किया जाता है, उसे देवता ग्रहण करते हैं; समय यही सब सुननेकी हमारी इच्छा है। परंतु वे नास्तिकोंकी दी हुईं वस्तु नहीं स्वीकार भ्रह्माजी बोले--मनके द्वारा इष्टदेवके प्रति जो
- **Translation**: 

---

### Verse 8 (Bramha 0.1148)
- **Original**: करते। नियम और आचारके साथ भावशुद्धिका भावना होतो है, उसे ही भक्ति और श्रद्धा कहते
- **Translation**: 

---

### Verse 9 (Bramha 0.1149)
- **Original**: भी उपयोग करना चाहिये। हृदयके भावको शुद्ध हैं। जो इष्टदेवकी कथा सुनता, उनके भक्तोंकी ! रखते हुए जो कुछ किया जाता है, वह सब पूजा करता तथा अग्रिकी उपासनामें संलग्र रहता
- **Translation**: 

---

### Verse 10 (Bramha 0.1150)
- **Original**: सफल होता है। भगवान्‌ सूर्यके स्तवन, जप, है, वह सनातन भक्त हैं। जो इष्टदेवका चिन्तन
- **Translation**: 

---

### Verse 11 (Bramha 0.1151)
- **Original**: उपहार-समर्पण, पूजन, उपबास (व्रत) और करता, उन्हींमें मन लगाता, उन्हींकी पूजामें रत ' भजनसे मनुष्य सब पापोंसे मुक्त हो जाता है। जो रहता तथा उन्हींके लिये कर्म करता है, वह
- **Translation**: 

---

### Verse 12 (Bramha 0.1152)
- **Original**: पृथ्वीपर मस्तक रखकर भगवान्‌ सूर्यको नमस्कार निश्चय ही सनातन भक्त है। जो इशष्टदेवके लिये
- **Translation**: 

---

### Verse 13 (Bramha 0.1153)
- **Original**: करता है, वह तत्काल सब पापोंसे छूट जाता है, किये जानेवाले कर्मोका अनुमोदन करता, उनके
- **Translation**: 

---

### Verse 14 (Bramha 0.1154)
- **Original**: इसमें तनिक भी संदेह नहीं है। जो मनुष्य भक्तोंमें दोष नहीं देखता, अन्य देवताकी निन्‍्दा
- **Translation**: 

---

### Verse 15 (Bramha 0.1155)
- **Original**: भक्तिपूर्वक सूर्यदेवकी प्रदक्षिणा करता है, उसके नहीँ करता, सूर्यके व्रत रखता तथा चलते, फिरते,
- **Translation**: 

---

### Verse 16 (Bramha 0.1156)
- **Original**: द्वारा सातों द्वीपोंसहित पृथ्वीकी परिक्रमा हो जाती ठहरते, सोते, सूँघते और आँख खोलते-मीचते
- **Translation**: 

---

### Verse 17 (Bramha 0.1157)
- **Original**: है। जो सूर्यदेवको अपने हृदयमें धारण करके समय भगवान्‌ भास्करका स्मरण करता है, वह
- **Translation**: 

---

### Verse 18 (Bramha 0.1158)
- **Original**: केवल आकाशकी प्रदक्षिणा करता है, उसके द्वारा मनुष्य अधिक भक्त माना गया है। विज्ञ पुरुषको
- **Translation**: 

---

### Verse 19 (Bramha 0.1159)
- **Original**: निश्चय ही सम्पूर्ण देवताओंकी परिक्रमा हो जाती सदा ऐसी ही भक्ति करनी चाहिये। भक्ति,
- **Translation**: 

---

### Verse 20 (Bramha 0.1160)
- **Original**: है।* जो षष्ठी या सप्तमीकों एक समय भोजत * भावशुद्धि: प्रयोक्तत्या नियमाचारसंयुता । भावशुद्धथ्ा क्रियते यत्तत्सव॑ सफल भवेत्‌
- **Translation**: 

---

