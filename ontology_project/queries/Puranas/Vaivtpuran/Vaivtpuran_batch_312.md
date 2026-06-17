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

### Verse 1 (Vaivtpuran 13.17711)
- **Original**: ततो विप्ला: पलायन्ते बैनतेयाद्‌ यथोरगा: । गणेश्वरप्रसादेव महाज्ञानी भवेद्‌ श्लुव॒म्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.17712)
- **Original**: पुत्रार्थी लभते पुत्रं भार्यार्थी विपुलां स्त्रियम्‌ । महाजड: कवीन्द्रश्न विद्यावांश्व॒ भवेद्‌ ध्रुवम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.17713)
- **Original**: इति श्रीब्रह्म॑तैवर्ते विष्णुपदिष्ट गणेशनाम्राष्टक॑ स्तोत्र सम्पूर्णम्‌। (गणपतिखण्ड '44
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.17714)
- **Original**: 85-98) #ड नह कर पड 0.> पे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.18601)
- **Original**: 816 » संक्षिप्त ब्रह्मवैवर्तपुराण « 2,220 00000 04000 00 00000 00000... 3.00... 5... 0. 3.3.0..0.2.). 5. ...0.. 5.00... 3+>4 3 ++++5+3+++8+5+++++5+5+.5.+...+5+.+क+ 3577 +7--++5......00-..आ0आ7004» 3 »प 35 >धि7- थक >ारवकाक गर्गकृतं श्रीकृष्णस्तोत्रम्‌ गर्ग उवाच है कृष्ण जगतां नाथ भक्तानां भवभक्लन । प्रसन्नो भव मामीश देहि दास्य॑ पदाम्बुजे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.18602)
- **Original**: त्वत्पित्रा मे धर्न दत्त तेन में कि प्रयोजनम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.18603)
- **Original**: देहि मे निश्चलां भक्ति भक्तानामभयप्रद
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.18604)
- **Original**: अणिमादिकसिद्धिषु योगेषु मुक्तिषु प्रभो । ज्ञानतत्त्वेइमरत्वे वा किंचिन्नास्ति स्पृह्ठा मम
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.18605)
- **Original**: इन्द्रत्बे वा मनुत्वे ला स्वर्गलोकफले चिरम्‌ । नास्ति में मनसो वाउछा त्वत्पादसेवनं विना
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.18606)
- **Original**: सालोक्य॑ साप्टिसारूप्ये सामीप्यैकत्वमीप्सितम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.18607)
- **Original**: नाहं गृह्माभि ते ब्रह्मंस्त्वत्पादसेवनं॑ बिना
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.18608)
- **Original**: गोलोके वापि पाताले वासे नास्ति मनोरथ:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.18609)
- **Original**: कि तु ते चरणाम्भोजे संतते स्मृतिरस्तु मे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.18610)
- **Original**: त्वन्मनत्रं शंकरात्‌ प्राप्प कतिजन्मफलोदयात्‌ । सर्वज्ञोन्‍ह सर्वदर्शी सर्वत्र गतिरस्तु में
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.18611)
- **Original**: कृपां कुरू कृपासिन्धो दीनबन्धो पदाम्बुजे । रक्ष मामभयं दत्त्वा मृत्युपें कि. करिष्यति
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.18612)
- **Original**: सर्वेषामी श्वर: शर्वस्त्वत्पादाम्भोजसेवया ।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.18613)
- **Original**: मृत्युझ्योउन्तकारश्च॒ बभूब 'योगिनां. गुरु:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.18614)
- **Original**: ब्रह्म विधाता जगतां त्वत्पादाम्भोजसेवया । यस्यैकदिवसे .. ब्रह्मनू.. पतन्तीन्द्राश्नतुर्दश
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.18615)
- **Original**: त्वत्पादसेवया थर्म: साक्षी च सर्वकर्मणाम्‌ । पाता च फलदाता च जित्वा कालं॑ सुदुर्जयम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.18616)
- **Original**: सहस्रवदन: शेषो यत्पादाम्बुजसेवया । धत्ते सिद्धार्थवद्‌ विश्व शिव: कण्ठे विष यथा
- **Translation**: 

---

