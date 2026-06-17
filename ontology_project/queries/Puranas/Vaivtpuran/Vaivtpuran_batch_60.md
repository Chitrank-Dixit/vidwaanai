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

### Verse 1 (Vaivtpuran 5.18545)
- **Original**: सेवया तब धर्मोड्यं रक्षितारं च रक्षति
- **Translation**: 

---

### Verse 2 (Vaivtpuran 5.18546)
- **Original**: तवाज़या च संहर्ता त्ववा काले निरूपिते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 5.18547)
- **Original**: निषेकलिपिकर्ताहं त्वत्पादाम्भोजसेवया । कर्मिणां फलदाता च॒ त्वं भक्तानां च नः प्रभु:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 5.18548)
- **Original**: ब्रह्माण्डे विप्वसदृशा भूत्ता विधयविणों वयम्‌। एवं कतिविधाः: सन्ति तेष्वनन्तेषु सेवका:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 5.18549)
- **Original**: यथा न संख्या रेणूनां तथा तेषामणीयसाम्‌। सर्वेषां जनकश्लैशों यस्तं स्तोतुं च कः क्षम:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 5.18550)
- **Original**: एकैकलोमविवरे ब्रह्माण्डमेकमेककम्‌। यस्यैव महतो विष्णो: षोडशांशस्तवैब॒सः
- **Translation**: 

---

### Verse 7 (Vaivtpuran 5.18551)
- **Original**: ध्यायन्ति योगिन: सर्वे तयैतदृपमीप्सितम्‌ । त्वद्भक्ता दास्थनिरताः सेवन्ते चरणाम्बुजम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 5.18552)
- **Original**: किशोरं॑ सुन्दरतर॑ यद्रूप॑ कमनीयकम्‌ । मन्त्रध्यानानुरूप॑ च. दर्शयास्माकमीश्चर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 5.18553)
- **Original**: नवीनजलदश्यामं॑ पीताम्बरधर॑ परम
- **Translation**: 

---

### Verse 10 (Vaivtpuran 5.18554)
- **Original**: द्विभुज॑ मुरलीहस्त॑ सस्मितं॑ सुमनोहरम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 5.18555)
- **Original**: मयूरपिच्छचूडं च मालतीजालमण्डितम्‌ । चन्दनागुरुकस्तूरीकुद्ुमद्रवचर्चितम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 5.18556)
- **Original**: अमूल्यरलसाराणां. भूषणैश्षल॒ विभूषितम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 5.18557)
- **Original**: अमूल्यरत्तरच्चितकिरीटमुकुटोज्ज्वलम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 5.18558)
- **Original**: शरत्प्रफुल्लकमलप्रभामोष्यास्यचनद्धकम्‌ । पक्कब्ििम्बसमानेन हाथरौष्टेन राजितम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 5.18559)
- **Original**: पक्कदाडिमबीजाभदन्तपर्ञझक्तिमनोरमम्‌ । केलीकदम्बमूले चर स्थितं॑ रासरसोत्सुकम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 5.18560)
- **Original**: गोपीवक्त्राणि पश्यन्त॑ राधावक्ष:स्थलस्थितम्‌ । एवं वाउ्छास्ति रूप॑ ते द्रष्ट केलिरसोत्सुकम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 5.18561)
- **Original**: इत्येबमुक्त्वा विश्वसृद्‌ प्रणनाम पुनः पुनः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 5.18562)
- **Original**: एवं स्तोत्रेण तुष्टाव धर्मोडप शंकर: स्वयम्‌। ननाम भूयों भूयश्व साश्रुपूर्णविलोचन:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 5.18563)
- **Original**: तिष्ठन्तोडपि पुनः स्तोतन्नं प्रचक्तुस्त्रिदशेश्वरा: । व्याप्तास्तत्रामरा: सर्वे श्रीकृष्णतेजसा मुने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 5.18564)
- **Original**: स्तवराजमिम नित्य थर्मेशब्रह्मभिः कृतम्‌। पूजाकाले हरेरेव भक्तियुक्तश्न॒ यः पठेत्‌
- **Translation**: 

---

