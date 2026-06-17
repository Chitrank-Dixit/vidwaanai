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

### Verse 1 (Vaivtpuran 19.6914)
- **Original**: छायाकी भाँति सदा उसके साथ लगी रहती हैं। इसका विनियोग कहा गया है। इस कवचके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 19.6915)
- **Original**: जो मन्दबुद्धि इस कवचकों बिना जाने ही धारण करनेसे लोग सर्वत्र विजयी होते हैं। पद्मा [लक्ष्मीकी भक्ति करता है, उसे एक करोड़ जप
- **Translation**: 

---

### Verse 3 (Vaivtpuran 19.17742)
- **Original**: + शियस्तोत्राणि * ज्ट्ष अंक्कफऋफऋ कफ कक कक कफ कक; 44% ###%######%############ऋ######%&##%#############%ऊक ;$ बाणासुरकृतं न्स्च्् सौतिरुवाच इदं चर कबचं प्रोक्‍्त॑ स्तोत्र च श्रणु शौनक । मन्त्राज: कल्पतरुव॑सिष्टो.. दत्तवानू. पुरा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 19.17743)
- **Original**: 34 नप्त: शिवाय। बाणासुर उवाच बन्दे सुराणां सारं च सुरेश नीललोहितम्‌ । योगीश्वर॑ योगबीर्ज योगिनां च्॒गुरोर्गुरुम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 19.17744)
- **Original**: ज्ञानानन्द ज्ञानरूपं ज्ञानबीज॑ सनातनम्‌ । तपसां फलदातारं॑ दातारं सर्वसम्पदाम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 19.17745)
- **Original**: तपोरूप तपोब्रीज॑ तपोधनधन वरम्‌ । वर वरेण्य वरदमीड्य॑ सिद्धगणैर्वरै
- **Translation**: 

---

### Verse 7 (Vaivtpuran 19.17746)
- **Original**: कारणं भक्तिमुक्तीनां नरकार्णवतारणम्‌ । आशुतोष॑ं प्रसन्नास्यं करुणामयसागरम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 19.17747)
- **Original**: हिमचन्दनकुन्देन्दुकुमुदाम्भोजसंनिभभू._। ब्रहाज्योतिःस्वरूप॑ अ भक्तानुग्रहविग्रहम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 19.17748)
- **Original**: विषयाणां विभेदेन बिश्रन्त बहुरूपकम्‌ । जलरूपमग्निरूपमाकाशरूपपी श्वरम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 19.17749)
- **Original**: वायुरूपं चन्धरूपं सूर्यरूपं महत्प्रभुप्‌ । आत्मन: स्वपद॑ दातुं.. समर्थमवलीलया
- **Translation**: 

---

### Verse 11 (Vaivtpuran 19.17750)
- **Original**: भक्तजीवनमीशं च भक्तानुग्रहकातरम्‌ । वेदा न शक्ता य॑ स्तोतुं किपहे स्तौमि तं प्रभुम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 19.17751)
- **Original**: अपरिच्छिन्नमीशानमहो वाइमनसो: परम्‌ । व्याप्नचर्माम्बरथरं वृषभस्थं दिगम्बरम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 19.17752)
- **Original**: ब्रिशूलपट्टिशधरं सस्मितं चन्द्रशेखरम्‌ । इत्युक्त्वा स्तवराजेन नित्यं बाण: सुसंयत:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 19.17753)
- **Original**: प्राणमच्छंकरं भक्त्या दुर्वासाश्न मुनीश्चरः
- **Translation**: 

---

### Verse 15 (Vaivtpuran 19.17754)
- **Original**: इर्द दत्त वसिष्ठेन गन्धर्वाय पुरा मुने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 19.17755)
- **Original**: कथितं च महास्तोत्र शूलिनः परमादभुतम्‌ । डूदं स्तोत्र महापुण्यं पठेद्‌ भकत्या च यो नरः
- **Translation**: 

---

### Verse 17 (Vaivtpuran 19.17756)
- **Original**: स्तानस्थ सर्वतीर्थानां फलमाप्रोति निश्चितम्‌ । अपुत्रो लभते पुत्र वर्षमेक॑ श्रृणोति यः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 19.17757)
- **Original**: संयतश्न हविष्याशी प्रणम्य शंकर गुरुम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 19.17758)
- **Original**: गलतल्कुष्ठी महाशूली वर्षमेक॑ श्रुणोति यः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 19.17759)
- **Original**: अबश्य॑ मुच्यते रोगाद्‌ व्यासवाक्यमिति श्रुतम्‌
- **Translation**: 

---

