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

### Verse 1 (Rig Ved 0.521)
- **Original**: पन के तुल्य वेग वाले, सहख्र चश्लु वाले, बुद्धि के अधीश्वर इन्द्र एवं वायु देवों का ज्ञानीजन अपनी सुरक्षा के लिए आवाहन करते हैं।
- **Translation**: 

---

### Verse 2 (Rig Ved 0.522)
- **Original**: 233. मित्र बयं हवामहे वरुणं सोमपीतये। जज्ञाना पूतदक्षसा
- **Translation**: 

---

### Verse 3 (Rig Ved 0.523)
- **Original**: सोमरस पोने के लिए यज्ञस्थल पर प्रकट होने वाले परमपवित्र एवं बलशाली मित्र और वरुणदेवों का हम आवाहन करते हैं
- **Translation**: 

---

### Verse 4 (Rig Ved 0.524)
- **Original**: 234. ऋतेन यावृताबृधावृतस्य ज्योतिषस्पती । ता मित्रावरुणा हुवे
- **Translation**: 

---

### Verse 5 (Rig Ved 0.525)
- **Original**: प्रत्यमार्ग पर चलने वालों का उत्साह बढ़ाने वाले, तेजस्वी मित्रावरुणों का हम आवाहन करते हैं
- **Translation**: 

---

### Verse 6 (Rig Ved 0.526)
- **Original**: 235. वरुण: प्राविता भुवन्मित्रो विश्वाभिरूतिभि:। करता नः सुराधस:
- **Translation**: 

---

### Verse 7 (Rig Ved 0.527)
- **Original**: वरुण एवं मित्र देवता अपने समस्त रक्षा साधनों से हम सबकी हर प्रकार से रक्षा करते हैं। वे हमें महान्‌ वैभव सम्पन्न करें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.528)
- **Original**: में0 1 सू0 23 25 236. मरुत्वन्तं हवामह इन्द्रमा सोमपीतये
- **Translation**: 

---

### Verse 9 (Rig Ved 0.529)
- **Original**: सजूर्गणेन तृम्पतु
- **Translation**: 

---

### Verse 10 (Rig Ved 0.530)
- **Original**: मरुदगणों के सहित इन्द्रदेव को सोमरस पान के निमित्त बुलाते हैं । वे मरद्गणों के साथ आकर तृप्त हों
- **Translation**: 

---

### Verse 11 (Rig Ved 0.531)
- **Original**: 237 इन्द्रज्येष्ठा मरुद्रणा देवास: पुषरातय: । विश्वे मम श्रुता हवम्‌
- **Translation**: 

---

### Verse 12 (Rig Ved 0.532)
- **Original**: दानी पूषादेव के समान इन्द्रदेव दान देने में श्रेष्ठ हैं । वे सब मरुट्गणों के साथ हमारे आवाहन को सुनें
- **Translation**: 

---

### Verse 13 (Rig Ved 0.533)
- **Original**: 238. हत बृत्रं सुदानव इन्द्रेण सहसा युजा। मा नो दुःशंस ईशत
- **Translation**: 

---

### Verse 14 (Rig Ved 0.534)
- **Original**: है उत्तम दानदाता मरुतो ! आप अपने उत्तम साथी और बलवान्‌ इन्द्रदेव के साथ दुष्टों का हनन करें । दुष्टता हमारा अतिक्रमण न कर सके
- **Translation**: 

---

### Verse 15 (Rig Ved 0.535)
- **Original**: 239. विश्वान्देवान्हवापहे मरुतः सोमपीतये । उय्या हि पृश्निमातरः
- **Translation**: 

---

### Verse 16 (Rig Ved 0.536)
- **Original**: सभी मरुदगणों को हम सोमपान के निमित्त बुलाते हैं । वे सभी अनेक रंगों वाली पृथ्वी के पुत्र महान्‌ बीर एवं पराक्रमी हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.537)
- **Original**: 240. जयतामिव तन्यतुर्मरुतामेति धृष्णुया। यच्छु्भ याथना नर:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.538)
- **Original**: वेग से प्रवाहित होने वाले मरुतों का शब्द विजयनाद के सदृश गुंजित होता है, उससे सभी मनुष्यों का मंगल होता है
- **Translation**: 

---

### Verse 19 (Rig Ved 0.539)
- **Original**: 241. हस्काराष्टिद्युतस्पर्यतो जाता अवन्तु नः। मरुतों मृव्ठयन्तु नः
- **Translation**: 

---

### Verse 20 (Rig Ved 0.540)
- **Original**: चमकने वालो विद्युत्‌ से उत्पन्न हुए मरद्गण हमारी रक्षा करें और प्रसन्‍ता प्रदान करें
- **Translation**: 

---

