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

### Verse 1 (Bramha 0.4541)
- **Original**: देवताओंके रूप एक-दूसरेसे भिन्न और पृथक्‌- आश्रमपर मुनिश्रेष्ठ अगस्त्यजी आये। शिष्योंसहित
- **Translation**: 

---

### Verse 2 (Bramha 0.4542)
- **Original**: पृथक्‌ हैं। सम्पूर्ण साकार रूपॉर्में पृथक्‌-पृथक्‌ मुनीश्चर आपस्तम्बने अगस्त्यजीका पूजन किया
- **Translation**: 

---

### Verse 3 (Bramha 0.4543)
- **Original**: थेद प्रमाण हैं। जो निराकार तत्त्व है, वह एक है। और इस प्रकार पूछा--' मुनिबर! तीनों देवताओंमें
- **Translation**: 

---

### Verse 4 (Bramha 0.4544)
- **Original**: वह उन तोनोंकी अपेक्षा उत्कृष्ट माना गया है। कौन पृज्य है? अनादि और अनन्त कौन है तथा. आपस्तम्ब बोले--इससे मैं किसी निर्णयपर बेदोंमें किसका यशोगान किया गया है? महामुने !
- **Translation**: 

---

### Verse 5 (Bramha 0.4545)
- **Original**: नहीं पहुँच सका। इसमें जो रहस्यकी बात हो, यही मेरा संशय है, इसे दूर करनेके लिये आप
- **Translation**: 

---

### Verse 6 (Bramha 0.4546)
- **Original**: उसे विचारकर बतलाइये। कुछ उपदेश करें।' अगस्त्यजीने कह्म--यद्यपि इन देवताओंमें परस्पर अगस्त्यजी बोले--धर्म, अर्थ, काम और
- **Translation**: 

---

### Verse 7 (Bramha 0.4547)
- **Original**: कोई भेद नहीं है तथापि सुखस्वरूप शिवसे हो मोक्षकी सिद्धिमें शब्द प्रमाण बतलावा जाता है।
- **Translation**: 

---

### Verse 8 (Bramha 0.4548)
- **Original**: सम्पूर्ण सिद्धियाँ प्राप्त होती हैं। मुने! पराभक्तिके उसमें भी वैदिक शब्द सबसे श्रेष्ठ प्रमाण है।। साथ भगवान्‌ शिवकी ही आराधना करो। वेदके द्वारा जिनका यशोगान होता है, वे परात्पर
- **Translation**: 

---

### Verse 9 (Bramha 0.4549)
- **Original**: दण्डकारण्यमें गौतमीके तटपर भगवान्‌ शिव पुरुष परमात्मा हैं। जो मृत्युके अधीन होता है, समस्त पापराशिका निवारण करते हैं। उसे अपर (क्षर पुरुष) जानना चाहिये और जो
- **Translation**: 

---

### Verse 10 (Bramha 0.4550)
- **Original**: . महर्षि अगस्त्यकी यह बात सुनकर आपस्तम्ब अपृत है, उसे पर (अक्षर पुरुष) कहते हैं।
- **Translation**: 

---

### Verse 11 (Bramha 0.4551)
- **Original**: मुनिको बड़ी प्रसन्नता हुई। उन्होंने गड्भामें जाकर अपृतके भी दो स्वरूप हैं-- मूर्त और अमूर्त। जो
- **Translation**: 

---

### Verse 12 (Bramha 0.4552)
- **Original**: स्नान किया और व्रतपालनका निवम लेकर भगवान्‌ अमूर्त (निराकार) है, उसे परब्रह्म जानना चाहिये
- **Translation**: 

---

### Verse 13 (Bramha 0.4553)
- **Original**: शंकरका स्तवन करना आरम्भ किया। और मूर्तको अपर ब्रह्म कहते हैं। गुणोंकी
- **Translation**: 

---

### Verse 14 (Bramha 0.4554)
- **Original**: आपस्तम्थ योले--जो काष्ठोंमें अग्नि, फूलोंमें व्यापकताके अनुसार मूर्तके भी तीन भेद हैं--ब्रह्मा,
- **Translation**: 

---

### Verse 15 (Bramha 0.4555)
- **Original**: सुगन्ध, बीजोंमें वृक्ष आदि, पत्थरोंमें सुवर्ण तथा विष्णु और शिब। ये एक होते हुए भी तीन
- **Translation**: 

---

### Verse 16 (Bramha 0.4556)
- **Original**: सम्पूर्ण भूतोंमें आत्मारूपसे छिपे रहते हैं, उत कहलाते हैं। इन तीनों देवताओंका भी वेद्यतत््व भगवान्‌ सोमनाथकी मैं शरण लेता हूँ। जिन्होंने ““जललगल्क्‍्कजफल कूद
- **Translation**: 

---

### Verse 17 (Bramha 0.4557)
- **Original**: जल का पल ज न छल कपए क्‍न्‍उ तन्न यो भेदमाचष्ट लिड्डभेदी स उच्यते । प्रायश्चित्त न तस्यास्ति यश्चैषां व्याहरेद्‌ भिदाम्‌
- **Translation**: 

---

### Verse 18 (Bramha 0.4558)
- **Original**: (130। 11-13)
- **Translation**: 

---

### Verse 19 (Bramha 0.4559)
- **Original**: 222 * संक्षिप्त ब्रक्मपुराण * खेल-खेलमें ही इस विश्वकी रचना की, जो तीनों
- **Translation**: 

---

### Verse 20 (Bramha 0.4560)
- **Original**: प्रसन्न होकर कहा--'मुने! कोई थर माँगो।' लोकोंके भरण-पोषण करेवाले तथा उसके रचयिता
- **Translation**: 

---

