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

### Verse 1 (Vaivtpuran 19.18666)
- **Original**: नागपत्ीकृतं स्तोत्र त्रिसंध्य॑यः पठेन्नर:। सर्वपापात्‌ प्रमुक्तस्तु यात्यन्ते श्रीहरें: पदम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 19.18667)
- **Original**: इहलोके हरेर्भक्तिमन्ते दास्य॑ लभेद्‌ श्रुवम्‌। लभते पार्षदों भूत्ता सालोक्यादिचतुष्टयम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 19.18668)
- **Original**: ड्ति श्रीब्रह्मवैवर्ते नागप्त्री कृत श्रीकृष्णस्तोत्रं सम्पूर्णम्‌। (श्रीकृष्णजन्मखण्ड 19। 17--34) भय कालियकृतं श्रीकृष्णस्तवनम्‌ कालिय उबाच वरे5न्यस्मिन्‌ू मम विभो वाजञ्छा नास्ति वरप्रद
- **Translation**: 

---

### Verse 4 (Vaivtpuran 19.18669)
- **Original**: भक्ति स्मृति त्वत्पदाब्जे देहि जन्मनि जन्मनि। जन्म ब्रह्मकुले वबापि तिर्यग्योनिषु वा समम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 19.18670)
- **Original**: तद्‌ भवेत्‌ सफल यत्र स्मृतिस्त्वच्चरणाम्बुजे । स निष्फल: स्वर्गवासों नास्ति चेत्‌ त्वत्पदस्मृति:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 19.18671)
- **Original**: त्वत्पादध्यानयुक्तस्थ यत्तत्‌ स्थान च तत्परम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 19.18672)
- **Original**: क्षणं वा कोटिकल्पं वा पुरुषायु: क्षयोउस्तु बा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 19.18673)
- **Original**: यदि त्वत्सेवया याति सफलो निष्फलोउन्यथा। तेषां चायुर्व्ययो नास्ति ये त्वत्पादाब्जसेवका:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 19.18674)
- **Original**: न सन्ति जन्ममरणरोगशोकार्तिभीतय:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 19.18675)
- **Original**: इन्धत्वे बामरत्वे या ब्रहात्वे चातिदुर्लभे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 19.18676)
- **Original**: बाउ्छा नास्त्येव भक्तानां त्वत्पादसेवर्न विना। सुजीर्णपटखण्डस्थ सम॑ नूतनमेव च
- **Translation**: 

---

### Verse 12 (Vaivtpuran 19.18677)
- **Original**: पश्यन्ति भक्ता: कि चान्यत्‌ सालोक्यादिचतुष्टयम्‌ । सम्प्रामस्त्वन्मनुर्त्रह्मत्रनन्‍्ताद्‌_ यावदेव हि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 19.18678)
- **Original**: तावतू. त्वद्धावनेनेव त्वद्वणों5हमनुग्रहात्‌। मां च भक्तमपक्क॑ वा विज्ञाय गरुडः स्वयम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 19.18679)
- **Original**: देशाद्‌ दूर च न्यक्वारं चकार दृढभक्तिमानू। भवता च दृढ़ा भक्तिर्दत्ता मे वरदेश्वर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 19.18680)
- **Original**: सच भक्तश्न भक्तो5हं नमां त्यक्तुं क्षमोउधुना। त्वत्यादपद्मचिल्लाक्ते दृष्टठा श्रीमस्तक॑ मम
- **Translation**: 

---

### Verse 16 (Vaivtpuran 19.18681)
- **Original**: । सदो्ष गुणयुक्ते मां सोउथुना त्यक्तुमक्षम: । ममाराध्याक्ष नागेनद्रा न तदवध्योउहमी श्वर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 19.18682)
- **Original**: भय न केभ्व: सर्वत्र तमनन्तं गुरुं विना।य॑ देवेन्द्राश्न देवाश्ष मुनवों मनवों नराः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 19.18683)
- **Original**: स्वप्रे ध्यानेन पश्यन्ति चक्षुषो गोचर: स॒ में । भक्तानुरोधात्‌ साकार: कुतस्ते विग्रहों विभो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 19.18684)
- **Original**: सगुणस्त्व॑ च साकारों निराकारश्न निर्गुण:। स्वेच्छामय: सर्वधाम सर्वबीज॑ सनातनम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 19.18685)
- **Original**: सर्वेषामीश्वर: साक्षी सर्वात्मा सर्वरूपधृक्‌ । बरह्मेशशेषधर्मेन्द्र वेदबेदाड्रपारगा:
- **Translation**: 

---

