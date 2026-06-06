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

### Verse 1 (Vaivtpuran 39.8179)
- **Original**: आँसू छलक आये थे। वे सभी हाथमें दूब और स्त्रियाँ प्रकृतिके और पुरुषणण पुरुषके अंशसे [पुष्प लेकर मड्भनलाशासन कर रहे थे। तब उत्पन्न हुए; क्योंकि माया-शक्ति बिना सृष्टि नहीं
- **Translation**: 

---

### Verse 2 (Vaivtpuran 39.8180)
- **Original**: परशुरामने दण्डकी भाँति भूमिपर लेटकर उन हो सकती। ब्रह्मन्‌! प्रत्येक विश्वमें सृष्टि सदा [सबको प्रणाम किया। तब क्रमश: “तात' यों ब्रह्मासे ही प्रकट होती है। विष्णु उसके पालक
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.8181)
- **Original**: कहते हुए पहले ब्रह्माने उन्हें अपनी गोदमें बैठा और निरन्तर मड्ल प्रदान करनेवाले शिव संहारक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.8182)
- **Original**: लिया। फिर जगदुरु स्वयं ब्रह्मा परशुरामसे हैं। परशुराम! यह ज्ञान दत्तात्रेयजीका दिया हुआ
- **Translation**: 

---

### Verse 5 (Vaivtpuran 39.8183)
- **Original**: हितकारक, नीतियुक्त, वेदका सारतत्त्व और है, उन्होंने पुष्करतीर्थमें माघी पूर्णिमाके दिन
- **Translation**: 

---

### Verse 6 (Vaivtpuran 39.8184)
- **Original**: परिणाममें सुखदायक बचन बोले। दीक्षाके अवसरपर मुनिवरोंके संनिकट मुझे दिया
- **Translation**: 

---

### Verse 7 (Vaivtpuran 39.8185)
- **Original**: । . ब्रह्माने कहा--राम ! जो सम्पूर्ण सम्पत्तियोंको था। इतना कहकर कार्तवीर्यने मुस्कराते हुए
- **Translation**: 

---

### Verse 8 (Vaivtpuran 39.8186)
- **Original**: देनेवाला परमोत्कृष्ट, सर्वसम्मत और सत्य है, परशुरामको नमस्कार किया और शीघ्र ही बाणसहित
- **Translation**: 

---

### Verse 9 (Vaivtpuran 39.8187)
- **Original**: वह काण्वशाखोक्त वचन कहता हूँ, सुनों। जो धनुष हाथमें लेकर वह रथपर जा बैठा। सभी पूजनीयोंमें इष्ट, पृज्यतम और प्रधान है, तत्पश्चात्‌ परशुरामने श्रीहरिका स्मरण करते
- **Translation**: 

---

### Verse 10 (Vaivtpuran 39.8188)
- **Original**: वह जन्म देनेके कारण जनक और पालन करनेके हुए ब्रह्मास्त्रद्वारा राजाकी सेनाका सफाया कर कारण पिता कहा जाता है। किंतु मुने! जो
- **Translation**: 

---

### Verse 11 (Vaivtpuran 39.8189)
- **Original**: इे8ड + संक्षिप्त ब्रह्मवैवर्तपुराण « 1+7+4]8]7/]
- **Translation**: 

---

### Verse 12 (Vaivtpuran 39.8190)
- **Original**: 8] 37] 7] 73 777 7 802888 8888] अन्नदाता पिता है, वह जन्मदाता पितासे बड़ा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 39.8191)
- **Original**: है, उस गुरुसे बढ़कर बन्धु दूसरा कौन है? हे है; क्योंकि पितासे उत्पन्न हुआ शरीर अन्नके बिना
- **Translation**: 

---

### Verse 14 (Vaivtpuran 39.8192)
- **Original**: पुत्र! श्रीकृष्ण तुम्हारे अभीष्टदेव हैं और स्वयं नित्य क्षीण होता जाता है। माता उन दोनोंसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 39.8193)
- **Original**: शंकर गुरु हैं;अतः तुम अभीष्टदेवसे भी बढ़कर सौ गुनी पूज्या, मान्या और वन्दनीया है; क्योंकि
- **Translation**: 

---

### Verse 16 (Vaivtpuran 39.8194)
- **Original**: पूजनीय गुरुकी शरण ग्रहण करो। जिनके गर्भमें धारण करने और पालन-पोषण करनेसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 39.8195)
- **Original**: आश्रयसे तुमने इक्कीस बार पृथ्वीको भूपालोंसे वह उन दोनोंसे बड़ी है। श्रुतिमें ऐसा सुना गया
- **Translation**: 

---

### Verse 18 (Vaivtpuran 39.8196)
- **Original**: रहित कर दिया है और श्रीहरिकी भक्ति प्राप्त है कि अपना अभीष्टदेव उन सबसे सौगुना बढ़कर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 39.8197)
- **Original**: की है; उन शिवकी शरणमें जाओ। जो पूज्य है और ज्ञान, विद्या तथा मन्त्र देनेवाला
- **Translation**: 

---

### Verse 20 (Vaivtpuran 39.8198)
- **Original**: मड्जलस्वरूप, कल्याणकी मूर्ति, कल्याणदाता, गुरु अभीष्टदेवसे भी बढ़कर है। गुरुपुत्र गुरुकी
- **Translation**: 

---

