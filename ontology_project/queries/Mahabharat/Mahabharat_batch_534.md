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

### Verse 1 (Mahabharat 0.5331)
- **Original**: राजन्‌ ! इन्हींको सेनाध्यक्ष बनाकर हम झन्नुओंपर विजय पा उस महातपस्वीने कठोर ब्रतोंका पालन करके बड़े यत्रसे
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5331)
- **Original**: राजन्‌ ! इन्हींको सेनाध्यक्ष बनाकर हम झन्नुओंपर विजय पा उस महातपस्वीने कठोर ब्रतोंका पालन करके बड़े यत्रसे
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5332)
- **Original**: सकते हैं। झंकरजीकी आराध्नाकी थी। उसके पराक्रम और रूपकी
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5332)
- **Original**: सकते हैं। झंकरजीकी आराध्नाकी थी। उसके पराक्रम और रूपकी
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5333)
- **Original**: ड्रोेणकुमारके ऐसा कहनेपर सभी योद्धा राजा झल्यको कहीं भी तुलना नहीं थी। वह सम्पूर्ण विद्याओंका पारगामी,
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5333)
- **Original**: ड्रोेणकुमारके ऐसा कहनेपर सभी योद्धा राजा झल्यको कहीं भी तुलना नहीं थी। वह सम्पूर्ण विद्याओंका पारगामी,
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5334)
- **Original**: घेस्कर खड़े हो गये और उनकी जय-जयकार करने लगे। गुणोंका समुद्र तथा सबकी प्रश्ंसाका पात्र था।
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5334)
- **Original**: घेस्कर खड़े हो गये और उनकी जय-जयकार करने लगे। गुणोंका समुद्र तथा सबकी प्रश्ंसाका पात्र था।
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5335)
- **Original**: अब उन्होंने बड़े आवेशमें भरकर युद्धका निश्चय किया। उसके पास पहुँचकर दु्योधनने कहा--आप हमारे
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5335)
- **Original**: अब उन्होंने बड़े आवेशमें भरकर युद्धका निश्चय किया। उसके पास पहुँचकर दु्योधनने कहा--आप हमारे
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5336)
- **Original**: राजा झल्य ड्रोण तथा भीष्यके समान पराक्रमी थे, वे एक शुरूके पुत्र हैं, हम सब ल्तेगोंकों आपका ही भरोसा है;
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5336)
- **Original**: राजा झल्य ड्रोण तथा भीष्यके समान पराक्रमी थे, वे एक शुरूके पुत्र हैं, हम सब ल्तेगोंकों आपका ही भरोसा है;
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5337)
- **Original**: उत्तम रथपर बैठे हुए थे। दुर्ोधन रथसे उतरकर उनके सामने
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5337)
- **Original**: उत्तम रथपर बैठे हुए थे। दुर्ोधन रथसे उतरकर उनके सामने
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5338)
- **Original**: 96 संक्षिप्त महाभारत ( शल्यपर्व भूमिपर खड़ा हो गया और हाथ जोड़कर जोला--
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5338)
- **Original**: 96 संक्षिप्त महाभारत ( शल्यपर्व भूमिपर खड़ा हो गया और हाथ जोड़कर जोला--
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5339)
- **Original**: जय हो, तुम चिस्जीवी रहो और सामने आये हुए समस्त मित्रवत्सल ! आप झूस्वीर हैं, इसलिये हमारी सेनाके
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5339)
- **Original**: जय हो, तुम चिस्जीवी रहो और सामने आये हुए समस्त मित्रवत्सल ! आप झूस्वीर हैं, इसलिये हमारी सेनाके
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5340)
- **Original**: अध्यक्ष बनिये।' । एजा शल्यनें कहा--कुरुतण! यदि तुम मुझे
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5340)
- **Original**: अध्यक्ष बनिये।' । एजा शल्यनें कहा--कुरुतण! यदि तुम मुझे
- **Translation**: 

---

