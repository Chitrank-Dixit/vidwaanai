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

### Verse 1 (Nard Puran 224.3101)
- **Original**: संहिताका बड़े उत्साहसे अध्ययन किया। अनघ! इस प्रकार ये मोक्षधर्म बतलाये गये, जो पाठकों और श्रेताओंके हृदयमें भगवान्‌की भक्ति बढ़ानेवाले हैं। #3+#> अप सि>->>> 1, शान्तं प्रसन्नवद्न वक्ष:स्थलस्थया लक्ष्म्या कौस्तुभेन भ्राजत्किरीटवलयं त॑ दृष्ठा भक्तिभावेन जगद्वीजस्वरूपाय हंसाय मत्स्यरूपाय चतु:सनाय.. कूर्माय भार्गवेद्राय रामाय चतुर्व्युहाय राघयाय विश्वरूपाय आदित्यसोमनेत्राय श्रीश्ञाय बृहदारण्यवेद्याय गोविन्दाय जगत्कत्रे अधोक्षजाय धर्माय विरिक्नये.. त्रिककुदे वृषाकपषपष॒ ऋद्धाय निरक्ननाय नित्याय सहओजोबलाय हृषीकेशाय जगन्नाथाय . &
- **Translation**: 

---

### Verse 2 (Nard Puran 224.3102)
- **Original**: .शान्त॑. प्रसन्नददन॑. पीतकौशेयवाससम्‌ । शड्खचक्रगदापकैमूर्तिस्धरुपासितम्‌ ै श्रीनिवासाय भक्तवश्याय शार्किणे । अष्टप्रकृत्यथधीशाय वेधसे । पुण्डरीकनिभाक्षाय योगिने । स्त्याय. सत्यसंधाय बैकुण्ठायाच्युतायः च
- **Translation**: 

---

### Verse 3 (Nard Puran 224.3103)
- **Original**: वामनाय त्रिधातवे । धृतार्चिषे विष्णवे ते3नन्ताय कपिलाय च
- **Translation**: 

---

### Verse 4 (Nard Puran 224.3104)
- **Original**: ऋण्यजु:सामरूपिणे । एकश्ृज्जाय प्रभवे.. विश्वकर्मणे । धूर्भुव:स्वःस्वरूपाय हाव्ययायाक्षराय च । नमस्ते पाहि. मामीश शरणागतबत्सल
- **Translation**: 

---

### Verse 5 (Nard Puran 224.3105)
- **Original**: मणिनूपुरशोभितम्‌। 000 कह 5705-00 सिद्धनिकौ:
- **Translation**: 

---

### Verse 6 (Nard Puran 224.3106)
- **Original**: तुष्टावः मधुसूदनम्‌
- **Translation**: 

---

### Verse 7 (Nard Puran 224.3107)
- **Original**: नमस्ते निभृतात्मने । हरये बाराहतनुधारिणे । नृसिंहाय पृथवे. स्वसुखात्मने
- **Translation**: 

---

### Verse 8 (Nard Puran 224.3108)
- **Original**: नाभेयाय जागद्धात्रे विधात्रेउन्तकराय च
- **Translation**: 

---

### Verse 9 (Nard Puran 224.3109)
- **Original**: पराय च वेद्याय ध्येयाय.. परमात्मने
- **Translation**: 

---

### Verse 10 (Nard Puran 224.3110)
- **Original**: नरनारायणाख्याय.. शिपिविष्टायः विष्णवे
- **Translation**: 

---

### Verse 11 (Nard Puran 224.3111)
- **Original**: ऋतधघाम्ते विधाम्ने च सुपर्णाय स्वरोचिषे
- **Translation**: 

---

### Verse 12 (Nard Puran 224.3112)
- **Original**: ऋभवे सुधाम्ने विश्वाय. सृष्टिस्थित्यन्तकारिणे । यज्ञाय यज्ञभोक्रे च स्थविष्तायाणवे5र्थिने
- **Translation**: 

---

### Verse 13 (Nard Puran 224.3113)
- **Original**: च। ईज्याय साक्षिणेवजाय बहुशीर्षाड्प्निबाहवे
- **Translation**: 

---

### Verse 14 (Nard Puran 224.3114)
- **Original**: । कृष्णाय वेदकर्त्ने च बुद्धकल्किस्वरूपिणे
- **Translation**: 

---

### Verse 15 (Nard Puran 224.3115)
- **Original**: सुब्रताख्याय चाजिताय च
- **Translation**: 

---

### Verse 16 (Nard Puran 224.3116)
- **Original**: ब्रह्मणे5 नन्‍्तशक्तये
- **Translation**: 

---

### Verse 17 (Nard Puran 224.3117)
- **Original**: क्षेत्रज्ञाय विभासिने
- **Translation**: 

---

### Verse 18 (Nard Puran 224.3118)
- **Original**: च श्रवसे शास्त्रयोनये
- **Translation**: 

---

### Verse 19 (Nard Puran 224.3119)
- **Original**: निर्मुणाय. च
- **Translation**: 

---

### Verse 20 (Nard Puran 224.3120)
- **Original**: (ना0 पूर्व0 62। 47-65)
- **Translation**: 

---

