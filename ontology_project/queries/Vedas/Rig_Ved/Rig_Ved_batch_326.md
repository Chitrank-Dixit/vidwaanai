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

### Verse 1 (Rig Ved 0.6501)
- **Original**: 2848. अर्वाज्॑ त्वा सुखे रथे वहतामिन्द्र केशिना । घृतस्नू बहिरासदे
- **Translation**: 

---

### Verse 2 (Rig Ved 0.6502)
- **Original**: हे इन्द्रदेव ! दोप्तिमान्‌ (स्निग्घ) केशवाले अश्व आपको सुखकर रथ द्वारा हमारे निकट ले आयें । आप यहाँ यज्ञस्थल पर कुश के पवित्र आसन पर सुशोभित हों
- **Translation**: 

---

### Verse 3 (Rig Ved 0.6503)
- **Original**: [ सूक्त - 42 ] [ऋषि- विश्वामित्र गाधिन । देवता- इद्ध
- **Translation**: 

---

### Verse 4 (Rig Ved 0.6504)
- **Original**: छत्द- गायत्री ।
- **Translation**: 

---

### Verse 5 (Rig Ved 0.6505)
- **Original**: 2849. उप नः सुतमा गहि सोममिद्ध गवाशिरम्‌ । हरिभ्यां यस्ते अस्मयु:
- **Translation**: 

---

### Verse 6 (Rig Ved 0.6506)
- **Original**: हे इन्द्रदेव ! याज़कों की अभिलाषा करते हुए आप अश्वों से योजित अपने रथ द्वारा हमारे पास आयें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.6507)
- **Original**: हमारे द्वारा अभिषुत गोदुग्धादि पिश्रित सोम का पान करें
- **Translation**: 

---

### Verse 8 (Rig Ved 0.6508)
- **Original**: 2850, तमिन्द्र मदमा गहि बर्दि:ष्ठां ग्रावभि: सुतम्‌ । कुविन्वस्य तृष्णव:
- **Translation**: 

---

### Verse 9 (Rig Ved 0.6509)
- **Original**: है इन्द्रदेव ! आप पाषाणों से निष्यन्न कुश के आसन पर सुसज्जित तथा हर्ष प्रदायक सोम के निकट आयें । प्रचुर मात्रा में इसका पान करके तृप्त हों
- **Translation**: 

---

### Verse 10 (Rig Ved 0.6510)
- **Original**: 2851. इन्द्रमित्था गिरो ममाच्छागुरिषिता इत: । आवृते सोमपीतये
- **Translation**: 

---

### Verse 11 (Rig Ved 0.6511)
- **Original**: इन्द्रदेव को बुलाने के लिए भेजी गई स्तुतियाँ, उनको सोमपान के लिए इस यज्ञम्थल पर भली-भाँति लायें
- **Translation**: 

---

### Verse 12 (Rig Ved 0.6512)
- **Original**: 2852. इन्द्रं सोमस्य पीतये स्तोमैरिह हवामहे
- **Translation**: 

---

### Verse 13 (Rig Ved 0.6513)
- **Original**: उक्थेभि: कुविदागमत्‌
- **Translation**: 

---

### Verse 14 (Rig Ved 0.6514)
- **Original**: हम इन्द्रदेव को सोमपान के लिए यहाँ इस यज्ञ में स्तुति गान करते हुए बुलाते हैं । स्तोत्रों द्वारा वे अनेक, बार विभिन्न यज्चों में आ चुके हैं
- **Translation**: 

---

### Verse 15 (Rig Ved 0.6515)
- **Original**: 2853 इन्द्र सोमा: सुता इमे तान्दधिष्व शतक्रतो । जठरे वाजिनीवसो
- **Translation**: 

---

### Verse 16 (Rig Ved 0.6516)
- **Original**: है शतकर्मा इन्धदेव ! आपके निमित्त सोम प्रस्तुत है ।इसे उदर में धारण करें ।आप अन्न- धन के अधीक्र हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.6517)
- **Original**: 2854 विद्या हि त्वा धनज्जयं वाजेषु दधृषं कवे। अधा ते सुम्नमीमहे
- **Translation**: 

---

### Verse 18 (Rig Ved 0.6518)
- **Original**: हे क्रान्दद्शी इन्द्रदेव ! हम आपको शत्रुओं के पराभवकर्त्ता और धनों के विजेता के रूप में जानते हैं; अतएव हम आपसे धन की याचना करते हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.6519)
- **Original**: 2855, इममिन्द्र गवाशिरं यवाशिरं च न: पिब। आगत्या वृषभि: सुतम्‌
- **Translation**: 

---

### Verse 20 (Rig Ved 0.6520)
- **Original**: हे इद्धदेव ! आप अपने बलवान्‌ अश्रों द्वारा आकर हमारे द्वारा अभिषुत गो-दुग्ध तथा जौ मिश्रित सोमरस का पान करें
- **Translation**: 

---

