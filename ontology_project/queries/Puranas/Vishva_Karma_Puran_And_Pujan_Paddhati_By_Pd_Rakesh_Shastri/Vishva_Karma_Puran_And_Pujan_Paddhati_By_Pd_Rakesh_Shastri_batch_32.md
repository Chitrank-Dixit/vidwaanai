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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.621)
- **Original**: विश्वकर्मा चालीसा दोहा-. मनु मय त्वष्टा विश्वकर्मा, शिल्प कर्म आधार। तीन लोक चौदह भुवन, करनी का विस्तार
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.622)
- **Original**: सोरठा-प्रत्न सुपर्ण महाराज, सनग सनातन अहिमून। शिल्पन के सरताज, आदि शिल्प के गुरु तुम
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.623)
- **Original**: जगत गुरु जग ईश पियारे। विश्वकर्मा. महाराज. हमारे
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.624)
- **Original**: देव दनुज सबके दुख टारे। दीनन के तुम हो रखवारे
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.625)
- **Original**: ' जल, थल, पर्वत और अकाशा।
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.626)
- **Original**: '... श्री विश्वकर्मा पुराण एवं पूजन पद्धति 207
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.627)
- **Original**: चांद सूर्य नित करहिं प्रकाशा
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.628)
- **Original**: - नाथ तुम्हारी अद्भुत करनी । महिमा अमित जाहि नहिं बरनी
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.629)
- **Original**: सृष्टि आदि कर्ता हो स्वामी । बार बार है तुम्हें नमामी
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.630)
- **Original**: भव निधि पड़े बहुत दुख पाये । सब तजि शरन तुम्हारी आये
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.631)
- **Original**: जप तप भजन न होय गोसाई । बंधे कीट मर्कट की नाई
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.632)
- **Original**: बस्घन छोर हमें अपनाओ । निज चरणों का दास बनाओ
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.633)
- **Original**: जयति-जयति विश्वकर्मा स्वामी । मम उर बस नाथ विज्ञानी
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.634)
- **Original**: सुमिरन सजन तुम्हारा भावै। बुरे कर्म से मन हट जावे
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.635)
- **Original**: साधु सन्त के तुम रखवारे। भक्त जनन के प्राण पियारे
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.636)
- **Original**: स्वारथ वश तब भक्ति विसारी। नाथ पड़ा हूं शरण तुम्हारी
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.637)
- **Original**: तुरमहिं भजै अक्षय सुख पावै। जन्म जनम के दुःख विनसावै
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.638)
- **Original**: पुरवहु॒ नाथ. मनोरथ. मोरा। मन क्रम वचन दास मैं तोरा
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.639)
- **Original**: एक. लालसा... यही हमारी । केवल भक्ती चहीं तिहारी
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.640)
- **Original**: मंगल करन अम्ल हारी। निभुवन महिमा विदित तुम्हारी
- **Translation**: 

---

