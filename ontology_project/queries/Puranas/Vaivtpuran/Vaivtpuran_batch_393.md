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

### Verse 1 (Vaivtpuran 19.17829)
- **Original**: स्वयं शम्भुश्न बराणाय तथा दुबांससे पुरा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 19.17830)
- **Original**: मूलेन सर्व देय॑ च नैवेद्यादिकमुत्तमम्‌ । ध्यायेतन्रित्यादिकं ध्यानं बेदोक्त॑ सर्वसम्मतम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 19.17831)
- **Original**: 33% नमो महादेवाय बाणासुर उवाच महेश्वर महाभाग कवर्च यत्‌ प्रकाशितम्‌ । संसारपावनं नाम कृपया कथय प्रभो
- **Translation**: 

---

### Verse 4 (Vaivtpuran 19.17832)
- **Original**: महेश्वर उबाच श्रृणु यक्ष्यामि हे बत्स कवच परमाद्भुतम्‌ । अहं तुभ्य॑ प्रदास्थामि गोपनीय सुदुर्लभम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 19.17833)
- **Original**: पुरा दुर्वाससे दत्त तरैलोक्यविजयाय च । ममैवेदं च कवच भक्‍त्या यो धारयेत्‌ सुधी:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 19.17834)
- **Original**: जेतुं शक्रोति तैलोक्यं भगवानिव लीलया । संसारपावनस्थास्थ कवचस्य॒ प्रजापति:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 19.17835)
- **Original**: ऋषिएछन्दश्व॒ गायत्री देवो5ह॑ चव महेश्वर: । थर्मार्थकाममोक्षेपु विनियोग: प्रकीर्तित:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 19.17836)
- **Original**: पह्ललक्षजपेनैब सिद्धिदं कवच भवेत्‌। यो भवेत्‌ सिद्धकवच्ो मम तुल्यो भवेद्‌ भुवि । तेजला सिद्धियोगेन तपसा विक़रमेण च
- **Translation**: 

---

### Verse 9 (Vaivtpuran 19.17837)
- **Original**: शम्भुरषं मस्तक पातु मुखं पातु महेश्वरः । दन्तपद्कक्ति मीलकण्ठोउप्यधरोष्ठ॑ हर: स्वयम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 19.17838)
- **Original**: क़ण्ठं॑ पातु चन्रचूड: स्कन्थौ वृषभवाहन: । वक्ष:स्थलं नीलकण्ठ: पातु पृष्ठ दिगम्बर:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 19.17839)
- **Original**: सर्वाड्रं पातु विश्वेश: सर्वदिक्षु च सर्वदा । स्वप्ने जागरणे चैव स्थाणुर्मे पातु संततम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 19.17840)
- **Original**: डइति ते कथितं बाण कब परमादभुतम्‌ । यस्पै कस्मै न दातव्यं गोपनीय प्रयत्नतः
- **Translation**: 

---

### Verse 13 (Vaivtpuran 19.17841)
- **Original**: यत्‌ फल सर्वतीर्थानां स्नानेन लभते नरः । तत्‌ फल लभते नून॑ कवचस्यैव धारणात्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 19.17842)
- **Original**: इुदं कवचमज़ात्वा भजेन्मां यः सुमन्दधी: । शतलक्षप्रजप्तोषपि न॒ मन्त्र: सिद्धिदायक:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 19.17843)
- **Original**: इति अऔब्रह्मवैवर्ते मन्त्रस॒हित॑ संसारपावनं शिवकवर्च सम्पूर्णम्‌। ( ब्रह्मखण्ड 19। 39--54)
- **Translation**: 

---

### Verse 16 (Vaivtpuran 19.18661)
- **Original**: 818 न संक्षिप्त ब्रह्मवैवर्तपुराण के 44424क्‍204::42:0024क्‍4045444244:4/40 04... लक्ष्मीसरस्वतीदुर्गाजाह्बीवेदमातृभि: । सेवितं॑ सिद्धसड्वैश्व॒ मुनीन्द्रैमनुभि: सदा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 19.18662)
- **Original**: निष्कारणायाखिलकारणाय सर्वेश्वरायापि परात्पयराय। स्ववम्प्रकाशाय परावराय. परावराणामंधिपाय. ते. नमः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 19.18663)
- **Original**: है कृष्ण हे कृष्ण सुरासुरेश ब्रहोश शेषेश प्रजापतीश। मुनीश मन्वीश चराचरेश सिद्धीश सिद्धेश गुणेश पाहि
- **Translation**: 

---

### Verse 19 (Vaivtpuran 19.18664)
- **Original**: अर्मेश. धर्मीश शुभाशुभेश वेदेश _ वेदेष्वनिरूपितश्च। सर्वेश सर्वात्मक सर्वबन्धो जीवीश जीवेश्वर पाहि मत्प्रभुम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 19.18665)
- **Original**: इत्येव॑ स्तवनं॑ कृत्वा भक्तिनप्रात्मकन्धरा। विधृत्य. चरणाम्भोज॑ तस्थौ नागेशवाहइभा
- **Translation**: 

---

