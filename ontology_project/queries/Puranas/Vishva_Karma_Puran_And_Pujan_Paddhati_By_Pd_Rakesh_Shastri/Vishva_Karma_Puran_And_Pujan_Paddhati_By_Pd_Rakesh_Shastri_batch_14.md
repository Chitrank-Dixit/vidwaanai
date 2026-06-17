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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.261)
- **Original**: जलें पिवेदुषः काले कवचे नाभिमंगितमु
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.262)
- **Original**: बाल ग्रहामहारोगा नाशमायातितत्क्षसात्‌
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.263)
- **Original**: संततिः कनंकचायुरारोग्वैश्वय- मंगलमू
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.264)
- **Original**: कवचं यः पठेतस्य वर्द्धते शुक्ल चंद्रवत्‌
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.265)
- **Original**: गुरुभक्ता यदातव्यंना भक्तायकदाचनः
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.266)
- **Original**: गुल्लादूगुत्यतरंग गुह्ं गुणेरात्मद्रदर्शनम्‌
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.267)
- **Original**: इतिकवचं पठित्वा
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.268)
- **Original**: पुनः लं पृथ्वी तत्वामन इत्यादिपि गंधादि सर्वोंपचारान्‌ मनसासमर्षयामीत्यु्त त्वा प्रार्थयेत
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.269)
- **Original**: यस्यस्मृत्या चना भोक्त्याजप पूजादि कर्मसु
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.270)
- **Original**: न्यून॑ संपूर्ण तोपातिनभस्त हिश्व कर्मणो
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.271)
- **Original**: इति श्री विश्व सारोद्धारतन्त्रे शिव ब्रह्मसंवादे विश्वकर्मपरब्रह्म कवचस्तो्रं संपूर्णामस्तु ऊ तस्सादिश्वकर्म पर ब्रह्मार्पणामस्तु
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.272)
- **Original**: शिवमस्तु
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.273)
- **Original**: श्री गणेशायनम:
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.274)
- **Original**: अथ श्री विश्वकर्म नामाष्टोत्तरशतक प्रारम्म:
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.275)
- **Original**: अस्य श्री विश्व कर्मनामाष्टोत्तर शतक
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.276)
- **Original**: 22 श्री विश्वकर्मा पुराण एवं पूजन पद्धति
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.277)
- **Original**: स्तोत्र मंत्रस्य ब्रह्मा ऋषि
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.278)
- **Original**: श्री विश्वकर्मा देवता
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.279)
- **Original**: अनुष्टुपछंदः
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.280)
- **Original**: सर्वाभीष्ट सिद्प्यर्थ श्री विश्वकर्मप्रीत्यर्थ जे विनियोग:
- **Translation**: 

---

