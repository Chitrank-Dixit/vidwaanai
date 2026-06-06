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

### Verse 1 (Agni Puran 0.2501)
- **Original**: किया हुआ श्राद्ध अक्षय होता है। गया, प्रयाग, गढ़ा, श्राद्धकल्पका पाठ करता है, उसे श्राद्ध करनेका
- **Translation**: 

---

### Verse 2 (Agni Puran 0.2502)
- **Original**: कुरुक्षेत्र, नर्मदा, श्रीपर्वत, -प्रभास, शालग्रामतीर्थ 'फल मिलता है
- **Translation**: 

---

### Verse 3 (Agni Puran 0.2503)
- **Original**: (गण्डकी), काशी, गोदावरी तथा श्रीपुरुषोत्तमक्षेत्र उत्तम तीर्थमें, युगादि और मन्वादि तिथिमें
- **Translation**: 

---

### Verse 4 (Agni Puran 0.2504)
- **Original**: आदि तीथ्थोंमें श्राद्ध उत्तम होता है
- **Translation**: 

---

### Verse 5 (Agni Puran 0.2505)
- **Original**: 57--62
- **Translation**: 

---

### Verse 6 (Agni Puran 0.2506)
- **Original**: इस प्रकार आदि आस्नेय्र महापुराणमें 'आाद्ध-कल्पका वर्णन” नामक एक सौं सत्रहवाँ अध्याय यूद हुआ
- **Translation**: 

---

### Verse 7 (Agni Puran 0.2507)
- **Original**: 11757 दि एक सौ अठारहवाँ अध्याय भारतवर्षका वर्णन अग्निदेव कहते हैं-- समुद्रके उत्तर और
- **Translation**: 

---

### Verse 8 (Agni Puran 0.2508)
- **Original**: भारतकी स्थिति मध्यमें है। इसमें पूर्वकी ओर हिमालयके दक्षिण जो वर्ष है, उसका नाम
- **Translation**: 

---

### Verse 9 (Agni Puran 0.2509)
- **Original**: किरात और (पश्चिममें) यवन रहते हैं। मध्यभागमें “भारत” है। उसका विस्तार नौ हजार योजन है।
- **Translation**: 

---

### Verse 10 (Agni Puran 0.2510)
- **Original**: ब्राह्मण आदि वर्णोंका निवास है। वेद-स्मृति स्वर्ग तथा अपवर्ग पानेकी इच्छावाले पुरुषोंक
- **Translation**: 

---

### Verse 11 (Agni Puran 0.2511)
- **Original**: आदि नदियाँ पारियात्र पर्वतसे निकली हैं। लिये यह कर्मभूमि है। महेन्द्र, मलय, सह,
- **Translation**: 

---

### Verse 12 (Agni Puran 0.2512)
- **Original**: विन्ध्याचलसे नर्मदा आदि प्रकट हुई हैं। सह्या पर्वतसे शुक्तिमान्‌, हिमालय, विन्ध्य और पारियात्र--ये
- **Translation**: 

---

### Verse 13 (Agni Puran 0.2513)
- **Original**: तापी, पयोष्णी, गोदावरी, भीमरथी और कृष्णवेणा सात यहाँके कुल-पर्वत हैं। इन्द्रढ्वीप, कसेरु,
- **Translation**: 

---

### Verse 14 (Agni Puran 0.2514)
- **Original**: आदि नदियोंका प्रादुर्भाव हुआ है
- **Translation**: 

---

### Verse 15 (Agni Puran 0.2515)
- **Original**: ताप्रवर्ण, ग्स्तिमान्‌, नागद्वीप, सौम्य, गान्धर्व/। _मलयसे कृतमाला आदि और महेन्द्र पर्बतसे और बारुण--ये आठ द्वीप हैं। समुद्रसे घिरा हुआ
- **Translation**: 

---

### Verse 16 (Agni Puran 0.2516)
- **Original**: त्रिसामा आदि नदियाँ निकली हैं। शुक्तिमानूसे भारत नववाँ द्वीप है
- **Translation**: 

---

### Verse 17 (Agni Puran 0.2517)
- **Original**: कुमारी आदि और हिमालयसे चन्द्रभागा आदिका भारतद्वीप उत्तरसे दक्षिणती ओर हजारों
- **Translation**: 

---

### Verse 18 (Agni Puran 0.2518)
- **Original**: प्रादुर्भाव हुआ है। भारतके पश्चिमभागमें कुरु, योजन लंबा है। भारतके उपर्युक्त नौ भाग हैं।। पाञझ्नाल और मध्यदेश आदिकी स्थिति है
- **Translation**: 

---

### Verse 19 (Agni Puran 0.2519)
- **Original**: इस प्रकार आदि आरनेय महाएयणमें “भ्ात्तवर्षका वर्णन” कामक एक साँ अठारहवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 20 (Agni Puran 0.2520)
- **Original**: #च्टन-टॉमि-भोड >> * स्तण्याधा दक्षाएण्ये मृगा: कालझो गिरी । चक्रवाका: शरद्रीपे हंसा: सरसि मातसे
- **Translation**: 

---

