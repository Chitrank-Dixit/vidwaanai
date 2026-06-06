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

### Verse 1 (Mahabharat 0.3401)
- **Original**: राजाओंने द्रोणाबार्यका जय-जयकार किया। वें सब श्रेष्ठ हैं। इसलिये जिस प्रकार देवताओंने स्वाभिकार्तिकजीको
- **Translation**: 

---

### Verse 2 (Mahabharat 0.3401)
- **Original**: राजाओंने द्रोणाबार्यका जय-जयकार किया। वें सब श्रेष्ठ हैं। इसलिये जिस प्रकार देवताओंने स्वाभिकार्तिकजीको
- **Translation**: 

---

### Verse 3 (Mahabharat 0.3402)
- **Original**: ड्रोणाचार्यका उत्साह बढ़ाने छगे। तब आचार्यने दुर्योधनसे अपना सेनाध्यक्ष बनाया था, उसी प्रकार आप इन्हें अपना
- **Translation**: 

---

### Verse 4 (Mahabharat 0.3402)
- **Original**: ड्रोणाचार्यका उत्साह बढ़ाने छगे। तब आचार्यने दुर्योधनसे अपना सेनाध्यक्ष बनाया था, उसी प्रकार आप इन्हें अपना
- **Translation**: 

---

### Verse 5 (Mahabharat 0.3403)
- **Original**: कहा, 'राजन्‌ ! मैं छहों अड्डयुक्त बेद, मनुजीका कहा हुआ सेनापति बनाइये। अर्थशासत्र, भगवान्‌ झंकरकी दी हुई बाणविद्या और कई कर्णकी यह बात सुनकर दु्योधनने सेनाके बीचमें खड़े
- **Translation**: 

---

### Verse 6 (Mahabharat 0.3403)
- **Original**: कहा, 'राजन्‌ ! मैं छहों अड्डयुक्त बेद, मनुजीका कहा हुआ सेनापति बनाइये। अर्थशासत्र, भगवान्‌ झंकरकी दी हुई बाणविद्या और कई कर्णकी यह बात सुनकर दु्योधनने सेनाके बीचमें खड़े
- **Translation**: 

---

### Verse 7 (Mahabharat 0.3404)
- **Original**: प्रकास्के अख-झख जानता हूँ। तुमने विजयकी अभिलापासे हुए आचार्य द्रेणके पास जाकर कहा, 'भगवन्‌ ! वर्ण, कुछ,
- **Translation**: 

---

### Verse 8 (Mahabharat 0.3404)
- **Original**: प्रकास्के अख-झख जानता हूँ। तुमने विजयकी अभिलापासे हुए आचार्य द्रेणके पास जाकर कहा, 'भगवन्‌ ! वर्ण, कुछ,
- **Translation**: 

---

### Verse 9 (Mahabharat 0.3405)
- **Original**: मुझमें .जो-जो गुण बताये हैं, उन सभीको निभाता हुआ मैं का पाण्डवॉके साथ संग्राम करूँगा। किंतु मैं द्रुपदपुत्र धृष्टझुज्न का किये 2 बध किसी प्रकार नहीं कर सकूँगा; क्योंकि उप्तको उत्पत्ति तो ह ड्।
- **Translation**: 

---

### Verse 10 (Mahabharat 0.3405)
- **Original**: मुझमें .जो-जो गुण बताये हैं, उन सभीको निभाता हुआ मैं का पाण्डवॉके साथ संग्राम करूँगा। किंतु मैं द्रुपदपुत्र धृष्टझुज्न का किये 2 बध किसी प्रकार नहीं कर सकूँगा; क्योंकि उप्तको उत्पत्ति तो ह ड्।
- **Translation**: 

---

### Verse 11 (Mahabharat 0.3406)
- **Original**: ) हि मेरे ही बधके लिये हुई है।' गुणोंमें आप सबसे बढ़े-चढ़े हैं। आपके समान राजाओमें भी (977,-//
- **Translation**: 

---

### Verse 12 (Mahabharat 0.3406)
- **Original**: ) हि मेरे ही बधके लिये हुई है।' गुणोंमें आप सबसे बढ़े-चढ़े हैं। आपके समान राजाओमें भी (977,-//
- **Translation**: 

---

### Verse 13 (Mahabharat 0.3407)
- **Original**: 8: बडे मय) 517 हमारा कोई रक्षक नहीं है। अतः कुद्र जिस प्रकार
- **Translation**: 

---

### Verse 14 (Mahabharat 0.3407)
- **Original**: 8: बडे मय) 517 हमारा कोई रक्षक नहीं है। अतः कुद्र जिस प्रकार
- **Translation**: 

---

### Verse 15 (Mahabharat 0.3408)
- **Original**: राजन्‌ ! इस प्रकार आचार्यकी अनुमति मिलनेपर आपके देवताओंकी रक्षा करते हैं; उसी प्रकार आप हमारी रक्षा
- **Translation**: 

---

### Verse 16 (Mahabharat 0.3408)
- **Original**: राजन्‌ ! इस प्रकार आचार्यकी अनुमति मिलनेपर आपके देवताओंकी रक्षा करते हैं; उसी प्रकार आप हमारी रक्षा
- **Translation**: 

---

### Verse 17 (Mahabharat 0.3409)
- **Original**: पुत्र दुर्षोधनने उन्हें विधिपूर्वक सेनापतिके पदपर अभिषिक्त कीजिये। हम आपके नेतृत्वमें ही झन्नुओपर विजय करना
- **Translation**: 

---

### Verse 18 (Mahabharat 0.3409)
- **Original**: पुत्र दुर्षोधनने उन्हें विधिपूर्वक सेनापतिके पदपर अभिषिक्त कीजिये। हम आपके नेतृत्वमें ही झन्नुओपर विजय करना
- **Translation**: 

---

### Verse 19 (Mahabharat 0.3410)
- **Original**: किया। उस समय बाजोंके घोष और शद्भोंकी ध्वनिसे सब चाहते हैं। अतः आप हमारे सेनापति बननेकी कृपा करें । यदि
- **Translation**: 

---

### Verse 20 (Mahabharat 0.3410)
- **Original**: किया। उस समय बाजोंके घोष और शद्भोंकी ध्वनिसे सब चाहते हैं। अतः आप हमारे सेनापति बननेकी कृपा करें । यदि
- **Translation**: 

---

