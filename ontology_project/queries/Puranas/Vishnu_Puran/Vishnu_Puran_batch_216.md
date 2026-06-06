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

### Verse 1 (Vishnu Puran 0.4301)
- **Original**: 13) &2&: 7 छझीवअंश ॒॑ऋझऋझऋझऋ ्ूक्‍ऋचच 253 153 सकता' इसी बातको सुननेकी मुझे इच्छा हो रही आत्मन्येष न दोषाय शब्दोउहमिति यो द्विज
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4302)
- **Original**: हे ब्रह्मन्‌ ! 'जो है [अर्थात्‌ जो आत्मा कर्त्ता- भोक्तारूपरो ब्राह्मण उवाच शब्दो5हमिति दोषाय नात्मन्येष तथैव तत्‌। अनाह्मन्यात्मविज्ञानं शब्दो वा प्रान्तिकक्षण:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4303)
- **Original**: 86 जिड्ढा ब्रवीत्यहमिति दल्तोष्ठी तालुके नृष । एते नाह॑ यतः सर्ते ब्राढनिष्पादनहेतव:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4304)
- **Original**: 87 किं हेतुभिर्वदत्येषा बागेबाहमिति स्वयम्‌। अतः: पीवानसीत्येतद्ृक्तुमित्थ॑ न युज्यते
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4305)
- **Original**: 88 पिण्ड: पृथम्यत: पुंसः झिर:पाण्यादिलक्षण: । ततो5हमिति कुप्रैतां संज्ञां राजन्करोम्यहम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4306)
- **Original**: 89 यदान्तो5स्ति पर: को5पि मत्त: पार्थिवसत्तम । तदैषोडहमयं चान्यो वक्तुमेवमपीष्यते
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4307)
- **Original**: 90 सह का पदक यत, । तदा हि को खच:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4308)
- **Original**: 919 त्वै राजा शिब्रिका चेयपिमे वाहा: पुरःसरा: । अय॑ च भवतो छोको न सदेतन्नपोच्यते
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4309)
- **Original**: 92 वृक्षाह्रू ततश्षेयं शिबिका त्वदश्चिष्ठिता । कि वृक्षसंज्ञा वास्या: स्याह्ारुसंज्ञाथ वा नुप
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4310)
- **Original**: 93 वृक्षारूढो महाराजो नाय॑ वदति ते जनः । नच्न दारुणि सर्वस्त्वां ग्रवीति शिविकागतम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4311)
- **Original**: 94 शिबिका दारुसट्भातो रचनास्थितिसंस्थितः । अन्विष्यतां नृपश्रेष्ठ तद्भेदे शिब्विका त्वया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4312)
- **Original**: 95 एवं छत्रशलाकानां पृथग्भावे विमृइयताम्‌ । क्व यात॑ उत्रमित्येष न्यायस्त्वयि तथा मयि
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4313)
- **Original**: 96 पुमान्‌ स्त्री गौरजो वाजी कुझरो विहगस्तरु: । देहेषु लछोकसंज्ञेयं विज्ञेया कर्महेतुषु
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4314)
- **Original**: 97 पुमान्न देवों न नरो न पशुर्न च पादप: । आरीराकृतिभेदास्तु भूपैते कर्मयोनयः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4315)
- **Original**: 98 से प्रतीत होता हुआ सदा सत्तारूपसे वर्तमान है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4316)
- **Original**: वहीं मैं हैं --ऐसा क्यों नहीं कहा जा सकता ? हे ट्विज ! यह 'अहं' शब्द तो आत्मामें किसी प्रकारके दोषका कारण नहीं होता
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4317)
- **Original**: ब्राह्मण बोले--हे राजन्‌ ! तुमने जो कहा कि 'अहे' शब्दसे आत्मामें कोई दोष नहीं आता सो ठीक ही है, किन्तु अनात्मामें ही आत्मस्थका ज्ञान करानेवात्म्र भ्रान्तिमूलक अहं' द्ञाब्द ही दोषका कारण है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4318)
- **Original**: है नूप ! 'अहें' शब्दका उचारण जिह्ा, दत्त, ओछ और तालसे हो होता है, किक्तु ये सब उस ञब्दके उच्चारणके कारण हैं, 'अहं' (मैं) नहीं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4319)
- **Original**: तो क्‍या जिह्मादि कारणोंके द्वारा यह वाणो हो स्वयं अपनेको 'अहं' कहतो है ? नहों । अतः ऐसी स्थितिमें 'तू मोद। है' ऐसा कहना भी डचित नहीं है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4320)
- **Original**: सिर तथा कर-चरणादिरूप यह दारीर भी आत्मासे पृथक्‌ ही है
- **Translation**: 

---

