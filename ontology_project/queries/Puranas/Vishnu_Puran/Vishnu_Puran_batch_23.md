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

### Verse 1 (Vishnu Puran 0.441)
- **Original**: 25 आ्ाकृता बैकृताशैव जगतो पूलहेतव: । सुजतो जगदीदास्थ किमन्यच्छेतुमिच्छसि
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.442)
- **Original**: 26 अमेषेय उयाय सब्डेपात्कथित: सर्गो देवादीनां मुने त्वया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.443)
- **Original**: विस्तराच्छ़तुमिच्छापि त्वत्तो मुनिवरोत्तम
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.444)
- **Original**: 27 अीपश्शर उयाच कर्मप्रर्भाविता: पूं: कुशछाकुशलैस्तु ता; । चौथा मुख्यसर्ग है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.445)
- **Original**: पर्वत-व॒क्षादि स्थाबर हों मुख्य सर्गके अत्तर्गत हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.446)
- **Original**: पाँचवाँ जो तिर्यक्‌स्तोत्त नतत्रया उसे तिर्यक्‌ (कौट-पतंगादि) योनि थी कहते हैं। फिर छठा सर्ग ऊर्ध्य-ल्लोताओंका है जो 'देवसर्ग' कहलाता है। डसके पक्षात्‌ सातवां सर्ग अर्वाकृ-स्ोताओंका है, वह मुष्य सर्म है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.447)
- **Original**: आठवोँ अनुमह-सर्ग है । बट स्रात्विक और ताप्स्लिक है । ये पाँच वैकृत (विकारों) सर्ग है और पहले तीन 'प्राकृत सर्ग' कहत्जते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.448)
- **Original**: गनाँ कौमार-सर्ग है जो प्राकृत और वैकृत भी है। इस प्रकार सृष्टि-स्चनामें प्रवृत्त हुए जगदीश्वर प्रजापतिके प्राकृत और चैकुत नामक थे जगवके मूलभूत नो सर्ग तुम्हें सुजाये। अब और क्या सुनना चाहते हो 7
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.449)
- **Original**: श्रीमैत्रेयजी घोले--- हे मुने ! आपने इन देल्लादिकोंके सागौंका संक्षेपसे बर्णन क्रिया । अब, है मुनिश्रेष्ठ ! मैं इन्हें
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.450)
- **Original**: आपफे मुद्यारविन्दसे सिल्तारपूर्वक सुनना चाहता दूँ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.451)
- **Original**: श्रीपराइरजी बोले--हे मैतेश ! सम्पूर्ण प्रजा ख्यात्या तया ह्वा्निमुक्ता: संहारे छ्युपसंहता:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.452)
- **Original**: अपने ूर्च-शुभाशुभ क्मोसे युक्त है; अतः प्रक्रयकालमें स्थावरान्ताः सुग़द्यास्तु प्रजा ब्रह्म॑श्चतुर्विधा: । ब्रह्मण: कुर्बत: सृष्टि जज्ञिरे मानसास्तु ता;
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.453)
- **Original**: 29 ततो देवासुरपितृत्मनुष्यांक्ष चतुष्टयम्‌ । सिसृक्षरम्भांस्यतानि स्वमात्मानमबूयुजत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.454)
- **Original**: 30 युक्तात्मनस्तपोमात्रा. झयुद्रिक्ता3भूल्मजापते: । सिसृक्षोर्जधनात्पूर्वमसुरा जज्ञिरि ततः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.455)
- **Original**: 39 उत्ससर्ज ततस्तां तु तप्तोमात्रात्मिकों तनुम्‌। सा तु स्यक्ता तनुस्तेन मैत्रेयाभूद्विभावरी
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.456)
- **Original**: 39 सिसंक्षुरन्यदेहस्थ: प्रीतिमाप ततः सुरा: । सत्त्वोद्रिक्ता: समुद्धूता मुखतो ब्रह्मणो द्विज
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.457)
- **Original**: 33 त्यक्ता सापि लनुस्तेन सत्त्वप्रायमभूदिनम्‌। ततो हि बलिनों रात्रावसुरा देवता दिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.458)
- **Original**: 34 सत्त्वमात्रात्स्किमेल ततोन्यां जगृहे तनुम््‌ । पितृबन्भन्यमानस्य पितरस्तस्थ जज्षिरे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.459)
- **Original**: 375 उत्ससर्ज ततर्तां तु पितृन्सृष्ठापि स प्रभु: । सा चोत्सृष्टाभवत्सन्ध्या दिननक्तान्तरस्थिता
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.460)
- **Original**: 36 रजोमात्रात्मिकामन्यां जगृहे स तनु ततः। सजोमात्रोत्कटा जाता पनुष्या द्विजसत्तम
- **Translation**: 

---

