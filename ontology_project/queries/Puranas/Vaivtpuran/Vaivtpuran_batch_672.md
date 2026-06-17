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

### Verse 1 (Vaivtpuran 70.18924)
- **Original**: नमो गोपाडुनेशाथ गणेशेश्वररूपिणे । नमः सुरगणेशाय राधेशाय नमो नमः
- **Translation**: 

---

### Verse 2 (Vaivtpuran 70.18925)
- **Original**: राधारमणरूपाय राधारूपधराय.. च। राधाराध्याय राधाया: प्राणाध्िकतराय च
- **Translation**: 

---

### Verse 3 (Vaivtpuran 70.18926)
- **Original**: राधासाध्याय.. राधाध्रिदेवप्रियतमाय.. च । राध्ाप्राणाधिदेवाय. विश्वरूपाय ते नम्मः
- **Translation**: 

---

### Verse 4 (Vaivtpuran 70.18927)
- **Original**: बेदस्तुतात्मवेदज्ञरूपिणे वेदिने. नमः । वेदाधिष्ठातृदेवव वेदबीजाय ते नमः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 70.18928)
- **Original**: यस्य लोमसु विश्वानि चासंख्यानि च नित्यश: । पहटद्विष्णोरीश्वराय.. विश्वेशाय नमो. नमः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 70.18929)
- **Original**: स्वयं प्रकृतिरूपाय प्रकृताय नमो नमः । प्रकृतीश्चररूपाय प्रधानपुरुषाय च
- **Translation**: 

---

### Verse 7 (Vaivtpuran 70.18930)
- **Original**: इत्येब॑स्तवन कृत्या मूच्छामाप सभातले । पपात सहसा भूमौ पुनरीशं ददर्श सः
- **Translation**: 

---

### Verse 8 (Vaivtpuran 70.18931)
- **Original**: बहिःस्थ॑ हृदवस्थं चर परमात्मानमीश्वरम्‌ । परित: श्यामरूपं च विश्वस्थं विश्वपेव॒ च
- **Translation**: 

---

### Verse 9 (Vaivtpuran 70.18932)
- **Original**: अक़्ूरं मूर्च्छितं दृष्ठा नन्‍दः सादरपूर्वकम्‌ । रलसिंहासने. रप्ये बासयामास नारद
- **Translation**: 

---

### Verse 10 (Vaivtpuran 70.18933)
- **Original**: पप्रच्छ सर्ववृत्तान्त॑ किंचिद दृष्टमिति त्वया । मिष्टान्नं॑ भोजयामास कुशलं अर पुनः पुनः
- **Translation**: 

---

### Verse 11 (Vaivtpuran 70.18934)
- **Original**: अक़्ूरः कथयामास कंसवृत्तान्तमीप्सितम्‌ । स्वपित्रोमोंक्षणार्थ च गमन॑ रामकृष्णयो:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 70.18935)
- **Original**: इत्यक्रूरकृतं स्तोत्र यः पठेतू सुसमाहितः । अपुत्रों लभते पुत्रमभायों लभते प्रियाम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 70.18936)
- **Original**: अथनो धनमाप्रोति निर्भूमिरुर्वरं॑ महीम्‌ । हतप्रज: प्रजां लेभे प्रतिष्ठां चाप्रतिष्ठित:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 70.18937)
- **Original**: डत्ति अऔकब्रह्मवैवर्ते अक्रूरकृतं श्रीकृष्णस्तोत्र- सम्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 70। 56-72) कंसबान्धवजनकूता श्रीकृष्णस्तुति: भ्रह्मादिस्तम्बपर्यन्तमसंख्य॑ विश्वमेव च । सर्व॑ चराचराधारं यः: सृजत्येव लीलया
- **Translation**: 

---

### Verse 15 (Vaivtpuran 70.18938)
- **Original**: ब्रहोशशेषधर्माश्च॒ दिनेशश्व॒ गणेश्वरः । मुनीन्द्रवर्गों देवेन्द्रों ध्यायते यमहर्निशम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 70.18939)
- **Original**: वेदाः स्तुबन्ति य॑ कृष्णं स्तौति भीता सरस्वती । स्तौति य॑ प्रकृतिईष्टा प्राकृतं प्रकृतेः परम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 70.18940)
- **Original**: स्वेच्छामयं निरीहं च निर्गुणं च निरक्षनम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 70.18941)
- **Original**: परात्परतरं ब्रह्म परमात्मानमी श्वरम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 70.18942)
- **Original**: नित्यं ज्योतिःस्वरूपं॑ च भक्तानुग्रहविग्रहम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 70.18943)
- **Original**: नित्यानन्द॑ च नित्यं च नित्यमक्षरविग्रहम्‌
- **Translation**: 

---

