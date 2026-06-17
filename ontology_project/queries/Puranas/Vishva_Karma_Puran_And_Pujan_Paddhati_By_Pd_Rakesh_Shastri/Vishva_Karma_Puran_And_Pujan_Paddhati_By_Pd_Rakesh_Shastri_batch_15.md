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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.281)
- **Original**: अथध्यानमू
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.282)
- **Original**: पंचाननो दशमुजा घृतवद दीक्ष: कंयूरहारमणिकुंडलचंडतेजा:
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.283)
- **Original**: 1। भस्मांकितो मणि नयासन संस्थितोउसो सर्वे शवरोवसतुमेहदिविश्वकर्मा
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.284)
- **Original**: विश्वकर्मामनुसतवष्टास्थाष्ठि स्थविरो घुवः
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.285)
- **Original**: विष्णर्वे शवनरों योगी शिल्पाचार्य: क्रियपरः
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.286)
- **Original**: अमयी निर्भय: शांतः सत्यव्यामः सतां प्रिय:
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.287)
- **Original**: लीकाध्यक्ष: लुराध्यक्षो वरदो5मयदोवरः
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.288)
- **Original**: मयोमन्दर्महातेजा: शिव योगी हरिप्रियः
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.289)
- **Original**: लोकाध्यक्ष: लुराध्यक्षो वरदोडमयदोवरः
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.290)
- **Original**: मयोमन्द्रमहातेजा: शिव योगी हरिप्रियः # कायदः शयदः कांतः कुलीन कौशल प्रद:
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.291)
- **Original**: दातासत्य: स्वरादिगिज्ञेगृहस्थाशमिणोमतिः
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.292)
- **Original**: वनवासी महामायों रूपाध्यक्षोद्म चिंतित:
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.293)
- **Original**: स्वापनः शाघ्र -सोचिंत्य: कौशलः कर्मठोनर:
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.294)
- **Original**: जटीमुंडी शिखीदेवः संवृत्तांग: पिशाचराटू
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.295)
- **Original**: शास्त्रविधिविधिकरो लो केश: पावन: परः
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.296)
- **Original**: हरोबुद्धि प्रदो5नंतः सत्यसंकल्पईश्वरः
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.297)
- **Original**: सत्यकामः सत्यरूचिः सत्यार्थ: शंपवः शिव:
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.298)
- **Original**: नादप्रियोबो घकर्ता करणा श्री रायुघप्रियः
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.299)
- **Original**: घना खड़गी ध्वजीवर्मी शूली चक्रोकपालभूत
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.300)
- **Original**: अजरो प्रणवो व्यक्तोव्यक्त: कृष्णोयजुर्डविः
- **Translation**: 

---

