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

### Verse 1 (Vaivtpuran 23.1482)
- **Original**: जराबस्थाको हर लेनेबाला है। महात्माजन ही उस लोकका दर्शन कर पाते हैं। . नारदजीने देखा, दूर सभा-मण्डपके मध्य- मुने ! वहाँ सूर्य और चन्द्रमाकी किरणें नहीं पहुँच
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1483)
- **Original**: भागमें शान्तस्वरूप, कल्याणदाता एवं मनोहर पार्ती। परकोटोंके रूपमें प्रकट हुए अत्यन्त ऊँचे, शिव विराजमान हैं। उनके पाँच मुख पाँच बहुत बढ़े हुए तथा ज्वालाओंसे जगमगाते हुए
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1484)
- **Original**: चन्द्रमाओंके समान आह्वाददायक जान पड़ते हैं। असंख्य पावक उस लोकको चारों ओरसे घेरकर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1485)
- **Original**: प्रत्येक मुखमें प्रफुल्ल कमलके समान तीन-तीन स्थित हैं। उस श्रेष्ठ धामका विस्तार एक लाख
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1486)
- **Original**: नेत्र हैं। उन्होंने मस्तकपर गज्भजाजीको धारण कर योजन है। उसमें श्रेष्ठ रत्रोंके बने हुए तीन हजार
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1487)
- **Original**: रखा है तथा उनके भालदेशमें निर्मल चन्द्रमाका गृह हैं। हौरेके सार-तत्त्वसे बने हुए भाँति-
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1488)
- **Original**: मुकुट शोभा पा रहा है। तपाये हुए सुवर्णके भाँतिके चित्र-विचित्र मनोहर भवन उसकी शोभा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1489)
- **Original**: समान कान्तिमती पीली जटा धारण करनेवाले बढ़ाते हैं। बहाँ माणिक्य तथा मुक्तामणिके दर्पण
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1490)
- **Original**: दिगम्बर भगवान्‌ शिव उस समय आकाशगज्जामें हैं। विश्वकर्मने उस लोकको सपनेमें भी नहीं
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1491)
- **Original**: उत्पन्न कमलोंके बीज (पद्माक्ष)-की मालासे देखा होगा। एकमात्र शिवसेवी महात्माजन हो
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1492)
- **Original**: सानन्द ' श्रीकृष्ण” नामका जप कर रहे थे। उनकी उसमें कल्पपर्यन्त निरन्तर वास करते हैं। वह
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1493)
- **Original**: अद्गजकान्ति गौर वर्णकी है, वे अनन्त और शिवलोक करोड़ों-करोड़ों सिद्धों तथा शिव-
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1494)
- **Original**: अविनाशी हैं। उनके कण्ठमें सुन्दर नील चिह्न पार्षदोंसे युक्त है। वहाँ लाखों विकट भैरव निवास
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1495)
- **Original**: शोभा पाता है। वे नागराजके हारसे अलंकृत हैं। करते हैं। सैकड़ों लाख क्षेत्र उसे घेरे हुए हैं।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1496)
- **Original**: बड़े-बड़े योगीन्द्र, सिद्धेन्द्र और मुनीन्द्र उनके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1497)
- **Original**: 72 » संक्षिम ख्हावैयर्तपुराण * अं 5 अंक % 45% 55% 5 हक ऊऊअऊडऋदऊ कद धर शक ऋडऊ कक डक इक ऋडअऊ दर अ कक अप ड 4 555 शक अ 5 8 45% 85 6 45 8 85 चरणोंकी वन्दना करते हैं। वे सिद्धेश्वर हैं,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1498)
- **Original**: हो गये। फिर उन्होंने मुनिको बड़े वेगसे पकड़कर सिद्धिविधानके कारण हैं, मृत्युक्य हैं तथा काल
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1499)
- **Original**: हृदयसे लगा लिया और आशीर्वाद तथा आसन और यमका भी अन्त करनेवाले हैं। उनका मुख
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1500)
- **Original**: आदि दिये। साथ ही उन तपोधनसे आनेका प्रसन्नतासूचक हास्यसे अत्यन्त मनोहर जान
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1501)
- **Original**: प्रयोजन और कुशल-मड्जल पूछा। इसके बाद पड़ता है। वे सम्पूर्ण आश्नितोंकों कल्याण तथा
- **Translation**: 

---

