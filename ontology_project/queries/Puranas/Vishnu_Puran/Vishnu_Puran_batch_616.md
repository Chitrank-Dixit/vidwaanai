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

### Verse 1 (Vishnu Puran 0.12301)
- **Original**: आपस्तदा प्रवृद्धास्तु वेगवत्यो महास्वना:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12302)
- **Original**: 15 सर्वमापूरयन्तीद॑ तिष्ठन्ति विचरन्ति च। है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12303)
- **Original**: उस रात्रिका अन्त होनेपर अजन्मा भगवान्‌ विष्णु जागते हैं और बह्मारूप धारणकर, जैसा तुमसे पहले कहा था उसी क्रमसे फिर सृष्टि रचते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12304)
- **Original**: हे द्विज ! इस प्रकार तुमसे कल्पान्तमें होनेवाले नैमित्तिक एवं अवान्तर-प्रकूयका वर्णन क्रिया । अब दूसरे प्राकृत प्रकयका वर्णन सुनो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12305)
- **Original**: हे मुने
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12306)
- **Original**: अनाचृष्टि आदिके संयोगसे सम्पूर्ण व्लेक और निश्विल पातालोंके नष्ट हो जानेपर तथा भगवदिच्छासे उस प्रकयकालके उपस्थित होनेपर जब महत्तत््व्से छेकर [ पृथिंवी आदि पद्च ] विदेषपर्यन्त सम्पूर्ण विकार क्षीण हो जाते हैं तो प्रथम जल पृथिवीके गुण गर्बको अपनेमें लीन कर लेता है । इस प्रकार गन्ध छिन लिये जानेसे पृथिवीका प्रलय हो जाता है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12307)
- **Original**: 12--154
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12308)
- **Original**: गख्ध-तन्मात्राके नष्ट हो जानेपर पृथिवी जलमय हो जाती है, उस समय बड़े बेगसे घोर जाब्द करता हुआ जल बढ़कर इस सम्पूर्ण जगतको ज्याप्त कर लेता है। यह जल कभी स्थिर होता और कभी बहने सल्जलिनोमिंमालेन लोका व्याप्ताः समनन्‍्तत:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12309)
- **Original**: हगता है। इस प्रकार तस्क्॒माल्ओसे पूर्ण इस जलसे अपामपि गुणो यस्तु ज्योतिषा पीयते तु सः । नव्यन्त्यापस्ततस्ताक्ष रसतन्पात्रसंक्षयात्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12310)
- **Original**: । 17 ततश्वापो हतरसा ज्योतिष प्राधुवन्ति वै। अग्न्ववस्थे तु सलिले तेजसा सर्वतो वृते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12311)
- **Original**: 18 स चाम्ि: सर्वतो व्याप्य चादत्ते तज्जलं तथा । सर्वमापूर्यतेः्चिर्भिस्तदा जगदिदं शनै:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12312)
- **Original**: 19 अर्चिर्भिस्संबृते तर्स्मिस्तिय॑गूर्ध्वमथस्तदा । ज्योतिषो5पि परं रूप॑ बायुरत्ति प्रभाकरम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12313)
- **Original**: 20 प्रलीने च्र ततस्तस्मिन्वायुभूतेडखिल्लात्मनि । प्रणष्टे रूपतन्मात्रे इतरूपो विभावसु:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12314)
- **Original**: 21 प्रशाम्यति तदा ज्योतिर्वायुदोधूयते महान्‌ । निरात्ल्ेके तथा त्जेके वाव्ववस्थे च तेजसि
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12315)
- **Original**: 22 ततस्तु मूलमासाद्य वायुस्सम्भवमात्मन: । ऊर्ध्व चाधश्च तिर्यक्न॒ दोधवीति दिशों दश
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12316)
- **Original**: 23 वायोरपि गुण स्पर्शमाकाशों ग्रसते ततः । प्रशाम्यति ततो वायु: ख॑ तु तिप्ठत्यनावृतम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12317)
- **Original**: 24 । सम्पूर्ण लोक सब ओरसे न्याप्त हो जाते हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12318)
- **Original**: तदनन्तर जह्के गृण रसको तेज अपनेमें लीन कर लेता है। इस प्रकार रस-तन्मात्राका क्षय हो जानेसे जल भी नष्ट हो जाता है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12319)
- **Original**: तब रसहीन हो जानेसे जल अग्निरूप हो जाता है तथा अग्रिके सघ ओर व्याप्त हो जानेसे जलके अग्रिमें स्थित हो जानेपर वह अग्नि सब ओर फैलकर सम्पूर्ण जलको सोख लेता है और धीरे-धीरे यह सम्पूर्ण जगत्‌ ज्वाल्मसे पूर्ण हो जाता है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12320)
- **Original**: जिस समय सम्पूर्ण लोक ऊपर-नीचे तथा सब ओर अरग्रि-शिखाओंसे व्याप्त हो जाता है उस समय अग्रिके प्रकाशक स्वरूपको वायु अपनेमें लीन कर छेता है
- **Translation**: 

---

