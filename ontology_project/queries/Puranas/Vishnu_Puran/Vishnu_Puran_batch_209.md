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

### Verse 1 (Vishnu Puran 0.4161)
- **Original**: हे मैत्रेय ! गर्भपातके दोषसे तथा बहुत ऊँचे उछलनेके क्यूरण वह हरिणी भी पछाड़ खाकर गिर पड़ी और मर गयी
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4162)
- **Original**: उस हरिणीको मरी हुई देख तपस्वी भरत उसके बच्चेकों अपने आश्रमपर ले आये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4163)
- **Original**: है मुते ! फिर राजा भरत उस मृगछौनेक नित्यप्रति पाल्न-पोषण करने लूगे और वह भी उनसे पोषित होकर दिन-दिन बढ़ने लगा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4164)
- **Original**: वह बच्चा कभी तो उस आश्रमक्रे आसपास ही घास चरता रहता और कभी वनमें दुस्‍तक जाकर फिर सिंहके भयसे लौट आता
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4165)
- **Original**: प्रातःकाऊ वह बहुत दूर भी चला जाता, तो भी सायंकालको फिर आश्रममें हो लेट आता और भरतजीके आश्रमको पर्णशालाके आँगनमें पड़ रहता
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4166)
- **Original**: हे द्विज ! इस प्रकार कभी पास और कभी दूर रहनेवाले उस मृगमें ही राजाका चित्त सर्वदा आसक्त रहने छगा, बह अन्य तविषयॉक्ी ओर जाता ही नहीं था
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4167)
- **Original**: जिन्होंने सम्पूर्ण राज-पाट और अपने पुत्र तथा बच्धु- खान्धवॉको छोड़ दिया था ये डी भरतजों उस हरिणके खद्येपर अत्यन्त ममता करने लगे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4168)
- **Original**: उसे बाहर जानेके अनन्तर यदि स्प्रैटनेमें देरी हो जाती तो से मसन-ही-मन सोचने छगते 'अहो ! उस बच्चेको आज किसी भेड़ियेने तो नहीं खा लिया ? किसी सिंहके पञ्ेमें तो आज वह नहीं पड़ गया 2
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4169)
- **Original**: देखो, उसके खुरोंके चिह्ोंसे यह पृथिवी कैसी चिन्नित हो रही है ? मेरी ही प्रसन्नताके लिये उत्पन्न हुआ वह मृगछौना न जाने आज कहाँ रह गया है ?
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4170)
- **Original**: क्या यह बनसे कुशलपूर्वक त्मैटकर अपने सींगोंसे मेरे भुजाको खुजलाकर मुझे आनन्दित करेंगा ?
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4171)
- **Original**: देखो, उसके नवजात दाँतोंसे कटी हुई शिखाबाले ये कुश और काद सामाध्यायी [हिखाहीन] बह्मचारियोंके समान कैसे सुशोभित हो रहे हैं?
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4172)
- **Original**: देरके गये हुए उस बच्लेके निमित्त भरत. मुनि इसी प्रकार चिन्ता करने रूगते थे और
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4173)
- **Original**: आ्श3 ) छ दितीयअंश आर 9 द्वितीय अंश 149 समाधिभड्डस्तस्यासीत्तन्ययत्वाद्तात्यन: .। सन्त्यक्तराज्यभोगर्ड्धिस्वजनस्थापि भूपतेः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4174)
- **Original**: 29 चपले चपले तस्मिन्दूरगं दूरगामिनि । मृगपोते3भवश्चित्त स्थैर्यवत्तस्य भूपते:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4175)
- **Original**: 30 कालेन गच्छता सो5थ काल चक्रे महीपति: । पितेव सास्त्रं पुत्रेण मृगपोत्तेन वीक्षित:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4176)
- **Original**: 39 मृगमेव. तदाद्वाक्षीत््यजग्म्राणानसाबपि । ज़न्मयत्वेन मैत्रेय नान्यत्किज्लिद्चिन्तयत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4177)
- **Original**: 32 ततश्न तत्कालकृतां भावनां प्राप्य तादृशीम्‌। जम्बूमागें महारण्ये जातो जातिस्मरों मृग:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4178)
- **Original**: 33 जातिस्मरत्वादुद्टिम: संसारस्य द्विजोत्तम । विहाय मातरं भूयः झालग्राममुपाययों
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4179)
- **Original**: 34 जुष्कैस्तृणैस्तथा पं: स कुर्वन्नात्मपोषणम्‌ । मृगत्वहेतुभूतस्य कर्मणों निष्कृति ययौ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4180)
- **Original**: 35 तत्र चोस्सष्टदेहोउसौ जज्ञे जातिस्मरों द्विज: । सदाचारवतां शुद्धे योगिनां प्रवरे कुले
- **Translation**: 

---

