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

### Verse 1 (Bramha 0.4461)
- **Original**: भलीभाँति जाननेवाले सनकादि मुनि भी जिनके करनेसे वही कर्म अनन्त फल देनेबाला होता है
- **Translation**: 

---

### Verse 2 (Bramha 0.4462)
- **Original**: तत्त्वको ठौक-ठीक नहीं जानते, वे सम्पूर्ण अभीष्ट गृहस्थ पुरुषके सब कार्योंमें यहाँ पतली ही
- **Translation**: 

---

### Verse 3 (Bramha 0.4463)
- **Original**: बस्तुओंके दाता अन्धकासुरविनाशक पार्वतीपति सहायता करनेवाली है। उसके सहयोग बिना
- **Translation**: 

---

### Verse 4 (Bramha 0.4464)
- **Original**: भगवान्‌ शिव हमपर प्रसन्न हों। जब पाप, छोटे-से-छोटे कार्य भी सिद्ध नहों होते। नाथ!
- **Translation**: 

---

### Verse 5 (Bramha 0.4465)
- **Original**: दरिद्रता, लोभ, याचना, मोह और विपत्ति आदि पुरुष अकेले जो कर्म करता है, उसका आधा अनन्त सांसारिक दु:ख प्रकट हुए, उनका प्रभाव फल हो उसे मिलता है। किंतु पत्रीके साथ जो
- **Translation**: 

---

### Verse 6 (Bramha 0.4466)
- **Original**: फैलने लगा और उनसे सम्पूर्ण जगत्‌ व्याप्त हो कर्म किया जाता है, उसका पूरा फल पुरुषको
- **Translation**: 

---

### Verse 7 (Bramha 0.4467)
- **Original**: गया, तब यह सब अवस्था देखकर देवेश्वर प्राप्त होता है। सुना जाता है-- दण्डकारण्यमें
- **Translation**: 

---

### Verse 8 (Bramha 0.4468)
- **Original**: महादेवजी बड़े चकित हुए और देवी पार्वतीसे सरिताओमें श्रेष्ठ गौतमी गड्जा बहती हैं। वे समस्त
- **Translation**: 

---

### Verse 9 (Bramha 0.4469)
- **Original**: बोले--'लोकेश्वरि! यह सम्पूर्ण जगत्‌ नष्ट होना पापोंका नाश करनेवाली तथा सम्पूर्ण अभिलषित
- **Translation**: 

---

### Verse 10 (Bramha 0.4470)
- **Original**: चाहता है। तुम इसकी रक्षा करो। लोकमाता वस्तुओंको देनेवाली हैं। अत: मेंरे साथ यहाँ चलिये
- **Translation**: 

---

### Verse 11 (Bramha 0.4471)
- **Original**: उमा! तुम सबको शरण देनेवाली, उत्तम ऐश्वर्यसे और महान्‌ फलदायक पुण्यकर्मका अनुष्ठान कीजिये।
- **Translation**: 

---

### Verse 12 (Bramha 0.4472)
- **Original**: युक्त, परम कल्याणमयी तथा सम्पूर्ण जगत्‌की इससे आप संग्राममें अपने शत्रुओंका संहार करके ' प्रतिष्ठा हो। बरदायिनि! तुम्हारी जय हो। तुम महान्‌ सुखके भागी होंगे। भोग, समाधि, परम मुक्ति, स्वाहा, स्वधा, स्वस्ति, * श्रुतमस्ति पुनक्षेद॑ स्त्रियों याश्व पतिक्रता:। ता एबं सर्व॑ जानन्ति धरृ्त ताभिश्वराचरम्‌
- **Translation**: 

---

### Verse 13 (Bramha 0.4473)
- **Original**: (129। 54) 7 अज्ञात्वेकगु्ण कर्म फल दास्यति कर्मिण: । झ्ात्या शवगुण॑ तत्स्याद्‌ भार्यया च तदक्षयम्‌
- **Translation**: 

---

### Verse 14 (Bramha 0.4474)
- **Original**: (129। 59)
- **Translation**: 

---

### Verse 15 (Bramha 0.4475)
- **Original**: तपसस्‍तीर्थ, इद्तीर्थ और थृषाकपि एवं अब्जक-तीर्थकी महिया 3219 अनादि सिद्धि, वाणी, बुद्धि तथा अजर-अमर
- **Translation**: 

---

### Verse 16 (Bramha 0.4476)
- **Original**: मेरा अपमान किया है, उसका नाश करनेपर ही हो। मेरी आज्ञाके अनुसार तीनों लोकोंमें विद्या
- **Translation**: 

---

### Verse 17 (Bramha 0.4477)
- **Original**: मैं अपना नया जन्म मानूँगा। विजय और आदि रूपसे तुम रक्षा करती हो। तुमने ही
- **Translation**: 

---

### Verse 18 (Bramha 0.4478)
- **Original**: लक्ष्मीकी अपेक्षा कीर्ति ही श्रेष्ठ है।' यह सुनकर प्रकृतिरूपसे इस विचित्र त्रिलोकीको सृष्टि की
- **Translation**: 

---

### Verse 19 (Bramha 0.4479)
- **Original**: शिवने इन्द्रसे कहा--'अकेले मेरे द्वारा तुम्हारे है।' शंकरजीके यों कहनेपर उनकी प्राणवल्लभा ' शत्रुका वध नहीं हो सकता। अत: तुम अविनाशी भगवती उमा उनका आलिज्भन करके प्रेमालाप
- **Translation**: 

---

### Verse 20 (Bramha 0.4480)
- **Original**: भगवान्‌ जनार्दनकी भी आराधना करो। शची करने लगीं और थककर भगबवान्‌के आधे
- **Translation**: 

---

