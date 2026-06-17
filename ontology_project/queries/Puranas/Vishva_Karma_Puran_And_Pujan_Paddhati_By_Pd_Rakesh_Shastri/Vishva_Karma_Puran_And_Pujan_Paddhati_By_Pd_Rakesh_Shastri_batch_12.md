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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.221)
- **Original**: अस्य श्री विश्दकर्म परब्रह्मककवचस्तो नरमत्रस्थ सानगादि . पंच ऋषयः
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.222)
- **Original**: अनुष्टुप छंदः
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.223)
- **Original**: विश्वकर्मपरब्रह्मदेवता
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.224)
- **Original**: अं बीजमू
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.225)
- **Original**: क्लीं शक्ति:
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.226)
- **Original**: हीं कीलकें
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.227)
- **Original**: ममधर्मज्ञानार्थसिदूध्यर्थ विश्वकर्मपरब्रह्न प्रसाद सिदूध्यर्थ कवचस्त्रोतपारायणेविनियोग:
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.228)
- **Original**: मूलेन पूर्ववन्न्यासंकृत्वा
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.229)
- **Original**: ध्यानं
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.230)
- **Original**: पंचकन्रंदशभुन्र॑ त्रिनेत्रं दंड घारिणम्‌
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.231)
- **Original**: ध्यात्वाश्री विश्वकर्माणां वारिवाहों परिस्थितिमू
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.232)
- **Original**: मानसै रेवसंपूज्यहयु पचारैद्रष्टाभिः
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.233)
- **Original**: शुचिः ततः पठेद्विव्य॑ कवच विश्वकर्मणः '
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.234)
- **Original**: विश्वकर्माशिर: पातु ललाटंपातु मेमनुः
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.235)
- **Original**: कालदेशंमयः पातुत्वष्टानेजयुगंतथा
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.236)
- **Original**: शिल्पी गंडदयंपातु दैवज्ञ' पातुवोष्टकौ
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.237)
- **Original**: अं बीजं वदनंपातः क्लीं बीजं कंठदेशकं
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.238)
- **Original**: हीं बीज॑ हृदयंपातु चोदरंथातुमहीश्वरः ब्रह्मातुनाभिदेशंव मध्यंपातुमनो भवः
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.239)
- **Original**: कटथ्सीज्ञपतिः पातु पातुचोरुमहेश्वरः
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.240)
- **Original**: जानुदेशेपर ब्रह्मानंधे पातु विराद् प्रभु:
- **Translation**: 

---

