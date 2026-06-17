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

### Verse 1 (Vaivtpuran 4.8496)
- **Original**: आदेशसे सृष्टिकर्ता सृष्टिकौ रचना करते हैं, ब्राह्मणोंकी गायत्री हों। तुम सत्पुरुषोंक लिये
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8497)
- **Original**: पालनकर्ता रक्षा करते हैं और संहर्ता समय सत्त्वस्वरूप और दुष्टोके लिये कलहकी अद्भुर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8498)
- **Original**: आनेपर संहार करते हैं; उन दुर्गाको मैं प्रणाम हो। निर्गुणकी ज्योति और सगुणकी शक्ति तुम्हों
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8499)
- **Original**: करता हूँ। जिनके बिना स्वयं भगवान्‌ श्रीकृष्ण, हो। तुम सूर्यमें प्रभा, अग्निमें दाहिका-शक्ति,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8500)
- **Original**: जो ज्योतिःस्वरूप एवं निर्गुण हैं, सृष्टि-रचना जलमें शीतलता और चन्द्रमामें शोभा हो। भूमिमें करनेमें समर्थ नहीं होते; उन देवीको मेरा गन्ध और आकाशमें शब्द तुम्हारा ही रूप है। तुम
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8501)
- **Original**: नमस्कार है। जगज्जननी! रक्षा करो, रक्षा करो; भूख-प्यास आदि तथा प्राणियोंकी समस्त शक्ति
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8502)
- **Original**: मेंर अपराधको क्षमा कर दो। भला, कहीं बच्चेके हो। संसारमें सबकी उत्पत्तिकी कारण, साररूपा,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8503)
- **Original**: अपराध करनेसे माता कुपित होती है। स्मृति, मेधा, बुद्धि अथवा दिद्वानोंकी ज्ञाशशक्ति
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8504)
- **Original**: । इतना कहकर परशुराम उन्हें प्रणाम करके तुम्हीं हो। श्रीकृष्णने शिवजीको कृपापूर्वक सम्पूर्ण
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8505)
- **Original**: रोने लगे। तब दुर्गा प्रसन्न हो गयीं और शीघ्र ही ज्ञानकी प्रसविनी जो शुभ विद्या प्रदान की थी, न हा 52: हि. थ् पट >>: वह तुम्हीं हो; उसीसे शिवजी मृत्युक्रय हुए हैं।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8506)
- **Original**: (* ब्रह्मा, विष्णु और महेशकी सृष्टि, पालन और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8507)
- **Original**: संहार करनेवाली जो त्रिविध शक्तियाँ हैं, उनके रूपमें तुम्हीं विद्यमान हो; अत: तुम्हें नमस्कार है।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8508)
- **Original**: 6 जब मधु-कैटभके भयसे डरकर ब्रह्मा काँप उठे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8509)
- **Original**: 7] थे, उस समय जिनकी स्तुति करके वे भयमुक्त
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8510)
- **Original**: # हुए थे; उन देवीकों मैं सिर झुकाकर प्रणाम करता हूँ। मधु-कैटभके युद्धमें जगत्‌के रक्षक ये भगवान्‌ विष्णु जिन परमेश्वरीका स्तवन करके शक्तिमान्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8511)
- **Original**: & 2> 0) ( हुए थे; उन दुर्गाकों मैं नमस्कार करता उन्हें अभयका वरदान देती हुई बोलॉं--'हे वत्स! त्रिपुरके महायुद्धमें रथसहित शिवजीके गिर जानेपर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8512)
- **Original**: तुम अमर हो जाओ। बेटा! अब शान्ति धारण सभी देवताओंने जिनकी स्तुति की थी; उन
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8513)
- **Original**: करो। शिवजीकी कृपासे सदा सर्वत्र तुम्हारी दुर्गाको मैं प्रणाम करता हूँ। जिनका स्तवन करके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8514)
- **Original**: विजय हो। सर्वान्तरात्मा भगवान्‌ श्रीहरि सदा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8515)
- **Original**: *गणपतिरत्रण्ड «» 395 66460 04 47:7 00 । 00 0 । 0 0।। ]] 2 ]]]/
- **Translation**: 

---

