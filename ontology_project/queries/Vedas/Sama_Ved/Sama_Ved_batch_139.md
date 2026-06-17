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

### Verse 1 (Sama Ved 0.2761)
- **Original**: 1069. ते स्थाम देव वरुण ते मित्र सूरिभि: सह। डषं स्वश्न धीमहि
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2762)
- **Original**: हे वरुणदेव ! ज्ञानवानों के साथ आपको स्तुति करते हुए हम वैभवयुक्त हों । हे मित्र ! आपकी स्तुति से हम अन्न, धन और स्वर्गोपम सुखों को प्राप्ति करें
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2763)
- **Original**: 1070. भिन्थि विश्वा अप द्विष: परि बाधो जही मृथ: । वसु स्पाहँ तदा भर
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2764)
- **Original**: हे इन्रदेव ! आप सभी दुरात्माओं का संहार करें । श्रेष्ठकर्मों के अवरोधक शत्रुओं का विनाश करें और इच्छित धन से हमें युक्त करें
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2765)
- **Original**: 1071.यस्य ते विश्वमानुषम्पूरेर्दत्तस्य वेदति । वसु स्पाहँ तदा भर
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2766)
- **Original**: हे इन्द्रदेव ! आप द्वारा प्रदत्त जिस वैभव को सभी मानव उचित ढंग से जानते हैं, उस वाड्छित ऐश्वर्य को हमें पर्याप्त मात्रा में प्रदान करें
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2767)
- **Original**: 1072. यद्वीडाविन्द्र यत्स्थिरे यत्पर्शाने पराभृतम्‌ । बसु स्पाहँ तदा भर
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2768)
- **Original**: हे इन्द्रदेव ! सुरक्षित अभेद्य कोष में रखे गये, स्थिर स्थान पर रखे गये, किसी के स्पर्श से मुक्त स्थान पर रखे गये तथा शत्रुओं पर विजय प्राप्त करके लाये गये; ऐसे सभी धन को जो हमारे द्वारा वांछनीय है, हमें पर्याप्त मात्रा में उपलब्ध कराएँ
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2769)
- **Original**: 1073.यज्ञस्थ॒ हि स्थ तऋषद्धत्विजा सस्‍्नी वाजेषु कर्मसु । इन्द्राग्गी तस्य बोधतम्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2770)
- **Original**: हे इन्द्राग्न ! आप ही यज्ञ के कऋ्त्विज्‌ हैं । युद्ध की तरह यज्ञ कर्मों में भी आपकी पवित्रता रहती है; अतएव हमारी प्रार्थना के अभिष्राय को दृष्टिगत रख करके आप स्वीकारें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2771)
- **Original**: 1074.तोशासा रथयावाना वृत्रहणापराजिता
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2772)
- **Original**: इन्द्राग्नी तस्थ बोधतम्‌
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2773)
- **Original**: हे इन्र और अग्निदेव ! आप शत्रुहनन कर्त्ता, रथ से यात्रा करने वाले, घेरा डालने वाले दुष्टों के संहारक और कभी परास्त न होने वाले हैं; ऐसे आप हमारी स्तुति को स्वीकार करें
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2774)
- **Original**: 1075, इर्द वां मदिरं मध्वधुक्षनद्रिभिर्नर: । इन्द्राग्नी तस्य बोधतम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2775)
- **Original**: हे इन्द्राग्ने ! ऋत्विजों ने आपके लिए आनन्दप्रद मधुर सोमरस तैयार किया है । इसके लिए आप हमारी प्रार्थना स्वीकार करें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2776)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2777)
- **Original**: 7.6 सापवेद-संहिता
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2778)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2779)
- **Original**: 1076. इन्द्रायेन्दो मरुत्वते पवस्व मधुमत्तम:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2780)
- **Original**: अर्कस्य योनिमासदम्‌
- **Translation**: 

---

