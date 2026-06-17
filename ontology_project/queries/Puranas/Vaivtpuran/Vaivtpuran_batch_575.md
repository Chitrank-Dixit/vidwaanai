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

### Verse 1 (Vaivtpuran 44.17811)
- **Original**: त्व॑ ज्योति: परम॑ ख्रह्म सगुणो निर्गुण: स्वयम्‌ । गुणभेदान्मूर्तिभेदो ब्रह्मविष्णुशिवात्मक:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 44.17812)
- **Original**: बलिद्वारे गदापाणि: स्वयमेव भवान्‌ प्रभो । स्वयं प्रदत्ता शक्राय तस्मै श्रीरपि लीलया
- **Translation**: 

---

### Verse 3 (Vaivtpuran 44.17813)
- **Original**: क्षमस्त्॒ भगवज्छाभो हर क्रोध च्र॒ संहर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 44.17814)
- **Original**: किं पौरुषं च भवतो ब्लाह्मणस्यापि हिंसया
- **Translation**: 

---

### Verse 5 (Vaivtpuran 44.17815)
- **Original**: अहं जीवज्छरीरिण न दास्यामि निशाकरम्‌ । शरणागतदीनात॑ लज्जित॑ पापसंयुतम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 44.17816)
- **Original**: अहं च॒ त्वत्पदाम्भोजे शरणं यामि शंकर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 44.17817)
- **Original**: यथोचितं कुरु बिभो जगत्‌ सर्ब॑ तथैब च
- **Translation**: 

---

### Verse 8 (Vaivtpuran 44.17818)
- **Original**: शुक्रस्य वचन श्रुत्वा प्रसन्नो भगवाउिछव: । डत्युक्ता च॒ निशानाथं समानय शुभ भवेतू
- **Translation**: 

---

### Verse 9 (Vaivtpuran 44.17819)
- **Original**: इति श्रीब्रह्मवैवर्ते शुक्रकृतं शिवस्तोत्रं सम्पूर्णम्‌ ( श्रीकृष्णजन्मखण्ड 81
- **Translation**: 

---

### Verse 10 (Vaivtpuran 44.17820)
- **Original**: 35-42) 438 सपर4000500
- **Translation**: 

---

### Verse 11 (Vaivtpuran 44.17844)
- **Original**: # श्रीदुर्गास्तोत्राणि * 789 कक कक ऋऋ कक क्ऋ5%%% 54% ####%###%#9%%####%### 4 #%% 4 ##%ऋऋ%% 3» हूं श्रीं क्‍्लीं सर्वपूज्ये देवि मड्रलचण्डिके । ऐं क्र फद्‌ स्वाहेत्येव॑ चाप्येकविंशाक्षरों मनु:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 44.17845)
- **Original**: पूज्य: कल्पतरुझ्लैवभक्तानां सर्वकामद: । दशलक्षजपेनैव मन्ब्नसिद्धधिर्भवेश्वणाम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 44.17846)
- **Original**: मन्त्रसिद्धिर्भवेद्‌ वस्थ स॒॒ विष्णु: सर्वकामदः । ध्यानं च श्रूयतां ब्रह्मन्‌ वेदोक्त॑ सर्वसम्मतम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 44.17847)
- **Original**: देवीं षोडशवर्षीयां शश्रत्सुस्थिरयौजनाम्‌ । सर्वरूपगुणाद्यां च कोमलाडु मनोहराम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 44.17848)
- **Original**: श्रेतचम्पकवर्णाभां अन्द्रकोटिसमप्रभाम्‌ । वह़िशुद्धांशुकाधानां रलभूषणभूषिताम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 44.17849)
- **Original**: बिभ्रतीं कबरीभारं मल्लिकामाल्यभूषितम्‌ । विम्बोष्ठी सुदर्ती शुद्धां शरत्पद्मनिभाननाम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 44.17850)
- **Original**: ईषद्धास्यप्रसन्नास्यां. सुनीलोत्यललोचनाम्‌ । जगद्धात्री च दात्रीं च॒ सर्वेभ्य: सर्वसम्पदाम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 44.17851)
- **Original**: संसारसागरे घोरे पोतरूपां वरां भजे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 44.17852)
- **Original**: देव्याश्न ध्यानमित्येव॑ स्तवनं श्रूयतां मुने । प्रयतः सड्डूटग्रस्तो येन तुष्टाव शंकरः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 44.17853)
- **Original**: शंकर उवाच रक्ष रक्ष जगन्मातर्देवि मड्गलचण्डिके । हारिके विपदां. राशेईर्षमड्रलकारिके
- **Translation**: 

---

