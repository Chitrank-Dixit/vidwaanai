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

### Verse 1 (Vishnu Puran 0.2141)
- **Original**: 76 पादप्रणामायनते तपुत्थाप्य पिता सुतम्‌। हिरण्यकशिपु: प्राह प्रह्मादपमितौजसम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2142)
- **Original**: 12 हिःण्यकशिपुरुकाच पठ्यतां भवता वत्स सारभूत॑ सुभाषितम्‌ । कालेनैतावता यत्ते सदोद्युक्तेन शिक्षितम
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2143)
- **Original**: 13 प्रह्माट उवाच श्रूयतां तात यक्ष्यामि सारभूत॑ तवाज्ञया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2144)
- **Original**: समाहितमना भूत्वा यत्मे चेतस्ववस्थितम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2145)
- **Original**: 94 अनादिमभध्यान्तमजपमवृद्धिक्षयमच्युतम्‌ । प्रणतो5स्म्यन्तसन्तान सर्वकारणकारणम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2146)
- **Original**: 15 अीपदारशार उताय एतत्निशम्य दैत्येद्ध/ सकोपो रक्तछोचन: । विलोक्य तदणुरुं प्राह स्फुरिताधरपललख:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2147)
- **Original**: 16 हिरण्यकशिपुरवाब ब्रह्मनन्धो किमेतत्ते विपक्षस्तुतिसंहितम्‌। असारं ग्राहितो बालो मामवज्ञाय दुर्मते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2148)
- **Original**: 97 गृस्स्याच दैतल्येश्व न कोपस्प वहामागन्तुमहसि । मपोपदेशजनित नायं॑ बदति ते सुतः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2149)
- **Original**: 18 हिरण्यकरशिपुरुवाच अनुशिष्टोउसि केनेद्ग्वत्स प्र्माद कध्यताम्‌ । प्रब्रवीति गुरुस्तव
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2150)
- **Original**: 19 प्रहाद उताच बने वर्मा लान आह के सास
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2151)
- **Original**: 20 को बिष्णु: सुदुर्बुद्धे य॑ ब्रवीषि पुनः पुनः । जगतामीश्वरस्येह पुरतः प्रसभ॑ मम
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2152)
- **Original**: 21 अद्ाद उपाच न शब्दगोचरं यस्य योगिध्येयं परं पदम। यतो यश्च स्वर्य विश्व स विष्णु: परमेश्वर:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2153)
- **Original**: 22 हिरण्यकशिएस्वाच परमेश्वरसंज्ञोजज्ञ किमन्यो मय्यवस्थिते । तथापि मर्तुकामर्स्त्व प्रब्रवीषि पुनः पुनः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2154)
- **Original**: 23 श्रीविष्णुपुराण (6 अ* 17 प्रद्यपानमें छूगा हुआ था
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2155)
- **Original**: तब, अपने चरणोमें झुके हुए अपने परम तेजस्बी पुत्र प्रहादजोको उठाकर पिता डिरण्यकदिपुने कहा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2156)
- **Original**: हिरण्यकदिपु. जोला--वत्स !_ अबतक अध्ययममें निरन्तर तत्पर रहकर तुमने जो कुछ पढ़ा है डसक़ा सारभूत शुभ भाषण हमें सुनाओ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2157)
- **Original**: प्रह्मादजी खोले--पिताजी ! मेरे मनसें जो सबके साराशरूपसे स्थित है वह मैं आपको आज्ञानुसार सुनाता हूँ, सावधान होकर सुनिये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2158)
- **Original**: जो आदि, मध्य और अन्तसे रहित, अजन्मा, वृद्धि-क्षय-शून्‍्य और अच्यूत हैं, समस्त कारणोंके कारण तथा जगत्‌के स्थिति और अन्तकर्ता उन श्रीहरिको मैं प्रणाम करता हूँ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2159)
- **Original**: श्रीपराझरजी बोले--यह सुन देत्यफ्ज हिरण्यकशिपुने क्रोधसे नेत्र व्वछ कर प्रहादके गुरूकी ओर देखकर काँपते हुए ओटोंसे कहा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2160)
- **Original**: हिरण्यकश्षिपु बोला--रे दुर्युद्धि ब्राह्मणाधम ! यह क्या? तूने मेरें अवज्ञा कर इस बालकको मेरे विपक्षीकी स्तुतिसे युक्त असार शिक्षा दी है ]
- **Translation**: 

---

