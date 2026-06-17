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

### Verse 1 (Garuda1 0.1241)
- **Original**: ।)), जगण (।5
- **Translation**: 

---

### Verse 2 (Garuda1 0.1242)
- **Original**: ) और रगण (5।5) होता है। इसमें सात और आठ वर्णोंपर यति होती है। एला नामका छन्‍्द सगण (।
- **Translation**: 

---

### Verse 3 (Garuda1 0.1243)
- **Original**: 5), यगण (।55), नगण ( ।।।), नगण (
- **Translation**: 

---

### Verse 4 (Garuda1 0.1244)
- **Original**: ।)) और यगण ( । 55 )-से संयुक्त होता है। चित्रलेखा छन्दके प्रत्येक चरणमें मगण (555), रगण (5।5), मगण (555), यगण (।55) तथा यगण (।55) होता है, यति सात और आठ वर्णोंपर होती है।
- **Translation**: 

---

### Verse 5 (Garuda1 0.1245)
- **Original**: 312 » पुराण गारुईड बल्ष्ये सारे विष्णुकथाअयम्‌ * [ संक्षिप्त गरुडपुराणाडू ऋक़कऋऋऋऋकऋकऋकडऋकआआऋकऋऋकऋककफऋऊऋकऋककऋकऋ कक ऋकफ कफ #कऋ# #फऋ#फ़फ़क़क कर ऋ कफ ऋफ़क ऋ का ऋ कफ कऋ कक
- **Translation**: 

---

### Verse 6 (Garuda1 0.1246)
- **Original**: ऋकफ कक ऋ
- **Translation**: 

---

### Verse 7 (Garuda1 0.1247)
- **Original**: ऋकऋ कक कक. कक ऋक कऋ ू_ू_झूू्््??्?्म्9म्मऊन-्मम्न क् म् नम ाभ रु भम्णऋूूओुओऋिऋिऋषिऋंषंॉिऑिऑॉंंऑंररओं॑-::<5:22: 24%: 4220 0क्‍ 20% 2:2क्‍0क्‍:00-20-22222 यहाँतक पंद्रह वर्णोंके चरणवाले अतिशर्करी छन्दके अवान्तर शभरेदोंका वर्णन बताया गया है। जिस छन्‍्दके प्रत्येक चरणमें भगण (5
- **Translation**: 

---

### Verse 8 (Garuda1 0.1248)
- **Original**: ), रगण (5। 5), नगण (
- **Translation**: 

---

### Verse 9 (Garuda1 0.1249)
- **Original**: ।), नगण (
- **Translation**: 

---

### Verse 10 (Garuda1 0.1250)
- **Original**: ।।), नगण (
- **Translation**: 

---

### Verse 11 (Garuda1 0.1251)
- **Original**: ) तथा एक गुरु (5) होता है और जिसमें सात तथा नौ वर्णोंपर यति हो तो उसे वृषभगजजुम्भित छन्‍्द कहते हैं। जिसके सभी चरणोंमें नगण (
- **Translation**: 

---

### Verse 12 (Garuda1 0.1252)
- **Original**: ), जगण ( ।5।), भगण (5
- **Translation**: 

---

### Verse 13 (Garuda1 0.1253)
- **Original**: ।), जगण (।5।), रगण (55) और एक गुरु (5) हो, उसका नाम वाणिनी छन्द हैं। यति चरणकी समाप्तिपर होती है। पिड्जलद्वारा इन दोनों छन्दोंको अष्टि श्रेणीके छन्दके अन्तर्गत स्वीकार किया गया है। .. य्गण (
- **Translation**: 

---

### Verse 14 (Garuda1 0.1254)
- **Original**: 55), मगण (555), नगण (
- **Translation**: 

---

### Verse 15 (Garuda1 0.1255)
- **Original**: ), सगण (।।5), भगण (5।।), एक लघु (।) और एक गुरू (5)-से संयुक्त चरणवाले छनन्‍्दका नाम शिखरिणी है। इसमें यति छः तथा ग्यारह वर्णोंपर होती है। पृथ्वी छन्‍्दके प्रत्येक चरणमें ज़गण (।5
- **Translation**: 

---

### Verse 16 (Garuda1 0.1256)
- **Original**: ), सगण (
- **Translation**: 

---

### Verse 17 (Garuda1 0.1257)
- **Original**: 5), जगण (।5
- **Translation**: 

---

### Verse 18 (Garuda1 0.1258)
- **Original**: ), सगण ( ।5), यगण ( ।55), एक लघु (। ) तथा एक गुरु (5) होता है। इसकी यति आठ और नौ वर्णोंपर होतो है। जिस छनन्‍्दके चरण भगण (5
- **Translation**: 

---

### Verse 19 (Garuda1 0.1259)
- **Original**: ), रगण (5
- **Translation**: 

---

### Verse 20 (Garuda1 0.1260)
- **Original**: 5), नगण (
- **Translation**: 

---

