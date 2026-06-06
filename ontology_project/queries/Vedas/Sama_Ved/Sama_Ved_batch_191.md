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

### Verse 1 (Sama Ved 0.3801)
- **Original**: इन्द्र 1440-1443, 1450-1452, 1456-1459, 1468-1470, 1483-1488 । सूर्य 1453-1455
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3802)
- **Original**: सरस्वान्‌ 1460 । सरस्वती 1461
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3803)
- **Original**: सविता 1462
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3804)
- **Original**: ब्रह्मणस्पति 1463 । अग्नि पवमान 1464 । मित्रावरुण 1465-1467 । अग्नि 1474-1479 । अग्नि अथवा हवींषि 1480-1482
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3805)
- **Original**: छन्द- गायत्री 1435-1439, (1444-1452, 1460-1470, 1475-1482। अनुष्टप्‌ 1440-1442
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3806)
- **Original**: यृहती 1443 । जगती 1453-1455 । बा्हत प्रगाथ (विषमा बृहती, समा सतोबृहती) 1456-1459 । त्रिप्टुप्‌ 1471-1473, 1483-1485
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3807)
- **Original**: वर्धमाना गायत्री 1474 । अष्टि 1486
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3808)
- **Original**: । अतिशक्वरी 1487, 1488 ।
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3809)
- **Original**: इति त्रयोदशो5 ध्याय:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3810)
- **Original**: क्‍ा0सस2-बननस्स0 8333-77
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3811)
- **Original**: चतुर्दशो5 ध्याय:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3812)
- **Original**: प्रथम: खण्ड:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3813)
- **Original**: 1489. अभि प्र गोपतिं गिरेन्द्रमर्च यथा विदे
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3814)
- **Original**: सूनुं सत्यस्य सत्पतिम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3815)
- **Original**: हे स्तोताओ ! सत्य यज्ञ के पोषक भद्रजनों के संरक्षक, गो-पालक, इन इन्द्रदेव की सुन्दर स्तोत्रों से प्रार्थना करो
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3816)
- **Original**: 1490. आ हरयः ससृज़िरे3रुषीरधि बर्हिषि। यत्राभि संनवामहे
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3817)
- **Original**: इन्द्रदेव के अन्च प्रकाशयुक्त कुश-आसन पर इन्द्रदेव को अधिष्ठित करें । जहाँ प्रतिष्ठित हुए इद्धदेव की हम (यजमान) स्तुति करते हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3818)
- **Original**: 1491. इन्द्राय गाव आशिर दुदुढ्ढे वच्रिणे मधु । यत्सीमुपह्रे विदत्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3819)
- **Original**: जब यज्ञस्थल में समीप ही इन्द्रदेव मधुर रस का पान करते हैं, तब गौएँ वज्रहस्त इन्द्रदेव के (पान करने के) लिए मधुर दुग्ध प्रदान करती हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3820)
- **Original**: 1492.आ नो विश्वासु हव्यमिन्द्रं समत्सु भूषत । उप ब्रह्माणि सवनानि वृत्रहन्‌ परमज्या ऋचीषम
- **Translation**: 

---

