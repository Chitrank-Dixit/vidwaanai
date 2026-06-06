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

### Verse 1 (Vaivtpuran 13.11702)
- **Original**: ईश्वरको देखकर वह दानव शास्त्रके अनुसार उनके पास दौड़े आये और मन्द मुस्कानसे युक्त
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11703)
- **Original**: श्रुतिसे परे गुणातीत प्रभुका जिस प्रकार जन्म प्रसन्नमुखद्वारा उन्होंने उन बालकोंको अभय दान
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11704)
- **Original**: हुआ, उसे दृष्टिमें लाकर उनकी स्तुति करने लगा। दिया। श्रीकृष्ण और बलरामको देखकर बालक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11705)
- **Original**: दानव बोला--प्रभो! आप ही अपने हर्षसे नाचने लगे। उनका भय दूर हो गया। क्यों
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11706)
- **Original**: अंशसे वामन हुए थे और मेरे पिताके यज्ञमें न हो, भगवान्‌की स्मृति ही अभयदायिनी तथा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11707)
- **Original**: याचक बने थे। आपने पहले तो हमारे राज्य और सब प्रकारसे मज्नल प्रदान करनेवाली है।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11708)
- **Original**: लक्ष्मीकों हर लिया। पर पुनः: बलिकी भक्तिके बालकोंको निगल जानेको उद्यत हुए उस वशीभूत होकर हम सब लोगोंकों सुतललोकमें दानवकों देख मधुसूदन श्रीकृष्णने महाबली
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11709)
- **Original**: स्थान दिया। आप महान्‌ वीर, सर्वेश्वर और बलरामको सम्बोधित करके कहा। भ्क्तवत्सल हैं। मैं पापी हूँ और शापसे गर्दभ श्रीकृष्ण बोले--भैया! यह दानव राजा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11710)
- **Original**: हुआ हूँ। आप शीघ्र ही मेरा वध कर डालिये। बलिका बलवान पुत्र है। इसका नाम साहसिक
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11711)
- **Original**: दुर्वासा मुंनिके शापसे मुझे ऐसा घृणित जन्म है। पूर्वकालमें दुर्वासाने इसे शाप दिया था। उस
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11712)
- **Original**: मिला है। जगत्पते! मुनिने मेरी मृत्यु आपके ब्रह्मशापसे ही यह गदहा हुआ है। यह बड़ा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11713)
- **Original**: हाथसे बतायी थी। आप अत्यन्त तीखे और पापी तथा महान्‌ बल-पराक्रमसे सम्पन्न है; अत:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11714)
- **Original**: अतिशय तेजस्वी षोडशार चक्रसे मेरा वध
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11715)
- **Original**: * भ्रीकृष्णजन्मखण्ड « प्श्र 5555 %4 444 45114 ##4 444 5 554 ## 46 # # 4 $ 55% 4 ### # 4 # 4 5 1 ऊ # # 4 # 6 #% हक़ ऋऊ डक # कह
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11716)
- **Original**: 6 ###ऋ#ऋऊ ऋक के कौजिये। मुक्तिदाता जगन्नाथ! ऐसा करके मुझे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11717)
- **Original**: लिये यहाँ पधारे हैं। आपने पूतनाकों माताके उत्तम गति दीजिये। आप ही वसुधाका उद्धार
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11718)
- **Original**: समान गति प्रदान की है; क्योंकि आप कृपानिधान हैं। करनेके लिये अंशत: बाराहरूपमें अवतीर्ण हुए
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11719)
- **Original**: आप बक, केशी तथा प्रलम्बासुरको और मुझे थे। नाथ! आप ही वेदोंके रक्षक तथा हिरण्याक्षके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11720)
- **Original**: भी मोक्ष देनेवाले हैं। स्वेच्छामय! गुणातीत! नाशक हैं। आप पूर्ण परमात्मा स्वयं ही
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11721)
- **Original**: भक्तभयभञ्जन! राधिकानाथ! प्रसन्न होइये, प्रसन्न हिरण्यकशिपुके वधके लिये नृसिंहरूपमें प्रकट
- **Translation**: 

---

