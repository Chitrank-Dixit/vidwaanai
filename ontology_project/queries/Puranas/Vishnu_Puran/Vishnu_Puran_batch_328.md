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

### Verse 1 (Vishnu Puran 0.6541)
- **Original**: जागेपर ऋषियेंनि पूछा, इस मन्त्पूत जलको किसने पिया है 7
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6542)
- **Original**: इसका ऋषय: पप्रच्छुः केनैतन्मनत्रपूत वारि पीतम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6543)
- **Original**: पान करनेपर हों युवनाश्वकी पत्नी महाबलतिक्रमशील
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6544)
- **Original**: अत्न हि राज्ञो युवनाश्रस्थ पत्नी महाबलपराक्रमं पुत्र जनयिष्यति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6545)
- **Original**: इत्याकर्ण्य स पुत्र उत्पन्न करेगी।' यह सुनकर राजाने कहॉा--- “मैंने हो बिना जाने यह जल पी लिया है”
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6546)
- **Original**: अन्खर चतुर्थ अं 235 राजा अजानता मया पीतमित्याह
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6547)
- **Original**: अतः युवनाश्रक्के उदरमें गर्भ स्थापित हो गया और क्रमञञः गर्भश्ष युवनाश्रस्थोदे!र अभवत्‌ क्रमेण चल
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6548)
- **Original**: बढ़ने लगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6549)
- **Original**: बथासमय बालक-राजाकी दायीं यवृधे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6550)
- **Original**: प्राप्तसमयश्न दक्षिणं कुक्षिमव- निफ्तेरनि्िद्य निश्चक्राम
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6551)
- **Original**: न चासौ राजा ममार
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6552)
- **Original**: जातो नामैंध क॑ धास्थतीति ते मुनयः प्रोचु:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6553)
- **Original**: अथागत्य देवराजो5ब्रवीत्‌ मामय॑ धास्यतीति
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6554)
- **Original**: ततो. माल्धातृनामा सो5भवत्‌ । बक्त्रे चास्य प्रदेशिनी देवेन्द्रेण न्यस्ता ता पषौ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6555)
- **Original**: तां चामृतस्राविणीमास्वाध्याद्नेव स व्यवर्द्धध
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6556)
- **Original**: ततस्तु माखाता चक्रवर्ती सप्तद्वीप' महीं बुभुजे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6557)
- **Original**: तत्नार्य इलोकः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6558)
- **Original**: यावत्सूर्य उद्देत्यस्त॑यावश्च प्रतितिष्ठति । सर्व तदोवनाश्रस्य मान्धातु: क्षेत्रमुच्यते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6559)
- **Original**: 65 मान्धाता झतबिन्दोर्दुहितरं. बिन्दुमती- मुपयेमे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6560)
- **Original**: पुरुकुत्समम्बरीषष मुचुकुन्द च तस्याँ पुत्रन्नयमुत्पादयामास
- **Translation**: 

---

