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

### Verse 1 (Bramha 0.6161)
- **Original**: जो युद्ध होगा, उसमें फिर सम्मिलित होऊँगा। दैत्यके मारे जानेसे गोप और गोपियॉकों बड़ी
- **Translation**: 

---

### Verse 2 (Bramha 0.6162)
- **Original**: धरणीधर! उग्रसेनकुमार कंस जब अपने अनुचरोंसहित प्रसन्नता हुई। वे श्रीकृष्णों सब ओरसे घेरकर
- **Translation**: 

---

### Verse 3 (Bramha 0.6163)
- **Original**: मारा जायगा, उस समय पृथ्वीका भार आप बहुत आश्चर्ययकित हो उनकी स्तुति करने लगे। इसी
- **Translation**: 

---

### Verse 4 (Bramha 0.6164)
- **Original**: कुछ उतार देंगे। उसके बाद भी राजाओंके साथ समय देवर्षि नारद बड़ी उतावलीके साथ बहाँ
- **Translation**: 

---

### Verse 5 (Bramha 0.6165)
- **Original**: आपके अनेक युद्ध हमें देखनेको मिलेंगे। गोविन्द! आये और बादलोंमें स्थित हो गये। केशौको मारा
- **Translation**: 

---

### Verse 6 (Bramha 0.6166)
- **Original**: आपने देवताओंका बहुत बड़ा कार्य सिद्ध किया और गया देख ये हर्षसे फूले नहीं समाते थे।
- **Translation**: 

---

### Verse 7 (Bramha 0.6167)
- **Original**: मुझे भी बहुत आदर दिया । आपका कल्याण हो, अब नारदजी बोले--जगन्नाथ ! आपको धन्यवाद
- **Translation**: 

---

### Verse 8 (Bramha 0.6168)
- **Original**: मैं जाता हूँ। है। अच्युत! आपने खेल-खेलमें ही इस केशोको
- **Translation**: 

---

### Verse 9 (Bramha 0.6169)
- **Original**: यों कहकर नारदजी चले गये। तब मार डाला। यह देवताओंको बड़ा क्लेश दिया करता ' श्रीकृष्ण अत्यन्त सौम्यभावसे ग्वालोंके साथ गोकुलमें था। मधुसूदन ! आपने इस अवतारमें जो-जो महान्‌
- **Translation**: 

---

### Verse 10 (Bramha 0.6170)
- **Original**: चले आये। मकर ,00 अक्ूरका नन्दगाँवमें जाना, श्रीराम-कृष्णकी मथुरायात्रा, गोपियोंकी कथा, अक्ूरको यमुनामें भगवहर्शन, उनके द्वारा भगवान्‌की स्तुति, मथुरा-प्रवेश, रजक-वध और मालीपर कृपा व्यासजी कहते हैं-- अक्रूरजी शीघ्र चलनेयाले
- **Translation**: 

---

### Verse 11 (Bramha 0.6171)
- **Original**: मैं विकसित कमलके समान नेत्रोंवाले भगवान्‌ रथपर चढ़कर मधथुरासे निकले और श्रीकृष्णके ' विष्णुके मुखका दर्शन करूँगा। जो स्मरण अथवा दर्शनका लोभ लेकर नन्दगाँवकी ओर चल दिये।
- **Translation**: 

---

### Verse 12 (Bramha 0.6172)
- **Original**: ध्यानमें आकर भी मनुष्यके सारे पाप हर लेता है, मार्गममें सोचने लगे-“अहा! मुझसे बढ़कर
- **Translation**: 

---

### Verse 13 (Bramha 0.6173)
- **Original**: वही कमल-सदृश नेत्रोंवाला श्रीविष्णुका सुन्दर सौभाग्यशाली कोई नहीं है, क्योंकि आज मैं
- **Translation**: 

---

### Verse 14 (Bramha 0.6174)
- **Original**: मुख आज मुझे देखनेको मिलेगा। जिससे सम्पूर्ण अंशसहित अबतीर्ण हुए साक्षात्‌ भगवान्‌ विष्णुका
- **Translation**: 

---

### Verse 15 (Bramha 0.6175)
- **Original**: बेद और बेदाज़ोंका प्रादुर्भाव हुआ है तथा जो मुख देखूँगा। आज मेरा जन्म सफल हुआ और
- **Translation**: 

---

### Verse 16 (Bramha 0.6176)
- **Original**: देवताओंके लिये सर्वश्रेष्ठ आश्रय है, भगवान्‌के आनेवाला प्रभात बहुत ही सुन्दर होगा। क्योंकि
- **Translation**: 

---

### Verse 17 (Bramha 0.6177)
- **Original**: उसी मुखका आज मैं दर्शन करूँगा।* ब्रह्मा, इन्द्र, * चित्तयामास चाक्ररों नास्ति धन्यतरों मया। सो5हमंशाबतीर्णस्य मुख द्रक्ष्यामि चक्रिण:
- **Translation**: 

---

### Verse 18 (Bramha 0.6178)
- **Original**: अप्य मे सफल जन्म सुप्रभाता व मे तिशा। यदुष्रिद्वाब्जपत्राक्ष विष्णोद्रक्ष्यास्पह॑ मुखम्‌
- **Translation**: 

---

### Verse 19 (Bramha 0.6179)
- **Original**: पार्प हरति यत्पुंसां स्मृ्त संकल्पतामयम्‌। तत्पुण्डरीकतपर् दिष्णो्द्रक्ष्यास्पह मुखम्‌ #
- **Translation**: 

---

### Verse 20 (Bramha 0.6180)
- **Original**: निर्जमुक्ष यतो वेदा वेदाबड्रान्यखिलानि थ। द्रक्ष्यामि यत्पर॑ धाम देवानां भगवन्मुखम्‌
- **Translation**: 

---

