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

### Verse 1 (Bramha 0.3801)
- **Original**: अन्तमें भगवान्‌ शंकरका स्मरण करके उन्हींको पत्लीरूपमें प्राप्त करके कई पुत्र उत्पन्न किये,
- **Translation**: 

---

### Verse 2 (Bramha 0.3802)
- **Original**: प्राप्त कर लेता है। नागतीर्थकी महिमा ख्रह्माजी कहते हैं--नागतीर्थक नामसे जो
- **Translation**: 

---

### Verse 3 (Bramha 0.3803)
- **Original**: सका। माता-पिताके सिवा धाय, अमात्य और प्रसिद्ध क्षेत्र है, वह सब अभीष्ट वस्तुओंको
- **Translation**: 

---

### Verse 4 (Bramha 0.3804)
- **Original**: पुरोहित भी यह बात नहीं जानते थे। उस भयंकर देनेवाला तथा मज्गलमय है। बहाँ भगवान्‌ नागेश्वर
- **Translation**: 

---

### Verse 5 (Bramha 0.3805)
- **Original**: सर्पको देखकर पत्नीसहित राजाको प्रतिदिन बड़ा निवास करते हैं। उनके माहात्म्यकी विस्तृत कथा
- **Translation**: 

---

### Verse 6 (Bramha 0.3806)
- **Original**: संताप होता था। वे सोचते, सर्परूप पुत्रकी अपेक्षा भी सुनो। प्रतिष्लानपुरमें चन्द्रवंशी राजा शूरसेन
- **Translation**: 

---

### Verse 7 (Bramha 0.3807)
- **Original**: तो पुत्रहीन रहना ही अच्छा है। वह था तो बहुत राज्य करते थे। वे समस्त गुणोंके सागर और
- **Translation**: 

---

### Verse 8 (Bramha 0.3808)
- **Original**: बड़ा सर्प, किंतु बातें मनुष्योंकी-सी करता था। युद्धिमान्‌ थे। उन्होंने अपनी पत्नीके साथ पुत्र
- **Translation**: 

---

### Verse 9 (Bramha 0.3809)
- **Original**: उसने पितासे कहा-- मेरे चूड़ाकरण, उपनयन उत्पन्न होनेके लिये बड़े-बड़े यलत किये। दीर्घकालके
- **Translation**: 

---

### Verse 10 (Bramha 0.3810)
- **Original**: तथा वेदाध्ययन-संस्कार कराइये। द्विज जबतक पश्चात्‌ उन्हें एक पुत्र हुआ, किन्तु वह भयानक
- **Translation**: 

---

### Verse 11 (Bramha 0.3811)
- **Original**: वेदका अध्ययन नहीं करता, तबतक शुद्रके समान आकारवाला सर्प था। राजाने उस पुत्रकों बहुत
- **Translation**: 

---

### Verse 12 (Bramha 0.3812)
- **Original**: रहता है।' छिपाकर रखा। किसीको इस बातका पता न लगा
- **Translation**: 

---

### Verse 13 (Bramha 0.3813)
- **Original**: पुत्रको यह बात सुनकर शूरसेन बहुत दुःखी कि राजाका पुत्र सर्प है। अन्तःपुर अथवा
- **Translation**: 

---

### Verse 14 (Bramha 0.3814)
- **Original**: हुए। उन्होंने किसी ब्राह्मणकों बुलाकर उसके बाहरका मनुष्य भी इस भेदसे परिचित न हो
- **Translation**: 

---

### Verse 15 (Bramha 0.3815)
- **Original**: संस्कार आदि कराये। वेदाध्ययत समाप्त करके
- **Translation**: 

---

### Verse 16 (Bramha 0.3816)
- **Original**: 188 * संक्षिप्त ब्रह्मपुराण * सर्पने अपने पितासे कहा-“नृपश्रैष्ट ! मेरा विवाह
- **Translation**: 

---

### Verse 17 (Bramha 0.3817)
- **Original**: लिये कैसे प्रात्त हो सकती है, बताओ।' कर दीजिये। मुझे स्त्री प्रात करनेकी इच्छा हो रहो
- **Translation**: 

---

### Verse 18 (Bramha 0.3818)
- **Original**: . बूढ़े अमात्यने कहा--' महाराज! आपके मनमें है। मेरा विश्वास है, ऐसा किये बिना आपका कोई
- **Translation**: 

---

### Verse 19 (Bramha 0.3819)
- **Original**: जो बात है, मैं उसे समझ गया। अब आप मुझे भी कार्य सिद्ध न हो सकेगा। पुत्रका यह निश्चय
- **Translation**: 

---

### Verse 20 (Bramha 0.3820)
- **Original**: कार्य-सिद्धिके लिये जानेकी आज्ञा दें।” महाराज जानकर राजाने अमात्योंको बुलाया और उसके
- **Translation**: 

---

