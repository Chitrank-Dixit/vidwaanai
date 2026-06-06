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

### Verse 1 (Vaivtpuran 119.19030)
- **Original**: 830 + संक्षिप्त ब्रह्मवैवर्तपुराण * कक 55 55% %%$% कक कक क5###%######### 6 # # # त्वमेब कलया सूर्यस्वमेव कलया शशी । कलया च्‌ हुताशश्च॒ कलया पवनः स्वयम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 119.19031)
- **Original**: कलया वरुणश्लैव कुबेरश्ष॒ यम्रस्तथा । कलया त्व॑ महेनद्रश कलया थर्म एवं चा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 119.19032)
- **Original**: त्वमेव कलया शेष ईशानो निर्ऋतिस्तथा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 119.19033)
- **Original**: मुनयों मनवश्चैवग्रहाश्ल फलदायकाः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 119.19034)
- **Original**: कलाकलायाश्चांशेन सर्वे जीवाश्षराचरा: । त्वं ब्रह्म परम॑ ज्योतिर्ध्यायन्ते योगिनस्तथा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 119.19035)
- **Original**: तत्त्वाद्वियन्ते भक्तास्ते ध्यायन्ते च तदन्तरे । नवीननीरदश्यामं पीतकौशेयवाससम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 119.19036)
- **Original**: ईंषद्धास्यप्रसन्नास्य॑ भक्तेशं॑ भक्तवत्सलम्‌ । चन्दनोक्षितसर्वाड्र.. द्विभुज॑. मुरलीधरम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 119.19037)
- **Original**: मयूरपिच्छयूडंढ च॑ मालतीमाल्यभूषितम्‌ । अमूल्ग्ररत्ननिर्माणकेयूरवलयान्वितम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 119.19038)
- **Original**: मणिकुण्डलयुग्मेन.._ गण्डस्थलविराजितम्‌ । रलसाराडुलीयं॑ च॒_ क्कणन्मझऔररखितम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 119.19039)
- **Original**: कोटिकन्दर्पलीलाभं शरत्कमललोचनम्‌ । शरत्पूर्णेन्दुनिन्द्यास्यं चन््कोटिसमप्रभम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 119.19040)
- **Original**: वीक्षितं सस्मिताभिश्चव गोपीनां कोटिकोटिभि: । वयस्यै: . पार्षदैगोंपे: सेवित॑. श्वेतचामरैः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 119.19041)
- **Original**: गोपबालकवेष॑ च राधथावक्ष:स्थलस्थितम्‌ । ध्यानासाध्यं दुराराध्यं ब्रहोशशेषबन्दितम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 119.19042)
- **Original**: सिद्धेन्लैश मुनीन्द्रैश योगीन्द्रै: प्रणतं स्तुतम्‌ । वेदानिर्यचनीय॑ च पर॑ स्वेच्छामय विभुम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 119.19043)
- **Original**: स्थूलात्‌ स्थूलतमं रूप॑ सूक्ष्मात्‌ सूक्ष्मतर्मं परम्‌ । सत्यं नित्यं प्रशस्तं च्॒ प्रकृते: परमीश्चरम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 119.19044)
- **Original**: निर्लिप्त च निरीहं॑ च्॒ भगवन्तं सनातनम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 119.19045)
- **Original**: एवं ध्यात्वा च ते पूता: स्तरिग्धदूर्वाक्षताज्नलम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 119.19046)
- **Original**: पद्मापद्मार्चित पादपचणोे चर दातुमुत्सुकाः । बेदा: स्तोतुमशक्तास्त्वाभशक्ता सा सरस्वती
- **Translation**: 

---

### Verse 18 (Vaivtpuran 119.19047)
- **Original**: शेष: स्तोतुमशक्तश्न॒ स्वयम्भू: शम्भुरीक्वरम्‌ । गणेशश्र॒ दिनेशश्व॒ महेन्द्रश्नन्न
- **Translation**: 

---

### Verse 19 (Vaivtpuran 119.19048)
- **Original**: एबं. च
- **Translation**: 

---

### Verse 20 (Vaivtpuran 119.19049)
- **Original**: स्तोतुं नाल॑ धनेशश्व॒ किमन्ये जडबुद्धयः । गुणातीतमनीहूँ च किं स्तौमि निर्गुणं परम्‌
- **Translation**: 

---

