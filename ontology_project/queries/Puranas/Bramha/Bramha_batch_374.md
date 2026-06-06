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

### Verse 1 (Bramha 0.7461)
- **Original**: करनेवाला मानव विजय-लाभ करता है। कृमि, दशार्ण, कुमार्य, तक्ग॒ण, क्रथ, सिन्धु नदीका , त्रयोदशीकों श्रद्धासहित श्राद्ध करनेवाला पुरुष उत्तर तट, नर्मदाका दक्षिण तट और करतोयाका
- **Translation**: 

---

### Verse 2 (Bramha 0.7462)
- **Original**: संतान-वृद्धि, पशु, मेधा, स्वतन्त्रता, उत्तम पुष्टि, पूर्व तट-इन प्रदेशोंमें श्राद्ध नहीं करना चाहिये।
- **Translation**: 

---

### Verse 3 (Bramha 0.7463)
- **Original**: दीर्घायु अथवा ऐश्वर्यका भागी होता है--इसमें
- **Translation**: 

---

### Verse 4 (Bramha 0.7464)
- **Original**: * आद्ध-कल्पका वर्णन « 361 वनिक भी संदेह नहीं है। जिसके पितर युवावस्थामें
- **Translation**: 

---

### Verse 5 (Bramha 0.7465)
- **Original**: करनेबाला पुरुष उत्तम आरोग्य लाभ करता है। ही मृत्युको प्रात्त हुए अथवा शस्स्रद्वारा मारे गये
- **Translation**: 

---

### Verse 6 (Bramha 0.7466)
- **Original**: पूर्वाषाढ़ नक्षत्रमें यशकी प्राप्ति होती है। उत्तराषाढ़ामें हों, वे उन पितरोंकों तृत्त करनेकी इच्छासे श्राद्ससे शोक दूर होता है। श्रवणमें श्राद्धके चतुर्दशी तिधिको श्रद्धापूर्वक श्राद्ध करें। जो
- **Translation**: 

---

### Verse 7 (Bramha 0.7467)
- **Original**: अनुष्ठानसे शुभ लोक प्राप्त होते हैं। धनिष्ठामें पुरुष पवित्र होकर अमावास्थाकों यलपूर्बक
- **Translation**: 

---

### Verse 8 (Bramha 0.7468)
- **Original**: श्राद्धसे अधिक धनका लाभ होता है। अभिजित्में श्राद्ध करता है, बह सम्पूर्ण कामनाओं तथा
- **Translation**: 

---

### Verse 9 (Bramha 0.7469)
- **Original**: श्राद्धसे बेदोंकी दिद्वत्ता प्राप्त होती है। शतभिषामें अक्षय स्वर्गको प्राप्त करता है। पितरोंकी पूजा करनेसे वैद्यकके कार्यमें सिद्धि मुनिवरो! अब पितरोंकों प्रसन्नताके लिये
- **Translation**: 

---

### Verse 10 (Bramha 0.7470)
- **Original**: प्राप्त होती है। पूर्वाभाद्रपदामें श्राद्धसे भेड़ और जो-जो वस्तु देनी चाहिये, उसका वर्णन सुनो।
- **Translation**: 

---

### Verse 11 (Bramha 0.7471)
- **Original**: बकरी तथा उत्तराभाद्रपदामें गौएँ प्राप्त होती हैं। जो श्राद्धकर्ममें गुडमिश्रित अन्न, तिल, मधु
- **Translation**: 

---

### Verse 12 (Bramha 0.7472)
- **Original**: रेवतीमें श्राद्धका अनुष्ठान करनेसे जस्ता आदि अथवा मधुमिश्रित अन्न देता है, उसका वह
- **Translation**: 

---

### Verse 13 (Bramha 0.7473)
- **Original**: धातुओंकी तथा अश्विनीमें घोड़ोंकी प्राप्ति होती सम्पूर्ण दान अक्षय होता है। पितर कहते
- **Translation**: 

---

### Verse 14 (Bramha 0.7474)
- **Original**: है। भरणी नक्षत्रमें श्राद्ध करनेवाला पुरुष उत्तम हैं--' क्या हमारे कुलमें ऐसा कोई पुरुष होगा,
- **Translation**: 

---

### Verse 15 (Bramha 0.7475)
- **Original**: आयु प्राप्त करता है। तत्त्वज्ञ पुरुष उक्त नक्षत्रोमें जो हमें जलाञलि देगा, वर्षामें और मधघा
- **Translation**: 

---

### Verse 16 (Bramha 0.7476)
- **Original**: श्राद्ध करनेपर ऐसे ही फलोंके भागी होते हैं। नक्षत्रमें हमको मधुमिश्रित खोर अर्पण करेगा?
- **Translation**: 

---

### Verse 17 (Bramha 0.7477)
- **Original**: अत: अक्षय फलकी इच्छा रखनेवाले पुरुषको मनुष्यॉंकों बहुत-से पुत्रोंकी अभिलाषा करनी
- **Translation**: 

---

### Verse 18 (Bramha 0.7478)
- **Original**: कन्याराशिपर सूर्यके रहते उक्त नक्षत्रोंमें काम्य चाहिये। यदि उनमेंसे एक भी गया चला जाय
- **Translation**: 

---

### Verse 19 (Bramha 0.7479)
- **Original**: श्राद्धका अनुष्ठान अवश्य करना चाहिये। सूर्यके अथवा कन्याका विवाह करे या नील वृषका
- **Translation**: 

---

### Verse 20 (Bramha 0.7480)
- **Original**: कन्याराशिपर स्थित रहते मनुष्य जिन-जिन उत्सर्ग करे तो पितरोंकों पूर्ण तृप्ति और उत्तम
- **Translation**: 

---

