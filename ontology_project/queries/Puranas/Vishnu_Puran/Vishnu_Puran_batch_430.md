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

### Verse 1 (Vishnu Puran 0.8581)
- **Original**: तस्थाप्यष्टो सुतास्सुपाल्याद्या भवितार:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8582)
- **Original**: तस्य महापद्यस्यानु पृथिवीं भोक्ष्यन्ति
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8583)
- **Original**: महापद्मपुत्राशैक वर्षशतमवनीपतयो भविष्यन्ति
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8584)
- **Original**: ततश्व नव चैतान्नन्दान्‌ कौटिल्यो ब्राह्मणस्समुद्धरिष्यति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8585)
- **Original**: तेषामभाजे मोर्याः पृथचिवरीं भोक्ष्यन्ति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8586)
- **Original**: कौटिल्य एवं च न्द्रगुप्रपुत्पन्नं राज्येउभिषेक्ष्यति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8587)
- **Original**: । तस्थापि पुत्रो बिन्दुसारों भविष्यति
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8588)
- **Original**: तस्थाप्यशोकवर्द्धनस्ततस्सुयशास्ततक्ष दशरंथ- स्ततक्ष॒ संयुतस्ततइशालिशूकस्तस्मात्सोम्रर्मा तस्यापि सोमशर्मणइश्तथन्वा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8589)
- **Original**: तस्यापि यूहद्रथनामा भविता
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8590)
- **Original**: एबमेते मोर्य्या दश भूपतयो भविष्यन्ति अब्दशतं सप्तत्रिशददुत्तरम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8591)
- **Original**: तेषामन्ते पृथितीं दश शुड्ज्रा भोक्ष्यन्ति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8592)
- **Original**: पुण्यमित्रस्सेनापतिस्स्वामिरन हत्वा राज्य॑ करिष्यति तस्यात्मजो5पिमित्र:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8593)
- **Original**: तस्मात्सुज्येप्टस्ततो. बसुमित्रस्तस्मादप्युदडुस्ततः पुलिन्दकस्ततो घोषवसुस्तस्मादपि वच्रमित्रस्ततो श्रोकिष्णुपराण [ अ* 24 पृथिवीका पालन करेंगे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8594)
- **Original**: नन्दीका पुत्र शिश्लुनाभ होगा, झिशुनाभका का्नकवर्ण, काकबर्णका द्षेमधर्मा, क्षेमरधर्माका क्षतौजा, क्षतौजाका विधिसार, विघिसारका अजातशतरु, अजातक्ञत्रुका अर्भक, अर्भकका उदयन, उदयनका नन्दिवर्दन और नन्दिवर्द्धनका पुत्र महानन्दी होगा। ये शिशुनाभवंशीय नृपतिगण तीन सौ बासठ वर्ष पृथिवीका झ्ासन करेंगे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8595)
- **Original**: महानन्दीके शुद्राके गर्भसे उत्पन्न महापद्य नामक नन्‍्द दूसरे परज्ञरामके समान सम्पूर्ण क्षत्रियोंका नाडा करनेवात्त्र होगा। तबसे शुद्रजातीय राजा राज्य करेंगे। राजा महापदा सम्पूर्ण पृथिवीका एकच्छत्र और अनुल्लब्लित राज्य- शासन करेगा। ठसके सुमाली आदि आठ पुत्र होंगे जो प्रह्मफट्राके पीछे पृथ्चिवीका राज्य भोगेंगे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8596)
- **Original**: 20--24
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8597)
- **Original**: महापरा और उसके पूत्र सौ वर्षतक पृथिवीका झञासन करेंगे। तदनच्तर इन नखों नन्‍्दोंको कौटिल्थनामक एक ब्राह्मण नष्ट करेगा, उनका अन्त होनेपर मौर्य नृपतिगण पूथिवीको भोगेंगे। कौटिल्य ही [ सुरा नामकी दासीसे नन्‍्दद्वारा ] उत्पन्न हुए चन्दगुप्तको राज्याभिषिक्त करेगा ।
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8598)
- **Original**: 25---28
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8599)
- **Original**: चअन्द्रगुप्तका पुत्र बिन्दुसार, बिन्दुसासका अशोकवर्द्धन, अशोकवर्द्धनका सुयशा, सुयज्ञावत्र दशरथ, दशरथका संयुत, संयुतका शाल्िशूक, द्ालिशूकका सोमशझर्मा, सोमदार्माका झतथधन्वा तथा दशातघन्वाका पुत्र बृहद्रथ होगा। इस प्रकार एक सौ तिहत्तर वर्षतक ये दस मौर्यवंद्ञी राजा राज्य कोंगे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8600)
- **Original**: 29--32
- **Translation**: 

---

