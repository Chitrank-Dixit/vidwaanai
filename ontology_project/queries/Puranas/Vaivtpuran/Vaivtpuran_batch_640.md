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

### Verse 1 (Vaivtpuran 65.18867)
- **Original**: तायत्कालं पुनस्तप्त्वा वर प्राप ददर्श तम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 65.18868)
- **Original**: ईदृ्श॑ परमेशं च द्रक्ष्याम्यद्या तमुद्धव
- **Translation**: 

---

### Verse 3 (Vaivtpuran 65.18869)
- **Original**: पुरा शम्भुस्तपस्तेपे यावद्धे ज्रह्मणो बय: । ज्योतिर्मण्डलमध्ये चर गोलोके त॑ ददर्श सः
- **Translation**: 

---

### Verse 4 (Vaivtpuran 65.18870)
- **Original**: सर्व॑तत्त्व॑ सर्वसिद्धं मम तत्त्य॑ परे वरम्‌ । सम्प्राप तत्पदाम्भोजे भक्ति च निर्मलां पराम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 65.18871)
- **Original**: चकारात्मसमं ते च यो भक्त भक्तवत्सल: । ईदृशं परमेशं च॒ द्रक्ष्याम्यद्य तमुद्धव
- **Translation**: 

---

### Verse 6 (Vaivtpuran 65.18872)
- **Original**: सहस््रशक्रपातान्त॑ निराहारः कृशोदरः । यस्यानन्तस्तपस्तेपे भक्‍त्या त्ञ॒ परमात्मन:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 65.18873)
- **Original**: तदा चात्मसमं ज्ञानं ददौ तस्मै य इंश्वरः । ईंदृशं परमेश च द्॒क्ष्याम्यद्य तमुद्धव
- **Translation**: 

---

### Verse 8 (Vaivtpuran 65.18874)
- **Original**: सहस्रशक्रपातान्त॑ धर्मस्तेपे च यत्तप: । तदा बभूव साक्षी स॒ श्र्मिणां सर्वकर्मिणाम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 65.18875)
- **Original**: शास्ता च फलदाता चअ्र यत्प्रसादान्वृणामिह । सर्वेशमीदृशमहो द्रक्षाम्यद्य तपमुद्धव
- **Translation**: 

---

### Verse 10 (Vaivtpuran 65.18876)
- **Original**: अष्टाविंशतिरिनद्राणां पतने. यहिबानिशम्‌ । एवं क्रमेण मासाब्दे: शताब्द ब्रह्मणो बय:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 65.18877)
- **Original**: अहो यस्य निमेषेण ब्रह्मण: पतन भवेत्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 65.18878)
- **Original**: ईद परमात्मानं. द्रक्ष्याम्यद्य.. तपुद्धव
- **Translation**: 

---

### Verse 13 (Vaivtpuran 65.18879)
- **Original**: नास्ति भूरजसां संख्या यथैव ब्रह्मणां तथा। तथैव बन्धो विश्वानां तदाधारो महाविराट्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 65.18880)
- **Original**: विश्वे विश्वे च॒ प्रत्येक ब्रह्मविष्णुशिवादय:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 65.18881)
- **Original**: मुनयों मनवः सिद्धा मानवाद्याश्चराचरा:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 65.18882)
- **Original**: यतषोडशांश: स विराद सृष्टो नष्टश्न॒ लीलया
- **Translation**: 

---

### Verse 17 (Vaivtpuran 65.18883)
- **Original**: ईंदृ्श सर्वशास्तारं द्रक्ष्याम्यद्य.. तमुद्धव
- **Translation**: 

---

### Verse 18 (Vaivtpuran 65.18884)
- **Original**: इत्येवमुक्त्वाक्ूरश् पुलकाझ्नितविग्रह: । मूर्च्छां प्राप साथ्रुनेत्रों दध्यौँ तच्यरणाम्बुजम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 65.18885)
- **Original**: बभूव भक्तिपूर्णश्र स्मार॑ स्मारं पदाम्बुजम्‌ । कृत्वा प्रदक्षिणं बापषि कृष्णस्य परमात्पन:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 65.18886)
- **Original**: उद्धवश्च॒ तमाश्लिष्य प्रशशंस पुनः पुन:।स च शीघ्र ययौ गेहमक़ूरोईपि स्वमन्दिरे
- **Translation**: 

---

