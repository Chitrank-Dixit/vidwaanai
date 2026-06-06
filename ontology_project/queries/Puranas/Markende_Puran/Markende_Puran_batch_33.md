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

### Verse 1 (Markende Puran 0.641)
- **Original**: न? पततिको सम्पूर्ण देवताओंसे जड़ा मानती हो रहा है। अब दिनको सुष्टि कैसे हो ?' इस प्रकार
- **Translation**: 

---

### Verse 2 (Markende Puran 0.642)
- **Original**: 1? पतिकी सेवासे ही मुझे महान्‌ फलकौ प्राप्त सब देवता आपसमें बात करने लगे। यज्ञेके हुई है तथा सम्पूर्ण कामनाओं एवं फलॉको बिनाशकी आशल्लासे वहाँ एकत्रित हुए देवताओंके
- **Translation**: 

---

### Verse 3 (Markende Puran 0.643)
- **Original**: प्राप्तिके साथ हो मेरे सारे त्रिष्न भी दूर हो गये।
- **Translation**: 

---

### Verse 4 (Markende Puran 0.644)
- **Original**: वबन सुनकर ग्रजापति ब्रह्माजोने कहा--' पतित्रताके
- **Translation**: 

---

### Verse 5 (Markende Puran 0.645)
- **Original**: साभ्वो! मनुप्यको पाँच ऋण सदा ही चुकाने माहात्म्यसे इस समय सूर्यका उदय नहाँ हो रहा
- **Translation**: 

---

### Verse 6 (Markende Puran 0.646)
- **Original**: चाहिये। अपने वर्णधर्मके अगुप्तार थनका संग्रह हैं और सूर्योदय न होनेसे मनुष्यों तथा तुम
- **Translation**: 

---

### Verse 7 (Markende Puran 0.647)
- **Original**: करता आवश्यक्त है। उसके प्राप्त होनेपर शास्व्रविधिके देवताओंकी भी हांसि है; अत: तुमलोग महर्षि
- **Translation**: 

---

### Verse 8 (Markende Puran 0.648)
- **Original**: अनुसार उसका सत्पात्रको दान करना चाहिये। अत्रिकी पतिव्वता पत्नी तपस्चिनी अतसूयाके पास
- **Translation**: 

---

### Verse 9 (Markende Puran 0.649)
- **Original**: संत्य, सरलता, तपस्या, दाग और दवासे सदा जाओ और सूर्योदयकी कामनासे उन्हें प्रसन्न
- **Translation**: 

---

### Verse 10 (Markende Puran 0.650)
- **Original**: युक्त रहना चाहिये। राग-द्रेषका परित्याग करके करो।'* शास्त्रोक्त करमोंका अपनी शक्तिके अनुसार प्रतिदिन जब देखताओंने जाकर अनसूयाजीक़ों प्रसन्न
- **Translation**: 

---

### Verse 11 (Markende Puran 0.651)
- **Original**: श्रद्धापूर्वक अनुष्ठान करना आहिबे। ऐसा करनेसे किया। वे बौलीं--'तुम क्या चाहते हो,
- **Translation**: 

---

### Verse 12 (Markende Puran 0.652)
- **Original**: मनुष्य अपने वर्णकरे लिये बिहित उत्तम लोकोंको बतलाओ
- **Translation**: 

---

### Verse 13 (Markende Puran 0.653)
- **Original**: देबहाओंने साधना को कि “पूर्वदत्‌
- **Translation**: 

---

### Verse 14 (Markende Puran 0.654)
- **Original**: प्राप्त होता है। पतित्नते! इस प्रकार महान क्लेश दिन होने लगे।' उद्यनेपर गुरुणोंकों ग्राजापत्व आदि लोकोंको प्राप्त अनसुधाने कहा--देलताओं ! पांतित्रताका महत्त्व
- **Translation**: 

---

### Verse 15 (Markende Puran 0.655)
- **Original**: होती हैं; परन्तु स्त्रियाँ केजल पतिकी सेना किसी प्रकार क्रम नहीं हो सकता; एसलिये में
- **Translation**: 

---

### Verse 16 (Markende Puran 0.656)
- **Original**: करनेमात्रसे पुरुधोंके दुःख सब्बकर उपार्जित किये उस साध्वोको मनाकर दिनको सृष्टि ककूँगी। मुझे
- **Translation**: 

---

### Verse 17 (Markende Puran 0.657)
- **Original**: हुए युण्यका आधा भाग प्राप्त कर लेती हैं। ऐसा उपाय करता है, जिससे फिर पहलेकी हीं
- **Translation**: 

---

### Verse 18 (Markende Puran 0.658)
- **Original**: स्त्रियोंक लिये अला यज्ञ, श्राद्ध या उपवासका भ्रौति दिन-रातकों व्यवस्था चलती रहें और उस
- **Translation**: 

---

### Verse 19 (Markende Puran 0.659)
- **Original**: धिधात नहीं है। वे पतिकी सेवामात्रसे हौ उन पतिब्रवाके पतिका भी नाश न हो।। अधीष्ट लोक्होंको प्राप्त कर लेती हैं। अत: महभागे! घुबने क्रहा--देवताओंसे वो कहकर अनसूया
- **Translation**: 

---

### Verse 20 (Markende Puran 0.660)
- **Original**: तुप्हें सद्य पतिकी सेवापें अपना मन लगाना देवी उस ब्राह्मणीके घर गर्यी और उसके कुशल
- **Translation**: 

---

