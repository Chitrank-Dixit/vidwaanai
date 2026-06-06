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

### Verse 1 (Sama Ved 0.1821)
- **Original**: 704, ऊर्जो नपातं स हिनायमस्मयुर्दाशेम हव्यदातये । भुवद्वाजेष्वविता भुवदवृथ उत त्राता तनूनाम्‌
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1822)
- **Original**: बल-पराक्रम को सतत बनाये रखने वाले अग्निदेव की हम प्रार्थना करते हैं ! वे निश्चय ही हमारे लिए हितकारी हैं । वे हमारे हव्य को देवताओं तक पहुँचाते हैं । युद्ध में वे हमारी रक्षा करते हुए उन्नति में सहायक और हर प्रकार से हमारी रक्षा करने वाले सिद्ध हों
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1823)
- **Original**: 705. एब्टा षु ब्रवाएि ते5ग्न इत्थेतरा गिर:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1824)
- **Original**: एशिरवर्धास इन्दुभि:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1825)
- **Original**: उत्तम विधि से की गई हमारी स्तुति से प्रसन्न होकर हे अग्विदेव ! आप प्रकट हों । यह सोमरस आपको वृद्धि प्रदान करने वालः है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1826)
- **Original**: 706. यत्र क्‍्व च ते मनो दक्षं दधस उत्तरम्‌। तत्र योनि कृणवसे
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1827)
- **Original**: है अग्निदेव ! आप जिस याजक से प्रसन होते हैं, उसे बल और श्रेष्ठ आवास प्रदान करते हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1828)
- **Original**: 707, न हि ते पूर्तमक्षिपद्‌भुवन्नेमानां पते । अथा दुबो वनवसे
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1829)
- **Original**: है अग्निदेव ! आपका तेज चक्षुओं के लिए हानिकारक नहीं है । हे व्रतपालक, मानवों के स्वामी ! आप हमारी प्रार्थना स्वीकार करें
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1830)
- **Original**: 708. वयपमु त्वामपूर्व्य स्थूरं न कच्चिद्‌भरन्तो5वस्यवः । बच्ि चित्र हवामहे
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1831)
- **Original**: है वद्धपाणि इन्द्रदेव ! सोमप्रदाता हम, आपको अपनी रक्षा के लिए उसी प्रकार आवाहित करते हैं, जैसे निर्बल व्यवित द्वारा सामर्थ्यवान्‌ को बुलाया जाता है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1832)
- **Original**: 709. उप त्वा कर्मननूतये स नो युवोग्रश्चक्राम यो धृषत्‌
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1833)
- **Original**: त्वामिध्यवितारं ववृमहे सखाय इन्द्र सानसिम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1834)
- **Original**: हे शत्रु-संहारक देवेन्द्र ! हम कर्मशील रहते हुए सहायता के लिए तरुण और शूरवौर रूप में विद्यमान आपका आश्रय लेते हैं। मित्रवत्‌ सहायता के लिए हम आपको पुकारते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1835)
- **Original**: 710.अधा हीन्द्र गिर्वण उप त्वा काम ईमहे ससृग्महे । उदेव ग्मन्त उदभि:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1836)
- **Original**: हे स्तुत्य इन्द्रदेव ! पानी ले जाते हुए, जल फेंककर खेलते मनुष्य की भाँति, हम आपके पास आकर अपनी इच्छा- तृप्ति की प्रार्थना करत हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1837)
- **Original**: 18 सापवेद- संहिता 7191.वार्ण त्वा यव्याभिर्वर्धन्ति शूर ब्रह्माणि। वावृध्वांसं चिदद्विबों दिवेदिवे
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1838)
- **Original**: है वज़धारी-शूरवीर इन्रदेव ! जैसे नदियों के जल से समुद्र कौ गरिमा बढ़ती है, उसी तरह हम अपनी स्तुतियों से आपकी गरिमा का विस्तार करते हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1839)
- **Original**: 712.युझ्ञन्ति हरी इषिरस्यथ गाथयोरौ रथ उरुयुगे वचोयुजा । इन्द्रवाहा स्वर्विदा
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1840)
- **Original**: गतिशील इन्द्रदेव के महान्‌ रथ में आज्ञा मात्र से हो श्रेष्ठ घोड़े जुड़ जाते हैं । वे स्तुति करने बालों के स्तोत्र से उत्साहित हो गन्तव्य तक पहुँचाते हैं
- **Translation**: 

---

