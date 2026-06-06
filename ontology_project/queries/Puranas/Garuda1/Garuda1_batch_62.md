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

### Verse 1 (Garuda1 0.1221)
- **Original**: ।), सगण (
- **Translation**: 

---

### Verse 2 (Garuda1 0.1222)
- **Original**: ।5) और दो गुरु ($ 5)-से युक्त छन्दकों असम्बाधा कहते हैं, इसमें पाँच और नौ वर्णॉपर यति होती है। जिस छन्दमें नगण (
- **Translation**: 

---

### Verse 3 (Garuda1 0.1223)
- **Original**: ।), नगण (।
- **Translation**: 

---

### Verse 4 (Garuda1 0.1224)
- **Original**: ), रगण (5
- **Translation**: 

---

### Verse 5 (Garuda1 0.1225)
- **Original**: 5), सगण (
- **Translation**: 

---

### Verse 6 (Garuda1 0.1226)
- **Original**: 5), एक लघु (।) और एक गुरु (5) हो, उसे अपराजिता छन्‍्द कहा गया है। इसमें सात-सात वर्णोंपर यति होती है। यदि प्रत्येक चरणमें नगण (
- **Translation**: 

---

### Verse 7 (Garuda1 0.1227)
- **Original**: ।।), नगण (
- **Translation**: 

---

### Verse 8 (Garuda1 0.1228)
- **Original**: ), भगण (5 ।।), नगण (
- **Translation**: 

---

### Verse 9 (Garuda1 0.1229)
- **Original**: ।), एक लघु (।) तथा एक गुरु (5) हो, तो उसे प्रहरणकलिका के नामसे जाता जाता है। इसमें भी सात-सात वर्णपर ही यति होती हैं। खसन्ततिलका हन्दमें सभी चरण क्रमश: तंगण (55
- **Translation**: 

---

### Verse 10 (Garuda1 0.1230)
- **Original**: ), भगण (5
- **Translation**: 

---

### Verse 11 (Garuda1 0.1231)
- **Original**: ।), दो जगण (।5
- **Translation**: 

---

### Verse 12 (Garuda1 0.1232)
- **Original**: ), दो गुरु (55)- से युक्त होते हैं। इसीको सिंहोन्रता और उद्धर्षिणी भी कहते हैं। जिस छन्दके प्रत्येक पादमें भगण (5।।), जगण (।5।), सगण (
- **Translation**: 

---

### Verse 13 (Garuda1 0.1233)
- **Original**: । 5), नगण (
- **Translation**: 

---

### Verse 14 (Garuda1 0.1234)
- **Original**: ।) तथा दो गुरु (55) हों उसका नाम इन्दुबदना होता है। जिसका प्रत्येक चरण नगण ( ।
- **Translation**: 

---

### Verse 15 (Garuda1 0.1235)
- **Original**: ।।), रगण (5।5), नगण (
- **Translation**: 

---

### Verse 16 (Garuda1 0.1236)
- **Original**: ।।), रगण (5
- **Translation**: 

---

### Verse 17 (Garuda1 0.1237)
- **Original**: 5), एक लघु (।) और एक गुरु (5)-से संयुक्त होता है, उसीको सुकेशी छन्द कहते हैं। यहाँवक चौंदह बर्णोके चरणवाले शर्करी छनन्‍्दके अवान्तर भेदोंका वर्णन प्रतिपादित किया गया। जिस हन्दके प्रत्येक चरणमें चौदह लघु (चार नगण फिर दो लघु वर्ण) और अन्तमें एक गुरु हो, वह शशिकला छन्‍्द है। इसी छन्दमें जब यति छः और नौ अर्णोंपर हो तो वह ख्रक्‌ अर्थात्‌ माला नामक छन्द हो जाता है। जब वह यति आठ एवं सात वर्णोंपर हों तो यह मणिगुणनिकर नामक छन्द बन जाता है। मालिनी छन्द अपने प्रत्येक चरणमें नगण (।
- **Translation**: 

---

### Verse 18 (Garuda1 0.1238)
- **Original**: ), नगण (।
- **Translation**: 

---

### Verse 19 (Garuda1 0.1239)
- **Original**: ), मगण (555), यगण (। 55), यगण ( ।55)-से सन्निहित होता है। इसमें आठ और सात वर्णोंपर यति होती है। प्रभद्रक नामक हन्दके प्रत्येक चरणमें नगण (
- **Translation**: 

---

### Verse 20 (Garuda1 0.1240)
- **Original**: ), जगण (।5।), भगण (5
- **Translation**: 

---

