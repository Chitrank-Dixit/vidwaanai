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

### Verse 1 (Rig Ved 0.641)
- **Original**: 286. दर्श नु विश्वदर्शत दर्श रथमधि क्षमि। एता जुघत मे गिर:
- **Translation**: 

---

### Verse 2 (Rig Ved 0.642)
- **Original**: दर्शन योग्य वरुणदेव को उनके रथ के साथ हमने भूमि पर देखा है । उन्होंने हमारी स्तुतियाँ स्वीकारी हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.643)
- **Original**: 287 इम॑ में वरुण श्रुधी हवमद्या च मृठय। त्वामवस्युरा चके
- **Translation**: 

---

### Verse 4 (Rig Ved 0.644)
- **Original**: है वरुणदेव ! आप हमारी प्रार्थना पर ध्यान दें, हमें सुखी बनायें । अपनी रक्षा के लिए हम आपकी स्तुति करते हैं
- **Translation**: 

---

### Verse 5 (Rig Ved 0.645)
- **Original**: पं0 1 सू0 26 33 288. त्वं विश्वस्य मेधिर दिवश्च ग्मक्ष राजसि। स यामनि प्रति श्रुधि
- **Translation**: 

---

### Verse 6 (Rig Ved 0.646)
- **Original**: है मेधावी वरुणदेव ! आप द्युलोकु भूलोक और सारे विश्वपर आधिपत्य रखते हैं, आप हमारे आवाहन को स्वीकार कर 'हम रक्षा करेंगे- ऐसा प्रत्युत्तर प्रदान करें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.647)
- **Original**: 289. उदुत्तमं मुमुग्धि नो वि पाशं मध्यम॑ चूत। अवाधमानि जीवसे
- **Translation**: 

---

### Verse 8 (Rig Ved 0.648)
- **Original**: है वरुणदेव ! हमारे उत्तम (ऊपर के) पाश को खोल टें, हमारे मध्यम पाश को काट दें और हमारे नीचे के पाश को हटाकर हमें उत्तम जीवन प्रदान करें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.649)
- **Original**: [सूक्त-26 ] [ऋषि -शुनःशेप आजीगर्ति (कृत्रिम देवरात वैश्वामित्र )
- **Translation**: 

---

### Verse 10 (Rig Ved 0.650)
- **Original**: देवता-अग्नि
- **Translation**: 

---

### Verse 11 (Rig Ved 0.651)
- **Original**: छन्द-गायत्री । ] 290, वसिष्वा हि मियेध्य वस््राण्यू्जा पते। सेम॑ नो अध्वर॑ यज
- **Translation**: 

---

### Verse 12 (Rig Ved 0.652)
- **Original**: हे यज्ञ योग्य, (हवियोग्य) अननों के पालक अभ्निदिव ! आप अपने तेजरूप वस्तरों को पहनकर हमारे यज्ञ को सम्पादित करें
- **Translation**: 

---

### Verse 13 (Rig Ved 0.653)
- **Original**: 291. नि नो होता वरेण्य: सदा यविष्ठ मन्मभि:। अग्ने दिवित्मता बच:
- **Translation**: 

---

### Verse 14 (Rig Ved 0.654)
- **Original**: सदा तरुण रहने वाले हे अग्निदेव ! आप सर्वोत्तम होता (यज्ञ सम्पन कर्त्ता ) के रूप में यज्ञकुण्ड में स्थापित होकर यजमान के स्तुति वचनों का श्रवण करें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.655)
- **Original**: 292. आ हि ध्मा सूनवे पितापिर्यजत्यापये । सखा सख्ये वरेण्य:
- **Translation**: 

---

### Verse 16 (Rig Ved 0.656)
- **Original**: है बरण करने योग्य अग्निदेव ! जैसे पिता अपने पुत्र के, भाई अपने भाई के और मित्र अपने मित्र के सहायक होते हैं, वैसे हो आप हमारी सहायता करें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.657)
- **Original**: 293. आ नो बहीं रिशादसो वरुणो मित्रो अर्यमा। सीदन्तु मनुघो यथा
- **Translation**: 

---

### Verse 18 (Rig Ved 0.658)
- **Original**: जिस प्रकार प्रजापति के यज्ञ में “मनु" आकर शोभा बढ़ाते हैं, उसी प्रकार शत्रुनाशक वरुणदेव, मित्र- देव एवं अर्यमादेव हमारे यज्ञ में आकर विराजमान हों
- **Translation**: 

---

### Verse 19 (Rig Ved 0.659)
- **Original**: 294 पूर्व्य होतरस्थ नो मन्दस्व सख्यस्थ च। डमा उ घु श्रुधी गिर:
- **Translation**: 

---

### Verse 20 (Rig Ved 0.660)
- **Original**: पुरातन होता है अग्निदेव ! आप हमारे इस यज्ञ से और हमारे मित्रभाव से प्रसल हों और हमारी स्तुतियों को भली प्रकार सुनें
- **Translation**: 

---

