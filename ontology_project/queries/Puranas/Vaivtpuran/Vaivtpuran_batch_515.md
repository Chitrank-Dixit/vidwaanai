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

### Verse 1 (Vaivtpuran 31.7471)
- **Original**: मनोहर दिव्य शय्या, माला और तीन पुष्पाज्ञलि करोड़ों कामदेवोंकी भाँति सुन्दर, लीलाके धाम,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 31.7472)
- **Original**: निवेदित करना चाहिये। तदनन्तर षडड्भकी पूजा मनोहर और रक्नोंक आभूषणोंसे विभूषित हैं।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 31.7473)
- **Original**: करके फिर गणकी विधिवत पूजा करे। तत्पश्चात्‌ जिनके सम्पूर्ण अड्रोंमें चन्दनकी खौर लगी है।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 31.7474)
- **Original**: श्रीदामा, सुदामा, वसुदामा, हरिभानु, चन्द्रभानु, जो श्रेष्ठ पीताम्बर धारण किये हुए हैं। मुस्कराती
- **Translation**: 

---

### Verse 5 (Vaivtpuran 31.7475)
- **Original**: सूर्यभानु और सुभानु-इन सातों श्रेष्ठ पार्षदोंका हुई गोपियाँ सदा जिनको ओर निहार रही हैं।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 31.7476)
- **Original**: भक्तिभावसहित पूजन करे। फिर जो गोपीश्वरी, जो प्रफुल्ल मालती-पुष्पोंकी माला तथा वनमालासे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 31.7477)
- **Original**: मूलप्रकृति, आइ्याशक्ति, कृष्णशक्ति और विभूषित हैं। जो सिरपर ऐसी कलंँगी धारण किये
- **Translation**: 

---

### Verse 8 (Vaivtpuran 31.7478)
- **Original**: कृष्णद्वारा पूज्य हैं, उन राधिकाकी भक्तिपूर्वक हुए हैं, जिसमें कुन्द-पुष्पोंकी बहुतायत है, जो
- **Translation**: 

---

### Verse 9 (Vaivtpuran 31.7479)
- **Original**: पूजा करे। विद्वान्‌कों चाहिये कि वह गोप और कर्पूरसे सुवासित है और चन्द्रमा एवं ताराओंसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 31.7480)
- **Original**: गोपियोंके समुदाय, मुझ शान्तस्वरूप महादेव, युक्त आकाशकी प्रभाका उपहास कर रही है।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 31.7481)
- **Original**: ब्रह्मा, पार्वती, लक्ष्मी, सरस्वती, पृथ्वी, विग्रहधारी जिनके सर्वाड़में रत्नोंके भूषण सुशोभित हैं। जो
- **Translation**: 

---

### Verse 12 (Vaivtpuran 31.7482)
- **Original**: सम्पूर्ण देवता और देवषट्ककी पश्चोपचारद्वारा कण्ठे वा दक्षिणे बाहौँ सोउपि विष्णुर्न संशय: । स॒ च भक्तों वसेद्‌ यत्र लक्ष्मीर्वाणी वसेत्तत:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 31.7483)
- **Original**: यदि स्यात्‌ सिद्धकवचों जीवन्मुकों भवेतु सः। निश्चित कोटिवर्षाणां पूजाया: फलमापुयात्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 31.7484)
- **Original**: राजसूयसहस्ताणि वाजपेयशतानि च । अभश्रमेधायुतान्येव नरमेधायुतानि च
- **Translation**: 

---

### Verse 15 (Vaivtpuran 31.7485)
- **Original**: महादातानि. यान्येव प्रादक्षिण्य॑ भुवस्तथा । जैलोक्यविजयस्यास्थ कला नाहन्ति षोडशीम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 31.7486)
- **Original**: ब्रतोपवासनियम॑ स्वाध्यायाध्ययन तपः । स्रान॑ च सर्वतीर्थेषु नास्याहन्ति कलामपि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 31.7487)
- **Original**: सिद्धित्वममरत्वं च दास्यत्वं श्रीहरेरपि । यदि स्यात्‌ सिद्धकबथः सर्व॑ प्राप्रोति निश्चितम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 31.7488)
- **Original**: स॒ भवेत्‌ सिद्धकवचो दशलक्षं जपेतु यः। यो भवेत्‌ सिद्धकवच: सर्वकज्ञ: स भवेद्‌ ध्रुवम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 31.7489)
- **Original**: इरद॑ कवचमज्ञात्वा भजेत्‌ कृष्ण. सुमन्दधी: । कोटिकल्पप्रजप्तोएप न मन्त्र: सिद्धिदायक:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 31.7490)
- **Original**: गृहीत्वा कवच वत्स महाँ निःक्षत्रियाँ कुरु। त्रिःसप्तकृत्तो निःशद्रंः सदानन्दोइबलौीलया
- **Translation**: 

---

