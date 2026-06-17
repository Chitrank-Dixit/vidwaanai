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

### Verse 1 (Sama Ved 0.1241)
- **Original**: है सोमदेव ! देवताओं को आकृष्ट करने वाला, पापी एवं दुष्टों का नाश करने वाला आपका दिव्य रस अत्यन्त हर्षप्रद है । उस पोषक रस सहित आप कलश में प्रतिष्ठित हों
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1242)
- **Original**: 4729. तिस्रो वाच उदीरते गावो मिमन्ति धेनव:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1243)
- **Original**: हरिरेति कनिक्रदत्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1244)
- **Original**: यजनकाल में जब तीनों वेदों के मंत्र बोले जाते हैं, गौएँ दुह्ढे जाने के लिए रँभाती हैं, तब हरे रंग का सोमरस शब्द करता बुआ शोधित होता है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1245)
- **Original**: 472. इन्द्रायेन्दो मरुत्वते पवस्व मधुमत्तमः। अर्कस्य योनिमासदम्‌
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1246)
- **Original**: अत्यन्त मधुर हे सोम ! आप इस यज्ञ के स्थान (यज्ञशाला) में, जिसके सहायक मरुद्गण हैं. उन इन्द्रदेव के लिए कलश में स्थित हों
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1247)
- **Original**: 473. असाव्य॑ शुर्मदायाप्सु दक्षो गिरिष्ठा:। श्येनो न योनिमासदत्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1248)
- **Original**: पर्वत पर उत्पन सोम आनन्द के लिए निचोड़ा गया एवं जल के संयोग से व्यापक बना और श्येन पक्षी के समान अपने निश्चित स्थान पर विराजित है
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1249)
- **Original**: 474. पवस्व दक्षसाधनो देवेभ्य: पीतये हरे । मरुद्भ्यो वायवे मद:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1250)
- **Original**: है हरिताभ सोम ! आप हर्ष और शक्ति के साधनभूत हैं । देवों और मरुतों के पीने के निमित्त आप कलश में स्थित हों
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1251)
- **Original**: 475. परि स्वानो गिरिष्ठा: पवित्रे सोमो अक्षरत्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1252)
- **Original**: मदेषु सर्वधा असि
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1253)
- **Original**: यह सोध पवित्र कलश में निकाला गया है । हे सोमदेव ! आप पर्वत पर उत्पन्न होने वाले हैं, रस निकाले जाने पर आनन्ट देने खालों में आप सबसे श्रेष्ठ हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1254)
- **Original**: 5.2 सामवेद-संहिता 476. परि प्रिया दिव: कविर्वयांसि नप्त्योर्हित: । स्वानैर्याति कविक्रतु:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1255)
- **Original**: 90 ।। बुद्धि को बढ़ाने वाला यह सोम, सोमरस निकालने के दो फलकों (द्युलोक एवं पृथ्वी) के बीच में स्थित होकर, ब्रह्मनिष्ठों द्वारा सचेतन प्राणियों तक पहुँचाया जाता है
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1256)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1257)
- **Original**: के केक
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1258)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1259)
- **Original**: 477. प्र सोमासो मदच्युतः श्रवसे नो मघोनाम्‌ 5 सुता विदथे अक्रमुः
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1260)
- **Original**: आनन्ददायक सोम अभिषुत होकर हमारे यज्ञ में अन्न और यश प्रदाता बनकर स्थित होता है
- **Translation**: 

---

