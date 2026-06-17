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

### Verse 1 (Vishnu Puran 0.821)
- **Original**: 16 यस्य सल्लातकोपस्थ भयमेति चराचरम्‌। ते से मामतिगर्वेण देवराजावमन्यसे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.822)
- **Original**: 27 औपराशर उवाच महेद्रो बारणस्कन्धादवतीर्य त्वरान्वित: । प्रसादयामास मुर्नि वुर्वाससमकल्मघम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.823)
- **Original**: 18 प्रसाद्यमान: स॒तदा प्रणिपातपुर:सरम्‌ । इत्युबाच सहस्लाक्ष॑ दुर्वासा मुनिसत्तम:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.824)
- **Original**: 19 दुर्वासा उकाच नाहे कृपालुहदयो न च॒ मां भजते क्षमा । अन्‍्ये ते मुनय: झाक्र दुर्वाससमत्रेहि माम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.825)
- **Original**: 20 गौतमादिभिरन्यैस्त्व॑ गर्बमारोपितो सुधा । अक्षान्तिसारसर्वस्व॑ दुर्वाससमयेहि माम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.826)
- **Original**: 21 वसिष्ठाधेर्दयासारैस्स्तोत्रं कुर्वखिरुच्कै: । गये गतो5सि येनैबं मामप्यद्यावमन्यसे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.827)
- **Original**: 22 ज्वलूजटाकलापस्प भुकुटीकुटिलं पुखम्‌। निरीक्ष्य कस्निभुवने मम यो न गतो भयम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.828)
- **Original**: 23 नाई क्षमिष्ये बहुना किमुक्तेन शतक़तो। विडम्बनामिमां भूय: करोष्यनुनयात्मिकाम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.829)
- **Original**: 24 अ्ीफ्यइर उयात्त इत्युक्त्वा प्रययौ विप्रो देवराजोउपि त॑ पुनः । आरुद्दौरावतं ब्रह्मम्‌ प्रययावमराबतीम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.830)
- **Original**: 25 तत: प्रभृति निःश्रीकं सहाक्रं भुवनत्रयम्‌। मैश्रेयासीदपध्यस्त॑ सद्बीणोषधिवीरुधम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.831)
- **Original**: 26 न यज्ञा: समवर्त्तन्त न तपस्यन्ति तापसा: । न चर दानादिधर्मेषु मनअ्रक्रे तदा जनः
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.832)
- **Original**: 27 निःसत्त्वा: सकला छ्तमेका स्तरेभाद्युपहतेन्द्रिया: । स्वल्पे5पि हि यभूवुस्ते साभिलाषा द्विजोत्तम ।
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.833)
- **Original**: 28 यत:ः सर्व ततो लक्ष्मी: सरत्त्व॑ भूत्यनुसारि च । नि:श्रीकाणां कुत: सत्त्व विना तेन गुणा: कुत:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.834)
- **Original**: 29 जायगा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.835)
- **Original**: इन्द्र ! निश्चय ही तू मुझे और ब्राह्मणोंके समान ही समझता है, इसोल्यि तुझ अति सानीने हमारा इस प्रकार अपमान किया है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.836)
- **Original**: अच्छा, तूने मेरी दी हुई माल्यको पृथिवीपर फेंका है इसलिये तेरा यह त्रिभुवन भो ज्ीघ्र ही श्रीहीन हो जायगा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.837)
- **Original**: रे देवराज ! जिसके क्रुद्ध होनेपर सम्पूर्ण चराचर जगत्‌ भयभीत हो जाता है उस येरा ही तूने अति गर्वसे इस प्रकार अपमान किया !
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.838)
- **Original**: श्रीपराशरजी बोले--तब ते इन्द्ने तुर्त ही ऐराबत हाथीसे उतरकर निष्याप मुनिवर दुर्वासाजोको ( अनुनय-बिनय करके ] प्रसत्न किया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.839)
- **Original**: तब उसके प्रणामादि करनेसे प्रसन्न होकर घुनिश्रेष्ठ दुर्वासाजी उससे इस्र प्रकार कहने छगे। 19
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.840)
- **Original**: दुर्वासाजी बोले--इन्द्र ! मैं कृपालु-चित्त नहीं हूँ, मेरे अन्तःकरणमें क्षमाकों स्थान नहीं है
- **Translation**: 

---

