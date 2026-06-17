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

### Verse 1 (Bramha 0.8501)
- **Original**: धीर पुरुष मनको बशमें रखनेसे क्रोधपर और नहीं देता।* क्षर और अक्षर-ये पुरुषके दो भेद हैं।
- **Translation**: 

---

### Verse 2 (Bramha 0.8502)
- **Original**: संकल्पका त्याग करनेसे कामपर विजय पाता है। सम्पूर्ण भूत तो क्षर (विनाशी) हैं और दिव्य सत्त्वगुणका सेवन करनेसे वह निद्राका नाश कर अमृतस्बरूप चेतन आत्मा अक्षर (अविनाशी) है।
- **Translation**: 

---

### Verse 3 (Bramha 0.8503)
- **Original**: सकता है। धैर्यके द्वारा योगी शिश्त और उदरकी नौ द्वारॉवाले पुर (शरीर)-का निर्माण करके जितेन्द्रिय
- **Translation**: 

---

### Verse 4 (Bramha 0.8504)
- **Original**: रक्षा करे। नेत्रोंकी सहायतासे हाथ और पैरोंकी रक्षा तथा नियमपरायण हंस (आत्मा) उसमें वास करता
- **Translation**: 

---

### Verse 5 (Bramha 0.8505)
- **Original**: करे। मनके द्वाण नेत्र और कानोंकी तथा कर्मके द्वारा है। समस्त चराचर भूतोंका आत्मा ऐसा ही है।
- **Translation**: 

---

### Verse 6 (Bramha 0.8506)
- **Original**: मन और बाणीकी रक्षा करे। प्रमादके त्यागसे अजन्मा आत्मा भाँति-भाँतिके विकल्पोंका त्याग
- **Translation**: 

---

### Verse 7 (Bramha 0.8507)
- **Original**: भवका और विद्ठान्‌ पुरुषोंक सेवनसे दम्भका और शरीरोंका संचय करता है, इसलिये पारदर्शी
- **Translation**: 

---

### Verse 8 (Bramha 0.8508)
- **Original**: त्याग करे[
- **Translation**: 

---

### Verse 9 (Bramha 0.8509)
- **Original**: इस प्रकार योगके साधकको * सर्वतःपाणिपाद॑ तत्सर्वतो5क्षिशिरोमुखम्‌ । सर्वत:श्रुतिमललोके . सर्वमाबृत्य तिष्ठति
- **Translation**: 

---

### Verse 10 (Bramha 0.8510)
- **Original**: तदेवाणोरणुतरं तन्‍्महद्धवो.. महत्तरम्‌। तदन्त: सर्वभूतानां धुवं॑ तिप्ठम दृश्यते
- **Translation**: 

---

### Verse 11 (Bramha 0.8511)
- **Original**: 30-31)
- **Translation**: 

---

### Verse 12 (Bramha 0.8512)
- **Original**: क्रोधं शमेन जयति काम संकल्पवर्जनातू। सत्तसंसेवनाद्धीरों निद्रामुच्छेत्तुमरईति
- **Translation**: 

---

### Verse 13 (Bramha 0.8513)
- **Original**: धृत्या शिश्रोदरं॑ रक्षेत्पाणिपाद च चक्षुपा। चक्लु; श्रोत्रं च मत्रसा मनो वाच॑ं चर कर्मणा
- **Translation**: 

---

### Verse 14 (Bramha 0.8514)
- **Original**: अप्रमादाद्‌ भय॑ जछाद्‌ दम्भं प्राज़ोपसेवनात्‌
- **Translation**: 

---

### Verse 15 (Bramha 0.8515)
- **Original**: (235। 40--42)
- **Translation**: 

---

### Verse 16 (Bramha 0.8516)
- **Original**: डण्8 » संक्षिप्त झह्पुराण + आलस्य छोड़कर इन योग-सम्बन्धी दोषोंको
- **Translation**: 

---

### Verse 17 (Bramha 0.8517)
- **Original**: मलिनता दूर होकर इनमें स्वच्छता आ जाती हैं। जौतनेका प्रयत्न करना चाहिये। वह आग्नि,
- **Translation**: 

---

### Verse 18 (Bramha 0.8518)
- **Original**: फिर अन्तःकरणमें ब्रह्मका साक्षात्कार हो जाता ब्राह्मण तथा देवताओंको सदा प्रणाम करे। मनपर , है। योगी धूमरहित अग्नि, दीप्तिमान्‌ सूर्य तथा प्रभाव डालनेवाली हिंसायुक्त उददण्डतापूर्ण वाणी
- **Translation**: 

---

### Verse 19 (Bramha 0.8519)
- **Original**: आकाशमें चमकती हुई बिजलीकी भाँति आत्माका न बोले। तेजोमय ब्रह्म ही वीर्य (सबका आदि ! हृदयदेशमें दर्शन करता है। सब कुछ आत्मामें है कारण) है, यह सम्पूर्ण जगत्‌ उसीका कार्य है।
- **Translation**: 

---

### Verse 20 (Bramha 0.8520)
- **Original**: और आत्मा सबमें व्यापक है; इसलिये वह सर्वत्र समस्त चराचर जगत्‌ उस भब्रह्मके ही ईक्षण
- **Translation**: 

---

