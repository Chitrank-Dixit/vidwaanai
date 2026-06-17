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

### Verse 1 (Vaivtpuran 21.18742)
- **Original**: विनोदमुरलीशब्द॑ कुर्वन्त॑ कुज़चिन्मुदा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 21.18743)
- **Original**: गायन्तं रम्यसंगीत॑ कुत्रचिद बालक: सह । स्तुत्वा शक्र: स्तवेन्द्रेण प्रणनाम हरिं भिया
- **Translation**: 

---

### Verse 3 (Vaivtpuran 21.18744)
- **Original**: पुरा दत्तेन गुरुणा रणे वृत्रासुरेण च। कृष्णेन दत्त कृपया ब्रह्मणे च तपस्यते
- **Translation**: 

---

### Verse 4 (Vaivtpuran 21.18745)
- **Original**: एकादशाक्षरों मन्त्र: कवच सर्वलक्षणम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 21.18746)
- **Original**: दत्तमेतत्‌ कुमाराय पुष्करे ब्रह्मणा पुरा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 21.18747)
- **Original**: कुमारोउड्रिसे दत्तो गुरवेडड्लिससा मुने । इदमिन्द्रकृतं स्तोत्न॑ नित्य भक्‍त्या चर यः पठेतू
- **Translation**: 

---

### Verse 7 (Vaivtpuran 21.18748)
- **Original**: इृह प्राप्य दृढां भक्तिमन्ये दास्‍्य॑ लभेद्‌ ध्रुवम्‌। जन्ममृत्युजराव्याधिशोकेभ्यो . मुच्यते. नरः। न हि पश्यति स्वप्रेडपि यमदूतं यमालयम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 21.18749)
- **Original**: इति श्रीब्रह्मवैवर्ते इन्द्रकृतं परमेश्चरत्रीकृष्णस्तोत्र सम्पूर्णम्‌ । ( श्रीकृष्णजन्मखण्ड 21। 176--196 ) +*0-“-म्यथ..-2>> नन्दकृतं अश्रीकृष्णस्तवनम्‌ ननन्‍्द उवाच नमो ब्रह्मण्यदेवाय गोब्नाह्मणहिताय च। जगद्द्धिाय कृष्णाय गोविन्दाय नमो नमः
- **Translation**: 

---

### Verse 9 (Vaivtpuran 21.18750)
- **Original**: नमो ब्रह्मण्यदेवाय ब्रहाणे. परमात्मने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 21.18751)
- **Original**: अनन्तकोटिब्रह्माण्डधामधाप्रे. नमो5स्तु ते। नमो मत्स्यादिरू्पाणां जीबरूपाय साक्षिणे। निर्लिप्ताय निर्गुणाय निराकाराय ते नम:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 21.18752)
- **Original**: अतिसूक्ष्मस्वरूपाय स्थूलात्‌ स्थूलतमाय च। सर्वेश्वराय सर्वाय तेजोरूपाय ते नमः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 21.18753)
- **Original**: अतिसूक्ष्मस्वरूपाय ध्यानासाध्याय योगिनाम्‌। ख्रह्विष्णुप्हेशानां. वन्द्याय नित्यरूपिणे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 21.18754)
- **Original**: धाप्ने चतुर्णां वर्णानां युगेष्वेब चतुर्ष च। शुक्लरक्तपीतश्यामाभिधानगुणशालिने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 21.18755)
- **Original**: योगिने योगरूपाय गुरवे योगिनामपि। सिद्धेश्वराय सिद्धाय सिद्धानां गुरबे नम्तः
- **Translation**: 

---

### Verse 15 (Vaivtpuran 21.18756)
- **Original**: यं स्तोतुमक्षमो ब्रह्मा विष्णुर्य स्तोतुमक्षम: । य॑ स्तोतुमक्षमो रुद्रः शेषों य॑ स्तोतुमक्षम:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 21.18757)
- **Original**: य॑ स्तोतुमक्षमों धर्मो य॑ स्तोतुमक्षमो रविः
- **Translation**: 

---

### Verse 17 (Vaivtpuran 21.18758)
- **Original**: यं॑ स्तोतुमक्षमो लम्बोदरशापि घड़ाननः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 21.18759)
- **Original**: यं स्तोतुमक्षमा: सर्वे मुनयः सनकादयः
- **Translation**: 

---

### Verse 19 (Vaivtpuran 21.18760)
- **Original**: कपिलो न क्षमः स्तोतुं सिद्धेद्धाणां गुरोगुरु:
- **Translation**: 

---

### Verse 20 (Vaivtpuran 21.18761)
- **Original**: न शक्तौ स्तवनं कु नरनारायणावृषी । अन्ये जडधियः के वा स्तोतुं शक्ताः परात्परम्‌
- **Translation**: 

---

