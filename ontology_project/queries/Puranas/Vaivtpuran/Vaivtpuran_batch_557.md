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

### Verse 1 (Vaivtpuran 39.8159)
- **Original**: + गणपतिखण्ड + 383 ######%##%#$% #% #%%%%$%%$%$%ऋ%ऋ$%ऊऋ%%$%%$%ऊ## कक: 55% कक और सृष्टि-रचनाके समय प्रकट हो जाती है। जैसे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 39.8160)
- **Original**: दिया। फिर लीलापूर्बक पाशुपतास्त्रका प्रयोग मिट्टीके बिना कुम्हार घड़ा नहीं बना सकता और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.8161)
- **Original**: करके राजाकी जीवनलीला समाप्त कर दी। इसी स्वर्णके बिना सोनार कुण्डलका निर्माण करनेमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.8162)
- **Original**: प्रकार परशुरामने शिवजीका स्मरण करते हुए असमर्थ है (उसी तरह स्रष्टा मायाके बिना सृष्टि-
- **Translation**: 

---

### Verse 5 (Vaivtpuran 39.8163)
- **Original**: खेल-ही-खेलमें क्रमशः इक्कीस बार पृथ्बीको रचना नहीं कर सकते)। वह शक्ति ईश्वरकौ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 39.8164)
- **Original**: राजाओंसे शून्य कर दिया। परशुरामने अपनी इच्छासे सृष्टिकालमें राधा, पद्मा, सावित्री, दुर्गादेवी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 39.8165)
- **Original**: प्रतिज्ञाकी रक्षा करनेके लिये क्षत्रियोंके गर्भमें और सरस्वती नामसे पाँच प्रकारकी हो जाती हैं।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 39.8166)
- **Original**: स्थित तथा माताकी गोदमें खेलनेवाले शिशुओंका, परमात्मा श्रीकृष्णकी जो प्राणाधिष्ठात्री देवी हैं, [नौजवानोंका तथा वृद्धोंका संहार कर डाला। इस वह प्राणोंसे भी बढ़कर प्रियतमा 'राधा' कही
- **Translation**: 

---

### Verse 9 (Vaivtpuran 39.8167)
- **Original**: प्रकार कार्तवीर्य गोलोकमें श्रीकृष्णके संनिकट जाती हैं। जो सम्पूर्ण मज़लॉको सम्पन्न करनेवाली,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 39.8168)
- **Original**: चला गया और परशुराम श्रीहरिका स्मरण करते परमानन्दरूपा तथा ऐश्वर्यका अधिष्ठात्री देवी हैं; हुए अपने आश्रमको लौट गये। महेश्वरने इक्कीस वे “लक्ष्मी' नामसे पुकारी जाती हैं। जो वेद, बार पृथ्वीको भूपालॉंसे हीन देख और रामको शास्त्र और योगकी जननी, परम दुर्लभ और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 39.8169)
- **Original**: फरसेद्वारा क्रीडा करते देखकर उनका नाम परमेश्वरकी विद्याकी अधिप्ठात्री देवी हैं; उनका
- **Translation**: 

---

### Verse 12 (Vaivtpuran 39.8170)
- **Original**: परशुराम रख दिया। नारद! तब देवता, मुनि, नाम “सावित्री” है। जो सर्वशक्तिस्वरूपिणी,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 39.8171)
- **Original**: देवियाँ, सिद्ध, गन्धर्व, किन्नर-ये सभी लोग सर्वज्ञानात्मिका, सर्वस्वरूपा और बुद्धिकी अधिष्ठात्री
- **Translation**: 

---

### Verse 14 (Vaivtpuran 39.8172)
- **Original**: परशुरामके मस्तकपर पुष्पोंकी वृष्टि करने लगे। देवी हैं; वे दुर्गनाशिनी 'दुर्गा' कहलाती हैं। जो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 39.8173)
- **Original**: स्वर्गमें दुन्दुभियाँ बजने लगीं और हरिनाम- वाणीकी अधिष्ठात्री देवी और सदा शास्त्र-ज्ञान
- **Translation**: 

---

### Verse 16 (Vaivtpuran 39.8174)
- **Original**: संकीर्तन होने लगा। इस प्रकार परशुरामके प्रदान करनेवाली हैं तथा जो श्रीकृष्णके कण्ठसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 39.8175)
- **Original**: उज्ज्वल यशसे सारा जगत्‌ व्याप्त हो गया। फिर उत्पन्न हुई हैं; बे देवी 'सरस्वती' कही जाती हैं।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 39.8176)
- **Original**: ब्रह्मा, भृगु, शुक्र, च्यवन, वाल्मीकि तथा परम आदियें स्वयं मूलप्रकृति परमेश्वरीदेवी पाँच प्रकारकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 39.8177)
- **Original**: प्रसन्न हुए जमदग्रि ब्रह्मलोकसे वहाँ पधारे। उनके थीं। परंतु वे ही पीछे सृष्टि-क्रमसे बहुत-सी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 39.8178)
- **Original**: सारे अज्ज पुलकायमान थे और नेत्रोंमें आनन्दके कलाओंवाली हो गयीं। सृष्टि-कालमें मायाद्वारा
- **Translation**: 

---

