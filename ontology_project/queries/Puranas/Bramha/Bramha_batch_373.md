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

### Verse 1 (Bramha 0.7441)
- **Original**: बतलाया। यह सभी धर्मों और दानोंका मूल है। +ढल्‍्सय2 2290-00 श्राद्ध-कल्पका वर्णन मुनियोंने पूछा-- भगवन्‌! अब श्राद्ध-कल्पका
- **Translation**: 

---

### Verse 2 (Bramha 0.7442)
- **Original**: प्रत्येक मासकी अमावास्या और पूर्णिमाको श्राद्धके विस्तारपूर्वक वर्णन कौजिये। तपोधन ! कब, कहाँ,
- **Translation**: 

---

### Verse 3 (Bramha 0.7443)
- **Original**: योग्य काल बताया गया है। नित्यश्राद्धमें विश्वेदेवोंका किन देशोंमें और किन लोगोंको किस प्रकार
- **Translation**: 

---

### Verse 4 (Bramha 0.7444)
- **Original**: पूजन नहीं होता। नैमित्तिक श्राद्ध विश्वेदेवोंके श्राद्ध करना चाहिये-यह बतानेकी कृपा करें।
- **Translation**: 

---

### Verse 5 (Bramha 0.7445)
- **Original**: पूजनपूर्वक होता है। नित्य, नैमित्तिक और काम्य--ये व्यासजी बोले--मुनिवरो! सुनो, मैं श्राद्ध-
- **Translation**: 

---

### Verse 6 (Bramha 0.7446)
- **Original**: तीन प्रकारके श्राद्ध माने गये हैं। इन तौनोंका कल्पका विस्तारके साथ वर्णन करता हूँ। जब,
- **Translation**: 

---

### Verse 7 (Bramha 0.7447)
- **Original**: प्रतिवर्ष अनुष्ठान करना चाहिये। जातकर्म आदि जहाँ, जिन प्रदेशोंमें और जिन लोगोंद्वारा जिस
- **Translation**: 

---

### Verse 8 (Bramha 0.7448)
- **Original**: संस्कारोंक अवसरपर आशभ्युदयिक श्राद्ध भी करना प्रकार श्राद्ध किया जाना चाहिये, वह सब
- **Translation**: 

---

### Verse 9 (Bramha 0.7449)
- **Original**: उचित है। उसमें युग्म ब्राह्मणोंकों निमन्त्रित बतलाता हूँ। अपने कुलोचित धर्मका पालन
- **Translation**: 

---

### Verse 10 (Bramha 0.7450)
- **Original**: करनेका विधान है। आशभ्युदयिक श्राद्ध मातासे करनेवाले ब्राह्मण, क्षत्रिय और वैश्योंको उचित है
- **Translation**: 

---

### Verse 11 (Bramha 0.7451)
- **Original**: आरम्भ होता है। जब सूर्य कम्याराशिपर जाते है, कि वे अपने-अपने वर्णके अनुरूप वेदोक्त विधिसे
- **Translation**: 

---

### Verse 12 (Bramha 0.7452)
- **Original**: तब कृष्णपक्षके पंद्रह दिनोंतक पार्वणकी विधिसे मन्त्रोच्चारणपूर्वक श्राद्धका अनुष्ठान करें। स्त्रियों
- **Translation**: 

---

### Verse 13 (Bramha 0.7453)
- **Original**: श्राद्ध करना चाहिये। प्रतिपदाको श्राद्ध करनेसे और ज्ट्रोंक् ब्राह्मणको आज्ञाके अनुसार मन्त्रोच्चारणके ' धनकी प्राप्ति होती है। द्वितीया संतान देनेवाली है। बिना ही विधिवत्‌ श्राद्ध करना चाहिये। उनके
- **Translation**: 

---

### Verse 14 (Bramha 0.7454)
- **Original**: तृतीया पुत्रप्राप्तिको अभिलाषा पूर्ण करती है। लिये अग्निमें होम आदि वर्जित हैं। पुष्कर आदि
- **Translation**: 

---

### Verse 15 (Bramha 0.7455)
- **Original**: चतुर्थी शत्रुका नाश करनेवाली है। पञ्चमीकों तीर्थ, पवित्र मन्दिर, पर्वतशिखर, पावन प्रदेश,
- **Translation**: 

---

### Verse 16 (Bramha 0.7456)
- **Original**: श्राद्ध करनेसे मनुष्य लक्ष्मीको प्राप्त करता हैं पुण्यसलिला नदी, नद, सरोवर, संगम, सात
- **Translation**: 

---

### Verse 17 (Bramha 0.7457)
- **Original**: और षष्ठीको श्राद्ध करके वह पूजनीय होता है। समुद्रोंक तट, लिपे-पुते अपने घर, दिव्य वृक्षोंके
- **Translation**: 

---

### Verse 18 (Bramha 0.7458)
- **Original**: सत्मीको गणोंका आधिपत्य, अष्टमीको उत्तम मूल और यज्ञ-कुण्ड-ये सभी उत्तम स्थान हैं।
- **Translation**: 

---

### Verse 19 (Bramha 0.7459)
- **Original**: बुद्धि, नौमीको स्त्री, दशमीको मनोरथकौ पूर्णता इन सबयें श्राद्ध करना चाहिये। और एकादशीको श्राद्ध करनेसे मनुष्य सम्पूर्ण अब श्राद्धके लिये वर्जित स्थान बतलाता हूँ।
- **Translation**: 

---

### Verse 20 (Bramha 0.7460)
- **Original**: बेदोंको प्राप्त करता है। ट्वादशीको पितरोंकी पूजा किरात (किलात), कलिड्ड (उड़ीसा), कोक्ूलूण,
- **Translation**: 

---

