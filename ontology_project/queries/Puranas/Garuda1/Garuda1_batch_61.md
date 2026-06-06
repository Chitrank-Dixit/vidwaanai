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

### Verse 1 (Garuda1 0.1201)
- **Original**: ), भगण (5।।) तथा रगण (5।5) होते हैं। जो छन्‍द मगण (555), मगण (555), यगण (।55), यगण (।55)-से संयुक्त है, उसका नाम वैश्वदेवी है। इसमें पाँच और सात वर्णॉंपर यति होती है। जब छन्दके प्रत्येक चरणमें मगण (555), भगण (5
- **Translation**: 

---

### Verse 2 (Garuda1 0.1202)
- **Original**: ।), सगण (
- **Translation**: 

---

### Verse 3 (Garuda1 0.1203)
- **Original**: ।5) और मगण (555) हो तो उसे जलधरमाला कहते हैं। चन्द्रवर्त्म छन्दसे यहाँतक बारह वर्णवाले जगती छन्दके भेद हैं। जिस छन्‍्दके प्रत्येक चरणमें नगण (।
- **Translation**: 

---

### Verse 4 (Garuda1 0.1204)
- **Original**: ), नगण (
- **Translation**: 

---

### Verse 5 (Garuda1 0.1205)
- **Original**: ), तगण (55।), तगण (55।) और एक गुरु (5) हो, तो उसका नाम क्षमावृत्त है। इसमें सात और छः: वर्णोंपर यति होती है। प्रहर्थिणी नामक छन्‍्द मगण (555), नगण (
- **Translation**: 

---

### Verse 6 (Garuda1 0.1206)
- **Original**: ), जगण (
- **Translation**: 

---

### Verse 7 (Garuda1 0.1207)
- **Original**: ), रगण (5।5) एवं एक गुरु (5)-से युक्त होता है। इसके प्रत्येक चरणमें तीन और दस वर्णपर यतिका विधान है। जो छन्‍द जगण (।5
- **Translation**: 

---

### Verse 8 (Garuda1 0.1208)
- **Original**: ), भरगण (5।।
- **Translation**: 

---

### Verse 9 (Garuda1 0.1209)
- **Original**: ), सगण (
- **Translation**: 

---

### Verse 10 (Garuda1 0.1210)
- **Original**: 5), जगण (।5।) और एक गुरु (5)-से सभ्रिहित होता है, उसको रुचिरा कहा गया है। इसमें यति चार तथा नौ वर्णोंपर होती है। मत्तमयूर नामक छन्‍्दकों मगण (555), तगण (55।), यगण (।55), सगण ( 5) और एक गुरु (5)-से युक्त माना गया है। इसके प्रत्येक पादमें चार तथा नौ वर्णॉंपर यति होती है। मद्जुभाषिशी छन्दके प्रत्येक चरणमें सगण (
- **Translation**: 

---

### Verse 11 (Garuda1 0.1211)
- **Original**: 5), जगण (
- **Translation**: 

---

### Verse 12 (Garuda1 0.1212)
- **Original**: ।5।), सगण (
- **Translation**: 

---

### Verse 13 (Garuda1 0.1213)
- **Original**: । 5), जगण (।5।) और एक गुरु (5) होता है। सुनन्दिनी नामक छन्दके प्रत्येक चरणमें सगण (
- **Translation**: 

---

### Verse 14 (Garuda1 0.1214)
- **Original**: । 5), जगण (5
- **Translation**: 

---

### Verse 15 (Garuda1 0.1215)
- **Original**: ), सगण (।। 5) होते हो हैं, किंतु अन्तिम जगणके स्थानपर इसमें मगण (555) होता है। अन्तमें एक गुरु (5) रहता है और जो छन्‍्द नगण (
- **Translation**: 

---

### Verse 16 (Garuda1 0.1216)
- **Original**: ), नंगण (
- **Translation**: 

---

### Verse 17 (Garuda1 0.1217)
- **Original**: ।।), तगण (55
- **Translation**: 

---

### Verse 18 (Garuda1 0.1218)
- **Original**: ), तगण (55
- **Translation**: 

---

### Verse 19 (Garuda1 0.1219)
- **Original**: ।) तथा एक गुरु (5)-से युक्त है, उसका नाम चन्द्रिका है। इसमें सात और छ: वर्णोंपर यति होती है। ये तेरह वर्णवाले अतिजगती उन्दके अवान्तर भेद हैं। मगण (555), तगण (55
- **Translation**: 

---

### Verse 20 (Garuda1 0.1220)
- **Original**: ), नगण (
- **Translation**: 

---

