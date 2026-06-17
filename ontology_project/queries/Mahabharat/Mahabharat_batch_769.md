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

### Verse 1 (Mahabharat 941.7681)
- **Original**: तीनों व्याइतियाँ और सम्पूर्ण देवता भी ये देवकौनन्दन रक्षा करते हैं। कुत्तीनन्दन ! ये त्याज्य बस्तुका त्याग करके
- **Translation**: 

---

### Verse 2 (Mahabharat 941.7681)
- **Original**: तीनों व्याइतियाँ और सम्पूर्ण देवता भी ये देवकौनन्दन रक्षा करते हैं। कुत्तीनन्दन ! ये त्याज्य बस्तुका त्याग करके
- **Translation**: 

---

### Verse 3 (Mahabharat 941.7682)
- **Original**: श्रीकृष्ण ही हैं। संवत्सर, ऋतु, पक्ष, दिन-रात, कला, काझ्ठा, असुरतेंका वध करनेके लिये स्वयं कारण बनते हैं। कार्य और
- **Translation**: 

---

### Verse 4 (Mahabharat 941.7682)
- **Original**: श्रीकृष्ण ही हैं। संवत्सर, ऋतु, पक्ष, दिन-रात, कला, काझ्ठा, असुरतेंका वध करनेके लिये स्वयं कारण बनते हैं। कार्य और
- **Translation**: 

---

### Verse 5 (Mahabharat 941.7683)
- **Original**: मात्रा, मुहूर्त, लब और क्षण--इन सबको श्रीकृष्णका ही कारण इन्हींके स्वरूप हैं। विश्वकर्मा, विश्वरूप, विश्वभोक्ता,
- **Translation**: 

---

### Verse 6 (Mahabharat 941.7683)
- **Original**: मात्रा, मुहूर्त, लब और क्षण--इन सबको श्रीकृष्णका ही कारण इन्हींके स्वरूप हैं। विश्वकर्मा, विश्वरूप, विश्वभोक्ता,
- **Translation**: 

---

### Verse 7 (Mahabharat 941.7684)
- **Original**: स्वरूप समझो
- **Translation**: 

---

### Verse 8 (Mahabharat 941.7684)
- **Original**: स्वरूप समझो
- **Translation**: 

---

### Verse 9 (Mahabharat 941.7685)
- **Original**: चन््रमा, सूर्य, ग्रह, नक्षत्र, तारा, अमावास्या, विश्वविधाता और विश्वविजेता भी ये ही हैं। ये ही एक हाथमें
- **Translation**: 

---

### Verse 10 (Mahabharat 941.7685)
- **Original**: चन््रमा, सूर्य, ग्रह, नक्षत्र, तारा, अमावास्या, विश्वविधाता और विश्वविजेता भी ये ही हैं। ये ही एक हाथमें
- **Translation**: 

---

### Verse 11 (Mahabharat 941.7686)
- **Original**: पूर्णिमा, नक्षत्र, योग और ऋतु--इन सबकी उत्पत्ति श्रिशूछ और दूसरे हाथमें रक्तसे भरा ख़्पर छिये हुए विकराल
- **Translation**: 

---

### Verse 12 (Mahabharat 941.7686)
- **Original**: पूर्णिमा, नक्षत्र, योग और ऋतु--इन सबकी उत्पत्ति श्रिशूछ और दूसरे हाथमें रक्तसे भरा ख़्पर छिये हुए विकराल
- **Translation**: 

---

### Verse 13 (Mahabharat 941.7687)
- **Original**: श्रीकृष्णसे ही हुई है। रुढ्क, आदित्य, बसु, अश्विनीकुमार, रूप धारण करते हैं। अपने नाना प्रकारके चरित्रोंसे जगतमें
- **Translation**: 

---

### Verse 14 (Mahabharat 941.7687)
- **Original**: श्रीकृष्णसे ही हुई है। रुढ्क, आदित्य, बसु, अश्विनीकुमार, रूप धारण करते हैं। अपने नाना प्रकारके चरित्रोंसे जगतमें
- **Translation**: 

---

### Verse 15 (Mahabharat 941.7688)
- **Original**: साध्य, विश्वेदेव, मरुद्गण, प्रजापति, देवमाता अदिति और विख्यात हुए इन श्रीकृष्णकी ही सब लोग स्तुति करते हैं। ' सप्तर्षि भी श्रीकृष्णसे ही प्रकट हुए हैं। ये विश्वरूप श्रीकृष्ण सैकड़ों गन्धर्थ,अप्सराएँ तथा देवता सदा इनकी सेवामें
- **Translation**: 

---

### Verse 16 (Mahabharat 941.7688)
- **Original**: साध्य, विश्वेदेव, मरुद्गण, प्रजापति, देवमाता अदिति और विख्यात हुए इन श्रीकृष्णकी ही सब लोग स्तुति करते हैं। ' सप्तर्षि भी श्रीकृष्णसे ही प्रकट हुए हैं। ये विश्वरूप श्रीकृष्ण सैकड़ों गन्धर्थ,अप्सराएँ तथा देवता सदा इनकी सेवामें
- **Translation**: 

---

### Verse 17 (Mahabharat 941.7689)
- **Original**: ही बायुरूप धारण करके संसारकों चेष्टा प्रदान करते, उपस्थित रहते हैं। राक्षस भी इनसे सम्मति लिया करते हैं।
- **Translation**: 

---

### Verse 18 (Mahabharat 941.7689)
- **Original**: ही बायुरूप धारण करके संसारकों चेष्टा प्रदान करते, उपस्थित रहते हैं। राक्षस भी इनसे सम्मति लिया करते हैं।
- **Translation**: 

---

### Verse 19 (Mahabharat 941.7690)
- **Original**: अग्रिकप होकर सबको भस्म करते, जलका रूप धारणकर एकमात्र ये ही धनके रक्षक और विश्वविजयी हैं। यज्॒में
- **Translation**: 

---

### Verse 20 (Mahabharat 941.7690)
- **Original**: अग्रिकप होकर सबको भस्म करते, जलका रूप धारणकर एकमात्र ये ही धनके रक्षक और विश्वविजयी हैं। यज्॒में
- **Translation**: 

---

