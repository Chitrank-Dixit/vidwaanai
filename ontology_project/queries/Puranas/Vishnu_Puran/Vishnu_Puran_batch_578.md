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

### Verse 1 (Vishnu Puran 0.11541)
- **Original**: तुमत्मेगोंके साथ समान आसन और भोजनका व्यवहार कस्के तुम्हें हमहीने गरवॉला बना दिया है; इसमें तुप्हारा कोई दोष नहीं है क्योंकि हमने ही प्रीतिबश नीतिका विचार नहीं किया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11542)
- **Original**: है बलराम ! हमने जो तुम्हें यह अर्घ्ध आदि निवेदन किया है यह प्रेमवदा ही किया है, वास्तवमें हमारे कुलूकी तरफसे तुम्हारे कुलको अर्ध्यादि देना उचित नहीं है”
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11543)
- **Original**: श्रीपराशरजी खोले--ऐसा कहकर कौरवगण यह
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11544)
- **Original**: निश्चय करके कि "हम कृष्णके पुत्र साम्बको नहीं छोडेंगे''
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11545)
- **Original**: तुरन्त हस्तिनापुरमें चले गये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11546)
- **Original**: तदनत्तर हलायूध श्रोबलरामजोने उनके तिरस्कारसे उत्पन्न हुए क्रोघसे मत्त होकर घूरते हुए पृथिवीमें ल्थत मारी
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11547)
- **Original**: महात्मा बलरशमगजीके पाद-प्रहारसे पृथिवी फट गयी और वे अपने आच्दसे सम्पूर्ण दिशाओंकों गुँजाकर कम्पायमान करने लगे तथा ल्लाल-लाल नेत्र और टेढ़ी भूकुटे करके बोले--
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11548)
- **Original**: 291-22
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11549)
- **Original**: “अहो ! इन सारहीन दुग़त्मा कौरवॉको यह कैसा राजमदका अभिमान है। कौरवोंका महीपालत्व तो स्वतःसिद्ध है और हमारा सामयिक--ऐसा समझकर ही आज ये महाराज उग्रसेनकी आज्ञा नहीं मानते; बल्कि उसका उल्लड्भुन कर रहे हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11550)
- **Original**: आज राजा उग्यसेन सुधर्मा-सभामें स्वयं विराजमान होते हैं, डसमें शाचीपति इन्द्र भी नहीं बैठने पाते। परन्तु इन
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11551)
- **Original**: आ0 35 ] पारिजाततरो: . पुष्पमक्षरीर्बनिताजन: । बिभर्ति यस्य भृत्यानां सो5प्येषां न महीपति:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11552)
- **Original**: 25 समस्तभूभतां नाथ उप्रसेनस्स तिष्ठतु
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11553)
- **Original**: अद्य निष्कोरवामुर्वी कृत्वा यास्यामरि तत्पुरीम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11554)
- **Original**: 26 कर्ण दुर्योधन द्रोणमद्य भीष्मं सबाह्लिकम्‌ । दुशशासनादीन्भूरि चर भूरिश्रवसमेब चर
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11555)
- **Original**: 27 सोमदत्त॑ झल्ं चैव भीमार्जुनयुधिष्ठिरान्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11556)
- **Original**: यमोौ च कौरवांश्ञान्यानवत्वा साभ्ररथद्विपान्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11557)
- **Original**: 28 वीरमादाय त॑ साम्बं॑ सफ्त्रीके ततः पुरीम्‌। द्वारकामुग्रसेनादीन्गत्वा द्रक्ष्यामि बाल्धवान्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11558)
- **Original**: 29 अथ वा कोौरवावासं समस्तेः कुरुभिस्सह । भागीरथ्यां क्षिपाम्याशु नगर॑ नागसाह्ृयम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11559)
- **Original**: 30 अपक्शर उकच इत्युक्त्वा मदरक्ताक्ष: कर्षणाधोमुखं हलम्‌ । प्राकारबप्रदुर्गल्य चकर्ष मुसलायुध:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11560)
- **Original**: 31 आधुूर्णितं तत्सहसा ततो बै हास्तिन॑ पुरम्‌। दृष्टठा संक्षुब्धहदयाश्रुक्षुध: सर्वकौरवा:
- **Translation**: 

---

