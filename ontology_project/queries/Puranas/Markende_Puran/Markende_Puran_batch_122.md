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

### Verse 1 (Markende Puran 0.2421)
- **Original**: उद्गग्रश्न॒ रणे देव्या शिलावृक्षादिधिईतः। दन्तमुष्ठितलैसेव करालश् निषातित:
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2422)
- **Original**: देवी क्रुद्धा गदापातेश्ूूर्णयामास चौद्धतम। वाघ्कलं भिन्दिपालेन बाणैस्ताप्रं तथान्थक्रम्‌
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2423)
- **Original**: उग्रास्यमुग्रबीर्द॑ च तपथैध ञ्ञ महाहनुम।
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2424)
- **Original**: ब्रिनेत्रा च॒ विशूलेन जथान परमेश्वरी
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2425)
- **Original**: बिडालस्यासिना कायात्यातयामास से शिरः
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2426)
- **Original**: दुर्शर दुर्पुख्खन चोभी शरेरनिन्ये यमक्षयम्‌
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2427)
- **Original**: महिपासुरके सेतापति उस महापराक्रमी चिक्षुस्क्ते मरे जानेपर देवताओंकों पीड़ा देनेवाला चामर हाथीपर चदकर आया। उसने भी देवीके ऊपर शक्तिका प्रहार किया, किन्तु ज़गदप्बागे उसे अपने हुंकारसे हो आहत एवं निष्प्रभ करके हत्काल पृथ्वीपर गिरा दिया
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2428)
- **Original**: शरक्तिकों टृूटकर गिरी हुई देख चामरकों बड़ा क्ोष हुआ। अब उसने शूल चलाया, फिन्तें देबीने ठसे भी अपने बाणोंद्राय काट डाला
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2429)
- **Original**: इतनेमें ही देवीका सिंह उछलऋर हाथोके मस्तकपर चढ् बैठा और टस दैत्यके राथ खूब जोर लगाकर बाहुबुद्ध करने लगा
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2430)
- **Original**: वे दोनों लड़ते- लड़ते हाथीसे पृथ्खोपर ऊआ गये और अत्वन्त ऋोधमें भरकर एक दूसरेपर बड़े भयंकर बाहयुझ्धेन स्रुयुभे तेनोच््स्त्रिदशारिणा
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2431)
- **Original**: प्रहार करते हुए लड़ने लगे
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2432)
- **Original**: तदनततर युद्ट्यामानी ततस्ती तु तस्यात्रागास्मही गती। युयुधातेदनिरंरव्धी 1, इसपर झाए किसी कसी ध्रतिरें-- काश बे ऊझालदारेन काजरय अश्शोषणम्लोमावशकिटज्ा “थे ऐ श्लोफ़ श्रष्क हैं। 4(प84
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2433)
- **Original**: । उप्रदर्शनमत्यग्रे रण त्ववे । गएँ: सिंहेत पेज्या च दाय#तेडक्तीलानै,
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2434)
- **Original**: सिंह जड़े बेगसे आकाशकी और उछला और प्रहाररतिदारुएौँ:
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2435)
- **Original**: उधरसे गिरते समय उम्रने पं॑जोंकी पारतें चामरझा खाइगपातर ताइणत
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2436)
- **Original**: + सेनायतिबोंसहित महिषासुरक्ता ्रध* इक 44454 ##& # 4 4 # «4 # 44 # #8 4 44 # 64 ज ऋ 57 कक +व 97 क कथा कक आधमध्का 8 कक ऋाऋााा 71 कक 7954 3 कल, सिर धड़से अलग कर दिथ।
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2437)
- **Original**: इसी प्रकार उद्म्न भी शिला और वृक्ष आदिकाी खाकर रणभूमिमें देवीके हाथसे मारा गया तथा ऋराल भी दाँतों, मुफ्तों और थप्पड़ोंकी चोटसे धराशायी हो गया
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2438)
- **Original**: क्रोधर्में भरी हुईं देवीने गदाकी चोंटसें उद्धतका कचूयर निकाल डाला। भिन्दिपालत्े वाष्कलको तथा जाणोंसे ताप्र और अन्धककों मौतके घाट उतार दिया
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2439)
- **Original**: तीन नेत्रोंत्राली परमेश्चरोये जिशूलसे उग्मास्य, उग्रत्रीव तथा पहाहनु दामक दैत्पकों मार ड़ाला
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2440)
- **Original**: तलवारकी चौट्से विडालके मस्तककों धड़से काट गिंराबा। दुर्धर और दुमुंख-8न दोनोंकों भो अपने बाणोंसे धसलोक भेज दिया
- **Translation**: 

---

