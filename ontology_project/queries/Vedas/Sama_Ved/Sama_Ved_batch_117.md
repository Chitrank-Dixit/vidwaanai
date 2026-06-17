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

### Verse 1 (Sama Ved 0.2321)
- **Original**: पवित्रता को प्राप्त होने वाले हे सोमदेव ! आपका शक्तिवर्द्धक एवं तेजस्वी रस सुशोभित होता है । समस्त विश्व में उसकी प्रकाश किरणें दिखाई देती हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2322)
- **Original**: <92.प्र यद्वावों न भूर्णयस्त्वेषा अयासो अक्रमु:। घ्नन्तः कृष्णामप त्वचम्‌
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2323)
- **Original**: : सूर्य की किरणों की तरह तेजस्वों गतिमान्‌ सोम, जो त्वचा की कालिमा दूर करता है, सत्पात्रों में संगृहीत होकर प्रशंसा प्राप्त करता है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2324)
- **Original**: 5.2 सामवेद-संहिता 893.सुवितस्य वनामहे5ति सेतु दुराय्यम्‌। साह्माम दस्युमव्गरतम्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2325)
- **Original**: हे सुख प्रदान करने वाले सोमदेव ! अस्ढा बन्धनों को दूर करने तथा (सत्कर्म से विरत) दुष्कर्म में निरत शत्रुओं का शमन करने के लिए हम आपकी वन्दना करते हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2326)
- **Original**: 894. श्रृण्वे वृष्टेरिव स्वनः पवमानस्य शुष्मिण:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2327)
- **Original**: चरन्ति विद्युतो दिवि
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2328)
- **Original**: पवित्र किये जाते समय (पात्र में गिरती हुई धार से उत्पन) सोम की ध्वनि, वर्षा के समय होने वाली जल की ध्वनि के समान मधुर है । उस तेजस्वी सोम की किरणें आकाश में सर्वत्र फैलती हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2329)
- **Original**: 895.आ पवस्व महीमिषं गोमदिन्दो हिरण्यवत्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2330)
- **Original**: अश्ववत्सोम वीरवत्‌
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2331)
- **Original**: सुपात्र में स्थित हे सोमदेव ! आप अन के भण्डार प्रदान करें, साथ ही साथ पुत्र-पौत्र गौएँ, अश्व एवं स्वर्णादि अपार वैभव भी प्रदान करें
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2332)
- **Original**: 896.पवस्व विश्वचर्षण आ मही रोदसी पृण । उषा: सूर्यो न रश्मिभि:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2333)
- **Original**: उषाकाल के बाद अपनी स्वर्णिम रश्मियों से जगत्‌ को आलोकित करने वाले सूर्यदेव की भाँति हे विश्व द्रष्टा सोमदेव ! अपने तृप्तिदायक पवित्र हुए रस से आप धरती और आकाश को भर दें । (सारे संसार में पवित्रता का संचार करें )
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2334)
- **Original**: 897.परिण: शर्मयन्त्या धारया सोम विश्वत: । सरा रसेव विष्टपम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2335)
- **Original**: हे सोमदेव ! जल से घिरी हुई पृथ्वी की भाँति आप अपनी सुखद रसधार से हमें चारों ओर से घेर लें । (जीवन के प्रत्येक क्षेत्र में आपकी अनुकम्पा से सुखद अनुभूति का लाभ मिले)
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2336)
- **Original**: [ पृश्वी समुद्र से घिरी है, यह ज्ञान वैदिककाल से हो ऋषियों को है।]
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2337)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2338)
- **Original**: के के के
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2339)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2340)
- **Original**: 898.आशुए बृहन्मते परि प्रियेण धाम्ना। यत्रा देवा इति ब्रुवन्‌
- **Translation**: 

---

