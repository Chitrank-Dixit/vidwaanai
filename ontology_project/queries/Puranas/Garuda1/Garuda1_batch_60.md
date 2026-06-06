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

### Verse 1 (Garuda1 0.1181)
- **Original**: ), यगण ( ।55), नगण (।
- **Translation**: 

---

### Verse 2 (Garuda1 0.1182)
- **Original**: ), यगण ( ।55) हो, उस छन्दकों कुसुमविचित्रा कहते हैं। जगण (
- **Translation**: 

---

### Verse 3 (Garuda1 0.1183)
- **Original**: 5), सगण (।
- **Translation**: 

---

### Verse 4 (Garuda1 0.1184)
- **Original**: ।5), जगण (।5।), सगण (
- **Translation**: 

---

### Verse 5 (Garuda1 0.1185)
- **Original**: ।5)-से युक्त प्रत्येक पादवाले छनन्‍्दका नाम जलोद्धतगति है। प्रत्येक पादमें चार रगण (545, 5।5, 5।5, 55)-से युक्त छन्द स्त्रग्विणी माना गया है। चार-चार यगणों (।55,। 55, 55, 55 )- से जिसके सभी चरण संयुक्त हैं, उसको भुजज्जुप्रयात छन्दकी संज्ञा दी गयी है। प्रियंबदा छन्द नगण (
- **Translation**: 

---

### Verse 6 (Garuda1 0.1186)
- **Original**: ), भगण (5।।), जगण (।5
- **Translation**: 

---

### Verse 7 (Garuda1 0.1187)
- **Original**: ) और रगण (5
- **Translation**: 

---

### Verse 8 (Garuda1 0.1188)
- **Original**: 5)-इन आर गणोंसे युक्त होता है। अणिमाला नामक जो छन्द है, उसके प्रत्येक पादमें तगण (55
- **Translation**: 

---

### Verse 9 (Garuda1 0.1189)
- **Original**: ), यगण (। 55), तगण (55
- **Translation**: 

---

### Verse 10 (Garuda1 0.1190)
- **Original**: ) तथा यगण (।55) होता है। जिस छन्दके प्रत्येक पादमें तगण (55
- **Translation**: 

---

### Verse 11 (Garuda1 0.1191)
- **Original**: ), भगण (5
- **Translation**: 

---

### Verse 12 (Garuda1 0.1192)
- **Original**: ।), जगण (।5।) और रगण (5।5) हो तो उसका नाम ललिता है। इस छन्दमें छठे वर्णपर यति होती है। प्रमिताक्षणा वृत्त ससण (
- **Translation**: 

---

### Verse 13 (Garuda1 0.1193)
- **Original**: 5), जगण (।5
- **Translation**: 

---

### Verse 14 (Garuda1 0.1194)
- **Original**: ), सगण (
- **Translation**: 

---

### Verse 15 (Garuda1 0.1195)
- **Original**: ।5), सगण (
- **Translation**: 

---

### Verse 16 (Garuda1 0.1196)
- **Original**: ।5)-से युक्त होता है। उज्बला
- **Translation**: 

---

### Verse 17 (Garuda1 0.1197)
- **Original**: आचारकाण्ड ] + छन्द-विधान ( समवृत्तलक्षण ) * 311 $.
- **Translation**: 

---

### Verse 18 (Garuda1 0.1198)
- **Original**: 4 6 ..4.....ै...............3....4..2.... 5 0 30ै430 0 4 40440 00 44 4403.44040 0404 04044 04/44/4333 ऋ-ःेेड /#
- **Translation**: 

---

### Verse 19 (Garuda1 0.1199)
- **Original**: #;#ऋकऋकऋऋक्रऋ#%कक़कंक्रक कर ऑ कफ क़ क़ कक # क ##ऋकऋ #ऋ ##ऋ कक # # कर ऋ कक ऋ.#ऋक्त ऋ कक ऋऋऋ कक ऋऋक्ककफ़ककऋकऋकऋकऋकऋकऋआ छन्दमें नगण (
- **Translation**: 

---

### Verse 20 (Garuda1 0.1200)
- **Original**: ), नगण (।
- **Translation**: 

---

