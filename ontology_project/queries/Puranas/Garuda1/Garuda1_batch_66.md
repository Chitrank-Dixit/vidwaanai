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

### Verse 1 (Garuda1 0.1301)
- **Original**: ।5।), भगण (5
- **Translation**: 

---

### Verse 2 (Garuda1 0.1302)
- **Original**: ), जगण (।5।), भगण (5
- **Translation**: 

---

### Verse 3 (Garuda1 0.1303)
- **Original**: ), जगण (
- **Translation**: 

---

### Verse 4 (Garuda1 0.1304)
- **Original**: ), भगण (5
- **Translation**: 

---

### Verse 5 (Garuda1 0.1305)
- **Original**: ), एक लघु (।) तथा एक गुरु (5)-से युक्त छन्द हो और उसमें ग्यारह तथा बारह वर्णोंपर यति हो, उसका नाम अश्वललित है। इसे अन्य ग्रन्थोंमें अद्वितनया भी कहा गया है। जिस छन्‍्दमें मगण (555), मगण (555), तगण (55
- **Translation**: 

---

### Verse 6 (Garuda1 0.1306)
- **Original**: ), नगण (
- **Translation**: 

---

### Verse 7 (Garuda1 0.1307)
- **Original**: ), नगण ( ।
- **Translation**: 

---

### Verse 8 (Garuda1 0.1308)
- **Original**: ), नगण (।।
- **Translation**: 

---

### Verse 9 (Garuda1 0.1309)
- **Original**: ), तगण (
- **Translation**: 

---

### Verse 10 (Garuda1 0.1310)
- **Original**: ।), एक लघु (
- **Translation**: 

---

### Verse 11 (Garuda1 0.1311)
- **Original**: ) तथा एक गुरु (5) होता है और जिसमें आठ, पाँच तथा दस वर्णोंपर यति होती है, उसको मत्ताक्रीड कहा जाता है। ये दोनों छन्द तेईस वर्णांवाले विकृति छन्द-वर्गके अन्तर्गत हैं। जिस छन्दका प्रत्येक पाद भगण (5।।), तगण (55
- **Translation**: 

---

### Verse 12 (Garuda1 0.1312)
- **Original**: ), नगण (
- **Translation**: 

---

### Verse 13 (Garuda1 0.1313)
- **Original**: ), सगण (
- **Translation**: 

---

### Verse 14 (Garuda1 0.1314)
- **Original**: । 5), भगण (5
- **Translation**: 

---

### Verse 15 (Garuda1 0.1315)
- **Original**: ), भगण (5
- **Translation**: 

---

### Verse 16 (Garuda1 0.1316)
- **Original**: ), नगण (
- **Translation**: 

---

### Verse 17 (Garuda1 0.1317)
- **Original**: ।), यगण (।55)-से संयुक्त होता है और उसमें पाँच, सात तथा बारह वर्णोंपर यति होती है, उसको तन्यी छन्द कहते हैं। यह तन्‍्वी छन्‍्द चौबीस वर्णोके चरणवाले संकृति छन्द-वर्गका अवान्तर भेद है। क्रौकपदा नामका जो छन्द है, उस छन्‍्दमें भगण (5
- **Translation**: 

---

### Verse 18 (Garuda1 0.1318)
- **Original**: ।), मगण (555), सगण (
- **Translation**: 

---

### Verse 19 (Garuda1 0.1319)
- **Original**: 5), भगण (5
- **Translation**: 

---

### Verse 20 (Garuda1 0.1320)
- **Original**: ।) एवं नगणं (
- **Translation**: 

---

