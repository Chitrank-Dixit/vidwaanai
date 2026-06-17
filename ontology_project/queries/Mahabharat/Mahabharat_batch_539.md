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

### Verse 1 (Mahabharat 0.5381)
- **Original**: हमलोग युद्धके लिये उपस्थित हुए थे, उस समय हमारे प्रास
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5381)
- **Original**: हमलोग युद्धके लिये उपस्थित हुए थे, उस समय हमारे प्रास
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5382)
- **Original**: ग्यारह हजार रथ, दस हजार सात सौ हाथो, दो लाख घोड़े तथा तीन करोड़ पैदल थे और पाण्डवोंके पास छ: हजार रथ,
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5382)
- **Original**: ग्यारह हजार रथ, दस हजार सात सौ हाथो, दो लाख घोड़े तथा तीन करोड़ पैदल थे और पाण्डवोंके पास छ: हजार रथ,
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5383)
- **Original**: छ: हजार हाथी, दस हजार घोड़े तथा एक करोड़ पैदल मौजूद
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5383)
- **Original**: छ: हजार हाथी, दस हजार घोड़े तथा एक करोड़ पैदल मौजूद
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5384)
- **Original**: और जहाँ ये राजा खड़े हैं, वहीं मुझे ले चत्म्रे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5384)
- **Original**: और जहाँ ये राजा खड़े हैं, वहीं मुझे ले चत्म्रे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5385)
- **Original**: आज थे। बस, इतनी ही सेतरा बच गयी थी और यही युद्धके लिये
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5385)
- **Original**: आज थे। बस, इतनी ही सेतरा बच गयी थी और यही युद्धके लिये
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5386)
- **Original**: संग्राममें ये मेरे साथने ठहर नहीं सकते।' सेनापतिकी उपस्थित थी। त्रातःकाल सूर्योदय होते ही दोनों ओस्के योद्धा
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5386)
- **Original**: संग्राममें ये मेरे साथने ठहर नहीं सकते।' सेनापतिकी उपस्थित थी। त्रातःकाल सूर्योदय होते ही दोनों ओस्के योद्धा
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5387)
- **Original**: आज्ञासे सारधिने उनके रथको राजा युधिष्ठिरके पास पहुँचा एक-दडूसरेको मार डालनेकी इच्छासे आगें बढ़े । फिर तो दोनों
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5387)
- **Original**: आज्ञासे सारधिने उनके रथको राजा युधिष्ठिरके पास पहुँचा एक-दडूसरेको मार डालनेकी इच्छासे आगें बढ़े । फिर तो दोनों
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5388)
- **Original**: दिया। वहाँ पहुँचकर बड़े वेगसे आक्रमण करती. हुई दल्लोंपें अत्यन्त भयंकर युद्ध-छिड़ गया। हजारों घुड़सवार,
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5388)
- **Original**: दिया। वहाँ पहुँचकर बड़े वेगसे आक्रमण करती. हुई दल्लोंपें अत्यन्त भयंकर युद्ध-छिड़ गया। हजारों घुड़सवार,
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5389)
- **Original**: पाण्डबोंकी बिज्ञाल सेनाकों झाल्यने अकेले ही रोक दिया.। पैदल, रथी और हाथीसवार पराक्रम दिखाते हुए एक-दूसरेसे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5389)
- **Original**: पाण्डबोंकी बिज्ञाल सेनाकों झाल्यने अकेले ही रोक दिया.। पैदल, रथी और हाथीसवार पराक्रम दिखाते हुए एक-दूसरेसे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5390)
- **Original**: उस समय मद्रराजकों समरभूमिमें डटे हुए देख भागनेवाले घिड़ गये।
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5390)
- **Original**: उस समय मद्रराजकों समरभूमिमें डटे हुए देख भागनेवाले घिड़ गये।
- **Translation**: 

---

