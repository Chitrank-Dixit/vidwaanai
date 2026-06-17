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

### Verse 1 (Sama Ved 0.381)
- **Original**: 127. य आनयत्परावतः सुनीती तुर्वश यदुम्‌ । इन्द्र: स नो युवा सखा
- **Translation**: 

---

### Verse 2 (Sama Ved 0.382)
- **Original**: शत्रुओं के द्वारा तुर्वश और यदु (पराक्रमी राजाओं ) को बहुत दूर फेंका गया था । वहाँ से इन्द्रदेय ही उन्हें उत्तम नीति से सरलतापूर्वक लौटा कर लाये थे । बे युवा (स्फूर्तिवान) इन्द्रदेव हमारे मित्र हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.383)
- **Original**: 128, मा न इन्द्राभ्या3 दिशः सूरो अक्तुष्वा यमत्‌ । त्वा युजा वनेम ततू
- **Translation**: 

---

### Verse 4 (Sama Ved 0.384)
- **Original**: है इन्द्रदेव ! सर्वत्र विवरणशील, सब ओर शख्त्र फेंकने वाले (राक्षस), रात्रि के समय हमारे निकट न आ सकें । (यदि वे पास में आएँ भी तो) आपके अनुग्रह से वे नष्ट हो जाएँ
- **Translation**: 

---

### Verse 5 (Sama Ved 0.385)
- **Original**: 129. एन्द्र सानसिं रयिं सजित्वानं सदासहम्‌। वर्धिष्ठमूतये भर
- **Translation**: 

---

### Verse 6 (Sama Ved 0.386)
- **Original**: .. हे इद्धदेव ! आप हमारे जीवन संरक्षण के लिये तथा शत्रुओं को पराभूत करने के निमित्त, हमें धन-धान्य से पूर्ण करें
- **Translation**: 

---

### Verse 7 (Sama Ved 0.387)
- **Original**: 130. इन्द्रं बयं महाधन इन्द्रमभें हवामहे । युजं वृत्रेषु वच्रिणम्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.388)
- **Original**: हम छोटे-बड़े सभी (जीवन) संग्रामों में, वृत्रासुर-संहारक, वद्रपाणि इन्द्रदेव को सहायतार्थ बुलाते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.389)
- **Original**: 131. अपिवत्कद्ठुव: सुतमिन्द्र: सहस्रबाद्धे । तत्राददिष्ट पौस्थम्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.390)
- **Original**: कद के द्वारा निष्पन्‍नन सोमरस का इद्धदेव ने पान किया और हजारों भुजा वाले बलशाली शत्रु का संहार किया, जिससे इन्धदेव का दर्शनीय पराक्रम प्रकट हुआ
- **Translation**: 

---

### Verse 11 (Sama Ved 0.391)
- **Original**: 132. वयमिन्द्र त्वायवो5भि प्र नोनुमो बृषन्‌ । विद्धी त्वा 3 स्थ नो बसो
- **Translation**: 

---

### Verse 12 (Sama Ved 0.392)
- **Original**: हे श्रेष्ठ वीर इन्द्रदेव
- **Translation**: 

---

### Verse 13 (Sama Ved 0.393)
- **Original**: हम आपकी कामना करते हुए बारम्बार नमन करते हैं । हे सबको आश्रय देने वाले ! आप हमारी प्रार्थनाओं को सुनें-समझें
- **Translation**: 

---

### Verse 14 (Sama Ved 0.394)
- **Original**: पूर्वार्चिके ऐद्रपर्वणि द्वितीयो5 ध्याय: 2.3 133. आ घा ये अग्निमिन्धते स्तृणन्ति बर्हिरानुषक्‌ । येषामिन्द्रो युवा सखा। ।9
- **Translation**: 

---

### Verse 15 (Sama Ved 0.395)
- **Original**: । श्रेष्ठ अग्नि को प्रदीष्त करने वाले याज्ञिकों के मित्र, चिर युवा इद्धदेव हैं । बे (याजक) उनके लिए कुश- आसन बिछते हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.396)
- **Original**: 134. भिन्थि विश्वा अप द्विष: परि बाधो जही मृथः
- **Translation**: 

---

### Verse 17 (Sama Ved 0.397)
- **Original**: बसु स्पाहँ तदा भर
- **Translation**: 

---

### Verse 18 (Sama Ved 0.398)
- **Original**: आप विश्व भर के द्वेष करने वालों को नष्ट करें, विध्न पैदा करने वाले दुष्टों को पराजित करें और सराहनीय वैभव हमें भरपूर मात्रा में प्रदान करें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.399)
- **Original**: इति द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.400)
- **Original**: के के के
- **Translation**: 

---

