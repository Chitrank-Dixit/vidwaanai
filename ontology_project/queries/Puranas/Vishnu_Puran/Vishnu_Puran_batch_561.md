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

### Verse 1 (Vishnu Puran 0.11201)
- **Original**: हम तो इतना ही जानते हैं कि ] हे दैत्यदलन ! आप लोकरक्षार्में तत्पर हैं और इस संसारके काँटोंको निकाल रहे हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11202)
- **Original**: हे कृष्ण ! इस पारिजात-वृक्षको आप द्वारकापुरी ले जाइये, जिस समय आप मर्त्यल्नेक छोड़ देंगे, उस समय वह भूर्व्म्रेकर्में नहीं रहेगा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11203)
- **Original**: हे देवदेव ! हे जगन्नाथ ! हे कृष्ण! हे बिष्णो! हे महाबाहो ! हे शह्लुच्कगदापाणे ! मेरी इस धृष्टताको क्षमा कीजिये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11204)
- **Original**: श्रीपराइरजी बोले--तदनन्तर श्रौहरि देवराजसे 'तुम्तारी जैसी इच्छा है लैसा हो सही ऐसा कहकर सिद्ध, गर्व और देवर्षिगणसे स्तुत हो भूलेंकमें चले आये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11205)
- **Original**: हे द्विज ! द्वास्कापुरीके ऊपर पहुँचकर श्रोकृष्णचन्द्रने [ अपने आनेकों सूचना देते हुए ] शब्ठ बजाकर ट्वार्कासासियोंकों आनन्दित किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11206)
- **Original**: तदनन्तर सत्यभामाके सहित गरुडसे उतरकर उस पारिजात-महावृक्षको [सल्यभामाके] गृहोद्यानमें छगा दिया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11207)
- **Original**: जिसके पास आकर सब मनुष्योंको अपने पूर्वजन्प्का स्मरण हो आता है और जिसके पुष्पोंसे निकल्गी हुई गन्धसे तीन योजनतक पृथिवी सुगन्धित रहती
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11208)
- **Original**: आ* श2 ] ततस्ते यादवास्सरवें देहबन्धानमानुषान्‌ । ददृशुः पादपे तस्मिन्‌ कुर्वन्तो मुखदर्शनम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11209)
- **Original**: 13 किल्लरैस्समुपानीत॑ हस्त्यश्रादि ततो धनम्‌। विभज्य प्रददो कृष्णो बान्धवानां महामति:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11210)
- **Original**: 94 कन्याश्न कृष्णो जग्माह नरकस्य परिग्रहान्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11211)
- **Original**: 15 ता: कन्या नरकेणासन्सर्वतो यास्समाहता:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11212)
- **Original**: 16 एकस्मिन्नेब गोविन्दः काले तासाँ महामुने । विधिवत्पाणीन्यूथगोहेषु॒धर्मतः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11213)
- **Original**: 17 षोडशस्त्रीसह्लाणि शततमेके ततोडधिकम्‌। ताबन्ति चक्रे रूपाणि भगवान्‌ मथुसूदन:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11214)
- **Original**: 18 एकैकमेव ता: कन्या मेनिरे मधुसूदन: । ममैब पाणिग्रहर्ण मैत्रेय कृतवानिति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11215)
- **Original**: 19 निशासु च जगत्स्रष्टा तासां गेहेघु केशव: । उबास विप्र सर्वासां विश्वरूपधरों हरि:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11216)
- **Original**: 20 पञ्ञम अंश 395 है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11217)
- **Original**: यादवोंने उस वुक्षके पास जाकर अपना सुख देखा तो उन्हें अपना शरीर अमानुष दिखायी दिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11218)
- **Original**: तदनत्तर महामति श्रीकृष्णचन्द्रन. नरकासुरके सेबकोंद्वारा त्थये हुए हाथी-घोड़े आंदे धनको अपने बन्धु-बान्थवोंमें काट दिया और नरकासुरकी बरण की हुई कन्याओंको स्वयं ले लिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11219)
- **Original**: जुभ समय प्राप्त होनेपर श्रीजनार्दनने उन समस्त कन्याओकि साथ, जिन्हें नरकासुर बल्त्त्‌ हर लाया था, बिवाह किया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11220)
- **Original**: है महामुने ! श्रीगोठिन्दने एक हो समय पृथक-पृथक्‌ भवनोंमें उन सबके साथ विधिवत्‌ धर्मपूर्वक पाणिग्रहण किया
- **Translation**: 

---

