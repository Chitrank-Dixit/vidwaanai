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

### Verse 1 (Vishnu Puran 0.12981)
- **Original**: अजमीदस्थ नलिनी नाम 57 20 18
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12982)
- **Original**: अजगीदस्पान्य ऋक्षनामा 1 22 56
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12983)
- **Original**: अजचन्यमरे किष्णौ 1 2 20
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12984)
- **Original**: अजापतच विप्रोड्सौ 28 7.
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12985)
- **Original**: अज्ाहशरक 6 73 52
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12986)
- **Original**: अजानता कृतमिदम्‌ 5 दंड डंड
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12987)
- **Original**: अजीजनत्पुष्करिण्याम्‌ 5 1 26
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12988)
- **Original**: अज्ञान॑ तामसो भाव: 4 6 5.
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12989)
- **Original**: अज्ञानतमसाच्छन्न: 4 13 38
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12990)
- **Original**: अज्ञातकुलनामानम्‌ 3 115 975
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12991)
- **Original**: अप्डानं तुसहस्ाणाम्‌ 3 3 25
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12992)
- **Original**: अणुष़ण्युपपन्नों च 3 15 27
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12993)
- **Original**: अणुष्टाड्रह्मदत्त: 3 16 92
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12994)
- **Original**: अणुप्रयाणि धान्यानि 1 65 615
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12995)
- **Original**: अणोरणीयांसमसत्स्वरूपम्‌ 3. 2 44
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12996)
- **Original**: अत ऊर्म्य प्रवक्ष्यामि 2 8 53
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12997)
- **Original**: अतश्व माजातुः 5 1 एड
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12998)
- **Original**: अतक्ष पुस्यशम्‌ 1 67. छूड अविधष्या: 9 22 29
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12999)
- **Original**: अतिविपूके 4 20 17
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13000)
- **Original**: अतिचपलचित्ता 5. टैड 9
- **Translation**: 

---

