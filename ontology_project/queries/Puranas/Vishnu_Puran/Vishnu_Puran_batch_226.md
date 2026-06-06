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

### Verse 1 (Vishnu Puran 0.4501)
- **Original**: 1 नगरस्य बहिः सो3थ निदाघं ददुशे मुनि:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4502)
- **Original**: महाबलपरीवारे पुरे बिशति पार्थिवे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4503)
- **Original**: 2 ब्राह्मण . बोले--हे नरेश्वर ! तदनन्तर सहस्र वर्ष व्यतीत होनेपर महर्षि ऋभु निदाघ्को ज्ानोपदेश करनेके लिये फिर उसो नगरकोे गये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4504)
- **Original**: वहाँ पहुँचनेपर उन्होंने देखा कि वहाँका राजा बहुत-सी सेना आदिके साथ बड़ी ध्रुम-धघामसे नगरमें प्रवेश कर
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4505)
- **Original**: 160 दूरे स्थितं महाभागं जनसम्मर्टवर्जकम्‌। क्षुतक्षापकण्ठपायान्तमरण्यात्ससमित्कुशम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4506)
- **Original**: हे दृष्ठा निदाघ॑ से ऋभुरुपगम्याभिवाद्य च। उदाच कस्मादेकात्ते स्थीयते भवता द्विज
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4507)
- **Original**: 4 निदाष उयाच भ्रो बिप्र जनसम्मदों महानेष नरेश्वर:। प्रविविश्लु: पुरं रम्ये तेनात्र स्थीयते मया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4508)
- **Original**: 5 ऋषुरुताच नराधिपो5त्र कतप: कतमझेतरों जनः । कथ्यतां मे द्विजश्रेष्ठ त्वमभिज्ञो मतो मम ।। 6 निदाघ उनाच योड्य॑ गजेन्वमुन्मत्तमद्रिधृज्ल्‍समुच्छितम्‌ । अधिरूलोे नरेन्‍द्रोड्यं परिलोकस्तथेतरः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4509)
- **Original**: 7 ऋषुसुयाच एतौ हि गजराजानौं युगपद्र्शितो मम। भवता न विशेषेण पृथक्चिटह्रोपलक्षणो
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4510)
- **Original**: 8 तत्कथ्यतां महाभाग विशेषो भवतानयो: । ज्ञातुमिच्छाप्यह कोउनञ्न गज: को वा नराधिप:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4511)
- **Original**: 9 निदाच तयाच गजो योउयमथो ब्रह्मान्नुपर्यस्थैय भूपति: । वाह्मवाहकसम्बन्ध को न जानाति वै द्विज
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4512)
- **Original**: 10 ऋभुख्वाच जानाम्यहं यथा ब्रह्मास्तथा मामवलोधय ।
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4513)
- **Original**: अथ:शब्दनिगद्यं हि कि चोर्ध्वमभिधीयते
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4514)
- **Original**: 11 ब्राह्मण उवात्त इत्युक्त: सहसारुद्धा निदाघः प्राह तमृभुम्‌। श्रूयतां कथयाम्थेष यन्प्रां त्व॑ परिपृच्छसि
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4515)
- **Original**: 12 उपर्यह यथा राजा त्वमथः कुझरों यथा। अवबोधाय ते ब्रह्नन्दृष्टान्तो दर्शितों मया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4516)
- **Original**: 13 ऋषभुरुवाच ते राजेव ट्विजश्रेष्ठ स्थितोईःह गजवद्यदि । तदेतत्त्वे समाचक्ष्त्ष कतमस्त्वमह॑ तथा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4517)
- **Original**: 14 श्रोविष्णुपुराण [ आ* 16 रहा है और बनसे कुशा तथा समिध केकर आया हुआ महाभाग निटाघ जनसमुहसे हटकर भूखा-प्यासा दूर स्वड़ा है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4518)
- **Original**: निदाघको देखकर ऋभु उसके निकट गये और उसका अभिवाटन करके खोले--' हे ट्विज
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4519)
- **Original**: यहाँ एकान्तमें आप कैसे स्ड़े हैं!
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4520)
- **Original**: निदाघ बोले --- हे विप्रवर ' आज इस अति रमणीक नगरमें राजा जाना चाहता है, सो मार्गमें बड़ी भोड़ हो रही है; इसस्ख्यि मैं यहाँ खड़ा हैँ
- **Translation**: 

---

