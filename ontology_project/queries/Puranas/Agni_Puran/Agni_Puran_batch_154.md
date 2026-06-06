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

### Verse 1 (Agni Puran 0.3061)
- **Original**: आत्मा (शरीर)-में तथा “श' सहित वकका (दाहिनी जाँघ)-में, 'ड' सहित दारुकका दाहिने
- **Translation**: 

---

### Verse 2 (Agni Puran 0.3062)
- **Original**: हड्डीमें न्‍्यास करे। 'ष” सहित श्वेतका मज्जामें, घुटनेमें तथा 'ढ' सहित अर्द्धजलेश्वरका पिण्डलीमें
- **Translation**: 

---

### Verse 3 (Agni Puran 0.3063)
- **Original**: 'स' सहित भृगुका शुक्र एवं धातुमें, “ह” सहित न्यास करें। “ण' सहित उमाकान्तका दाहिने
- **Translation**: 

---

### Verse 4 (Agni Puran 0.3064)
- **Original**: नकुलीशका प्राणमें तथा “क्ष' सहित संबर्तका पैरकी अन्जुलियोंमें, “त' सहित आषाढ़ीका नितम्बमें,
- **Translation**: 

---

### Verse 5 (Agni Puran 0.3065)
- **Original**: पश्चकोशोंमें न्यास करना चाहिये। “हीं” बीजसे 'थ' सहित दण्डीका वाम ऊरु (बायीं जाँघ)-में
- **Translation**: 

---

### Verse 6 (Agni Puran 0.3066)
- **Original**: रुद्रशक्तियोंका पूजन करके उपासक सम्पूर्ण तथा 'द” सहित भिदका बायें घुटनेमें न्यास करे।
- **Translation**: 

---

### Verse 7 (Agni Puran 0.3067)
- **Original**: मनोरथोंको प्राप्त कर लेता है
- **Translation**: 

---

### Verse 8 (Agni Puran 0.3068)
- **Original**: इस प्रकार आदि आस्नेय महापृराणमें 'मालिती-मनत्र आदिके न्यासका वर्णत” कामका एक साँ पैतालीसवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 9 (Agni Puran 0.3069)
- **Original**: 145 # नी एक सौ छियालीसवाँ अध्याय त्रिखण्डी-मन्त्रका वर्णन, पीठस्थानपर पूजनीय शक्तियों तथा आठ अष्टक देवियोंका कथन भगवान्‌ महेश्वर कहते हैं-- स्कन्द! अब मैं
- **Translation**: 

---

### Verse 10 (Agni Puran 0.3070)
- **Original**: (40 नमश्चामुण्डे ब्रह्माणि अघोरे अमोधे बरदे ब्रह्मा, विष्णु तथा महेश्वरसे सम्बन्ध रखनेवाली
- **Translation**: 

---

### Verse 11 (Agni Puran 0.3071)
- **Original**: विच्चे स्वाहा। 30 नमश्चामुण्डे माहेश्वरि अघोरे त्रिखण्डीका वर्णन करूँगा
- **Translation**: 

---

### Verse 12 (Agni Puran 0.3072)
- **Original**: अमोधे बरदे विच्चे स्वाहा। 30 नमश्लामुण्डे * 3» नप्तो भगवते रुद्राय नमः। नमश्चामुण्डे
- **Translation**: 

---

### Verse 13 (Agni Puran 0.3073)
- **Original**: कौमारि अघोरे अमोधे बरदे विच्चे स्वाहा। 30 नमश्लवाकाशमातृणां. सर्वकामार्थसाथनीनाम- नपश्चामुण्डे वैष्णवि अघोरे अमोधे बरदे विच्चे जरामरीणां सर्वव्राप्रतिहतगतीनां स्वरूपपरिवर्तिनीनां
- **Translation**: 

---

### Verse 14 (Agni Puran 0.3074)
- **Original**: स्वाहा। 30 नमश्लामुण्डे बाराहि अघोरे अमोधे सर्वसत्त्ववशीकरणोत्सादनोन्मूलनसमस्तकर्म-
- **Translation**: 

---

### Verse 15 (Agni Puran 0.3075)
- **Original**: बरदे विच्ये स्वाहा। 30 नमश्चामुण्डे इन्द्राणि प्रवृत्तानां सर्वमातृगुढ्ां हृदयं परमसिद्ध॑ परकर्मच्छेदर्न
- **Translation**: 

---

### Verse 16 (Agni Puran 0.3076)
- **Original**: अघोरे अमोघे बरदे विच्छे स्वाहा । 34 नमश्चामुण्डे परमसिद्धिकरं मातृणां वचन शुभम्‌।' इस
- **Translation**: 

---

### Verse 17 (Agni Puran 0.3077)
- **Original**: चण्डि अघोरे अमोधे वरदे विच्चे स्वाहा। ब्रह्मखण्डपदमें रुद्रमन्त्र-सम्बन्धी एक सौं इक्कीस
- **Translation**: 

---

### Verse 18 (Agni Puran 0.3078)
- **Original**: 50 नमश्लामुण्डे ईशानिं अघोरे अमोधे बरदे अक्षर हैं
- **Translation**: 

---

### Verse 19 (Agni Puran 0.3079)
- **Original**: विच्चे स्वाहा।' यह यथोचित अक्षरवाले पदोंका (अब विष्णुखण्डपद बताया जाता है--)
- **Translation**: 

---

### Verse 20 (Agni Puran 0.3080)
- **Original**: दूसरा मन्त्रखण्ड है, जो 'विष्णुखण्डपद' कहा
- **Translation**: 

---

