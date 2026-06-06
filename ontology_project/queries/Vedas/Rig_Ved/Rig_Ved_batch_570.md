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

### Verse 1 (Rig Ved 0.11381)
- **Original**: जिनका धन अविनाश हैं, ऐसे पूषन्‌देव से हम धन को याचना करते हैं । वे प्रार्थना सुनकर हमारी दरिद्रता को दूर कर दें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.11382)
- **Original**: 4953, पूषन्तव ब्रते वय॑ न रिष्येम कदा चन। स्तोतारस्त इह स्मसि
- **Translation**: 

---

### Verse 3 (Rig Ved 0.11383)
- **Original**: हे पूषगदेव ! आपका यजन करते हुए, आपकी स्तुति करने वाले हम सब कभी नष्ट न हों, प्रत्युत पहले की तरह ही सुरक्षित रहें
- **Translation**: 

---

### Verse 4 (Rig Ved 0.11384)
- **Original**: 4954. परि पूषा परस्ताद्धस्तं दधातु दक्षिणम्‌। पुनर्नों नष्टमाजतु
- **Translation**: 

---

### Verse 5 (Rig Ved 0.11385)
- **Original**: हे पूषन्‌देव ! आप हमारे गो-धन को कुमा्गगामी होकर नष्ट होने से बचाएँ और अपहृत हुए गो-धन को पुन: प्राप्त कराएँ
- **Translation**: 

---

### Verse 6 (Rig Ved 0.11386)
- **Original**: [ सूक्त - 55 ] [ऋषि - भरद्वाज वा्हस्पत्य । देवता -पृषा ! छत्द - गायत्री ।] 4955, एहि वां विपुचो नपादाघृणे सं सचावहै । रथधीर्ऋतस्य नो भव
- **Translation**: 

---

### Verse 7 (Rig Ved 0.11387)
- **Original**: हे पूषन्देव ! आपको स्तुति करने वाले स्तोता और आपका यज़न करने वाले हम, दोनों मिलकर रहेंगे । आप हमारे पास आएँ और बज्ञ कर्म का नेतृत्व करें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.11388)
- **Original**: 4956, रथीतमं कपर्दिनमीशानं राधसों मह:
- **Translation**: 

---

### Verse 9 (Rig Ved 0.11389)
- **Original**: राय: सखायमीमहे
- **Translation**: 

---

### Verse 10 (Rig Ved 0.11390)
- **Original**: मस्तक पर केश हैं जिनके, ऐसे महारथी योद्धा, धन के स्वामी, जो हमारे सखा हैं, उन पूषन्‌देव से हम धन की याचता करते हैं
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11391)
- **Original**: 4957. रायो थारास्याघृणे वसो राशिरजाश्व । धीवतोधीबत: सखा
- **Translation**: 

---

### Verse 12 (Rig Ved 0.11392)
- **Original**: है अजरूपी अश्न वाले देव ! आप धन के प्रबाह एवं ऐश्वर्य की राशि हैं । आप स्तुति करने वाले स्तोताओं के मित्र हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.11393)
- **Original**: 4958. पृषणं न्व1जाश्रमुप स्तोषाम वाजिनम्‌ । स्वसुर्यों जार उच्यते
- **Translation**: 

---

### Verse 14 (Rig Ved 0.11394)
- **Original**: <0 ऋण वेद संहिता भाग - 2 अश्व एवं झग (बकरी) जिनके याहन हैं, उन पूषादेव की हम स्तुति करते हैं। वे पृषादेव उषा के स्वामी कहलाते हैं
- **Translation**: 

---

### Verse 15 (Rig Ved 0.11395)
- **Original**: 4959, मातुर्दिथ्िषुमब्रव॑ स्वसुर्जार: शृणोतु नः । भ्रातेद्धस्थ सखा मम
- **Translation**: 

---

### Verse 16 (Rig Ved 0.11396)
- **Original**: वे पूषादेव जो उषा के पति सूर्यदेव एवं इन्द्रदेव के भाई और हमारे सखा हैं, उन रात्रि माता के सहचर को हम स्तुति करते हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.11397)
- **Original**: 4960. आजास: पृषणं रथे निशृम्भास्ते जनश्रियम्‌। देव॑ वहन्तु बिशभ्रत:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.11398)
- **Original**: लोगों को वैभवशाली बनाने वाले पृषादेव को, रथ में जुते छाग, रथ को खींचकर यहाँ (यज्ञशाला में) लाएँ
- **Translation**: 

---

### Verse 19 (Rig Ved 0.11399)
- **Original**: [ सूक्त - 56 ] [ऋषि - भरद्वाज बा्हस्पत्य । देवता -पृषा । छन्द - गायत्री, 6 अनुष्ट॒प्‌
- **Translation**: 

---

### Verse 20 (Rig Ved 0.11400)
- **Original**: ] 4961. य एनमादिदेशति करम्भादिति पृषणम्‌ । न तेन देव आदिशे
- **Translation**: 

---

