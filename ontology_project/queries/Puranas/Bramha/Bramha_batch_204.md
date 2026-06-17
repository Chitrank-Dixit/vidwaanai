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

### Verse 1 (Bramha 0.4061)
- **Original**: मेरी बात सुनकर इन्द्र और बृहस्पति दोनोंको है। सब पदार्थोंके रहस्यकों जाननेमें आपके सिवा
- **Translation**: 

---

### Verse 2 (Bramha 0.4062)
- **Original**: बड़ा आश्चर्य हुआ। उन्होंने फिर मुझसे ही और कोई समर्थ नहीं है।' पूछा--' सुरश्रेष्ठ) खण्डधर्मत्व दोषका निवारण तब बृहस्पतिजीने इन्द्से कंहा-“चलकर
- **Translation**: 

---

### Verse 3 (Bramha 0.4063)
- **Original**: कैसे होगा ?' तब मैंने पुन: सोचकर कहा--' सुनो; ब्रह्मजीसे पूछो । वे ही भूत, भविष्य और बर्तमानकी
- **Translation**: 

---

### Verse 4 (Bramha 0.4064)
- **Original**: एक उपाय बताता हूँ, जो समस्त दोषोंका हारक, बातें जानते हैं। महामते! जिस कारणसे ऐसा ! समस्त सिद्धियोंका कारक और दुःखमय संसार- होता है, वह सब वे बता देंगे।' ऐसा निश्चय
- **Translation**: 

---

### Verse 5 (Bramha 0.4065)
- **Original**: सागरसे समस्त प्राणियोंका तारक है। जिनके करके वे दोनों मेरे पास आये और मुझे नमस्कार
- **Translation**: 

---

### Verse 6 (Bramha 0.4066)
- **Original**: चित्तमें संताप रहता है, उनको इसी उपायकी करके हाथ जोड़कर बोले--' भगवन्‌! किस दोषसे
- **Translation**: 

---

### Verse 7 (Bramha 0.4067)
- **Original**: शरण लेनी चाहिये। यह समस्त जीवॉकों शान्ति शचीपति इन्द्र अपने राज्यसे भ्रष्ट होते हैं? नाथ!
- **Translation**: 

---

### Verse 8 (Bramha 0.4068)
- **Original**: प्रदान करनेवाला है। वह उपाय है--गौतमी इस संदेहका निवारण कीजिये।' देवीके तटपर जाकर भगवान्‌ विष्णु और शिवकी उनका यह प्रश्न सुनकर मैंने बहुत देरतक
- **Translation**: 

---

### Verse 9 (Bramha 0.4069)
- **Original**: स्तुति करना।' यह सुनकर वे उसी समय गौतमीके विचार किया। तत्पश्चात्‌ बृहस्पतिसे कहा--' ब्रद्मन्‌!
- **Translation**: 

---

### Verse 10 (Bramha 0.4070)
- **Original**: तटपर गये और स्नान करके बड़ी प्रसन्नताके साथ खण्डधर्म नामक दोषके कारण इन्द्रको राज्यपदसे
- **Translation**: 

---

### Verse 11 (Bramha 0.4071)
- **Original**: भगवान्‌ विष्णु और शिवकी स्तुति करने लगे। च्युत होना पड़ता है। देश-काल आदिके दोषसे,
- **Translation**: 

---

### Verse 12 (Bramha 0.4072)
- **Original**: इद्धने श्रीविष्णुकी स्तुति की और बृहस्पतिने श्रीशिवकी। श्रद्धा और मन्त्रका अभाव होनेसे, यधावत्‌ दक्षिणा
- **Translation**: 

---

### Verse 13 (Bramha 0.4073)
- **Original**: . इन्र बोले--मत्स्य, कूर्म और वाराहरूप धारण न देनेसे, असत्‌ वस्तुका दान करनेसे और
- **Translation**: 

---

### Verse 14 (Bramha 0.4074)
- **Original**: करनेवाले भगवान्‌ विष्णुको बारंबार नमस्कार है। विशेषत: देवता तथा ब्राह्मणॉंकी अवहेलनाके
- **Translation**: 

---

### Verse 15 (Bramha 0.4075)
- **Original**: नरसिंहदेव तथा वामनकों भी नमस्कार है। पातकसे जो देहधारियोंका अपना धर्म खण्डित हो
- **Translation**: 

---

### Verse 16 (Bramha 0.4076)
- **Original**: हयग्रीवरूपधारी भगवान्‌को नमस्कार है। त्रिविक्रम ! जाता है, उससे अत्यधिक मानसिक संतापका
- **Translation**: 

---

### Verse 17 (Bramha 0.4077)
- **Original**: आपको नमस्कार है। श्रीराम, बुद्ध और कल्किरूप सामना करना पड़ता है तथा पदकी हानि भी
- **Translation**: 

---

### Verse 18 (Bramha 0.4078)
- **Original**: भगवान्‌कों नमस्कार है। परमेश्वर! आप अनन्त अनिवार्य हो जाती है। क्षोभपूर्ण चित्तसे किया
- **Translation**: 

---

### Verse 19 (Bramha 0.4079)
- **Original**: एवं अच्युत हैं। आपको नमस्कार है। परशुरामरूपधारी ! हुआ धर्म भी अनिष्टका हो कारण होता है। उससे
- **Translation**: 

---

### Verse 20 (Bramha 0.4080)
- **Original**: आपको नमस्कार है। मैं इन्द्र, वरुण और यम
- **Translation**: 

---

