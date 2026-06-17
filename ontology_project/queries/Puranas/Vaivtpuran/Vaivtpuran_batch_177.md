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

### Verse 1 (Vaivtpuran 12.10026)
- **Original**: थे। त्रेतामें इनका वर्ण लाल हुआ और द्वापरमें सूतिकागारमें आकर अपना पुत्र तुम्हारे यहाँ रख
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.10027)
- **Original**: ये भगवान्‌ पीतवर्णके हो गये। कलियुगके दिया है और तुम्हारी कन्या वे मथुरा ले गये
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.10028)
- **Original**: आरम्भमें इनका वर्ण कृष्ण हो गया। ये श्रीमान्‌ हैं। ऐसा उन्होंने कंसके भयसे किया है। यह
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.10029)
- **Original**: तेजकी राशि हैं, परिपूर्णतम ब्रह्म हैं; इसलिये पुत्र वसुदेवका है और जो इससे ज्येष्ठ है, वह
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.10030)
- **Original**: “कृष्ण' कहे गये हैं। 'कृष्णः' पदमें जो 'ककार' भी उन्होंका है। यह निश्चित बात है। इस
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.10031)
- **Original**: है, वह ब्रह्माका वाचक है। 'ऋकार' अनन्त बालकका अन्नप्राशा और नामकरण-संस्कार
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.10032)
- **Original**: (शेषनाग)-का वाचक है। मूर्धन्य 'षकार' करनेके लिये वसुदेवने गुप्तरूपसे मुझे यहाँ भेजा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.10033)
- **Original**: शिवका और “णकार' धर्मका बोधक है। अन्तमें है। अत: तुम ब्रजमें इन बालकोंके संस्कारकी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.10034)
- **Original**: जो “अकार' है, बह श्वेतद्वीपनिवासी विष्णुका तैयारी करो। तुम्हारा यह शिशु पूर्ण ब्रह्मस्वरूप
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.10035)
- **Original**: बाचक है तथा विसर्ग नर-नारायण-अर्थका है और मायासे इस भूतलपर अवतीर्ण हो पृथ्वीका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.10036)
- **Original**: बोधक माना गया है। ये श्रीहरि उपर्युक्त सब भार उतारनेके लिये उद्यमशील है। ब्रह्माजीने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.10037)
- **Original**: देवताओंके तेजकी राशि हैं। सर्वस्वरूप, सर्वाधार इसकी आराधना की थी। अत: उनकी प्रार्थनासे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.10038)
- **Original**: तथा सर्वबीज हैं; इसलिये “कृष्ण” कहे गये हैं। यह भूतलका भार हरण करेगा। इस शिशुके रूपमें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.10039)
- **Original**: 'कृष्‌' शब्द निर्वाणका बाचक है, 'णकार' साक्षात्‌ राधिकावल्लभ गोलोकनाथ भगवान्‌ श्रीकृष्ण मोक्षका बोधक है और “अकार' का अर्थ दाता पधारे हैं। वैकुण्ठमें जो कमलाकान्त नारायण हैं है। ये श्रीहरि निर्वाण मोक्ष प्रदान करनेवाले हैं; तथा श्वेतद्वीपमें जो जगत्पालक विष्णु निवास
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.10040)
- **Original**: इसलिये 'कृष्ण' कहे गये हैं। 'कृष्‌' का अर्थ करते हैं, वे भी इन्हींमें अन्तर्भूत हैं। महर्षि कपिल
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.10041)
- **Original**: है निश्वेष्ट, 'ण' का अर्थ है भक्ति और 'अकार'का तथा इनके अन्यान्य अंश ऋषि नर-नारायण भी अर्थ है दाता। भगवान्‌ निष्कर्म भक्तिके दाता इनसे भिन्न नहीं हैं। ये सबके तेजोंकी राशि हैं।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.10042)
- **Original**: हैं; इसलिये उनका नाम “कृष्ण' है। 'कृष्‌' का
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.2926)
- **Original**: पतिरूपसे प्राप्त हुए? क्‍योंकि ये परम प्रभु तो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.2927)
- **Original**: वह नरेश उसमें सम्मिलित नहीं होता था। यज्ञ बिलकुल निः:स्पृह हैं। दूसरा प्रश्न यह है कि ऐसी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.2928)
- **Original**: और विष्णु-पूजाकी निन्‍दा करना उसका मानो सुयोग्या देवीको यृक्ष क्यों होना पड़ा और यह
- **Translation**: 

---

