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

### Verse 1 (Vishnu Puran 0.11601)
- **Original**: द्विक्िद नामक एक महावीर्यशाल्ली. वानस्श्रे.- देव-विरोधी _दैत्यराज नरकासुरका मित्र था
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11602)
- **Original**: भगवान्‌ कृष्णने देवराज इन्द्रकी प्रेरणासे नरकासुरका वध किया था, इसल्ल्ये बोर वानर द्विविदने देवताओंसे वैर ठाना
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11603)
- **Original**: [उसने निश्चय किया कि] "मैं मर्त्तलोकका क्षय कर दूँगा और इस प्रकार यज्ञ-यागादिका उच्छेद करके सम्पूर्ण देवताओंसे इसका बदला चुका रुँगा"
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11604)
- **Original**: तबसे बह अज्ञानमोहित होकर यज्ञॉको विध्बंस करने लगा और साधुमर्यादाकों मिटाने तथा देहघारी जीवॉक्मे नष्ट करने कछगा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11605)
- **Original**: बह बन, देश, पुर और भिन्न-भिन्न आमोंकों जल्म्र देता तथा कभी पर्वत गिराकर ग्रामादिकोंको चूर्ण कर डालता
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11606)
- **Original**: कभी पहाड़ोंकी चट्टान उाइकर समुद्रके जलमें छोड़ देता और फिर कभी समुद्रमें घुसकर उसे क्षुभित कर देता
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11607)
- **Original**: हे द्विज ! उससे क्षुभित हुआ समुद्र ऊँची-ऊँचो तसझ्लोंसे उठकर अति बेगसे युक्त हो अपने तीरवर्ती ग्राम और पुर आदिको डुबो देता था
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11608)
- **Original**: कह कामरूपी बानर महान्‌ रूप घारणकर स्पेटने लूगता था और अपने लुण्ठनके संघर्षसे सम्पूर्ण धान्यों (खेतों) को कुचल डालता था
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11609)
- **Original**: हे ट्विज ! उस दुरात्पाने इस सम्पूर्ण जगत्‌को स्वाध्याय और वषट्कारसे शून्य कर दिया था, जिससे यह अत्यन्त दुःखमय हो गया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11610)
- **Original**: एक दिन श्रीबलभद्रजी रैबलोद्यानगें [ क्रीड़ासक्त होकर ] मदपान कर रहे थे। साथ ही महाभागा रेवती तथा अन्य सुन्दर रमणियाँ भी थीं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11611)
- **Original**: उस समय यदुश्रेष्ठ श्रीबकरामजी मन्दराचल पर्वतपर कुब्रेरके समान [ रैक्तकपर स्वयं ] रमण कर रहे थे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11612)
- **Original**: इसी समय वहाँ द्विकिद वानर आया और श्रीहलधरके हल और मूसल लेकर उनके सामने हो उनकी नकल करने लूगा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11613)
- **Original**: वह दुरात्मा कानर उन स्ियोंकी ओर देख- देखकर हँसने छगा और उसने मदिरासे भरे हुए घड़े प्वेड़कर फेंक दिये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11614)
- **Original**: अआ* के7 ] ततः कोपपरीतात्मा भर्स्सयामास त॑ हली। तथापि तमवज्ञाय चक्रे किलकिलध्वनिम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11615)
- **Original**: 15 ततः स्मयित्वा स बलो जग्राह मुसल॑ रुषा । सो5पि शैलशिलां भीमां जग्राह प्लवगोत्तम:ः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11616)
- **Original**: 16 चिक्षेप स च तां क्षिप्तां मुसलेन सहस्रधा । यादवश्रेष्ठस्सा पपात महीतले
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11617)
- **Original**: 17 अथ तन्पुसलं चासौ समुल्लद्ध्य प्र॒वड्भम: । वेगेनागत्य. रोषेण करेणोरस्यताडयत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11618)
- **Original**: 18 ततो बलेन कोपेन मुष्टिना मूर्ध्नि ताडित: । पपात रुधिरोद्धारी द्विविदः क्षीणजीवितः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11619)
- **Original**: 19 पतता .तच्छरीरेण .गिरेश्थूड्रमशीर्यत । मैत्रेय शतथा वज्िवज्रेणेव विदारितम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11620)
- **Original**: 20 पुष्पवृष्टि ततो देवा रामस्योपरि चिहक्षिपु: । प्रशशंसुस्ततो5भ्येत्य साध्वेतत्ते महत्कृतम्‌
- **Translation**: 

---

