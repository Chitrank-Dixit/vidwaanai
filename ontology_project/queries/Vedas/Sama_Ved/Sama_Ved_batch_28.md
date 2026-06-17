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

### Verse 1 (Sama Ved 0.541)
- **Original**: के के के
- **Translation**: 

---

### Verse 2 (Sama Ved 0.542)
- **Original**: नवमः: खण्ड:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.543)
- **Original**: 194. उत्त्वा मन्दन्तु सोमा: कृणुष्व राधो अद्विव:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.544)
- **Original**: अब ब्रह्मद्विषो जहि
- **Translation**: 

---

### Verse 5 (Sama Ved 0.545)
- **Original**: है इन्द्रदेव ! आपको यह सोमरस आनन्द प्रदान करे । हे वज्रधारी इन्द्रदेव
- **Translation**: 

---

### Verse 6 (Sama Ved 0.546)
- **Original**: ! आप हमें ऐश्वर्य देकर ज्ञान के साथ द्वेष रखने वालों का संहार करें
- **Translation**: 

---

### Verse 7 (Sama Ved 0.547)
- **Original**: 195.गिर्वण: पाहि नः सुतं मधोर्धाराभिरज्यसे । इन्द्र त्वादातमिद्यशः
- **Translation**: 

---

### Verse 8 (Sama Ved 0.548)
- **Original**: हे स्तुत्य इन्द्रदेव !आप हमारे द्वारा शोधित सोमरस पान करें; क्योंकि आप इस आनन्ददायी सोमरस की धागओं से सिंचित होते हैं । हे इन्द्रदेव ! आपको कृपा से ही हमें यश मिलता है
- **Translation**: 

---

### Verse 9 (Sama Ved 0.549)
- **Original**: 196.सदा व इन्द्रश्न॑कैषदा उपो नु स सपर्यन्‌ । न देवो वृतः शूर इन्द्र:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.550)
- **Original**: (है स्तोताओ !) ये इन्द्रदेव सदैव तुम्हारे सहयोगी हैं । वे पूजन के साथ ही तुम्हारे यज्ञ की ओर उन्मुख होते हैं । ऐसे ही महान्‌ वीर इन्द्रदेव, हमारे द्वारा पूज्य हैं
- **Translation**: 

---

### Verse 11 (Sama Ved 0.551)
- **Original**: 197. आ त्वा विशन्त्विन्दवः समुद्रमिव सिन्धव: । न त्वामिद्धाति रिच्यत्ते
- **Translation**: 

---

### Verse 12 (Sama Ved 0.552)
- **Original**: हे इद्धदेव ! नदियों के समुद्र में मिलने की भाँति, सोमरस आपके अन्दर प्रविष्ट होता है । हे इन्द्रदेव ! आपसे अधिक महान्‌ और कोई नहीं है
- **Translation**: 

---

### Verse 13 (Sama Ved 0.553)
- **Original**: 198. इन्द्रमिद्गाधिनो बृहदिन्द्रमर्केभिरकिंण: । इन्द्र वाणीरनूषत
- **Translation**: 

---

### Verse 14 (Sama Ved 0.554)
- **Original**: साप्रगान के साधकों ने, गाये जाने योग्य बृहत्‌ साम की स्तुतियों से देवराज इन्द्र को प्रसन्‍न किया है । इसी तरह याज्िकों ने भी मन्त्रोच्चारण के द्वारा इन्द्रदेव की प्रार्थना की है
- **Translation**: 

---

### Verse 15 (Sama Ved 0.555)
- **Original**: 199. इन्द्र इषे ददातु न ऋभुक्षणमृभुं_ रयिम्‌ । वाजी ददातु वाजिनम्‌
- **Translation**: 

---

### Verse 16 (Sama Ved 0.556)
- **Original**: बलवान्‌ इद्धदेव हमें श्रेष्ठ धन से सदैव पूर्ण रखें । अन प्राप्ति के लिये श्रेष्ठ उत्तराधिकार प्रदान करें । है बलशाली ! हमें बलवान्‌ बनायें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.557)
- **Original**: 2.10 सायवेट-संहिता 200, इन्द्रो अड़् महद्धयमभी षदप चुच्यवत्‌ । स हि स्थिरो विचर्षणि:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.558)
- **Original**: युद्ध में स्थिर रहने वाले विश्वद्रष्टा इन्द्रदेव, महान्‌ पराभवकारी भय को शीघ्र ही दूर करते एवं उन्हें स्थायी रूप से हटा देते हैं*
- **Translation**: 

---

### Verse 19 (Sama Ved 0.559)
- **Original**: 209. इमा उ त्वा सुतेसुते नक्षन्ते गिर्वणो गिर: । गावी वत्सं न धेनव:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.560)
- **Original**: हे स्तुत्य इद्धदेय ! जिस प्रकार दुधारू गौएँ बछड़ों के पास स्त्रयं ही जा पहुँचती हैं, उसीप्रकार प्रत्येक यज्ञ में हमारी स्तुतियाँ आपके पास पहुँचती हैं
- **Translation**: 

---

