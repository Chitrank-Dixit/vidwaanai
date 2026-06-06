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

### Verse 1 (Mahabharat 0.5231)
- **Original**: घोड़ोंको धीरे-धीरे आगे बढ़ाया। आपकी ओरसे युद्धके लिये अबच्थां देख दुर्वोधन हाहाकार करके उठा और अपने
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5231)
- **Original**: घोड़ोंको धीरे-धीरे आगे बढ़ाया। आपकी ओरसे युद्धके लिये अबच्थां देख दुर्वोधन हाहाकार करके उठा और अपने
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5232)
- **Original**: पश्चीस हजार पैदल खड़े थे, उन्हें भीपसेन और थ्ृष्टशुप्नने सारधिसे बोल्म--'सूत ! तुम धीरे-भीरे घोड़ोंको आगे
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5232)
- **Original**: पश्चीस हजार पैदल खड़े थे, उन्हें भीपसेन और थ्ृष्टशुप्नने सारधिसे बोल्म--'सूत ! तुम धीरे-भीरे घोड़ोंको आगे
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5233)
- **Original**: अपनी चतुरड्षिणी सेनासे घेर लिया और बाणोंसे:मारता बढ़ाओ। जब हाथमें धनुष लेकर मैं अपनी सम्पूर्ण सेनके आरम्भ किया। वे भी. भीम और धृष्टशुप्रका-डटकर पीछे खड़ा रहूँगा, उस समय अं्जुन मुझे परास्त नहीं कर
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5233)
- **Original**: अपनी चतुरड्षिणी सेनासे घेर लिया और बाणोंसे:मारता बढ़ाओ। जब हाथमें धनुष लेकर मैं अपनी सम्पूर्ण सेनके आरम्भ किया। वे भी. भीम और धृष्टशुप्रका-डटकर पीछे खड़ा रहूँगा, उस समय अं्जुन मुझे परास्त नहीं कर
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5234)
- **Original**: मुकाबला करने छगे। उस समय भीमसेन क्रोधमें भरकर सकते
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5234)
- **Original**: मुकाबला करने छगे। उस समय भीमसेन क्रोधमें भरकर सकते
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5235)
- **Original**: यदि ये मुझसे लड़ने आयेंगे तो निससन्‍्देह उन्हें मार
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5235)
- **Original**: यदि ये मुझसे लड़ने आयेंगे तो निससन्‍्देह उन्हें मार
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5236)
- **Original**: हाथमें गदा लियें रथसे उतर पड़े और उन सबके साथ युद्ध डालूगा। आज मैं अर्जुन, औकृष्ण तथा घमंडी भीमसेनको
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5236)
- **Original**: हाथमें गदा लियें रथसे उतर पड़े और उन सबके साथ युद्ध डालूगा। आज मैं अर्जुन, औकृष्ण तथा घमंडी भीमसेनको
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5237)
- **Original**: करने छंगे। भीमसेन युद्धपर्मका पालन करतेबाले थे, बचे-खुचे अन्य शत्रुओंके साथ मौतके घाट उतारकर कर्णके
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5237)
- **Original**: करने छंगे। भीमसेन युद्धपर्मका पालन करतेबाले थे, बचे-खुचे अन्य शत्रुओंके साथ मौतके घाट उतारकर कर्णके
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5238)
- **Original**: इसीलिये स्वयं रथपर बैठकर उन्होंने उन पैदल्ॉंके साथ युद्ध ऋणसे मुक्त होऊँगा।
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5238)
- **Original**: इसीलिये स्वयं रथपर बैठकर उन्होंने उन पैदल्ॉंके साथ युद्ध ऋणसे मुक्त होऊँगा।
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5239)
- **Original**: नहीं किया। उन्हें अपने बाहुअलका पूरा भरोसा था।
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5239)
- **Original**: नहीं किया। उन्हें अपने बाहुअलका पूरा भरोसा था।
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5240)
- **Original**: 3. मैं
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5240)
- **Original**: 3. मैं
- **Translation**: 

---

