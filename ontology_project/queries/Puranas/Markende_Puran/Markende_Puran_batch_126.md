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

### Verse 1 (Markende Puran 0.2501)
- **Original**: -इतरा अधिक पाठ है।
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2502)
- **Original**: 198 “संक्षिप्त मार्केण्डेयपुराण * 4445545:6:₹ %60/0 3 7 77555 7 90107 4 3557 & # 4. & 6 45::4::4:::::520:8:7:% 45 7075 7 + 7 + 10 +5 ++6 #% 6 %8.4:4:44::534.320 0 हल 7 7 755 & 6 #& 6: अतुर्थोउध्याय: इन्द्रादि देवताओंद्वारा देवीकी स्तुति ध्याच या श्री: स्वयं सुकृतिमाँ भवनेष्चलक्ष्मी: ( <“0कालाभ्राभों कदाह्षैररिकुलभयदां भौलिकद्वेट्ेरखां प्रापात्मनां कृतभियां हृदयेषु बुर्द्धि:। श्डू चक्रे कुपाणं ब्रिशिखमपि कररुद्ठहन्ती त्रिनेत्राम्‌। श्रद्धा सतां कुलजनप्रभवस्थ .लज्जा सिंहस्कन्धाथिरूडां त्रिभुवनमखिल॑ तेजसा पूरयन्तों ता त्वां ना: स्मपरिपालबदेनिलिशम
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2503)
- **Original**: ध्यायेद्‌ दुर्गा जयारां ब्रिदशपरिवृत्ां सेदितां सिर्द्रिकामे
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2504)
- **Original**: कि. वर्णयाम तव रूपमचिन्यमेतत्‌ सिंद्धिकी इच्छा रखनेबत्राले पुरुष जिनकी सेवा कि चातिवीर्यमसुरक्षबक्तारि भूरि। करते हैं तथा देवता जिन्हें सल्त ओग्से घेरे रहते
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2505)
- **Original**: कि चाहवेघु चरितानि तंवाद्धुतानि उन 'जवा' गामवाली दुर्भादेवीका ध्यान करे। सर्वेषु देव्यसुरदेवगणादिकेघु
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2506)
- **Original**: उसके श्रोअज्ञोंकी आभा काले मेवके समान
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2507)
- **Original**: हेतुः सपस्तजगतां त्रिगुणापि दोप श्याप है। ते अपने कठाक्षोंसे शत्रुसपृहंको भव
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2508)
- **Original**: र्न॒ज्ायसे हरिहरादिभिरष्यपारा। प्रदान करती हैं । उनके मस्तकपर आबडद्ध चन्द्रमाको
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2509)
- **Original**: सर्वाअश्रयाखिलपिर्द जगदंशभूत- रेखा शोभा पाती हैं। वे अपने हार्थोर्में शद्दु, चक्र, मव्याकृता हि परमा प्रकृतिस्त्वमाद्या
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2510)
- **Original**: कृपाण और नत्रिशूल धारण करती हैं। उनक्रे तीन
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2511)
- **Original**: यस्याः. सपस्तसुरता. समुदीरणेन नेत्र हैं।जे सिंहके कंभैपर चढ़ी हुईं हैं और अपने
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2512)
- **Original**: तृप्ति प्रमाति सक्लेषु मखेशु देलि। तेजसे तीतों लोकोंकों परिपूर्ण कर रहीं हैं।)
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2513)
- **Original**: स्वाहासि जे पितृगणस्थ चर तृप्तिहेतु- झापिरवाक 4 1 5 म रुच्चार्यसे त्वमत एबं जनैः स्वधा च
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2514)
- **Original**: '#' शक्रादयः सुरगणा निहतेअतिवीें या मुक्तिहेतुरविचिन्यमहात्रता त्व- तस्मिल्‍ुसात्मनि सुरारिबले च देव्या। प्रभ्यस्यसे. सुनिसतेन्द्रियतत्त्यसारि:। तां तुश्ृबु: प्रणतिनारालिरोधरांसा मोक्षार्थिभिमुनिभिरस्तसपस्तदोचै- वाग्मि: _ प्रहर्पपुलकोट्रमचारुदेहा:
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2515)
- **Original**: चिंद्यासि सा भगवत्ती परपा हि देवि
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2516)
- **Original**: देव्या ग्रया ततमिर्द जगदात्मशक्त्या शब्दान्मिका सुविमलग्यज़ुपां निधान- निश्शेषदेयगणज्ञक्तिसपूहमूर्ता
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2517)
- **Original**: । मुद्दी थरप्मपदपाठवताो ज्ञ॒ साप्ताम्‌। ताम्रध्विकामखिलदेवमहर्थिपुज्यां देवी असी भगवती भवभावनाय भक्त्या नता; स्थ विदधातृ शुभानि सा न:
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2518)
- **Original**: वार्ता ज्ञ सर्वजगतां परमा्शिह्जी
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2519)
- **Original**: बस्वाः प्रभावपतुल॑ भगबाननन्तो प्रेधाप्ति देवि विदिताखिलशास्वसारा ब्रह्मा हरश न हि बक्तुमल॑ बल॑ ञ्। दुर्गांसि वुर्गभवसागरनौरसड्भा । सा चण्डिक्राणथिलजगत्परिपालनाय श्री; कैटभारिंद्दबैककृताधियासा नाज्ञाय चाशुभभधस्थ मतिं करोतु
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2520)
- **Original**: शौरी त्यमेव शशिमौलिकृतप्रतिष्ठा
- **Translation**: 

---

