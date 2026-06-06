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

### Verse 1 (Vaivtpuran 20.18710)
- **Original**: सतां सदैव सन्त तमसन्तमसतामपि
- **Translation**: 

---

### Verse 2 (Vaivtpuran 20.18711)
- **Original**: योगीशं योगसाध्यं॑ च नमामि शिवसेवितम्‌ । मनत्र॒बीज॑ मन्त्रराज॑ मन्त्रद॑ फलदं फलम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 20.18712)
- **Original**: मन्त्रसिद्ध्धस्वरूपं त॑ नमामि च परात्परम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 20.18713)
- **Original**: सुखं दुःखं चल सुखद दुःखर्द पुण्यमेव च
- **Translation**: 

---

### Verse 5 (Vaivtpuran 20.18714)
- **Original**: पुण्यप्रदे च शुभदं॑ शुभबीज॑ नमाम्यहम्‌ । इत्येव॑ स्तवनं कृत्वा दत्त्ता गाश्न सबालकान्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 20.18715)
- **Original**: निपत्यथ दण्डबद्‌ भूमौ रुरोद प्रणनाम च । ददर्श चक्षुरुन्मील्य विधाता जगतां मुने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 20.18716)
- **Original**: ब्रह्मणा च कृतं स्तोत्र नित्यं भक्त्या च॒ यः पठेत्‌ । इृह लोके सुख भुक्त्वा यात्यन्ते भ्रीहरे: पदम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 20.18717)
- **Original**: लभते दास्यमतुलं॑ स्थानमीश्वरसंनिधौ । लब्ध्वा च कृष्णसांनिध्यं पार्षदप्रवरों भवेत्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 20.18718)
- **Original**: डति अीब्रह्मवैवर्ते ब्रह्मणा कृत #रीकृष्णस्तोत्रं सम्पूर्णय्‌। ( श्रीकृष्णजन्मखण्ड 20
- **Translation**: 

---

### Verse 10 (Vaivtpuran 20.18719)
- **Original**: 37--55) +#700000-ल्थ:थहक्‍तत2>>> इन्द्रकृतं परमेश्वरश्रीकृष्णस्तोत्रम्‌ इन्द्र उज़्ाच अक्षर॑ परम ब्रह्म ज्योतीरूप॑ सनातनम्‌ । गुणातीत॑ निराकारें. स्वेच्छामयमनन्तकम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 20.18720)
- **Original**: भक्तध्यानाय सेवायै नानारूपधर बरम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 20.18721)
- **Original**: शुक्लरक्तपीतश्याम॑ युगानुक़्रमणणेन. च
- **Translation**: 

---

### Verse 13 (Vaivtpuran 20.18722)
- **Original**: शुक्लतेज:स्वरूपं च सत्ये सत्यस्वरूपिणम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 20.18723)
- **Original**: त्रेतायां कुड्डुमाकारं ज्वलन्त॑ ब्रह्मतेजसा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 20.18724)
- **Original**: द्वापेः पीतवर्ण चर शोभित॑ पीतवाससा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 20.18725)
- **Original**: कृष्णवर्ण कलौ कृष्णं परिपूर्णतम प्रभुम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 20.18726)
- **Original**: नवधाराथरोत्कृष्टश्वामसुन्दरविग्रहम्‌ । नन्दैकनन्दन॑ वन्दे वशोदानन्दन॑ प्रभुम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 20.18727)
- **Original**: गोपिकाचेतनहरं॑ राधाप्राणाधिक॑ परम्‌। विनोदमुरलीशब्द॑ कुर्वन्त॑ कौतुकेन च
- **Translation**: 

---

### Verse 19 (Vaivtpuran 20.18728)
- **Original**: रूपेणाप्रतिमेनैव रलभूषणभूषितम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 20.18729)
- **Original**: कंदर्पकोटिसौन्दर्य बिश्रतं शान्तमी भ्वरम्‌
- **Translation**: 

---

