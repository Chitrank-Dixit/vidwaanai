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

### Verse 1 (Vishnu Puran 0.1321)
- **Original**: उस निस्य-योगयुक्त बाल्कको भयभीत करनेके लिये अपने मुखसे अग्निकी छपटें निकारती हुई सैकड़ों स्थास्याँ घोर नाद करने लगीं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1322)
- **Original**: वे राक्षसगण भी “इसको मारो-मारों, काटो-काटों, खाओ-खाओ' इस प्रकार चिल्लाने छगे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1323)
- **Original**: फिर सिंह, ऊँट और मकर मआमादिके-से मुखजाले ने राक्षस राजपुत्रको त्राण देनेके लिये नाना प्रकारसे गस्जने लूगे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1324)
- **Original**: किन्तु उस भगवदासक्तचित्त बालकको ये गक्षस, उनके शब्द, स्थारियाँ और अख्ब-झख्बादि कुछ भी दिखायी नहीं दिये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1325)
- **Original**: वह राजपुत्र एकाग्रचित्तसे निरन्तर अपने आश्रयभूत विष्णुभगवान्‌कों ही देखता रहा और
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1326)
- **Original**: आ* 12 ] ततः सर्वासु मायासु बिलीनासु पुनः सुराः । सक्लेभ॑ परम जम्मुस्तत्पराभवशक्िता:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1327)
- **Original**: 31 ते समेत्य जगद्योनिमनादिनिधन हरिम्‌। शरण्यं झरणंं यातास्तपसा तस्य तापिताः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1328)
- **Original**: 32 देवा ऊचुः देखदेव जगन्नाथ परेश पुरुषोत्तम । धुवस्य तपसा तप्तास्त्वां क्‍्य॑ शरण गता:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1329)
- **Original**: 33 दिने दिने कलालेशै: शशाड्र: पूर्यते यथा । तथायं तपसा देव प्रयात्युद्धिमहर्निशम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1330)
- **Original**: 34 औत्तानपादितपसा वयमित्थ जनार्दन । भीतास्त्वां शरण यातास्तपसस्त निवर्तय
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1331)
- **Original**: 35 न विद्य: कि शक्रत्व॑ सूर्यत्व किमभीष्सति । वित्तपाम्बुपसोमानां साभिलाष: पदेषु किप्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1332)
- **Original**: 36 तदस्माक॑ प्रसीदेश हृदयाच्छल्यमुझ्धर । उत्तानपादतनय तपसः. सन्निवर्तय
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1333)
- **Original**: 37 औभपगफ्कनुवाच नेन्वत्व॑ न चर सूर्यत्व॑ं नैवाम्बुपधनेशताम्‌। प्रार्थयत्येष य॑ कार्म त॑ करोम्यखिलं सुराः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1334)
- **Original**: 38 यात देवा यथाकामं स्वस्थार्न विगतज्वरा: । निर्क्तयाम्यह॑बालें तपस्पासक्तमानसम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1335)
- **Original**: 39 श्रीपरारार उनाच इत्युक्ता देवदेबेन प्रणम्य त्रिदशास्ततः । प्रयवुः स्वानि धिष्ण्यानि झतक्रतुपुरोगमा:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1336)
- **Original**: 40 भगवानपि सर्वात्मा तन्मयत्वेन तोषितः । गत्वा ध्रुबमुबाचेदे चतुर्भुजबपुहीरिं:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1337)
- **Original**: 41 औभगयानुवाच औत्तानपादे भद्>गं ते तपसा परितोषितः । बरदो5हमनुप्राप्तो बर॑ वरय सुब्रत
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1338)
- **Original**: 42 बाह्मार्थनिरपेक्ष ते मयि चित्त यदाहितम्‌। तुप्टोडई भवतस्तेन तद्बृणीघ्र॒ बर॑ परम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1339)
- **Original**: 43 श्रीपराश्षर उदाच श्रुल्वेत्थ गदितं तस्य देवदेवस्थ बालक: । उन्मीलिताक्षो ददृशे ध्यानदृष्टे हरि पुरः-
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1340)
- **Original**: ड4ड है उसने किसीकी ओर किसी भी प्रकार दुष्टिपात नहीं किया
- **Translation**: 

---

