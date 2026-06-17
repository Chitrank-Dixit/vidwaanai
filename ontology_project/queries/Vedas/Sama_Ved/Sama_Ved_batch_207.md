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

### Verse 1 (Sama Ved 0.4121)
- **Original**: 1616.अग्रेगो राजाप्यस्तविष्यते बिमानो अह्डां भुवनेष्वर्पित: । हरिर्धृतस्नु: सुदूशीको अर्णवो ज्योतीरथ: पवते राय ओक्‍्य:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.4122)
- **Original**: प्रगतिशील राजा सोम, जल में मिश्रित होता हुआ प्रशंसित होता है । वह दिवस का मापक (निर्माण करने वाला) सोम जल में स्थापित है । हरित्‌ वर्ण के जल मिश्रित, सुन्दर, दर्शनीय और जल में निवास करने वाला, ज्योतिस्वरूप रथ वाला सोम धनागार स्वरूप है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.4123)
- **Original**: इति चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.4124)
- **Original**: 16.8 सापवेट-संहिता ऋषि, देवता, छन्‍्द-विवरण ऋषि- मेध्यातिथि काण्व 1573-1574, 1587-1588, 1607-1608 । विश्वामित्र गाधिन (575-1578 । भर्म प्रागाथ 1579-1582 । सोभरि काण्व 1583-1584 । शुनःशेष आजीगर्ति 1585, 1599, 1601 । सुकक्ष आड्रिसस 1586 । विश्वकर्मा भौवन 1589 । अनानत पारुच्छेपि 1590-1592। भरद्वाज बार्हस्पत्य 1593। गोतम राहुगण 1594। ऋजिश्वा भरद्वाज 1595। बामदेव गौतम 1596-1598 । हर्यत प्रागाव 160 2-1604 । देवातिधि काण्व 1605-1606 । वालखिल्य (श्रुष्टिगु काण्व) 1609-1610 । पर्वत-नारद 1611-16613 । अत्रि भौम 1614-1616
- **Translation**: 

---

### Verse 5 (Sama Ved 0.4125)
- **Original**: देवता- इन्द्र 1573-1574, 1579-1582, 1586-1588, 1599-1601, 1605-1610 । इन्द्राग्गी 1575-1578
- **Translation**: 

---

### Verse 6 (Sama Ved 0.4126)
- **Original**: अग्नि 1583-1584
- **Translation**: 

---

### Verse 7 (Sama Ved 0.4127)
- **Original**: वरुण 1585
- **Translation**: 

---

### Verse 8 (Sama Ved 0.4128)
- **Original**: विश्वकर्मा 1589 । पवमान सोम 1590-1592, 1611-1616
- **Translation**: 

---

### Verse 9 (Sama Ved 0.4129)
- **Original**: पूृषा 1593
- **Translation**: 

---

### Verse 10 (Sama Ved 0.4130)
- **Original**: मरुद्गण 1594। विश्लेदेवा 1595
- **Translation**: 

---

### Verse 11 (Sama Ved 0.4131)
- **Original**: द्यावापरथिवी 1596-1598 । अग्नि अथवा हवींषि 1602-1604 । छन्द- बार्हत प्रगाथ (विषमा यृहती, समा समोबृहती) 1573-1574, 1579-1584, 1587-1588, 1605-1610 । गायत्री 1575-1578, 1585-1586, 1593-1604। त्रिष्टप्‌ 1589
- **Translation**: 

---

### Verse 12 (Sama Ved 0.4132)
- **Original**: । अत्यष्टि 1590-1592 । उष्णिक्‌ 1611-1613
- **Translation**: 

---

### Verse 13 (Sama Ved 0.4133)
- **Original**: जगती 1614-1616 ।
- **Translation**: 

---

### Verse 14 (Sama Ved 0.4134)
- **Original**: इति षोडशो5 ध्याय:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.4135)
- **Original**: ता 8 उस <ू0 -> नयी
- **Translation**: 

---

### Verse 16 (Sama Ved 0.4136)
- **Original**: अथ सप्तदशो5 ध्याय:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.4137)
- **Original**: प्रथम: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.4138)
- **Original**: 1617. विश्वेभिरग्ने अग्निभिरिमं यज्ञमिदं वचः
- **Translation**: 

---

### Verse 19 (Sama Ved 0.4139)
- **Original**: चनो था: सहसो यहो
- **Translation**: 

---

### Verse 20 (Sama Ved 0.4140)
- **Original**: हे बल के पुत्र ! सभी अग्नियों के साथ आप हमारे यज्ञ में पधारें और स्तुतियों को सुनते हुए हमें अन्न (पोषण) प्रदान करें
- **Translation**: 

---

