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

### Verse 1 (Vaivtpuran 36.7922)
- **Original**: दुर्वासाने राजाकों दिया था। उस समय राजाने महाविद्या तथा तीनों लोकोंमें दुर्लभ उस गोपनीय
- **Translation**: 

---

### Verse 2 (Vaivtpuran 36.7923)
- **Original**: दस लाख जप करके मन्त्र सिद्ध किया और * परशुराम उवाच-- नमः शंकरकान्ताय॑ सारायै॑ते नमो नमः । नमो दुर्गतिनाशिन्ये मायायै ते नमो नमः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 36.7924)
- **Original**: नमो नमो जगद॒धात्ये॑ जगत्कत्य॑ नमो नमः । नमो5स्तु ते जगन्मात्रे कारणायै नमो नमः
- **Translation**: 

---

### Verse 4 (Vaivtpuran 36.7925)
- **Original**: प्रसीद जगतां मातः सृष्टिसंहारकारिणि । त्वत्पादे शरणं यामि प्रतिज्ञा सार्थिकां कुरु
- **Translation**: 

---

### Verse 5 (Vaivtpuran 36.7926)
- **Original**: युष्माभि: शिवलोके च मह्ां दत्तों वर; पुरा ।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 36.7927)
- **Original**: त्वयि मे विमुखायां च को मां रक्षितुमोश्वरः
- **Translation**: 

---

### Verse 7 (Vaivtpuran 36.7928)
- **Original**: त्वं प्रसन्ना
- **Translation**: 

---

### Verse 8 (Vaivtpuran 36.7929)
- **Original**: भक्त भक्तयत्सले
- **Translation**: 

---

### Verse 9 (Vaivtpuran 36.7930)
- **Original**: ते बरं सफल॑ कु त्वमहंसि वरानने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 36.7931)
- **Original**: जामदग्न्यस्तव॑ श्रुत्वा प्रसन्नाभवदम्बिका । मा भैरित्येवमुक्वा तु तप्ैवान्तरधीयत
- **Translation**: 

---

### Verse 11 (Vaivtpuran 36.7932)
- **Original**: एतद्‌ भृगुकृतं स्तोत्र भक्तियुक्तत्ष यः पठेत्‌ । महाभयात्‌ समुत्ती्ण: स॒ भवेदवलीलया
- **Translation**: 

---

### Verse 12 (Vaivtpuran 36.7933)
- **Original**: ज्ञानिश्रेष्ठे. भवेच्चैव.. यैरिपक्षविमर्दक:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 36.7934)
- **Original**: (गणपतिखण्ड 36। 29-36) स॒ पूजितक्ष त्रैलोक्ये तैलोक्यविजयी भवेत्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 36.7935)
- **Original**: * गणपतिखणड * 375 ऋकऋऋऋ 4 ### ##क # कक 4 # #
- **Translation**: 

---

### Verse 15 (Vaivtpuran 36.7936)
- **Original**: कक ऋऊ्ऋऋ 4 45455 #### ###%##ऊ इस उत्तम कबचके पाँच लाख जपसे ही वे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 36.7937)
- **Original**: नाभिकी रक्षा करे। “34 हीं कालिकाय॑ स्वाहा' सिद्धकवच हो गये। तत्पश्चात्‌ वे अयोध्यामें लौट
- **Translation**: 

---

### Verse 17 (Vaivtpuran 36.7938)
- **Original**: सदा मेरे पृष्ठभागकी रक्षा करे। 'रक्तबीजविनाशिन्य आये और इसी कवचकोी कृपासे उन्होंने सारी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 36.7939)
- **Original**: स्वाहा' सदा हाथोंकी रक्षा करे। '30 हीं क्लीं पृथ्वीकों जीत लिया।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 36.7940)
- **Original**: मुण्डमालिन्यै स्वाहा' सदा पैरोंकी रक्षा करे।' 30 नारदजीने कहा--प्रभो! जो तीनों लोकोंमें
- **Translation**: 

---

### Verse 20 (Vaivtpuran 36.7941)
- **Original**: हीं चामुण्डायै स्वाहा' सदा मेरे सर्वाज्जकी रक्षा दुर्लभ है, उस दशाक्षरी विद्याको तो मैंने सुन
- **Translation**: 

---

