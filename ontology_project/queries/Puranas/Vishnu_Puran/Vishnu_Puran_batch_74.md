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

### Verse 1 (Vishnu Puran 0.1461)
- **Original**: और जो लोग समाहित-चित्तसे सायड्लल और प्रातःकालके सपय तेरा गुण-कोर्तन करेंगे उनको महान्‌ पुण्य होगा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1462)
- **Original**: अीपराशरजी बोस्ढे--हे महामते ! इस प्रकार पूर्वकालमें जगत्पति देवाधिदेव भगवान्‌ जनार्दनसे वर पाकर धुत उस अत्युत्तम स्थानमें स्थित हुए
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1463)
- **Original**: हे मुने ! अपने माता-पिताको घ॒र्मपूर्वक सेजा करनेसे तथा द्वाददाक्षर-मन्त्रके माहात्य्य और तपके प्रभावसे उनके मान, वैभव एगे प्रभावकी वृद्धि देखकर देव और असुरोके आचार्य शुक्रदेवने ये इल्मेक कहे हैं---
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1464)
- **Original**: “अहो ! इस भुक्‍्के तपका कैसा प्रभाव है ? अहो ! इसकी तपस्थाका कैसा अद्भुत फल है जो इस घुतको ही आगे रखकर सप्मर्षिगण स्थित हो रहे हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1465)
- **Original**: इसकी यह सुनीति नामवाल्ली माता भी अवद्य ही सत्य और अस्याश्च महिमानं कः शक्तो वर्णयितुं भुति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1466)
- **Original**: हितकर वचन बोलनेवाली है*
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1467)
- **Original**: संसारमें ऐसा कौन है * सुनोतिने धुवको पुण्योपार्जन करनेका उपदेश दिया था, जिसके आचरणसे उन्हें उत्तम व्पेक प्राप्त _हुआ। अतएय *सुनीति' सूनृता कही गयी है ।
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1468)
- **Original**: प्र श्रीविष्णुपुराण [ अ« 13 जैल्मेक्याश्रयतां प्राप्त परं स्थान स्थिरायति। स्थान प्राप्ता परं धृत्वा या कुक्षित्रिवरे धुवम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1469)
- **Original**: 109 यश्जैतत्कीर्त्तयेन्नित्य॑ ध्रुवस्थारोहणं दिवि। सर्वपापविनिर्मुक्त: स्वर्गलोके महीयते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1470)
- **Original**: 102 स्थानभ्रेश न चाप्रोति दिवि वा यदि वा भुवि । जो इसकी महिमसाका वर्णन कर सके ? जिसने अपनी कोख्में उस धुवकों धारण करके त्रिकोकीका आश्षयभूत अति उत्तम स्थान प्राप्त कर छिया, जो भविष्यमें भी स्थिर रहतेवाला है'
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1471)
- **Original**: 100-101
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1472)
- **Original**: जो व्यक्ति घुक्‍्के इस दिव्यल्त्रेक-प्राप्तिके प्रसज्ञका कीर्तन करता है बह सब पापोंसे मुक्त होकर स्वर्गल्ोकमें पुजित होता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1473)
- **Original**: वह स्वर्गमें रहे अथवा पृथित्रीमें, कभी अपने स्थानसे च्युत नहों होता तथा समस्त मड़न्‍लोंसे सर्वकल्याणसंयुक्तो दीर्घकालं स जीवति
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1474)
- **Original**: भरपूर रहकर बहुत कालतक जोबित रहता है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1475)
- **Original**: हे ब्व्गननन-स इति श्रीविष्णुपुराणे प्रथमेंडशे द्वादशो5घ्याय:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1476)
- **Original**: ् तेरहवाँ अध्याय राजा खेन और पृथुका चरित्र ऑपराजर उबाच धुवाच्छिष्टिं च भव्यं च भव्याच्छाभुर्व्यजायत । विष्टेराधत्त सुच्छाया पञ्नपुत्नानकल्मधान्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1477)
- **Original**: 1 रिपुं रिपुक्षय॑ विष्र॑ वृकल॑ वृकतेजसम्‌ । रिपोराथत्त बृहती चाक्षूर्ष सर्वतेजसम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1478)
- **Original**: 2 अजीजनत्पुष्करिण्यां वारुण्यां चाक्षुषो मनुम्‌ । अ्रजापतेरात्मजायां वीरणस्थ महात्मन:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1479)
- **Original**: 3 मनोरजायन्त दशश नड्ब॒लायां महौजस:। कन्यायां तपतां श्रेष्ठ वैराजस्थ प्रजापते:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1480)
- **Original**: 4 कुरु: पुरु: शतझुप्नस्तपस्वी सत्यवाउल्कुचि: । अम्रिप्टोमोउतिराज्रश्च सुझुप्तनश्नेति ते नव। अभिमन्युश्न दशमो नड्बलायां महौजसः
- **Translation**: 

---

