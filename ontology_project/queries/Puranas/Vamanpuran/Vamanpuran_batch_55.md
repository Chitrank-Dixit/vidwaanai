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

### Verse 1 (Vamanpuran 0.1081)
- **Original**: नहीं होता
- **Translation**: 

---

### Verse 2 (Vamanpuran 0.1082)
- **Original**: 53--56
- **Translation**: 

---

### Verse 3 (Vamanpuran 0.1083)
- **Original**: # इस अ्कार क्रीवामवपुराणमें बारहवाँ अध्याय समाप्त हुआ
- **Translation**: 

---

### Verse 4 (Vamanpuran 0.1084)
- **Original**: 842 8+>+ सुकेशिके प्रश्नके उत्तरमें ऋषियोंका जम्बू-द्वीपकी स्थिति और उनमें स्थित तथा नदियोंका वर्णन सुकेशिस्याच सुकेशीने कहा-- आदरणीय ऋषियो ! आप लोगोंने भवद्धिरुदिता घोरा पुष्करद्वीपसंस्थिति:।
- **Translation**: 

---

### Verse 5 (Vamanpuran 0.1085)
- **Original**: पुष्करद्रीपके भयंकर अवस्थानका वर्णन किया, अब आप जम्बूद्वीपस्थ तु संस्थान कथयन्तु महर्षयः
- **Translation**: 

---

### Verse 6 (Vamanpuran 0.1086)
- **Original**: लोग (कृपाकर) जम्यूद्वीपकी स्थितिका वर्णन करें
- **Translation**: 

---

### Verse 7 (Vamanpuran 0.1087)
- **Original**: अष्य ऊचुर ऋषियोंने कहा--राक्षसेध्वर! (अब) तुम हम लोगोंसे जम्बूद्वीपस्थ संस्था कथ्यमानं निशामय।
- **Translation**: 

---

### Verse 8 (Vamanpuran 0.1088)
- **Original**: जम्बूद्वीपकी स्थितिका वर्णन सुनो। यह द्वीप अत्यन्त नवभेद॑ सुविस्तीर्ण स्वर्गमोक्षफलप्रदम्‌
- **Translation**: 

---

### Verse 9 (Vamanpuran 0.1089)
- **Original**: विशाल है और नव भागोंमें विभक्त है। यह स्वर्ग एव मध्ये त्विलावृतो वर्षो भद्गाश्व पूर्वतो5द्भुत:।
- **Translation**: 

---

### Verse 10 (Vamanpuran 0.1090)
- **Original**: मोक्ष-फलको देनेवाला है। जम्बूद्वीपके बीचमें इलावृतवर्ष, पूर्व उत्तरतश्लापि हिरण्यो राक्षसेश्वर
- **Translation**: 

---

### Verse 11 (Vamanpuran 0.1091)
- **Original**: पूर्वमें अद्भुत भद्राश्ववर्ष तथा पूर्वोत्तरमें हिरण्यकवर्ष है। पूर्वदक्षिणतश्षापि किंनरो वर्ष उच्चते।
- **Translation**: 

---

### Verse 12 (Vamanpuran 0.1092)
- **Original**: पूर्व-दक्षिणमें किन्नरवर्ष, दक्षिणमें भारतवर्ष तथा दक्षिण- भारतो दक्षिणे प्रोक्तो हरिरदक्षिणपश्चिमे
- **Translation**: 

---

### Verse 13 (Vamanpuran 0.1093)
- **Original**: पश्चिममें हरिवर्ष बताया गया है। इसके पश्चिममें पश्चिमे केतुमालश्ष रम्यकः पश्चिमोत्ते।
- **Translation**: 

---

### Verse 14 (Vamanpuran 0.1094)
- **Original**: केतुमालवर्ष, पश्चिमोत्तरमें रस्यकवर्ष और उत्तरमें कल्पवृक्षसे उत्ते च कुरुर्वर्ष;। कल्पवृक्षसमावृत:
- **Translation**: 

---

### Verse 15 (Vamanpuran 0.1095)
- **Original**: समादृत कुरुवर्ष है
- **Translation**: 

---

### Verse 16 (Vamanpuran 0.1096)
- **Original**: अध्याय 13 ]* सुकेशिके प्रश्तके उत्तरमें ऋषियोंका जम्यू-द्वीपकी और उनमें स्थित पर्वत तथा नदियोंका वर्णन 59 पुण्या रम्या नवैवैते वर्षा: शालकर्टंकट। सुकेशि! ये नव पवित्र और रमणोय वर्ष हैं। इलाबृताद्या ये चा्ट्रौ वर्षमुक्त्वैव भारतम्‌
- **Translation**: 

---

### Verse 17 (Vamanpuran 0.1097)
- **Original**: भारतवर्षके अतिरिक्त इलावृतादि आठ वर्षोमें युगावस्था न तेष्वस्ति युगावस्था जरामृत्युभयं न च। तेषां स्वाभाविका सिद्धि: सुखप्राया ह्ययलत: । विपर्ययों न तेष्वस्ति नोत्तमाधममध्यमा:
- **Translation**: 

---

### Verse 18 (Vamanpuran 0.1098)
- **Original**: 7 यदेतद्‌ भारत॑ वर्ष नवद्वीप॑ निशाचर। सागरान्तरिता: सर्वे अगम्याक्ष परस्परम्‌ू
- **Translation**: 

---

### Verse 19 (Vamanpuran 0.1099)
- **Original**: 8 इन्द्रह्ीप: कसेरुमांस्ताम्रवर्णों गर्भस्तिमान्‌। नागद्वीप: कटाहश्व सिंहलो वारुणस्तथा
- **Translation**: 

---

### Verse 20 (Vamanpuran 0.1100)
- **Original**: 9 अय॑ तु नवमस्तेषां द्वीप: सागरसंवृतः। कुमाराख्य: परिख्यातो द्वीपो5यं दक्षिणोत्तर:
- **Translation**: 

---

