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

### Verse 1 (Sama Ved 0.3521)
- **Original**: अग्नि धि7ष्णय ऐश्वर 1367-1369 । हिरण्यस्त्प आंगिरस 1370-1372 । सार्पराज्ञी 1376-1378 । देवता- आप्री सूक्त ( इध्म अथवा समिद्ध अग्नि, तनूनपातू, नराशंस, इडा ) 1347-1350 । आदित्य 1351-1353 । इद्ध 1354-1356, 1360-1363 । पवमान सोम 1357-1359, 1364-1372
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3522)
- **Original**: अग्नि 1373-1375 । आत्मा अथवा सूर्य 1376-1378 । छन्द- गायत्री 1347-1356, 1376-1378 । त्रिष्टुप्‌ 1357-1359 । बार्हत प्रगाथ (विषमा बृहती, समा सतोबृहती) 1360-1363 । पिपीलिकमध्या अनुष्टप्‌ 1364-1366
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3523)
- **Original**: द्विपदा विराट गायत्री 1367-1369 । जगती 1370-1372 । वियाट्‌ स्वाना 1373-1375 ।
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3524)
- **Original**: डति एकादशोउ ध्यायः
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3525)
- **Original**: --,0्णपदिटिममिक.00000----
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3526)
- **Original**: अथ द्वादशो5 ध्याय:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3527)
- **Original**: प्रथम: खण्ड:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3528)
- **Original**: 1379. उपप्रयन्तो अध्यरं मन्त्र वोचेमाग्नये । आरे अस्मे च शृण्वते
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3529)
- **Original**: श्रेष्ठ यज्ञ कर्म करने वाले याजकों की स्तुति सुनने को उद्यत अग्निदेव की हम वन्दना करते हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3530)
- **Original**: 1380. यः स्नीहितीषु पूर्व्य: संजग्मानासु कृष्टिषु । अरक्षद्ाशुषे गयम्‌
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3531)
- **Original**: सदा जाज्वल्यमान्‌ वे अग्निटेव परस्पर स्नेह-सौजन्ययुक्त प्रजाओं के एकत्र होने पर, दाताओं के ऐश्वर्य की रक्षा करते हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3532)
- **Original**: 1381. स नो वेदो अमात्यमग्नी रक्षतु शन्तम:। उतास्मान्पात्यं हसः
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3533)
- **Original**: अत्यन्त कल्याणकारी वे अग्निदेव हमारे धन की रक्षा में सहायक हों और हमें पापों से दूर करें
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3534)
- **Original**: 1382. उत ब्रुवन्तु जन्तव उदग्निर्वृत्रहाजनि । धनञ्यो रणेरणे
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3535)
- **Original**: . शत्रुनाशक युद्ध में शत्रुओं को पराजित कर घन जीतने वाले अग्निदेव का प्राकट्य हुआ है, उद्गाता उनकी स्तुति करें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3536)
- **Original**: [अभि-विद्या के अन्वेषण की प्रेरणा मंत्र में निहित है ।]
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3537)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3538)
- **Original**: क्र के
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3539)
- **Original**: द्वितीय खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3540)
- **Original**: 1383. अग्ने युक्ष्वा हि ये तवाश्वासो देव साधव: । अर॑ वहन्त्याशव:
- **Translation**: 

---

