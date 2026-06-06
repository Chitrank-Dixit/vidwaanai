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

### Verse 1 (Vaivtpuran 3.18315)
- **Original**: चतुर्विशतिनामानि. धर्मवक्‍त्रोद्गानि चव । यः पठेत्‌ प्रातरुत्थाय स सुखी सर्वतो जयी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 3.18316)
- **Original**: मृत्युकाले हरे्नाम तस्य साथ्यं भयेद्‌ श्रुवम्‌ । स यात्यन्ते हरे: स्थान हरिदास्यं लभेद्‌ धरुवम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 3.18317)
- **Original**: निर्त्य॑धर्मस्त॑ घटते नाथर्मे तद्गतिर्भवेत्‌ । चतुर्व्गफल॑ तस्य शश्वत्‌ करगत॑ भवेत्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 3.18318)
- **Original**: त॑ दृष्टा सर्वपापानि पलायन्ते भयेन च
- **Translation**: 

---

### Verse 5 (Vaivtpuran 3.18319)
- **Original**: भयानि चैबव दुःखानि लजैनतेयमिवोरगा:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 3.18320)
- **Original**: इति ज्रीब्रह्मवैवर्ते धर्मकृत अ्रीकृष्णस्तोत्र सम्पूर्णम्‌। (ब्रह्मजण्ड 3। 45--52)
- **Translation**: 

---

### Verse 7 (Vaivtpuran 3.18321)
- **Original**: <06 + संक्षिप्त ब्रह्म॑वैवर्तपुराण * सरस्वतीकृतं श्रीकृष्णस्तोत्रम्‌ सरस्वत्युवाच रासमण्डलमध्यस्थं रासोह्थससमुत्सुकम्‌ । रत्रसिंहासनस्थं_ च रन्नभूषणभूषितम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 3.18322)
- **Original**: रासेश्व
- **Translation**: 

---

### Verse 9 (Vaivtpuran 3.18323)
- **Original**: रासकर वर॑ रासेश्नरीक्वरम्‌ । रासाथिष्ठातृदेव॑ च बन्दे रासविनोदिनम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 3.18324)
- **Original**: रासायासपरिश्रान्तं रासरासविहारिणम्‌ । रासोत्सुकानां गोपीनां कान्तं शान्तं मनोहरम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 3.18325)
- **Original**: तमित्युक्तया प्रहष्टटदना सती । उवास सा सकामा चव॒ रल्सिंहासने यरे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 3.18326)
- **Original**: डति वाणीकृतं स्तोत्र प्रातरुत्थाय यः पठेत्‌ । बुद्धिमान्‌ धनवान्‌ सो5पि विद्यावान्‌ पुत्रवान्‌ सदा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 3.18327)
- **Original**: इति श्रीब्रह्मवैवर्ते सरस्वतीकृ्त श्रीकृष्णस्तोत्रं सम्पूर्णय्‌। ( ब्रह्मखण्ड 3। 60--64) +ज+ल >> ्यएथ4 9-00 महालक्ष्मीकृतं॑ श्रीकृष्णस्तोत्रम्‌ महालक्ष्मीरुवाच सत्यस्वरूपं सत्येशं सत्यबीर्ज सनातनम्‌ । सत्याधारं चर सत्यज्ञं सत्यमूलं नमाम्यहम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 3.18328)
- **Original**: ड्ति श्रीब्रह्मवैवर्ते महालक्ष्मीकृतं श्रीकृष्णस्तोत्र सम्पूर्णम्‌। (ब्रह्मखण्ड 3। 68) दुर्गाकृतं श्रीकृष्णस्तोत्रम्‌ प्रकृतिस्वाच अहं प्रकृतिरिशानी सर्वेशा सर्वरूपिणी । सर्वशक्तिस्वरूपा चर मया चर शक्तिमजगत्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 3.18329)
- **Original**: त्वया सृष्टा न स्वतन्त्रा त्वमेव जगतां पति:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 3.18330)
- **Original**: गतिश्व पाता स्त्रष्टा च॒ संहर्ता चर पुनर्विधि:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 3.18331)
- **Original**: परमानन्दरूपं त्वां बन्दे चानन्दपूर्वकम्‌ । चक्षु्निमेषकाले चर ब्रह्मण: पतन भवेतू
- **Translation**: 

---

### Verse 18 (Vaivtpuran 3.18332)
- **Original**: तस्य प्रभावमतुलं वर्णितुं कः क्षमों विभो। भ्रूभड्डलीलामात्रेण विष्णुकोरटिं सृजेत्तु यः
- **Translation**: 

---

### Verse 19 (Vaivtpuran 3.18333)
- **Original**: चराचरांश्न॒ विश्वेषु देवान्‌ ब्रह्मपुरोगमान्‌ । मद्ठिथा: कति वा देवीः स्रष्दुं शक्तश्न लीलया
- **Translation**: 

---

### Verse 20 (Vaivtpuran 3.18334)
- **Original**: परिपूर्णतर्म स्वीड्य॑ वन्दे चानन्दपूर्वकम्‌ । महान्‌ विराड्‌ यत्कलांशो विश्वासंख्याश्रयो विभो
- **Translation**: 

---

