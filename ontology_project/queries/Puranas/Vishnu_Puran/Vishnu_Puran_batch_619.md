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

### Verse 1 (Vishnu Puran 0.12361)
- **Original**: 46 हिपरार्द्धात्मक: काल: कथितो यो मया तब । तदहस्तस्य॒मैत्रेय विष्णोरीशस्य कथ्यते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12362)
- **Original**: 47 व्यक्ते च प्रकृतो लीने प्रकृत्यां पुर॒ुषे तथा । तत्र स्थिते निशा चास्य तत्ममाणा महामुने
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12363)
- **Original**: 48 नैबाहस्तस्य न निश्ञा नित्यस्थ परमात्मनः । उपचारस्तथाप्येष तस्थेशस्य॒द्विजोच्यते
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12364)
- **Original**: 49 इत्येष तब मैत्रेय कथित: प्राकृतों लयः । आत्यन्तिकमथो ब्रह्मश्निबोध प्रतिसझ्लरम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12365)
- **Original**: 50 और वचेदान्तोंमें विष्णुनामसे बर्णन किया है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12366)
- **Original**: वैदिक कर्म दो प्रकारका है--प्रवृत्तिरूप (कर्मबोग) और निवुत्तिरूप (साख्ययोग) । इन दोनों प्रकारके कर्मेंसि उस सर्वभूत पुरुषोत्तमका ही यजन किया जाता है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12367)
- **Original**: ऋक्‌, यजुः और सामवेदोक्त प्रवृत्ति-मार्ससे लोग उन यज्ञपति पुरुषोत्तम यज्ञ-पुरुषका ही पूजन करते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12368)
- **Original**: तथा निवृत्ति-सार्गमें स्थित योगिजन भी उन्हीं ज्ञानात्मा ज्ञानस्वरूप मुक्ति-फल-दायक भगवान्‌ विष्णुका हो ज्ञानयोगद्वारा यजन करते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12369)
- **Original**: हस्व, दीर्घ और घ्रुत--इन त्रिविध स्वरॉसे जो कुछ कहा जाता है तथा जो वाणीका विषय नहीं है वह सब भी अव्ययात्मा विष्णु ही है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12370)
- **Original**: वह विश्वकप घारी विश्वरूप परमात्मा श्रीहरि ही व्यक्त, अव्यक्त एवं अचिनाशों पुरुष हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12371)
- **Original**: हे मैत्रेय ! उन सर्वव्यापक और अधिकृतरूप परमात्मामें ही व्यक्ताव्यक्तरूपिणी प्रकृति और पुरुष ल्तैन हो जाते हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12372)
- **Original**: हे मैत्रेय ! मैंने तुमसे जो द्विपरा्द्धकाल कहा है वह उन विष्णुभगबानका केबल एक दिन है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12373)
- **Original**: हे महामुने ! व्यक्त जगत्‌के अव्यक्त-प्रकृतिमें और प्रकृतिके पुरुषमें लीन हो जानेपर इतने ही कालकी विष्णुभगवानकी रात्रि होती है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12374)
- **Original**: हे द्विज ! वास्तवमें तो उन नित्य परमात्माका न कोई दिन है और न रात्रि, तथापि केवक् उपचार (अध्यारोप) से ऐसा कहा जाता है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12375)
- **Original**: है मैत्रेय ! इस प्रकार मैंने तुमसे यह प्राकृत प्ररयका वर्णन किया, अब तुम आत्यन्तिक प्रकुयका वर्णन और सुनो
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12376)
- **Original**: क्क्त्जज औ पाए इति श्रीविष्णुपुराणे षष्ठेंडशें चतुर्थोंड्ध्याय:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12377)
- **Original**: 3-+-__ -जैर्‌ 00000 पाँचवाँ अध्याय आध्यात्मिकादि त्रिविध तापोंका वर्णन, भगवान्‌ तथा वासुदेव शब्दोंकी व्याख्या और भगवानके पारमार्थिक स्वरूपका वर्णन अपराशर उवाच आध्यात्मिकादि मैत्रेय ज्ञात्वा तापत्रयं बुध: । श्रीपराशरजी बोले--हे मैत्रेय ! आध्यात्मिक, आधिदेधिक और आधिभौतिक तीनों तापोंकों जानकर उत्पन्नज्ञानवैराग्य: प्राप्नोत्यात्यन्तिक लयम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12378)
- **Original**: शान और वैराग्य उत्पन्न होनेपर पण्डितजन आत्यन्तिक आध्यात्मिको5पि द्विविधइशारीरो मानसस्तथा । प्रकृय॒प्राप्त करते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12379)
- **Original**: आध्यात्मिक ताप आरोरिक और मानसिक दो प्रकारके होते हैं; उनमें शारीरो बहुप्रिभ्रेंदेर्शिद्योते श्रूयततां च सः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12380)
- **Original**: शारीरिक तापके भी कितने ही भेद हैं, वह सुनो
- **Translation**: 

---

