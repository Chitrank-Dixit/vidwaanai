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

### Verse 1 (Vishnu Puran 0.321)
- **Original**: आप परजद्मयकी ही आराधना करके मुमुक्षुजन मुक्त होते हैं। भला वासुदेवकी आराधना किये बिना कौन मोक्ष प्राप्त कर सकता है ?
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.322)
- **Original**: मनसे जो कुछ अहण (संकल्प) किया जाता है, चक्षु आदि इन्द्रियोंसे जो कुछ ग्रहण (जिषय) करनेयोग्य है, बुद्धिद्वारा जो कुछ विचारणीय है वह सब आपहीका रूप है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.323)
- **Original**: हे प्रभो! मैं आपस्लैन्ध् रूप हूँ, आपहके आश्रित हूँ और आपहीके द्वा रची गयी हूँ तथा आपहीकी दारणमें हूँ। इसीलिये लोकमें मुझे माधवी' भी कहते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.324)
- **Original**: हे सम्पूर्ण ज्ञानमय ! हे रथूलमय ! हे अव्यय ! आपकी जय हो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.325)
- **Original**: है अनन्त ! हे अव्यक्त ! हे व्यक्तमय प्रभो ! आपकी जय हो
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.326)
- **Original**: हे परापर-स्वरूप
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.327)
- **Original**: हे विश्वात्नन! हे यज्ञपते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.328)
- **Original**: हे अनथ ! आपकी जय हो । हे प्रभो । आप ही गज्ञ है, आप हो वषदकर हैं,आप ही ओंकार हैं और आप ही (आहवनीयादि) अभ्रियाँ हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.329)
- **Original**: है हरे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.330)
- **Original**: आप हो येद, बेदाग और यज्पुरुष हैं तथा सूर्य आदि ग्रह, तारे, नक्षत्र और सम्पूर्ण जगत्‌ भी आप ही हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.331)
- **Original**: हे पुरुषोत्तम ! हे परमेश्वर ! सूर्त-अमूर्त, डृइ्य-अदृद्य तथा जो कुछ मैंने कहा है और जो नहीं कहा, वह सब आप ही हैं। अतः आपको नमस्कार है, बारम्बार नमस्कार है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.332)
- **Original**: श्रीपराश्रजी बोलछे--पृथिवीद्वारा इस प्रकार स्तुति किये जानेपर सामस्वर ही जिनकी ध्वनि है उन भगवान्‌ धरणीधरने घर्घर शब्दसे गर्जना की
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.333)
- **Original**: फिर बविकसित कमलके समान नेत्रॉंबाले उन महावगहने अपनी डाढ्ोंसे पृथिवीको उठा लिया और बे कमल-दल्के समान क्याम तथा नीलाचलके सदृत्ञ विशालकाय भगवान्‌ रसातलसे बाहर निकले
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.334)
- **Original**: निकलते समय उनके मुखके श्वाससे ठछलते हुए जलने जनलोकमें रहनेवाले मसहातेजस्वी और निष्पाप सनन्‍दनादि सुनौश्चरोक्त्र सिगो दिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.335)
- **Original**: जर थड्टा शब्द करता हुआ उनके खुरेंसे विदीर्ण हुए रसातलमें नीचेकी ओर जाने रूगा और जनस्प्रेकमें रहनेवाले सिद्धमणण उनके श्वास-वायुसे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.336)
- **Original**: अन्ड ] उत्तिष्ठतस्तस्थ जलार्दकुक्षे- महावराहस्य महीं विधुन्चतोी बेदमयं शारीरें रोमान्तरस्था मुनयः स्तुवन्ति
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.337)
- **Original**: 29 तुष्टवुस्तोषपरीतचेतसो चिगृह्या । ते षप छोके जने ये निवसन्ति योगिन: । सननन्‍्दनाद्या. छ्यतिनप्रकन्धरा धराधर धीरतरोद्धतेक्षणम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.338)
- **Original**: 30 जयेश्वराणां परमेश केशव प्रभो गदाशद्भुधरासिचक्रधक्‌ । प्रसूतिनाशस्थितिहेतुरीश्चर- स्त्वमेव नान्यत्परमं चर यत्पदम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.339)
- **Original**: 31 ह॒ताशजिल्लोइसि. तनूरुहाणि दर्भा: प्रभो यज्ञपुमांस्त्वमेव
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.340)
- **Original**: 32 बिलोचने रात़्यहनी महात्य- स्सर्वाश्रय॑ ब्रह्म पर॑ शिरस्ते । सूक्तान्यशेषाणि सटाकलापो पघ्राणं समस्तानि हींषि देव
- **Translation**: 

---

