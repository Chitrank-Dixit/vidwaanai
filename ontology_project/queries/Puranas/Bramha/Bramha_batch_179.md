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

### Verse 1 (Bramha 0.3561)
- **Original**: राजाको बड़ा विस्मय हुआ। उन्होंने उर्वशीसे रद्रकुण्ड, विष्णुकुण्ड, सूर्यकुण्ड, सोमकुण्ड, ब्रह्मकुण्ड,
- **Translation**: 

---

### Verse 2 (Bramha 0.3562)
- **Original**: कहा--'इसको मेंरे पास बुला लाओ।' उर्वशीने कुमारकुण्ड तथा वरुणकुण्ड भी हैं। उस स्थानपर
- **Translation**: 

---

### Verse 3 (Bramha 0.3563)
- **Original**: जाकर राजाका संदेश सुना दिया। सरस्वतीने स्वीकार अप्सरा नामकी नदी गौतमी गड्जामें मिली है। उस
- **Translation**: 

---

### Verse 4 (Bramha 0.3564)
- **Original**: कर लिया तथा अपनी प्रतिज्ञाक अनुसार वह तीर्थके स्मरणमात्रेसे मनुष्य कृतकृत्य हो जाता है।
- **Translation**: 

---

### Verse 5 (Bramha 0.3565)
- **Original**: पुरूरबाके पास आयी। राजाने सरस्वती नदीके तटपर बह सब पापोंका निवारण करनेवाला है। उसके साथ अनेक वर्षोंतक विहार किया। यह देख उससे आगे पुरूरवस्‌ नामक तीर्थ है। उसके
- **Translation**: 

---

### Verse 6 (Bramha 0.3566)
- **Original**: मैंने सरस्वतीको शाप दे दिया। मेरे शापके कारण दर्शनकी तो बात ही क्‍या, स्मरणमात्रसे ही पापोंका
- **Translation**: 

---

### Verse 7 (Bramha 0.3567)
- **Original**: वह मृत्युलोकमें कहीं लुप्त हो गयी है और कहीं नाश हो जाता है। एक समय राजा पुरूरवा
- **Translation**: 

---

### Verse 8 (Bramha 0.3568)
- **Original**: दिखायी देती है। जहाँ सरस्वती नदी गड्जामें मिली ब्रह्माजीकी सभामें गये। यहाँ देवनदी सरस्वती
- **Translation**: 

---

### Verse 9 (Bramha 0.3569)
- **Original**: है, वहाँ पहुँचकर राजा पुरूरवाने तपस्या की और ब्रह्माजीके पास बैठी हँस रही थीं। उस रूपवती
- **Translation**: 

---

### Verse 10 (Bramha 0.3570)
- **Original**: महादेबवजीकी आराधना करके गड्जाजीके प्रसादसे देवीको देखकर राजाने उर्वशीसे पूछा, 'ब्रह्माजीके
- **Translation**: 

---

### Verse 11 (Bramha 0.3571)
- **Original**: सम्पूर्ण अभीष्ट प्रात कर लिया। तबसे उस स्थानका पास यह रूपवती साध्वी स्त्री कौन है ? यह तो
- **Translation**: 

---

### Verse 12 (Bramha 0.3572)
- **Original**: नाम पुरूरवस्तोर्थ, सरस्वती-संगम और ब्रह्मतीर्थ पड़ सबसे सुन्दरी युवती है और अपने सौन्दर्यके
- **Translation**: 

---

### Verse 13 (Bramha 0.3573)
- **Original**: गया। वहाँ सिद्धेश्वर नामसे प्रसिद्ध महांदेवजी' रहते प्रकाशसे इस सभाको उद्दीप्त कर रही है।' उर्वशीने
- **Translation**: 

---

### Verse 14 (Bramha 0.3574)
- **Original**: हैं। वह तीर्थ समस्त कामनाओंको देनेवाला है।
- **Translation**: 

---

### Verse 15 (Bramha 0.3575)
- **Original**: # सुपर्णा-संगम, पुरूरवस्तीर्थ, पद्मतीर्थ, शमीतीर्ध, सोम आदि तीर्थोंकी महिमा * उसके सिवा सावित्री, गायत्री, श्रद्धा, मेधा
- **Translation**: 

---

### Verse 16 (Bramha 0.3576)
- **Original**: कर्णिका-संगम, बैणबी-संगम, कृशरा-संगम, और सरस्वती-ये पाँच पुण्य तीर्थ हैं। वहाँ स्नान
- **Translation**: 

---

### Verse 17 (Bramha 0.3577)
- **Original**: वासवी-संगम, शिवशर्मा, शिखी, कुसुम्भिका, और जलपान करनेसे मनुष्य सब पापोंसे मुक्त हो
- **Translation**: 

---

### Verse 18 (Bramha 0.3578)
- **Original**: उपारथ्या, शान्तिजा, देवजा, अज, बृद्ध, सुर और जाता है। ये पाँचों मेरी कन्याएँ हैं, जो नदीरूपमें
- **Translation**: 

---

### Verse 19 (Bramha 0.3579)
- **Original**: भद्र आदि। ये तथा और भी बहुत-से नद- परिणत हो गयी हैं। जहाँ वे भगवती गड्भासे
- **Translation**: 

---

### Verse 20 (Bramha 0.3580)
- **Original**: नदीगण गौतमीमें मिले हैं। पृथ्वीपर जितने तीर्थ मिली हैं, वहीं पाँच तीर्थ हैं। वे पाँच नदियाँ और
- **Translation**: 

---

