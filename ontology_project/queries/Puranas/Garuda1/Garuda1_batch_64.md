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

### Verse 1 (Garuda1 0.1261)
- **Original**: ।), नगण (
- **Translation**: 

---

### Verse 2 (Garuda1 0.1262)
- **Original**: ), भगण (5
- **Translation**: 

---

### Verse 3 (Garuda1 0.1263)
- **Original**: ।), एक लघु (। ) तथा एक गुरु (5)-से संयुक्त होते हैं और जिनमें दस एवं सात वर्णोंपर यति होती है, उसे बंशपत्रपतित कहा गया है। हरिणी छनन्‍्द नगण (
- **Translation**: 

---

### Verse 4 (Garuda1 0.1264)
- **Original**: ), सगण (
- **Translation**: 

---

### Verse 5 (Garuda1 0.1265)
- **Original**: 5), मगण (555), रगण (5।5), सगण (
- **Translation**: 

---

### Verse 6 (Garuda1 0.1266)
- **Original**: 5), एक लघु (।) और एक गुरु (5)-से संसृष्ट होता है। इसमें यति क्रमश: छ:, चार तथा सात वर्णोंपर होती है। मगण (555), भगण (5।), नगण (
- **Translation**: 

---

### Verse 7 (Garuda1 0.1267)
- **Original**: ।), तगण (55
- **Translation**: 

---

### Verse 8 (Garuda1 0.1268)
- **Original**: ), तगण (55
- **Translation**: 

---

### Verse 9 (Garuda1 0.1269)
- **Original**: ), दो गुरु (55)-से युक्त चरणोंवाले छन्‍्दकों मन्दाक़रान्ता कहते हैं। इसमें चार, छः और सात वर्णोंपर यति होती है। नईटक छनन्‍्द नगण ( ।
- **Translation**: 

---

### Verse 10 (Garuda1 0.1270)
- **Original**: ।), जगण (
- **Translation**: 

---

### Verse 11 (Garuda1 0.1271)
- **Original**: ), भगण (5$
- **Translation**: 

---

### Verse 12 (Garuda1 0.1272)
- **Original**: ।), जगण (।5), जगण (।5
- **Translation**: 

---

### Verse 13 (Garuda1 0.1273)
- **Original**: ), एक लघु (।) और एक गुरु (5)-से संयुक्त होता है। इसमें यति सात और दस वर्णोंपर होती है। यदि यही यति सात, छ: और चार वर्णोंपर हो तो छन्‍्दका नाम कोकिलक हो जाता है। शिखरिणीसे कोकिलकतक इन छन्दोंको सत्रह वर्णोंवाले अत्यष्टि छन्द- वर्गमें समझना चाहिये। जिस छन्दमें मगण (555), तगण (55
- **Translation**: 

---

### Verse 14 (Garuda1 0.1274)
- **Original**: ), नगण (।।
- **Translation**: 

---

### Verse 15 (Garuda1 0.1275)
- **Original**: ), यगण (।55), यगण (।55), यगण (
- **Translation**: 

---

### Verse 16 (Garuda1 0.1276)
- **Original**: 55) होता है और पाँच, छः तथा सात वर्णोंपर यति होती है, उसको कुसुमितलता छन्द कहते हैं। इसे अठारह अक्षरोंके चरणवाले धृति छन्‍्दका अवान्तर भेद कहा गया है। यगण (।55), मगण (555), नगण (।
- **Translation**: 

---

### Verse 17 (Garuda1 0.1277)
- **Original**: ।), सगण (
- **Translation**: 

---

### Verse 18 (Garuda1 0.1278)
- **Original**: 5), रगण (55), रगण (5।5) और एक गुरु (5)-से युक्त छन्दका नाम मेघविस्फूर्जिता है। इसमें छः, छः: और सात वर्णोंपर यति होती है। शार्दूलविक्रीडित नामक जो छन्द है, उसके प्रत्येक चरणमें मगण (555), सगण (।
- **Translation**: 

---

### Verse 19 (Garuda1 0.1279)
- **Original**: 5), जगण (
- **Translation**: 

---

### Verse 20 (Garuda1 0.1280)
- **Original**: ), सगण (
- **Translation**: 

---

