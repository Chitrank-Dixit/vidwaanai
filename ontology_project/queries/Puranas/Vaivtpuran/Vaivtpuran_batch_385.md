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

### Verse 1 (Vaivtpuran 18.18384)
- **Original**: हरिभक्ति हरेदास्य॑ लभते वैष्णवों जनः । वरार्थी यः पठेद्‌ भकत्या चास्तिकः परमास्थया
- **Translation**: 

---

### Verse 2 (Vaivtpuran 18.18385)
- **Original**: धर्मार्थकामपोक्षाणां निश्चित लभते फलम्‌ । विद्यार्थी लभते विद्यां धनार्थी लभते धनम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 18.18386)
- **Original**: भार्यार्थी लभते भारयाँ पुत्रार्थी लभते सुतम्‌ । धर्मार्थी लभते धर्म यशो5र्थी लभते यशः
- **Translation**: 

---

### Verse 4 (Vaivtpuran 18.18387)
- **Original**: भ्रष्टराज्यो लभेद्‌ राज्य प्रजाभ्रष्ट: प्रजां लधेत्‌ । रोगातों मुच्यते रोगाद्‌ बद्धो मुच्येत बन्धनात्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 18.18388)
- **Original**: भयान्मुच्येत भीतस्तु थर्न नष्टधनो लभेत्‌। दस्युग्रस्तो महारण्ये. हिंस्रजन्तुसमन्वित:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 18.18389)
- **Original**: दावाग्निदग्धो मुच्येत निमग्रश्न जलार्णवे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 18.18390)
- **Original**: इति अ्रीब्रह्मवैवर्ते मालावतीकृ्त महापुरुपस्तोत्र सम्पूर्णाम्‌ # ( ब्रह्मखण्ड 18। 9--49 ) #ज हज 8 जग 2.+00 0 श्रीकृष्णस्य द्वाविंशत्यक्षरों मन्त्रो ध्यानं च शौनक उवाच क्र॑ मन्त्र बालक: प्राप कुमारेण च धीमता । दत्त परे श्रीहरेश्व तद्भवानू वक्तुमईति
- **Translation**: 

---

### Verse 8 (Vaivtpuran 18.18391)
- **Original**: सौतिरुवाच कृष्णेन दत्तों गोलोके कृपया ब्रह्मणे पुरा । द्वार्विशत्यक्षो मन्त्रों बेदेघु च सुददुर्लभ:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 18.18392)
- **Original**: त॑ च॒ ब्रह्मा ददौ भक्‍त्या कुमाराय च धीमते । कुमारेण स दत्तश्न॒ मनत्रश्न॒ शिशवे द्विज
- **Translation**: 

---

### Verse 10 (Vaivtpuran 18.18393)
- **Original**: 33% श्री नमो भगवते रासमण्डलेश्वराय । श्रीकृष्णाय स्वाहेति च मन्त्रो5यं कल्पपादपः
- **Translation**: 

---

### Verse 11 (Vaivtpuran 18.18394)
- **Original**: महापुरुषस्तोत्रं च्व॒ पूववोक्ते कबच॑ जन यत्‌ । अस्यौपयोगिकं॑ ध्यानं सामवेदोक्तमेव च
- **Translation**: 

---

### Verse 12 (Vaivtpuran 18.18395)
- **Original**: तेजोमण्डलरूपे. च सूर्यकोटिसमप्रभे । योगिभिर्वाज्छित ध्याने योगैः सिद्धगणै: सुरै:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 18.18396)
- **Original**: ध्यायन्ते वैष्णवा रूप॑ तदध्यन्तरसंनिधौ । अतीवकमनीयानिर्वचनीयं मनोहरम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 18.18397)
- **Original**: नवीनजलदश्यामं शरत्पड्डुजलोचनम्‌ । शरत्पार्वणचन्द्रास्य॑ 'पक्रविम्बाधिकाधरम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 18.18398)
- **Original**: मुक्तापड्क्तिविनिन्दैकदन्तपड्ञक्तिमनोहरम्‌ू_। सस्मि्त मुरलीन्यस्तहस्तावलम्बनेन._ च
- **Translation**: 

---

### Verse 16 (Vaivtpuran 18.18399)
- **Original**: कोटिकन्दर्पलावण्यलीलाधाम मनोहरम्‌ । चन्द्रलक्षप्रभाजुए्ट पुष्टश्रीयुक्तविग्रहम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 18.18400)
- **Original**: ब्रिभड्रभड्डिमायुक्त. द्विंभुज॑ पीतवाससम्‌ । रत्नकेयूरवलयरलनूपुरभूषितम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 18.18401)
- **Original**: रलकुण्डलयुग्मेन गण्डस्थलविराजितम्‌ । मयूरपिच्छचूडं7ड च. रत्नमालाविभूषितम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 18.18402)
- **Original**: शोभितं॑ जानुपर्यन्त॑ मालतीवनमालया । चन्दनोक्षितसर्वाड्रं भक्तानुग्रहकारकम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 18.18403)
- **Original**: मणिना कौस्तुभेन्द्रेण वक्षःस्थलसमुज्ज्यलम्‌ । बीक्षितं गोपिकाभिश्च॒ शश्रद्द्धिमलोचनै:
- **Translation**: 

---

