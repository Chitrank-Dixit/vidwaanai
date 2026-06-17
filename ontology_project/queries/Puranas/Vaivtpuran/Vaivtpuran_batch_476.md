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

### Verse 1 (Vaivtpuran 24.7089)
- **Original**: नारायण कहते हैं--नारद ! भूपालके वचनको मेरा अतिथि बना हुआ राजराजेश्वर कार्तवीर्य
- **Translation**: 

---

### Verse 2 (Vaivtpuran 24.7090)
- **Original**: सुनकर मुनिवरने श्रीहरिका स्मरण करके जो मूच्छित हो गया है, तब कृपापरवश हो उन्होंने
- **Translation**: 

---

### Verse 3 (Vaivtpuran 24.7091)
- **Original**: हितकर, सत्य और नीतिका साररूप था, ऐसा उस सेनाकों लौटा लिया। फिर तो वह कृत्रिम
- **Translation**: 

---

### Verse 4 (Vaivtpuran 24.7092)
- **Original**: बचन कहना आरम्भ किया। सेना जाकर कपिलाके शरीरमें विलीन हो गवी।। . मुनिने कहा--महाभाग! अपने घर जाओ तदनन्तर कृपालु मुनिने शीघ्र ही राजाकों अपनी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 24.7093)
- **Original**: और सनातनधर्मकी रक्षा करो; क्योंकि धर्मके चरण-धूलि देकर “तुम्हारी जय हो' ऐसा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 24.7094)
- **Original**: सुरक्षित रहनेपर सारी सम्पत्तियाँ सदा स्थिररूपसे शुभाशीर्बाद प्रदान किया और अपने कमण्डलुके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 24.7095)
- **Original**: निवास करती हैं-यह पूर्णतया निश्चित है। जलके छोटे देकर उसे चैतन्य कराया। होशमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 24.7096)
- **Original**: राजन्‌! तुम्हें भोजनसे वच्चित देखकर मैं अपने आनेपर वह राजा युद्धभूमिमें उठकर खड़ा हो
- **Translation**: 

---

### Verse 9 (Vaivtpuran 24.7097)
- **Original**: घर लाया और विधिपूर्वक यथाशक्ति तुम्हारा गया और भक्तिपूर्वक हाथ जोड़े हुए उसने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 24.7098)
- **Original**: आदर-सत्कार किया। इस समय तुम्हें मूर्च्छित मुनिवरको सिर झुकाकर प्रणाम किया। तब मुनिने
- **Translation**: 

---

### Verse 11 (Vaivtpuran 24.7099)
- **Original**: देखकर मैंने चरणधूलि और शुभाशीर्वाद दिया, राजाकों शुभाशीष देकर हृदयसे लगा लिया और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 24.7100)
- **Original**: जिससे तुम्हारी मूर्च्छा दूर हुई; अत: तुम्हारा ऐसा पुनः उसे स्नान कराकर यत्रपूर्वक भोजन कराया;
- **Translation**: 

---

### Verse 13 (Vaivtpuran 24.7101)
- **Original**: कहना उचित नहीं है। क्योंकि ब्राह्मणोंका हृदय सदा मकक्‍्खनके समान उस वचनकों सुनकर राजाने मुनिवरकों कोमल होता है; परंतु दूसरोंका हृदय सदा छुरेकी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 24.7102)
- **Original**: प्रणाम किया और एक-दूसरे रथपर सवार हो धारके सदुर्श तेज, असाध्य और दारुण होता है।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 24.7103)
- **Original**: युद्ध दीजिये'--ऐसे ललकारा। तब मुनि भी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 24.7104)
- **Original**: * गणपतिखण्ड « 345 44 4 4 4 8
- **Translation**: 

---

### Verse 17 (Vaivtpuran 24.7105)
- **Original**: 2 2 22 2 22002 04 22002 02 0000 0 0 0 00 /
- **Translation**: 

---

### Verse 18 (Vaivtpuran 24.7106)
- **Original**: ।0] 8 ]ै] कबच धारण करके उससे युद्ध करनेके लिये
- **Translation**: 

---

### Verse 19 (Vaivtpuran 24.7107)
- **Original**: मुहानेपर जृम्भणास्त्र छोड़ा। उस अस्त्रके प्रभावसे उद्यत हो गये। क्रोधके कारण राजाकी बुद्धि मारी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 24.7108)
- **Original**: राजाकों निद्राने आ घेरा और बह मृतक-तुल्य गयी थी; अत: वह मुनिके साथ जूझने लगा।
- **Translation**: 

---

