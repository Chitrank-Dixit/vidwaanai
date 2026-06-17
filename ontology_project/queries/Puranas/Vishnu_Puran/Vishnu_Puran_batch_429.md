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

### Verse 1 (Vishnu Puran 0.8561)
- **Original**: ततञर होगा, बल्मककका विशाखयूप, विशाखयूपका जनक, विज्ञाखयूप:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8562)
- **Original**: तत्पुन्नो. जनक:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8563)
- **Original**: जनकका नन्दिवर्द्धन तथा नन्दिवर्दधनका पुत्र नन्‍्दो होगा। तस्य चर नन्दिवर्द्धन:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8564)
- **Original**: ततो नन्‍्दी
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8565)
- **Original**: ये पाँच प्रद्योतबशीय नृपतिगण एक सौ अड़॒तीस वर्ष
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8566)
- **Original**: 298 इल्येतेडष्टव्रिंशादुत्तरमब्दशर्त पत्ञ प्रद्योता: पृथियीं भ्रोक्ष्यन्ति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8567)
- **Original**: ततश्र शिशुनाभ:ः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8568)
- **Original**: तत्पुत्रः काकवर्णो भव्िता
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8569)
- **Original**: तस्य च पुत्र: क्षेमरर्मा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8570)
- **Original**: तस्यापि क्षतौजा:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8571)
- **Original**: तत्पुत्रो विधिसारः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8572)
- **Original**: ततश्चाजातशत्रु:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8573)
- **Original**: तस्मादर्भकः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8574)
- **Original**: त्स्माच्चोदयनः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8575)
- **Original**: तस्मादपि नन्दिवर्द्धन:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8576)
- **Original**: ततो महानन्दी
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8577)
- **Original**: इत्येते जैशनाभा भूपालास्रीणि वर्षशतानि द्विषष्टठध्रधिकानि भविष्यन्ति
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8578)
- **Original**: महानन्दिनस्ततइशूद्रागरभोद्धवो 5तिलुब्यो 5ति- बलो महापद्नामा नन्‍्दः परशुराम इबापरो- उखिलक्षत्रान्तकारी भविष्यति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8579)
- **Original**: तत: प्रभृति झूद्रा भूपाला भविष्यन्ति
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8580)
- **Original**: स चैकच्छत्रामनुल्‍छड्ल्तिशासनो महापद्य: पृथिवीं भोक्ष्वते
- **Translation**: 

---

