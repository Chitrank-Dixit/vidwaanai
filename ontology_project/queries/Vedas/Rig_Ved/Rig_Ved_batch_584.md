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

### Verse 1 (Rig Ved 0.11661)
- **Original**: घडा ज पाएए:&7/एएष शा : (66 55 एफ (ऋरूला प्रा 07917 वा 0णाएएट (एग्राब्राद 2#0
- **Translation**: 

---

### Verse 2 (Rig Ved 0.11662)
- **Original**: 1 09 0जा89
- **Translation**: 

---

### Verse 3 (Rig Ved 0.11663)
- **Original**: द्रोए 922 श
- **Translation**: 

---

### Verse 4 (Rig Ved 0.11664)
- **Original**: #0741 छ73त्राह। #94(ल3754 बंआाड एज ग00 €35
- **Translation**: 

---

### Verse 5 (Rig Ved 0.11665)
- **Original**: 4 ।श्रा
- **Translation**: 

---

### Verse 6 (Rig Ved 0.11666)
- **Original**: # 63009 [96 04 /7006
- **Translation**: 

---

### Verse 7 (Rig Ved 0.11667)
- **Original**: 78 0 लि: धैंज!
- **Translation**: 

---

### Verse 8 (Rig Ved 0.11668)
- **Original**: 5 7 अल 93 6 00 ट्वो आ( नल एज 9006 शि_्ा7 0 5.303/
- **Translation**: 

---

### Verse 9 (Rig Ved 0.11669)
- **Original**: कराती 9384 5079 ₹
- **Translation**: 

---

### Verse 10 (Rig Ved 0.11670)
- **Original**: 54 आए (:7
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11671)
- **Original**: दा छाए 5 50005 एजाशाश: 5पा फैट 9 " [7060 79579 गओ डिएडओ 0! #
- **Translation**: 

---

### Verse 12 (Rig Ved 0.11672)
- **Original**: #25घा।#ला' णज।
- **Translation**: 

---

### Verse 13 (Rig Ved 0.11673)
- **Original**: ल 05559 70]5 + 4900 707 + 72
- **Translation**: 

---

### Verse 14 (Rig Ved 0.11674)
- **Original**: 4₹ 6007 टछका * [.9 छित्ांगा पललाशा#एं बराहर70
- **Translation**: 

---

### Verse 15 (Rig Ved 0.11675)
- **Original**: /447847 4.भा
- **Translation**: 

---

### Verse 16 (Rig Ved 0.11676)
- **Original**: रउ्ट 5 '7 आएं 5.99
- **Translation**: 

---

### Verse 17 (Rig Ved 0.11677)
- **Original**: (3शाट्व3 फेंग 2770 #726"5 फर्क सम संत गान5लआा। लि गाताह्ाप ए।7 43073 [09 ता 65 रिसाव 70065 जय 8:355 भ्राफा 7ल्‍ज्याट * राजांह ढा मी (0
- **Translation**: 

---

### Verse 18 (Rig Ved 0.11678)
- **Original**: %755 [9556 ]0567 77 7:96 (0546+ (.86
- **Translation**: 

---

### Verse 19 (Rig Ved 0.11679)
- **Original**: 0एश् 7 मारता 90] 97:55 आग छा * 99एगा5ए 67 (5 । है.
- **Translation**: 

---

### Verse 20 (Rig Ved 0.11680)
- **Original**: 0 $5। है 1
- **Translation**: 

---

