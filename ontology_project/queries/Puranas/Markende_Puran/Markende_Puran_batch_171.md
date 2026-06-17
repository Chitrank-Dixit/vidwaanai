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

### Verse 1 (Markende Puran 0.3401)
- **Original**: पृथ्वीपर मोक्षको प्राप्ति कराती हो
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3402)
- **Original**: सम्पूर्ण विद्याएँ तुम्हारे ही भिन्न-भिन्न स्वरूप हैं।
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3403)
- **Original**: जगत्‌में जितनी स्त्रियाँ हैं, बे सब तुम्हारी ही
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3404)
- **Original**: मूर्तियाँ हैं। जगदम्ब! एकमात्र तुमने ही इस विश्वको व्याप्त कर .रखा है। तुम्हारी स्तुति क्या
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3405)
- **Original**: हो सकती है? तुम तो स्तवन करने योग्य पदार्थोंसे परे एवं परा वाणी हो
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3406)
- **Original**: देवि ! जब तुम सर्वस्वरूप एवं स्वर्ग तथा मोक्ष प्रदान करनेवाली हो, तब इसी रूपमें तुम्हारी स्तुति हो गयी। तुम्हारी स्तुतिके लिये इससे अच्छी उक्तियाँ और क्‍या हो सकती हैं ?
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3407)
- **Original**: बुद्धिरूपसे सब लोगोंके इृदयमें विराजमान रहनेवाली तथा स्वर्ग एवं मोक्ष प्रदान करनेवाली नारायणी देवि! तुम्हें नमस्कार है
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3408)
- **Original**: कला, काष्ठा आदिके रूपसे क्रमशः परिणाम (अबस्था-परिवर्तन)-की ओर ले जानेवाली तथा विश्वका उपसंहार करनेमें समर्थ नारायणी ! तुम्हें नमस्कार है
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3409)
- **Original**: नारायणी ! तुम सब प्रकारका मड्गल प्रदान करनेवाली मड्भलमयौं हो। कल्याणदायिनौ शिवा हो। सब पुरुषार्थोकों सिद्ध करनेवाली, शरणागतवत्सला, तीन नेत्रोंवाली एवं गौरी हो। तुम्हें नमस्कार है
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3410)
- **Original**: तुम सृष्टि, पालन और संहारकी शक्तिभूता, सनातनी देवी, गुणोंका आधार तथा सर्वगुणमयी हो। नारायणि ! तुम्हें नमस्कार है
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3411)
- **Original**: शरणमें आये हुए दीनों एबं पीड़ितोंकी रक्षामें संलग्न रहनेवाली तथा सबकी पीड़ा दूर करनेवाली नारायणी देवी ! तुम्हें नमस्कार है
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3412)
- **Original**: नारायणि ! तुम ब्रह्माणीका रूप धारण करके हँंसोंसे जुते हुए विमानपर बैठती तथा कुश-मिश्रित जल छिड़कतो रहतो हो। तुम्हें नमस्कार है
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3413)
- **Original**: माहे भ्वरीरूपसे त्रिशूल, चन्द्रमा एवं सर्पको धारण करनेवालो तथा महान्‌ वृषभकी पीठपर बैठनेवाली और मुर्गोंसे घिरी रहनेवाली तथा महाशक्ति धारण करनेवाली कौमारीरूपभारिणी निष्पापे नारायणि! तुम्हें नमस्कार है
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3414)
- **Original**: शझ्लु, चक्र, गदा और शार्ड्रधनुषरूप उत्तम आयुधोंको धारण करनेवाली वैष्णबी शक्तिरूपा नारायणि! तुम प्रसन्न होओ। तुम्हें नमस्कार है
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3415)
- **Original**: हाथमें भयानक महाचक्र लिये और दाढ़ोंपर धरतीको उठाये वाराहीरूपधारिणी कल्याणमयी नारायणि! तुम्हें नमस्कार है
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3416)
- **Original**: भयड्ढडर नृसिंहरूपसे दैत्योंक बधके लिये उद्योग करनेवाली तथा त्रिभुवनकी रक्षामें संलग्न रहनेवाली नारायणि! तुम्हें नमस्कार है
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3417)
- **Original**: मस्तकपर किरीट और हाथमें महावज् धारण करनेवाली, सहस्र नेत्रोंक कारण उद्दीप्त दिखायी देनेवाली और वृत्रासुरके प्राणॉका अपहरण करनेवाली इन्द्रशक्तिरूपा नारायणी देवि! तुम्हें नमस्कार है
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3418)
- **Original**: शिवदूतीरूपसे दैत्योंकी महती सेनाका संहार करनेवाली, भयड्डूर रूप धारण तथा विकट गर्जना करनेबाली नारायणि! तुम्हें नमस्कार है
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3419)
- **Original**: दाढ़ोंक कारण विकराल
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3420)
- **Original**: +देवताओंद्वारा देवीकी स्तुति तथा देवीद्वारा देवताऑको खरदात्र* मुखवाली मुण्डमालासे विभूषित मुण्डमर्दिनी चामुण्डारूपा नारायणि! तुम्हें नमस्कार है
- **Translation**: 

---

