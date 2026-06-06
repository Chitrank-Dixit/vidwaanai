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

### Verse 1 (Rig Ved 0.10401)
- **Original**: है अभ्देव ! आप अपनी प्रज्वलित , तीक्ष्ण ज्वालाओं से विष्नकारक तत्त्वों (शत्रुओं ) को नष्ट करें और जो आपकी उपासना तथा स्तुति करते है, उनको बल एबं ऐश्वर्य प्रदान करें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.10402)
- **Original**: 4522, सुबीरं रयिमा भर जातवेदो विचर्षणे
- **Translation**: 

---

### Verse 3 (Rig Ved 0.10403)
- **Original**: जहि रक्षांसि सुक्रतों
- **Translation**: 

---

### Verse 4 (Rig Ved 0.10404)
- **Original**: हे सर्वज्ञाता अग्निदेव ! आप दुष्टों का संहारकर , हमें श्रेष्ठ सन्तानयुक्त ऐश्वर्य प्रदान करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.10405)
- **Original**: 4523 त्व॑ न: पाह्मंंहसो जातवेदों अधायत: । रक्षा णो ब्रह्मणस्कवे
- **Translation**: 

---

### Verse 6 (Rig Ved 0.10406)
- **Original**: है ज्ञानी अग्निदेव ! आप ज्ञान के द्रष्टा हैं। आप पाप और पापी शत्रुओं से हमारी रक्षा करें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.10407)
- **Original**: 4524. यो नो अग्ने दुरेव आ मर्तों वधाय दाशति। तस्मान्न: पाह्म॑ंहस:
- **Translation**: 

---

### Verse 8 (Rig Ved 0.10408)
- **Original**: है अग्निदेव ! आप हमें उस मनुष्य से बचाएँ, जो दुर्भावनापूर्वक हमें मारने के लिए प्रयलल करता है । पापों 'से भी हमारी रक्षा करें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.10409)
- **Original**: 4525, त्वं त॑ देव जिद्नया परि बाधस्व दुष्कृतम्‌
- **Translation**: 

---

### Verse 10 (Rig Ved 0.10410)
- **Original**: मर्तों यो नो जिघांसति
- **Translation**: 

---

### Verse 11 (Rig Ved 0.10411)
- **Original**: है अग्निदेव
- **Translation**: 

---

### Verse 12 (Rig Ved 0.10412)
- **Original**: आप अपनो तेजस्विता बढ़ाकर उनका संहार करें, जो दुष्ट हमें मारने का अभिप्राय रखते हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.10413)
- **Original**: 32 4526. भरद्वाजाय सप्रथ: शर्म यच्छ सहन्त्य । अग्ने वरेण्यं बसु
- **Translation**: 

---

### Verse 14 (Rig Ved 0.10414)
- **Original**: है अग्निदेव !आप तेजस्वी हैं, आप भरद्वाज को सब प्रकार का यशस्बी निवास प्रदान करें तथा श्रेष्ठ धन दें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.10415)
- **Original**: 4527, अम्निर्वत्राणि जड्घनदद्रविणस्युर्विपन्यया। समिद्ध: शुक्र आहुत:
- **Translation**: 

---

### Verse 16 (Rig Ved 0.10416)
- **Original**: सत्पयास्ों से प्रसन्न होकर याजकों को प्रसन्नता प्रदान करने वाले हे प्रदीग्त अग्निदेव ! हमें बन्धन में रखने वाली दुष्ट वृत्तियों का विनाश करें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.10417)
- **Original**: पं0 6 सू0 16 23 4528, गर्भे मातु: पितुष्पिता विदिद्युतानों अक्षरे। सीदब्नृतस्य योनिमा
- **Translation**: 

---

### Verse 18 (Rig Ved 0.10418)
- **Original**: पृथ्वों माता के गर्भ में विशेष रूप से देदोप्यमान एवं अन्तरिक्ष में संरक्षक की भूमिका में नियुक्त अभ्तिदेव यज्ञवेदी पर विराजमान हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.10419)
- **Original**: 4529. ब्रह्म प्रजावदा भर जातवेदो विचर्षणे। अग्ने यद्दीदयद्धिवि
- **Translation**: 

---

### Verse 20 (Rig Ved 0.10420)
- **Original**: सब जानने वाले दिव्य-द्रष्टा, हे अग्निदेव ! अन्तरिक्षलोक में देवों को प्राप्त सुख , ऐश्वर्य एवं सन्‍्तान आदि से हमें भी सम्पन्न करें
- **Translation**: 

---

