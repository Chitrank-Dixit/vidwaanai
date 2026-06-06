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

### Verse 1 (Rig Ved 0.10421)
- **Original**: 4530. उप त्वा रण्वसद्दृशं प्रयस्वन्तः सहस्कृत। अग्ने ससृज्महे गिर:
- **Translation**: 

---

### Verse 2 (Rig Ved 0.10422)
- **Original**: हे बल-पुत्र अग्निदेव आप रमणीय दिखाई देते हैं । हम हविष्यान्न अर्पित करते हुए आपकी स्तूति करते है
- **Translation**: 

---

### Verse 3 (Rig Ved 0.10423)
- **Original**: 4531. उपच्छायामिव घृणेरगन्म शर्म ते वयम्‌। अग्ने हिरण्य5सन्दृशः
- **Translation**: 

---

### Verse 4 (Rig Ved 0.10424)
- **Original**: है अग्निदिव ! आप स्वर्णपयों आभा वाले हैं। आपके साम्रीष्य से हमें यैसा ही सुख मिलता है, जैसा कि थके हुए प्राणियों को छाया में मिलता है
- **Translation**: 

---

### Verse 5 (Rig Ved 0.10425)
- **Original**: 4532. य उग्र इव शर्यहा तिग्मशूड्गो न वंसग: । अम्ने पुरो रुरोजिथ
- **Translation**: 

---

### Verse 6 (Rig Ved 0.10426)
- **Original**: हे अग्निदेव ! आप महान योद्धा के बाणों एवं बैल के तीक्ष्ण सींगों के समान शत्रुओं का संहार करते हैं । हे देव ! आपने ही असुरों के तीन नगरों को नष्ट किया है
- **Translation**: 

---

### Verse 7 (Rig Ved 0.10427)
- **Original**: 4533. आ य॑ हस्ते न खादिनं शिशु जातं न बिश्रति। विशामर्ग्नि स्वध्वरम्‌
- **Translation**: 

---

### Verse 8 (Rig Ved 0.10428)
- **Original**: (अरणि मन्धन से उत्पन्न) अग्नि को अध्वर्युगण नवजात शिशु की तरह (प्रेमभाव से) हाथ में धारण करते है हे कब्नौचजो ! आप हिंसक पशु की भाँति सावधानों से अग्नि की परिचर्या करें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.10429)
- **Original**: 4534 प्र देव॑ देववीतये भरता वसुवित्तमप्‌। आ स्वे योनौ नि षीदतु
- **Translation**: 

---

### Verse 10 (Rig Ved 0.10430)
- **Original**: है अध्वर्यों ! आप देवगणों के निमित्त, इन तेजस्वी एवं ऐश्वर्यवान्‌ अग्निदेव को यज्ञवेटी पर स्थापित करते हुए हव्य अर्पित करें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.10431)
- **Original**: 4535. आ जात॑ जातवेदसि प्रियं शिशीतातिधिम्‌
- **Translation**: 

---

### Verse 12 (Rig Ved 0.10432)
- **Original**: स्थोन आ गृहपतिम्‌
- **Translation**: 

---

### Verse 13 (Rig Ved 0.10433)
- **Original**: हे अध्वयों ! आप अतिधि जैसे पूज्य , गृहपति अग्निदेव को यज्ञवेदी पर स्थापित कर , ज्ञानी , सुखकर अम्निदेव को उत्तम हवि अर्पित करें
- **Translation**: 

---

### Verse 14 (Rig Ved 0.10434)
- **Original**: 4536. अनेे युक्ष्वा हि ये तवाश्वासो देव साधव: । अर वहन्ति मन्यवे
- **Translation**: 

---

### Verse 15 (Rig Ved 0.10435)
- **Original**: हे ज्योतिर्मान्‌ अभ्देव ! आप उन समस्त श्रेष्ठ एवं कुशल अश्रों (ऊर्जा धाराओं ) को नियोजित करें, जो आपको यज्ञ हेतु वहन करते हैं
- **Translation**: 

---

### Verse 16 (Rig Ved 0.10436)
- **Original**: 4537, अच्छा नो याह्या वहाभि प्रयांसि बीतये। आ देवान्सोमपीतये
- **Translation**: 

---

### Verse 17 (Rig Ved 0.10437)
- **Original**: है अग्निदेव ! हवि ग्रहण करने और सोमपान करने के निमित्त आप हमारी ओर उन्मुख हों और देवों को भी प्रकट करें #डह
- **Translation**: 

---

### Verse 18 (Rig Ved 0.10438)
- **Original**: 4538. उदग्ने भारत द्युमदजस्रेण दविद्युतत्‌। शोचा वि भाहाजर
- **Translation**: 

---

### Verse 19 (Rig Ved 0.10439)
- **Original**: संसार का भरण-पोषण करने वाले हे अग्निदेव ! आप प्रज्वलित होकर उनत हों, कभी क्षीण न होने वाले अपने तेज से प्रकाशित हों और जगत्‌ में प्रकाश फैलाएँ
- **Translation**: 

---

### Verse 20 (Rig Ved 0.10440)
- **Original**: 4 ऋ्वेद संहिता भाग - 2 4539. वीती यो देवं मर्तो दुवस्थेदग्निमीव्ीताध्वरे हविष्मान्‌। होतारं सत्ययजं रोदस्योरुत्तानहस्तो नमसा विवासेत्‌
- **Translation**: 

---

