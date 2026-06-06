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

### Verse 1 (Padam Puran 7.1701)
- **Original**: सावित्रीजापनिरत:.. शआद्धकुत्मुच्यते. शृही । मातापित्रोर्हिते युक्तो ब्राहप्णस्य हिते स्तः
- **Translation**: 

---

### Verse 2 (Padam Puran 7.1702)
- **Original**: दाता यज्या वेदभत्ते बरह्मल्मेके महोयते।त्रिवर्गसेवी सतते देवानाँ च समर्चनम्‌
- **Translation**: 

---

### Verse 3 (Padam Puran 7.1703)
- **Original**: एतस्मान्न॒ प्रमाद्येत. विज्येषेण. द्विजोत्तमः
- **Translation**: 

---

### Verse 4 (Padam Puran 7.1704)
- **Original**: यथाशक्ति चरन्‌ धर्म निन्दितानि विवर्जयेत्‌
- **Translation**: 

---

### Verse 5 (Padam Puran 7.1705)
- **Original**: जिधूणब सोहकलिले लब्ध्या योगमनुत्तमम्‌। गृहरथों मुच्यते बन्धान्नात्र कार्या विचारणा
- **Translation**: 

---

### Verse 6 (Padam Puran 7.1706)
- **Original**: विगरहीतिजयाक्षेपहिसाबय्थवधघात्मनाम्‌ । अन्यमन्युसमुत्थानों दोषाणों मर्षण क्षमा
- **Translation**: 

---

### Verse 7 (Padam Puran 7.1707)
- **Original**: स्वदुःशेषु च कारुण्य परदुःखेषु सौहदम्‌। दयेति मुनयः प्राहुः साक्षाद्धर्मस्थ साधनम्‌
- **Translation**: 

---

### Verse 8 (Padam Puran 7.1708)
- **Original**: अज्ननि वेदाअत्वारों मीमोसा न्यायविस्तर:
- **Translation**: 

---

### Verse 9 (Padam Puran 7.1709)
- **Original**: पुराण॑- धर्मशास्त्रे च विद्या एताश्नतुर्दश
- **Translation**: 

---

### Verse 10 (Padam Puran 7.1710)
- **Original**: चतुर्दशानों बिधानों धारणा हि. यधार्थतः
- **Translation**: 

---

### Verse 11 (Padam Puran 7.1711)
- **Original**: विज्ञानमिति तट्ठिद्याध्ेन धर्मों विवर्धते
- **Translation**: 

---

### Verse 12 (Padam Puran 7.1712)
- **Original**: अधीत्य विधिवद्विद्यामथ॑ चैबोपल्भ्य तु । धर्मकर्माण. कुर्यीत. ट्लेतद्विज्ञानमुच्यते
- **Translation**: 

---

### Verse 13 (Padam Puran 7.1713)
- **Original**: ' स्पेन ल्फरेके जयति सत्य॑ ततू परम पदम्‌।यथाभूताप्रमाद॑ तु॒ सत्यमाहुर्मनीफिण:
- **Translation**: 

---

### Verse 14 (Padam Puran 7.1714)
- **Original**: दमेः जमः. प्रज्ञप्रसादतः
- **Translation**: 

---

### Verse 15 (Padam Puran 7.1715)
- **Original**: अध्यात्ममक्षर विद्यात्त गत्वा न श्ोचति
- **Translation**: 

---

### Verse 16 (Padam Puran 7.1716)
- **Original**: अया स देयों भगवान्‌ विध्यया विद्वते पर:। साक्षादेव हृषीकेशस्तम्ज्ञानमितति कीर्तितम्‌
- **Translation**: 

---

### Verse 17 (Padam Puran 7.1717)
- **Original**: - / झुचिः
- **Translation**: 

---

### Verse 18 (Padam Puran 7.1718)
- **Original**: महायज्ञपरों बिप्रों. ऊूभते - तदनुतमम्‌
- **Translation**: 

---

### Verse 19 (Padam Puran 7.1719)
- **Original**: धर्मस्पावतन॑ यल्राच्छीरे. परिपाल्येत्‌। न हि देहे खिना विष्णु: पुरुषैर्बिद्यते परः
- **Translation**: 

---

### Verse 20 (Padam Puran 7.1720)
- **Original**: नित्य॑धर्मार्थकामेषु युज्वेत नियतो द्विज:।न घर्मवर्जित॑ काममथै या मनसा स्मरेत्‌
- **Translation**: 

---

