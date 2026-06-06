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

### Verse 1 (Sama Ved 0.3661)
- **Original**: पवमान सोम 1386-1388, 1394-1395, 1399-1401, 1408-1410, 1418-1420, 1423-1428 । इन्द्र 1389-1393, 1402-1404, 1411-1412, 1421-1422, 1429-1434
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3662)
- **Original**: . छन्द- गायत्री 1379-1385, 1396-1398, 1405-1407, 1415-1417। अनुष्टप्‌ 1386-1388, 1402-1404, 1429-1430, 1433-1434
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3663)
- **Original**: काकुभ प्रगाथ (विषमा ककुंपू, समा सतोबृहती) 1389-1390, 1394-1395, 1413-1414
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3664)
- **Original**: बृहती 1391-1393, 1431। विष्टप्‌ 1399-1401, 1408-1410, 1418-1420, 1426-1428 । बार्हत प्रगाथ (विषमा बृहती, समा सतोबृहती) 1411-1412, 1421-1422 । जगती 1423-1425 । स्कम्धोग्रीवी बृहती 1432
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3665)
- **Original**: इति द्वादशो5 ध्याय:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3666)
- **Original**: ा पल -गहनरसन्‍23-+...--
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3667)
- **Original**: अथ त्रयोदशो<5 ध्याय:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3668)
- **Original**: अथ प्रथम: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3669)
- **Original**: 1435. पवस्व वृष्टिमा सुनो 5पामूर्मि दिवस्परि । अयक्ष्मा बृहतीरिष:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3670)
- **Original**: हे दिव्य सोम ! आप (हमारे लिए) च्युलोक से उत्तम रीति से वृष्टि करें । जल को तरंगित करें और स्वास्थ्यकारी अन हमें प्रदान करें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3671)
- **Original**: * 1436. तया पवस्व धारया यया गाव इहागमन्‌ । जन्यास उप नो गृहम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3672)
- **Original**: हे सोमदेव ! आप उस (दिव्य) जलधारा से पवित्र हों (अर्थात्‌ जल बरसाएँ), जिससे दुधारू गौएँ (पोषक तत्व-अन्नादि) हमारे घर पहुँचें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3673)
- **Original**: 1437. घृत॑ पवस्व धारया यज्ञेषु देववीतम: । अस्मभ्य॑ं वृष्टिमा पव
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3674)
- **Original**: हे सोमदेव ! यज्ञ में देवों द्वारा चाहे गये आप धार-रूप जल की वृष्टि करें । (मूसलाधार वर्षा करें)
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3675)
- **Original**: 1438. स न ऊर्जे व्य3व्ययं पवित्रं घाव धारया
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3676)
- **Original**: देवास: शृणवन्‌ हि कम्‌
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3677)
- **Original**: हे सोमदेव ! हमें (पोषणयुक्त) अन्न प्रदान करने के लिए आप छने से धाररूप में मकर (शोधित होकर) कलश में प्रविष्ट हों
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3678)
- **Original**: देवगण आपके (मधुर) शब्द सुनकर उल्लसित हों
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3679)
- **Original**: 1439. पवमानों असिधष्यदद्र॒क्षांस्पपजड्घनत्‌। प्रलवद्रोचयब्रुच:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3680)
- **Original**: शत्रुओं का नाश करने वाला, तेज से देदीप्यमान, पवित्र होने वाला सोमरस कलश में स्नवित होता है
- **Translation**: 

---

