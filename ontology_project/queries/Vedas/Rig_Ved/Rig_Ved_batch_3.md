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

### Verse 1 (Rig Ved 0.41)
- **Original**: घृत के समान प्राणप्रद वृष्टि-सम्यल कराने वाले मित्र और वरुण देवों का हम आबाहन करते हैं । मित्र हमें बलशाली बनायें तथा वरुणदेव हमारे हिंसक शत्रुओं का नाश करें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.42)
- **Original**: 17, ऋतेन मित्रावरुणावृतावृधावृतस्पृशा। क्रतुं बृहन्तमाशाथे
- **Translation**: 

---

### Verse 3 (Rig Ved 0.43)
- **Original**: सत्य को फलितार्थ करने वाले सत्ययज्ञ के पुृष्टिकारक देव भित्रावरुणो ! आप दोनों हमारे पुण्यदायो कार्यों (प्रवर्तमान सोमयाग) को सत्य से परिपूर्ण करें
- **Translation**: 

---

### Verse 4 (Rig Ved 0.44)
- **Original**: 18, कवी नो मित्रावरुणा तुविजाता उरुक्षया। दक्ष दधाते अपसम्‌
- **Translation**: 

---

### Verse 5 (Rig Ved 0.45)
- **Original**: अनेक कर्मों को सम्पल कराने वाले विवेकशील तथा अनेक स्थलों में निवास करने वाले मित्रावरुण हमारी क्षमताओं और कार्यो को पुष्ट बनाते हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.46)
- **Original**: [ सूक्त - 3 ] [ऋषि-मधुच्छन्दा वैश्वामित्र
- **Translation**: 

---

### Verse 7 (Rig Ved 0.47)
- **Original**: देवता-1-3 अश्विनीकुमार, 4-6 इन्द्र, 7-9 विश्वेदेवा, 10-12 सरस्वती । छत्द-गायत्रों ।] 19, अश्विना यज्वरीरिषो द्रवत्पाणी शुभस्पती
- **Translation**: 

---

### Verse 8 (Rig Ved 0.48)
- **Original**: पुरुभुजा चनस्यतम्‌
- **Translation**: 

---

### Verse 9 (Rig Ved 0.49)
- **Original**: हे विशालबाहो ! शुभ कर्मपालक, द्रुतगति से कार्य सम्पल करने वाले अश्विनीकुमारो ! हमारे द्वारा समर्पित हविष्यानों से आप भली प्रकार सन्तुष्ट हों
- **Translation**: 

---

### Verse 10 (Rig Ved 0.50)
- **Original**: 20. अश्विना पुरुदंससा नरा शवीरया धिया। धिष्णया बनत॑ गिर:
- **Translation**: 

---

### Verse 11 (Rig Ved 0.51)
- **Original**: असंख्य कर्मों को सम्पादित करने वाले,घैर्य धारण करने वाले, बुद्धिमान्‌ हे अश्विनीकुमायो ! आप अपनी उत्तम बुद्धि से हमारी वाणियों (प्रार्थाओं) को स्वीकार करें
- **Translation**: 

---

### Verse 12 (Rig Ved 0.52)
- **Original**: 21. दल्ला युवाकव: सुता नासत्या वृक्तबर्हिष:। आ यात॑ रुद्रवर्तनी
- **Translation**: 

---

### Verse 13 (Rig Ved 0.53)
- **Original**: रोगों को विनष्ट करने वाले, सदा सत्य बोलने वाले रुद्रदेव के समान (शत्रु संहारक) प्रवृत्ति वाले, दर्शनीय है अश्विनौकुमारों ! आप यहाँ आयें और बिछी हुई कुशाओं पर विराजमान होकर प्रस्तुत संस्कारित सोमरस का पान करें
- **Translation**: 

---

### Verse 14 (Rig Ved 0.54)
- **Original**: 22. इन्द्रा याहि चित्रभानो सुता इमे त्वायव:। अण्वीभिस्तना पूतास:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.55)
- **Original**: है अद्भुत दीप्तिमान्‌ इन्द्रदेव ! अँगुलियों द्वारा स्रवित, श्रेष्ठ पवित्रतायुक्त यह सोमरस आपके निमित्त है। आप आयें और सोमसस का पान करें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.56)
- **Original**: 23. इन्द्रा याहि धियेषितो विप्रजूत: सुतावतः। उप ब्रह्माणि बाघतः
- **Translation**: 

---

### Verse 17 (Rig Ved 0.57)
- **Original**: हे इन्रदेव ! श्रेष्ठ बुद्धि द्वारा जानने योग्य आप, सोमरस प्रस्तुत करते हुये ऋत्विजों के द्वारा बुलाये गये हैं । उनकी स्तुति के आधार पर आप यज्ञशाला में पधारें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.58)
- **Original**: 24. इन्द्रा याहि तूतुजान उप ब्रह्माणि हरिव:। सुते दथिष्व नश्चन:
- **Translation**: 

---

### Verse 19 (Rig Ved 0.59)
- **Original**: हे अश्वयुक्त इन्रदेव ! आप स्तबनों के श्रवणार्थ एवं इस यज्ञ में हमारे द्वारा प्रदत्त हवियों का सेवन करने के लिये यज्ञशाला में शीघ्र ही पधारे
- **Translation**: 

---

### Verse 20 (Rig Ved 0.60)
- **Original**: ड़ ऋण्वेद संहिता भाग-9 25. ओमासश्चर्षणी थ्रृतो विश्वेदेवास आ गत। दाश्वांसो दाशुष: सुतम्‌
- **Translation**: 

---

