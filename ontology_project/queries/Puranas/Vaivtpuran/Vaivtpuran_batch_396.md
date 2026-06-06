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

### Verse 1 (Vaivtpuran 19.19109)
- **Original**: 3» गोपेशाय स्वाहेति स्कन्ध पातु सदा मम्र । नमः किशोरवेधाय स्वाहा पृष्ठ सदावतु
- **Translation**: 

---

### Verse 2 (Vaivtpuran 19.19110)
- **Original**: उदरं पातु मे नित्यं मुकुन्दाय नमः सदा। 30 हीं क्लीं कृष्णाय स्वाहेति करौ पातु सदा मम
- **Translation**: 

---

### Verse 3 (Vaivtpuran 19.19111)
- **Original**: 39 विष्णवे नमो बाहुयुग्म॑ पातु सदा मम
- **Translation**: 

---

### Verse 4 (Vaivtpuran 19.19112)
- **Original**: 30 ह्रीं भगवते स्वाहा नखरं पातु मे सदा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 19.19113)
- **Original**: 3» नमो नारायणायेति नखरन्ध्ं सदाबतु । 30 ह्रीं हीं पद्मनाभाय नाभिं पातु सदा मम
- **Translation**: 

---

### Verse 6 (Vaivtpuran 19.19114)
- **Original**: 3» सर्वेशाय स्वाहेति कड्ढाल॑ पातु में सदा। 30 गोपीरमणाय स्वाहा नितम्ब॑ पातु मे सदा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 19.19115)
- **Original**: 34 गोपीरमणनाथाय पादौ पातु सदा मम । 30 हीं श्री रसिकेशाय स्वाहा सर्व सदावतु
- **Translation**: 

---

### Verse 8 (Vaivtpuran 19.19116)
- **Original**: 3» केशवाय स्वाहेति मप्र केशान्‌ सदावतु । नमः कृष्णाय स्वाहेति ब्रह्मरन्ध॑ सदावतु
- **Translation**: 

---

### Verse 9 (Vaivtpuran 19.19117)
- **Original**: 3» माधवाय स्वाहेति लोमानि में सदायतु । 30 हों श्रीं रसिकेशाय स्वाहा सर्व सदावतु
- **Translation**: 

---

### Verse 10 (Vaivtpuran 19.19118)
- **Original**: परिपूर्णतमः कृष्ण: प्राच्यां मां सर्वबदाबतु । स्वयं गोलोकनाथो मामाग्रेय्यां दिशि रक्षतु
- **Translation**: 

---

### Verse 11 (Vaivtpuran 19.19119)
- **Original**: पूर्णब्रह्मस्वरूपश्ष॒ दक्षिणे मां सदावतु । नैरत्यां पातु मां कृष्ण: पश्चिमे पातु मां हरिः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 19.19120)
- **Original**: गोविन्द: पातु मां शश्वद्‌ बायव्यां दिशि नित्यश:ः । उत्तर मां सदा पातु रसिकानां शिरोमणि:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 19.19121)
- **Original**: ऐशान्यां मां सदा पातु बृन्दावनविहारकृत्‌ । बृन्दावतीप्राणनाथ: . पातु. मामूध्ब॑देशतः
- **Translation**: 

---

### Verse 14 (Vaivtpuran 19.19122)
- **Original**: सदैव माधव: पातु बलिहारी महाबलः
- **Translation**: 

---

### Verse 15 (Vaivtpuran 19.19123)
- **Original**: जले स्थले चान्तरिक्षे नृसिंह: पातु मां सदा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 19.19124)
- **Original**: स्वप्न जागरणे शश्वत्‌ पातु मां माधव: सदा। सर्वान्तरात्मा निर्लिप्त: पातु मां सर्वतों विभु:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 19.19125)
- **Original**: इति ते कधथित॑ वत्स सर्वमन्त्रौधविग्रहम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 19.19126)
- **Original**: त्रैलोक्यविजय॑ नाम कवर्च॑ परमाद्भुतम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 19.19127)
- **Original**: मया श्रुतं कृष्णवक्त्रातू प्रवक्तव्यं न कस्यचित्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 19.19128)
- **Original**: गुरुमभ्यर्ज्य,य विधिवत्‌ कवच धारयेत्तु यः
- **Translation**: 

---

