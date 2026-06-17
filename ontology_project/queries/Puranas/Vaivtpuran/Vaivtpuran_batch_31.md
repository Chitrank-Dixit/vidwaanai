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

### Verse 1 (Vaivtpuran 4.8516)
- **Original**: तुमपर प्रसन्न रहें। श्रीकृष्णमें तथा कल्याणदाता
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8517)
- **Original**: देवता, राजा अथवा बन्धु-बान्धव क्रुद्ध हो गये गुरुदेव शिवमें तुम्हारी सुदृढ़ भक्ति बनी रहे;
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8518)
- **Original**: हों, उसके लिये ये सभी इस स्तोत्रराजकी कृपासे क्योंकि जिसकी इष्टदेव तथा गुरुमें शाश्वती भक्ति
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8519)
- **Original**: प्रसन्न होकर वरदाता हो जाते हैं। जिसे चोर- होती है, उसपर यदि सभी देवता कुपित हो जाये
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8520)
- **Original**: डाकुओंने घेर लिया हो, साँपने डस लिया हो, तो भी उसे मार नहीं सकते। तुम तो श्रीकृष्णके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8521)
- **Original**: जो भयानक शक्रुके चंगुलमें फँैस गया हो अथवा भक्त और शंकरके शिष्य हो तथा मुझ गुरुपत्नीकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8522)
- **Original**: व्याधिग्रस्त हो;-वह इस स्तोत्रके स्मरणमात्रसे मुक्त स्तुति कर रहे हो; इसलिये किसकी शक्ति है जो
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8523)
- **Original**: हो जाता है। राजद्वारपर, श्मशानमें, कारागारमें तुम्हें मार सके। अहो! जो अन्यान्य देवताओंके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8524)
- **Original**: और बन्धनमें पड़ा हुआ तथा अगाध जलराशिमें भक्त हैं अथवा उनकी भक्ति न करके निरंकुश
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8525)
- **Original**: डूबता हुआ मनुष्य इस स्तोत्रके प्रभावसे मुक्त ही हैं, परंतु श्रीकृष्णके भक्त हैं तो उनका कहीं
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8526)
- **Original**: हो जाता है। स्वामिभेद, पुत्रभेद तथा भयंकर भी अमड्भल नहीं होता। भार्गव! भला, जिन
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8527)
- **Original**: मित्रभेदके अवसरपर इस स्तोत्रके स्मरणमात्रसे भाग्यवानोंपर बलवान चन्द्रमा प्रसन्न हैं तो दुर्बल
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8528)
- **Original**: निश्चय ही अभीष्टार्थकी प्राप्ति होती है। जो स्त्री तारागण रुष्ट होकर उनका कया बिगाड़ सकते हैं।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8529)
- **Original**: वर्षपर्यन्त भक्तिपूर्वक दुर्गाका भलीभाँति पूजन सभामें महान्‌ आत्मबलसे सम्पन्न सुखी नरेश
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8530)
- **Original**: करके हविष्यान्न खाकर इस स्तोत्रराजको सुनती जिसपर संतुष्ट है, उसका दुर्बल भृत्यवर्ग कुपित
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8531)
- **Original**: है, वह महावन्ध्या हो तो भी प्रसववाली हो होकर क्‍या कर लेगा? यों कहकर पार्वती हर्षित
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8532)
- **Original**: जाती है। उसे ज्ञानी एवं चिरजीवी दिव्य पुत्र हो परशुरामकों शुभाशौर्वांद देकर अन्तःपुरमें चली
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8533)
- **Original**: प्राप्त होता है। छ: महीनेतक इसका श्रवण करनेसे गयीं। तब तुरंत हरि-नामका घोष गूँज उठा।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8534)
- **Original**: दुर्भगा सौभाग्यवती हो जाती है। जो काकवन्ध्या जो मनुष्य इस काण्वशाखोक्त स्तोत्रका
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8535)
- **Original**: और मृतवत्सा नारी भक्तिपूर्वक नौ मासतक इस पूजाके समय, यात्राके अवसरपर अथवा
- **Translation**: 

---

