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

### Verse 1 (Vishnu Puran 0.13201)
- **Original**: च्यकनात्सुदासः: सुदासात्‌ श्ड (4.
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13202)
- **Original**: सत्र फरल्िलिसनायि 43... खगासंझ्ा ददौ सापम्‌ 34.
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13203)
- **Original**: झयासंशसुते योज्सौ शृश.
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13204)
- **Original**: 9अंत्त वोरुधो यस्तु 6.
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13205)
- **Original**: डिल्रे बाहुको क्यु श्र 19
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13206)
- **Original**: जगदादौतधा नध्ये 0 जगत; प्रख्योत्प्यों: 22
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13207)
- **Original**: आादेतदतायारम्‌ 20.
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13208)
- **Original**: जात्वर्ग जगरूव 71
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13209)
- **Original**: जऊादिताभदाक्वर्यर 87.
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13210)
- **Original**: ऊदेशखगन्नाथ 132.
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13211)
- **Original**: जगतगुप्फाणय हु1
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13212)
- **Original**: जग़ाम वसुधा खोमर्‌ डई..
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13213)
- **Original**: जगाम सोर्अफेेकर्सम्‌ 25.
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13214)
- **Original**: जमुर्मुदै तहो देवा: 7.
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13215)
- **Original**: खपान धरणी पा: 16.
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13216)
- **Original**: जफत तेत विश्शेषात्‌ 65. जज्वाऊ गगर्शाशोह: छ4..
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13217)
- **Original**: जद देफकूटछ 80 37
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13218)
- **Original**: ज्लुपृहदस्थानों राखुपरतयासम्‌ 58
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13219)
- **Original**: जनपमैकेगिपिदेंव:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13220)
- **Original**: ... जनस्लेकगौस्सिद्े: 2.
- **Translation**: 

---

