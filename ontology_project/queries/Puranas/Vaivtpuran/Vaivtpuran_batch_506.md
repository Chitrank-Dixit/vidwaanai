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

### Verse 1 (Vaivtpuran 28.7318)
- **Original**: महेश्वको मैं मस्तक झुकाता हूँ। यों कहकर अखिनाशी, विश्वपर शासन करनेवाले, तन्त्ररहित,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.7319)
- **Original**: भगुवंशी परशुराम शंकरजीके चरण-कमलोंपर स्वतन्त्र, तन्त्रके कारण, ध्यानद्वारा असाध्य,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.7320)
- **Original**: गिर पड़े। तब शिवजीने परम प्रसन्न होकर उन्हें दुराराध्य, साधन करनेमें अत्यन्त सुगम और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.7321)
- **Original**: शुभाशीर्वाद दिये। नारद! जो भक्तिभावसहित इस दयाके सागर हैं। दीनबन्धो! मैं अत्यन्त दीन हूँ।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.7322)
- **Original**: परशुरामकृत स्तोत्रका पाठ करता है, वह सम्पूर्ण करुणासिन्धो! मेरी रक्षा कीजिये। आज मेरा जन्म
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.7323)
- **Original**: पापोंसे पूर्णतया मुक्त होकर शिवलोकमें जाता सफल तथा जीवन सुजीवन हो गया; क्योंकि
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.7324)
- **Original**: है।।.. - (अध्याय 29) #+ल000- पथ 400>000 + परशुराम उवाच- ईश त्वां स्तोतुमिच्छामि सर्वधा स्तोतुमक्षमम्‌ । अक्षराक्षरबीज॑ च कि वा स्तौमि निरीहकम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.7325)
- **Original**: न योजनां कर्तुमीशों देवेश॑ स्तौमि मूढधी:। वेदा न शक्ता य॑ स्तोतुं कस्त्वां स्तोतुमिहेश्वर:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.7326)
- **Original**: बुद्धेवाड्सनसो: पार सारात्सारं॑ परात्परम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.7327)
- **Original**: ज्ञानबुद्धेसाध्य॑ च सिद्ध॑ सिद्धैर्निषेवितम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 29.7328)
- **Original**: + गणापतिखण्ड * 353 परशुरामका शिवजीसे अपना अभिप्राय प्रकट करना, उसे सुनकर भद्रकालीका कुपित होना, परशुरामका रोने लगना, शिवजीका कृपा करके उन्हें नानाप्रकारके दिव्यास्त्र एवं शस्त्रास्त्र प्रदान करना तदनन्तर महादेवजीके पूछनेपर परशुरामने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 29.7329)
- **Original**: । . इस बातकों सुनकर भगवती पार्वती और कहा--'दयानिधान! मैं भृगुबंशी जमदग्रिका पुत्र
- **Translation**: 

---

### Verse 13 (Vaivtpuran 29.7330)
- **Original**: भद्रकालीने क्रुद्ध होकर परशुरामकी भर्त्सना की। परशुराम हूँ। आपका दास हूँ। आपके शरणागत
- **Translation**: 

---

### Verse 14 (Vaivtpuran 29.7331)
- **Original**: तब परशुराम भगवती गौरी और कालिकाके हूँ। आप मेरी रक्षा करें! इसके बाद सारी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 29.7332)
- **Original**: क्रोधभरे बचन सुनकर उच्चस्वरसे रोने लगे और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 29.7333)
- **Original**: शयाकइा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 29.7334)
- **Original**: प्राण-विसर्जनके लिये तैयार हो गये। तब दयासागर 7 4 न्‍ः “
- **Translation**: 

---

### Verse 18 (Vaivtpuran 29.7335)
- **Original**: भक्तानुग्रहकारी प्रभु महादेवने ब्राह्मण-बालककों
- **Translation**: 

---

### Verse 19 (Vaivtpuran 29.7336)
- **Original**: रोते देखकर ख्रेहाद्रचित्तसे अत्यन्त विनयपूर्ण बचनोंके द्वारा गौरी और कालिकाका क्रोध शान्त कक 5 किया और उन दोनोंकी तथा अन्यान्य सबकी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 29.7337)
- **Original**: अनुमति लेकर परशुरामसे कहना आरम्भ किया। ( शंकरजीने कहा--हे बत्स! आजसे तुम है थक ह
- **Translation**: 

---

