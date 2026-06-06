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

### Verse 1 (Bramha 0.1361)
- **Original**: करनेवाले भगवान्‌ भास्करने कल्याणमयी बाणीमें प्रणाम है। सम्पूर्ण देवताओंमें उत्कृष्ट तुम्हारा जो
- **Translation**: 

---

### Verse 2 (Bramha 0.1362)
- **Original**: कहा--' आप लोगोंको कौन-सा वर प्रदान किया रूप वेदवेत्ता पुरुषोंके द्वारा जानने योग्य, नित्य
- **Translation**: 

---

### Verse 3 (Bramha 0.1363)
- **Original**: जाय?' और सर्वज्ञानसम्पन्न है, उसको हमारा नमस्कार
- **Translation**: 

---

### Verse 4 (Bramha 0.1364)
- **Original**: देवताओंने कहा--प्रभो! आपका रूप अत्यन्त है। तुम्हारा जो स्वरूप इस विश्वकी सृष्टि करनेवाला,
- **Translation**: 

---

### Verse 5 (Bramha 0.1365)
- **Original**: तेजोमय है, इसका ताप कोई सह नहीं सकता। विश्वमय, अग्नि एवं देवताओंद्वारा पूजित, सम्पूर्ण
- **Translation**: 

---

### Verse 6 (Bramha 0.1366)
- **Original**: अतः जगत्‌के हितके लिये यह सबके सहने योग्य विश्वमें व्यापक और अचिन्त्य है, उसे हमारा
- **Translation**: 

---

### Verse 7 (Bramha 0.1367)
- **Original**: हो जाय। प्रणाम है। तुम्हारा जो रूप यज्ञ, बेद, लोक तथा
- **Translation**: 

---

### Verse 8 (Bramha 0.1368)
- **Original**: तब 'एबमस्तु' कहकर आदिकर्ता भगवान्‌ धुलोकसे भो परे परमात्मा नामसे विख्यात है,
- **Translation**: 

---

### Verse 9 (Bramha 0.1369)
- **Original**: सूर्य सम्पूर्ण लोकॉंके कार्य सिद्ध करनेके लिये उसको हमारा नमस्कार है। जो अविज्ञेय, अलक्ष्य,
- **Translation**: 

---

### Verse 10 (Bramha 0.1370)
- **Original**: समय-समयपर गर्मी, सर्दी और वर्षा करने लगे। * आदिदेखोडइसि. देवातामैश्वर्याच्च त्वमीश्वर:। आदिकर्तांस भूतानां. देवदेयों दिवाकर:
- **Translation**: 

---

### Verse 11 (Bramha 0.1371)
- **Original**: जीवन: सर्वधूतानां. देवगन्धर्वरक्षसाम्‌
- **Translation**: 

---

### Verse 12 (Bramha 0.1372)
- **Original**: मुतिकिन्नरसिद्धानां तथैयोरगपक्षिणाम्‌
- **Translation**: 

---

### Verse 13 (Bramha 0.1373)
- **Original**: त्वं ब्रह्मा त्व॑ महादेवस्त्वं॑ विष्णुस्त्व॑ प्रजापति:। वायुरित्द्रश्व सोमक्ष॒विवस्वान्‌ू वरुणस्तथा
- **Translation**: 

---

### Verse 14 (Bramha 0.1374)
- **Original**: त्व॑ काल: सुष्टिकर्ता च हर्ता भर्ता तथा प्रधु;। सरितः: सागरा: शैला विधयुदिन्द्रधनूंपि च
- **Translation**: 

---

### Verse 15 (Bramha 0.1375)
- **Original**: प्रलय: प्रभवश्षैव व्याव्यक्त: सनातनः:। ईश्वरात्पततो विद्या विद्याया: परत: शिवः
- **Translation**: 

---

### Verse 16 (Bramha 0.1376)
- **Original**: त्स्य ते सुरसिद्धगणैजुं््े भूग्वत्रिपुलहादिभि:। स्तुत॑ परममव्यक्त यद्ूपं तस्यथ ते समःआ बेद्यं बेदविदां नित्य सर्वज्ञानसमन्यितम्‌ । सर्वदेवादिदेवस्थ यद्रूप॑ तस्य ते नमः
- **Translation**: 

---

### Verse 17 (Bramha 0.1377)
- **Original**: विश्वकृद्धिश्व भूतं चच अैश्वासरसुराधथितम्‌ । विश्वस्थितमचिन्त्ये थ. यद्र्॒प तस्य ते नमः #
- **Translation**: 

---

### Verse 18 (Bramha 0.1378)
- **Original**: पर सनज्ञात्परे वेदात्पर॑ लोकात्पर॑ दिव:। परमात्मेत्यभिख्यातं यद्रुप॑ तस्थ ते नमः
- **Translation**: 

---

### Verse 19 (Bramha 0.1379)
- **Original**: अविज्ञेपमनालश्ष्यमध्यानगतमब्ययम्‌ । अनादिनिधन॑ चैव यद्गर्पं तस्थ ते नमः
- **Translation**: 

---

### Verse 20 (Bramha 0.1380)
- **Original**: नपो नम्त; कारणकारणाय नमो नम: पापविमोचनाय । नमो नमस्ते दितिजारदनाथ नमो नमो रोगविमोचताय
- **Translation**: 

---

