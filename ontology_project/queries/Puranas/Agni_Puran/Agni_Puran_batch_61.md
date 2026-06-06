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

### Verse 1 (Agni Puran 0.1201)
- **Original**: गामध देवी हिरण्य॑ बिन्देय॑ शर्मा पुरुषानहम्‌
- **Translation**: 

---

### Verse 2 (Agni Puran 0.1202)
- **Original**: जुघताम्‌
- **Translation**: 

---

### Verse 3 (Agni Puran 0.1203)
- **Original**: 5. चद्रां प्रभासां यज्ञसा ज्वलन्तों ज्रिय॑ लोके . देवजुष्टामुदाराम्‌ । तां पद्मिनीमी शरणं प्रपतश्चेउलक्ष्मीमें नश्यतां त्वाँ वृणे
- **Translation**: 

---

### Verse 4 (Agni Puran 0.1204)
- **Original**: 6. आदित्यवर्णे तपसो5धि जातों. यनस्पतिस्तव वृक्षोौ5धबिल्व: । तस्य फलानि तपसा नुदन्तु या अन्तर याश्ष बराह्म अलक्ष्मी:
- **Translation**: 

---

### Verse 5 (Agni Puran 0.1205)
- **Original**: 7. उपतु मां देवसखः: कॉर्िश्व सजिता . सह
- **Translation**: 

---

### Verse 6 (Agni Puran 0.1206)
- **Original**: प्रादुर्भृतोडस्मि राष्ट्रेस्सिन. कीर्तिमूर्धि ददातु में
- **Translation**: 

---

### Verse 7 (Agni Puran 0.1207)
- **Original**: <, श्षुत्पिपासामलां ज्येप्ठामलक्ष्मी नाशयाम्यहम्‌
- **Translation**: 

---

### Verse 8 (Agni Puran 0.1208)
- **Original**: अभूतिमसमूद्धि.। च सर्वा निर्णुद में पृहात्‌। 9, गन्द्टारां दुराधर्षों नित्षपुष्टा करीषिणोम्‌
- **Translation**: 

---

### Verse 9 (Agni Puran 0.1209)
- **Original**: ईश्वर सर्वभूतातां तामिहोपह्ये. क्रियम्‌
- **Translation**: 

---

### Verse 10 (Agni Puran 0.1210)
- **Original**: 10. मत्रस काममाकूतिं बाच: सत्यमशीमहि । पशूनां.. रूपमन्तस्थ शी: श्रयर्ता यश:
- **Translation**: 

---

### Verse 11 (Agni Puran 0.1211)
- **Original**: 11. कर्दमेत प्रजा भूता मयि सम्भव कर्दम
- **Translation**: 

---

### Verse 12 (Agni Puran 0.1212)
- **Original**: ब्रियं बासय में कुले मातर॑ चघद्ममालिनीम्‌
- **Translation**: 

---

### Verse 13 (Agni Puran 0.1213)
- **Original**: 12. आप। सूजन्तु स्किधानि चिक्‍लीत वस में गृहे।नि ला देवीं मातर॑ ब्रियँ वासव में कुले
- **Translation**: 

---

### Verse 14 (Agni Puran 0.1214)
- **Original**: 13. आई पुष्करिणी पुष्टि. पिछला. पद्ममालिनीम्‌
- **Translation**: 

---

### Verse 15 (Agni Puran 0.1215)
- **Original**: चन्द्रां हिरण्मयीं लक्ष्मी जातवेदों म आ यह
- **Translation**: 

---

### Verse 16 (Agni Puran 0.1216)
- **Original**: 14. आई यः करिणी यहिं सुवर्णा हेममालिनोम्‌
- **Translation**: 

---

### Verse 17 (Agni Puran 0.1217)
- **Original**: सूर्याँ हिरण्मयों लक्ष्मी जातवेदों म आ यह
- **Translation**: 

---

### Verse 18 (Agni Puran 0.1218)
- **Original**: 15. ता मभ आ सह. जातवेदों लक्ष्मीमनपगामिनोम्‌
- **Translation**: 

---

### Verse 19 (Agni Puran 0.1219)
- **Original**: यस्यां हिरण्यं प्रभूतं गायों दास्वो5 श्रान्‌ विन्देर्य पुरुषानहम्‌
- **Translation**: 

---

### Verse 20 (Agni Puran 0.1220)
- **Original**: 16. आनन्दमन्थरपुरन्दरमुक्तमाल्यं मौलौ बलेन निहित॑ महिषासुरस्थ । पादाम्बुज भवतु भे विजयाय मझुमओरफिखितमनोहस्मम्विकत्पा:
- **Translation**: 

---

