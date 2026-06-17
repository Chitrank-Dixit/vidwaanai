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

### Verse 1 (Vaivtpuran 4.8556)
- **Original**: गर्भवासकारक, सदा तत्त्वज्ञाका छेदक और जा पहुँचीं। वहाँ उन्होंने गणेशको देखा, जिनकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8557)
- **Original**: संशयोंका उद्गमस्थान है। इसलिये महाभागे! मेरी नयी जवानी थी; जो अत्यन्त सुन्दर, शुद्ध और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8558)
- **Original**: ओरसे मन लौटा लो और किसी अन्य पतिकी पीताम्बर धारण किये हुए थे; जिनके सारे शरीरमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8559)
- **Original**: तलाश करो। गणेशके ऐसे वचन सुनकर तुलसीको चन्दनकी खौर लगी थी; जो रत्नोंक आभूषणोंसे क्रोध आ गया। तब वह साध्वी गणेशकों शाप विभूषित थे; सुन्दरता जिनके मनका अपहरण [ देते हुए बोली--'तुम्हारा विवाह होगा।' यह नहीं कर सकती; जो कामनारहित, जितेन्द्रियोंमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8560)
- **Original**: सुनकर शिव-तनय सुरश्रेष्ठ गणेशने भी तुलसीको सर्वश्रेष्ठ और योगीन्द्रोंके गुरु-के-गुरु हैं तथा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8561)
- **Original**: शाप दिया--'देवि! तुम निस्संदेह असुरद्वारा ग्रस्त मन्द-मन्द मुस्कराते हुए जन्म, मृत्यु और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8562)
- **Original**: होओगी। तत्पश्चात्‌ महापुरुषोंके शापसे तुम वृक्ष बुढ़ापाका नाश करनेवाले श्रीकृष्णके चरणकमलॉका
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8563)
- **Original**: हो जाओगी।' नारद! महातपस्वी गणेश इतना ध्यान कर रहे थे; उन्हें देखते ही तुलसीका मन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8564)
- **Original**: कहकर चुप हो गये। उस शापको सुनकर गणेशकी ओर आकर्षित हो गया। तब तुलसी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8565)
- **Original**: तुलसीने फिर उस सुरश्रेष्ठ गणेशकी स्तुति की। उनसे लम्बोदर तथा गजमुख होनेका कारण
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8566)
- **Original**: तब प्रसन्न होकर गणेशने तुलसीसे कहा। पूछकर उनका उपहास करने लगी। ध्यान-भड़
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8567)
- **Original**: गणेश बोले--मनोरमे ! तुम पुष्पोंकी सारभूता होनेपर गणेशजीने पूछा-“वत्से! तुम कौन हो ?
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8568)
- **Original**: होओगी और कलांशसे स्वयं नारायणकी प्रिया किसको कन्या हो? यहाँ तुम्हारे आनेका क्या
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8569)
- **Original**: बनोगी। महाभागे! यों तो सभी देवता तुमसे प्रेम कारण है? माता! यह मुझे बतलाओ; क्योंकि
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8570)
- **Original**: करेंगे, परंतु श्रीकृष्णे लिये तुम विशेष प्रिय शुभे! तपस्वियोंका ध्यान भड्भ करना सदा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8571)
- **Original**: होओगी। तुम्हारे द्वारा की गयी पूजा मनुष्योंके पापजनक तथा अमड्गलकारी होता है। शुभे!
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8572)
- **Original**: लिये मुक्तिदायिनी होगी और मेरे लिये तुम सर्वदा श्रीकृष्ण कल्याण करें, कृपानिधि विप्रका विनाश
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8573)
- **Original**: त्याज्य रहोगी। तुलसीसे यों कहकर सुरश्रेष्ठ गणेश करें और मेरे ध्यान-भज्जसे उत्पन्न हुआ दोष
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8574)
- **Original**: पुनः तप करने चले गये। वे श्रीहरिकी आराधनामें तुम्हारे लिये अमड्गलकारक न हो।' व्यग्र होकर बदरीनाथके संनिकट गये। इधर इसपर तुलसीने कहा--प्रभो! मैं धर्मात्मजको
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8575)
- **Original**: तुलसीदेवी दुःखिते हृदयसे पुष्करमें जा पहुँची
- **Translation**: 

---

