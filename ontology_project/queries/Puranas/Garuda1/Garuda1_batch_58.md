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

### Verse 1 (Garuda1 0.1141)
- **Original**: ), सगण (
- **Translation**: 

---

### Verse 2 (Garuda1 0.1142)
- **Original**: 5) और एक गुरु (5) होता है, उसका नाम मत्ता है। जिसके प्रत्येक चरणमें नगण (
- **Translation**: 

---

### Verse 3 (Garuda1 0.1143)
- **Original**: ।।), रगण (5।5), जगण (
- **Translation**: 

---

### Verse 4 (Garuda1 0.1144)
- **Original**: ) तथा एक गुरु (5) है, उसे मतोरमा कहा गया है। ये सभी
- **Translation**: 

---

### Verse 5 (Garuda1 0.1145)
- **Original**: 310 + पुराणं गारुड वक्ष्ये सारं विष्णुकथाअयम्‌ * [ संक्षिप्त गरुडपुराणाडू ऋक्कऋ्कऋऋऋकऋकऋकऋक्कऋऋऊऋऋफऋकककऋकऋ कफ फऋ़ऋ कक: कक कक कक ऋकऋऋआआऋ ऋऋककफकऋ आफ कफ ऋऋकफकफ ऋऋ ऋफ़फकफ कफ कफ ऋ##ऋ#ऋऋफऋऋऋऋ दस वर्णोंवाले पड़ि उन्दके भेद हैं। जिस छन्दके प्रत्येक चरणमें दों तगण (55
- **Translation**: 

---

### Verse 6 (Garuda1 0.1146)
- **Original**: ), एक जगण (।5
- **Translation**: 

---

### Verse 7 (Garuda1 0.1147)
- **Original**: ), दो गुरु (55) होते हैं, उसे इन्द्रवज़ा कहते हैं और जिस हन्दमें क्रमश: एक जगण (।5। ), एक तगण (55
- **Translation**: 

---

### Verse 8 (Garuda1 0.1148)
- **Original**: ), एक जगण (
- **Translation**: 

---

### Verse 9 (Garuda1 0.1149)
- **Original**: ) एवं दो गुरु (55) हों, उसका नाम उपेन्द्रबज़ा है। जब एक ही छन्‍्दमें ये दोनों इन्द्रवज़ा तथा उपेन्द्रवज़ा छन्‍्द सम्मिलित रहते हैं, तो उसे उपजाति कहा जाता है। इनके अनेक भेद हैं। यथा-- सुमुखी नामक छन्दके प्रत्येक चरणमें एक नगण (।
- **Translation**: 

---

### Verse 10 (Garuda1 0.1150)
- **Original**: ), दो जगण (।5
- **Translation**: 

---

### Verse 11 (Garuda1 0.1151)
- **Original**: ), एक लघु (।) और एक गुरु (5) होता है। दोधक में तीन भगण (5
- **Translation**: 

---

### Verse 12 (Garuda1 0.1152)
- **Original**: ।) और दो गुरु (55) होते हैं। शालिनी नामक जो छन्‍्द है उसके सभी चरणोंमें एक मगण (555), दो तगण (55
- **Translation**: 

---

### Verse 13 (Garuda1 0.1153)
- **Original**: ) एबं दो गुरुओं (55) को युति होती है। इसके प्रत्येक चरणमें चौथे तथा सातवें अक्षरपर विराम होता है। जात्ो्मी उन्दके प्रत्येक चरणमें दो मगण (555, 555), एक तगण (55।) होता है और उसके बाद दो गुरु (55) होते हैं। इसमें भी चार, सातपर विराम होता है। जो हन्द प्रत्येक चरणमें मगण (555), भगण (5
- **Translation**: 

---

### Verse 14 (Garuda1 0.1154)
- **Original**: ।।), नगण (
- **Translation**: 

---

### Verse 15 (Garuda1 0.1155)
- **Original**: ।।), नगण (
- **Translation**: 

---

### Verse 16 (Garuda1 0.1156)
- **Original**: ।।), एक लघु (।) और एक गुरु (5)-से युक्त हो, उसे भ्रमरबिलासिता नामक छन्‍्द कहा गया है। रथोद्धता छन्‍द अपने सभी चरणोंमें एक रगण (5
- **Translation**: 

---

### Verse 17 (Garuda1 0.1157)
- **Original**: 5), नगण (।
- **Translation**: 

---

### Verse 18 (Garuda1 0.1158)
- **Original**: । ), रगण (5।5), एक लघु (।) एवं एक गुरु (5)-से संयुक्त होता है। स्वागता के प्रत्येक पादमें एक रगण (5
- **Translation**: 

---

### Verse 19 (Garuda1 0.1159)
- **Original**: 5), एक नगण ( ।
- **Translation**: 

---

### Verse 20 (Garuda1 0.1160)
- **Original**: ), एक भगण (5
- **Translation**: 

---

