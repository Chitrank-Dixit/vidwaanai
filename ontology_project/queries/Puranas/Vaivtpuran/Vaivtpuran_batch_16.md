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

### Verse 1 (Vaivtpuran 3.185)
- **Original**: कभी कोई विकार नहीं होता, जो अव्यक्त और सिंहासनपर नारायणके साथ वार्तालाप करते हुए
- **Translation**: 

---

### Verse 2 (Vaivtpuran 3.186)
- **Original**: व्यक्तरूप हैं तथा गोप-वेष धारण करते हैं, उन बैठ गये। जो मनुष्य भगवान्‌ शिवद्वारा किये गये
- **Translation**: 

---

### Verse 3 (Vaivtpuran 3.187)
- **Original**: गोविन्द श्रीकृष्णकी मैं बन्दना करता हूँ। जिनकी इस स्तोत्रका संयतचित्त होकर पाठ करता. है,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 3.188)
- **Original**: नित्य किशोरावस्था है, जो सदा शान्त रहते हैं उसे सम्पूर्ण सिद्धियाँ मिल जाती हैं और पग-
- **Translation**: 

---

### Verse 5 (Vaivtpuran 3.189)
- **Original**: जिनका सौन्दर्य करोड़ों कामदेबोंसे भी अधिक पगपर विजय प्राप्त होती है। उसके मित्र, धन
- **Translation**: 

---

### Verse 6 (Vaivtpuran 3.190)
- **Original**: है तथा जो नूतन जलधरके समान श्यामवर्ण और ऐश्वर्यकी सदा वृद्धि होती है तथा शत्रुसमूह,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 3.191)
- **Original**: हैं, उन परम मनोहर गोपीबल्लभको मैं प्रणाम दुःख और पाप नष्ट हो जाते हैं। करता हूँ। जो वृन्दावनके भीतर रासमण्डलमें सौति कहते हैं--तत्पश्चात्‌ श्रीकृष्णके नाभि-
- **Translation**: 

---

### Verse 8 (Vaivtpuran 3.192)
- **Original**: विराजमान होते हैं, रासलीलामें जिनका निवास कमलसे बड़े-बूढ़े महातपस्वी ब्रह्माजी प्रकट
- **Translation**: 

---

### Verse 9 (Vaivtpuran 3.193)
- **Original**: है तथा जो रासजनित उल्लासके लिये सदा हुए। उन्होंने अपने हाथमें कमण्डलु ले रखा था।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 3.194)
- **Original**: उत्सुक रहते हैं, उन रासेश्वरकों मैं नमस्कार उनके दाँत और केश सभी सफेद थे।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 3.195)
- **Original**: करता हूँ।ा चार मुख थे। वे ब्रह्माजी योगियोंके ईश्वर, ऐसा कहकर ब्रह्माजीने भगवान्‌ श्रीकृष्णके शिल्पियोंके स्वामी तथा सबके जन्मदाता गुरु हैं।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 3.196)
- **Original**: चरणोंमें प्रणाम किया और उनकी आज्ञासे तपस्याके फल देनेवाले और सम्पूर्ण सम्पत्तियोंके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 3.197)
- **Original**: नारायण तथा महादेवजीके साथ सम्भाषण करते जन्मदाता हैं। वे ही स्रष्टा और विधाता हैं तथा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 3.198)
- **Original**: हुए श्रेष्ठ रत्ममव सिंहासनपर बैठे। जो प्रातःकाल समस्त कर्मोंके कर्ता, धर्ता एवं संहर्ता हैं। चारों
- **Translation**: 

---

### Verse 15 (Vaivtpuran 3.199)
- **Original**: उठकर ब्रह्माजीके द्वारा किये गये इस स्तोत्रका बेदोंकों वे ही धारण करते हैं। वे वेदोंके ज्ञाता, पाठ करता है, उसके सारे पाप नष्ट हो जाते वेदोंकों प्रकट करनेवाले और उनके पति हैं और बुरे सपने अच्छे सपनोंमें बदल जाते (पालक) हैं। उनका शील-स्वभाव सुन्दर है।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 3.200)
- **Original**: हैं। भगवान्‌ गोविन्दमें भक्ति होती है, जो पुत्रों वे सरस्वतीके कान्‍त, शान्तचित्त और कृपाकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 3.201)
- **Original**: और पौत्रोंकी वृद्धि करनेवाली है। इस स्तोत्रका निधि हैं। उन्होंने श्रीकृष्णके सामने खड़े हो दोनों
- **Translation**: 

---

### Verse 18 (Vaivtpuran 3.202)
- **Original**: पाठ करनेसे अपयश नष्ट होता है और चिरकालतक हाथ जोड़कर उनका स्तवन किया। उस समय
- **Translation**: 

---

### Verse 19 (Vaivtpuran 3.203)
- **Original**: सुयश बढ़ता रहता है। * जयस्वरूपं॑ जयद॑ जयेशं जयकारणम्‌ । प्रवर॑जयदानां च वबन्दे तमपराजितम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 3.204)
- **Original**: विश्व विश्वेश्वेशं च विश्वेशं विधकारणम्‌
- **Translation**: 

---

