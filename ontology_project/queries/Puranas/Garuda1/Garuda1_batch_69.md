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

### Verse 1 (Garuda1 0.1361)
- **Original**: ), सगण (।
- **Translation**: 

---

### Verse 2 (Garuda1 0.1362)
- **Original**: ।5 ), जगण (।5।) और एक गुरु (5)-इस प्रकार दस अक्षर होते हैं, तृतोय पादमें भगण (5
- **Translation**: 

---

### Verse 3 (Garuda1 0.1363)
- **Original**: ), नगण (।
- **Translation**: 

---

### Verse 4 (Garuda1 0.1364)
- **Original**: ), जगण (।5।) एक लघु (।) तथा एक गुरु (5)--ये ग्यारह अक्षर होते हैं और चतुर्थ पादमें सगण (
- **Translation**: 

---

### Verse 5 (Garuda1 0.1365)
- **Original**: ।5 ), जगण (।5
- **Translation**: 

---

### Verse 6 (Garuda1 0.1366)
- **Original**: ), सगण (
- **Translation**: 

---

### Verse 7 (Garuda1 0.1367)
- **Original**: 5 ), जगण (।5
- **Translation**: 

---

### Verse 8 (Garuda1 0.1368)
- **Original**: ) तथा एक गुरु (5)-इस प्रकार तेरह अक्षर होते हैं तो वह उदगता नामक छन्द कहलाता है। इसी उदगता छन्दके तीसरे चरणमें जब रगण (5।5), नगण (
- **Translation**: 

---

### Verse 9 (Garuda1 0.1369)
- **Original**: ), यगण (।55) और एक गुरु (5)--इस प्रकार तेरह अक्षर हों और शेष तौन पाद पूर्ववत्‌ अर्थात्‌ उदगता छन्दके समान ही हों तो सौरभक नामक छन्द होता है। इसी उद्गता छन्दके तीसरे अरणमें जब दो नगण ( ।
- **Translation**: 

---

### Verse 10 (Garuda1 0.1370)
- **Original**: । ), दो सगण ( ।
- **Translation**: 

---

### Verse 11 (Garuda1 0.1371)
- **Original**: 45 ) हों तथा शेष तीनों चरण उदगताके हो समान हों तो ललित नामक छन्द होता है। ये सब उदगता छन्‍्दके अवान्तर भेद हैं। जिसके प्रथम पादमें मगण (555), सगण (
- **Translation**: 

---

### Verse 12 (Garuda1 0.1372)
- **Original**: ।5), जगण (।5।), भगण (5
- **Translation**: 

---

### Verse 13 (Garuda1 0.1373)
- **Original**: ) और दो गुरु (55)-इस प्रकार चौदह अक्षर होते हैं, द्वितोगय चरणमें सगण (।
- **Translation**: 

---

### Verse 14 (Garuda1 0.1374)
- **Original**: 5 ), नगण (
- **Translation**: 

---

### Verse 15 (Garuda1 0.1375)
- **Original**: ), जगण (
- **Translation**: 

---

### Verse 16 (Garuda1 0.1376)
- **Original**: ), रगण (5
- **Translation**: 

---

### Verse 17 (Garuda1 0.1377)
- **Original**: 5) तथा एक गुरु (5)--इस प्रकार तेरह अक्षर होते हैं, तीसरे चरणमें दो नगण ( ।
- **Translation**: 

---

### Verse 18 (Garuda1 0.1378)
- **Original**: । ) और एक सगण (।
- **Translation**: 

---

### Verse 19 (Garuda1 0.1379)
- **Original**: 5)-- इस प्रकार नौ अक्षर होते हैं तथा चौथे चरणमें तीन नगण (
- **Translation**: 

---

### Verse 20 (Garuda1 0.1380)
- **Original**: ), एक जगण (
- **Translation**: 

---

