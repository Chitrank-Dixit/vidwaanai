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

### Verse 1 (Mahabharat 0.7101)
- **Original**: हुएके समान उजाड़ हो जाते हैं; उनकी झोभा, समृद्धि उनसे उत्पन्न होनेवाले पुत्र केवल अपने पिताके ही
- **Translation**: 

---

### Verse 2 (Mahabharat 0.7101)
- **Original**: हुएके समान उजाड़ हो जाते हैं; उनकी झोभा, समृद्धि उनसे उत्पन्न होनेवाले पुत्र केवल अपने पिताके ही
- **Translation**: 

---

### Verse 3 (Mahabharat 0.7102)
- **Original**: और सम्पत्तिका नाश हो जाता है। महाराज मनुने ख्नियोंको उत्तराधिकारी होते हैं। उन्हें दौहिप्रके रूपमें अपने धनका
- **Translation**: 

---

### Verse 4 (Mahabharat 0.7102)
- **Original**: और सम्पत्तिका नाश हो जाता है। महाराज मनुने ख्नियोंको उत्तराधिकारी होते हैं। उन्हें दौहिप्रके रूपमें अपने धनका
- **Translation**: 

---

### Verse 5 (Mahabharat 0.7103)
- **Original**: पुरुषोंके अधीन करके कहा था--'मनुष्यो ! ख्तियाँ अबला, अधिकारी बनाना युक्तिसंगत नहीं जान पड़ता; क्‍योंकि
- **Translation**: 

---

### Verse 6 (Mahabharat 0.7103)
- **Original**: पुरुषोंके अधीन करके कहा था--'मनुष्यो ! ख्तियाँ अबला, अधिकारी बनाना युक्तिसंगत नहीं जान पड़ता; क्‍योंकि
- **Translation**: 

---

### Verse 7 (Mahabharat 0.7104)
- **Original**: ईर्ष्यालु, मान चाहनेवाली, कुपित होनेवाल्ली, पतिका हित आसुर-बिबाहसे जिन पुत्रोंकी उत्पत्ति होती है, वे दूसरोंके दोष
- **Translation**: 

---

### Verse 8 (Mahabharat 0.7104)
- **Original**: ईर्ष्यालु, मान चाहनेवाली, कुपित होनेवाल्ली, पतिका हित आसुर-बिबाहसे जिन पुत्रोंकी उत्पत्ति होती है, वे दूसरोंके दोष
- **Translation**: 

---

### Verse 9 (Mahabharat 0.7105)
- **Original**: चाहनेवाछी और विवेकक्कक्तिसे हीन होती हैं, तथापि ये देखनेबाले, पापाचारी, पराया धन हड़पनेवाले, झठ तथा
- **Translation**: 

---

### Verse 10 (Mahabharat 0.7105)
- **Original**: चाहनेवाछी और विवेकक्कक्तिसे हीन होती हैं, तथापि ये देखनेबाले, पापाचारी, पराया धन हड़पनेवाले, झठ तथा
- **Translation**: 

---

### Verse 11 (Mahabharat 0.7106)
- **Original**: सम्मानके योग्य हैं; अतः तुमत्थेग सदा इनका सत्कार करना; श्र्मके विपरीत बर्ताव करनेवाले होते हैं। इस विषयमें प्राचीन
- **Translation**: 

---

### Verse 12 (Mahabharat 0.7106)
- **Original**: सम्मानके योग्य हैं; अतः तुमत्थेग सदा इनका सत्कार करना; श्र्मके विपरीत बर्ताव करनेवाले होते हैं। इस विषयमें प्राचीन
- **Translation**: 

---

### Verse 13 (Mahabharat 0.7107)
- **Original**: क्योंकि खत्रीजाति ही धर्मकी प्राप्तिका कारण है। तुम्हारी बातोंको जाननेवाले धर्मज्ञ पुरुष यमकी गायी हुई गाथाका
- **Translation**: 

---

### Verse 14 (Mahabharat 0.7107)
- **Original**: क्योंकि खत्रीजाति ही धर्मकी प्राप्तिका कारण है। तुम्हारी बातोंको जाननेवाले धर्मज्ञ पुरुष यमकी गायी हुई गाथाका
- **Translation**: 

---

### Verse 15 (Mahabharat 0.7108)
- **Original**: परिचर्या और नमस्कार ख्ियोंके ही अधीन हैं। संतानकी इस प्रकार वर्णन करते हैं--'जो मनुष्य अपने पुत्रको बेचकर
- **Translation**: 

---

### Verse 16 (Mahabharat 0.7108)
- **Original**: परिचर्या और नमस्कार ख्ियोंके ही अधीन हैं। संतानकी इस प्रकार वर्णन करते हैं--'जो मनुष्य अपने पुत्रको बेचकर
- **Translation**: 

---

### Verse 17 (Mahabharat 0.7109)
- **Original**: उत्पत्ति, उसका लालन-पालन और ल्लोकयात्राका प्रसन्नता- धन पाना चाहता है अथवा जीविकाके लिये शुल्क लेकर
- **Translation**: 

---

### Verse 18 (Mahabharat 0.7109)
- **Original**: उत्पत्ति, उसका लालन-पालन और ल्लोकयात्राका प्रसन्नता- धन पाना चाहता है अथवा जीविकाके लिये शुल्क लेकर
- **Translation**: 

---

### Verse 19 (Mahabharat 0.7110)
- **Original**: पूर्वक निर्वाह भी उन्हींपर निर्भर है। यदि तुमल्लोग कन्याको बेच देता है, वह अत्यत्त भयंकर कारूसूुत्रनामक
- **Translation**: 

---

### Verse 20 (Mahabharat 0.7110)
- **Original**: पूर्वक निर्वाह भी उन्हींपर निर्भर है। यदि तुमल्लोग कन्याको बेच देता है, वह अत्यत्त भयंकर कारूसूुत्रनामक
- **Translation**: 

---

