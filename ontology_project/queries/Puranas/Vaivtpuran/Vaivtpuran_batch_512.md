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

### Verse 1 (Vaivtpuran 29.7438)
- **Original**: 3» कृष्णाय. दन्तरन्ध॑ दन्तोध्व॑ लीं सदावतु । 3* श्रीकृष्णाय स्वाहेति जिद्निकां पातु मे सदा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 29.7439)
- **Original**: रासेश्वराय. स्वाहेति तालुक॑ पातु मे सदा । राधिकेशाय स्वाहेति कण्ठे पातु सदा मम
- **Translation**: 

---

### Verse 3 (Vaivtpuran 29.7440)
- **Original**: मो गोपाडुनेशाय वक्ष: पातु सदा मम । 3 गोपेशाय स्वाहेति स्कन्थ पातु सदा मम
- **Translation**: 

---

### Verse 4 (Vaivtpuran 29.7441)
- **Original**: नम: किशोरबेशाय स्वाहा पृष्ठ॑ सदावबतु । उदरं पातु में नित्यं मुकुन्दाय नमः सदा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 29.7442)
- **Original**: 3» हीं क्लीं कृष्णाय स्वाहेति करी पादी सदा मम
- **Translation**: 

---

### Verse 6 (Vaivtpuran 29.7443)
- **Original**: 3* विष्णबे नमों बाहुयुग्म॑ पातु सदा मम
- **Translation**: 

---

### Verse 7 (Vaivtpuran 29.7444)
- **Original**: 35 हां भगवते स्वाहा नखरं पातु में सदा। 3& नमो नारायणायेति नखरन्श्न सदावतु
- **Translation**: 

---

### Verse 8 (Vaivtpuran 29.7445)
- **Original**: 3 हो हो पद्मनाभाय नाभि पातु सदा मम। 3» सर्वेशाय स्वाहेति कड्भाल॑ पातु मे सदा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 29.7446)
- **Original**: 3» गोपीरमणाय स्वाहा नितम्बं पातु मे सदा । 3» गोपीरमणनाथाय पादौ पातु सदा मम
- **Translation**: 

---

### Verse 10 (Vaivtpuran 29.7447)
- **Original**: 3$ हो श्रीं रसिकेशाय स्वाहा सर्व सदावतु । 3> केशवाय स्वाहेति मम केशान्‌ सदावतु
- **Translation**: 

---

### Verse 11 (Vaivtpuran 29.7448)
- **Original**: नमः कृष्णाय स्वाहेति ब्रहारन््5न॑ सदावतु । *» माधवाय स्वाहेति लोमानि मे सदावतु
- **Translation**: 

---

### Verse 12 (Vaivtpuran 29.7449)
- **Original**: 3» हीं श्रों रसिकेशाय स्वाहा सर्व सदावतु
- **Translation**: 

---

### Verse 13 (Vaivtpuran 29.7450)
- **Original**: परिपूर्णतम:. कृष्ण: .प्राच्यां मां सर्वदावतु । स्वयं गोलोकताथो मामाग्लेय्यां दिशि रक्षतु
- **Translation**: 

---

### Verse 14 (Vaivtpuran 29.7451)
- **Original**: पूर्णग्रह्मस्वरूपश दक्षिणे. मां सदावतु । नैरऋत्यां पातु मां कृष्ण: पक्चिमे पातु मां हरि:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 29.7452)
- **Original**: गोविन्द: पातु मां शश्वद्‌ वायब्यां दिशि नित्यश:। उत्तरे मां पातु रसिकानां शिरोमणि:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 29.7453)
- **Original**: ऐशान्यां मां सदा पातु वृन्दावनविहारकृत्‌ पातु सदैव माधव: पातु बलिहारी महाबल: । जले स्थले चान्तरिक्षे नृसिंह: पातु मां सदा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 29.7454)
- **Original**: स्वप्रे जागरणे शश्नवत्‌ पातु मां माधव: सदा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 29.7455)
- **Original**: सर्वान्तरात्मा निर्लिमतों रक्ष मां सर्वतों विभु:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 29.7456)
- **Original**: इति ते कथित वत्स सर्वमन्त्रौषधिग्रहम्‌ । त्रैलोक्वविजयं नाम कवच परमाद्धुतम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 29.7457)
- **Original**: मवा ब्रुतं कृष्णवक्त्रातू प्रवक्तव्य॑ न कस्यचित्‌ । गुरुमभ्यर्च्य विधिवत्‌ कवच धारयेत्‌ तु यः
- **Translation**: 

---

