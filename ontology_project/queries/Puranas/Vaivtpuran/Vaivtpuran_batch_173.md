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

### Verse 1 (Vaivtpuran 12.6554)
- **Original**: करता है, उसके लिये सौ लाख जपनेपर भी मन्त्र करें । पश्चिममें पार्वतीपुत्र, वायव्यकोणमें शंकरात्मज,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.6555)
- **Original**: सिद्धिदायक नहीं होता।* इस प्रकार सूर्यपुत्र उत्तरमें परिपूर्णतम श्रीकृष्णणा अंश, ईशानकोणमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.6556)
- **Original**: शनैश्वरकको यह कवच प्रदान करके सुरेश्वर विष्णु एकदन्त और ऊर्ध्वभागमें हेरम्ब रक्षा करें। अधोभागमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.6557)
- **Original**: चुप हो गये। तब समीपमें स्थित परमानन्दमें सर्वपृज्य गणाधिप सब ओरसे मेरी रक्षा करें।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.6558)
- **Original**: निमग्र हुए देवताओंने कहा। (अध्याय 13) 40044 #स्पऑलिफयेट->> >> ल * संसारमोहनस्यास्थ कवचस्य॒ प्रजापति: । ऋषिश्ठन्द्ष॒ यृहती देवो लम्बोदर: स्वयम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.6559)
- **Original**: धर्मार्थकाममोक्षेपु विनियोग: प्रकीर्तित:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.6560)
- **Original**: सर्वेषां कवचानां च सारभूतमिद॑ मुने । 3* ग॑ हुं श्रीगणेशाय स्वाहा में पातु मस्तकम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.6561)
- **Original**: ट्वात्रिंशदक्षरों मनत्रों ललाटो मे सदाउवतु
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.6562)
- **Original**: श्रीं गमिति च संततं पातु लोचनम्‌। तालुक॑ पातु विपध्लेशः: संत धरणीतले
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.6563)
- **Original**: क्लीमिति च संतत पातु नासिकाम्‌ । 3» गाँ ग॑ शूर्पकर्णाय स्वाहा पात्वधर॑मम। जिह्मां पातु मे षोडशाक्षर:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.6564)
- **Original**: 35% हीं विप्ननाशाय स्वाहा कर्ण सदाउवतु
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.6565)
- **Original**: हीं विनायकायेति स्वाहा पृष्ठ सदाउयतु
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.6566)
- **Original**: सदा पातु । 6< कै 2» 835 ढ40 9 433 47 4 4 4 पातु सर्वाज्ज॑_विप्रनिष्नरकृतू
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.6567)
- **Original**: पातु आग्रेय्यां विप्लेशों नैरफ़त्यां तु गजाननः
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.6568)
- **Original**: पार्वतीपुत्रो.. वायव्यां शंकरात्मज: । कृष्णस्यांशशोत्ते _ च परिपूर्णतमस्य च
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.6569)
- **Original**: । गणाधिप: पातु सर्वपूज्यक्ष॒ सर्वत:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.6570)
- **Original**: इति ते कथित॑ यखत्स सर्वमन्त्रौषधिग्रहमू । संसारमोहन॑ नाम कवच परमाद्भुतम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.6571)
- **Original**: श्रीकृष्णेणे पुरा दत्त गोलोके रासमण्डले । वृन्दाने. विनीताय महां दिनकरात्मज
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.9964)
- **Original**: 'डीड8 + संक्षिप्त ब्रह्मवैयर्तपुराण « स््ंड3535352<2442<< 24255 %402040%44%4:04040030000 00040 040
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.9965)
- **Original**: /।//// 8, ब्राह्मणने नन्दशिशुके कण्ठमें बह कवच
- **Translation**: 

---

