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

### Verse 1 (Sama Ved 0.2541)
- **Original**: यज्ञ की भाँति निरंतर परमार्थ में निरत, क्रीड़ा करने वाले हे सोमदेव ! आप स्तोताओं को शौर्य-पराक्रम प्रदान करते हुए शुद्धता को प्राप्त होते हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2542)
- **Original**: 975,यवंयवं नो अन्धसा पुष्टंपुष्टं परि स्नव । विश्वा च सोम सौभगा
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2543)
- **Original**: है सोमदेव ! अपने दिव्य पोषक रस को, अन्न एवं वनस्पतियों के साथ हमें उपलब्ध कराते रहें । हमें सम्पूर्ण वैभव प्रदान करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2544)
- **Original**: 976.इन्दो यथा तव स्तवो यथा ते जातमन्धस: । नि बर्हिषि प्रिये सद:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2545)
- **Original**: देवताओं के प्रिय आहार, हे सोमदेव ! याजकों द्वारा जिस भावना से आपकी स्तुति की जाती है, उसी स्नेह के साथ आप यज्ञशाला में श्रेष्ठ आसन ग्रहण करें
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2546)
- **Original**: 977.उत नो गोविदश्चवित्पवस्व सोमान्धसा । मक्षृ्‌तमेभिरहभि:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2547)
- **Original**: है सोमदेव
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2548)
- **Original**: आप हमें गाय, घोड़े, अन्न आदि के रूप में अपार वैभव शीघ्र प्रदान करें
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2549)
- **Original**: 978.यो जिनाति न जीयते हन्ति शत्रुमभीत्य । स पवस्व॒ सहस्नजित्‌
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2550)
- **Original**: शत्रुओं पर विजय प्राप्त करने वाले, हे सोमदेव ! अपने प्रहारों से असुरों का विनाश करके आप उन पर विजय प्राप्त करते हैं । कभी पराजित न होने वाले आप पवित्रता को प्राप्त हों
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2551)
- **Original**: 979.यास्ते धारा मधुश्ुतो5सृग्रमिन्द ऊतये । ताभिः पवित्रमासद:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2552)
- **Original**: अपनी मधुर रस की थाराओं से सभी को संरक्षण देने वाले, हे सोमदेव ! आप उन धाराओं के साथ शुद्धता को धारण करें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2553)
- **Original**: 980.सो अर्पेन्द्राय पीतये तिरो वाराण्यव्यया । सीदन्नृतस्य योनिमा
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2554)
- **Original**: ऊन के हने द्वारा शुद्ध होने वाले हे सोमदेव ! यज्ञ के मूल स्थान पर स्थापित होकर, आप इ्धदेव की तृप्ति के लिए तैयार हों
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2555)
- **Original**: 981.त्वं सोम परि स्त्रव स्वादिष्ठो अड्विरोभ्य: । वरिवोविद्घृतं पयः
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2556)
- **Original**: धन-वैभव प्रदान करने वाले हे स्वादिष्ट सोम ! आप अंगिरादि ऋषियों के लिए घृत-दुग्धझुक्त पौष्टिक आहार प्रदान करें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2557)
- **Original**: इति द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2558)
- **Original**: के के के
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2559)
- **Original**: 6.4ड सामवेट-संहिता
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2560)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

