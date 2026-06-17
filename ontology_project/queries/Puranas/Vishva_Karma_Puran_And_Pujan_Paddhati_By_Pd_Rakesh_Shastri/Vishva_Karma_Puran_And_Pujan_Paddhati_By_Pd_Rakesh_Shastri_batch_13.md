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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.241)
- **Original**: पदौददेनो सदापातु सर्वाग विश्वकर्मकः
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.242)
- **Original**: सचद्योजात पूर्वदिशिवामदेवंतु दक्षिणे
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.243)
- **Original**: अधोरंपश्चिमेपातु तत्पुरुष॑चोत्तरे तथा
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.244)
- **Original**: ईशानंपातुचो ध्वया घः पातुमहीश्वरः
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.245)
- **Original**: आनेय्यांपातुचेशा नोनैकऋत्ये थिरिजापति:
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.246)
- **Original**: वायव्येपातुमां घावाचे शान्येपातु विश्वसुक्‌
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.247)
- **Original**: प्रथिव्यांसानगः पातु जले पातु सनातनः
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.248)
- **Original**: आकाशे चाहभूनों मांपातु प्रलस्क्वसर्वतः
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.249)
- **Original**: सुपर्ण: सर्वदा पातुसर्वसंकटनाशनः
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.250)
- **Original**: य इदंब्रह्मककवर्च न्रैलोक्येचापिदुर्लभम्‌
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.251)
- **Original**: शुचिर्मृत्वपठे नित्यंकवच॑ पापनाशनमू
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.252)
- **Original**: भूतप्रेतापिशाचादि कूष्मांड ब्रहमराक्षसा:
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.253)
- **Original**: दिवाचरात्रिचरामहाभूतगणाः: खगाः
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.254)
- **Original**: सुकुदुच्चारणादेव नाशंयातिनसंशय:
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.255)
- **Original**: महादरिद्रयुक्तोवायुक्तोवा सर्वपातकै:
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.256)
- **Original**: मुच्यते सर्वपापेक्य: श्रीमानू सर्वसुखीभवेतू
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.257)
- **Original**: गच्छेदू द्रह्ममयं देहाविश्वकर्म मुजोदूतय
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.258)
- **Original**: विश्वकर्मा व्यकवचं यः पठोसततंनरः
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.259)
- **Original**: अन्नपानसदासष्टिर्धनधान्यादि जायते
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.260)
- **Original**: अमेन :' सहशीमंत्रोनभूतो न भविष्यति
- **Translation**: 

---

