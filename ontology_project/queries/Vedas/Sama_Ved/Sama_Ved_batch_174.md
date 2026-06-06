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

### Verse 1 (Sama Ved 0.3461)
- **Original**: 5 ;: 1352. सुप्रावीरस्तु स क्षयः प्र नु यामन्त्सुदानवः । ये नो अंहो5तिपिप्रति
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3462)
- **Original**: हे कल्याणकारी देवो ! आप हमारे उत्तम रक्षक हों । यज्ञ में वास करने वाले आप हमारी रक्षा करें और हमें पापों से मुक्त कराएँ
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3463)
- **Original**: 1353. उत स्वराजो अदितिरदब्धस्य ब्रतस्य ये । महो राजान ईशते
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3464)
- **Original**: मित्रादि देवगण अपनी माता अदिति सहित हमारे संकल्पों के पोषक हैं । हमारा अभीष्ट पूर्ण करने में समर्थ हैं, अत: वे शासक हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3465)
- **Original**: 1354. उ त्वा मदन्तु सोमा: कृणुष्व राधो अद्विव: । अब ब्रह्मद्विषो जहि
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3466)
- **Original**: है सशक्त इन्द्रदेव ! सोमरस का पान करते हुए आप प्रमुदित हों । हमें ऐश्वर्य प्रदान करें तथा सदज्ञान से द्वेष करने वालों का नाश करें
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3467)
- **Original**: 1355. पदा पणीनराधसो नि बाधस्व महाँ असि । न हि त्वा कश्चन प्रति
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3468)
- **Original**: हे इद्ध ! आप महान्‌ हैं । आपके समान सामर्थ्यवान्‌ कोई नहीं । आप दान न देने वालों को पीड़ित करें
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3469)
- **Original**: 1356. त्वमीशिषे सुतानामिन्द्र त्वमसुतानाम्‌ । त्व॑ राजा जनानाम्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3470)
- **Original**: हे इन्द्र
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3471)
- **Original**: आप रस-युकत पदार्थों एवं रस विहीन पदार्थों के स्वामी हैं। आप समस्त प्राणियों के शासक हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3472)
- **Original**: इति प्रथम:खण्ड:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3473)
- **Original**: 11.2 सामवेद-संहिता ै
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3474)
- **Original**: द्वितीय:खण्ड:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3475)
- **Original**: 1357. आ जागृविर्विप्र ऋतं मतीनां सोम: पुनानो असदच्चमूषु । सपन्ति य॑ं मिथुनासो निकामा अध्वर्यवो रथिरास: सुहस्ता:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3476)
- **Original**: चैतन्य, सत्य स्तुतियों का ज्ञाता सोम शुद्ध होकर पात्र में स्नवित होता है। उत्तम कर्म-कुशल, देहधारी, मनोकांक्षी अध्वर्यु इसे एकत्रित करके सुरक्षित रखते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3477)
- **Original**: 1358. स पुनान उप सूरे दधान ओभे अप्रा रोदसी वी ष आव: । प्रिया चिहद्यस्य प्रियसास ऊती सतो धन कारिणे न प्र यंसत्‌
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3478)
- **Original**: पवित्र होने वाला, वह सोम इन्द्र को प्राप्त करता है । आकाश और प्रथ्वी को अपने तेज से पूर्ण करने वाला यह सोम है: जिसकी अत्यन्त प्रिय रसयुक्त धाराएँ हमारा संरक्षण करती हैं और ऐश्वर्य प्रदान करती हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3479)
- **Original**: 1359. स वर्धिता वर्धन: पूयमान: सोमो मीढ्‌वाँ अभि नो ज्योतिषावीत्‌ । यत्र नः पूर्वे पितर: पदज्ञाः स्वर्विदों अभि गा अद्विमिष्णन्‌
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3480)
- **Original**: वृद्धि पाने वाला, देवत्व की वृद्धि करने वाला, इष्ठप्रदायक, शोधित सोम अपने तेज से हर प्रकार से रक्षा करे ।मन्त्रज्ञ आत्मज्ञानी, हमारे पूर्वज अपनी गौओं (यज्ञधेनु) को (सोमलता से युक्त) पर्वत के निकट ले जाते थे
- **Translation**: 

---

