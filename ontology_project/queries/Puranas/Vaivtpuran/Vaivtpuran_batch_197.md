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

### Verse 1 (Vaivtpuran 13.10082)
- **Original**: डएड ] संक्षिप्त ब्रह्मवैवर्तपुराण + 45% ऋ
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10083)
- **Original**: ऋऋ#ऋ #% % 8 % 6 4 4 #% #% 46 6566 8££ 4 # 4 4 ££ £ $ # # % ऋ ऋ ऋक 4 ऊ 5 कक ऋ़ कर ऋ # ऋ ऋक कक # 4 4 % 6 धर ऋ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10084)
- **Original**: 8 # # ह इन्द्रयागकी परम्पराका भंजन, इन्द्रके कोपसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10085)
- **Original**: बन्धु-बान्धवोंको ज्ञानोपदेश देकर उनका शोक दूर गोकुलकी रक्षा, गोपियोंके वस्त्रोंका अपहरण,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10086)
- **Original**: करेंगे। इसके बाद अपने भाईका और अपना उनके ब्रतका सम्पादन, पुनः उन्हें वस्त्र अर्पण
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10087)
- **Original**: उपनयन-संस्कार कराकर गुरुके मुखसे विद्या तथा मनोबाज्छित बरदान देनेका कार्य करके ये
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10088)
- **Original**: ग्रहण करेंगे। गुरुजीको उनका मरा हुआ पुत्र श्यामसुन्दर अपनी लीलाओंसे उनके चित्तको चुरा लाकर देंगे और फिर घर लौट आयेंगे। इसके लेंगे और उन्हें सर्वधा अपने अधीन कर लेंगे।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10089)
- **Original**: बाद राजा जरासंधके सैनिकोंको चकमा देकर तदनन्तर इनके द्वारा अत्यन्त रमणीय रासोत्सवका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10090)
- **Original**: दुरात्मा कालयवनका वध, द्वारकापुरीका निर्माण, आयोजन होगा, जो सबका आनन्दवर्धन करेगा।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10091)
- **Original**: मुचुकुन्दका उद्धार तथा यादवॉसहित द्वारकापुरीको शरद्‌ और वसनन्‍्त ऋतुमें रातके समय पूर्ण
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10092)
- **Original**: प्रस्थान करेंगे। वहाँ कौतूहलवश स्त्रीसमूहोंके चन्द्रमाका उदय होनेपर रासमण्डलमें गोपियोंकों
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10093)
- **Original**: साथ विवाह करके उनके साथ क्रीडा-विहार नूतन प्रेम-मिलनका सुख प्रदान करके ये श्यामसुन्दर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10094)
- **Original**: करेंगे। उनका तथा उनके पृत्र-पौत्रादिका सौभाग्यवर्धन उनका मनोरथ पूर्ण करेंगे। फिर कौतृहलवश
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10095)
- **Original**: करेंगे। मणिसम्बन्धी मिथ्या कलड्डूका मार्जन, उनके साथ जल-विहार भी करेंगे। तत्पश्चात्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10096)
- **Original**: पाण्डबोंकी सहायता, भूभार-हरण, धर्मपुत्र राजा श्रीदामाके शापके कारण इनका गोप-गोपियों तथा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10097)
- **Original**: युधिष्ठिरके राजसूययज्ञका लीलापूर्वक सम्पादन, श्रीराधाके साथ (पार्थिव) सौ वर्षोके लिये वियोग [पारिजातका अपहरण, इन्द्रके गर्वंका गड्जन, हो जायगा। उस समय ये मथुरा चले जायँगे और सत्यभामाके ब्रतकी पूर्ति, बाणासुरकी भुजाओंका वहाँ इनका जाना गोपियोंके लिये शोकवर्द्धक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10098)
- **Original**: खण्डन, शिवके सैनिकोंका मर्दन, महादेवजीको होगा। उस समय पुनः ये उनके पास आकर उन्हें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10099)
- **Original**: जृम्भणास्त्रसे बाँधना, बाणपुत्री उघाका अपहरण, समझा-बुझाकर घैर्य बँधायेंगे और आध्यात्मिक अनिरुद्धको बाणासुरके बन्धनसे छुटकारा दिलाना, ज्ञान प्रदान करेंगे। उस प्रबोधन और आध्यात्मिक
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10100)
- **Original**: वाराणसीपुरीका दहन, ब्राह्मणकी दरिद्रताका दूरीकरण, ज्ञानके द्वारा ये रथ तथा सारथि अक्रूरकी रक्षा एक ब्राह्मणके मरे हुए पुत्रोंकों लाकर उसे देना, करेंगे। फिर रथपर आरूढ़ हो पिता, भाई एवं
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10101)
- **Original**: दुष्टोंका दमन आदि करना तथा तीर्थयात्राके ब्रजवासियोंके साथ यमुनाजीकों लाँघकर ब्रजसे प्रसड्रसे तुम त्रजवासियोंके साथ पुनः मिलना मथुराको पधारेंगे। मार्गमें यमुनाजीके जलके
- **Translation**: 

---

