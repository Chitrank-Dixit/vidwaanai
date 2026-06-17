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

### Verse 1 (Mahabharat 0.551)
- **Original**: मन्दपालने और उन पक्षियोंमें सबसे बड़े जरितारिने अभ्नि- पूजनीय हैं। तुम देवताओंको लेकर यहाँसे चले जाओ, इसीमें
- **Translation**: 

---

### Verse 2 (Mahabharat 0.551)
- **Original**: मन्दपालने और उन पक्षियोंमें सबसे बड़े जरितारिने अभ्नि- पूजनीय हैं। तुम देवताओंको लेकर यहाँसे चले जाओ, इसीमें
- **Translation**: 

---

### Verse 3 (Mahabharat 0.552)
- **Original**: देवताकी स्तुति करके अपनी रक्षाका वचन ले लिया था। तुल्हारी झोभा है। इस अवसरपर खाण्डब वनका दाह दैवने
- **Translation**: 

---

### Verse 4 (Mahabharat 0.552)
- **Original**: देवताकी स्तुति करके अपनी रक्षाका वचन ले लिया था। तुल्हारी झोभा है। इस अवसरपर खाण्डब वनका दाह दैवने
- **Translation**: 

---

### Verse 5 (Mahabharat 0.553)
- **Original**: . अभ्निदेवने भगवान्‌ श्रीकृष्ण और अर्जुनकी सहायतासे ही रच रखा है।' आकाशवाणी सुनकर देवराज इद्र क्रोध
- **Translation**: 

---

### Verse 6 (Mahabharat 0.553)
- **Original**: . अभ्निदेवने भगवान्‌ श्रीकृष्ण और अर्जुनकी सहायतासे ही रच रखा है।' आकाशवाणी सुनकर देवराज इद्र क्रोध
- **Translation**: 

---

### Verse 7 (Mahabharat 0.554)
- **Original**: प्रज्वलित होकर खाण्डव वनकोो जला डाला। अनन्तर और ईं््या छोड़कर स्वर्गमें लौट गये, देवलाओंने भी अपनी
- **Translation**: 

---

### Verse 8 (Mahabharat 0.554)
- **Original**: प्रज्वलित होकर खाण्डव वनकोो जला डाला। अनन्तर और ईं््या छोड़कर स्वर्गमें लौट गये, देवलाओंने भी अपनी
- **Translation**: 

---

### Verse 9 (Mahabharat 0.555)
- **Original**: ब्राह्मणके रूपमें उनके सामने प्रकट हुए। उसी समय देवराज सेनाके साथ उनका अनुगमन किया। देवताओंको समर-
- **Translation**: 

---

### Verse 10 (Mahabharat 0.555)
- **Original**: ब्राह्मणके रूपमें उनके सामने प्रकट हुए। उसी समय देवराज सेनाके साथ उनका अनुगमन किया। देवताओंको समर-
- **Translation**: 

---

### Verse 11 (Mahabharat 0.556)
- **Original**: इन्र भी देवताओंके साथ अन्तरिक्षसे वहाँ उतरे। उन्होंने भूमिसे हटते देखकर भगवान्‌ श्रीकृष्ण और अर्जुनने इर्ष-
- **Translation**: 

---

### Verse 12 (Mahabharat 0.556)
- **Original**: इन्र भी देवताओंके साथ अन्तरिक्षसे वहाँ उतरे। उन्होंने भूमिसे हटते देखकर भगवान्‌ श्रीकृष्ण और अर्जुनने इर्ष-
- **Translation**: 

---

### Verse 13 (Mahabharat 0.557)
- **Original**: श्रीकृष्ण और अर्जुनसे कहा, 'आपलोगोंने यह ऐसा दुष्कर ध्वनि की। खाण्डव वन अनाथके घरकी तरह धक-धक
- **Translation**: 

---

### Verse 14 (Mahabharat 0.557)
- **Original**: श्रीकृष्ण और अर्जुनसे कहा, 'आपलोगोंने यह ऐसा दुष्कर ध्वनि की। खाण्डव वन अनाथके घरकी तरह धक-धक
- **Translation**: 

---

### Verse 15 (Mahabharat 0.558)
- **Original**: कार्य किया है; जो देवताओंके लिये भी असाध्य है।ः मैं जलने लगा। आपलोगॉपर प्रसन्न हूँ। इसलिये आप मनुष्योंके लिये भगवान्‌ ्रीकृष्णने देखा कि मय दानव यकायक
- **Translation**: 

---

### Verse 16 (Mahabharat 0.558)
- **Original**: कार्य किया है; जो देवताओंके लिये भी असाध्य है।ः मैं जलने लगा। आपलोगॉपर प्रसन्न हूँ। इसलिये आप मनुष्योंके लिये भगवान्‌ ्रीकृष्णने देखा कि मय दानव यकायक
- **Translation**: 

---

### Verse 17 (Mahabharat 0.559)
- **Original**: दुल्लंध-से-दुर्लेभ वस्तु भी मुझसे माँग सकते हैं।' अजुनने तक्षकके निवास-स्थानसे निकलकर भागा जा रहा है और
- **Translation**: 

---

### Verse 18 (Mahabharat 0.559)
- **Original**: दुल्लंध-से-दुर्लेभ वस्तु भी मुझसे माँग सकते हैं।' अजुनने तक्षकके निवास-स्थानसे निकलकर भागा जा रहा है और
- **Translation**: 

---

### Verse 19 (Mahabharat 0.560)
- **Original**: कहा, 'मुझे आप सब प्रकारके अब दे दीजिये।' इन्द्रने कहा, अप्नि मूर्तिमान्‌ होकर जलानेके लिये उसका पीछा कर रहा अर्जुन
- **Translation**: 

---

### Verse 20 (Mahabharat 0.560)
- **Original**: कहा, 'मुझे आप सब प्रकारके अब दे दीजिये।' इन्द्रने कहा, अप्नि मूर्तिमान्‌ होकर जलानेके लिये उसका पीछा कर रहा अर्जुन
- **Translation**: 

---

