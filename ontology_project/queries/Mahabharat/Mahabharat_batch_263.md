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

### Verse 1 (Mahabharat 0.2621)
- **Original**: 'राजन्‌ ! ऐसा नियम है कि दूत अपना उद्देश्य पूर्ण होनेपर ही वु्षोध्चन अपने सज्ियोंसहिल आसनसे खड़ा हो गया।
- **Translation**: 

---

### Verse 2 (Mahabharat 0.2621)
- **Original**: 'राजन्‌ ! ऐसा नियम है कि दूत अपना उद्देश्य पूर्ण होनेपर ही वु्षोध्चन अपने सज्ियोंसहिल आसनसे खड़ा हो गया।
- **Translation**: 

---

### Verse 3 (Mahabharat 0.2622)
- **Original**: भोजनादि प्रहण करते हैं। अतः जब मेरा काम पूरा हो जाय, भगवान्‌ दुर्योधन और उसके मन्जियोंसे मिलकर फिर जहाँ
- **Translation**: 

---

### Verse 4 (Mahabharat 0.2622)
- **Original**: भोजनादि प्रहण करते हैं। अतः जब मेरा काम पूरा हो जाय, भगवान्‌ दुर्योधन और उसके मन्जियोंसे मिलकर फिर जहाँ
- **Translation**: 

---

### Verse 5 (Mahabharat 0.2623)
- **Original**: तब तुम भी मेरा और मेरे मन्त्रियोंका सत्कार करना। मैं 'एकश्रित हुए सब राजाओंसे अनुप्तार मिले।
- **Translation**: 

---

### Verse 6 (Mahabharat 0.2623)
- **Original**: तब तुम भी मेरा और मेरे मन्त्रियोंका सत्कार करना। मैं 'एकश्रित हुए सब राजाओंसे अनुप्तार मिले।
- **Translation**: 

---

### Verse 7 (Mahabharat 0.2624)
- **Original**: काम, क्रोध, द्वेष, स्वार्थ, कपट अथवा स्थेभमें पड़कर कि आम प्ग
- **Translation**: 

---

### Verse 8 (Mahabharat 0.2624)
- **Original**: काम, क्रोध, द्वेष, स्वार्थ, कपट अथवा स्थेभमें पड़कर कि आम प्ग
- **Translation**: 

---

### Verse 9 (Mahabharat 0.2625)
- **Original**: ! काका 550
- **Translation**: 

---

### Verse 10 (Mahabharat 0.2625)
- **Original**: ! काका 550
- **Translation**: 

---

### Verse 11 (Mahabharat 0.2626)
- **Original**: धर्मको किसी प्रकार नहीं छोड़ सकता । भोजन या तो प्रेमवश किया जाता है या आपत्तिमें पढ़कर किया जाता है। सो का
- **Translation**: 

---

### Verse 12 (Mahabharat 0.2626)
- **Original**: धर्मको किसी प्रकार नहीं छोड़ सकता । भोजन या तो प्रेमवश किया जाता है या आपत्तिमें पढ़कर किया जाता है। सो का
- **Translation**: 

---

### Verse 13 (Mahabharat 0.2627)
- **Original**: तुम्हारा तो मेरे प्रति प्रेम नहीं है और मैं किसी आपत्तिमें ग्रस्त
- **Translation**: 

---

### Verse 14 (Mahabharat 0.2627)
- **Original**: तुम्हारा तो मेरे प्रति प्रेम नहीं है और मैं किसी आपत्तिमें ग्रस्त
- **Translation**: 

---

### Verse 15 (Mahabharat 0.2628)
- **Original**: नहीं हूँ। देखो, पाण्डव तो तुप्हारे भाई ही हैं; वे सदा अपने रे स्रेहियोंके अनुकूल रहते हैं और उनमें सभी सद्गुण विद्यमान हैं। फिर भी तुम बिना कारण जन्पसे ही उनसे द्वेष करते हो ।
- **Translation**: 

---

### Verse 16 (Mahabharat 0.2628)
- **Original**: नहीं हूँ। देखो, पाण्डव तो तुप्हारे भाई ही हैं; वे सदा अपने रे स्रेहियोंके अनुकूल रहते हैं और उनमें सभी सद्गुण विद्यमान हैं। फिर भी तुम बिना कारण जन्पसे ही उनसे द्वेष करते हो ।
- **Translation**: 

---

### Verse 17 (Mahabharat 0.2629)
- **Original**: उनके साथ द्वेष करना ठीक नहीं है। वे तो सर्वदा अपने धर्ममें स्थित रहते हैं। उनसे जो द्वेष करता है, वह तो मुझसे भी द्वेष च्इं करता है और जो उनके अनुकूल है, वह मेरे भी अनुकूल हैं। (/
- **Translation**: 

---

### Verse 18 (Mahabharat 0.2629)
- **Original**: उनके साथ द्वेष करना ठीक नहीं है। वे तो सर्वदा अपने धर्ममें स्थित रहते हैं। उनसे जो द्वेष करता है, वह तो मुझसे भी द्वेष च्इं करता है और जो उनके अनुकूल है, वह मेरे भी अनुकूल हैं। (/
- **Translation**: 

---

### Verse 19 (Mahabharat 0.2630)
- **Original**: धर्मात्पा पाण्डवोंके साथ तो तुम मुझे एकरूप हुआ हीं ज्थ्र ज्क #2“4 24
- **Translation**: 

---

### Verse 20 (Mahabharat 0.2630)
- **Original**: धर्मात्पा पाण्डवोंके साथ तो तुम मुझे एकरूप हुआ हीं ज्थ्र ज्क #2“4 24
- **Translation**: 

---

