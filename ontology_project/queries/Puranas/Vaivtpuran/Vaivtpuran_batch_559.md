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

### Verse 1 (Vaivtpuran 39.8199)
- **Original**: कल्याणके कारण, पार्वतीके आराध्य और शान्तरूप भाँति ही मान्य है; किंतु गुरुपन्नी उससे भी हैं; अपने गुरुदेव उन शिवकी शरणमें जाओ। अधिक पूज्या है। देवताके रुष्ट होनेपर गुरु रक्षा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 39.8200)
- **Original**: तुम्हारे इष्टदेव जो गोलोकनाथ भगवान्‌ श्रीकृष्ण कर लेते हैं, परंतु गुरुके क्रुद्ध होनेपर कोई भी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.8201)
- **Original**: हैं, वे ही अपने अंशसे शिवका रूप धारण करके रक्षा नहीं कर सकता। इसलिये गुरु ही ब्रह्मा,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.8202)
- **Original**: तुम्हारे गुरु हुए हैं, अतः उन्हींकी शरण ग्रहण गुरु ही विष्णु, गुरु ही महेश्वरदेव, गुरु ही परब्रह्म
- **Translation**: 

---

### Verse 5 (Vaivtpuran 39.8203)
- **Original**: करो। बेटा! समस्त प्राणियोंमें श्रीकृष्ण आत्मा और ब्राह्मणोंसे भी बढ़कर प्रिय हैं। गुरु ही ज्ञान
- **Translation**: 

---

### Verse 6 (Vaivtpuran 39.8204)
- **Original**: हैं, शिव ज्ञान हैं, मैं मन हूँ और विष्णुकी सारी देते हैं और वह ज्ञान हरि-भक्ति उत्पन्न करता
- **Translation**: 

---

### Verse 7 (Vaivtpuran 39.8205)
- **Original**: शक्तियोंसे सम्पन्न प्रकृति प्राण है। जो ज्ञानदाता, है। इस प्रकार जो हरि-भक्ति प्रदान करनेवाला
- **Translation**: 

---

### Verse 8 (Vaivtpuran 39.8206)
- **Original**: ज्ञानस्वरूप, ज्ञानके कारण, सनातन मृत्युको है, उससे बढ़कर बन्धु दूसरा कौन है? अज्ञानरूपी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 39.8207)
- **Original**: जीतनेवाले तथा कालके भी काल हैं; उन गुरुकौ अन्धकारसे आच्छादित हुए मनुष्यको जहाँसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 39.8208)
- **Original**: शरणमें जाओ। जो ब्रह्मज्योति:स्वरूप, भक्तोंके ज्ञानरूपी दीपक प्राप्त होता है, जिसे पाकर सब
- **Translation**: 

---

### Verse 11 (Vaivtpuran 39.8209)
- **Original**: लिये मूर्तिमान्‌ अनुग्रह, सर्वज्ञ, ऐश्वर्यशाली और कुछ निर्मल दीखने लगता है, उससे बढ़कर बन्धु
- **Translation**: 

---

### Verse 12 (Vaivtpuran 39.8210)
- **Original**: सनातन हैं; उन गुरुदेवकी शरणका आश्रय लो। दूसरा कौन है? गुरुके दिये हुए मन्त्रका जप
- **Translation**: 

---

### Verse 13 (Vaivtpuran 39.8211)
- **Original**: प्रकृतिस्वरूपिणी पार्वतीने लाखों वर्षोतक तपस्या करनेसे ज्ञानकी प्राप्ति होती है और उस ज्ञानसे [करके जिन परमेश्वरकों अपने मनोनीत प्रियतम सर्वज्ञता तथा सिद्धि मिलती है; अतः गुरुसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 39.8212)
- **Original**: पतिके रूपमें प्राप्त किया है; उन गुरुदेवकी शरण बढ़कर बन्धु दूसरा कौन है? गुरुद्वारा दी गयी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 39.8213)
- **Original**: ग्रहण करो। नारद! इतना कहकर कमलजन्मा जिस विद्याके बलसे मनुष्य सर्वत्र सुखपूर्वक
- **Translation**: 

---

### Verse 16 (Vaivtpuran 39.8214)
- **Original**: ब्रह्मा मुनियोंक साथ चले गये। तब परशुरामने विजयी होता है और जगत्‌में पूज्य भी हो जाता
- **Translation**: 

---

### Verse 17 (Vaivtpuran 39.8215)
- **Original**: भी कैलास जानेका विचार किया। (अध्याय 40) #+65+8 “कल 9ल्‍0000-0 परशुरामका कैलास-गमन, वहाँ शिव-भवनमें पार्षदोंसहित गणेशको प्रणाम करके आगे बढ़नेको उद्यत होना, गणेशद्वारा रोके जानेपर उनके साथ वार्तालाप श्रीनारायण कहते हैं--नारद! श्रीहरिका
- **Translation**: 

---

### Verse 18 (Vaivtpuran 39.8216)
- **Original**: शिवाकों तथा दोनों गुरुपुत्र कार्तिकेय और कवच धारण करके जब परशुरामने पृथ्वीको
- **Translation**: 

---

### Verse 19 (Vaivtpuran 39.8217)
- **Original**: गणेश्वरकों, जो गुणोंमें नारायणके समान थे, क्षत्रियोंसे रहित कर दिया, तब वे अपने गुरुदेव
- **Translation**: 

---

### Verse 20 (Vaivtpuran 39.8218)
- **Original**: देखनेके लिये कैलासको चले। वे भृगुवंशी शिवकों नमस्कार करने और गुरुपन्नी अम्बा महात्मा मनके समान वेगशाली थे; अतः उसी
- **Translation**: 

---

