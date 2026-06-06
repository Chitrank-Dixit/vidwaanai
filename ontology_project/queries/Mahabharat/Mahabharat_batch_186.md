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

### Verse 1 (Mahabharat 0.1851)
- **Original**: स्थानपर आये, जहाँ कि उनके सब भाई मारे गये थे। उन्हें कहकर अजजुनने झब्दबेधका कौझल दिखाते हुए सारी
- **Translation**: 

---

### Verse 2 (Mahabharat 0.1851)
- **Original**: स्थानपर आये, जहाँ कि उनके सब भाई मारे गये थे। उन्हें कहकर अजजुनने झब्दबेधका कौझल दिखाते हुए सारी
- **Translation**: 

---

### Verse 3 (Mahabharat 0.1852)
- **Original**: देखकर भीमको बड़ा दुःख हुआ । इधर प्यास भी उन्हें बेतरह दिज्ञाओंको अभिमन्त्रित बाणोंसे व्याप्त कर दिया। तब यक्षने
- **Translation**: 

---

### Verse 4 (Mahabharat 0.1852)
- **Original**: देखकर भीमको बड़ा दुःख हुआ । इधर प्यास भी उन्हें बेतरह दिज्ञाओंको अभिमन्त्रित बाणोंसे व्याप्त कर दिया। तब यक्षने
- **Translation**: 

---

### Verse 5 (Mahabharat 0.1853)
- **Original**: सता रही थी। उन्होंने समझा “यह काम यक्ष-राक्षसोंका है कहा, 'अर्जुन ! इस वृथा उद्योगसे क्‍या होना है ? तुप मेरे
- **Translation**: 

---

### Verse 6 (Mahabharat 0.1853)
- **Original**: सता रही थी। उन्होंने समझा “यह काम यक्ष-राक्षसोंका है कहा, 'अर्जुन ! इस वृथा उद्योगसे क्‍या होना है ? तुप मेरे
- **Translation**: 

---

### Verse 7 (Mahabharat 0.1854)
- **Original**: और आज मुझे उनसे अवश्य युद्ध करना पड़ेगा, इसलिये प्श्नोंका उत्त देकर जल पी सकते हो । यदि बिना उत्तर दिये
- **Translation**: 

---

### Verse 8 (Mahabharat 0.1854)
- **Original**: और आज मुझे उनसे अवश्य युद्ध करना पड़ेगा, इसलिये प्श्नोंका उत्त देकर जल पी सकते हो । यदि बिना उत्तर दिये
- **Translation**: 

---

### Verse 9 (Mahabharat 0.1855)
- **Original**: पहले पानी पी हूँ।' यह सोचकर वे प्याससे व्याकुछ होकर पीओगे तो पीते ही मर जाओगे।' यक्षके ऐसा कहनेपर
- **Translation**: 

---

### Verse 10 (Mahabharat 0.1855)
- **Original**: पहले पानी पी हूँ।' यह सोचकर वे प्याससे व्याकुछ होकर पीओगे तो पीते ही मर जाओगे।' यक्षके ऐसा कहनेपर
- **Translation**: 

---

### Verse 11 (Mahabharat 0.1856)
- **Original**: जलकी ओर चले। इतनेहीपें यक्ष बोल उठा, “भैया संव्यसाची धनकयने उसकी कोई पस्वा नहीं की और वे जल
- **Translation**: 

---

### Verse 12 (Mahabharat 0.1856)
- **Original**: जलकी ओर चले। इतनेहीपें यक्ष बोल उठा, “भैया संव्यसाची धनकयने उसकी कोई पस्वा नहीं की और वे जल
- **Translation**: 

---

### Verse 13 (Mahabharat 0.1857)
- **Original**: भीमसेन ! साहस न करे । पहलेहीसे मेरा एक नियम है। मेरे पीते ही गिर गये। प्श्नोंका उत्तर देकर तुम जल पी सकते हो ओर ले जा भी अब कुन्तीनन्दन युयिष्ठिस्ने भीमसेनसे कहा, भरतनन्दन !
- **Translation**: 

---

### Verse 14 (Mahabharat 0.1857)
- **Original**: भीमसेन ! साहस न करे । पहलेहीसे मेरा एक नियम है। मेरे पीते ही गिर गये। प्श्नोंका उत्तर देकर तुम जल पी सकते हो ओर ले जा भी अब कुन्तीनन्दन युयिष्ठिस्ने भीमसेनसे कहा, भरतनन्दन !
- **Translation**: 

---

### Verse 15 (Mahabharat 0.1858)
- **Original**: सकते हो ।' अतुललित तेजस्वी यक्षके ऐसा कहनेपर भी भीमने नकुछ, सहदेव और अर्जुन जल लानेके लिये बड़ी देरके गये
- **Translation**: 

---

### Verse 16 (Mahabharat 0.1858)
- **Original**: सकते हो ।' अतुललित तेजस्वी यक्षके ऐसा कहनेपर भी भीमने नकुछ, सहदेव और अर्जुन जल लानेके लिये बड़ी देरके गये
- **Translation**: 

---

### Verse 17 (Mahabharat 0.1859)
- **Original**: उसके प्रश्नोंका उत्तर दिये बिना ही जल पीया और पीते ही ये हुए हैं, अभीतक नहीं ल्गटे । तुम उन्हें लिया छाओ और जल
- **Translation**: 

---

### Verse 18 (Mahabharat 0.1859)
- **Original**: उसके प्रश्नोंका उत्तर दिये बिना ही जल पीया और पीते ही ये हुए हैं, अभीतक नहीं ल्गटे । तुम उन्हें लिया छाओ और जल
- **Translation**: 

---

### Verse 19 (Mahabharat 0.1860)
- **Original**: भूमिषर गिर गये। क+औ--+ यक्ष-युथ्िष्ठिर-संवाद वैज्ग्पायनजी कहते हैं--कधर महाराज युथिप्ठिर भीमको
- **Translation**: 

---

### Verse 20 (Mahabharat 0.1860)
- **Original**: भूमिषर गिर गये। क+औ--+ यक्ष-युथ्िष्ठिर-संवाद वैज्ग्पायनजी कहते हैं--कधर महाराज युथिप्ठिर भीमको
- **Translation**: 

---

