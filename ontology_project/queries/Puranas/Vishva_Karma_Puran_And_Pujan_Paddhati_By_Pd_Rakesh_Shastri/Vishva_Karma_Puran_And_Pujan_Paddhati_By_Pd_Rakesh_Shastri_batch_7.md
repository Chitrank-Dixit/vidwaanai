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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.121)
- **Original**: जैलोक्य-सूत्रकर्ततारं दिसुजं विश्वेदर्शितम्‌ । आगच्छ विश्वकर्मस्तें यज्ञेडस्मिनु सनिधो भव
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.122)
- **Original**: पार्थना-नमामि विश्वकर्माण दविभुजं विश्ववन्दितमू । गृहवास्तु-विधातारं महाबलपराक्रेममू
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.123)
- **Original**: प्रसीद विश्वकर्मस्तवं शिर्पजिद्यायिक्ञारद । दण्डपाणे ! नमस्तुम्यं तेजो मूर्तिघर प्रभो
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.124)
- **Original**: आसन- सुवर्णरचित देव ! दिव्यास्तरणशोभितम्‌ । आसन हि मया दत्त गृहाणाड्िरिसो-सुत
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.125)
- **Original**: पादार्य-इदं पाद्य मया दत्त सर्वसौगस्थसंयुतमू । गृहीत्वा विश्वकर्मेश प्रसनो भव वोस्तुज !
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.126)
- **Original**: दिव्यीौषधिरसोपेत . गन्ध-पुष्पाउक्षतै: सह
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.127)
- **Original**: गुहाणार्प्य मया दत्त विश्वकर्मनू कृपा कुरु
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.128)
- **Original**: जआचमन-सुगन्धवासितं दिव्यं॑ निर्मल संलिल विभो । सूहाणाउडचमनं सौम्य ! विश्वकर्मन्‌ कुपां कुरु
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.129)
- **Original**: मधुपरक-नमो देवाय भद्राय यृहनिर्माणशालिने ! । मधघुपर्क गृहाणेद॑ विश्वकर्मन्‌ सुधोपमम्‌
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.130)
- **Original**: पंचामृत से स्नान कराकर विशुद्ध जल से स्नान कराये- पच्लामृतं मया नीत॑ पयो दधि चूत मधु । शुद्ध॑शर्करया युक्त विश्वकर्मनू ! प्रयूह्मतामू
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.131)
- **Original**: गंगाजल समानीतें. सर्वपापहरं शुभमू । पू्त॑ पयोउधवा दिव्य॑ रनानार्थ प्रतियूद्वतामू ! । यस्त्र यज्ञोपवीत-- स्वदेशनिर्पित॑ वस्त्र॑ नूतन पावन परमू। . शरीराच्छादनाथयि . गृह्तां सून्वर््धन !
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.132)
- **Original**: । नवभिस्तन्तुभियुक्तै निगुणं देक्तामयमू। ज्पवीत्त मया दत्त गृद्यतां . धर्मनन्दन भूषण चंदन- शिरस्क॑ कुण्डलें हार॑ सोत्तरीयं तथैव च। अलंकार प्रगृह्माउत्र विश्वकर्मनू ! प्रसीद वै
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.133)
- **Original**: श्रीखण्ड॑ चन्दन दिव्य गन्धढू्य सुमनोहर्मू। विलेपनं सुरश्रेष्ठ ! गृहायतां वन्दनं शुभमु
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.134)
- **Original**: अक्षत-अशताश्द कलानार । चुकमाकाः: सुशोभिताः मया निवेदिता भक्त्या यूहाण दास्तुनन्दन
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.135)
- **Original**: पृष्य- मल्लिकादि सुगन्धीनि मालत्यादीनि वै प्रथो । मयाहतानि पूजार्थ पुष्पाणि प्रतिगृद्मतामू
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.136)
- **Original**: सौरभाणि सुमाल्यानि सुपुष्प-रचितानि वै। मया निवेदितान्यत्र शिल्पाचार्य ! सुगृह्मताम्‌
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.137)
- **Original**: तुलसीदल या बिल्वपन्र चढ़ाने का मन्त्र [8 श्री विश्वकर्मा पुराण एवं पूजन पद्धति 'श्री विश्वकर्मा पुराण एवं पूजन पद्धति
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.138)
- **Original**: कोमलानि सुगन्धीनि मंजरी संयुतानि च। तुलस्याः सदलान्यद्य विश्वकर्मन्‌ ! प्रगृह्मतामू
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.139)
- **Original**: निदलैविल्वपत्रैश्च कोमलै: शडरप्रियै: । तव पूजां करिष्यामि प्रसीद शिल्पिनांवर !
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.140)
- **Original**: धूप- वचस्पत्ति-रसोदूभूतं _ सुगन्धाटूयं मनोहरम्‌ । घूप॑ गृहाण कर्मेश ! द्रुतकर्म-परायण !
- **Translation**: 

---

