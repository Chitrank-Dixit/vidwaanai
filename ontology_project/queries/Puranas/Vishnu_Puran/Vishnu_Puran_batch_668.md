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

### Verse 1 (Vishnu Puran 0.13341)
- **Original**: टस्सादुशोगरवितिक्ू 16.
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13342)
- **Original**: तस्पाण् महामराः 36.
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13343)
- **Original**: तंरनात्शालः इंडंड.
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13344)
- **Original**: तस्पादपि सज्ञवः शड.
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13345)
- **Original**: वणादुशना 12
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13346)
- **Original**: वराद्धाओण्यः 5
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13347)
- **Original**: तम्मादेतामह त्यक्त्वा कह.
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13348)
- **Original**: तस्माद्धिएण्यग्रपः हृ49
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13349)
- **Original**: तस्तान खक्ाड़- 180.
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13350)
- **Original**: तह्कादसमझराज्‌ 44 रामाद्धरोत: 21
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13351)
- **Original**: स्मात्क्पष्टमि: 40.
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13352)
- **Original**: लस्मादेत आगे नफन्‌ 16.
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13353)
- **Original**: तस्मात्पडिति कुर्याव्‌ 6.
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13354)
- **Original**: तस्मादध्पर्धपेषतस्‌ 45... तस्मात्रपमकोच्तम्‌ 11
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13355)
- **Original**: जष्मादुत्सपेशया: 63.
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13356)
- **Original**: क़्मात्खदाक्ता राजेद 5.
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13357)
- **Original**: तत्मादनुदिते सूर्य 15.
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13358)
- **Original**: तस्मादतिप्रिपूल्ययाम्‌ 63.
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13359)
- **Original**: कामात्सदाकाएका 20...
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13360)
- **Original**: तस्माष्फेयास्यसेफरणि 48. । तम्मात्पार्थ ने सन्‍्तापः 106.
- **Translation**: 

---

