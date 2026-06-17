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

### Verse 1 (Vishnu Puran 0.4841)
- **Original**: 3 तदनेनेववेदानां शाखाभेदाच्द्रिजोत्तम । चतुर्यगेषु पठितान्समस्तेष्बृवधारय
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4842)
- **Original**: 4 भ्रीपराशरजी बोले--सृष्टिके आदिमें ईश्वरसे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4843)
- **Original**: आविर्भूत वेद ऋक्‌ यजुः आदि चार पादौँसे युक्त और एक रुक्त मच्जवाला था। उसीसे समस्त कामनाओंको देनेवाले अम्िहोत्रादि दस प्रकार्के ग्ज्ञॉका भ्रचार हुआ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4844)
- **Original**: तदनन्तर अट्डाईसलें द्वापसयुगमें मेरे पुत कृष्णदैपायनने इस चतुष्पादयुक्त एक हो चेदके चार भाग किये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4845)
- **Original**: परम बुद्धिमान टलेद्व्यासन उनका जिस प्रकार विभाग किया है, ठीक उसी प्रकार अन्यान्य ब्ेदल्यासोंने तथा मेने भो पहले किया था
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4846)
- **Original**: अत्तः हे ट्विज ! समस्त चतर्युगॉर्मे इन्हीं आखाभेटोंस वेदका पाठ होता है--ऐसा जानो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4847)
- **Original**: अब्ड ] 173 कृष्णबैपायन व्यासं बिद्धि नारायणं प्रभुम्‌ । को हान्यो भुवि मैत्रेय महाभारतकृद्धवेत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4848)
- **Original**: 5 तेन व्यस्ता यथा वेदा मत्पुत्रेण महात्मना । द्वापरे छात्र मैत्रेय तस्मिज्छूणु यथातथम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4849)
- **Original**: 6 ब्रह्मणा चोदितो व्यासो वेदाच््यस्तु प्रचक्रमे । अथ छ्षिष्याग्रजग्राह चतुरों बेदपारगानु
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4850)
- **Original**: 7 ऋग्वेद्पाठकं॑ पैले जग्राह स महापुनि: । वैज्वम्पायननामान॑ यजुर्वेदस्थ चाग्रहीत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4851)
- **Original**: 8 जैमिनि सामवेदस्य तथैवाधर्वनेदलित्‌ । सुपन्तुस्तस्य शिष्यो5भूद्वेटव्यासस्य धीमत:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4852)
- **Original**: 9 रोमहर्षणनामानं॑ महाबुद्धि. महासुनि: । सूतं जग्राह ज्िष्यं स इतिहासपुराणयो:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4853)
- **Original**: 10 एक आसीझलजुर्वेदस्तं चतुर्धा व्यकल्पयत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4854)
- **Original**: चातुहेत्रमभूत्तस्मिस्तेवन यज्ञमथाकरोत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4855)
- **Original**: 11 आध्वर्यवं वजुर्भिस्तु ऋग्भिहोत्रं तथा मुनि: । औद़ात्रं सामभिश्क्रे ब्रह्म चाप्यथर्वभि:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4856)
- **Original**: 12 ततस्स ऋच उदलघृत्य ऋग्वेद कृतवान्मुनि: । यजूंषि च यजुर्वेदे सामवेदं थ सामभि:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4857)
- **Original**: 13 राज्ञां चाथर्ववेदेन सर्वकर्माणि ञ्ञ प्रभु: । कारयामास मैत्रेय ब्रह्मत्व॑ च्॒ यथास्थिति
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4858)
- **Original**: 14 सो5यमेको यथा वेदस्तरुस्तेन पृथक्कतः । चतुर्धाथ ततो जात॑ बेदपादपकाननम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4859)
- **Original**: 15 बिभेद॑ प्रथपं विप्र पेलो ऋग्वेदपादपम्‌। इन्द्रप्रमितये प्रादाद्वाष्फकाय च संहिते। 16 चतुर्धा स बिभेदाध बराष्कलो$पि चर संहिताम्‌। बोध्यादिभ्यो ददो ताश्न शिष्येभ्यस्स महामुनिः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4860)
- **Original**: 97 बोध्याभिमाढकों तद्डद्याज़बल्क्यपरादरौ । प्रतिशाखास्तु शाखायास्तस्थास्ते जगृहुर्मुने
- **Translation**: 

---

