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

### Verse 1 (Vaivtpuran 543.15874)
- **Original**: रागाधिष्नातृदेवी._ त्व॑ अ्माणश्च॒ सरस्वती । प्राणानामधिदेवी त्व॑ कृष्णस्थ परमात्मनः
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15875)
- **Original**: गोलोके च स्वय॑ राधा श्रीकृष्णस्यैव वक्षसि । गोलोकाधिष्ठिता देवी. वृन्दावनवने. बने
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15876)
- **Original**: श्रीरासमण्डले रम्या वृन्दावनविनोदिनी । शतशृज्ञाधिदेवी त्वं नाप्ना चित्रावलीति च
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15877)
- **Original**: दक्षकन्या कुत्र कल्पे कुत्र कल्पे च शैलजा । देवमातादितिस्त्व॑ं. च॒ सर्वाधारा. वसुन्धरा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15878)
- **Original**: त्वमेव गड्जा तुलसों त्व॑ च स्वाहा स्वधा सती । त्वदंशांशांशकलया सर्वदेवादियोषित:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15879)
- **Original**: 692 + संक्षिप्त ब्रह्मबैवर्तपुराण न ###6##### 68 # 4 8 ### 44 # 44545 54 कक 55 अक कद डक इक अर अ5 अं ध अअ अ5 5 5 458 54 4 485 8 8 8 8 8 श्रीदुर्गेने कहा--शंकर ! तुम्हारा कल्याण
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15880)
- **Original**: हो नाचने लगे और गन्धर्व-किन्नर गान करने हो! तुम्हारे मनमें जो इच्छा हो, वह वर माँग लो।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15881)
- **Original**: लगे। तात! इसी अवसरपर अनुपम स्तवराज भी चूँकि तुम समस्त देवताओंमें श्रेष्ठ हो; अत: मैं
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15882)
- **Original**: प्रकट हुआ--जो विज्नों, विप्नकर्ताओं और शत्रुओंका तुम्हें विजय प्रदान करूँगी। संहारक, परमैश्वर्यका उत्पादक, सुखद, परम शुभ, श्रीमहादेवजी बोले--परमे श्वरि ! तुम आद्या
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15883)
- **Original**: निर्वाण--मोक्षका दाता, हरि-भक्तिप्रद, गोलोकका सनातनी शक्ति हो; अतः दुर्गे! 'दैत्यका विनाश हो
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15884)
- **Original**: वास प्रदान करनेवाला, सर्वसिद्धिप्रद और श्रेष्ठ है। जाय '--बह मेरा अभीष्ट वर मुझे प्रदान करो।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15885)
- **Original**: उस स्तवराजका पाठ करनेसे पार्वती सदा प्रसन्न भरगवतीने कहा--महाभाग! तुम तो स्वयं
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15886)
- **Original**: रहती हैं। वह मनुष्योंके लोभ, मोह, काम, क्रोध ही भगवान्‌ विधाता और ज्योतिर्मय परमेश्वर हो;
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15887)
- **Original**: और कर्मके मूलका उच्छेदक, बल-बुद्धिकारक, अत: जगदुरो! श्रीहरिका स्मरण करो और इस
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15888)
- **Original**: जन्म-मृत्युका बिनाशक, धन, पुत्र, स्त्री, भूमि दैत्यको जीत लो। आदि समस्त सम्पत्तियोंका प्रदाता, शोक-दुःखका इसी बीच सर्वव्यापी विष्णुने अपनी एक
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15889)
- **Original**: हरण करनेवाला, सम्पूर्ण सिद्धियोंका दाता तथा कलासे वृषका रूप धारण किया और शूलपाणि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15890)
- **Original**: सर्वोत्तम है। इस स्तोत्रराजके पाठसे महावन्ध्या शंकरके उस उग्र र्थको, जिसका पहिया ऊपर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15891)
- **Original**: भी प्रसविनी हो जाती है, बँधा हुआ बन्धनमुक्त उठ गया था, प्रकृतिस्थ कर दिया। तत्पश्चात्‌ उसे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15892)
- **Original**: हो जाता है, दुःखी निश्चय ही भयसे छूट जाता है, अपने सिरपर उठा लिया। उन्होंने शंकरको एक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15893)
- **Original**: रोगीका रोग नष्ट हो जाता है, दरिद्र धनी हो जाता मन्त्रपूत शस्त्र भी प्रदान किया। तब शंकरने उस
- **Translation**: 

---

