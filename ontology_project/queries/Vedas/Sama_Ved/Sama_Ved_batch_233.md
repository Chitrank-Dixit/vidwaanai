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

### Verse 1 (Sama Ved 0.4641)
- **Original**: 1831. अग्निज्योतिज्योतिरग्निरिन्द्रो ज्योतिज्योतिरिद्ध: । सूर्यों ज्योतिज्योति: सूर्य:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.4642)
- **Original**: अग्नि ज्योति है, और ज्योति ही अग्नि है । इन्द्र ज्योति है, और ज्योति ही इन्द्र है । सूर्य ज्योति है, और ज्योति ही सूर्य है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.4643)
- **Original**: 1832. पुनरूर्जा नि वर्तस्व पुनरग्न इषायुषा
- **Translation**: 

---

### Verse 4 (Sama Ved 0.4644)
- **Original**: पुनर्न: पाह्मांहसः
- **Translation**: 

---

### Verse 5 (Sama Ved 0.4645)
- **Original**: हे अनने ! ऊर्जा रूप (बल रूप) में हमारे पास आएँ । अन्न और आयु प्राप्त कराने वाले हों । पापों से हमारी बार-बार रक्षा करें
- **Translation**: 

---

### Verse 6 (Sama Ved 0.4646)
- **Original**: 1833. सह रण्या नि वर्तस्वाग्ने पिन्वस्व धारया । विश्वप्स्या विश्वतस्परि
- **Translation**: 

---

### Verse 7 (Sama Ved 0.4647)
- **Original**: *, अग्ने ! सब ऐश्वर्यों को साथ लेकर आएँ । दिव्य और सांसारिक ऐश्वर्यों के उपभोग में निहित आनन्द धारा से हमें सिंचित करें
- **Translation**: 

---

### Verse 8 (Sama Ved 0.4648)
- **Original**: इति षष्ठ: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.4649)
- **Original**: # के के
- **Translation**: 

---

### Verse 10 (Sama Ved 0.4650)
- **Original**: सप्तम: खण्ड:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.4651)
- **Original**: 1834. यदिद्धाहं यथा त्वमीशीय वस्व एक इत्‌ । स्तोता मे गोसखा स्थात्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.4652)
- **Original**: हे इन्द्रदेव ! आप धन के एकमात्र अधीश्वर हैं । यदि हम भी आपके समान ऐश्वर्यवान बनें, तो गौओं के मित्र गौओं के साथ हमारे प्रशंसक होंगे । (फिर आपके लिए भला क्या कहना !)
- **Translation**: 

---

### Verse 13 (Sama Ved 0.4653)
- **Original**: 1835. शिक्षेयमस्मै दित्सेयं शचीपते मनीषिणे । यदहं गोपति: स्थाम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.4654)
- **Original**: है इन्द्रदेव ! यदि हम (गौओं के स्वामी) ऐश्वर्यवान बनें, तो अपने बुद्धिमान प्रशंसक को घन देने की इच्छा करें और उसे धन प्रदान भी करें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.4655)
- **Original**: 1836. थेनुष्ट इन्द्र सूनता यजमानाय सुन्वते । गामश्वं पिप्युषी दुहे
- **Translation**: 

---

### Verse 16 (Sama Ved 0.4656)
- **Original**: हे इद्धदेव ! आपकी स्तुतियाँ गौ रूप धारण करती हैं और सोम यज्ञ करने वाले यजमान को पोषित करती हुई उसके इच्छित पदार्थों (गो-अश्व आदि) को उपलब्ध कराती हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.4657)
- **Original**: 1837. आपो हि ष्ठा मयोभुवस्ता न ऊर्जे दधातन । महे रणाय चक्षसे
- **Translation**: 

---

### Verse 18 (Sama Ved 0.4658)
- **Original**: है जल समूह ! आप सुख के उत्पत्तिकारक हैं । हमारे लिए बल, बैभव एवं दिव्य रमणीय ज्ञान प्रदान करने वाले बनें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.4659)
- **Original**: 1838.यो व: शिवतमो रसस्तस्य भाजयतेह न: । उशतीरिव मातर:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.4660)
- **Original**: हे जल समूह ! अपने अत्यन्त सुखकारी रस रूप का हमें सेवन करने दें । जैसे बच्चे को माता अपने दुग्ध रूप रस से पोषण देती है, वैसे ही हमें पोषित करें
- **Translation**: 

---

