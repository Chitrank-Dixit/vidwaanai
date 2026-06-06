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

### Verse 1 (Sama Ved 0.4241)
- **Original**: सैकड़ों साधनों (हर प्रकार) से हमारी रक्षा करने वाले, वृत्रासुर का हनन करने वाले, सोमपायी हे इन्द्रदेव ! हमारे यज्ञ में आप अवश्य पधारें और शत्रुओं को हम से दूर करें
- **Translation**: 

---

### Verse 2 (Sama Ved 0.4242)
- **Original**: 1660. आ त्वा विशन्त्विन्दव: समुद्रभिव सिन्धवः । न त्वामिन्ध्राति रिच्यते
- **Translation**: 

---

### Verse 3 (Sama Ved 0.4243)
- **Original**: हे इन्रदेव ! समुद्र को प्राप्त होने वाली नदियों की तरह आपको सोमरस प्राप्त हो । अन्य कोई देव आप से उत्तम नहीं है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.4244)
- **Original**: 1669. विव्यक्थ महिना वृषन्भक्ष॑ सोमस्य जागृवे
- **Translation**: 

---

### Verse 5 (Sama Ved 0.4245)
- **Original**: य इन्द्र जठरेषु ते
- **Translation**: 

---

### Verse 6 (Sama Ved 0.4246)
- **Original**: ; हे शक्तिमान्‌, जागरणशील इन्द्रदेव ! आप सोमपान के लिए अपनी ख्याति से सभी स्थानों में व्यापक होते हैं। आपके द्वारा उदरस्थ सोम भी प्रशंसनीय है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.4247)
- **Original**: 1662. अरं त इन्द्र कुक्षये सोमो भवतु वृत्रहन्‌। अरं धामभ्य इन्दव:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.4248)
- **Original**: हे वृत्रहन्ता इन्द्रदेव ! हमारे द्वारा प्रदत्त सोम आपके लिए पर्याप्त हो, आपके साथ-साथ (आपकी प्रेरणा से) सोमरस सभी देवताओं के लिए पर्याप्त हो
- **Translation**: 

---

### Verse 9 (Sama Ved 0.4249)
- **Original**: 1663. जराबोध तद्विविट्टि विशेविशे यज्ियाय । स्तोम॑ रुद्राय दृशीकम्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.4250)
- **Original**: स्तुतियों से प्रदीप्त है अग्निदेव ! प्रत्येक मनुष्य के कल्याण के लिए आप यज्ञ मंडप में प्रकट हों । याजक गण रौद्र अग्निदेव के निमित्त सुन्दर स्तवग्रों को उच्चारित करें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.4251)
- **Original**: 18.2 सामवेट-संहिता 1664.स नो महाँ अनिमानो धूमकेतु: पुरुश्चन्द्र: धिये वाजाय हिन्वतु
- **Translation**: 

---

### Verse 12 (Sama Ved 0.4252)
- **Original**: अपरिमित धूम्र ध्वजा से युक्त, (प्रज्वलित होने वाले) आनन्दप्रद, महान्‌ अग्निदेव, हमें ज्ञान और बैभव की ओर प्रेरित करें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.4253)
- **Original**: 1665. स रेवाँ इव विश्पतिर्देव्य: केतु: शूणोतु नः । उक्थैरग्निर्बृहद्भानु:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.4254)
- **Original**: विश्वपालक, अत्यंत तेजस्वी और ध्वजा सदृश गुणों से युक्त दूरदर्शी अग्निदेव ! आप वैभवशाली राजा के समान हमारी स्तवन रूपी वाणियों को ग्रहण करें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.4255)
- **Original**: 1666. तट्ढो गाय सुते सचा पुरुहताय सत्वने । शं यह्वे न शाकिने
- **Translation**: 

---

### Verse 16 (Sama Ved 0.4256)
- **Original**: हे स्तोताओ ! सोम रस संग्रहित करने के बाद, सर्वस॒हायक और शक्तिमान्‌ इन्द्रदेव के लिए संगठित होकर स्तोत्रों का गान करें । जैसे गौओं को घास सुखप्रद है, वैसे ही इन्द्रदेव को स्तोत्र सुखदायक हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.4257)
- **Original**: 1667. न घा वसुर्नि यमते दान॑ बाजस्य गोमत: । यत्सीमुपश्रवद्विर:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.4258)
- **Original**: सभी के आश्रयदाता वे इन्धदेव, हमारी स्तुतियों को सुनने के बाद, हमें धन-धान्य के रूप में अपार वैभव देने से नहीं रुकते
- **Translation**: 

---

### Verse 19 (Sama Ved 0.4259)
- **Original**: 1668. कुवित्सस्य प्र हि ब्र॒ज॑ गोमन्त॑ दस्युहा गमत्‌ । शचीभिरप नो वरत्‌
- **Translation**: 

---

### Verse 20 (Sama Ved 0.4260)
- **Original**: शत्रुसंहारक इन्द्रदेव दुराचारियों द्वारा चुराई गई गौओं को छुड़ाकर अपने स्वामित्व में लेते हैं और हमें प्रदान करते हैं
- **Translation**: 

---

