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

### Verse 1 (Vishnu Puran 0.13381)
- **Original**: तस्मिआर्मफे निस्पयम्‌ 1 286 33 रस्मास्सुन्टेएस्ल: 4 7रंड « है5-
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13382)
- **Original**: वस्मिआफ्ते किमिहस्पलप्याए 3 43778 ह291 (जभृति 4. रड 5 है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13383)
- **Original**: तस्मिलिसत्ति पनुज्क 237 डे है तप्मासयुल्मोमातिः ह।.. 4 4 श4- 49.
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13384)
- **Original**: तपसिमनते बहबुचण ड 0 सफ्रयफ़र सम्याशासुप- - 4 1878 24
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13385)
- **Original**: तस्मिप्रशेर् अस सर्वरूपि, 4 20627 ऋषाव सकिए: 0. 4 है 27:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13386)
- **Original**: तस्पस हे 082 47:17 तत्मादष्यविक्षित्‌ 4 553 73%
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13387)
- **Original**: नशिन्काटे बशोदापि 56 8 है 7रे0 तत्मांध दमः 4. 10 735
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13388)
- **Original**: तरिप्रासभदैतेये 6 7 ।39/98715:08 तलाबादः _ौ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13389)
- **Original**: ह 71 ड1-
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13390)
- **Original**: तत्मिससस्सिस्तु है हरे 7 डंडे सस्ब्रक्त तिऊुम्भ: हे 48 राय ड4ड
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13391)
- **Original**: सस्मिन्यालेसपध्यर्य्य -* 6 एश&#ह8 39 तममान्न प्रसेनजित्‌ 4 80207 47:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13392)
- **Original**: तल चापुताय हल ईडफ8 788 क्र्मादष्पज: 4. 477 85
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13393)
- **Original**: तस्मै लमेने तनया नरेन्‍््र 2 007 तस्म्ामाणुह: 4 “1987 43-
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13394)
- **Original**: गस्यपै जातमाकल ₹ै- 13 88 56 सत्मादेलाशिधि: 4 20 0 5
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13395)
- **Original**: ठख शारमपाद्रीस 1: है8 रेस शस्माण शेसवर 4 रश्त7 066
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13396)
- **Original**: तस्यपूतरास्तु चलाए 9 95 शर1 तस्मात्सु
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13397)
- **Original**: 78 है 23845 8/
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13398)
- **Original**: तत्यप्रभाषभतुलूम 1 8:96
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13399)
- **Original**: सस्माद्िश्वजित्‌ 4 723 4 121
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13400)
- **Original**: त््यपुत्रो महाभाग: है 17 (10 रुस्ाद्धारेतु बच ए9 «0 3... क्थतर्ा/+ंजवोगाद्‌ «है आरे0सूक 9 सक्मात्यादृषि साझनः
- **Translation**: 

---

