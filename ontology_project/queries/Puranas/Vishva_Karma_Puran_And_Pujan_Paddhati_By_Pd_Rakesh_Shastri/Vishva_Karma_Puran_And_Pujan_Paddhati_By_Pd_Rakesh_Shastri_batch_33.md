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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.641)
- **Original**: आरत-हरण भक्त भय हारी। शरण शरण मैं शरण तिहारी
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.642)
- **Original**: तुम सबके गुरु सबके स्वामी । तुम सबहीं के अन्तरयामी
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.643)
- **Original**: सर्व शक्ति तुम सब आधारा) तुमहिं भजै सो उतरहिं पारा
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.644)
- **Original**: घट घट माहिं तुम्हारो बासा । सर्व श्री विश्वकर्मा पुराण एवं पूजन पद्धति
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.645)
- **Original**: ठौर जिमि. दीप प्रकाशा
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.646)
- **Original**: यह विधि तुमको जाने कोई । भक्त अरु ज्ञानी कहिए सोई ही जगत पित्ता तुमहीं हो ईशा। याते हम विनवत जगदीशा
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.647)
- **Original**: नाथ कृपा अब हम पर कीजै
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.648)
- **Original**: भक्ति आपनी हमको दीजै
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.649)
- **Original**: प्रेम भक्ति बिनु कृपा न होई । सर्व शास्त्र में देखे जोई
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.650)
- **Original**: कर्म योग कर सेवत कोई। जो. हरि ज्योति आप प्रगटाई। घर घर में सोई दरशाई
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.651)
- **Original**: तुम सब ठौर सबन ते न्यारे। को लखि सके चरित्र तुम्हारे
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.652)
- **Original**: तुम सबके प्रभु अन्तरयामी। जीव बिसर रहे तुमको स्वामी
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.653)
- **Original**: विश्वकर्मा को जो कोई ध्यावै। होय मुक्ति जीवन फल पावै
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.654)
- **Original**: डूब न जावे नाव हमारी) हम आये हैं शरण तुम्हारी
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.655)
- **Original**: हम सेवक हैं. नाथ तुम्हारे। भव सागर से करो किनारे
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.656)
- **Original**: सुतत पितु मातु न कोई संघाती । सब तजि भजन करहुं दिन राती
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.657)
- **Original**: दीनबन्धु _ दीनन हितकारी। शरण पड़ा हूं नाथ तुम्हारी
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.658)
- **Original**: विश्वकर्मा ही. ब्रह्म कहावै। विश्वकर्मा सब सृष्टि रचावै
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.659)
- **Original**: पढ़े जो विश्वकर्मा चालीसा
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.660)
- **Original**: सुफल काज हों बीसों बीसा
- **Translation**: 

---

