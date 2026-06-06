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

### Verse 1 (Mahabharat 941.7671)
- **Original**: तेजस्वी हैं। बड़े-बड़े यज्ञोमें विध्रोड्धारा ऋग्वेदकी सहस्नों सृष्टिकी परम्परा प्रचलित हुई है तथा इन्होंने ही इस प्राचीन
- **Translation**: 

---

### Verse 2 (Mahabharat 941.7671)
- **Original**: तेजस्वी हैं। बड़े-बड़े यज्ञोमें विध्रोड्धारा ऋग्वेदकी सहस्नों सृष्टिकी परम्परा प्रचलित हुई है तथा इन्होंने ही इस प्राचीन
- **Translation**: 

---

### Verse 3 (Mahabharat 941.7672)
- **Original**: पुततन ऋचाओंसे एकमात्र इन्हींकी स्तुति की जाती है। इन विश्वका निर्माण किया है। सृष्टिके आरम्भमें इनकी नाभिसे
- **Translation**: 

---

### Verse 4 (Mahabharat 941.7672)
- **Original**: पुततन ऋचाओंसे एकमात्र इन्हींकी स्तुति की जाती है। इन विश्वका निर्माण किया है। सृष्टिके आरम्भमें इनकी नाभिसे
- **Translation**: 

---

### Verse 5 (Mahabharat 941.7673)
- **Original**: श्रीकृष्णके सिवा दूसरा कोई ऐसा नहीं है, जो महातेजस्वी कमल उत्पन्न हुआ और उसीके भीतर अमित तेजस्वी ब्रह्माजी
- **Translation**: 

---

### Verse 6 (Mahabharat 941.7673)
- **Original**: श्रीकृष्णके सिवा दूसरा कोई ऐसा नहीं है, जो महातेजस्वी कमल उत्पन्न हुआ और उसीके भीतर अमित तेजस्वी ब्रह्माजी
- **Translation**: 

---

### Verse 7 (Mahabharat 941.7674)
- **Original**: दुर्वासाकों अपने घरमें ठहर सके। इनको हो अद्वितीय स्वतः प्रकट हुए। इन्होंने ही आ्राचीन कालमें दैल्योंका संहार
- **Translation**: 

---

### Verse 8 (Mahabharat 941.7674)
- **Original**: दुर्वासाकों अपने घरमें ठहर सके। इनको हो अद्वितीय स्वतः प्रकट हुए। इन्होंने ही आ्राचीन कालमें दैल्योंका संहार
- **Translation**: 

---

### Verse 9 (Mahabharat 941.7675)
- **Original**: पुततन ऋषि कहते हैं। ये बिश्वके रणयिता हैं और अपने किया और ये ही दैत्य-सप्राद्‌ बलिके रूपमें प्रकट हुए। समस्त
- **Translation**: 

---

### Verse 10 (Mahabharat 941.7675)
- **Original**: पुततन ऋषि कहते हैं। ये बिश्वके रणयिता हैं और अपने किया और ये ही दैत्य-सप्राद्‌ बलिके रूपमें प्रकट हुए। समस्त
- **Translation**: 

---

### Verse 11 (Mahabharat 941.7676)
- **Original**: स्वरूपसे ही अनेकों पदार्थोको उत्पन्न करते रहते हैं। ये प्राणियोंकी उत्पत्ति इन्हींसे हुई है। भूत और भविष्य इनका ही
- **Translation**: 

---

### Verse 12 (Mahabharat 941.7676)
- **Original**: स्वरूपसे ही अनेकों पदार्थोको उत्पन्न करते रहते हैं। ये प्राणियोंकी उत्पत्ति इन्हींसे हुई है। भूत और भविष्य इनका ही
- **Translation**: 

---

### Verse 13 (Mahabharat 941.7677)
- **Original**: देवताओंके देवता होकर भी वेदोंका अध्ययन और ग्रालीन स्वरूप है और ये ही सम्पूर्ण जगतकी रक्षा करते हैं। जब
- **Translation**: 

---

### Verse 14 (Mahabharat 941.7677)
- **Original**: देवताओंके देवता होकर भी वेदोंका अध्ययन और ग्रालीन स्वरूप है और ये ही सम्पूर्ण जगतकी रक्षा करते हैं। जब
- **Translation**: 

---

### Verse 15 (Mahabharat 941.7678)
- **Original**: विधियोंका पालन करते हैं। लोकिक और वैदिक कर्मका जो धर्मका हवास होने लूगता है, उस समय ये श्रीकृष्ण देवताओं
- **Translation**: 

---

### Verse 16 (Mahabharat 941.7678)
- **Original**: विधियोंका पालन करते हैं। लोकिक और वैदिक कर्मका जो धर्मका हवास होने लूगता है, उस समय ये श्रीकृष्ण देवताओं
- **Translation**: 

---

### Verse 17 (Mahabharat 941.7679)
- **Original**: फल है, वह सब श्रीकृष्ण ही हैं। ये ही सम्पूर्ण ल्लकोंकी शुद् तथा मनुष्योंके बंझमें अवतार लेकर स्वयं धर्मका आचरण
- **Translation**: 

---

### Verse 18 (Mahabharat 941.7679)
- **Original**: फल है, वह सब श्रीकृष्ण ही हैं। ये ही सम्पूर्ण ल्लकोंकी शुद् तथा मनुष्योंके बंझमें अवतार लेकर स्वयं धर्मका आचरण
- **Translation**: 

---

### Verse 19 (Mahabharat 941.7680)
- **Original**: ज्योति हैं तथा तीनों ल्लेक, तीनों लोकपाल, प्रिविघ अप्रि, करते हुए उसकी स्थापना और पर-अपर--सब लोकोंकी
- **Translation**: 

---

### Verse 20 (Mahabharat 941.7680)
- **Original**: ज्योति हैं तथा तीनों ल्लेक, तीनों लोकपाल, प्रिविघ अप्रि, करते हुए उसकी स्थापना और पर-अपर--सब लोकोंकी
- **Translation**: 

---

