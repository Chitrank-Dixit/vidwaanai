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

### Verse 1 (Vaivtpuran 10.9956)
- **Original**: अधरौईट इषीकेशो दन्तपंक्ति.. गदाग्रजः
- **Translation**: 

---

### Verse 2 (Vaivtpuran 10.9957)
- **Original**: रासेश्वरक्ष रसनां तालुक॑ वामनो विभु:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 10.9958)
- **Original**: वक्ष: पातु मुकुन्दस्त जठर॑ पातु दैत्यहा । जनार्दन: पातु नाभि पातु विष्णुश् ते हनुम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 10.9959)
- **Original**: नितम्बयुग्म॑ गुह्ं च पातु ते पुरुषोत्तम:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 10.9960)
- **Original**: जानुयुग्म॑ जानकौश: पातु ते सर्वदा विभु:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 10.9961)
- **Original**: हस्तयुग्म॑ नूसिंहश पातु. सर्वत्र सड्डूटे ई वराहश्व॒ पातु ते कमलोद्धव:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 10.9962)
- **Original**: ऊद्ध्व॑ नारायण: पातु हथघस्तात्‌ू कमलापति: यहाँ दशास्यहा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 10.9963)
- **Original**: वनमाली पातु याम्यां वैकुण्ठ: पातु नैऋती पातु ते सन्ततमजों वायय्यां विष्टरश्नवा:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.674)
- **Original**: ड्ेड » संक्षिम अहयवैवर्तपुराण + ऋडकक$क%#ऋ%%#%#%#%% %#%% %## %%##%#%##### ##%#% ## % #%#% ## # ##%#%# ### # ##%#### ##% # %## ## ##% ## #%# %#% %#% पापोंका नाश करके वह अवश्य ही पुण्यभोग
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.675)
- **Original**: प्राप्ति भी श्रीकृष्णभक्तको अभीष्ट नहीं है। तथा श्रीहरिकी सेवाका सौभाग्य पाता है।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.676)
- **Original**: श्रीहरिके सालोक्य, सार्ट्ि, सामीप्य और सायुज्यको मनुष्योंको तभीतक पत्नीकी इच्छा होती है,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.677)
- **Original**: तथा निर्वाणमोक्षकों भी वैष्णवजन नहीं लेना तभीतक पुत्र प्याग लगता है, तभीतक ऐश्वर्यको
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.678)
- **Original**: चाहते।* भगवान्‌की अविचल भक्ति तथा उनका प्राप्ति अभीष्ट होती है और तभीतक सुख-
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.679)
- **Original**: परम दुर्लभ दास्य प्राप्त हो-यही सोते, जागते दुःख होते हैं, जबतक कि उनका मन श्रीकृष्णमें
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.680)
- **Original**: हर समय भक्तोंकी इच्छा रहती है। अत: यही नहीं लगता। श्रीकृष्णमें मन लगते ही भक्तिरूपी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.681)
- **Original**: हमारे लिये श्रेष्ठ वर है। प्रभो! आप याचकोंके दुर्लड्डय खड़ग मानदोंके कर्ममय वृक्षोंका मूलोच्छेद
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.682)
- **Original**: लिये कल्पवृक्ष हैं; अतः मुझे बरके रूपमें कर डालता है। जिन पुण्यात्माओंके पुत्र परम श्रीहरिका दास्य-सुख तथा वैष्णव पुत्र प्रदान वैष्णव होते हैं, उनके वे पुत्र लीलापूर्वक कुलकी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.683)
- **Original**: कीजिये। आपको संतुष्ट पाकर जो दूसरा कोई बहुसंख्यक पीढ़ियोंका उद्धार कर देते हैं। अहो!
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.684)
- **Original**: वर माँगता है, वह बर्बर है। शम्भो! यदि आप एक वरसे ही कृतार्थ हुआ पुरुष यदि दूसरा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.685)
- **Original**: मुझे दुष्कर्मी मानकर यह उपर्युक्त बर नहीं देंगे खबर चाहता है तो मुझे आश्चर्य होता है। दूसरे
- **Translation**: 

---

