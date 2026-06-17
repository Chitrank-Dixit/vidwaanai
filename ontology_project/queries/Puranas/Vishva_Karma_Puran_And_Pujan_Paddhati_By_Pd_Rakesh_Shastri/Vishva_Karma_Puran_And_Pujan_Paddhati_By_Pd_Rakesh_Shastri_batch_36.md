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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.701)
- **Original**: श्री विश्वकर्मा की जय
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.702)
- **Original**: 206 श्री विश्वकर्मा पुराण एवं पूजन पद्धति
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.703)
- **Original**: श्री विश्वकर्मा जी की आरती जय श्री विश्वकर्मा, प्रभु जय श्री विश्वकर्मा । सकल सृष्टि के करता, रक्षक श्रुति घर्मा
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.704)
- **Original**: आदि सृष्टि में विधि को, श्रुति उपदेश दिया । जीव मात्र का जग में, ज्ञान विकास किया
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.705)
- **Original**: ऋषि अंगिरा तप से, शान्ति नहीं पाई। ध्यान किया तब प्रभु का सकल सिद्धि आई
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.706)
- **Original**: रोगग्रस्त राजा ने, जब आश्रय लीना। संकटमोचन बनकर, दूर दुःख कीना
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.707)
- **Original**: जब रक्षकार दम्पत्ति, तुम्हारी टेर करी। सुनकर दीप प्रार्थना, विपत्ति हरी सगरी
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.708)
- **Original**: एकानन . चतुरानन, . पंचानन राजे। दिभुज, चतुर्भुज, दशभुज, सकल रूप साजे
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.709)
- **Original**: ध्यान धरे तव पद का, सकल सिद्धि आवे। मन दिविधा मिट जावे, अटल शान्ति पावे
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.710)
- **Original**: थी विश्वकर्मा की आरती, जो कोई गावे। मजत यजानन स्वामी, सुख सम्पत्ति पावे
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.711)
- **Original**: शी विश्वकर्मा पुराण एवं पूजन पद्धति 207
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.712)
- **Original**: हमारे अन्य प्रकाशन : 4 श्री विश्वकर्मा पुराण #$ कृष्णनीति # सुन्दर कांड छ सम्पूर्ण आरती संग्रह है ( रंगीन चित्रों सहित ) % 'सशावतार # योगेश्वर कृष्ण 8 गंगापुत्र भीष्म छह सहाबत्नी भीम # अभिमन्यु 4? 'विश्वापभित्र श क्सुन्ती 4 द्रौपदी # महाभारत # हमारे देवी देवता # सरल रामायण के शिव तन्त्र # सनतों की वाणी %# अनमोत्न वचन प्रकाशक : साधना पॉकेट खुक्स ः : 39, यू0 ए0 बैंग्लो रोड, हज जवाहर नगर, दिल्‍ली-40007 किया
- **Translation**: 

---

