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

### Verse 1 (Vaivtpuran 75.9128)
- **Original**: लक्ष्य यद्‌ू गुणरूपं च वर्णनीयं विचक्षणै:। किं वर्णयाम्यलक्ष्यं ते तेजोरूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 75.9129)
- **Original**: अशरीरं विग्रहवदिद्धियवदतीन्द्रियम्‌। यदसाक्षि सर्वसाक्षि तेजोरूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 75.9130)
- **Original**: गमनाईमपाद यदचक्षु सर्वदर्शनम्‌। हस्तास्यहीनं यद्‌ भोक्तुं तेजोरूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 75.9131)
- **Original**: वेदे निरूषितं बस्तु सन्‍्तः शक्ताक्ष वर्णितुम्‌। वेदेइनिरूपितं यत्तत्तेजोरूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 75.9132)
- **Original**: सर्वेश॑ यदनीशं यत्‌ सर्वादि यदनादि यतू। सर्वात्मकमनात्म॑ वत्तेजोरूप॑ नमाम्यहम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 75.9133)
- **Original**: अहं विधाता जगतां वेदानां जनक: स्वयम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 75.9134)
- **Original**: पाता धर्मों हरे हर्ता स्तोतुं शक्कों न को5पि यत्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 75.9135)
- **Original**: सेवया तब धर्मोई्यं रक्षितारं च रक्षति। तवाज्ञया च 'संहर्ता त्ववा काले निरूपिते
- **Translation**: 

---

### Verse 9 (Vaivtpuran 75.9136)
- **Original**: निषेकलिपिकर्ताहं त्वत्पादाम्भोजसेवया । कर्मिणां फलदाता च त्वं भक्तानां च नः प्रभु:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 75.9137)
- **Original**: ब्रह्माण्डे विम्बसदृशा भूत्वा विषयिणों वयम्‌। एवं कतिविधा: सन्ति तेष्वनन्तेषु सेवका:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 75.9138)
- **Original**: यथा न संख्या रेणूनां तथा तेषामणीयसाम्‌। सर्वेषां जनकडेेशो यस्त्वां स्तोतुं च कः क्षम:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 75.9139)
- **Original**: एकैकलोमविवरे च्रह्माण्डमेकमेककम्‌ । यस्यैव महतो विष्णों: षोडशांशस्ततैव सः
- **Translation**: 

---

### Verse 13 (Vaivtpuran 75.9140)
- **Original**: ध्यायन्ति योगिन: सर्वे. तबैतद्रूपमीप्सितम्‌ । त्वदूभक्ता दास्यनिरता: सेवन्ते चरणाम्बुजम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 75.9141)
- **Original**: किशोर॑ सुन्दरतर॑ यद्रुप॑ कमनीयकम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 75.9142)
- **Original**: मल्त्रध्यानानुरूप॑ च. दर्शयास्माकमीश्वर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 75.9143)
- **Original**: नवीनजलदश्याम॑ पीताम्बरधरं परम्‌। द्विभुज॑ मुरलीहस्त॑ सस्मितं सुमनोहरम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 75.9144)
- **Original**: मयूरपुच्छचूडं च मालतीजालमण्डितम्‌। चन्दनागुरुकस्तूरीकुंकुमद्रवचर्चितम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 75.9145)
- **Original**: अमूल्यरत्रसाराणां भूषणैश्ष विभूषितम्‌ । अमूल्यरब्ररचितकिरीटमुकुटोज्ज्वलम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 75.9146)
- **Original**: शरत्प्रफुल्लकमलप्रभामोष्यास्यचन्धकम्‌ । पक्‍्वबिम्बसमानेन हाधरौष्ठेन राजितम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 75.9147)
- **Original**: पक्‍वदाडिम्बबीजाभदन्तपंक्तिमनोरमम्‌ । केलिकदम्बमूले च॑ स्थित रासरसोत्सुकम्‌ गोपीवक्त्राण.. पश्यन्त॑ राधावक्ष:स्थलस्थितम्‌ । एवं बाउ्छास्ति रूप॑ ते द्रष्ट केलिरसोत्सुकम्‌
- **Translation**: 

---

