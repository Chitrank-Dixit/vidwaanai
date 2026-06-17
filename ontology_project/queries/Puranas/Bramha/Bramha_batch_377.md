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

### Verse 1 (Bramha 0.7521)
- **Original**: प्रपितामह हैं, वे लेपभागभोजी पितरोंकी श्रेणीमें एक हो अर्ध्य और एक ही पवित्रकका विधान
- **Translation**: 

---

### Verse 2 (Bramha 0.7522)
- **Original**: चले जाते हैं। उन्हें पितृपिण्ड पानेका अधिकार है। अग्निकरण और आवाहनकी क्रिया भी इसमें
- **Translation**: 

---

### Verse 3 (Bramha 0.7523)
- **Original**: नहीं रहता। उनसे आरम्भ करके चार पीढ़ी नहीं होती । सपिण्डीकरणमें अपसव्य होकर अयुग्म
- **Translation**: 

---

### Verse 4 (Bramha 0.7524)
- **Original**: ऊपरके पितर, जो अबतक पुत्रके लेपभागका अन्न ब्राह्मणॉंकों भोजन कराना चाहिये। इसमें जो
- **Translation**: 

---

### Verse 5 (Bramha 0.7525)
- **Original**: ग्रहण करते थे, उसके सम्बन्धसे रहित हो जाते विशेष क्रिया है, उसका वर्णन करता हूँ; एकाग्रचित्त
- **Translation**: 

---

### Verse 6 (Bramha 0.7526)
- **Original**: हैं। अब उनको लेपभागका अन्न पानेका अधिकार होकर सुनो। सपिण्डीकरणमें तिल, चन्दन और
- **Translation**: 

---

### Verse 7 (Bramha 0.7527)
- **Original**: नहीं रहता। वे सम्बन्धहीन अन्नका उपभोग करते जलसे युक्त चार पात्र होते हैं। उनमेंसे तीन तो
- **Translation**: 

---

### Verse 8 (Bramha 0.7528)
- **Original**: हैं। पिता, पितामह और प्रपितामह--इन तीन पितरोंके लिये रखे और एक प्रेतके लिये। प्रेतके
- **Translation**: 

---

### Verse 9 (Bramha 0.7529)
- **Original**: पुरुषोंको पिण्डका अधिकारी समझना चाहिये। पात्रसे अर्घ्यजल लेकर 'ये समाना: समनसः0'
- **Translation**: 

---

### Verse 10 (Bramha 0.7530)
- **Original**: इनसे भिन्न अर्थात्‌ पितामहके पितामहसे लेकर इत्यादि मन्त्रका जप करते हुए पितरोंके तीनों
- **Translation**: 

---

### Verse 11 (Bramha 0.7531)
- **Original**: ऊपरके जो तीन पीढ़ींके पुरुष हैं, वे लेपभागके पात्रोंमें छोड़ना चाहिये। शेष कार्य अन्य श्राद्धोंकी
- **Translation**: 

---

### Verse 12 (Bramha 0.7532)
- **Original**: अधिकारी हैं। इस प्रकार छः ये और सातवाँ भाँति करना चाहिये। स्त्रियोंक लिये भी इसी
- **Translation**: 

---

### Verse 13 (Bramha 0.7533)
- **Original**: यजमान--सब मिलकर सात पुरुषोंका घनिष्ठ प्रकार एकोदिष्टका विधान है। यदि पुत्र न हो तो
- **Translation**: 

---

### Verse 14 (Bramha 0.7534)
- **Original**: सम्बन्ध होता है--ऐसा मुनियोंका कथन है। यह स्त्रियॉंका सपिण्डीकरण नहीं होता। पुरुषोंको
- **Translation**: 

---

### Verse 15 (Bramha 0.7535)
- **Original**: सम्बन्ध यजमानसे लेकर ऊपरके लेपभागभोजी उचित है कि वे स्त्रियोंके लिये भी प्रतिवर्ष उनकी
- **Translation**: 

---

### Verse 16 (Bramha 0.7536)
- **Original**: पितरोंतक माना जाता है। इनसे ऊपरके सभी मृत्युतिधिको एकोदिष्ट श्राद्ध करें। पुत्रके अभावमें
- **Translation**: 

---

### Verse 17 (Bramha 0.7537)
- **Original**: पितर पूर्वज कहलाते हैं। पूर्वजोंमेंसे जो नरकमें सपिण्ड और सपिण्डके अभावमें सहोदक इस
- **Translation**: 

---

### Verse 18 (Bramha 0.7538)
- **Original**: निबास करते हैं, जो पशु-पश्षीकी योनिमें पड़े हैं विधिको पूर्ण करें। जिसके कोई पुत्र न हो,
- **Translation**: 

---

### Verse 19 (Bramha 0.7539)
- **Original**: तथा जो भूत आदिके रूपमें स्थित हैं, उन सबको उसका श्राद्ध उसके दौहित्र कर सकते हैं।
- **Translation**: 

---

### Verse 20 (Bramha 0.7540)
- **Original**: विधिपूर्वक श्राद्ध करनेवाला यजमान तृप्त करता युत्रिका--विधिसे ब्याही हुई कन्याके पुत्र तो
- **Translation**: 

---

