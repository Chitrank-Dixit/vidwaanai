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

### Verse 1 (Vaivtpuran 4.8787)
- **Original**: आनेबाला नहीं है। मुने! विरजाके किनारे कहीं इतना कहकर श्रीहरि उस सभामें चुप हो
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8788)
- **Original**: तो पद्मराग और इन्द्रनील मणियोंकी खानें हैं, गये। तब उन सब देवताओंने उन्हें प्रणाम किया
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8789)
- **Original**: कहीं मरकतमणिकी खानें श्रेणीबद्ध दिखायी देती और वहाँसे अद्भुत गोलोककी यात्रा की। वह
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8790)
- **Original**: हैं, कहीं स्यमन्‍्तकमणिकी तथा कहीं स्वर्णमुद्राओंकी उत्कृष्ट एवं विचित्र परम धाम जरा एबं मृत्युको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8791)
- **Original**: खानें शोभा पाती हैं। कहीं बहुमूल्य पीले रंगकी हर लेनेवाला है। वह अगम्य लोक बैकुण्ठसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8792)
- **Original**: मणिश्रेणियोंक आकर विरजातटको अलंकृत करते * ब्रह्मोबाच नमामि कमलाकान्त॑ शान्त॑ सर्वेशमच्युतमू। यय॑ यस्य कलाभेदा: कलांशकलया सुरा:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8793)
- **Original**: मनव मुनौद्धाश॒मानुषाश चराचरा: । कलाकलांशकलया भूतास्त्वत्तो निरञ्ञन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8794)
- **Original**: शंकर उवाच त्वामक्षयपक्ष3 था. राममव्यक्रमीश्वरम्‌ । अनादिमादिमानन्दरूपिणं.. सर्वरूपिणम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8795)
- **Original**: अणिमादिकसिद्धीनां कारण. सर्वकारणम्‌। सिद्धिज्ञं सिद्धिदं सिद्धिरूप॑ कः स्तोतुमीश्चर:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8796)
- **Original**: धर्म उबाच येदे निरूपित॑ वस्तु वर्णनीयं॑ विचक्षणै: । वेदे$निर्वचनीयं यत्तन्निर्वक्तु च कः क्षम:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8797)
- **Original**: यस्य सम्भावनीयं यद्‌ गुणरूपं निरक्षमम्‌ । तदतिरिक्त॑ स्तवन॑ किमहं स्तौमि निर्गुणम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8798)
- **Original**: अ्रह्मादीनामिदं॑ स्तोत्र षट्श्लोकोक्त महामुने । पठित्वा मुच्यते दुर्गाद्वाज्छितं च लभेन्नर:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8799)
- **Original**: (श्रीकृष्णजन्मखण्ड 4
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8800)
- **Original**: 62-68)
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8801)
- **Original**: * भश्रीकृष्णजन्मखण्ड * 405 (0444/000444440440
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8802)
- **Original**: 06060 00 04]44440054044044040400434054544>>नशभ््न्नन-॑ न्न्ले ।)700]0000000000009
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8803)
- **Original**: हैं। कहीं रत्रोंके, कहीं कौस्तुभभणिके और कहाँ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8804)
- **Original**: हैं। चन्दन, अगुरु, कस्तूरी और कुंकुमयुक्त अनिर्वचनीय मणियोंके उत्तम आकर हैं। विरजाके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8805)
- **Original**: जलका वहाँ सब ओर छिड़कांब हुआ है। उस तट-प्रान्तमें कहीं-कहीं उत्तम रमणीय
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8806)
- **Original**: मुने! रत्रमय अलंकारों तथा रत्नोंकी मालाओंसे विहारस्थल उपलब्ध होते हैं। अलंकृत करोड़ों गोपकिशोरियोंके समूहसे रासमण्डल उस परम आश्चर्यजनक तटको देखकर वे
- **Translation**: 

---

