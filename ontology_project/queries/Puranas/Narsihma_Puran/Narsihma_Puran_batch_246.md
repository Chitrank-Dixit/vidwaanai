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

### Verse 1 (Narsihma Puran 0.4901)
- **Original**: 15--225,
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.4902)
- **Original**: वह ठीर्थं तत्वज्जानों तपस्थो ऋषियोंद्वाय सेवित था। यहाँ मुनियोके सुरम्य आश्रम थे, जो पुराणोंमें प्रसिद्ध हैं। यह तोर्ष चक्रनदोसे भूषित है और वहाँके शिलाखण्ड भगवान्‌के चक्रसे चिट्ठित हैं। बह तो जितना ही सुरम्य था, उतना ही एकान्त। उसका विस्तार बड़ा था और वहाँ चित स्वत: प्रसन्न रहता था। वहाँपर कुछ चक्रसे चिह्ठित प्राणी रहते थे, जितका दर्शन बहुत हों पावन था। वहाँ पृण्यतोर्थके यात्रों यथ्वेष्ट विचस्ते रहते थे। उस महापरथ्ित्र शालग्रामक्षेत्रमें महामति पुण्डरीकजों प्रसस्नचित्त हो तीर्थ सेवन करने लगे।
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.4903)
- **Original**: 20178 श्रीनरसिंहपुराण ( अध्याय 64 नताॉोक्‍ी-->---फहफफ:फ-+-+न->+--7333क्‍क्‍ल्‍ल्‍ल्‍लल्‍ल्‍.ल्‍-क्‍->"*-::::::::::"क्‍ह.8------- पुण्डरीकः प्रसन्नात्मा तीर्थानि समसेवत। स्तात्वा देवहुदे तोर्थे सरस्वत्यां च सुव़्त:
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.4904)
- **Original**: 27 जातिस्मयाँ चक्रकुण्डे चक्रनगद्मामृतेष्वपि। तथान्यान्यपि तीर्थानि तस्मिन्नेव चचार सः
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.4905)
- **Original**: 28 ततः क्षेत्रप्रभावेण तीर्थानां चैब तेजसा। मनः प्रस्ादमगमत्तस्थ तस्मिन्महात्पन:
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.4906)
- **Original**: 29 सो5पि तीर्थे विशुद्धात्मा ध्यानयोगपरायण:। तत्रैव सिरिद्धमाकाइस्तन्‌ समाराध्य जगत्पतिम्‌
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.4907)
- **Original**: 30 शास्त्रोक्तेत विधानेन भक्त्या परमया युतः। उवास चिरपेकाकी नि्वन्द्रः संयतेन्द्रिय:
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.4908)
- **Original**: 31 शाकमूलफलाहार: संतुष्ट: समदर्शन:। यमैश्चल॒नियमैश्लैव॒ तथा चासनबन्ध्नै:
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.4909)
- **Original**: 32 प्राणायापै: सुतीक्षणैश्न प्रत्याहारैश्व संततेः:। धारणाभिस्तथा ध्यान: समाधिभिरतन्द्रित:
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.4910)
- **Original**: 33 योगाभ्यासं तदा सम्यक्‌ चक्रे विगतकल्मष:
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.4911)
- **Original**: आराध्य. देवदेवेशं . तदतेनान्तरात्मना
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.4912)
- **Original**: 34 पुण्डकीकों महाभाग: पुरुषार्थविशारद:। प्रसादं॑ परमाकाडशक्षन्‌ विष्णोस्तद्वतमानस:
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.4913)
- **Original**: 35 तस्य तस्मिन्रिवसत: शालप्रामे महात्मन:। पुण्डरीकस्य राजेन्द्र कालो5गच्छ्महांस्तत:
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.4914)
- **Original**: 36 मुने कदाचित्त देशं नारदः परमार्थवित्‌। जगाम सुमहातेजा: साक्षादादित्यसंनिभ:
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.4915)
- **Original**: 37 त॑ ड्रंह्टकामो देवर्षि: पुण्डरीक॑ तपोनिश्िम्‌। विष्णुभक्तिपरीतात्मा वैष्णवानां हिते रत:
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.4916)
- **Original**: 38 स॒ दृष्ठा नारदं प्राप्त सर्वतेजःप्रभान्वितम्‌। महामतिं महाप्राज्ज॑ सर्वागमविशारदम्‌
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.4917)
- **Original**: 39 प्राक्षलि: प्रणतो भूत्वा प्रहष्टेनान्तरात्मना। अर्ध दत्त्वा यथायोग्य॑ प्रणाममकरोत्‌ ततः
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.4918)
- **Original**: 40 को5यमत्यद्भुताकारस्तेजस्वी इद्यवेषधक्‌ । आतोद्यहस्त: सुपुस्तों जटामण्डलभूषण:
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.4919)
- **Original**: 41 विवस्थानथ वा वह्विरित्द्रों वरुण एवं वा। डति संचिन्तयन्‌ विप्र: पप्रच्छ परमद्ुति:
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.4920)
- **Original**: 42 जे नियमपूर्वक यहाँ देवहद तीर्थमें, पूर्वजन्यकी स्मृति दिलानेवाली सरस्वतोके जलमें, चक्र-कुण्डमें और चक्र- जदी (नारायणो)-के जलमें भी स्रान करके उसी क्षेत्रके अन्तर्गत अन्यान्य तीर्थोँमें भ्रमण कसो रहते थे
- **Translation**: 

---

