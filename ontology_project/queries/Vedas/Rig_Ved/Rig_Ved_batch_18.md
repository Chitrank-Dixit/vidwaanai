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

### Verse 1 (Rig Ved 0.341)
- **Original**: है अटल व्रत वाले मित्रावरुण ! आप दोनों ऋतु के अनुसार वल प्रदान करने वाले हैं। आप कठिनाई से सिद्ध होने वाले इस यज्ञ को सम्पन्न करते हैं
- **Translation**: 

---

### Verse 2 (Rig Ved 0.342)
- **Original**: 153. द्रबिणोदा द्रविणसो ग्रावहस्तासो अध्वरे। यज्ञेषु देवमीव्ठते
- **Translation**: 

---

### Verse 3 (Rig Ved 0.343)
- **Original**: थन की कापना वाले याजक सोमरस तैयार करने के निमित्त हाथ में पत्थर धारण करके पवित्र यज्ञ में धनप्रदायक अभ्निदेव की स्तुति करते हैं
- **Translation**: 

---

### Verse 4 (Rig Ved 0.344)
- **Original**: 18 ऋ्वेद संहिता धाग-9 154 द्रविणोदा ददातु नो वसूनि यानि शृण्विरे
- **Translation**: 

---

### Verse 5 (Rig Ved 0.345)
- **Original**: देवेषु ता वनामहे
- **Translation**: 

---

### Verse 6 (Rig Ved 0.346)
- **Original**: है घनप्रदायक अग्निदेव ! हमें वे सभी धन प्रदान करें, जिनके विषय में हमने श्रवण किया है । वे समस्त धन हम देवगणों को ही अर्पित करते हैं
- **Translation**: 

---

### Verse 7 (Rig Ved 0.347)
- **Original**: [दिव-शक्तियों से प्राप्त विधूतियों का उपयोग देवकायों के लिये ही करने का भाव व्यक्त किया गया है
- **Translation**: 

---

### Verse 8 (Rig Ved 0.348)
- **Original**: ] 155, द्रविणोदा: पिपीषति जुहोत प्र च तिष्ठत। नेट्टादतुभिरिष्यत
- **Translation**: 

---

### Verse 9 (Rig Ved 0.349)
- **Original**: घनप्रदायक अग्निदेव नेष्टापात्र (नेट्टधिष्णया स्थान-यज्ञ कुण्ड) से ऋतु के अनुसार सोमरस पीने की इच्छा करते हैं। अत: हे याजकगण ! आप वहाँ जाकर यज्ञ करें और पुन: अपने निवास स्थान के लिये प्रस्थान करें
- **Translation**: 

---

### Verse 10 (Rig Ved 0.350)
- **Original**: 156. यत्‌ त्या तुरीयमृतुभिद्रविणोदों यजामहे। अध समा नो ददिर्भव
- **Translation**: 

---

### Verse 11 (Rig Ved 0.351)
- **Original**: है धनप्रदायक अग्निदेव ! क्रतुओं के अनुगत होकर हम आपके निमित्त सोम के चौथे भाग को अर्पित करते हैं; इसलिए आप हमारे लिये धन प्रदान करने वाले हों
- **Translation**: 

---

### Verse 12 (Rig Ved 0.352)
- **Original**: 157 अश्विना पिबतं मधु दीद्यग्नी शुचिविता । ऋतुना यज्ञवाहसा
- **Translation**: 

---

### Verse 13 (Rig Ved 0.353)
- **Original**: दीप्तिमानू शुद्ध कर्म करने वाले, ऋतु के अनुसार यज्ञवाहक हे अश्विनीकुमारो ! आप इस मधुर सोमरस का पान करें
- **Translation**: 

---

### Verse 14 (Rig Ved 0.354)
- **Original**: 158, गा्हपत्येन सन्त्य ऋतुना यज्ञनीरसि। देवान्‌ देवयते यज
- **Translation**: 

---

### Verse 15 (Rig Ved 0.355)
- **Original**: हे इष्ठप्रद अग्निदेव ! आप गार्हपत्य के नियमन में ऋतुओं के अनुगत यज्ञ का निर्वाह करने वाले हैं, अत: देवत्व प्राप्ति की कामना वाले याजकों के निमित्त देवों का यज़न करें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.356)
- **Original**: [ सूक्त - 16 ] [ऋषि - मेथातिथि काण्व । देवता-इन्द्र
- **Translation**: 

---

### Verse 17 (Rig Ved 0.357)
- **Original**: छन्द-गायत्री
- **Translation**: 

---

### Verse 18 (Rig Ved 0.358)
- **Original**: ] 159. आ त््या वहन्तु हरयो वृषणं सोमपीतये। इन्द्र त्या सूरचक्षस:
- **Translation**: 

---

### Verse 19 (Rig Ved 0.359)
- **Original**: हे बलवान्‌ इन्द्रदेव ! आपके तेजस्वी घोड़े सोमरस पीने के लिए आपको यज्ञस्थल पर लाएँ तथा सूर्य के समान प्रकाशयुक्त ऋष्विज्‌ मन्त्रों द्वारा आपकी स्तुति करें
- **Translation**: 

---

### Verse 20 (Rig Ved 0.360)
- **Original**: 160, इमा धाना घृतस्नुवो हरी इहोप वक्षतः। इन्द्र सुखतमे रथे
- **Translation**: 

---

