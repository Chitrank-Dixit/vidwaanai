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

### Verse 1 (Rig Ved 0.2381)
- **Original**: इन बल सम्पन्न अम्निदेव की देदीप्यमान किरणें सर्वत्र फैल रही हैं, ऐसे वे अग्निदेव हमारे पापों को विनष्ट करें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.2382)
- **Original**: 1082. त्वं हि विश्वतोमुख विश्वतः परिभूरसि। अप नः शोशुचदघम्‌
- **Translation**: 

---

### Verse 3 (Rig Ved 0.2383)
- **Original**: हे सर्वतोमुखी अग्निदेव ! आप निश्चय ही सभी ओर व्याप्त होने वाले हैं, आप हमारे पापों को विनष्ट करें
- **Translation**: 

---

### Verse 4 (Rig Ved 0.2384)
- **Original**: - 1083 द्विषो नो विश्वतोमुखाति नावेब पारय। अप न: शोशुचदघम्‌
- **Translation**: 

---

### Verse 5 (Rig Ved 0.2385)
- **Original**: हे सर्वतोमुखी अग्निदेव ! आप नौका के सदृश सभो शत्रुओं से हमें पार ले जाएँ । आप हमारे पापों को विनष्ट करें
- **Translation**: 

---

### Verse 6 (Rig Ved 0.2386)
- **Original**: 1084 स नः सिन्धुमिव नावयाति पर्षा स्वस्तये । अप न: शोशुचदघम्‌
- **Translation**: 

---

### Verse 7 (Rig Ved 0.2387)
- **Original**: है अग्निदेव ! आप नौका द्वारा नदी के पार ले जाने के समान हिंसक शत्रुओं से हमें पार ले जाएँ । आप हमारे पापों को विनष्ट करें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.2388)
- **Original**: हड0 ऋण्वेद संहिता घाग-9 [ सूक्त - 98 ] [ऋषि - कुत्स आड्रिरस
- **Translation**: 

---

### Verse 9 (Rig Ved 0.2389)
- **Original**: देवता - अग्नि अथवा यैश्वानर- अग्नि
- **Translation**: 

---

### Verse 10 (Rig Ved 0.2390)
- **Original**: छत्द - त्रिष्टप्‌ ।] 1085. वैश्वानरस्थ सुमतौ स्याम राजा हि क॑ भुवनानामभिश्री: । इतो जातो विश्वमिदं वि चा्टे वैश्वानरो यतते सूर्येण
- **Translation**: 

---

### Verse 11 (Rig Ved 0.2391)
- **Original**: हम वैश्वानर अग्निदेव की प्रसन्नता बढ़ाने वाले हों । वे ही स्ूर्ण लोकों के पोषक और सबके द्रष्टा हैं। राजा के सदृश सामर्श्यवान्‌ ये वैश्वानर अग्निदेव सूर्य के समान हो यल करते है.
- **Translation**: 

---

### Verse 12 (Rig Ved 0.2392)
- **Original**: * 1086. पृष्टो दिवि पृष्टो अग्नि: पृथिव्यां पृष्टो विश्वा ओषधीरा विवेश वैश्वानर: सहसा पृष्टो अग्नि: स नो दिवा स रिष: पातु नक्तम्‌
- **Translation**: 

---

### Verse 13 (Rig Ved 0.2393)
- **Original**: ये वैश्वानर अग्निदेव द्युलोक और पृथ्वी लोक में प्रशंसनीय # । ये सम्पूर्ण ओषधियों में व्याप्त होकर प्रशंसा के पात्र हैं। बलों के कारण प्रशंसनीय ये अग्निदेव दिन और रात्रि में हिंसक प्राणियों से हमारी रक्षा करें
- **Translation**: 

---

### Verse 14 (Rig Ved 0.2394)
- **Original**: 1087, वैश्वानर तब तत्सत्यमस्त्वस्मात्रायो मघवान: सचन्ताम्‌। तन्नो मित्रो वरुणो मामहन्तामदिति: सिन्धु: पृथिवी उत दयो:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.2395)
- **Original**: हे वैश्वानर अग्निदेव
- **Translation**: 

---

### Verse 16 (Rig Ved 0.2396)
- **Original**: आपका कार्य सत्य हो । है ऐश्वर्यवान्‌ ! हमें धन युक्त ऐश्वर्य से अभिषूरित करें । हमारे इस निवेदन का मित्र, वरुण, अदिति, सिन्धु, पृथिवी और दयौ आदि देव अनुमोदन करें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.2397)
- **Original**: [ सूक्त - 99 ] [ऋषि-काश्यप मारीच । देवता-अग्नि अथवा-जातवेद अग्नि
- **Translation**: 

---

### Verse 18 (Rig Ved 0.2398)
- **Original**: छन्द-ब्रिष्टप्‌
- **Translation**: 

---

### Verse 19 (Rig Ved 0.2399)
- **Original**: ] 1088. जातवेदसे सुनवाम सोममरातीयतो नि दहाति वेद: । स न: पर्षदति दुर्गाणि विश्वा नावेव सिन्युं दुरितात्यग्नि:
- **Translation**: 

---

### Verse 20 (Rig Ved 0.2400)
- **Original**: हम सर्वज्ञ अग्निदेव के लिए सोम - सवन करें । वे अग्विदेव हमारे रु ओं के सभी धनों को भसमी गत क़रें। नाव द्वारा नदी से पार कराने के समान वे अग्निदेव हमें साूर्ण दूःखों से पार लगाएँ और पापों रक्षित करें
- **Translation**: 

---

