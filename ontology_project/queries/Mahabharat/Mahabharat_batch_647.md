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

### Verse 1 (Mahabharat 0.6461)
- **Original**: बहुत बड़ी सम्पत्ति पाकर हर्षसे फूल नहीं उठता और संकट प्रशंसा करते हैं। जिसने दमका पालन नहीं किया है, उसे
- **Translation**: 

---

### Verse 2 (Mahabharat 0.6461)
- **Original**: बहुत बड़ी सम्पत्ति पाकर हर्षसे फूल नहीं उठता और संकट प्रशंसा करते हैं। जिसने दमका पालन नहीं किया है, उसे
- **Translation**: 

---

### Verse 3 (Mahabharat 0.6462)
- **Original**: पड़नेपर जिसे झोकके कारण घबराहट नहीं होती; वह द्विज अपने कर्मोंमें पूर्ण सफलता नहीं मिलती; क्योंकि क्रिया, तप
- **Translation**: 

---

### Verse 4 (Mahabharat 0.6462)
- **Original**: पड़नेपर जिसे झोकके कारण घबराहट नहीं होती; वह द्विज अपने कर्मोंमें पूर्ण सफलता नहीं मिलती; क्योंकि क्रिया, तप
- **Translation**: 

---

### Verse 5 (Mahabharat 0.6463)
- **Original**: स्थिरबुद्धिबाला तथा जितेन्द्रिय कहलाता है। जो झाखका और सत्य--इन सबका आधार “दम' ही है। दमसे तेजकी
- **Translation**: 

---

### Verse 6 (Mahabharat 0.6463)
- **Original**: स्थिरबुद्धिबाला तथा जितेन्द्रिय कहलाता है। जो झाखका और सत्य--इन सबका आधार “दम' ही है। दमसे तेजकी
- **Translation**: 

---

### Verse 7 (Mahabharat 0.6464)
- **Original**: ज्ञाता, वैदिक कमोंका अनुष्ठान करनेवाला, सदाचारी और वृद्धि होती है। दम परम पवित्र बताया गया है। दमनझील
- **Translation**: 

---

### Verse 8 (Mahabharat 0.6464)
- **Original**: ज्ञाता, वैदिक कमोंका अनुष्ठान करनेवाला, सदाचारी और वृद्धि होती है। दम परम पवित्र बताया गया है। दमनझील
- **Translation**: 

---

### Verse 9 (Mahabharat 0.6465)
- **Original**: पवित्र है तथा सर्वदा दपका पालन करता रहता है, उसे महान्‌ पुरुष पाप तथा भयसे रहित होकर “महत्‌' पदको प्राप्त होता
- **Translation**: 

---

### Verse 10 (Mahabharat 0.6465)
- **Original**: पवित्र है तथा सर्वदा दपका पालन करता रहता है, उसे महान्‌ पुरुष पाप तथा भयसे रहित होकर “महत्‌' पदको प्राप्त होता
- **Translation**: 

---

### Verse 11 (Mahabharat 0.6466)
- **Original**: फलकी प्राप्त होती है। जिनका अच्तःकरण दूपित है, वे लोग है
- **Translation**: 

---

### Verse 12 (Mahabharat 0.6466)
- **Original**: फलकी प्राप्त होती है। जिनका अच्तःकरण दूपित है, वे लोग है
- **Translation**: 

---

### Verse 13 (Mahabharat 0.6467)
- **Original**: 'दम' का पालन करनेवाल्ा मनुष्य सुखसे सोता, सुखसे
- **Translation**: 

---

### Verse 14 (Mahabharat 0.6467)
- **Original**: 'दम' का पालन करनेवाल्ा मनुष्य सुखसे सोता, सुखसे
- **Translation**: 

---

### Verse 15 (Mahabharat 0.6468)
- **Original**: दोषदृष्टिका अभाव; क्षमा; शान्ति, संतोष, मीठे बच्चन जागता तथा सुखसे संसारमें विचररता है और उसका मन भी
- **Translation**: 

---

### Verse 16 (Mahabharat 0.6468)
- **Original**: दोषदृष्टिका अभाव; क्षमा; शान्ति, संतोष, मीठे बच्चन जागता तथा सुखसे संसारमें विचररता है और उसका मन भी
- **Translation**: 

---

### Verse 17 (Mahabharat 0.6469)
- **Original**: बोलना, सत्यभाषण, दान तथा उद्योगझीलता आदि गुणोंको असन्न रहता है। दमसे ही तेजको धारण किया जाता है,
- **Translation**: 

---

### Verse 18 (Mahabharat 0.6469)
- **Original**: बोलना, सत्यभाषण, दान तथा उद्योगझीलता आदि गुणोंको असन्न रहता है। दमसे ही तेजको धारण किया जाता है,
- **Translation**: 

---

### Verse 19 (Mahabharat 0.6470)
- **Original**: नहीं अपनाते। उनमें तो काम, क्रोध, लोभ, ईर्ष्या तथा डींग दमनझीलः पुरुष ही सजोगुणपर”विजय पाताः है तथा वही
- **Translation**: 

---

### Verse 20 (Mahabharat 0.6470)
- **Original**: नहीं अपनाते। उनमें तो काम, क्रोध, लोभ, ईर्ष्या तथा डींग दमनझीलः पुरुष ही सजोगुणपर”विजय पाताः है तथा वही
- **Translation**: 

---

