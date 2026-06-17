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

### Verse 1 (Vishnu Puran 0.6441)
- **Original**: श्रीविष्णुपुराण [ आ* 2 अतुलबुद्धि महाराज रैबतने अपनी कुशस्थली नामकी पुरी और ही प्रकारबी देखी तथा स्फटिक-पर्वतके समान जिनका वक्ष:स्थल है उन भगवान्‌ हल्म्रयुधको अपनी कन्या दे दी
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6442)
- **Original**: भगयान्‌ बलूदेवजीने उसे बहुत ऊँचो देखकर अपने हलके अग्रभागसे दबाकर नीची कर ली। तब रेवती भी तत्कालीन अन्य स्त्रियोंके समान (छोटे शरीरकरी) हो गयी
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6443)
- **Original**: तदनन्तर बलरामजीने महाराज रैबतकी कन्या रेवतीसे विधिंपूर्वक विवाह किया तथा राजा भो कन्यादान करनेके अनन्तर एकाप्रचित्तसे तपस्था करनेके लिये हिमालयपर चले का औ -+ इति श्रीविष्णुपुराणे चतुर्थेष्शे प्रथमो5ध्यायः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6444)
- **Original**: कम और 7 दूसरा अध्याय कुक्ष्वाकुके वंशका वर्णन तथा सौभरिच्यरित्र श्रीप्ाञ्र उताच श्रीपराझ्रजी खोलले--जिस समय रैवत ककुद्यी यावच्च ब्रह्मलोकात्स ककुझी रैवतो नाभ्येति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6445)
- **Original**: ब्रह्मलेकसे लौटकर नहीं आये थे उसी समय युण्यजन तावत्पुण्यजनरसज्ञा राक्षसास्तामस्य पुरी कुशस्थल्डी निज्चु:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6446)
- **Original**: तथ्चास्थ श्रातृशत पुण्यजन- त्रासाहिशों भेजे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6447)
- **Original**: तदन्वयाश्र क्षत्रिया- स्सर्वदिक्षभवन्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6448)
- **Original**: धृष्टस्यापि . धाईक॑ क्षत्रमभवत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6449)
- **Original**: नाभागस्यात्मजो नाभाग- संज्ञोी>भवत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6450)
- **Original**: . तस्थाप्यम्बरीष:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6451)
- **Original**: अम्बरीषस्यापि विरूपो5भवत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6452)
- **Original**: विरूपा- त्यूषदश्नो जज्ञे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6453)
- **Original**: ततश्च रथीतर:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6454)
- **Original**: अ्रायं इलोक:--एते क्षत्रप्रसृता वै पुनआ्विरसा: स्मृता:। रथीतराणां प्रवराः क्षत्रोपेता द्विजातय:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6455)
- **Original**: इतति क्षुतवतश्च मनोरिक्ष्वाकुः पुत्रों जज्ञे घ्राणतः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6456)
- **Original**: तस्य पुत्नझ्तप्रधाना विकुक्षिनिमिदण्डा - ख्यात्नयः पुत्रा बभूवु:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6457)
- **Original**: शकुनिप्रपुखा: पश्चाशत्पुत्रा उत्तरापथरक्षितारों बभूखु:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6458)
- **Original**: नामक राक्षसॉने उनकी पुरी कुशस्थलीका ध्वेस कर दिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6459)
- **Original**: उनके सौ भाई पुण्यज़न राक्षसोके भयसे दसों दिज्ञाओंमें भाग गये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6460)
- **Original**: उल्ींके वैशमें उत्पन्न हुए क्षत्रियगण समस्त दिज्ञाओँमें फैले
- **Translation**: 

---

