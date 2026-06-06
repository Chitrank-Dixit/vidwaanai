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

### Verse 1 (Vaivtpuran 35.7822)
- **Original**: वेष धारण करके राजासे कवचकी याचना की। ब्राह्मण युद्धके लिये उद्योगशील हो, ऐसा तो न
- **Translation**: 

---

### Verse 2 (Vaivtpuran 35.7823)
- **Original**: राजाने 'ब्रह्माण्ड-विजय ' नामक वह उत्तम कबच देखनेमें ही आया है और न सुना ही गया है।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 35.7824)
- **Original**: उन्हें दे दिया। उस कवचको लेकर परशुरामने भगवान्‌ नारायणके विद्यमान रहते यह दूसरी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 35.7825)
- **Original**: पुनः त्रिशूलसे ही प्रहार किया। उसके आघातसे तरहका उलट-फेर कैसे हो गया? मत्स्यराज, जो चद्धवंशमें उत्पन्न, गुणवान्‌ और रणाड्ुणमें यों कहकर राजेन्द्र कार्तवीर्य
- **Translation**: 

---

### Verse 5 (Vaivtpuran 35.7826)
- **Original**: महाबली था, जिसके मुखको कान्ति सैकड़ों शान्त हो गया। उसके उस वचनको सुनकर सभी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 35.7827)
- **Original**: चन्द्रमाओंके समान थी, भूतलपर गिर पड़ा। लोग मौन हो गये। तदनन्तर परशुरामके सभी नारदने कहा--महाभाग नारायण ! मत्स्यराजने भाई, जो बड़े शूरवीर तथा हाथोंमें अत्यन्त तीखे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 35.7828)
- **Original**: शिवजीके जिस कवचको धारण किया था, शस्त्र धारण किये हुए थे, उनकी आज्ञासे युद्ध
- **Translation**: 

---

### Verse 8 (Vaivtpuran 35.7829)
- **Original**: उसका वर्णन कीजिये; क्योंकि उसे सुननेके लिये करनेके लिये आगे बढ़े। तब जो स्वयं मड्भलस्वरूप
- **Translation**: 

---

### Verse 9 (Vaivtpuran 35.7830)
- **Original**: मुझे कौतृहल हो रहा है। तथा मड़लोंका आश्रयस्थान था, उस महाबली नारायण बोले--विप्रवर ! महात्मा शंकरके मत्स्यराजने भी उन सबको युद्धोन्‍्मुख देखकर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 35.7831)
- **Original**: उस 'ब्रह्मण्डविजय' नामक कबचका, जो सर्वाड्गकी युद्ध करना आरम्भ किया। उस राजेन्द्रने बाणोंका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 35.7832)
- **Original**: रक्षा करनेवाला है, वर्णन करता हूँ; सुनो। जाल बिछाकर उन सभीको रोक दिया। तब
- **Translation**: 

---

### Verse 12 (Vaivtpuran 35.7833)
- **Original**: पूर्वकालमें दुर्वासाने बुद्धिमान्‌ मत्स्थराजको सम्पूर्ण जमदग्निके पुत्रोंने उस बाण-समूहको छिलन्न-भिन्न
- **Translation**: 

---

### Verse 13 (Vaivtpuran 35.7834)
- **Original**: पापोंका समूल नाश करनेवाला पषडक्षर-मन्त्र कर दिया। मुने! राजाने सैकड़ों सूर्योंके समान
- **Translation**: 

---

### Verse 14 (Vaivtpuran 35.7835)
- **Original**: बतलाकर इसे प्रदान किया था। यदि सिद्धि प्राप्त प्रकाशमान दिव्यास्त्र चलाया; परंतु मुनियोंने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 35.7836)
- **Original**: हो जाय तो इस कबचके शरीरपर स्थित रहते माहे ध्वर-अस्त्रके द्वारा खेल-ही-खेलमें उसे काट
- **Translation**: 

---

### Verse 16 (Vaivtpuran 35.7837)
- **Original**: अस्त्र-शस्त्रके प्रहारके समय, जलमें तथा अग्रनिमें दिया। पुनः मुनियोंने दिव्यास्त्रद्वारा राजाके बाणसहित
- **Translation**: 

---

### Verse 17 (Vaivtpuran 35.7838)
- **Original**: प्राणियोंकी मृत्यु नहीं होती-इसमें संशय नहीं धनुष, रथ, सारथि और कवचकी धज्जियाँ उड़ा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 35.7839)
- **Original**: है। जिसे पढ़कर एवं धारण करके दुर्वासा सिद्ध दीं। इस प्रकार राजाको शस्त्रहीन देखकर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 35.7840)
- **Original**: होकर लोकपूजित हो गये, जिसके पढ़ने और मुनियोंको महान्‌ हर्ष हुआ। तब उन्होंने मत्स्यराजका
- **Translation**: 

---

### Verse 20 (Vaivtpuran 35.7841)
- **Original**: धारण करनेसे जैगीषव्य महायोगी कहलाने लगे। वध करनेकी इच्छासे शिवजीका त्रिशूल हाथमें
- **Translation**: 

---

