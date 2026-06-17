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

### Verse 1 (Sama Ved 0.61)
- **Original**: हे सर्वज्ञाता ! आप यज्ञ के विधाता हैं, समस्त देव शक्तियों को तुष्ट करने की सामर्थ्य रखते हैं । आप यज्ञ की विधि-व्यवस्था के स्वामी हैं-- ऐसे समर्थ आपको देवदूत रूप में हम स्वीकार करते हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.62)
- **Original**: 4. अम्निर्वत्राणि जड्डनद्‌ द्रविणस्युर्विपन्यया । समिद्ध: शुक्र आहुत:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.63)
- **Original**: उनके सत्ययासों से प्रसन्‍न होकर याजकों को सम्पन्नता प्रदान करने वाले हे प्रदीप्त अग्निदेव ! हमें बन्धन में रखने वाली दुष्टवृत्तियों का आप विनाश करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.64)
- **Original**: 5. प्रेष्ठं वो अतिथिं स्तुषे मित्रमिव प्रियम्‌ । अग्ने रथ॑ न वेद्यम्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.65)
- **Original**: हे अग्ने ! उपासकों की अभिलाषा पूरी करने वाले, सदा सब पर कृपा करने वाले, मित्र के समान व्यवहार करने वाले आप हमारी प्रार्थना से प्रसन्‍न हों
- **Translation**: 

---

### Verse 6 (Sama Ved 0.66)
- **Original**: 6. त्वं नो अग्ने महोभि: पाहि विश्वस्या अरातेः । उत द्विषो मर्त्यस्य
- **Translation**: 

---

### Verse 7 (Sama Ved 0.67)
- **Original**: है अग्ने ! संसार के, द्रेष करने वाले व्यक्तियों एवं शत्रुओं से आप हमारी रक्षा करें और विषम परिस्थितियों में हमें धैर्यवान्‌ बनायें
- **Translation**: 

---

### Verse 8 (Sama Ved 0.68)
- **Original**: 7. एड्रूपु ब्रवाणि ते5ग्न इत्थेतरा गिर: । एभिवर्धास इन्दुभि:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.69)
- **Original**: हम आपके लिए ही स्तुति करते हैं, आँप इन्हें सुनें, प्रकट हों और इस सोमरस से अपनी महानता का विस्तार करें
- **Translation**: 

---

### Verse 10 (Sama Ved 0.70)
- **Original**: «. आ ते वत्सो मनो यमत्परमाच्चित्सधस्थात्‌ । अग्ने त्वां कामये गिरा
- **Translation**: 

---

### Verse 11 (Sama Ved 0.71)
- **Original**: हे देव ! हम आपके पुत्र, हृदय से आपकी स्तुति करते हुए अपनी ओर आकर्षित करना चाहते हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.72)
- **Original**: 9. त्यामग्ने पुष्करादध्यथर्वा निरमन्थत । मूथ्नों विश्वस्य वाघतः
- **Translation**: 

---

### Verse 13 (Sama Ved 0.73)
- **Original**: परम श्रेष्ठ अखिल विश्व के धारणकर्ता, हे अग्निदेव
- **Translation**: 

---

### Verse 14 (Sama Ved 0.74)
- **Original**: विज्ञान वेत्ताओं (अथर्वा) ने आपको विश्व के महानतम आधार के रूप में अरणिमंथन द्वारा प्रकट किया
- **Translation**: 

---

### Verse 15 (Sama Ved 0.75)
- **Original**: 10. अग्ने विवस्व॒दा भरास्मभ्यमूतये महे । देवो हासि नो दृशे
- **Translation**: 

---

### Verse 16 (Sama Ved 0.76)
- **Original**: हे अग्ने ! हमारी श्रेष्ठता की रक्षा के निमित्त आप हमें उपयुक्त आवास प्रदान करें । आप ही प्रकाशों में श्रेष्ठ प्रकाशवान्‌ देव हैं । आप ही समर्थ एवं शक्तिशाली देवता हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.77)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.78)
- **Original**: । के के के
- **Translation**: 

---

### Verse 19 (Sama Ved 0.79)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.80)
- **Original**: 11. नमस्ते अग्न ओजसे गृणन्ति देव कृष्टय: । अमैरमित्रमर्दय
- **Translation**: 

---

