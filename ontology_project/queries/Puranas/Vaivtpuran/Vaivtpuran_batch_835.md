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

### Verse 1 (Vaivtpuran 543.15014)
- **Original**: दूसरा कोई प्राणी नहीं है। विशेषतः वह जो पाण्डवोंमें अर्जुन, नागकन्याओमें मनसा, वसुओमें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15015)
- **Original**: मेरे मनत्रकी उपासना करता है, सर्वश्रेष्ठ है। मैं द्रोण, बादलोंमें द्रोण, जम्बूद्वीपके नौ खण्डोंमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15016)
- **Original**: वृक्षोंमें अंकुर तथा सम्पूर्ण वस्तुओंमें उनका भारतवर्ष, कामियोंमें कामदेव, कामुकी स्त्रियोंमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15017)
- **Original**: आकार हूँ। समस्त भूतोंमें मेरा निवास है, मुझमें रम्भा और लोकोंमें गोलोक हूँ, जो समस्त
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15018)
- **Original**: सारा जगत्‌ फैला हुआ है। जैसे वृक्षमें फल लोकोंमें उत्तम और सबसे परे है। मातृकाओंमें
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15019)
- **Original**: और फलोंमें वृक्षका अंकुर है, उसी प्रकार मैं शान्ति, सुन्दरियोंमें रति, साक्षियोंमें धर्म, दिनके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15020)
- **Original**: सबका कारणरूप हूँ; मेरा कारण दूसरा नहीं है। क्षणोंमें संध्या, देवताओंमें इन्द्र, राक्षसोंमें विभीषण,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15021)
- **Original**: मैं सबका ईश्वर हूँ; मेरा ईश्वर दूसरा कोई नहीं रुद्रोंमें कालाग्रिरुद्र, भैरवोमें संहारभैरव, शद्डरोंमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15022)
- **Original**: है। मैं कारणका भी कारण हूँ। मनीषी पुरुष पाक्जन्य, अड्जोंमें मस्तक, पुराणोंमें भागवत,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15023)
- **Original**: मुझे ही सबके समस्त बीजोंका परम कारण बताते इतिहासोंमें महाभारत, पाञ्नरात्रोंमें कापिल, मनुओमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15024)
- **Original**: हैं। मेरी मायासे मोहित हुए पापीजन मुझे नहीं स्वायम्भुब, मुनियोंमें व्यासदेव, पितृपत्नियोंमें स्वधा,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15025)
- **Original**: जान पाते हैं। मैं सब जन्तुओंका आत्मा हूँ; परंतु अग्निप्रियाओंमें स्वाहा, यज्ञोंमें राजसूय, यज्ञपत्रनियोंमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15026)
- **Original**: दुर्बुद्धि और दुर्भाग्यसे बच्चित पापग्रस्त जीव मुझ दक्षिणा, अस्त्र-शस्त्रज्ञोंमें जमदग्निनन्दन महात्मा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15027)
- **Original**: अपने आत्माका भी आदर नहीं करते। जहाँ मैं परशुराम, पौराणिकोंमें सूत, नौतिज्ञोंमें अड्विरा, हूँ, उसी शरीरमें सब शक्तियाँ और भूख-प्यास ब्रतोंमें विष्णुब्रत, बलोंमें दैववल, ओषधियोंमें
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15028)
- **Original**: आदि हैं; मेरे निकलते ही सब उसी त9ह निकल दूर्वा, तृणोंमें कुश, धर्मकर्मांमें सत्य, स््रेहपात्रोंमें जाते हैं, जैसे राजाके पीछे-पीछे उसके सेवक। पुत्र, शत्रुआँमें व्याधि, व्याधियोंमें ज्वर, मेरी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15029)
- **Original**: त्रजराज नन्दजी! मेरे बाबा! इस ज्ञानको हृदयमें भक्तियोंमें दास्य-भक्ति, वरोंमें वर, आश्रमोंमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15030)
- **Original**: धारण करके व्रजको जाओ और राधा तथा यशोदा गृहस्थ, विवेकियोंमें संन्यासी, शस्त्रोंमें सुदर्शन
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15031)
- **Original**: मैयाकों इसका उपदेश दो। और शुभाशीर्वादोंमें कुशल हूँ। इस ज्ञानको भलीभाँति समझकर नन्‍्दजी ऐश्वर्यंमें महाज्ञान, सुखोंमें बैराग्य, प्रसन्नता
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15032)
- **Original**: अपने अनुगामी ब्रजवासियोंके साथ व्रजकों लौट प्रदान करनेवालोंमें मधुर वचन, दानोंमें आत्मदान,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15033)
- **Original**: गये। वहाँ जाकर उन्होंने उन दोनों नारीशिरोमणियोंसे संचयोंमें धर्मकर्मका संचय, कर्मोंमें मेश पूजन,
- **Translation**: 

---

