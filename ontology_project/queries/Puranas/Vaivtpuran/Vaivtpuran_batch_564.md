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

### Verse 1 (Vaivtpuran 39.8299)
- **Original**: पूछा-बेटा! यह क्‍या बात है?” तब स्कन्दने अमोघ अस्त्रकों आते देखकर स्वयं गणपतिने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 39.8300)
- **Original**: भयपूर्वक पूर्वापरका सारा वृत्तान्त उनसे कह उसे अपने बायें दाँतसे पकड़ लिया; उस अस्त्रको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.8301)
- **Original**: सुनाया। उसे सुनकर दुर्गाकों क्रोध आ गया। व्यर्थ नहीं होने दिया। तब महादेवजीके बलसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.8302)
- **Original**: वे कृपापरवश हो रोने लगीं और शम्भुके सामने बह फरसा वेगपूर्वक गिरकर मूलसहित गणेशके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 39.8303)
- **Original**: अपने पुत्र गणेशकों छातीसे लगाकर बोलीं। दाँतको काटकर पुनः परशुरामके हाथमें लौट
- **Translation**: 

---

### Verse 6 (Vaivtpuran 39.8304)
- **Original**: सती-साध्वी पार्वतीने शोकके कारण डरकर आया। यह देखकर वीरभद्र, कार्तिकेय और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 39.8305)
- **Original**: विनयपूर्वक शम्भुको समझाया और फिर प्रणत क्षेत्राल आदि पार्षद तथा आकाशमें देवगण
- **Translation**: 

---

### Verse 8 (Vaivtpuran 39.8306)
- **Original**: होकर प्रणतकी पीड़ा हरनेवाले पतिदेवसे कहने महान्‌ भयसे भीत होकर हाहाकार करने लगे।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 39.8307)
- **Original**: लगीं। (अध्याय 42-43) #4ल्‍0+ सफल :->8>ल> न
- **Translation**: 

---

### Verse 10 (Vaivtpuran 39.18118)
- **Original**: 798 » संक्षिस ख्रह्मवैयर्तपुराण « 2 3 3
- **Translation**: 

---

### Verse 11 (Vaivtpuran 39.18119)
- **Original**: सुस्रातः: सर्वतीर्थेषु सर्वयज्ञेष॒ यत्‌ू फलम्‌ । सर्वव्रतोपवासे च तत्‌ फर्ल लभते नरः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 39.18120)
- **Original**: गुरुमभ्यर्च्य विधियद्‌ वस्त्रालंकारचन्दनै: । कण्ठे वा दक्षिणे बाहौँ कवच धारयेत्तु यः
- **Translation**: 

---

### Verse 13 (Vaivtpuran 39.18121)
- **Original**: स॒ च जैलोक्यविजयी सर्वशत्रुप्रमर्दक: । इृद॑ कवचमज्ञात्वा भजेद्‌ दुर्गतिनाशिनीम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 39.18122)
- **Original**: शतलक्षप्रजप्तो5षपि न मन्त्र: सिद्धिदायक:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 39.18123)
- **Original**: कवच काण्वशाख्रोक्तमुक्त नारद सुन्दरम्‌ । यस्मै कस्मै न दातव्य॑ गोपनीय॑ सुदुर्लभम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 39.18124)
- **Original**: इति श्रीत्रह्मवैवर्ते ब्रह्माण्डविजर्य नाम दृगकिक्च॑ सम्पूर्णम्‌। (गणपतिखण्ड 39। 3--23) ते मनोयायिन: सर्वे सम्प्रापुस्त॑ मनोहरम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 39.18125)
- **Original**: हरेरन्तःपुरं गत्वा ददूशु:ः श्रीहरि पुरः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 39.18126)
- **Original**: रलसिंहासनर्स्थ. च रलालंकारभूषितम्‌ । रत्नकेयूरवलयरतलनूपुरशोभितम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 39.18127)
- **Original**: रत्रकुण्डलयुग्मेन गण्डस्थलविराजितम्‌ । पीतवस्त्रपरीधान बनमालाविभूषितम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 39.18128)
- **Original**: शान्त॑ सरस्वतीकान्त॑ लक्ष्मीधृतपदाम्बुजम्‌ । कोटिकन्दर्पलीलाभ॑ स्मितवक्त्र चतुर्भुजम्‌
- **Translation**: 

---

