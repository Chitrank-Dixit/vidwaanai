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

### Verse 1 (Sama Ved 0.3061)
- **Original**: हे सोमदेव ! समस्त प्राणियों का निरीक्षण करने वाले, सर्वज्ञ इद्धदेव के द्वारा पान किये जाने वाले शाप हमें सन्‍्तान, अन्न, बल और सदज्ञान आदि प्रदान करें
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3062)
- **Original**: 1186. वृर्शि दिव: परि स्रव द्ुप्न॑ं पृथिव्या अधि । सहो न: सोम पृत्सु धा:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3063)
- **Original**: हे सोमदेव ! आप आकाश से पृथ्वी के ऊपर दिव्य वृष्टि करें । पृथ्वी पर पोषक अन्न उत्पन्न करें और हमें संघर्ष की शक्ति प्रदान करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3064)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3065)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3066)
- **Original**: 1187. सोम: पुनानो अर्पति सहस्नधारो अत्यवि:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3067)
- **Original**: वायोरिद्धस्य निष्कृतम्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3068)
- **Original**: सहस्नरधार बनकर पवित्र होने वाला, हजारों धाराओं से बालों की छलनी से छाना गया शोधित सोम, वायु और इन्धदेवों के पान करने के लिए, श्रेष्ठ पात्रों में स्थित होता है
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3069)
- **Original**: 1188. पवमानमवस्यवो विप्रमभि प्र गायत
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3070)
- **Original**: सुष्वाणं देववीतये
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3071)
- **Original**: अपने संरक्षण की कामना करने वाले हे याजकों ! सबको पवित्र करने वाले, विशेष आनन्द प्रदान करने वाले, देवों के पान के योग्य, शोधित सोम के लिए सम्मानपूर्वक स्तुतियों का गान करो
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3072)
- **Original**: 1189. पबन्ते वाजसातये सोमाः सहस्नपाजस: । गृणाना देववीतये
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3073)
- **Original**: अन्न (पोषण) प्राप्त कराने के कारण स्तुत्य, देवतुल्य हजारों प्रकार से बलवर्द्धक वह सोमरस शोधित किया जा रहा है
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3074)
- **Original**: 1190, उत नो वाजसातये पवस्व बृहतीरिष: । द्युमदिन्दो सुवीर्यम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3075)
- **Original**: हे दिव्य सोमदेव ! आप जीवन-संग्राम की सफलता के लिए हमें श्रेष्ठ अन्न प्रदान करें, हमें तेजस्वी एवं सामर्थ्यवान्‌ बनाएँ
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3076)
- **Original**: 1191. अत्या हियाना न हेतृभिरसुग्नं वाजसातये । वि वारमव्यमाशव:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3077)
- **Original**: जीवन-संग्राम का प्रेरक सोम ऋष्तिजों द्वारा तीव्र गति से शोधित किया जाता है
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3078)
- **Original**: 1192. ते नः सहस्त्रिणं रविं पवन्तामा सुवीर्यम्‌। स्वाना देवास इन्दवः
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3079)
- **Original**: वह स्नरवित किया गया दिव्य सोमरस, हमें असंख्य ऐश्वर्य और उत्तम सामरथ्यों को प्रदान करे
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3080)
- **Original**: उत्तरार्थिके नवमो5ध्याय: 9.3 1193. वाश्रा अर्पन्तीन्दवो5भि वत्सं न मातर: । द्धन्विरे गभस्त्यो:
- **Translation**: 

---

