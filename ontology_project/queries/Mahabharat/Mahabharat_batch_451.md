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

### Verse 1 (Mahabharat 0.4501)
- **Original**: पार्थके साथ अकेल्ला रथारूढ़ होकर युद्ध कर सके । तुम तो निरें “मूर्ख और मूढचित्त "हों।' तुम मुझे अर्जुनके
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4501)
- **Original**: पार्थके साथ अकेल्ला रथारूढ़ होकर युद्ध कर सके । तुम तो निरें “मूर्ख और मूढचित्त "हों।' तुम मुझे अर्जुनके
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4502)
- **Original**: बल-पराक्रमकी बातें क्‍या सुनाते हो? अब मैं स्वयं ही
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4502)
- **Original**: बल-पराक्रमकी बातें क्‍या सुनाते हो? अब मैं स्वयं ही
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4503)
- **Original**: संधामें उसका वर्णन करूँगा । जो पुरुष अप्रिय, निदुर, क्षुद्र, ;। आशक्षेप करनेबात्म और क्षमाशीलॉंका तिरस्कार करनेवाल्ा होता' है; उसके जैसे सैकड़ोंको भी मैं मिट्टीमें मिल्मा देता हैँ. किंतु आज केवल समयकी ओर देखकर मैं तुर्हें क्षमा कर
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4503)
- **Original**: संधामें उसका वर्णन करूँगा । जो पुरुष अप्रिय, निदुर, क्षुद्र, ;। आशक्षेप करनेबात्म और क्षमाशीलॉंका तिरस्कार करनेवाल्ा होता' है; उसके जैसे सैकड़ोंको भी मैं मिट्टीमें मिल्मा देता हैँ. किंतु आज केवल समयकी ओर देखकर मैं तुर्हें क्षमा कर
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4504)
- **Original**: रहा हैं। मेरा तो तुप्हारे साथ बड़ी सरलूताका बर्ताव है, किंतु
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4504)
- **Original**: रहा हैं। मेरा तो तुप्हारे साथ बड़ी सरलूताका बर्ताव है, किंतु
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4505)
- **Original**: हुं टेढ़ी-टेड़ी बातें करते हों। दुप' बड़े ही मि्हेही हो।
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4505)
- **Original**: हुं टेढ़ी-टेड़ी बातें करते हों। दुप' बड़े ही मि्हेही हो।
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4506)
- **Original**: पित्रता तो सात पण साथ रहनेसे हो जाती है। यह बड़ा ही
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4506)
- **Original**: पित्रता तो सात पण साथ रहनेसे हो जाती है। यह बड़ा ही
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4507)
- **Original**: कठोर समय आ गया है। राजा दुर्धोधन रणभूमिमें आ गये
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4507)
- **Original**: कठोर समय आ गया है। राजा दुर्धोधन रणभूमिमें आ गये
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4508)
- **Original**: हैं। मैं उन्हींकी विजयेछ्छासे यहाँ आया हूँ। किंतु तुम
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4508)
- **Original**: हैं। मैं उन्हींकी विजयेछ्छासे यहाँ आया हूँ। किंतु तुम
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4509)
- **Original**: अर्जुनकी ही गुणगाथा गाये जाते हो, जब कि वास्तवमें
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4509)
- **Original**: अर्जुनकी ही गुणगाथा गाये जाते हो, जब कि वास्तवमें
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4510)
- **Original**: किंतु उसने उसे लेना स्वीकार न किया। इस प्रकार जब मैं उसके प्रति आपका अटूट ग्रेमसम्ब्थ भी नहीं है। आज
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4510)
- **Original**: किंतु उसने उसे लेना स्वीकार न किया। इस प्रकार जब मैं उसके प्रति आपका अटूट ग्रेमसम्ब्थ भी नहीं है। आज
- **Translation**: 

---

