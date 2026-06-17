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

### Verse 1 (Vaivtpuran 38.18276)
- **Original**: 30 हुं भ्रीं क्लीं भ्रियै स्वाहा सर्वाड्रं मे सदावतु
- **Translation**: 

---

### Verse 2 (Vaivtpuran 38.18277)
- **Original**: प्राच्यां पातु महालक्ष्मीराग्रेय्यां कमलालया । पद्मा मां दक्षिणे पातु नैक्रीत्यां श्रीहरिप्रिया
- **Translation**: 

---

### Verse 3 (Vaivtpuran 38.18278)
- **Original**: पद्मालया पश्चिमे मां बायव्यां पातु श्री: स्वयम्‌ । उत्ते कमला पातु ऐशान्यां सिन्धुकन्यका
- **Translation**: 

---

### Verse 4 (Vaivtpuran 38.18279)
- **Original**: नारायणेशी .पातूर्ध्यमधो. विष्णुप्रियावतु । संतर्त सर्वतः पातु विष्णुप्राणाधिका मम
- **Translation**: 

---

### Verse 5 (Vaivtpuran 38.18280)
- **Original**: इति ते कथित बत्स सर्वमन्त्रौधथिग्रहम्‌ । सर्वैश्वर्यप्रदं नाम कवच॑ परमाद्भुतम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 38.18281)
- **Original**: सुवर्णपर्वत॑ दत्त्वा मेरुतुल्यं॑ द्विजातये । यत्‌ फल॑ लभते थर्मी कबचेन ततोउधिकम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 38.18282)
- **Original**: गुरुमभ्यर्च्य विधिवत्‌ कवच धारयेत्‌ तु यः
- **Translation**: 

---

### Verse 8 (Vaivtpuran 38.18283)
- **Original**: कण्ठे वा दक्षिणे बाहौ स श्रीमान्‌ प्रतिजन्मनि
- **Translation**: 

---

### Verse 9 (Vaivtpuran 38.18284)
- **Original**: अस्ति लक्ष्मीगृहे तस्य निश्चला शतपृरुषम्‌ । देवेन्द्रैश्लासुरेन्द्रैआ सो5वध्यो निश्चितं भवेत्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 38.18285)
- **Original**: स॒सर्वपुण्यवान्‌ धीमान्‌ सर्वयज्ञेषु दीक्षितः। स॒ स्त्रात: सर्वतीर्थेषु यस्येदे कबच गले
- **Translation**: 

---

### Verse 11 (Vaivtpuran 38.18286)
- **Original**: अस्मै कस्मै न दातव्य॑ लोभमोहभयैरपि । गुरुभक्ताय शिष्याय शरणाय प्रकाशयेतू
- **Translation**: 

---

### Verse 12 (Vaivtpuran 38.18287)
- **Original**: डइ्दं_ कबचमज़ात्या जपेक्नक्ष्म जगत्प्रसूम । कोटिसंख्यं प्रजप्तोडषपि न मन्त्र: सिद्धिदायक:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 38.18288)
- **Original**: इ्ति अ्रीब्रह्मवैवर्ते महालक्ष्मीकवर्च सम्पूर्णम्‌। (गणपतिखण्ड 38। 64--82) (48 श्र 47
- **Translation**: 

---

### Verse 14 (Vaivtpuran 38.18289)
- **Original**: 440... व । 5 28:2490776 77: / 4 नारायणकृतं श्रीकृष्णस्तोत्रम्‌ नारायण उवाच वर॑ वरेण्य वरद॑ वराह वरकारणम्‌ । कारणं कारणानां क्र कर्म तत्कर्मकारणम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 38.18290)
- **Original**: तपस्तत्फलदं शश्चत्तपस्विनां च तापसम्‌ । बन्दे नवघनश्यामं॑ स्वात्माराम॑ मनोहरम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 38.18291)
- **Original**: निष्कामं कामरूपं च कामप्नं कामकारणम्‌ । सर्व सर्वेश्वरं सर्वबीजरूपमनुत्तमम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 38.18292)
- **Original**: बेदरूपं थेदबीजं॑ वेदोक्तफलदं फलम्‌ । वेदन्न॑ तद्विधानं च॒ सर्ववेदविदां वरम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 38.18293)
- **Original**: इत्युक्त्या भक्तियुक्तश्न स उबास तदाज्ञया । रन्नसिंहासने. रम्ये. पुरतः . परमात्मन:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 38.18294)
- **Original**: नारायणकृतं स्तोत्र यः थ्रूणोति समाहितः । त्रिसंध्यं च पटेत्नित्य॑ पाप॑ तस्य न विद्यते
- **Translation**: 

---

### Verse 20 (Vaivtpuran 38.18295)
- **Original**: पुत्रा्थी लभते पुत्र भायांथी लभते प्रियाम्‌ । भ्रष्टराज्यो लभेद्‌ राज्य॑ धर्न॑ भ्रष्टँशभनो लभेत्‌
- **Translation**: 

---

