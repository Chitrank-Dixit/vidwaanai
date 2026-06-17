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

### Verse 1 (Markende Puran 0.2141)
- **Original**: । महामाया हरेशैषा तया संमोहाते जगत्‌। परम्परा) बनाये रखनेवालें भगवती महामायाके प्रधावद्वारा पमतामय भँवरसे युक्त मोहके गहरे गर्तमें गिराये जाते हैं। इसलिये इसमें आश्चर्य नहीं करना चाहिये। जगदीशर भगवान्‌ विष्णुका ओगनिद्वारूपा जो भगवती महापाया हैं, उन्हींसे ज्ञानिनामपि चेतांसि देवी भगवती हि सा
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2142)
- **Original**: यह जगत्‌ पोहित हो रहा है। वे भगवती महामाया 6, पा0-याश्र। 2. पा0-यान्ति। 3. पा0-किंनु ते। 4. पा0--नन्वेते
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2143)
- **Original**: 5. पा0--रिण;
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2144)
- **Original**: 6, गा0-चैततू ।
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2145)
- **Original**: श्8र +संक्षिमत सार्कण्डेयपुराण * ड€02276%53:%8 752:800 158 # 0247 00244 00 :23/470:37440 17670 02340 0577 05367 0 9464 0 908 0 0ज देवी ज्ञानियोके भी चित्तकों जलपूर्वक खींचकर ' विच्योध्नना्थाय.. हरेईरिनेत्रकृतालयाम। मोहमें डाल देतों हैं। चे ही इस सम्पूर्ण चशाचर
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2146)
- **Original**: चिश्लेश्वरों जगद्धात्री स्थितिसंहारकारिणीम्‌
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2147)
- **Original**: जगतूकी सृष्टि करती हैं तथा वे हो प्रस्तन्न होनेषर
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2148)
- **Original**: निद्रा भगवतों सिष्णोरतुलां तेजस: प्रभुः
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2149)
- **Original**: मनुष्योंकों मुक्तिके लिग्रे वरदान देती हैं। वे
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2150)
- **Original**: ऋषि बोले--
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2151)
- **Original**: राजत्‌! वास्तवमें तो ये ही परा विद्या, संसार-बन्धन और मोक्षकों' देवी नित्यस्वरूपा ही हैं। सप्पूर्ण जगत्‌ उन्होंका रूप हेतुभूता समान देवी तथा अम्पूर्ण ईश्वरॉकी भी
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2152)
- **Original**: है तथा उन्होंने समा विश व्याप्त कर डा है, अधी श्वरी हैं
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2153)
- **Original**: «1--58
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2154)
- **Original**: तथापि उनका प्राकट्य प्रकारसे होता हैं। बह तजौकानच
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2155)
- **Original**: । मुझसे झुनो। यद्यपि वे नित्य और अजन्या हैं, तथापि पक्का हिफा दबे नरक मं भवान्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2156)
- **Original**: ये कैसाओस कार्य किक करनेके लिये पट ब्रबीति कथमुत्पन्ना सा कर्मास्याश्व किं द्विज। , उस्र समय उत्पन्न हुई । चत्मभावा चल स्रा देवी यल्वरूपा पदुझुबा
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2157)
- **Original**: कल्पके अन्त जब सम्पूर्ण जगत एकार्णबमें निमग्न तत्सव॑ श्रोत्तुमिच्छाप्रि त्यत्तो गहादिदां वर
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2158)
- **Original**: हो रहा था और सबके प्रभु भगवान्‌ विष्णु शेषनागकी राजाने पूछा--
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2159)
- **Original**: भगबन्‌! जिन्हें आप । शय्या त्रिछ्ाकर सोगनिद्राका आश्रय ले सो रहे थे, महामाया कहते हैं, त्रे देवी कौत हैं? ब्रह्मनू! । उस समय उनके कानोंकी पैलसे दो भयंकर असुर उनका आविर्भाव कैसे हुआ? तथा उनक्ने चरित्र
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2160)
- **Original**: उत्पन्न हुए, जो मधु और कैटभके नामसे विख्यात कौन-कौन हैं? ब्रह्मवेत्ताओंमें श्रेष्ठ महर्षे! उन। थे। वे दोनों ब्द्माजीका वथ करनेको तैयार हो गये। देवोका जैसा प्रभाव हो, जैसा स्वरूप हो और भगवान्‌ विष्णुके नाभिकमलमें बिगजमान प्रजापत्ति जिस प्रकार प्रादुर्भाव हुआ हो, वह सब में आपके मुखसे सुनना चाहता हूँ
- **Translation**: 

---

