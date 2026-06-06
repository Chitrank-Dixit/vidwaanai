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

### Verse 1 (Sama Ved 0.1161)
- **Original**: सम्पत्तिदाता याजकगण सुख, श्रेष्ठ-आवास और ऐश्वर्य की प्राप्ति करते हैं। अयाज्ञिकों को किसी पदार्थ की प्राप्ति नहीं होती तथा वे अभीष्ट ऐश्वर्य को स्पर्श करने में भी सक्षम नहीं होते
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1162)
- **Original**: 442. सदा गाव: शुचयो विश्वधायस: सदा देवा अरेपस:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1163)
- **Original**: (है याजको) ! गौएँ सर्वदा पवित्र, सभी प्राणियों को पोषण देने वाली, श्रेष्ठ तथा पाप-रहित होती हैं
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1164)
- **Original**: 443. आ याहि बनसा सह गाव: सचन्त वर्तनिं यदूधभि:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1165)
- **Original**: है उपादेवि ! अभीष्ठ प्रकाश के साध (पृथिवी पर) दूध से भरे थनों वाली गौएँ (अथवा पोषण से भरी किरणें) मार्ग में रहती हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1166)
- **Original**: 444. उप प्रक्षे मधुमति क्षियन्तः पुष्येम रयिं धीमहे त इन्द्र
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1167)
- **Original**: हे इद्धदेव ! मधुरस से पूर्ण यज्ञ के चम्मचों से युक्त ( यज्ञार्थ प्रस्तुत) धन-धान्य हम प्राप्त करें और आपके पास रहने वाले ।आपकी ओर उन्म्‌ख ), हम आपका ध्यान करने में समर्थ हों
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1168)
- **Original**: पूर्वार्चिके ऐड्रपर्वेणि चतु्थों5घ्याय: 7.63 445. अर्चनत्यर्क मरुतः स्वर्का आ स्तोभति श्रुतो युवा स इन्द्र:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1169)
- **Original**: श्रेष्ठ प्रकाशित मरूद्गण ! हम स्तुत्य इन्द्रदेव की अर्चना करते हैं । वे यौवनयुवत, प्रख्यात इन्द्रदेव सभी शत्रुओं का बध करने वाले हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1170)
- **Original**: 446, प्र व इन्द्राय वृत्रहन्तमाय विप्राय गा गायत य॑ जुजोषते
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1171)
- **Original**: है विवेकसम्पल मनुष्यो ! वत्र का बध करने में प्रवीण ज्ञानयुक्त इन्द्रदेव को लक्ष्यकर स्तोत्रों का गायन करो, जिन स्तोत्रों को वे आनन्दित होकर सुनते हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1172)
- **Original**: इति चतुर्त्रिश: खण्ड:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1173)
- **Original**: पञ्नत्रिश: खण्ड:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1174)
- **Original**: 447. अचेत्यग्निश्चिकितिईव्यवाड्‌ न सुमद्रथ:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1175)
- **Original**: समर्पित हविष्याननों को देवताओं के प्रति ले जाने वाले, ज्ञान-सम्पन्न, श्रेष्ठ हि से परिपूर्ण, देवताओं को प्रदत्त सभी पदार्थों को रथ के समान अभीष्ट स्थानों पर पहुँचाने वाले अग्निदेव सर्वज्ञ हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1176)
- **Original**: 48. अग्ने त्वं नो अन्तम उत त्राता शिवो भुवो वरूथ्य:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1177)
- **Original**: अम्निदेव आप स्तुत्य, निकटस्थ सहयोगी तथा हितकारी संरक्षक हो गए हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1178)
- **Original**: 449. भगो न चित्रों अग्निर्महोनां दधाति रत्मम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1179)
- **Original**: विशाल पदार्थों में सूर्यदेव के समान, स्तुत्य ऑप्निदेव स्तोताओं को ऐश्वर्य- सम्पन्न बनाते हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1180)
- **Original**: 450. विश्वस्य प्र स्तोभ पुरो वा सन्‍्यदिवेह नूनम्‌
- **Translation**: 

---

