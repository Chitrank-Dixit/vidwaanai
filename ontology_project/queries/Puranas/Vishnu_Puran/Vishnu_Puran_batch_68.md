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

### Verse 1 (Vishnu Puran 0.1341)
- **Original**: तब सम्पूर्ण मायाके लीन हो जानेपर उससे हार जानेकी आइंकासे देवताओँंकों बड़ा भव हुआ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1342)
- **Original**: अततः उसके तपसे सन्‍्तप्न हो वे सब आपसमें मिलकर जगत्‌के आदि-कारण, शरणागतवत्सलू,- अनादि और अनन्त श्रीहरिकी शासणमें गये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1343)
- **Original**: देवता बोले--हे देवाधिदेव, जगन्नाथ, परमेश्वर, पुरुषोत्तम ! हम सब धुबकी तपस्थासे सन्तप्त होकर आपकी जझरणमें आये हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1344)
- **Original**: हे देव ! जिस प्रकार चन्द्रमा अपनी कल्त्रओसे प्रतिदिन बढ़ता है उसी प्रकार यह भी तपस्याके कारण रात-दिन उचञ्नत हो रहा है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1345)
- **Original**: है जनार्दन ! इस उत्तानपादके पुत्रकी तपस्यासे भयभीत होकर हम आपकी दारणमें आये हैं, आप उसे तपसे निवृत्त कीजिये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1346)
- **Original**: हम नहीं जानते, वह इन्द्रत्व चाहता है या सूर्यत्य अथवा उसे कुत्नेर, वरुण या चऋद्रमाके पदकी अभिलल्‍नषा है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1347)
- **Original**: अतः है ईझ ! आप हमपर प्रसन्न होइये और इस उत्तानपादके पुज़्को तपसे निवृत्त करके हमारे हृदयका काँटा निकालिये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1348)
- **Original**: श्रीभगबान्‌ बोल्के--हे सुरगण ! उसे इन्द्र, सूर्य, वरुण अथया कुबेर आदि किसीके पदकी अभिल्‍ाषा नहीं है, उसकी जो कुछ इच्छा है तह मैं सब पूर्ण करूँगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1349)
- **Original**: हे देवगण! तुम निश्चित्त होकर इच्छानुसार अपने-अपने स्थानॉकों जाओ। मैं तपस्यामें लगे हुए उस बालक्कों निवृत्त करता हूँ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1350)
- **Original**: श्रीपराशरजी बोले--देवाधिदेव भगवानके ऐसा कलनेपर इन्द्र आदि समस्त देबगण उन्हें प्रणामकर अपने-अपने स्थानोंको गये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1351)
- **Original**: सर्वात्मा भगवान्‌ हरिने भी च्ुज॒की तन्मयतासे प्रसन्न हो उसके निकट चतुर्भुजरूपसे जाकर इस प्रकार कहा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1352)
- **Original**: श्रीभगवान्‌ खोल्ले--हे उत्तानपादके पुत्र धुव ! तेरा कल्याण हो । मैं तेरी तपस्यासे प्रसन्न होकर तुझे वर देनेके लिये प्रकट हुआ हूँ, हे सुक्त ! तू बर माँग
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1353)
- **Original**: तूने सम्पूर्ण बाह्म निषयोंसे उपरत होकर अपने चित्तको मुझमें ही लूगा दिया है। अतः मै तुझसे अति सस्तुष्ट हूँ। अब तू अपनी इच्छातुसार श्रेष्ठ अर माँग
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1354)
- **Original**: श्रोपराहरजी बोले--देलाधिटेज भगवानके ऐसे क्चन सुनकर बालक छुवने आँखें खोलीं और अपनी ध्यानावस्थामें देखे हुए भगवान्‌ हरिको साक्षात्‌ अपने
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1355)
- **Original**: ड8 श्रीक्षिष्णुपुणण [ अ> 12 अल्बुचक्रगदाशार्ड्बरासिधरमच्युतम्‌ू_। किरीटिन समालोक्य जगाम दिरसा महीम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1356)
- **Original**: 45 रोमाझिताड़ुः सहसा साध्यस परम गत: । स्तवाय देवदेबस्थ स चक्रे मानस घुब:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1357)
- **Original**: 46 कि वद्माप्ति स्तुतावस्य केनोक्तेनास्य संस्तुति: । इत्याकुलमतिदेब॑तमेव शरण ययौ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1358)
- **Original**: 47 घृव उवाच भ्रगवन्यदि मे तोष॑ तपसा परम गतः। स्तोतुं तदहमिच्छामि बरमेनं प्रयच्छ में
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1359)
- **Original**: 48 (त्र्माद्रर्यस्य वेदजैज्ञायते यस्य नो गति: । त॑ त्वों कथमहं देव स्तोतुं झक़्नोमि बालक:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1360)
- **Original**: त्वद्धक्तिप्रव्ण ह्वोतत्परमेश्वर मे मन: । स्तोतुं प्रकृत्त त्वत्यादो तत्न प्रज्ञां प्रयच्छ मे
- **Translation**: 

---

