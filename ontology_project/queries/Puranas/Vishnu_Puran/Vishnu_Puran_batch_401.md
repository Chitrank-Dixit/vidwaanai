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

### Verse 1 (Vishnu Puran 0.8001)
- **Original**: अनुसे आनकदुन्दुभि, उससे अभिजितू, अभिजितसे पुनर्वसुं और पुनर्वसुसे आहुक नामक पुत्र और आहुकीनाश्नी कन्याका जन्म हुआ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8002)
- **Original**: आहुकके देवक और उम्रसेन नामक दो पुत्र हुए
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8003)
- **Original**: उनमेंसे देवकके देववान्‌ उपदेव, सहदेख और देखरक्षित नामक चार पुत्र हुए
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8004)
- **Original**: इन चारोंकी चरकढेला, उपदेवा, देवरक्षिता, श्रीदेवा, शान्तिदेवा, सहदेखा और देवकी ये सात भगिनियाँ थीं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8005)
- **Original**: ये सब वसुरेक्‍्जोको खिवाही गयी थीं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8006)
- **Original**: उग्रसेनके भो कंस, न्यथोध, सुनाम, आनकाद, झड्डु, सुभूमि, राष्ट्रपाल, युद्रतुष्टि और सुतुश्टिपान्‌ नामक पुत्र तथा कैसा, कंसवत्ती, सूतन्‌ और शाष्ट्रपाक्लिका नामकी कत्याएँ हुई
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8007)
- **Original**: 282 भ्रजमानाथ विदृूरथ: पुत्रो5भवत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8008)
- **Original**: विदूरथाच्छूर: शूराच्छटमी शमिनः प्रतिक्षत्र: तस्मात्खयंभोजस्ततश्च हदिकः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8009)
- **Original**: तस्थापि कृतवर्मशतथ्नुर्देवाईदेवगर्भाद्या: पुत्रा बभूबु:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8010)
- **Original**: देवगर्भस्यापि झूर:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8011)
- **Original**: शूरस्यापि मारिषा नाम पल्‍्यभवत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8012)
- **Original**: तस्यां चासौ दष्मपुत्रानजनयद्टसुदेवपूर्वान्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8013)
- **Original**: वसुदेवस्य ततश्चासावानकदुन्दुभिसंज्ञामवाप
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8014)
- **Original**: तस्थय च देवभागदेक्श्रवोष्टक- ककुचक्रवत्सघारकसुझयहश्यामहामिकगण्द्ूष- संज्ञा नब भ्रातरोईभवन्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8015)
- **Original**: पृथा श्रुतदेवा श्रुतकीर्ति: श्रुतश्रवा राजाधिदेवी च॒ वसुदेवादीनां पञह्ञ भगिन्यो5भवन्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8016)
- **Original**: शुरस्य कुन्तिनाम सस्वाभवत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8017)
- **Original**: तस्मै चापुत्राय पृथामात्मजां विधिना शूरो दत्तवान्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8018)
- **Original**: तां च पाण्डुरुवाह
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8019)
- **Original**: तस्यां उ॒ धर्मानिलेन्द्रैयुथिष्टिरभीमसेनार्जुनाख्यास्त्रय: पुत्रास्समुत्पादिता:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8020)
- **Original**: पूर्वमेवानूढायाद्ध भगवता भास्वता कानीन: कर्णो नाम पुनत्रोउजन्यत
- **Translation**: 

---

