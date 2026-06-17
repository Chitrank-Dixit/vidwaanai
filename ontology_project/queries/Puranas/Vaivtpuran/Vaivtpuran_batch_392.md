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

### Verse 1 (Vaivtpuran 19.17760)
- **Original**: कारागारे5पि बद्धो यो नैव प्राप्नोति निर्वुतिम्‌ । स्तोत्र श्रुत्वा मासपेक॑ मुच्यते बन्धनाद्‌ ध्रुवम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 19.17761)
- **Original**: भ्रष्टाज्यो लभेद्‌ राज्यं भक्त्या मास श्रूणोति य:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 19.17762)
- **Original**: मास श्रुत्वा संयतश्न॒ लभेद्‌ भ्रष्टधनो धनम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 19.17763)
- **Original**: यश्ष्मग्रस्तो वर्षमेकमास्तिको यः श्रुणोति चेत्‌ । निश्चित. मुच्यते. रोगाच्छंकरस्थ प्रसादतः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 19.17764)
- **Original**: य: श्रृणोति सदा भक्त्या स्तवराजमिपं द्विज । तस्यासाथ्यं त्रिभुवने नास्ति किंचिच्य शौनक
- **Translation**: 

---

### Verse 6 (Vaivtpuran 19.17765)
- **Original**: कदाचिद्‌ बन्धुविच्छेदो न भवेत्‌ तस्य भारते । अचल. परमैश्वय लभते. नात्र. संशयः:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 19.17766)
- **Original**: सुसंयतो5तिभक्त्या च मासमेक॑ थ्रूणोति य: । अभायों लभते भायाँ सुविनीतां सत्ती बराम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 19.17767)
- **Original**: महामूर्खश्च दुर्मेधो मासमेक॑ श्रणोतिय: । बुद्धि. विद्यां च लभते गुरूपदेशमात्रत:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 19.17768)
- **Original**: कर्मदुःखी दरिद्रश्न मासं भकत्या श्रेणोतिय: । ध्रुवं॑ वित्त भवेत्‌ तस्य शंकरस्यप्रसादतः
- **Translation**: 

---

### Verse 10 (Vaivtpuran 19.17769)
- **Original**: इहलोके सुखं भुक्‍्त्बा कृत्वा कीर्ति सुदुर्लभाम्‌ । नानाप्रकारधर्म च॒ यात्यन्ते शंकरालयम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 19.17770)
- **Original**: पार्षदप्रवरों भूत्वा सेबते तत्र शंकरम्‌ । यः श्रृणोति त्रिसंध्ये॑ च नित्य स्तोत्रमनुत्तमम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 19.17771)
- **Original**: इति श्रीत्रह्मवैवर्ते गाणासुरकृतं शिवस्तोत्रं सम्पूर्णम्‌। (ब्रह्मखण्ड 19। 55-80) 870“ 2#2:690000
- **Translation**: 

---

### Verse 13 (Vaivtpuran 19.17821)
- **Original**: छ8ड- + संक्षिप्त ब्रह्मवैवर्तपुराण «» 30404020.00.0044 2 8 00000 0/00/000004
- **Translation**: 

---

### Verse 14 (Vaivtpuran 19.17822)
- **Original**: / 00 /4///000/0044804//
- **Translation**: 

---

### Verse 15 (Vaivtpuran 19.17823)
- **Original**: 4 4 4 4.4. । $$5$%5$5# 3.44. 0 /
- **Translation**: 

---

### Verse 16 (Vaivtpuran 19.17824)
- **Original**: / /0 2 020402। //
- **Translation**: 

---

### Verse 17 (Vaivtpuran 19.17825)
- **Original**: 8 6 82
- **Translation**: 

---

### Verse 18 (Vaivtpuran 19.17826)
- **Original**: मन्त्रसहितं संसारपावनं शिवकवचम्‌ सौतिरुवाच शिवस्यथ कवच स्तोत्र भ्रूयतामिति शौनक । वसिष्ठेन च यददत्तं गन्धर्वाय चर यो मनुः
- **Translation**: 

---

### Verse 19 (Vaivtpuran 19.17827)
- **Original**: 37 नमो भगवते शिवाय स्वाहेति च मनु: । दत्तो यसिष्ठेन पुरा पुष्के कृपया विभो
- **Translation**: 

---

### Verse 20 (Vaivtpuran 19.17828)
- **Original**: अयं मन्त्रो राबणाय प्रदत्तो ब्रह्मणा पुरा
- **Translation**: 

---

