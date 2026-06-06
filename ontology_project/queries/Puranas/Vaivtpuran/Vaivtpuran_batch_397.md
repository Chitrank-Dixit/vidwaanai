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

### Verse 1 (Vaivtpuran 19.19129)
- **Original**: कण्ठे बा दक्षिणे बाहाँ सो5पि विष्णुर्न संशय: । स च भक्तो बसेद्‌ यत्र लक्ष्मीबांणी वसेत्ततः
- **Translation**: 

---

### Verse 2 (Vaivtpuran 20.18691)
- **Original**: » भ्रीकृष्णस्तोत्राणि « <19 बरह्यणा कृतं अश्रीकृष्णस्तोत्रम्‌ ब्रह्मोब्राच सर्वस्वरूप॑ सर्वेशं सर्वकारणकारणम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 20.18692)
- **Original**: सर्वानिर्वचनीयं त॑ नमामि शिवरूपिणम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 20.18693)
- **Original**: नवीनजलदाकारं श्यामसुन्दरविग्रहम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 20.18694)
- **Original**: स्थितं जन्तुषु सर्वेषु निर्लिप्त साक्षिरूपिणम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 20.18695)
- **Original**: स्वात्मारामं॑ पूर्णकाम॑ जगद्धयापि जगत्परम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 20.18696)
- **Original**: सर्वस्वरूपं. सर्वेषां. बीजरूप॑ सनातनम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 20.18697)
- **Original**: सर्वाधारं. सर्ववर॑ सर्वशक्तिसमन्वितम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 20.18698)
- **Original**: सर्वाराध्य॑ सर्वगुरुं.. सर्वमड्गलकारणम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 20.18699)
- **Original**: सर्वमनत्रस्वककप॑ च॒ सर्वसम्पत्कर॑ वबरम्‌ । शक्तियुक्तमयुक्त च॒ स्तौमि स्वेच्छामयं विभुम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 20.18700)
- **Original**: शक्तीशं शक्तिबीज॑च शक्तिरूपधरं बरम्‌। संसारसागर. घोरे_ शक्तिनौकासमन्वितम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 20.18701)
- **Original**: कृपालुं कर्णधारं च नमामि भक्तवत्सलम्‌। आत्मस्वरूपपेकान्त॑ लिप्त निर्लिप्ततेव. च
- **Translation**: 

---

### Verse 13 (Vaivtpuran 20.18702)
- **Original**: सगुणं निर्गुणं ब्रह्म स्तौमि स्वेच्छास्वरूपिणम्‌। सर्वेन्द्रियाधिदेव॑ त्वामिन्द्रियालयमेव. च
- **Translation**: 

---

### Verse 14 (Vaivtpuran 20.18703)
- **Original**: सर्वेन्द्रस्वरूप॑ च विराड्रूप॑ नमाम्यहम्‌ । वेद च्॒ श्रेदजनक सर्ववेदाडुरूपिणम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 20.18704)
- **Original**: सर्वमन्त्रस्वरूप॑ चर नमामि परमसेश्वरम्‌। सारातू सारतरं द्रव्यमपूर्वमनिरूपणम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 20.18705)
- **Original**: स्वतन्त्रमस्वतन्र॑ च यशोदानन्दनं भजे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 20.18706)
- **Original**: शान्तं सर्वशरीरेषु तमदृष्टमनूहकम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 20.18707)
- **Original**: ध्यानासाध्य॑ विद्यमान योगीद्धाणां गुरुं भजे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 20.18708)
- **Original**: रासमण्डलमध्यस्थं रासोह्लाससमुत्सुकम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 20.18709)
- **Original**: गोपीभि: सेव्यमानं च तं॑ राधेशं नमराम्यझम्‌
- **Translation**: 

---

