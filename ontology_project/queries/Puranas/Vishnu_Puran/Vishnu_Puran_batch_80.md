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

### Verse 1 (Vishnu Puran 0.1581)
- **Original**: होंगे उन्हींसे तुम इनका स्तवन करो ।
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1582)
- **Original**: 56 अीपराशर उवाच ततः स नृपतिस्तो्ष तच्छुत्वा परम ययौ। सदुणैः इलाघ्यतामेति तस्माल्लभ्या गुणा मम
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1583)
- **Original**: 57 तस्माद्मद्य स्तोत्रेण गुणनिर्वर्णनं त्विमों । करिष्येते करिष्यामि तदेवाह॑ समाहित:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1584)
- **Original**: 58 यदिमौ वर्जनीयं च किझ्निदत्र वदिष्यत: । तदहं वर्जयिष्यामीत्येवे चक्रे मति नृषः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1585)
- **Original**: 59 अथ तौ चक्रतुः स्तोत्र पृथोैंन्यस्य धीमत: । भविष्यै: कर्मभि: सम्यक्सुस्वरी सूतमागधौ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1586)
- **Original**: 60 सत्यवाग्दानशीलोउय सत्यसन्धो नरेश्वर: । समः शात्रौ च मित्रे च व्यवहारस्थितो नृप:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1587)
- **Original**: 63 सूतेनोक्तान्‌ गुणानित्थं स तदा मागधेन च । चकार हृदि तादुक्‌ च कर्मणा कृतवानसो
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1588)
- **Original**: 64 प्रजा ऊचु: अराजके नृपश्रेष्ठ धरित्या सकलौषधी: । अस्तास्तत: क्षय यान्ति प्रजा: सर्वा: प्रजेश्चर
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1589)
- **Original**: 67 त्वन्नो वृत्तिप्रदो घात्रा प्रजापात्तो निरूपित: । देहि नः क्षुत्परीतानां प्रजानों जीवनौषधी:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1590)
- **Original**: 68 शरीपराशर उवाच ततस्तु नृपतिर्दिव्यमादायाजगव॑ थनु:। अरांश्व दिव्यान्कुपितः सोन्‍्त्रधाबइसुन्यराम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1591)
- **Original**: 69 ततो ननाश त्वरिता गौर्भूत्या च् वसुन्धरा । सा लोकानहालोकादीन्सन्त्रासादगमन्पही
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1592)
- **Original**: 70 यत्र यत्र ययो देवी सा तदा भूतधारिणी
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1593)
- **Original**: तत्न तत्र तु सा. वैन्‍्यं ददृशेउ्भ्युद्धतायुधम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1594)
- **Original**: । 712 श्रीविष्णुप्राण ( अः ₹3 भ्रीपराझ्रजी बोलले--यह सुत्कर ग़जाकों भी परम सन्‍्तोष हुआ; उन्होंने सोचा 'मनुष्य सदगुणोंके कारण ही प्रशंसाक पाज़ होता है; अतः मुझको भी गुण उपार्जन करने चाहिये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1595)
- **Original**: इसलिये अब स्वुतिके द्वारा ये जित गुणोंका वर्णन करेंगे मैं भी सावधानतापूर्यक वैसा हो करूँगा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1596)
- **Original**: यदि यहाँपर ये कुछ त्याज्य अबगुणोंको भी कहेंगे तो मैं उन्हें त्यागुंगा ।' इस प्रकार राजाने अपने चित्तमें निश्चय किया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1597)
- **Original**: तदनन्तर उन (सूत और मागध) दोनोने परम बुद्धिमान्‌ वेननन्दन मत्तराज पृथुका, उनके भावी कर्मोके आश्रयसे स्वरसहित भी प्रकार स्तथन किया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1598)
- **Original**: [ उन्होंने कहा-- ) “ये महाराज सत्यवादी, दानशोल, सत्यमर्यादावाले, लज्जाशील, सुहद, क्षमाशील, पराक्रमी और दुष्टोंका दमन करनेवाले हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1599)
- **Original**: ये घर्मज्ञ, कृतश, दयावान्‌, प्रियभाषो, माननीयोंको मान देनेवाले, यज्ञपरायण, ब्रह्मण्य, साघुसमाजमें सम्मानित और शत्रु तथा मित्रके साथ समान व्यवहार करनेवाले हैं'
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1600)
- **Original**: इस प्रकार सूत और मागधके कहे हुए गुणोंकों उन्होंने अपने चित्तमें धारण किया और उसी प्रकारके कार्य किये
- **Translation**: 

---

