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

### Verse 1 (Vaivtpuran 13.3029)
- **Original**: घोर तपस्याक्े द्वारा आराधना करके इन छायी रहती थी। उसे देखकर दुराचारी रावणका
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.3030)
- **Original**: जगदीश्वरको पतिरूपमें प्राप्त किया था। वह हृदय विकारसे संतप्त हो गया। वह बेदबतीको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.3031)
- **Original**: साक्षात्‌ रमा थी। सीतारूपसे विराजमान उस हाथसे खींचकर उसका श्रृंगार करनेको उद्यत
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.3032)
- **Original**: सुन्दरी देवीने बहुत दिनोंतक भगवान्‌ श्रीरामके हुआ। रावणकी इस कुचेष्टाकों देखकर उस
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.3033)
- **Original**: साथ सुख भोगा। उसे पूर्वजन्मकी बातें स्मरण साध्वीका मन क्रोधसे भर गया। उसने रावणको
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.3034)
- **Original**: थीं, फिर भी पूर्वस्रमयमें तपस्यासे जो कष्ट हुआ अपने तपोबलसे इस प्रकार स्तम्भित कर दिया
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.3035)
- **Original**: था, उसपर उसने ध्यान नहीं दिया। वर्तमान कि वह जडबत्‌ होकर हाथों एवं पैरोंसे निश्वेष्ट
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.3036)
- **Original**: सुखके सामने उसने सम्पूर्ण पूर्वक्लेशोंकी स्मृतिका हो गया। कुछ भी कहने-करनेकी उसमें क्षमता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.3037)
- **Original**: त्याग कर दिया था। श्रीराम परम गुणी, समस्त नहीं रह गयी। ऐसी स्थितिमें उसने मन-ही-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.3038)
- **Original**: सुलक्षणोंसे सम्पन्न, रसिक, शान्त-स्वभाव, अत्यन्त मन उस कमललोचना देवीके पास जाकर उसका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.3039)
- **Original**: कमनीय तथा स्त्रियोंके लिये साक्षात्‌ कामदेबके मानस स्तवन किया। शक्तिकी उपासना विफल
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.3040)
- **Original**: समान सुन्दर एवं श्रेष्ठटम देवता थे। वेदवतीने नहीं होती, इसे सिद्ध करनेके विचारसे देवी ऐसे मनो$भिलषित स्वामीको प्राप्त किया। कुछ वेदवती रावणपर संतुष्ट हो गयी और परलोकमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.3041)
- **Original**: कालके पश्चात्‌ रघुकुलभूषण, सत्यसंध भगवान्‌ उसकी स्तुतिका फल देना उन्होंने स्वीकार कर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.3042)
- **Original**: श्रीराम पिताके सत्यकी रक्षा करनेके लिये बनमें लिया। साथ ही उसे यह शाप दे दिया--'दुरात्मन्‌!
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.3043)
- **Original**: पधारे। वे सीता और लक्ष्मणके साथ समुद्रके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.3044)
- **Original**: + प्रकृतिखण्ड « 149 56 4 6 6
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.3045)
- **Original**: 6 5 9 5 5 8 8 8 8 87 ीॉी42(4(4(2।।4/4/28 2 6 82 84
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.3046)
- **Original**: / समीप ठहरे थे। वहाँ ब्राह्मणरूपधारी क्‍ गया। यह मारीच पूर्वजन्ममें बैकुण्ठधामके द्वारपर उनकी भेंट हुई। भगवान्‌ रामको दुःखी देखकर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.3047)
- **Original**: वहाँके द्वारणल जब और विजयका किंकर था विप्ररूपधारी अग्नरिका मन संतप्त हों उठा। तब
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.3048)
- **Original**: तथा वहीँ रहता था। वह बड़ा बलवान था। सर्वथा सत्यवादी उन अग्रिदेवने सत्यप्रेमी भगवान्‌
- **Translation**: 

---

