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

### Verse 1 (Vishnu Puran 0.1)
- **Original**: पानतयपजथ जम: श्रीविष्णुपुराण छवि प्रथम अंश पा नारायण नमस्कृत्य नर॑ स्व नरोत्तमम्‌। देवीं सरस्वती व्यास ततो जयमुदीरयेत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2)
- **Original**: पहला अध्याय ग्रन्धका उपोद्घात अ्ीसूत उच्च 34 पराझरे मुनिवर॑ कृतपौर्वाहिकक्रियम्‌। मैत्रेय: परिपप्रच्छ प्रणिपत्याभिवाद्य च
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3)
- **Original**: 1 त्वत्तो हि वेदाध्ययनमधीतमखिले गुरो। धर्मशासत्राणि सर्वाणि तथाड्ञनि यथाक्रमम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4)
- **Original**: 2 स्वह्मसादाध्ुनिश्रे'्ठ मामन्ये नाकृतअ्रमम्‌। वक्ष्यन्ति सर्वझाम्रेषु प्रायझ्नो येउपि विद्विव:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5)
- **Original**: है सो5हपिव्छामि धर्मज्ञ श्रोतुं त्कत्तो यथा जगत्‌ । बभूव भूयक्ष यथा महाभाग भविष्यति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6)
- **Original**: 4 यत्य्य॑य ज्॒ जगड्रह्मान्यतऔैतशराचरम्‌ । लीनमासीदहाथा यत्र लयमेध्यति यत्र ख।
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7)
- **Original**: 5 चद्मपराणानि भूतानि देवादीनां च सम्भवम्‌। समुद्र्पर्वतानों च संस्थान तर यथा भुवः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8)
- **Original**: 6 सूर्यादीनां घ संस्थान प्रपाणं मुनिसत्तम
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9)
- **Original**: देवादीनां तथा संज्ाअनूतमन्वत्ताणि च
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10)
- **Original**: 7 करूपान्‌ कल्पविभागांश्र चातुर्पुरविकल्पितान। कल्पाशत्य स्वरुप थे युगधर्माश कृत्छाशः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11)
- **Original**: 8 श्रीसूतजी ब्रोले--मैप्रेयजीने निश्यकमोंसे नियुत्त हुए मुनियर पराशरजीको प्रणाम कर एवं उनके चरण छूकर पूछा--
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12)
- **Original**: “हे गुरूदेय ! मैंने आपहोसे सम्पूर्ण वेद, केदाड़ और सकल घर्मशास्नोका क्रमशः अध्ययन किया है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13)
- **Original**: हे मुनिश्रेष्ठ ! आपकी कृपासे मेरे विपक्षी भी मेरे खिये यह नहीं कह सकेंगे क्रि 'मैंने सम्पूर्ण झास्ोंकि अध्यासमें परिश्रम नहीं क्रिया'
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.14)
- **Original**: हे धर्मज्ञ ! हे महाभाग ! अब मैं आपके मुखारविन्दसे यह सुनना चाहता हूँ कि यह जगव्‌ किस प्रकार उत्पन्न हुआ और आगे भी (दूसरे कल्फ्के आरम्भमें) कैसे होगा 7
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.15)
- **Original**: तथा हे ब्रह्मन्‌ ! इस संसारका उपादान-करण क्या है ? यह सम्पूर्ण शरायर किससे उत्पन्न हुआ है ? यह पहले किसमें लीन था >हैर आगे किसमें ह्मीन हो
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.16)
- **Original**: जायगा ?
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.17)
- **Original**: इसके अतिरिक्त ( आकाश आदि ] भूतोंका परिमाण, समुद्र, पर्वत तथा देवता आदिकों उत्पत्ति, पृथिवीका अधिफ्तान और सूर्य आदिक्य प्रिमण तथा ऊतका आधार, देखता आदिके यश, सनु. मन्यत्तर, (बार-बार आनेवाले] चारों यूगोंमें खिघक्त कल्प
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.18)
- **Original**: 2 श्रीविष्णुपुराण [ अ> 1 देवर्षिपार्थिवानां च चरित॑ यन्महामुने । वेदशाखाप्रणयनं यथावद्दयासकर्तृकम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.19)
- **Original**: 9 धर्माश्न ब्राह्मणादीनां तथा चाश्रमवासिनाम्‌ । श्रोतुपिच्छाम्यहं सर्व त्क्‍्तो वासिप्ठनन्दन
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.20)
- **Original**: 10 ब्रह्मग्रसादप्रवर्ण कुरुत्च पथि मानसम्‌। येनाहमेतज्जानीयां. त्वत्प्रसादान्पहामुने
- **Translation**: 

---

