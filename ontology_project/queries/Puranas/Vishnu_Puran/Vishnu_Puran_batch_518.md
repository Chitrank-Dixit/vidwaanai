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

### Verse 1 (Vishnu Puran 0.10341)
- **Original**: 24 ततः समस्तमझेषु नागरस्स तदा जनः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10342)
- **Original**: राजमञ्लेषु चारूढास्सह भुत्यर्नराधिपा:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10343)
- **Original**: 25 मल्लप्राभ्रिकवर्गश रड्डमध्यसमीपग: । कृतः कंसेन कंसो5पि तुड़मझे व्यवस्थित:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10344)
- **Original**: 26 अन्तःपुराणां मझ्नाश्व तथान्ये परिकल्पिता: । अन्ये ञ्र बारमुख्यानामन्ये नागरयोषिताम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10345)
- **Original**: 27 नन्दगोपादयो गोपा मज्ञेप॒न्येप्रवस्थिता: । अक््ूरवसुदेवौ च मम्नप्रान्ते व्यवस्थितो
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10346)
- **Original**: 28 जाशरीयोषितां मथ्ये टेवकोपरगर्खिनों । अन्तकालेउपि पुत्रस्य द्रक्ष्यामीति मुख स्थिता
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10347)
- **Original**: 29 वाचद्यमानेषु तूर्येषु चाणूरे चापि वल्गति। हाहाकारपरे लछोके ह्यास्फोटयति मुष्टिके
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10348)
- **Original**: 30 ईषद्धसन्ता तो वीरो बलभद्रजनार्दनो । गोपवेषधराौ बालौ. रघ्डद्धारमुपागतौ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10349)
- **Original**: 319 ततः कुबलयापीडो महामात्रप्रचोदित: । अध्यधावत वेगेन हन्तुं गोपकुमारकौ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10350)
- **Original**: 32 हाहाकारो महाक्ञज्ञे रड्रमध्ये द्विजोत्तम। बलदेवो5नुजं दृष्ठा बचने चेदमब्रवीत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10351)
- **Original**: 33 हन्तव्यों हि महाभाग नागो5यं शत्रुचोदित:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10352)
- **Original**: 34 इत्युक्तस्सोउग्रजेनाथ बलदेबेन नै द्विज । सिंहनादं ततश्षक्रे माधलः परवीरहा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10353)
- **Original**: 35 करेण करमाकृष्य तस्य केहिनिषूदनः । भ्रामयामास॒॑त॑ शौरिरिरावतसम॑ बले
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10354)
- **Original**: 36 ्रीविष्णुपुराण [ आअ*0 20 दोगे तो मैं तुष्हारी समस्त इच्छाएँ पूर्ण कर दूँगा; मेंरे इस कथनको लूम भिथ्या न समझना
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10355)
- **Original**: तुम न्यायसे अथवा अन्यायसे मेरे इन महाबलवान्‌ अपकारियोंको अवश्य मार डास्ओे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10356)
- **Original**: उनके मारे जानेपर यह सारा राज्य
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10357)
- **Original**: हमारा और ] तुम दोनॉंका सामान्य होगा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10358)
- **Original**: 19--21
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10359)
- **Original**: मल्स्म्रेंकों इस प्रकार आज्ञा दे ऊंसने अपने महावतकों बुल्थ्या और डसे आज्ञा दी कि तू कुनललयापोड हाथीको प्रल्छोकी रेगभूमिके द्वारपर खड़ा रत्त और जब .वे गोपकुमार युद्धके लिये यहाँ आदवें तो उन्हें इससे नष्ट करा दे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10360)
- **Original**: इस प्रकार उसे आज्ञा देकर और समस्त सिंहासनॉकों यधावत्‌ रखे देखकर, जिसकी मृत्यु पास आ गयी है बह कंस सूर्योदयकी प्रतीक्षा करने छगा
- **Translation**: 

---

