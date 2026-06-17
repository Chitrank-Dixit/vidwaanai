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

### Verse 1 (Bramha 0.3261)
- **Original**: प्रसन्न करनेके लिये माता अञ्ञनाको लाकर गोदावरीमें पर्वतपर ही रहती थी। एक समय केसरी दक्षिणसमुद्रके
- **Translation**: 

---

### Verse 2 (Bramha 0.3262)
- **Original**: नहलाया। इसी प्रकार हनुमानजी भी अद्विकाको तटपर गये थे। इसी बीचमें महर्षि अगस्त्य अज्ञन
- **Translation**: 

---

### Verse 3 (Bramha 0.3263)
- **Original**: लेकर बड़ी उताबलीके साथ गौतमी गड्जाके पर्वतपर आये। अज्जना और अद्विका दोनोंने
- **Translation**: 

---

### Verse 4 (Bramha 0.3264)
- **Original**: तटपर आये। तबसे वह पैशाच और आञ्ञनतीर्थके महषिंका यथोचित पूजन किया। इससे प्रसन्न
- **Translation**: 

---

### Verse 5 (Bramha 0.3265)
- **Original**: नामसे विख्यात हुआ। वह समस्त अभीष्ट बस्तुऑंको होकर महर्षिने कहा--'तुम दोनों वर माँगो।' वे
- **Translation**: 

---

### Verse 6 (Bramha 0.3266)
- **Original**: देनेवाला शुभ तीर्थ है। ब्रह्मगिरिसे तिरपन योजन बोलीं--मुनीश्चवर! हमें ऐसे पुत्र दीजिये, जो
- **Translation**: 

---

### Verse 7 (Bramha 0.3267)
- **Original**: पूर्वकी ओर मार्जार-तीर्थ है। मार्जार-तीर्थसे आगे सबसे बलवान, श्रेष्ठ और सब लोगोंका उपकार
- **Translation**: 

---

### Verse 8 (Bramha 0.3268)
- **Original**: हनुमत्‌-तीर्थ और वृषाकपि-तीर्थ है। उसके आगे करनेवाले हों।' “तथास्तु” कहकर मुनिश्रेष्ठ अगस्त्य
- **Translation**: 

---

### Verse 9 (Bramha 0.3269)
- **Original**: फेना-संगमतोर्थ बताया गया है, जो समस्त दक्षिण दिशामें चले गये। कुछ कालके बाद
- **Translation**: 

---

### Verse 10 (Bramha 0.3270)
- **Original**: कामनाओंको पूर्ण करनेवाला है। उसका स्वरूप अज्जनाने वायुके अंशसे हनुमानूजीको जन्म दिया
- **Translation**: 

---

### Verse 11 (Bramha 0.3271)
- **Original**: और फल उसीके प्रसद्भमें बताया जायगा। #4*-््मय्दल्य2.>> क्षुधातीर्थ और अहल्या-संगम-तीर्थका माहात्म्य ख्रह्माजी कहते हैं--नारद! अब श्षुधातीर्थका
- **Translation**: 

---

### Verse 12 (Bramha 0.3272)
- **Original**: और जलसे सम्पन्न था। अपनेको क्षुघासे पीड़ित वर्णन करता हूँ, एकाग्रचित्त होकर सुनो। वह
- **Translation**: 

---

### Verse 13 (Bramha 0.3273)
- **Original**: और गौतमको वैभवशाली देख कण्वका मन परम पुण्यमय तीर्थ मनुष्योंकी समस्त कामनाओंको
- **Translation**: 

---

### Verse 14 (Bramha 0.3274)
- **Original**: विरक्तिसे भर गया। वे सोचने लगे-“गौतम भी पूर्ण करनेवाला है। पूर्वकालमें कण्व नामसे
- **Translation**: 

---

### Verse 15 (Bramha 0.3275)
- **Original**: एक श्रेष्ठ ब्राह्मण हैं और मैं भी उन्होंकी भाँति प्रसिद्ध एक ऋषि थे। वे बेदवेत्ताओंमें श्रेष्ठ और
- **Translation**: 

---

### Verse 16 (Bramha 0.3276)
- **Original**: तपोनिष्ठ हूँ। बराबरवालेके पास याचना करना तपस्वी थे। महर्षि कण्ब भूखसे पीड़ित होकर कदापि उचित नहीं है। अतः यद्यपि मैं भूखसे अनेक आश्रमोंपर घूमा करते थे। एक दिन वे
- **Translation**: 

---

### Verse 17 (Bramha 0.3277)
- **Original**: व्याकुल हूँ और मेरे शरीरमें पोड़ा भी हो रहो है, गौतमके पवित्न आश्रमपर आये। वह आश्रम अन्न
- **Translation**: 

---

### Verse 18 (Bramha 0.3278)
- **Original**: तथापि गौतमके घरमें भोजन नहों करूँगा। इस
- **Translation**: 

---

### Verse 19 (Bramha 0.3279)
- **Original**: + क्षुधातीर्ध और अहल्या-संगम तीर्थका माहात्म्य * 157 ड्क्ल्न्नखिचच्च््््ल्िखवखि्ोजिलखओओओ्आओअओअ ज़््लञकझसआआआआआओआआ्णओओण्?ओअइअइअषयडयडःि3-ा: समय गौतमी गद्जाके तटपर चलूँ और उन्हींसे , क्षुधादेवी! तुम समस्त पापियोंके लिये पापमयी, सम्पत्ति माँगूँ।' ऐसा निश्चय करके महर्षि कण्व
- **Translation**: 

---

### Verse 20 (Bramha 0.3280)
- **Original**: दुःखमयी और लोभमयी हो। धर्म, अर्थ और परम पावन गज्जाजीके तटपर गये और स्नान करके
- **Translation**: 

---

