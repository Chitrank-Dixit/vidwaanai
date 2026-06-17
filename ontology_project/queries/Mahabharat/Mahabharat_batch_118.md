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

### Verse 1 (Mahabharat 0.1171)
- **Original**: इस बनमें महावीर हनुमानजी रहते थे। उन्हें अपने भाई पड़ी उसे देखते ही वह उस सौगन्धिक नामवाले कमलके
- **Translation**: 

---

### Verse 2 (Mahabharat 0.1171)
- **Original**: इस बनमें महावीर हनुमानजी रहते थे। उन्हें अपने भाई पड़ी उसे देखते ही वह उस सौगन्धिक नामवाले कमलके
- **Translation**: 

---

### Verse 3 (Mahabharat 0.1172)
- **Original**: भीमसेनके उधर आनेका पता लूग गया। उन्होंने सोचा कि
- **Translation**: 

---

### Verse 4 (Mahabharat 0.1172)
- **Original**: भीमसेनके उधर आनेका पता लूग गया। उन्होंने सोचा कि
- **Translation**: 

---

### Verse 5 (Mahabharat 0.1173)
- **Original**: 268 संक्षिप्त महाघारत [ बनपर्व भीपसेनका इधरसे होकर स्वर्गमें जाना उचित नहीं है, क्योंकि
- **Translation**: 

---

### Verse 6 (Mahabharat 0.1173)
- **Original**: 268 संक्षिप्त महाघारत [ बनपर्व भीपसेनका इधरसे होकर स्वर्गमें जाना उचित नहीं है, क्योंकि
- **Translation**: 

---

### Verse 7 (Mahabharat 0.1174)
- **Original**: रोककर हिमालयके समान स्थित थे। ऐसा करनेसे सम्भव है यार्गमें कोई उनका तिरस्कार कर दे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.1174)
- **Original**: रोककर हिमालयके समान स्थित थे। ऐसा करनेसे सम्भव है यार्गमें कोई उनका तिरस्कार कर दे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.1175)
- **Original**: उस महान्‌ बनमें हतुमानजीको अकेले लेटे देखकर अथवा उन्‍हें झाप दे दे। यह सोचकर उनकी रक्षा करनेके
- **Translation**: 

---

### Verse 10 (Mahabharat 0.1175)
- **Original**: उस महान्‌ बनमें हतुमानजीको अकेले लेटे देखकर अथवा उन्‍हें झाप दे दे। यह सोचकर उनकी रक्षा करनेके
- **Translation**: 

---

### Verse 11 (Mahabharat 0.1176)
- **Original**: महाबल्ली भीमसेन निर्भध उनके पास चले गये और विचारसे वे केलेके बगीचेमेंसे होकर जानेवाले सकड़े मार्यको
- **Translation**: 

---

### Verse 12 (Mahabharat 0.1176)
- **Original**: महाबल्ली भीमसेन निर्भध उनके पास चले गये और विचारसे वे केलेके बगीचेमेंसे होकर जानेवाले सकड़े मार्यको
- **Translation**: 

---

### Verse 13 (Mahabharat 0.1177)
- **Original**: बिजलीकी कड़कके समान भीषण सिंहनाद करने लूगे। रोककर लेट गये। यहाँ पड़े-पड़े जब ऑंघ आनेपर वे जैभाई
- **Translation**: 

---

### Verse 14 (Mahabharat 0.1177)
- **Original**: बिजलीकी कड़कके समान भीषण सिंहनाद करने लूगे। रोककर लेट गये। यहाँ पड़े-पड़े जब ऑंघ आनेपर वे जैभाई
- **Translation**: 

---

### Verse 15 (Mahabharat 0.1178)
- **Original**: भीमसेनकी उस गर्जनासे बनके जीव-जन्तु और पक्षियोंको 4 [/)
- **Translation**: 

---

### Verse 16 (Mahabharat 0.1178)
- **Original**: भीमसेनकी उस गर्जनासे बनके जीव-जन्तु और पक्षियोंको 4 [/)
- **Translation**: 

---

### Verse 17 (Mahabharat 0.1179)
- **Original**: #9 17 (
- **Translation**: 

---

### Verse 18 (Mahabharat 0.1179)
- **Original**: #9 17 (
- **Translation**: 

---

### Verse 19 (Mahabharat 0.1180)
- **Original**: 4 बड़ा जञास हुआ। महाबल्ली हनुमारजीने भी अपने नेज्रोंको 1 कुछ-कुछ खोलकर उपेक्षापूर्वक्ष भीमसेनकी ओर देखा और 2; फिर उन्हें अपने निकट पाकर मुसकराते हुए कहने लगे-- 5 टै
- **Translation**: 

---

### Verse 20 (Mahabharat 0.1180)
- **Original**: 4 बड़ा जञास हुआ। महाबल्ली हनुमारजीने भी अपने नेज्रोंको 1 कुछ-कुछ खोलकर उपेक्षापूर्वक्ष भीमसेनकी ओर देखा और 2; फिर उन्हें अपने निकट पाकर मुसकराते हुए कहने लगे-- 5 टै
- **Translation**: 

---

