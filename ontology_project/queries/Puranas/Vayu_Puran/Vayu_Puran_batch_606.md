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

### Verse 1 (Vayu Puran 0.12101)
- **Original**: वामहस्ते शिलायास्तु तया चोद्स्तकों गिरिः
- **Translation**: 

---

### Verse 2 (Vayu Puran 0.12102)
- **Original**: 43 स पव॑तः समानीतो ह्यगस्त्येन महात्मना- । तत्र ब्रह्मा हरेश्वैव तपश्चोग्रं च चक्रतुः
- **Translation**: 

---

### Verse 3 (Vayu Puran 0.12103)
- **Original**: डड तत्रागस्त्यस्थ हि वरं कुण्ड त्रलोक्यदु्लभम्‌ । यत्र सुन्यष्ठकं सिद्ध तपस्तप्त्वा शिवं गतमू
- **Translation**: 

---

### Verse 4 (Vayu Puran 0.12104)
- **Original**: .. कुण्डे मुन्यष्टक नत्वा पित ब्ह्मपुरं नयेत्‌
- **Translation**: 

---

### Verse 5 (Vayu Puran 0.12105)
- **Original**: 44 अगस्त्येनाथ देवषें उद्रयाद्रेमहात्मना । शिलाया बामहस्तेडपि स्थापितों गिरिराद्शुभः
- **Translation**: 

---

### Verse 6 (Vayu Puran 0.12106)
- **Original**: *बादित्रद्योदिव्यमितेराध्ो वादिश्रको गिरिः 746 है उतके केवल दर्शन करने से मनुष्य पाप कर्मो से मृक्ति पा जाता है। शिला के बाएँ हाथ पर उद्यल्वक नामक गिरि अतिष्ठित है, महात्मा अगस्त्थ ने उस पर्वत को यहाँ लाकर स्थापित किया था। उस पव॒त प्रान्त में भगवान्‌ ब्रह्मा एवं शिव ने उग्र तपस्या की थी। वहाँ अगस्त्य का त्रैलोक्य दुर्लभ परम रमणीय कुण्ड है, जिसमें आठ मुनियों ने परम कठोर तपस्या कर सिद्धि एवं शिव की प्राप्ति की थी। उस कुण्ड में उक्त आठों मुत्रियों को नमस्कार कर मनुष्य अपने पितरों को ब्रह्मपुर पहुंचाता है ।40-45। देवषि नारद जी ! महात्मा अगस्त्य ने शिला के बाएं हाथ पर उदयाचल पर्वत से लाकर इस पव॑त की स्थापना की थी, जो ++इत उत्तरमेते श्लोका मुद्रितपुस्तकपाठेडधिका उपलब्यन्ते-- स्थापित: विण्डदस्तत्र पितन्श्रह्मपुरं नयेत्‌ । कुण्डइचोचच्तकस्तत्र आपत्मनस्तसा कृत:
- **Translation**: 

---

### Verse 7 (Vayu Puran 0.12107)
- **Original**: ब्रह्मणा तत्र सावित्रीकुमाराभ्यां सह स्थितम
- **Translation**: 

---

### Verse 8 (Vayu Puran 0.12108)
- **Original**: हाहाहूहुप्रभूतयों गीतिनादं प्रचक्रिरे
- **Translation**: 

---

### Verse 9 (Vayu Puran 0.12109)
- **Original**: कुण्डमुश्च न्तरक॑ तत्र गीतवादित्रको ग्रिरि: । अग्रस्त्यो भगवान्यत्र तपश्चोग्न चकार ह
- **Translation**: 

---

### Verse 10 (Vayu Puran 0.12110)
- **Original**: ब्रह्मणस्तु बर लेभे माहात्म्यं भुवि दुलेभम्‌ । लोपामुद्रां तथा भार्यां पित णां परमां गतिम्‌
- **Translation**: 

---

### Verse 11 (Vayu Puran 0.12111)
- **Original**: स्‍्नातस्तत्र च मध्याह्न साबित्रीं समुपास्य च। कोटिजन्म भवेद्विप्रो धनाढ्यों वेदपारमः
- **Translation**: 

---

### Verse 12 (Vayu Puran 0.12112)
- **Original**: 5।। अगस्त्यस्य पदे स्तात्वा पिण्डदो“ब्रह्मलोकग्ः । पितृत्तिः सह धर्मात्मा पुम्यमानों दिवौकसाम्‌
- **Translation**: 

---

### Verse 13 (Vayu Puran 0.12113)
- **Original**: ब्रह्मयोनि प्रविश्याथ निर्गच्छेद्यस्तु मानव: । परं ब्रह्म स यातीह विमुक्तो योनिसंकटात्‌
- **Translation**: 

---

### Verse 14 (Vayu Puran 0.12114)
- **Original**: नत्वा गयाबुमारं च ब्राहण्यं लभते नरः
- **Translation**: 

---

### Verse 15 (Vayu Puran 0.12115)
- **Original**: सोमकुण्डाभिषेकी च सोमलोक नयेत्पित न्‌
- **Translation**: 

---

### Verse 16 (Vayu Puran 0.12116)
- **Original**: बलि; काकिलायां तु काकेम्य ऋणमोक्षद: । स्वगंद्वारेश्वरं नत्वा स्वगदित्ह्मापुरं ब्रजेत्‌
- **Translation**: 

---

### Verse 17 (Vayu Puran 0.12117)
- **Original**: पिण्डदो व्योमगज्ायां निर्मलः स्वनंयेपित॒ न । झिलाया दक्षिणे हस्ते भस्मकूटमधारयत्‌
- **Translation**: 

---

### Verse 18 (Vayu Puran 0.12118)
- **Original**: ततोश्सों भस्मकटा द्विभस्मस्तातश्व नारद
- **Translation**: 

---

### Verse 19 (Vayu Puran 0.12119)
- **Original**: 10।। वटो वटेइवरस्तन्न स्थितरच प्रपितामहः । मतद्भस्य पदे मुन्‍्ये पिण्डव: स्वर्नयेत्पित्‌ न्‌
- **Translation**: 

---

### Verse 20 (Vayu Puran 0.12120)
- **Original**: *हृदमर्ध॑ नास्ति ल, पुस्तके ।।
- **Translation**: 

---

