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

### Verse 1 (Bramha 0.4201)
- **Original**: और जहाँ सीताने स्नानादि किया, वह सीतातीर्थके यहाँ पिण्ड आदि देनेसे पवित्र हो स्वर्गलोकमें
- **Translation**: 

---

### Verse 2 (Bramha 0.4202)
- **Original**: नामसे कहलाया। सीतातोर्थ नाना प्रकारकी समस्त चले जायेँ। जन्मभरके कमाये हुए मानसिक,
- **Translation**: 

---

### Verse 3 (Bramha 0.4203)
- **Original**: पापराशिको निर्मूल करनेमें समर्थ है। जिसके वाचिक और शारीरिक पाप यहाँ स्नान करनेमात्रसे
- **Translation**: 

---

### Verse 4 (Bramha 0.4204)
- **Original**: चरणोंसे त्रिभुवनपावनी गड्जा प्रकट हुईं, उन्होंने ही तत्काल नष्ट हो जायँँ। जो लोग यहाँ याचकोंको
- **Translation**: 

---

### Verse 5 (Bramha 0.4205)
- **Original**: जहाँ स्नान किया, उस तीर्थकी विशिष्टताके विषयमें भक्तिपूर्वक थोड़ा भी दान दें, बह सब अक्षय
- **Translation**: 

---

### Verse 6 (Bramha 0.4206)
- **Original**: क्‍या कहा जा सकता है। अत: श्रीरामतीर्थके समान होकर दाताओंके लिये उत्तम फल देनेवाला हो।
- **Translation**: 

---

### Verse 7 (Bramha 0.4207)
- **Original**: कहीं कोई भी तीर्थ नहीं है। + >> दय4272>+ पुत्रतीर्थकी महिमा ब्रह्माजी कहते हैं--गौतमी-तटपर जो विख्यात
- **Translation**: 

---

### Verse 8 (Bramha 0.4208)
- **Original**: लक्ष्मीसे सुशोभित है। अदितिकी संतानोंका वैभव पुत्रतीर्थ है, वह पुण्यतीर्थ कहलाता है। उसकी
- **Translation**: 

---

### Verse 9 (Bramha 0.4209)
- **Original**: और अभ्युदय देखकर मैं दुबली होती जा रही हूँ। महिमाके श्रवणमात्रसे मनुष्य सम्पूर्ण अभिलषित
- **Translation**: 

---

### Verse 10 (Bramha 0.4210)
- **Original**: सम्भव है, जीवित न रह सकूँ। अदितिके महान्‌ बस्तुओंको प्राप्त कर लेता है। नारद! मैं उसके
- **Translation**: 

---

### Verse 11 (Bramha 0.4211)
- **Original**: ऐश्वर्यपर दृष्टि डालते ही मैं अवर्णनीय दुरवस्थाका स्वरूपका वर्णन करता हूँ, सावधान होकर सुनो।
- **Translation**: 

---

### Verse 12 (Bramha 0.4212)
- **Original**: अनुभव करने लगती हूँ। दावानलमें प्रवेश कर जब दिति एवं दनुके पुत्र दैत्य और दानवोंका
- **Translation**: 

---

### Verse 13 (Bramha 0.4213)
- **Original**: जाना भी सुखद है, किंतु स्वप्रमें भी सौतकी देवताओंद्वारा क्षय होने लगा, तब दिति पुत्र-
- **Translation**: 

---

### Verse 14 (Bramha 0.4214)
- **Original**: समृद्धि नहीं देखी जाती। वियोगके दुःखसे मनमें स्पर्धा लेकर अपनी बहन
- **Translation**: 

---

### Verse 15 (Bramha 0.4215)
- **Original**: दनु बोली--भद्ने! तुम अपने गुणोंसे पतिदेव दनुके पास आयी और इस प्रकार कहने लगी--' भट्रे!
- **Translation**: 

---

### Verse 16 (Bramha 0.4216)
- **Original**: कश्यपजीको संतुष्ट करो। यदि स्वामी संतुष्ट हो गये हम दोनोंके ही पुत्र क्षीण होते जा रहे हैं। हम ट तुम सम्पूर्ण अभीष्ट बस्तुओंको प्राप्त कर लोगी। संसारमें कौन ऐसा गुरुतर कार्य करें, जिससे
- **Translation**: 

---

### Verse 17 (Bramha 0.4217)
- **Original**: “बहुत अच्छा” कहकर दितिने सब्र प्रकारसे हमारा यह संकट दूर हो। देखो, अदितिका बंश , कश्यपजीको संतुष्ट किया। तब प्रजापति भगवान्‌ कितना संगठित और उत्तम है। उसका कभी क्षय
- **Translation**: 

---

### Verse 18 (Bramha 0.4218)
- **Original**: कश्यपने दितिसे कहा-'सुब्रते ! तुम्हें क्या दूँ? तुम नहीं होता। वह उत्तम राज्य, सुयश और विजय-
- **Translation**: 

---

### Verse 19 (Bramha 0.4219)
- **Original**: कोई अभीष्ट वर माँगो।' यह सुनकर दितिने
- **Translation**: 

---

### Verse 20 (Bramha 0.4220)
- **Original**: « पुत्रतीर्थकी महिमा * 207 07-72 स्‍-- 27535 बल +>>>>> 00 «8323 >>- 92270 ++2000 हब 22025-लनननन654:0000000:5200: 4-7 ऋ॑:णए-: >> ऋऋऋऋऋऋ*॑ऋ
- **Translation**: 

---

