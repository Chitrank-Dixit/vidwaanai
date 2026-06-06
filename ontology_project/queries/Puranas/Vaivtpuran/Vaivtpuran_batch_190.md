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

### Verse 1 (Vaivtpuran 13.3169)
- **Original**: 4 41767 67644 57 4 4 क कक तुलसीने कहा--भद्रपुरुष! मैं राजा धर्म-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.3170)
- **Original**: प्रशस्त कहते हैं और दूसरीको अप्रशस्त। लक्ष्मी, ध्वजकी कन्या हूँ। तपस्या करनेके विचारसे इस
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.3171)
- **Original**: सरस्वती, दुर्गा, सावित्री और राधिका-ये पाँच तपोवनमें ठहरी हुई हूँ। तुम कौन हो? यहाँसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.3172)
- **Original**: देवियाँ सृष्टिसूत्र हैं--सृष्टिकी मूल कारण हैं। इन सुखपूर्वक चले जाओ; क्योंकि उच्च कुलकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.3173)
- **Original**: आध्या देवियोंके प्रादुर्भावका प्रयोजन केवल सृष्टि किसी भी अकेली साध्वी कन्याके साथ एकान्तमें
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.3174)
- **Original**: करना है। इनके अंशसे प्रकट गड़ा आदि देवियाँ कोई भी कुलीन पुरुष बातचीत नहीं करता-ऐसा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.3175)
- **Original**: वास्तव-रूपा कहलाती हैं। इनको श्रेष्ठ माना जाता नियम मैंने श्रुतिमें सुना है। जो कलुषित कुलमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.3176)
- **Original**: है। ये यशःस्वरूपा और सम्पूर्ण मड्रलोंकी जननी उत्पन्न है तथा जिसे धर्मशास्त्र एवं श्रुतिका अर्थ
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.3177)
- **Original**: हैं। शतरूपा, देवहूति, स्वधा, स्वाहा, दक्षिणा, सुननेका कभी सुअवसर नहीं मिला, वह दुराचारी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.3178)
- **Original**: छायावती, रोहिणी, वरुणानी, शची, कुबेरपत्नी, व्यक्ति ही कामी बनकर परस्त्रीकी कामना करता
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.3179)
- **Original**: अदिति, दिति, लोपाझुद्रा, अनसूया, कोटिबी, है। स्त्रीकी मधुर वाणीमें कोई सार नहीं रहता।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.3180)
- **Original**: तुलसी, अहल्या, अरुन्धती, मेना, तारा, मन्दोदरी, वह सदा अभिमानमें चूर रहती है। वास्तवमें बह
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.3181)
- **Original**: दमयन्ती, वेदबती, गड्भा, मनसा, पुष्टि, तुष्टि, विषसे भरे हुए घड़ेके समान है, परंतु उसका मुख
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.3182)
- **Original**: स्मृति, मेधा, कालिका, वसुन्धरा, षष्ठी, मड्जलचण्डी, ऐसा जान पड़ता है मानो सदा अमृतसे भरा हो।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.3183)
- **Original**: धर्म-पत्नी मूर्ति, स्वस्ति, श्रद्धा, शान्ति, कान्ति, संसाररूपी कारागारमें जकड़नेके लिये वह साँकल
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.3184)
- **Original**: क्षमा, निद्रा, तन्द्रा, क्षुधा, पिपासा, सन्ध्या, दिवा, है। स्त्रीको इन्द्रजाल-स्वरूपा तथा स्वप्रके समान
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.3185)
- **Original**: रात्रि, सम्पत्ति, धृति, कीर्ति, क्रिया, शोभा, प्रभा मिथ्या कहते हैं। बाहरसे तो यह अत्यन्त सुन्दरता
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.3186)
- **Original**: और शिवा--स्त्रीरूपमें प्रकट ये देवियाँ प्रत्येक धारण करती है, परंतु उसके भीतरके अड्छ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.3187)
- **Original**: युगमें उत्तम मानी जाती हैं। कुत्सित भावोंसे भरे रहते हैं। उसका शरीर विष्ठा, जो स्वर्गकी दिव्य अप्सराएँ हैं, वे कृत्या- मूत्र, पीब और मल आदि नाना प्रकारकी दुर्गन्धपूर्ण
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.3188)
- **Original**: स्वरूपा हैं, उन्हें अप्रशस्त कहा गया है। अखिल बस्तुओंका आधार है। रक्तरज्ञित तथा दोषयुक्त
- **Translation**: 

---

