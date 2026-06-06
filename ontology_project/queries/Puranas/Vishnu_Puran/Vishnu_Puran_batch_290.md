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

### Verse 1 (Vishnu Puran 0.5781)
- **Original**: 20 पितृगीतान्तथैबात्र इलोकांस्ताउ्छूणु पार्थिव । श्रुत्वा तथैब भवता भाव्य तत्रादुतात्मना
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5782)
- **Original**: 21 अपि धन्य: कुले जायादस्माक मतिमान्नर: । अकुर्वन्क्‍त्तशाठ्य॑ यः पिण्डान्नो निर्वपिष्यति
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5783)
- **Original**: 22 रत्न वर्त्र॑ महायान॑ सर्वभोगादिक॑ वसु
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5784)
- **Original**: बिभवे सति विप्रेभ्यो योउस्मानुद्दिश्य दास्यति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5785)
- **Original**: 23 अन्नेन वा यथाशक्त्या काले'स्मिन्भक्तिनप्रधी: । भ्रोजयिष्यति विप्राग्र्यांस्तन्मात्रविभवों नर;
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5786)
- **Original**: 24 असमर्थोउन्नदानस्य धान्यमामं स्वशक्तित: । प्रदास्यति द्विजाग्रयेध्य: स्वल्पाल्पां बापि दक्षिणाम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5787)
- **Original**: 25 तत्राप्यसामर्थ्ययुत:. कराम्राग्रस्थितांस्तिछान्‌ । प्रणम्य ट्विजमुख्याय कस्मैचि्भूप दास्यति
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5788)
- **Original**: 26 तिलस्सप्ताप्टभिर्वापि समेत जलाखलिम्‌। भक्तिनप्रस्समुद्दिश्य भुव्यस्मार्क प्रदास्यति
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5789)
- **Original**: 27 यतः कुतश्चित्सम्प्राप्प गोभ्यो बापि गवाद्लिकम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5790)
- **Original**: अभाव प्रीणयन्नस्माउन्छुद्धायुक्त: प्रदास्यति
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5791)
- **Original**: 28 सर्वाभावे बने गत्वा कक्षमूलप्रदर्शकः । सूर्यादित्थेकपालानामिदमुच्ैव॑दिष्यति._
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5792)
- **Original**: 29 श्रीविष्णुपुराण [ आर 94 परम तृप्ति प्राप्त होती है और वे एक सहख्र युगतक शबत करते रहते हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5793)
- **Original**: गड्जीा, झतदू, यमुना, बिपाशा, सरस्वती और नैमिषारण्यस्थिता गोम्तीमें स््रान करके पितृगणका आदरपूर्वक अर्चन करनेसे मनुष्य समस्त पापोंकों नष्ट कर देता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5794)
- **Original**: पितृगण सर्वदा यह गान करते हैं कि वर्षाकाल (भाद्रपद शुक्धा त्रयोदशी) के मघानक्षत्रमें तृप्त होकर फिर माघकी अमावास्थाकों अपने पुत्र-पौत्रादिद्वारा दी गयी पुण्यतीथॉंकी जल्त्अलिसे हम कब तृप्ति स्वभ करेंगे!
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5795)
- **Original**: विशुद्ध चित्त, शुद्ध धन, प्रशास्त काल, उपर्युक्त विधि, योग्य पात्र और परम भक्ति--ये सब मनुष्यकों इच्छित फल देते हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5796)
- **Original**: है पार्थिव ! अब तुम पितृगणके गाये हुए कुछ इस्ज्रेकॉका श्रवण करो, उन्हें सुनकर तुम्हें आदरपुर्वक जैसा ही आचरण करना चाहिये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5797)
- **Original**: [पितृगण कहते हैं--] हमारे कुलमें कया कोई ऐसा मतिमान्‌ धन्य पुरुष उत्पत्र होगा जो वित्तल्लेलुपताको छोड़कर हमें पिप्डदान देगा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5798)
- **Original**: जो सम्पति होनेपर हमारे उद्देक्यसे ब्लाह्मणोंको रत्न, वस्न, ग्रान और सम्पूर्ण भोगसामग्री देगा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5799)
- **Original**: अथवा अन्न-बस््र मात्र वैभव होनेसे जो श्राद्धकालमें भक्ति-बिनम्र चित्तसे उत्तम ब्राह्मणोंकों यथाद्क्ति अन्न ही भोजन करायेगा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5800)
- **Original**: या अन्नदानमें भी असमर्थ होनेपर जो कऋषहयणगश्रेष्ठोंको कच्ा धान्य और थोड़ो-सी दक्षिणा ही देगा
- **Translation**: 

---

