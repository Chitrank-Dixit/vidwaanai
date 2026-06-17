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

### Verse 1 (Markende Puran 0.2741)
- **Original**: 38--47
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2742)
- **Original**: जो देवी सत्र प्राणियोर्मे जातिरूपसे स्थित हैं, उनको नमस्कार, उनकों नमस्कार, उनकौ बारबार नमस्कार है
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2743)
- **Original**: 41--43
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2744)
- **Original**: जो देवी सब प्राणियॉमे लब्जारूपसे स्थित हैं, उनको नमस्कार, उनको नमस्कार, उन्तकों बार्रजञार नमस्कार है
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2745)
- **Original**: 44--46
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2746)
- **Original**: जो देवी सत्र प्राणियोंपें शान्तिरूपसे स्थित हैँ, उनको नमस्कार, उनको नमस्कार, उनको लार्रखार नमस्कार है
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2747)
- **Original**: 47--49
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2748)
- **Original**: जो देवी स़ब प्राणियोंमें श्रद्धारूपसे स्थित हैं, उनको नमस्कार, उनको नमस्कार, उनको ब्रारंबार नमस्कार है
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2749)
- **Original**: 50--52
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2750)
- **Original**: जो देवों सब प्राणियोंर्से कान्तिरूपसे स्थित हैं, उनको ममसस्‍्कार, ठनको नमस्कार, उनको बारंबार नमस्कार है
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2751)
- **Original**: 53--55
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2752)
- **Original**: जो देवी सम्र प्राणियोंमें लक्ष्मीरूपसे स्थित हैं, उनको नमस्कार, उनको नमस्कार, उनको बारंबार नमस्कार है
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2753)
- **Original**: 56--58
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2754)
- **Original**: जो देवी सब प्राणियोमें वृत्तिरूपसे स्थित हैं, उनको नमस्कार, उनको नमस्कार, उनको बारंबार नमस्कार है
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2755)
- **Original**: 59--61
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2756)
- **Original**: जो देवी सब प्राणियॉमें स्मृतिरूपसे स्थित हैं, उनको नमस्कार, उतकों नमस्कार, उनको बारत्रार नमस्कार है
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2757)
- **Original**: 62--64
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2758)
- **Original**: जो देवी सब प्राणियोंमें दयारूपसे स्थित हैं, उनको नमस्कार, उनको नमस्कार, उनतकों बाहरंबार नमस्कार हैं
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2759)
- **Original**: 65--67
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2760)
- **Original**: जो देवी सब प्राणिवोंमें तुष्टिरूपसे स्थित हैं, डनकों वमस्कार, ठनकों नमस्कार, उनको बारंबार नमस्कार है
- **Translation**: 

---

