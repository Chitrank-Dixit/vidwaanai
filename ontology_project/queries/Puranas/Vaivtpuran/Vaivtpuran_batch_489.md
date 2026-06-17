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

### Verse 1 (Vaivtpuran 28.4186)
- **Original**: जो मनुष्य प्रात: उठकर निरन्तर इस ' यमाष्टक ' का धर्मात्मा, संयमी, जितेन्द्रिय और जीवबोंके लिये
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.4187)
- **Original**: पाठ करता है, उसे यमराजसे भय नहीं होता और कर्मफल देनेको उद्यत हैं, उन भगवान्‌ यमको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.4188)
- **Original**: उसके सारे पाप नष्ट हो जाते हैं । यदि महान्‌ पापी मैं प्रणाम करती हूँ। जो अपनी आत्मामें रमण
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.4189)
- **Original**: व्यक्ति भी भक्तिसे सम्पन्न होकर निरन्तर इसका पाठ करनेवाले, सर्वज्ञ, पुण्यात्मा पुरुषोंके मित्र तथा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.4190)
- **Original**: करता है तो यमराज अपने कायबव्यूहसे निश्चित ही पापियोंके लिये कष्टप्रद हैं, उन 'पुण्यमित्र' नामसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.4191)
- **Original**: उसकी शुद्धि कर देते हैं। (अध्याय 27-28) # 74 2+50200 नरककुण्डों और उनमें जानेवाले पापियों तथा पापोंका वर्णन दल नल नारायण कहते हैं--नारद!
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.4192)
- **Original**: प्रभावसे उन स्वरगॉमें जाते हैं। नरकोंमें जाना कोई रबिनन्दन धर्मराजने सावित्रीकों विधिपूर्वक मनुष्य नहीं चाहते, परंतु अशुभकर्म-विपाक विष्णुका महामन्त्र देकर 'अशुभकर्मका विपाक'
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.4193)
- **Original**: उन्हें नरकमें जानेके लिये विवश कर देते हैं। कहना आरम्भ किया। नरकोंके नाना प्रकारके कुण्ड हैं। विभिन्न पुराणोंके धर्मराजने कहा--पतित्रते! मानव शुभकर्मके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.4194)
- **Original**: भेदसे इनके नामोंके भी भेद हो गये हैं। ये विपाकसे नरकमें नहीं जा सकता। नरकमें जानेमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.4195)
- **Original**: सभी कुण्ड बड़े ही विस्तृत हैं। पापियोंको कारण है--अशुभकर्मका विपाक। अतएवं अब
- **Translation**: 

---

### Verse 11 (Vaivtpuran 28.4196)
- **Original**: दुःखका भोग कराना हो इन कुण्डोंका प्रयोजन मैं अशुभकर्मका विपाक बतलाता हूँ, सुनो। नाना
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.4197)
- **Original**: है। वत्से! ये भयंकर कुण्ड अत्यन्त भयावह तथा प्रकारके स्वर्ग हैं। प्राणी अपने-अपने करमोके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.4198)
- **Original**: कुत्सित हैं। इनमें छियासी कुण्ड तो प्रसिद्ध हैं, *+तप्सा धर्ममाराध्य पुष्के. भास्कर: पुरा। धर्माशं य॑ सुतं प्राप धर्मराजं॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.4199)
- **Original**: समता सर्वभूतेषु यस्यसर्वस्य साक्षिण: । अतो यत्नाम शमन इति त॑ प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.4200)
- **Original**: येनान्तश्वल कृतो विश्वे सर्वेषां जीविनां परम्‌ । कर्मानुरूपकालेन त॑ कृतान्त॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.4201)
- **Original**: बिर्भर्ति दण्ड दण्डाय पापिनां शुद्धिहितवे। नमामि त॑ दण्डधर यः शास्ता सर्वकर्मणाम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.4202)
- **Original**: विश्व यः कलयत्येव सर्वायुश्षापि सन्ततम्‌ । अतीब दुर्निवा्य॑ च त॑ काल॑ प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.4203)
- **Original**: तपस्थी वैष्णवों धर्मी संयमी संजितेन्द्रिय:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.4204)
- **Original**: जीविनां कर्मफलद॑ त॑ यम प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.4205)
- **Original**: स्वात्मारामश्ल॒ सर्वज्ञो मित्र पुण्यकृतां भवेत्‌ । पापिनां क्‍लेशदों यश्व पुण्यमित्रं नमास्यहम्‌
- **Translation**: 

---

