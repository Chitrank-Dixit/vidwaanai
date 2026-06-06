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

### Verse 1 (Garuda1 0.1281)
- **Original**: ।5 ), दो तगण (55
- **Translation**: 

---

### Verse 2 (Garuda1 0.1282)
- **Original**: ) तथा एक गुरु (5) होता है। इसमें बारह और सात यर्णोंपर यतिका विधान है। ये दोनों उन्नीस वर्णोंके चरणवाले अतिधृति छन्द-वर्गके भेद कहे गये हैं। इसके याद बीस वर्णोके चरणवालें कृति नामवाले छन्दोंका निरूपण किया जा रहा है-- जिसके प्रत्येक चरणमें भगण (5
- **Translation**: 

---

### Verse 3 (Garuda1 0.1283)
- **Original**: ), रगण (5
- **Translation**: 

---

### Verse 4 (Garuda1 0.1284)
- **Original**: 5), मगण (555), नगण (
- **Translation**: 

---

### Verse 5 (Garuda1 0.1285)
- **Original**: ), यगण (
- **Translation**: 

---

### Verse 6 (Garuda1 0.1286)
- **Original**: 55), भगण (5।।), एक लघु (।), एक गुरु (5) होता है और क्रमश: सात, सात तथा छ: वर्णोंपर यति होती है, उसे सुबदना छनन्‍्द कहते हैं। जिसके प्रत्येक पादमें रगण (5।5), जगण (।5।), रगण (5।5), जगण (
- **Translation**: 

---

### Verse 7 (Garuda1 0.1287)
- **Original**: ), रगण (5।5), जगण (
- **Translation**: 

---

### Verse 8 (Garuda1 0.1288)
- **Original**: ), एक लघु (।), एक गुरु (5) हो और पादान्तमें यति होती हो, उसे बृत्त छन्द कहते हैं। जिस छन्दमें मगण (555), रगण (5।5), भगण (5
- **Translation**: 

---

### Verse 9 (Garuda1 0.1289)
- **Original**: ), नगण (
- **Translation**: 

---

### Verse 10 (Garuda1 0.1290)
- **Original**: ), यगण (
- **Translation**: 

---

### Verse 11 (Garuda1 0.1291)
- **Original**: 55), यगण (
- **Translation**: 

---

### Verse 12 (Garuda1 0.1292)
- **Original**: 55), यगण (।55) हो और प्रत्येक चरणमें सात-सात वर्णोंपर यति होती हो, वह ख्मग्धरा छन्द है। प्रत्येक चरणमें इ्कीस वर्णोंवाले इस उन्‍्दकों प्रकृति वर्गका छन्द माना गया है। जिसके सभी पाद क्रमश: भगण (5
- **Translation**: 

---

### Verse 13 (Garuda1 0.1293)
- **Original**: ), रगण (5
- **Translation**: 

---

### Verse 14 (Garuda1 0.1294)
- **Original**: 5), नगण (
- **Translation**: 

---

### Verse 15 (Garuda1 0.1295)
- **Original**: ), रगण (5
- **Translation**: 

---

### Verse 16 (Garuda1 0.1296)
- **Original**: 5), नगण (
- **Translation**: 

---

### Verse 17 (Garuda1 0.1297)
- **Original**: ), रगण (55), नगण ( ।
- **Translation**: 

---

### Verse 18 (Garuda1 0.1298)
- **Original**: ।।) तथा एक गुरु (5)-से संयुक्त हों और उनमें दस तथा बारह वर्णोंपर यति हो, उसे
- **Translation**: 

---

### Verse 19 (Garuda1 0.1299)
- **Original**: + छन्द-विधान ( अर्द्धसमवृत्त लक्षण ) * सुभव्रक छन्‍्द कहते हैं। यह बाईस वर्णोवाले आकृति ऋछन्दके अन्तर्गत है। जो नगण (
- **Translation**: 

---

### Verse 20 (Garuda1 0.1300)
- **Original**: ), जगण (
- **Translation**: 

---

