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

### Verse 1 (Rig Ved 0.6461)
- **Original**: साधकों की मनोकामनाओं को पूर्ण करने वाले हे इन्द्रदेब ! अभिषुत सोम का पान करने के निमित्त हम आपका आवाहन करते हैं। आप अत्यन्त मधुर हविष्यात्र युक्त सोम का पान करें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.6462)
- **Original**: 2832. इन्द्र क्रतुविदं सुत्ं सोम॑ हर्य पुरुष्ठत
- **Translation**: 

---

### Verse 3 (Rig Ved 0.6463)
- **Original**: पिबा वृषस्व तातृपिम्‌
- **Translation**: 

---

### Verse 4 (Rig Ved 0.6464)
- **Original**: है हरि संज्ञक अश्वों के स्वामी और बहुवों द्वारा प्रशंसित इन््रदेव ! आप अभीष्टवर्षक हैं। यह अभिषुत सोम आपको तृप्त करने के लिए इस यज्ञ में विधिवत्‌ तैयार किया गया है । आप इसका पान करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.6465)
- **Original**: 2833. इन्द्र प्र णो धितावान यज्ञ विश्वेभिदेंवेभि: । तिर स्तवान विश्पते
- **Translation**: 

---

### Verse 6 (Rig Ved 0.6466)
- **Original**: हे स्तृत्य और प्रजापालक इन्द्रदेव ! आप सम्पूर्ण पूजनीय देवों के साथ हमारे इस हतव्यादि द्रव्यों से पूर्ण यज्ञ को संवर्द्धित करें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.6467)
- **Original**: 2834 इन्द्र सोमा: सुता इमे तब प्र यन्ति सत्पते। क्षय॑ चन्द्रास इन्दव:
- **Translation**: 

---

### Verse 8 (Rig Ved 0.6468)
- **Original**: हे सत्यव्रतियों के अधिपति इद्धदेव ! ये दीप्तियुक्त, आह्वादक और अभिषुत सोमरस आपके स्थान की ओर उन्मुख है (अर्थात्‌ आपको समर्पित है) , इसे ग्रहण करें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.6469)
- **Original**: 2835. द्िष्वा जठरे सुतं सोपमिन्द्र वरेण्यम्‌
- **Translation**: 

---

### Verse 10 (Rig Ved 0.6470)
- **Original**: तब द्युक्षास इन्दव:
- **Translation**: 

---

### Verse 11 (Rig Ved 0.6471)
- **Original**: है इद्धदेव ! यह अभिषुत सोम आपके द्वारा वरण करने योग्य है; क्योंकि यह दीप्तिमान्‌ और आपके पास स्वर्ग में रहने योग्य है । आप इसे अपने उदर में धारण करें
- **Translation**: 

---

### Verse 12 (Rig Ved 0.6472)
- **Original**: 2836. गिर्वण: पाहि नः सुत॑ मधोर्धाराभिरज्यसे । इन्द्र त्वादातमिद्यश:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.6473)
- **Original**: में0 3 सु0 ढेर? 59 हे स्तुत्य इन्द्रदेव ! हमारे द्वारा शोधित सोमरस का आप पान करें, क्योंकि इस आनन्ददायी सोमरस की धाराओं से आप सिंचित होते हैं । हे इन्द्रदेव
- **Translation**: 

---

### Verse 14 (Rig Ved 0.6474)
- **Original**: ! आपकी कृषा से ही हमें यश मिलता है
- **Translation**: 

---

### Verse 15 (Rig Ved 0.6475)
- **Original**: 2837, अभि दुम्नानि वनिन इन्ध सचन्ते अक्षिता। पीत्वी सोमस्य वावृधे
- **Translation**: 

---

### Verse 16 (Rig Ved 0.6476)
- **Original**: देवपूजक यजमान के द्वारा समर्पित दीप्तिमान्‌ और अक्षय सोमादियुक्त हवियाँ इन्द्रदेव की ओर जाती हैं । इस सोम को पीकर इद्धदेव विकसित होते हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.6477)
- **Original**: 2838. अर्वावतों न आ गहि परावतश्च वृत्रहन्‌। इमा जुषस्व नो गिर:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.6478)
- **Original**: हे वृत्रहन्ता इन्द्रदेव ! आप समीपस्थ स्थान से हमारे पास आयें । दूरस्थ स्थान से भी हमारे पास आयें । हमारे द्वारा समर्पित इन स्तुतियों को ग्रहण करें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.6479)
- **Original**: 2839. यदन्तरा परावतमर्वावतं च हूयसे । इन्द्रेह तत आ गहि
- **Translation**: 

---

### Verse 20 (Rig Ved 0.6480)
- **Original**: है इन्द्रदेव ! आप दूरस्थ टेश से, समीपस्थ देश से तथा मध्य के प्रदेशों से बुलाये जाते हैं, उन स्थानों से आप हमारे यज्ञ में आयें
- **Translation**: 

---

