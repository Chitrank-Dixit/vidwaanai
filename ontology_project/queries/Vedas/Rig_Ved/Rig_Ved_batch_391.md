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

### Verse 1 (Rig Ved 0.7801)
- **Original**: 3397. सं यत्त इन्द्र मन्‍्यव: सं चक्राणि द्धन्विरे । अध त्वे अध सूर्य
- **Translation**: 

---

### Verse 2 (Rig Ved 0.7802)
- **Original**: हे इन्द्रदेव ! जब हम आपकी प्रार्थना करते है, तब वे प्रार्थनाएँ चक्र के सदूश आपकी ओर गमन करती हैं । वे प्रार्थनाएँ सर्वप्रथम आपके समोप जाती हैं, बाद में सूर्यदेव के समीप गमन करती हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.7803)
- **Original**: 3398. उत समा हि त्वामाहुरिन्मघवानं शचीपते
- **Translation**: 

---

### Verse 4 (Rig Ved 0.7804)
- **Original**: दातारमविदीधयुम्‌
- **Translation**: 

---

### Verse 5 (Rig Ved 0.7805)
- **Original**: शक्तियों के स्वामी हे इन््रदेव ! स्तोतागण आपको ऐश्वर्यवानू, धन प्रदायक तथा तेजस्वी कहते हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.7806)
- **Original**: 3399. उत समा सद्य इत्परि शशमानाय सुन्यते
- **Translation**: 

---

### Verse 7 (Rig Ved 0.7807)
- **Original**: पुरू चिन्मंहसे बसु
- **Translation**: 

---

### Verse 8 (Rig Ved 0.7808)
- **Original**: है इद्धदेव ! स्तुति करने वालों तथा सोम अभिषव करने वालों को आप शीघ्र ही भ्रचुर ऐश्वर्य प्रदान करते हैं
- **Translation**: 

---

### Verse 9 (Rig Ved 0.7809)
- **Original**: 3400. नहि ध्मा ते शर्त चन राधो वरन्त आमुर:। न च्यौत्लानि करिष्यतः
- **Translation**: 

---

### Verse 10 (Rig Ved 0.7810)
- **Original**: हे इन्द्रदेव ! आपके सैकड़ों प्रकार के ऐश्वर्य को हिंसा करने वाले शत्रु नहीं प्राप्त कर सकते । रिपुओं का विनाश करने वाली आपकी सामर्थ्य को वे रोक नहीं सकते
- **Translation**: 

---

### Verse 11 (Rig Ved 0.7811)
- **Original**: 3401, अस्माँ अवन्तु ते शतमस्मान्सहस्रमूतय: । अस्मान्विश्वा अभिष्टयः
- **Translation**: 

---

### Verse 12 (Rig Ved 0.7812)
- **Original**: हे इद्धदेव ! आपके सैकड़ों रक्षण-साधन हमारी सुरक्षा करें, आपके सहस्नों रक्षण-साधन हमारी सुरक्षा करें और आपकी समस्त प्रेरणाएँ हमारी सुरक्षा करें
- **Translation**: 

---

### Verse 13 (Rig Ved 0.7813)
- **Original**: 3402. अस्माँ इहा वृणीष्य सख्याय स्वस्तये । महो राये दिवित्मते
- **Translation**: 

---

### Verse 14 (Rig Ved 0.7814)
- **Original**: है इद्धदेब ! आप हमें अपनी मित्रता की छत्रछाया में रखकर हमारा कल्याण करें तथा हम याजकों को तेजस्वी वैभव प्रदान करें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.7815)
- **Original**: 3403. अस्माँ अविड्डि विश्वहेन्द्र राया परीणसा। अस्मान्विश्वाभिरूतिभि:
- **Translation**: 

---

### Verse 16 (Rig Ved 0.7816)
- **Original**: है इन्द्रदेव ! आप अपने महान्‌ धर्नों तथा सम्पूर्ण रक्षण-साथर्नों द्वारा प्रतिदिन हमारी सुरक्षा करें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.7817)
- **Original**: 3404 अस्मभ्यं ताँ अपा वृधि वजाँ अस्तेव गोमत: । नवाभिरिद्धोतिभि:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.7818)
- **Original**: हे इन्द्रदेव ! जिस प्रकार वीर मनुष्य गृह-द्वार को खोलते हैं, उसी प्रकार आप हम मनुष्यों के निमित्त गौओं के गोष्ठ को खोलें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.7819)
- **Original**: 3405, अस्माक॑ धृष्णुया रथो द्युमाँ इद्धानपच्युत: । गव्युरश्चयुरीयते
- **Translation**: 

---

### Verse 20 (Rig Ved 0.7820)
- **Original**: हे इन्धदेव ! आप हमारे रिपुओं को परास्त करने वाले, अत्यधिक तेज वाले, विनष्ट न होने वाले तथा गौओं (किरणों) से युक्त हैं। आप अभ्रों से युक्त रथ द्वारा सर्वत्र गमन करने वाले हैं । आप उस रथ के साथ हम याजकों की सुरक्षा करें
- **Translation**: 

---

