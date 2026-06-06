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

### Verse 1 (Vaivtpuran 265.5117)
- **Original**: कथनानुसार पहले राधा नामका उच्चारण करके सर्वजीवन, सर्वाधार, परमपूज्य, सनातन ब्रह्मज्योति,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 265.5118)
- **Original**: पीछे कृष्ण या माधव कहते हैं। जो इसके सर्वसम्पत्तिस्वरूप, सम्पूर्ण सम्पदाओंके दाता,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 265.5119)
- **Original**: विपरीत उच्चारण करते या उन जगदम्बा सर्वमड्जलरूप, सर्वमड्गलकारण, सर्वमड्जलदाता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 265.5120)
- **Original**: श्रीकृष्णप्राणाधिका एवं प्रेममयी शक्ति श्रीरधिकाकी तथा समस्त मड्जलोंके भी मज्जल हैं। निन्दा करते हैं, वे चन्द्रमा तथा सूर्यकी स्थितिपर्यन्त श्रीकृष्णका दर्शन करके सशद्भित हो राजा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 265.5121)
- **Original**: कालसूत्र नरकमें यातना भोगते हैं। तत्पश्चात्‌ सौ सुयज्ञ तुरंत र्थसे उतर पड़े और नेत्रोंसे आँसू
- **Translation**: 

---

### Verse 6 (Vaivtpuran 265.5122)
- **Original**: वर्षोंतक स्त्री-पुत्रसे रहित तथा रोगी होते हैं। बहाते हुए पुलकित शरीरसे भगवान्‌के चरणोंमें। दुर्गें! इस प्रकार मैंने परम उत्तम राधिकाख्यानका मस्तक रखकर उन्होंने प्रणाम किया। परमात्मा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 265.5123)
- **Original**: वर्णन किया है। वह सती भगवती वैष्णवी, श्रीकृष्णे राजाकों अपना दासत्व, शुभाशीर्वाद
- **Translation**: 

---

### Verse 8 (Vaivtpuran 265.5124)
- **Original**: सनातनी, नारायणी, विष्णुमाया, मूलप्रकृति एवं तथा वह सत्य एवं अविचल श्रीकृष्णभक्ति प्रदान ईश्वरी नाम धारण करनेवाली तुम्हीं हो। मायाका की, जो हमलोगोंके लिये भी परम दुर्लभ है।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 265.5125)
- **Original**: आश्रय लेकर मुझसे पूछ रही हो। तुम स्वय॑ तदनन्तर श्रीराधा अपने रथसे उतरकर श्रीकृष्णके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 265.5126)
- **Original**: ही सर्वज्ञा, सर्वरूपिणी, स्त्रीजातिकी अधिदेवी वक्षमें विराजमान हो गयीं। उनकी अत्यन्त प्यारी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 265.5127)
- **Original**: तथा पूर्वजन्मकी बातोंको याद रखनेवाली श्रेष्ठ गोपियाँ सफेद चँवर लिये उनकी सेवामें लग
- **Translation**: 

---

### Verse 12 (Vaivtpuran 265.5128)
- **Original**: पराशक्ति हो। राधिकाकी कथा तो मैंने सुना दी, गयीँ। उनके आनेपर श्रीकृष्ण भक्ति और आदरसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 265.5129)
- **Original**: अब और क्‍या सुनना चाहती हो ? (अध्याय 54) #344000--र सफर न्‍->> >> श्रीराधाके ध्यान, षोडशोपचार-पूजन, परिचारिकापूजन, परिहारस्तवन, पूजन-महिमा तथा स्तुति एवं उसके माहात्म्यका वर्णन श्रीपार्वतीने पूछा--भगवन्‌! आप पुरुषोंके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 265.5130)
- **Original**: श्रीकृष्णी सेवासे उनके लोककों तुम बहुत ईश्वर श्रीकृष्णके मन्त्रके होते हुए उन वैष्णवनरेश
- **Translation**: 

---

### Verse 15 (Vaivtpuran 265.5131)
- **Original**: जन्मोंमें प्राप्त करोगे, अत: उनके प्राणोंकी सुयज्ञने राधाका मन्त्र क्यों ग्रहण किया? सुतपाने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 265.5132)
- **Original**: अधिष्ठात्री देवी परात्परस्वरूपा श्रीराधाका भजन राजाको श्रीराधाकी पूजाका कौन-सा विधान
- **Translation**: 

---

### Verse 17 (Vaivtpuran 265.5133)
- **Original**: करो। वे कृपामयी हैं। उनके प्रसादसे साधक बताया? तथा किस ध्यान, किस स्तोत्र, किस
- **Translation**: 

---

### Verse 18 (Vaivtpuran 265.5134)
- **Original**: शीघ्र ही उनके धामको प्राप्त कर लेता है '-ऐसा कवच और किस मन्त्रका उपदेश दिया? श्रोराधाकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 265.5135)
- **Original**: कहकर मुनिने उन्हें राधाके इस षडक्षर-मन्त्रका पूजापद्धति क्‍या है? ये सब बातें बताइये।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 265.5136)
- **Original**: उपदेश दिया। वह मन्त्र इस प्रकार है--30 श्रीमहेश्वर बोले--प्रिये! राजाने यह प्रश्न
- **Translation**: 

---

