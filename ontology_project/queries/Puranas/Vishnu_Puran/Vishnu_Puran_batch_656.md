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

### Verse 1 (Vishnu Puran 0.13101)
- **Original**: कि'मगैशं बाहुनाग्‌ 4 महे 2 एप तूदेशतों लेडा: 4 24 हएरर
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13102)
- **Original**: कथित खूर्पबातत्य 8 ज्कुद्धा 30 एप मोह गठ: कृष्णः 5 7 19
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13103)
- **Original**: किदस्पत्कुले जातः इफाउह2 पर हुए एप रामेण सहित: 5 18 26.
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13104)
- **Original**: कट्यमुफुटणमीविय्दिभेदे: इ 7 66 एप ऊष्णस्थस्पो्च: 84-38 315
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13105)
- **Original**: $कण्टकाजटज़ाज़ दाग ज धाम हर एप सतह: सुध्‌ 56 27 26
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13106)
- **Original**: क्डु्नम मुनि: पूर्वम्‌ 44 5 एव द्वीप: समुप्रेण 2 ड 33 ।कम्यूयनेरषप चासक्त' बहु 0562 एप साम्वस्सपत्रोक: 56 35 4
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13107)
- **Original**: कमण्योरफ्तसमेय सर श 158 41 एप नैमिचिको नाम & 4 7
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13108)
- **Original**: कण्वाष्पेधातिधिः शाफरए हल एगा मड्ो देश महोग्रमूत्तः «6. 36 587
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13109)
- **Original**: कंथयामियकापूर्तम्‌ कफृआएकातउार एच वसुपती क्रय 2 1536 286
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13110)
- **Original**: कंगमेषिस्सट्यत्तार्‌ हि हूं हट एवं सृत्प्रिशतिभ्याग्‌ है & 30
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13111)
- **Original**: कययवत्से केस्यायपात्पण: 4: ऋशऊांप्स एवं ज्येष्टो बोतिहोत्र: 4 (69. रंडट
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13112)
- **Original**: कक्‍मेष केडायान्‌ डे 24 128 एपप रथगारुदा 5 18 ₹र9
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13113)
- **Original**: कथापारीसत्वमवाप यह 4. 24 (8 एब्रेहि हुए वृष्णोइहम्‌ 5 शृ6ू 7
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13114)
- **Original**: कथितस्तामसः स्ः श 2 8#एफलू शेः कथित गे लगा सका 1 10
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13115)
- **Original**: फेद्रमिद्र; परे स्थानम्‌ 1 916 47.
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13116)
- **Original**: कक्षितो भकता ऊंड: 1 16 4 ऐक्यलित गठड: 5 30 86.
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13117)
- **Original**: रऋथितों भक्ता ब्रकून्‌ 3322, श्‌ ऐेल्टैलस्प दृष्यत्त त्‌ ना अं हर 9.
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13118)
- **Original**: फथित भूत जह्मन्‌ अदा ह्‌ ऐश्वर्यमददुग्ात्मन्‌ 0”. है 69 12
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13119)
- **Original**: कयिता गुरुणा सम्बक [064 4 ऐश्वर्यस्प समप्रस्य 7. 6 7 उड़े
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13120)
- **Original**: कॉयेते चातुपधग्यम्‌ बं> नह
- **Translation**: 

---

