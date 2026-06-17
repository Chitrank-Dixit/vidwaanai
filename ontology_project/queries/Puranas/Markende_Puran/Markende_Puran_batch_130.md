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

### Verse 1 (Markende Puran 0.2581)
- **Original**: चणिडके
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2582)
- **Original**: पूर्ब, पश्चिय और दक्षिण दिशारें आप हमारी रक्षा करें तथा ईश्वरिं! अपने ब्रिशूलकों घुमाकर आप 3प्तर दिशामें भो हमागी रक्षा करें
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2583)
- **Original**: प्रीनों लोकोंमें आपके जो परम सुन्दर एवं अत्यन्त भयड़ू2 रूप विचरते रहते हैं, उनके द्वारा भी आप हमारी ज़था इस भूलोककी रक्षा करें
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2584)
- **Original**: अम्बिके। आपके ऋर पह्नवॉमें शोभा पानेवाले खज़, शुल और गदा शाद्दि जो जो अस्त्र हों, उन सबके द्वारा आप रब ओरसे हमलोगोंकी रक्षा करें
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2585)
- **Original**: कऋषिरकाच
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2586)
- **Original**: ए8 4 एवं स्तुता सुरेर्दिव्य: कुसुपेर्नन्दनोद्धवैः। अर्चिता जगतां धात्री त्रथा गन्धानुलेपनः
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2587)
- **Original**: भक्तणा समस्तैस्त्रिदशैरदिब्वीर्थूपैस्तु धूपिता। प्राह प्रसादसुप्रुखी सप्रस्तान्‌ प्रणतान्‌ सुग़न्‌
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2588)
- **Original**: ऋषि कहते हैं--
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2589)
- **Original**: इस प्रकार जेब देवताओंने जगन्गाता दुर्गाकी स्तुति को और नन्दनवनके दिव्य पुध्पों पत्र गन्ध-चन्दन आदिके : * संक्षिप्त मार्केण्ड्रेसपुराण + 3244::524:4:5#&6# 56 # ##5 ककक्त्लभ
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2590)
- **Original**: 5 90:17 22754::5::#: 64 # 74077 47 % 7 * क7 785 35 5:55. 65 & ##< ## < 66 6 5 छार उनका पूजन किया, फिर सबने सिलकर जब भक्ति पूर्वक दिव्य धूपोंकी सुगन्ध निवेदन कौ, तब देवीने प्रसमथदन होकर प्रणाय करते हुए सब देवताओंस कहा--
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2591)
- **Original**: बेव्युकाच
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2592)
- **Original**: ब्रिवत्ां त्रिदशा: सर्वे यदस्मत्तोडभिवाड्छितम्‌
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2593)
- **Original**: देवी बोलॉ--
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2594)
- **Original**: देवताओं! तुम सब लोए मुझसे जिस वस्तुकी अभिलाष्षा रखते हो, उसे माँगो
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2595)
- **Original**: वेढ्ा ऊचु:
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2596)
- **Original**: 3 35 भगवत्या कृत सर्व न किंचिदव्िष्यते
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2597)
- **Original**: यदय॑ निहतः शरत्रुरस्माक॑ पहिघासुरः। यदि चापि वे वेयस्त्थथास्मार्क महेश्वरि
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2598)
- **Original**: संस्यृता संस्पृता त्व॑ नो हिंसेथाः परमापद:। यश्च मर्त्व; स्तर्वरेभिस्त्वां स्तोष्यत्यमलानने
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2599)
- **Original**: त्तस्थ चित्तर्द्धिविभवैर्धवदारादिसम्पदाम
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2600)
- **Original**: वृद्धये3स्मत्प्सन्ना त्वं भवेश्ञा: सर्वदाम्त्रिके
- **Translation**: 

---

