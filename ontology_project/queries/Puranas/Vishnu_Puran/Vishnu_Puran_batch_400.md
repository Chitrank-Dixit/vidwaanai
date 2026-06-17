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

### Verse 1 (Vishnu Puran 0.7981)
- **Original**: कुकुरादधृष्टः तस्माश कपोतरोमा ततश् विलोमा तस्मादपि तुम्बुरुसखो5भवदनुसंज्ञक्ष
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7982)
- **Original**: अनोरानक- दुन्दुभि:, ततश्चाभिजिद्‌ अभिजित: पुनर्वसुः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7983)
- **Original**: तस्थाप्याहृक आहकी च॑ कन्या
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7984)
- **Original**: आहुकस्य देवकोग्रसेनो ट्लो पुत्रों
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7985)
- **Original**: देववानुपदेवः सहदेवो देवरक्षितश्न देवकस्य चत्वारः पुत्रा:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7986)
- **Original**: तेषों वृकदेवोषदेवा देवरक्षिता श्रीदेवा शान्तिदेवा सहदेवा देवकी च सप्त भगिन्यः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7987)
- **Original**: ताश्च सर्वा वसुदेव उपयेपे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7988)
- **Original**: उग्रसेनस्थापि कंस-
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7989)
- **Original**: न्यग्रोधसुनामानकाह्नशद्जुसु धूमिराष्ट्रपालयुद्ध- तुष्टिसुतुष्टिमत्सज्ञा: पुत्रा बभूवु:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7990)
- **Original**: कंसाकंसबतीसुतनुराष्ट्रपालिकाह्वाश्रोग्रसेनस्य तनूजाः कन्या:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7991)
- **Original**: ओरीपराशरजी खोले-- अनमित्रके शिनि नागक पुत्र हुआ; झिनिके सत्यक और सस्यकसे सात्यकिका जन्म हुआ जिसका दूसरा नाम युयुधान था
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7992)
- **Original**: तदनन्तर सात्यकिके सञ्य, सजञयके कुणि और कुणिसे युग-घरका जन्म हुआ
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7993)
- **Original**: ये सब शैनेय नामसे खिख्यात हुए
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7994)
- **Original**: अममित्रके वशमें ही पृश्रिका जन्म हुआ और पृश्निसे धफलल्‍्ककी उत्पत्ति हुई जिसका प्रभाव पहले वर्णन कर चुके हैं। ध्रफल्कका चित्रक नामक एक छोटा भाई और था
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7995)
- **Original**: अश्रफल्कके गान्दिनीसे अक्रस्का जन्म हुआ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7996)
- **Original**: तथा [ एक दूसरी खीसे ] ठपमहदु, प्रदाम्रद, किश्वारि, गेजय, पिश्क्षित्र, उपक्षत्र, शतप्न, असिमिर्टन, धर्मदुक्‌, दृष्टधर्म, गन्धमोज, वाह और प्रतिवाह नामक युत्र तथा सुतारानान्री कन्याका जन्म हुआ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7997)
- **Original**: देववान और उपदेव ये दो अक्रूरके पुत्र थे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7998)
- **Original**: तथा चित्रकके पृथु, निपृथु आदि अनेक पुत्र थे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7999)
- **Original**: कुकुर, भजमान, झुचिकम्बल और बार्ह्िष ये चार अन्धकके पुत्र हुए
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8000)
- **Original**: इनपेंसे कुकुरसे धृष्ट, घृष्टसे कपोतरोमा, कपोतरोमासे बिलोमा तथा बिलोमासे तुप्बुक के मित्र अनुका जन्म हुआ
- **Translation**: 

---

