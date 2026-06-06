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

### Verse 1 (Bramha 0.2081)
- **Original**: अज्ञानि तब देवेश गरुत्माशास्तथा ग्रभों। दिक्याला: सायुधाश्नैव केशवाद्यास्तवाच्युत
- **Translation**: 

---

### Verse 2 (Bramha 0.2082)
- **Original**: ये चानये तव देवेश भेदा: प्रोक्ता मनीषिभि:। तेडपि सर्वे. जगन्नाथ. प्रसनायतलोचन
- **Translation**: 

---

### Verse 3 (Bramha 0.2083)
- **Original**: मया्िता: स्तुता: सर्वे तथा यूय॑ नमस्कृता:। प्रयच्छक बर॑ महां धर्मकामार्थमोक्षदम्‌
- **Translation**: 

---

### Verse 4 (Bramha 0.2084)
- **Original**: धेदास्ते कोर्तिता ये तु हरे संकर्षणादय:। तब पूजार्थसम्भूतास्ततस्त्वयि समाझ्रिता:
- **Translation**: 

---

### Verse 5 (Bramha 0.2085)
- **Original**: ,+ धेदस्तव देवेश बिद्यते परमार्थत:। विविध तब यद्रपमुक्त॑ तदुपचारत:
- **Translation**: 

---

### Verse 6 (Bramha 0.2086)
- **Original**: अद्ठेतं त्वां कथ॑ दैत॑ बक्‍तुं राष्नोति माउव:। एकस्त्वं हि हरें व्यापी चित्स्वभावों-निरञ्ञन:
- **Translation**: 

---

### Verse 7 (Bramha 0.2087)
- **Original**: परम॑ तत्र यद्रपं भावाभावविवर्जितम्‌ । निर्लेप॑ निर्णुणं श्रेष्ठ कूटस्थमचल ध्रुबम्‌
- **Translation**: 

---

### Verse 8 (Bramha 0.2088)
- **Original**: * राजा इन्द्रशुप्रके द्वारा भगवान्‌ शरीविष्णुकी स्तुति * मैं बुढ़ापे और सैकड़ों व्याधियोंसे युक्त हो
- **Translation**: 

---

### Verse 9 (Bramha 0.2089)
- **Original**: देखे हैं और अनेक माताओंका दर्शन किया है। भाँति-भातिके दुःखोंसे पीड़ित हूँ तथा अपने
- **Translation**: 

---

### Verse 10 (Bramha 0.2090)
- **Original**: अनेक प्रकारके जो दुःख और सुख हैं, उनके कर्मपाशमें बँधकर हर्ष-शोकमें मग्न हो विवेकशून्य
- **Translation**: 

---

### Verse 11 (Bramha 0.2091)
- **Original**: अनुभवका भी मुझे अवसर मिला है। भाई, बन्धु, हो गया हूँ। अत्यन्त भयंकर घोर संसार-समुद्रमें
- **Translation**: 

---

### Verse 12 (Bramha 0.2092)
- **Original**: पुत्र और कुटम्बी भी प्राप्त हुए हैं। विष्ठा और गिरा हुआ हूँ। यह जिषयरूपी जलराशिके कारण
- **Translation**: 

---

### Verse 13 (Bramha 0.2093)
- **Original**: मूत्रकी कोचसे भरे हुए स्थ्रियोंके गर्भाशयमें भी दुस्तर है। इसमें राग-द्वेषरूपी मत्स्य भरे पड़े हैं।
- **Translation**: 

---

### Verse 14 (Bramha 0.2094)
- **Original**: मैंने निवास किया है। प्रभो ! गर्भवासमें जो महान्‌ इन्द्रियरूपी भँवरोंसे यह बहुत गहरा प्रतीत होता
- **Translation**: 

---

### Verse 15 (Bramha 0.2095)
- **Original**: दुःख होता है, उसका भी मैंने अनुभव किया है। है। इसमें तृष्णा और शोकरूपी लहरें व्याप्त हैं।
- **Translation**: 

---

### Verse 16 (Bramha 0.2096)
- **Original**: बाल्यावस्था, युवावस्था और वृद्धावस्थामें जो यहाँ न कोई आश्रय है, न कोई अवलम्ब। यह
- **Translation**: 

---

### Verse 17 (Bramha 0.2097)
- **Original**: अनेक प्रकारके दुःख होते हैं, उनसे भी मैं बद्धित सारहीन एवं अत्यन्त चहल है। प्रभो! मैं मायासे
- **Translation**: 

---

### Verse 18 (Bramha 0.2098)
- **Original**: नहीं रहा। मृत्युके समय, यमलोकके मार्गमें तथा मोहित होकर इसके भीतर चिरकालसे भटक रहा
- **Translation**: 

---

### Verse 19 (Bramha 0.2099)
- **Original**: यमराजके घरमें जो दुःख प्राप्त होते हैं, उनको हूँ। हजारों भिन्न-भिन्न योनियोंमें बारंबार जन्म
- **Translation**: 

---

### Verse 20 (Bramha 0.2100)
- **Original**: तथा नरकॉमें होनेवाली यातनाओंको भी मैंने भोगा 103 लेता हूँ। जनार्दन! मैंने इस संसारमें नाना प्रकारके हजारों जन्म धारण किये हैं। अज्ञोंसहित वेद, है। कृमि, कौट, वृक्ष, हाथी, घोड़े, मृग, पक्षी, पैसे, ऊँट, गाय तथा अन्य बनवासी जन्तुओंको नाना प्रकारके शास्त्र, इतिहास-पुराण तथा अनेक
- **Translation**: 

---

