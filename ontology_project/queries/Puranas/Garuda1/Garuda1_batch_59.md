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

### Verse 1 (Garuda1 0.1161)
- **Original**: ।) और दो गुरु (55) होते हैं। वृत्ता नामक छन्दके प्रत्येक पादमें दो नगण (
- **Translation**: 

---

### Verse 2 (Garuda1 0.1162)
- **Original**: ), एक सगण (
- **Translation**: 

---

### Verse 3 (Garuda1 0.1163)
- **Original**: 5) और दो गुरु (55) सप्निहित होते हैं। समद्रिका छन्दमें दो नगण (
- **Translation**: 

---

### Verse 4 (Garuda1 0.1164)
- **Original**: ,।।), एक रगण (5
- **Translation**: 

---

### Verse 5 (Garuda1 0.1165)
- **Original**: 5), एक लघु (। ) तथा एक गुरु (5) होता है। जिस छन्दके प्रत्येक चरण रगण (5
- **Translation**: 

---

### Verse 6 (Garuda1 0.1166)
- **Original**: 5), जगण (।5। ), एक लघु (।) तथा एक गुरु (5)-से युक्त हों, वह श्येनिका नामक छन्द है। जहाँ सभी चारों चरणोंमें एक जगण (
- **Translation**: 

---

### Verse 7 (Garuda1 0.1167)
- **Original**: ।5।), एक सगण (।
- **Translation**: 

---

### Verse 8 (Garuda1 0.1168)
- **Original**: 5), एक तगण (55
- **Translation**: 

---

### Verse 9 (Garuda1 0.1169)
- **Original**: ), दो गुरु (55) हों तो वहाँ शिखण्डित छन्द होता है। महात्मा पिड्नलने इन्हें प्रिप्टुपू-छन्दका भेद बताया है। जिस छन्‍्दके प्रत्येक चरणमें एक रगण (5
- **Translation**: 

---

### Verse 10 (Garuda1 0.1170)
- **Original**: 5), एक नगण ( ।
- **Translation**: 

---

### Verse 11 (Garuda1 0.1171)
- **Original**: ।), एक भगण (5।।), एक सगण (।
- **Translation**: 

---

### Verse 12 (Garuda1 0.1172)
- **Original**: 5) हो, उसका नाम चद्द्रवर्तत और जिसमें एक जगण ( ।5।), एक तगण (55
- **Translation**: 

---

### Verse 13 (Garuda1 0.1173)
- **Original**: ), एक जगण (। 5
- **Translation**: 

---

### Verse 14 (Garuda1 0.1174)
- **Original**: ), एक रगण (545) हो, उसका नाम ंशस्थ छन्द है। जिस छन्दके प्रत्येक चरणमें दो तगण (55
- **Translation**: 

---

### Verse 15 (Garuda1 0.1175)
- **Original**: 55।), एक जगण (।5।) हो, उसे इन्द्रवंशा और जिसमें चार सगण-ही-सगण (
- **Translation**: 

---

### Verse 16 (Garuda1 0.1176)
- **Original**: ।5) होते हैं, उसे त्तोटक छन्द माना गया है। जिसके प्रत्येक पादमें नगण (
- **Translation**: 

---

### Verse 17 (Garuda1 0.1177)
- **Original**: ।), दो भगण (5
- **Translation**: 

---

### Verse 18 (Garuda1 0.1178)
- **Original**: ) और रगण (5।5) हो, उसका नाम ह्रुतविलम्बित है। जो छन्‍्द अपने सभी चारों चरणमें दो नगण (
- **Translation**: 

---

### Verse 19 (Garuda1 0.1179)
- **Original**: ), एक मगण (555), एक यगण (।55)-से संयुक्त रहता है, उसका नाम पुट है। इस छन्दमें आठ और चार वर्णों चर यति होती है। दो नगण (।।
- **Translation**: 

---

### Verse 20 (Garuda1 0.1180)
- **Original**: ।।) और दो रगण (5।5, 55)-से समन्वित प्रत्येक चरणवाला जो छन्‍्द है, उसका नाम मुदितबदला है। इसमें सात और पाँच वर्णोपर यति होती है। जिस छन्‍्दके प्रत्येक चरणमें नगण (
- **Translation**: 

---

