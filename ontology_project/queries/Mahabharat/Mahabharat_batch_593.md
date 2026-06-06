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

### Verse 1 (Mahabharat 0.5921)
- **Original**: करनेवाले वाक्योंक भी मैंने युक्तिपूर्कक विद्यार किया है और पृथ्वीका पालन कीजिये और राजमहल, शय्या, सवारी, वस्त्र . उन वाज्योका जो तात्पर्य है, उसे भी मैं विधिवत्‌ जानता है। तथा आभूषणोंको उपयोगमें लाइये
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5921)
- **Original**: करनेवाले वाक्योंक भी मैंने युक्तिपूर्कक विद्यार किया है और पृथ्वीका पालन कीजिये और राजमहल, शय्या, सवारी, वस्त्र . उन वाज्योका जो तात्पर्य है, उसे भी मैं विधिवत्‌ जानता है। तथा आभूषणोंको उपयोगमें लाइये
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5922)
- **Original**: जो बराबर दूसरोंसे दान
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5922)
- **Original**: जो बराबर दूसरोंसे दान
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5923)
- **Original**: तुम तो केवल झख्नविद्याके ही जानकार हो और वीरोंका शर्म छेता है तथा जो निरन्तर स्वयं ही दान करता रहता है, उन
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5923)
- **Original**: तुम तो केवल झख्नविद्याके ही जानकार हो और वीरोंका शर्म छेता है तथा जो निरन्तर स्वयं ही दान करता रहता है, उन
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5924)
- **Original**: पालन करते हो। झाख्तरके यथार्थ मर्मको तुम किसी प्रकार दोनोंपें क्या अन्तर है ? उनमें कौन-सा श्रेष्ठ है ? इसे आप
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5924)
- **Original**: पालन करते हो। झाख्तरके यथार्थ मर्मको तुम किसी प्रकार दोनोंपें क्या अन्तर है ? उनमें कौन-सा श्रेष्ठ है ? इसे आप
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5925)
- **Original**: नहीं समझ सकते। जो लोग झाखके सूक्ष्म रहस्यको जानते समझ्िये। संसारमें साथु-संतोंको अन्न देनेवाले राजाकी
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5925)
- **Original**: नहीं समझ सकते। जो लोग झाखके सूक्ष्म रहस्यको जानते समझ्िये। संसारमें साथु-संतोंको अन्न देनेवाले राजाकी
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5926)
- **Original**: हैं और धर्मका निश्चय करनलेमें कुशल हैं, तुम्हारी तरह तो वे आवश्यकता है; यदि दान करनेवाला राजा न रहे तो मोक्ष
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5926)
- **Original**: हैं और धर्मका निश्चय करनलेमें कुशल हैं, तुम्हारी तरह तो वे आवश्यकता है; यदि दान करनेवाला राजा न रहे तो मोक्ष
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5927)
- **Original**: भी मुझे उपदेझ नहीं दे सकते । तथापि प्रातृस्नेहवश तुमने जो चाहनेबाले महात्माऑका जीवन-निर्वाह कैसे हो ? अन्नसे ही
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5927)
- **Original**: भी मुझे उपदेझ नहीं दे सकते । तथापि प्रातृस्नेहवश तुमने जो चाहनेबाले महात्माऑका जीवन-निर्वाह कैसे हो ? अन्नसे ही
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5928)
- **Original**: कुछ कहा है, वह न्यायसंगत और उचित ही है, उससे मुझे भी श्राणकी पुष्टि होती है, इसल्लिये अन्न देनेबास्प्र प्राणदाता होता
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5928)
- **Original**: कुछ कहा है, वह न्यायसंगत और उचित ही है, उससे मुझे भी श्राणकी पुष्टि होती है, इसल्लिये अन्न देनेबास्प्र प्राणदाता होता
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5929)
- **Original**: तुम्हारे प्रति प्रसन्नता ही हुई है। युद्धेके धर्मों: और है। गृहस्थ-आश्रमसे अछग होकर भी त्यागी लोग गृहस्थोंके
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5929)
- **Original**: तुम्हारे प्रति प्रसन्नता ही हुई है। युद्धेके धर्मों: और है। गृहस्थ-आश्रमसे अछग होकर भी त्यागी लोग गृहस्थोंके
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5930)
- **Original**: संग्राम करनेकी कुझलतामें तो तुम्हारे समान तीनों ल्ोकॉमें ही सहारे जीवन धारण करते हैं। जो आसक्तिरहित एवं सब
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5930)
- **Original**: संग्राम करनेकी कुझलतामें तो तुम्हारे समान तीनों ल्ोकॉमें ही सहारे जीवन धारण करते हैं। जो आसक्तिरहित एवं सब
- **Translation**: 

---

