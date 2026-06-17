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

### Verse 1 (Vamanpuran 0.2481)
- **Original**: 46--49
- **Translation**: 

---

### Verse 2 (Vamanpuran 0.2482)
- **Original**: जानुओमें विश्वेदेवणण, दोनों जद्बरओमें सुरश्रेष्ट साध्यगण, नखोंमें यक्ष एवं रेखाओंमें अप्सराएँ थीं।
- **Translation**: 

---

### Verse 3 (Vamanpuran 0.2483)
- **Original**: 138 + भ्रीवामनपुराण * [ अध्याय 31 दृष्टिक्रक्षाण्यशेषाणि केशा: सूर्याशव: प्रभो:। तारका रोमकूपाणि रोमेषु चर महर्षय:
- **Translation**: 

---

### Verse 4 (Vamanpuran 0.2484)
- **Original**: 51 बाहवो विदिशस्तस्य दिशः श्रोत्रे महात्मन:। अश्विनौ श्रवणे तस्य नासा वायुर्महात्मन:
- **Translation**: 

---

### Verse 5 (Vamanpuran 0.2485)
- **Original**: 52 प्रसादे चन्द्रमा देवो मनो धर्म: समाश्रित:। सत्यमस्याभवद्‌ वाणी जिड्डा देवी सरस्वती
- **Translation**: 

---

### Verse 6 (Vamanpuran 0.2486)
- **Original**: 53 ग्रीवाउदितिर्देवमाता विद्यास्तद्वलयस्तथा। स्वर्गद्वारमभून्मैत्रं त्वष्टा पूषा च॒ वे श्रुवा
- **Translation**: 

---

### Verse 7 (Vamanpuran 0.2487)
- **Original**: 54 मुखे वैश्वानरश्नास्थ वृषणौ तु प्रजापति:। हृदयं चर पर॑ ब्रह्म पुंस्त्व॑ं वै कश्यपो मुनि:
- **Translation**: 

---

### Verse 8 (Vamanpuran 0.2488)
- **Original**: 55 पृष्ठेडस्थ बसबो देवा मरुत: सर्वसन्धिषु। वक्ष:स्थले तथा रुद्रो धै्यें चास्य महार्णव:
- **Translation**: 

---

### Verse 9 (Vamanpuran 0.2489)
- **Original**: 56 उदरे चास्य गन्धर्वा मरुतक्ष महाबला:। लक्ष्मीमेंधा धृति: कान्ति: सर्वविद्याश्न वै कटि:
- **Translation**: 

---

### Verse 10 (Vamanpuran 0.2490)
- **Original**: 57 सर्वज्योतीषि यानीह तपश्च॒ परम॑ महत्‌। तस्य देवाधिदेवस्य तेज: प्रोद्धृतमुत्तमम्‌
- **Translation**: 

---

### Verse 11 (Vamanpuran 0.2491)
- **Original**: 58 तनौ कुक्षिषु वेदाश्न जानुनी च महामखा:। डइृष्टयः पशवश्चास्य द्विजानां चेष्टितानि च
- **Translation**: 

---

### Verse 12 (Vamanpuran 0.2492)
- **Original**: 579 तस्य देवमयं रूप॑ दृष्टा विष्णोर्महात्मन:। उपसर्पन्ति ते दैत्या: पतड्भरा इब पावकम्‌
- **Translation**: 

---

### Verse 13 (Vamanpuran 0.2493)
- **Original**: 60 चिक्षुरस्तु महादैत्यः पादाडुर्ड गृहीतवान्‌। दन्ताभ्यां तस्य वै ग्रीवामबुष्टेनाहनद्धरि:
- **Translation**: 

---

### Verse 14 (Vamanpuran 0.2494)
- **Original**: 61 प्रमथ्य सर्वानसुरानू पादहस्ततलैविंभु:। कृत्वा रूप महाकाय॑ संजहाराशु मेदिनीम्‌
- **Translation**: 

---

### Verse 15 (Vamanpuran 0.2495)
- **Original**: 62 तस्य विक्रमतो भूमि चन्द्रादित्यौ स्तनान्तरें। नभो विक्रममाणस्य सक्थिदेशे स्थितावुभौ
- **Translation**: 

---

### Verse 16 (Vamanpuran 0.2496)
- **Original**: 63 पर॑ विक्रममाणस्य जानुमूले प्रभाकरौ। विष्णोरास्तां स्थितस्वयैता देवषालनकर्मीणि
- **Translation**: 

---

### Verse 17 (Vamanpuran 0.2497)
- **Original**: 64 जित्वा लोकत्रयं तांश्व हत्वा चासुरपुंगवान्‌। पुरंदराय त्रैलोक्यं ददौ विष्णुरुरुक्रम:
- **Translation**: 

---

### Verse 18 (Vamanpuran 0.2498)
- **Original**: 65 समस्त नक्षत्र उनकी दृष्टियाँ, सूर्यकिरणें प्रभुके केश, तारकाएँ उनके रोमकूप एवं महर्षिगण रोमोंमें स्थित थे। विदिशाएँ उनकी बाहें, दिशाएँ उन महात्माके कर्ण, दोनों अश्विनीकुमार श्रवण एवं वायु उन महात्माके नासिका- स्थानपर थे। उनके प्रसादमें (मधुर हास्यछटामें) चन्द्रदेव तथा मनमें धर्म आश्रित थे। सत्य उनकी वाणी तथा जिह्ला सरस्वतीदेवी थीं
- **Translation**: 

---

### Verse 19 (Vamanpuran 0.2499)
- **Original**: 50--53
- **Translation**: 

---

### Verse 20 (Vamanpuran 0.2500)
- **Original**: देवमाता अदिति उनकी ग्रीवा, विद्या उनकी अलियाँ, स्वर्गद्टार उनकी गुदा तथा त्वष्टा एवं पृूषा उनकी औौहें थे। वैश्वानर उनके मुख तथा प्रजापति वृषण थे। परंब्रह्म उनके हृदय तथा कश्यप मुनि उनके पुंस्त्व थे। उनकी पीठमें वसु देवता, सभी सन्धियोंमें मरुद॒गण, यक्ष:स्थलमें रुद्र तथा उनके घैर्यमें महार्णव आश्रित थे। उनके उदरमें गन्धर्य एवं महाबली मरुद्गण स्थित थे। खक्ष्मी, मेधा, धृति, कान्ति एवं सभी विद्याएँ उनकी करियमें स्थित थीं
- **Translation**: 

---

