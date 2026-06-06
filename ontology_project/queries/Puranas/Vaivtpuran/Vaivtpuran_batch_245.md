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

### Verse 1 (Vaivtpuran 13.11042)
- **Original**: सम्पन्न, श्यामकान्तिवाले, परम मनोहर, दो तुम्हारा कल्याण होगा।' श्रीकृष्णजी यह बात
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11043)
- **Original**: भुजाओंसे युक्त तथा गोपवेशधारी थे। उनके सुनकर विप्रपत्नियोंको बड़ी प्रसन्नता हुई, श्रद्धासे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11044)
- **Original**: हाथोंमें मुरली थी। उन्होंने मोरपल्लु और गुझ्ञाकी [63] सं0 ब्र0 वै0 पुराण 7
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11045)
- **Original**: ड92 + संक्षिप्त ग्रह्मवैवर्तपुराण * 440400040040400 0 0 00 0 0 0 ) ।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11046)
- **Original**: [] [न ऑऑअँअऑौऔौऑौ ऑऔऑऑऑप़पऑ मालासे आबद्ध टेढ़े मुकुट धारण कर रखे थे।! श्रीकृष्ण, विराजमान हैं, उसे यज्ञादि कर्मोंके वे रथसे तुरंत ही उतरकर श्रीहरिके चरणोंमें
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11047)
- **Original**: अनुष्ठानकी क्या आवश्यकता है? जिसने समुद्रको प्रणाम करके ब्राह्मणपत्नियोंसे बोले---आप लोग
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11048)
- **Original**: पी लिया, उसके लिये कुआँ लाँघनेमें क्‍या इस विमानपर चढ़ जाय॑ँ।' ब्राह्मणपत्नियाँ श्रीहरिको
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11049)
- **Original**: पुरुषार्थ है ?* नमस्कार करके मनोवाड्छित गोलोकमें जा ऐसा कहकर ब्राह्मणलोग उन श्रेष्ठ कामिनियोंको पहुँचीं। वे मानव-देहका त्याग करके तत्काल
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11050)
- **Original**: साथ ले हर्षपूर्वक अपने घरकों लौटे और उनके दिव्य गोपी हो गयीं। तत्पश्चात्‌ श्रीहरिने बैष्णवी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11051)
- **Original**: साथ आनन्दपूर्वक रहने लगे। उन सबका क्रौड़ामें मायाके द्वारा उनकी छायाका निर्माण करके स्वयं
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11052)
- **Original**: तथा अन्य सब कर्माँमें पहलेवाली स्त्रियोंकी ही उन्हें ब्राह्मणोंके घरोंमें भेज दिया। ब्राह्मण
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11053)
- **Original**: अपेक्षा अधिक प्रेम तथा उदारभाव प्रकट होता लोग अपनी पत्नियोंके लिये मन-ही-मन बहुत
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11054)
- **Original**: था; परंतु मायाशक्तिसे प्रभावित होनेके कारण उद्ठिग्र थे और सब ओर उनकी खोज कर रहे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11055)
- **Original**: ब्राह्मणतोग उसका अनुमान नहीं कर पाते थे। थे। इसी समय रास्तेमें उन्हें अपनी पत्रियाँ उधर सनातन पूर्णब्रह्म नारायणस्वरूप श्रीकृष्ण दिखायी दीं। उन्हें देखकर सब ब्राह्मणोंक मुख
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11056)
- **Original**: बलराम तथा ग्वालबालॉके साथ शीघ्र ही अपने और नेत्र प्रसन्नतासे खिल उठे। सम्पूर्ण अड्ज घरको चले गये। इस प्रकार मैंने श्रीहरिका सम्पूर्ण पुलकित हो गये और वे विनयपूर्वक उनसे बोले।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11057)
- **Original**: उत्तम माहात्म्य कह सुनाया। इसे मैंने पूर्वकालमें ब्राह्मणोंने कहा--अहो! तुम सब लोग
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11058)
- **Original**: अपने पिता धर्मके मुखसे सुना था। नारद! अब परम धन्य हो; क्‍योंकि तुमने साक्षात्‌ परमेश्वरके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11059)
- **Original**: तुम और क्‍या सुनना चाहते हो? दर्शन किये हैं। हमारा जीवन व्यर्थ है। हम
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11060)
- **Original**: नारदजीने पूछा--ऋषीन्द्र! किस पुण्यके लोगोंका वेदपाठ भी निरर्थक है। वेद और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11061)
- **Original**: प्रभावसे उन ब्राह्मणपत्रियोंको ऐसी गति प्राप्त पुराणमें सर्वत्र विद्वानोंद्वारा श्रीहरिकों ही समस्त
- **Translation**: 

---

