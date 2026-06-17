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

### Verse 1 (Rig Ved 0.161)
- **Original**: इन्द्रदेव, पाँचों श्रेणियों के मनुष्यों (ब्राह्मण, क्षत्रिय, वैश्य, शूद्र और निषाद) और सब ऐश्वर्यों- सम्पदाओं के अद्वितीय स्वामी हैं
- **Translation**: 

---

### Verse 2 (Rig Ved 0.162)
- **Original**: पमं0 1 सू0 8 है 70, इन्द्रं वो विश्वतस्परि हवामहे जनेभ्य:। अस्माकमस्तु केवल:
- **Translation**: 

---

### Verse 3 (Rig Ved 0.163)
- **Original**: हे ऋत्विजो ! हे यजमानो ! सभी लोगों में उत्तम, इन्द्रदेव को, आप सब के कल्याण के लिये हम आमंत्रित करते हैं, वे हमारे ऊपर विशेष कृपा करें
- **Translation**: 

---

### Verse 4 (Rig Ved 0.164)
- **Original**: [ सूक्त - 8 ] [ऋषि- मधुच्छन्दा वैश्वामित्र । देवता- इन्द्र । छन्द- गायत्री 71. एन्द्र सानर्सि रथिं सजित्वानं सदासहम्‌। वर्षिष्ठमूतये भर
- **Translation**: 

---

### Verse 5 (Rig Ved 0.165)
- **Original**: हे इन्धदेव ! आप हमारे जीवन संरक्षण के लिये तथा शत्रुओं को पराभूत करने के निमित्त हमें ऐश्वर्य स पूर्ण करें
- **Translation**: 

---

### Verse 6 (Rig Ved 0.166)
- **Original**: 72. नि येन मुष्टिहत्यया नि यूत्रा रुणधामहै। त्वोतासो न्यर्वता
- **Translation**: 

---

### Verse 7 (Rig Ved 0.167)
- **Original**: उस ऐश्वर्व के प्रभाव और आपके द्वारा रक्षित अश्वों के सहयोग से हम मुक्के का प्रहार करके (शक्ति प्रयोग द्वारा) शत्रुओं को भगा दें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.168)
- **Original**: 73, इन्द्र त्वोतास आ वयं बच्र॑ घना ददीमहि। जयेम स॑ युधि स्पृध:
- **Translation**: 

---

### Verse 9 (Rig Ved 0.169)
- **Original**: हे इन््रदेव ! आपके द्वारा संरक्षित होकर तीक्ष्ण बच्रों को घारण कर हम युद्ध में स्पर्धा करने वाले शत्रुओं पर विजय प्राप्त करें
- **Translation**: 

---

### Verse 10 (Rig Ved 0.170)
- **Original**: 74. बय॑ शूरेभिरस्तृभिरिन्द्र त्ववा युजा वयम्‌। सासह्याम पृतन्यत:
- **Translation**: 

---

### Verse 11 (Rig Ved 0.171)
- **Original**: हे इन्द्रदेव ! आपके द्वारा संरक्षित कुशल शस्त्र-चालक वीरों के साथ हम अपने शत्रुओं को पराजित करें
- **Translation**: 

---

### Verse 12 (Rig Ved 0.172)
- **Original**: 75, महाँ इन्द्र: परश्च नु महित्वमस्तु वज्रिणे। द्योर्न प्रथिना शवः
- **Translation**: 

---

### Verse 13 (Rig Ved 0.173)
- **Original**: हमारे इन्द्रदेव श्रेष्ठ और महान्‌ हैं । वज्रधारी इन्द्रदेब का यश चुलोक के समान व्यापक होकर फैले तथा इनके बल कौ प्रशंसा चतुर्दिक्‌ हो
- **Translation**: 

---

### Verse 14 (Rig Ved 0.174)
- **Original**: 76. समोहे वा य आशत नरस्तोकस्य सनितौ। विप्रासो वा धियायवः
- **Translation**: 

---

### Verse 15 (Rig Ved 0.175)
- **Original**: जो संग्राम में जुटते हैं, जो पुत्र के निर्माण में जुटते हैं और बुद्धिपूर्वक ज्ञान-प्राप्ति के लिए यत्ल करते है, वे सब इन्द्रदेव की स्तुति से इषफल पाते हैं
- **Translation**: 

---

### Verse 16 (Rig Ved 0.176)
- **Original**: 77, यः कुक्षि: सोमपातम: समुद्र इब पिन्वते
- **Translation**: 

---

### Verse 17 (Rig Ved 0.177)
- **Original**: उर्वीरापो न काकुद:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.178)
- **Original**: अत्यधिक सोमपान करने वाले इन्रदेव का उदर समुद्र की तरह विशाल हो जाता है । वह (सोमरस) जोभ से प्रवाहित होने वाले रसों की तरह सतत द्रवित होता रहता है । (सदा आर्द्र बनाये रहता है ।)
- **Translation**: 

---

### Verse 19 (Rig Ved 0.179)
- **Original**: 78. एवा हास्य सूनृता विरप्शी गोमती मही । पकवा शाखा न दाशुधे
- **Translation**: 

---

### Verse 20 (Rig Ved 0.180)
- **Original**: इन्द्रदेव की अति मधुर और सत्यवाणी उसी प्रकार सुख देती है, जिस प्रकार गो घन के दाता और पके फल वाली शाखाओं से युक्त वृक्ष यजमानों (हविदाता) को सुख देते हैं
- **Translation**: 

---

