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

### Verse 1 (Sama Ved 0.1681)
- **Original**: कुत्स आद्विरस 629
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1682)
- **Original**: सार्पराज्ञी 630-632 । भ्रस्कण्व काण्व 633-640 ।
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1683)
- **Original**: प्रजापति 641-650 । देवता- इद्ध 586-588, 595, 597-598, 601, 612, 623-625 । वरुण 589
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1684)
- **Original**: पवमान सोम 590, 592, 593, 596 । विश्वदेवा 591, 599, 610 । अन्न 514 । वायु 600 । प्रजापति 602 । सोम 603,604 । अग्नि605, 606, 609, 6 14-616 । अपांनपात्‌ 607 । रात्रि608 । लिड्रोक्त 611 । आत्मा अथवा अग्नि 613 । पुरुष 617-621 । द्यावापृधिवी 622 । गौ 626 । अग्नि पवमान 627 । सूर्य 628, 329, 633-640 । सूर्य अथवा आत्मा 630-632 । इन्द्र तैलोक्यात्मा 641-650 । छन्- बृहती 586 ।त्रिप्रपू 587, 589-590 594, 599,603-604, 606-607,612-614,622, 625-626,629 । गायत्री 5888,592-593,595, 597, 598, 600, 605, 627,630-640 । एकपाद्‌ जगती 591
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1685)
- **Original**: जगती 596, 609-610, 628 । अनुष्टप्‌ 601-602, 608, 617-621, 623-624 । महापंक्ति 611 । पंक्ति 615, 616 । शक्‍्वरी सोपसर्गा 641-650 ।
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1686)
- **Original**: 7 ्‌िइ6 रू 7
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1687)
- **Original**: ऋ- 70-22
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1688)
- **Original**: सामवेद-संहिता उत्तराचिक:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1689)
- **Original**: अथ प्रथमो5 ध्याय:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1690)
- **Original**: प्रथम: खण्ड:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1691)
- **Original**: 651.उपास्मै गायता नर: पवमानायेन्दवे । अभि देवाँ इयक्षते
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1692)
- **Original**: है याजको! देव शक्तियों के निमित, बज्ञार्थ प्रयुक्‍त होने वाले, शुद्ध हुए इस सोम की स्तुति करो
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1693)
- **Original**: 652.अभि ते मधुना पयो5 थर्वाणो अशिश्रयु:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1694)
- **Original**: देवं देवाय देवयु:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1695)
- **Original**: यह दिव्य रस देवों ने देव पुरुषों के लिए प्रकट किया है । इसे अधथर्वा ऋषियों (विज्ञान-वेत्ताओं) ने तुम्बारे (याजकों) लिए मधुर गो- दुग्ध के साथ मिलाया है ।
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1696)
- **Original**: 653.स नः पवस्व शं गवे शं जनाय शमर्वते । शं राजन्नोषधी भ्य:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1697)
- **Original**: है कल्याणकारी सोम ! आप स्वयं शुद्ध होकर पशुधन, प्रजाधन तथा अश्वादि सैन्यबल का कल्याण करें और ओषधियों को पवित्र बनाँ
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1698)
- **Original**: 654.दविद्युतत्या रुचा परिष्टो भन्त्या कृपा । सोमा: शुक्रा गवाशिर:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1699)
- **Original**: कान्तिमानू, तेजस्वी शब्दयुक्त धारा से शुद्ध हुए सोमरस को गाय के दूध में मिलाकर तेयार किया जाता है
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1700)
- **Original**: 655. हिन्वानो हेतृभिर्हित आ वाजं वाज्यक्रमीत्‌ । सीदन्तो वनुषो यथा
- **Translation**: 

---

