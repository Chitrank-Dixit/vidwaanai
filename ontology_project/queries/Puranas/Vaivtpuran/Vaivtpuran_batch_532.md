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

### Verse 1 (Vaivtpuran 32.18507)
- **Original**: तृणानां कुशरूपो यो व्याधिरूपश्च वैरिणाम्‌। गुणानां शान्तरूपो यश्ञित्ररूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 32.18508)
- **Original**: तेजोरूपो ज्ञानरूप: सर्वरूपश्च यो महान्‌। सर्वानिर्वचनीयं क्र त॑ नमामि स्वयं विभुम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 32.18509)
- **Original**: सर्वाधारेषु यो वायुर्वधात्मा नित्यरूपिणाम्‌। आकाशों व्यापकानां यो व्यापकं त॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 32.18510)
- **Original**: वेदानिर्यचचनीयं यन्न स्तोतुं पण्डित: क्षमः। यदनिर्वचनीयं चर को वा तत्‌ स्तोतुमीश्चरः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 32.18511)
- **Original**: वेदा न शक्ता य॑ स्तोतुं जडीभूता सरस्वती । त॑ च वाडुमनसोः पार॑ को विद्वान्‌ स्तोतुमीश्चरः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 32.18512)
- **Original**: शुद्धतेज: स्वरूपं च॒ भक्तानुग्रहविग्नहमू । अतीवकमनीयं च॒ श्यामरूपं नमराम्यहम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 32.18513)
- **Original**: द्विभुज॑ मुरलीवक्मं॑ किशोर सस्मित मुदा । शश्चद्गोपाड्नाभिश्च॒ वीक्ष्यमाणं. नमाम्यहम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 32.18514)
- **Original**: राधया दत्तताम्बूलं भुक्तवन्त॑ मनोहरम्‌। रलसिंहासनस्थ॑ च तमीशं प्रणमाम्यहम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 32.18515)
- **Original**: रलभूषणभूषाकां सेवितं.श्वेतचामौरैः । पार्षदप्रवरगोंपकुमारैस्तं नमाम्यहम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 32.18516)
- **Original**: युन्दावनान्ते. रम्ये _ रासोल्लाससमुत्सुकम्‌ । रासमण्डलमध्यस्थं नमामि रसिकेश्चरम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 32.18517)
- **Original**: शतश्रुड्जे महाशैले गोलोके रलपर्वते । विरजापुलिने रम्ये प्रणणामि विहारिणम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 32.18518)
- **Original**: परिपूर्णतमं॑ शान्त॑ राधाकान्त॑ मनोहरम्‌ । सत्य ब्रह्मस्वरूपं चर नित्यं कृष्णं नमाम्यहम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 32.18519)
- **Original**: श्रीकृष्णस्य स्तोत्रमिद त्िसंध्यं यः: पठेन्नर:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 32.18520)
- **Original**: धर्मार्थकाममोक्षाणां स दाता भारते भवेत्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 32.18521)
- **Original**: हरिदास्यं हरौ भक्ति लभेत्‌ स्तोत्रप्रसादतः: । इह लोके जगत्पूज्यों विष्णुतुल्यों भवेद्‌ श्रुवम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 32.18522)
- **Original**: सर्वसिद्धेश्व: शान्तो5प्यन्ते याति हरे: पदम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 32.18523)
- **Original**: तेजसा यशसा भाति यथा सूर्यों महीतले
- **Translation**: 

---

### Verse 18 (Vaivtpuran 32.18524)
- **Original**: जीवन्मुक्त: कृष्णभक्त: स भयेन्नात्र संशय: । अरोगी गुणबान्‌ दिद्वान्‌ पुत्रवान्‌ धनवान्‌ सदा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 32.18525)
- **Original**: बड़भिज्ञो दशबलो मनोयायी भवेद्‌ श्रुवम्‌ ।सर्वज्ञ: सर्वदश्य स॒ दाता सर्वसम्पदाम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 32.18526)
- **Original**: कल्पवृक्षसम: शश्वद्‌ भवेत्‌ कृष्णप्रसादत:
- **Translation**: 

---

