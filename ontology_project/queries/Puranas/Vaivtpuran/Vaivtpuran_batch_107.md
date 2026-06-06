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

### Verse 1 (Vaivtpuran 7.18453)
- **Original**: स्व्रीरूप॑ं कमनीय॑ च विधाय समुपस्थिता
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.18454)
- **Original**: निहत्य सर्वान्‌ शैलेन्द्रमामं त॑ हिमाचलम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.18455)
- **Original**: अभवं दक्षजायायां शिवस्त्री भवजन्मनि
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.18456)
- **Original**: अभवं शैलजायायां शैलाधीशस्य कर्मणा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.18457)
- **Original**: पाणिं जग्राह मे योगी प्रार्थितो ब्रह्मणा विभु:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.18458)
- **Original**: स्तौमि त्वामेव तेनेश पुत्रदुःख्ेन दुःखिता
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.18459)
- **Original**: देवेन विहिता वेदे साड़्ने स्वस्वामिदक्षिणा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.18460)
- **Original**: इत्युक्त्वा पार्वती तत्र बिरराम चव नारद
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.18461)
- **Original**: सत्पुत्रं लभते नूनं॑ विष्णुतुल्यपराक्रमम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.18462)
- **Original**: सुपुण्यकत्रतफर्ल लभते नात्र संशय:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.18463)
- **Original**: सुखद मोक्षदं सारं॑ स्वामिसौभाग्यवर्धनम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.18464)
- **Original**: हरिभक्तिप्रदं तत्त्वज्ञानबुद्धिविवर्धनम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.18465)
- **Original**: इति जब्रह्मवैवर्ते देव: पार्वत्या च कृत श्रीकृष्णस्तोत्रं सम्पूर्णम्‌। (गणपतिखण्ड 7। 93--131) #+8-+8*#थएथ8 7020-00 श्रीकृष्णस्य सप्तदशाक्षरो मन्त्रः महादेव उवाच 3» श्रीं नमः श्रीकृष्णाय परिपूर्णतमाय च । सिद्धोउ्यं पश्ललक्षेण जपेन मुनिपुद्ढडब । तर्पणं तदशांशं च॑ तदहशांशं चर मार्जनम्‌ । मन्त्नसिद्धस्य पुंसक्ष विश्व करतल मुने । मन्त्रेधु_ मन्त्रराजोई्य॑ महानू सप्तदशाक्षरः
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.18466)
- **Original**: तहशांशं च हवन तदशांशाभिषेचनम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.18467)
- **Original**: सुवर्णाना च शतक पुरश्चरणदक्षिणा
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.18468)
- **Original**: शक्त: पातुं समुद्रांश विश्व संहर्तुमीश्चर:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.18469)
- **Original**: पाकछ्नृभौतिकदेहेन वैकुण्ठं गन्तुमीश्चरः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.18470)
- **Original**: तस्य संस्पर्शमात्रेण. पादपद्डुजरेणुना । पूतानि सर्वतीर्थानि सद्यः पूता वसुन्धरा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.18471)
- **Original**: ड्ति श्रीत्रह्मवैवर्ते श्रीकृष्णस्य सतदत्ाक्षरें मनत्र: सम्पूर्ण: । (गणपतिखण्ड 32। 3-7) #>“_“-ऑस्पं228080 (637 ] सं0 ब्र0 बै0 पुराण 27
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.18472)
- **Original**: <1रे + संक्षिप्त ख्रह्मलैलर्तपुराण + 4:9:2/2 02 020/074088
- **Translation**: 

---

