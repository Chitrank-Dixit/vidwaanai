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

### Verse 1 (Rig Ved 0.1121)
- **Original**: 500, यो नः पृषन्नघो वृको दुःशेव आदिदेशति। अप स्म तं पथो जहि
- **Translation**: 

---

### Verse 2 (Rig Ved 0.1122)
- **Original**: हे पूषादेव ! जो हिंसक, चोर, जुआ खेलने वाले हम पर शासन करता चाहते हैं, उन्हें हम से दूर करें
- **Translation**: 

---

### Verse 3 (Rig Ved 0.1123)
- **Original**: हि ऋग्वेद संहिता भाग-9 501. अप त्य॑ परिषन्थिन॑ मुषीवाणं हुरश्चितम्‌। दूरमधि खुतेरज
- **Translation**: 

---

### Verse 4 (Rig Ved 0.1124)
- **Original**: हे पृषादेव ! मार्ग में घ्रात लगाने वाले तथा लुटनेवाले कुटिल चोर को हमारे मार्ग से दूर करके विनष्ट करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.1125)
- **Original**: 502. त्व॑ं तस्य इयाविनो5घशंसस्य कस्य चित्‌। पदाभि तिष्ठ तपुधिम्‌
- **Translation**: 

---

### Verse 6 (Rig Ved 0.1126)
- **Original**: आप हर किसी दुहरी चाल चलने वाले कुटिल हिंसकों के शरीर को पैरों से कुचलकर खड़े हों, अर्धात्‌ उन्हें दबाकर रखें, उन्हें बढ़ने न दें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.1127)
- **Original**: 503. आ तत्ते दख्न मन्तुम: पूषन्नवों वृणीमहे। येन पितृनचोदय:
- **Translation**: 

---

### Verse 8 (Rig Ved 0.1128)
- **Original**: है दुष्टनाशक, मनोषो पृषादेव ! हम अपनी रक्षा के निमित्त आपको स्तुति करते हैं। आपके संरक्षण ने ही हमारे पितरों को प्रवृद्ध किया था
- **Translation**: 

---

### Verse 9 (Rig Ved 0.1129)
- **Original**: 504. अथा नो विश्वसौभग हिरण्यवाशीमत्तम
- **Translation**: 

---

### Verse 10 (Rig Ved 0.1130)
- **Original**: धनानि सुषणा कृधि
- **Translation**: 

---

### Verse 11 (Rig Ved 0.1131)
- **Original**: हे सम्पूर्ण सौभाग्ययुक्त और स्वर्ण - आभूषणों से युक्त पृषादेव ! हमारे लिए सभो उत्तम धन एवं सामरथ्यों को प्रदान करें
- **Translation**: 

---

### Verse 12 (Rig Ved 0.1132)
- **Original**: 505. अति न: सश्वतो नय सुगा न: सुपथा कृणु। पृषन्निह क्रतुं विद:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.1133)
- **Original**: हे पूषादेव ! कुटिल दुष्टों से हमें दूर ले चलें । हमें सुगम-सुप का अवलम्बन प्रदान करें एवं अपने कर्तव्यों का बोध करायें
- **Translation**: 

---

### Verse 14 (Rig Ved 0.1134)
- **Original**: 506. अभि सूयवसं नय न नवज्वारों अध्वने। पृषन्निह क्रतुं विद:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.1135)
- **Original**: हे पृषादेव ! हमें उत्तम जौ (अन्न) वाले देश की ओर ले चले । मार्ग में नवीन संकट न आने पायें । हमें अपने कर्तव्यों का ज्ञान करायें । (हम इन कर्तव्यों को जानें ।)
- **Translation**: 

---

### Verse 16 (Rig Ved 0.1136)
- **Original**: 507, शग्धि पूर्धि प्र यंसि च शिशीहि प्रास्युदरम्‌
- **Translation**: 

---

### Verse 17 (Rig Ved 0.1137)
- **Original**: पृषन्निह क्रतुं विद:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.1138)
- **Original**: हे पृषादेव ! हमें सामर्थ्य दें । हमें धनों से युक्त करें । हमें साधनों से सम्पन्न करें । हमें तेजस्वी बनाएँ । हमारी उदरपूर्ति करें । हम अपने इन कर्त्तव्यों को जानें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.1139)
- **Original**: 508 पृषणं मेथामसि सूक्तैरभि गृूणीमसि। बसूनि दस्ममीमहे
- **Translation**: 

---

### Verse 20 (Rig Ved 0.1140)
- **Original**: हम पूषाटेव को नहीं भूलते । सूक्तों से उनकी स्तुति करते हैं । प्रकाशमान सम्पदा हम उनसे माँगते हैं
- **Translation**: 

---

