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

### Verse 1 (Bramha 0.341)
- **Original**: दो घड़ीके ही जीवनमें अपनी बुद्धि तथा सत्यके अश्वको पुन: समुद्रसे प्राप्त किया और उसके द्वारा
- **Translation**: 

---

### Verse 2 (Bramha 0.342)
- **Original**: प्रभावसे परमार्थ-साधनके द्वारा तीनों लोक जीत सौ अश्वमेध-यज्ञके अनुष्ठान पूर्ण किये। हमने लिये। दिलीपके पुत्र महाराज भगीरथ हुए, जिन्होंने सुना है, राजा सगरके साठ हजार पुत्र थे।
- **Translation**: 

---

### Verse 3 (Bramha 0.343)
- **Original**: नदियोंमें श्रेष्ठ गज्ाको स्वर्गसे पृथ्वीपर उतारकर मुनियोंने पूछा--साधुबर ! सगरके साठ हजार
- **Translation**: 

---

### Verse 4 (Bramha 0.344)
- **Original**: समुद्रतक पहुँचाया और उन्हें अपनी पुत्री बना पुत्र कैसे हुए। वे अत्यन्त बलवान्‌ और वीर किस
- **Translation**: 

---

### Verse 5 (Bramha 0.345)
- **Original**: लिया। भगीरथको पुत्री होनेके कारण ही गज्नाको प्रकार हुए? भागीरथी कहते हैं। भगीरथके पुत्र राजा श्रुत हुए। लोमहर्घणजीने कहा--सगरकी दो रानियाँ
- **Translation**: 

---

### Verse 6 (Bramha 0.346)
- **Original**: श्रुतके पुत्र नाभाग हुए, जो बड़े धर्मात्मा थे। थीं, जो तपस्या करके अपने पाप दग्ध कर चुकौ
- **Translation**: 

---

### Verse 7 (Bramha 0.347)
- **Original**: नाभागके पुत्र अम्बरीष हुए, जो सिन्धुद्दीपके पिता थीं। उनमें बड़ी रानी विदर्भनरेशकी कन्या थीं।
- **Translation**: 

---

### Verse 8 (Bramha 0.348)
- **Original**: थे। सिन्धुद्वीपके पुत्र अयुताजित्‌ हुए और अयुताजितूसे उनका नाम केशिनी था। छोटी रानीका नाम महती
- **Translation**: 

---

### Verse 9 (Bramha 0.349)
- **Original**: महायशस्वी ऋतुपर्णको उत्पत्ति हुई, जो द्यूतविद्याके था। वह अरिष्टनेमिकी पुत्री तथा परम धर्मपरायणा
- **Translation**: 

---

### Verse 10 (Bramha 0.350)
- **Original**: रहस्यको जानते थे। राजा ऋतुपर्ण महाराज नलके थीं। इस पृथ्वीपर उसके रूपकी समता करनेवाली
- **Translation**: 

---

### Verse 11 (Bramha 0.351)
- **Original**: सखा तथा बड़े बलवान थे। ऋतुपर्णके पुत्र दूसरी कोई स्त्री नहीं थी। महर्षि और्वने उन महायशस्त्री आर्तुर्पणि हुए। उनके पुत्र सुदास हुए, दोनोंको इस प्रकार वरदान दिया--एक रानी साठ
- **Translation**: 

---

### Verse 12 (Bramha 0.352)
- **Original**: जो इन्द्रके मित्र थे। सुदासके पुत्रको सौदास हजार पुत्र प्राप्त करेगी और दूसरीको एक ही पुत्र
- **Translation**: 

---

### Verse 13 (Bramha 0.353)
- **Original**: बताया गया है; वे ही कल्माषपादके नामसे होगा, किंतु वह वंश चलानेवाला होगा। इन दो
- **Translation**: 

---

### Verse 14 (Bramha 0.354)
- **Original**: विख्यात हुए तथा राजा मित्रसह भी उन्हींका नाम चरोमेंसे जिसकी जिसे इच्छा हो, वह बहो ले ले।'
- **Translation**: 

---

### Verse 15 (Bramha 0.355)
- **Original**: था। कल्माषपादके पुत्र सर्वकर्मा हुए, सर्वक्माके तब उनमेंसे एकने साठ हजार पुत्रोंका वरदान
- **Translation**: 

---

### Verse 16 (Bramha 0.356)
- **Original**: पुत्र अनरण्य थे। अनरण्यके दो पुत्र हुए--अनमित्र ग्रहण किया और दूसरीने वंश चलानेवाले एक ही
- **Translation**: 

---

### Verse 17 (Bramha 0.357)
- **Original**: और रघु। अनमित्रके पुत्र राजा दुलिदुह थे। उनके पुत्रको प्राप्त करना चाहा। मुनिने 'तथास्तु' कहकर
- **Translation**: 

---

### Verse 18 (Bramha 0.358)
- **Original**: पुत्रका नाम दिलीप हुआ, जो भगवान्‌ श्रीरामचद्रंजीके वरदान दे दिया; फिर एक रानीके राजा पश्चजन
- **Translation**: 

---

### Verse 19 (Bramha 0.359)
- **Original**: प्रपितामह थे। दिलीपके पुत्र महाबाहु रघु हुए, जो हुए और दूसरीने बोजसे भरी हुई एक दूँबी उत्पन्न
- **Translation**: 

---

### Verse 20 (Bramha 0.360)
- **Original**: अयोध्याके महाबली सम्राट्‌ थे। रचुक अज और
- **Translation**: 

---

