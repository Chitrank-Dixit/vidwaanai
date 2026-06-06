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

### Verse 1 (Mahabharat 0.691)
- **Original**: पालन करने लगे। वे नियमसे पितरोंका तर्पण और देशकी बड़ी उच्नति की है। यह बड़े सौभाग्यकी बात है कि
- **Translation**: 

---

### Verse 2 (Mahabharat 0.691)
- **Original**: पालन करने लगे। वे नियमसे पितरोंका तर्पण और देशकी बड़ी उच्नति की है। यह बड़े सौभाग्यकी बात है कि
- **Translation**: 

---

### Verse 3 (Mahabharat 0.692)
- **Original**: देवताओंकी पूजा करते । इस प्रकार सबके चले जानेपर-भी कुष्हारे-जैसे सत्फुप्रसे कुर्बं्की कीर्ति बढ़ गयी। इस यज्ञमें
- **Translation**: 

---

### Verse 4 (Mahabharat 0.692)
- **Original**: देवताओंकी पूजा करते । इस प्रकार सबके चले जानेपर-भी कुष्हारे-जैसे सत्फुप्रसे कुर्बं्की कीर्ति बढ़ गयी। इस यज्ञमें
- **Translation**: 

---

### Verse 5 (Mahabharat 0.693)
- **Original**: केवल दुर्थोधन और -झकुनि थर्मराज युथिष्ठिरके पास मेरा भी खूब सत्कार हुआ। अब पैं तुमसे जानेकी अनुमति
- **Translation**: 

---

### Verse 6 (Mahabharat 0.693)
- **Original**: केवल दुर्थोधन और -झकुनि थर्मराज युथिष्ठिरके पास मेरा भी खूब सत्कार हुआ। अब पैं तुमसे जानेकी अनुमति
- **Translation**: 

---

### Verse 7 (Mahabharat 0.694)
- **Original**: इख्प्रस्थमें ही रहे। फ++औ---+ दुर्योधनकी जलन और शकुनिकी सलाह वैज्ञप्पायरजी कहते हैं--अनमेजय ! सजा दुर्योधनने
- **Translation**: 

---

### Verse 8 (Mahabharat 0.694)
- **Original**: इख्प्रस्थमें ही रहे। फ++औ---+ दुर्योधनकी जलन और शकुनिकी सलाह वैज्ञप्पायरजी कहते हैं--अनमेजय ! सजा दुर्योधनने
- **Translation**: 

---

### Verse 9 (Mahabharat 0.695)
- **Original**: और दुःखी एवं रूजित हुआ । वह वहाँसे अभी कुछ ही आगे झकुनिके साथ इन्रप्रस्थमें ठहस्कर धीरे-धीरे सारी सभाका
- **Translation**: 

---

### Verse 10 (Mahabharat 0.695)
- **Original**: और दुःखी एवं रूजित हुआ । वह वहाँसे अभी कुछ ही आगे झकुनिके साथ इन्रप्रस्थमें ठहस्कर धीरे-धीरे सारी सभाका
- **Translation**: 

---

### Verse 11 (Mahabharat 0.696)
- **Original**: बढ़ा था कि स्थलके धोखे स्फटिकके समान निर्मल जल एवं निरीक्षण किया। उसने वहाँ ऐसा कल्ला-कौशल देखा, जो
- **Translation**: 

---

### Verse 12 (Mahabharat 0.696)
- **Original**: बढ़ा था कि स्थलके धोखे स्फटिकके समान निर्मल जल एवं निरीक्षण किया। उसने वहाँ ऐसा कल्ला-कौशल देखा, जो
- **Translation**: 

---

### Verse 13 (Mahabharat 0.697)
- **Original**: कमलोंसे सुओधित बाबलीमें जा पड़ा। धर्मराजकी आज्ञासे हस्तिनापुरमें कभी देखा नहीं था। एक दिन सभामें घूमते
- **Translation**: 

---

### Verse 14 (Mahabharat 0.697)
- **Original**: कमलोंसे सुओधित बाबलीमें जा पड़ा। धर्मराजकी आज्ञासे हस्तिनापुरमें कभी देखा नहीं था। एक दिन सभामें घूमते
- **Translation**: 

---

### Verse 15 (Mahabharat 0.698)
- **Original**: सेवकोने उसे उत्तम-उत्तम वस्त्र ल्लाकर दिये। उसकी यह दशा समय दुर्योधन किसी स्फटिकके चौकपें पहुँच गया और उसे
- **Translation**: 

---

### Verse 16 (Mahabharat 0.698)
- **Original**: सेवकोने उसे उत्तम-उत्तम वस्त्र ल्लाकर दिये। उसकी यह दशा समय दुर्योधन किसी स्फटिकके चौकपें पहुँच गया और उसे
- **Translation**: 

---

### Verse 17 (Mahabharat 0.699)
- **Original**: देखकर भीमसेन, अर्जुन, नकुछ, सहदेव, सब-के-सब हैसने जल समझकर उसने अपना बद्ध उठा लिया। पीछे अपना
- **Translation**: 

---

### Verse 18 (Mahabharat 0.699)
- **Original**: देखकर भीमसेन, अर्जुन, नकुछ, सहदेव, सब-के-सब हैसने जल समझकर उसने अपना बद्ध उठा लिया। पीछे अपना
- **Translation**: 

---

### Verse 19 (Mahabharat 0.700)
- **Original**: लूगे। दुर्योधनके असहिष्णु चित्तमें उनकी हैसीसे कष्ट तो भ्रम जानकर उसे दुःख हुआ और वह यों ही इधर-उधर
- **Translation**: 

---

### Verse 20 (Mahabharat 0.700)
- **Original**: लूगे। दुर्योधनके असहिष्णु चित्तमें उनकी हैसीसे कष्ट तो भ्रम जानकर उसे दुःख हुआ और वह यों ही इधर-उधर
- **Translation**: 

---

