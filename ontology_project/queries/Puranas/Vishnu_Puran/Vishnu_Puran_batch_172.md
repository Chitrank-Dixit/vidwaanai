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

### Verse 1 (Vishnu Puran 0.3421)
- **Original**: कल्पान्तमें जिनके मूखोंसे वियाश्रिशिखाके समान देदीप्यमान संकर्षण- नामक रुद्र निकलकर तीनों छलोकॉंका भक्षण कर जाता है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3422)
- **Original**: ले समस्त देबगणोंसे बन्दित शेषभगवान्‌ अश्षेष भूमण्डलकों मुकुटबत्‌ धारण किये हुए पाताल- तकमें विराजमान हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3423)
- **Original**: उनका बल-बीर्य, प्रभाव, स्वरूप (तत्त्व) और रूप (आकार) देवताओँसे भी नहीं जाना और कहा जा सकता
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3424)
- **Original**: जिनके फर्णोकी मणियॉकी आभासे अरुण यर्ण हुई यह समस्त पथिवी फूल्लेंकी मालाके समान रखी हुई है उनके बल-वीर्यका वर्णन भल्त् कौन करेगा 2
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3425)
- **Original**: 122 श्रीविष्णुपुराण ( भ* 6 बदा बिजुम्भतेनन्तो मदाघूर्णितलोचनः । तदा चलंति भूरेषा साब्यधितोया सकानना
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3426)
- **Original**: 23 गन्धर्वाप्सरसः सिद्धाः किन्नरोरगचारणा: । नान्ते गुणानों गच्छन्ति तेनानन्तोउयमव्ययः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3427)
- **Original**: 24 यस्य नागवधूहस्तैलेंपित॑ हसिचिन्दनम्‌ ! पहु: श्वासानिलापास्तं याति दिक्षृदवासताम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3428)
- **Original**: 25 आमराराध्य पुराणर्धिगगगों ज्योतीषि तत्त्वतः । ज्ञातवान्सकलं चैव निमित्तपठितं फलम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3429)
- **Original**: 26 तेनेय॑ नागवर्येण शिरसा विधृता मही। बिभर्ति माल्ण छोकानां सदेवासुरमानुषधाम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3430)
- **Original**: 27 जिस समय मदमत्तनयन चोषजी जमुहाई लेते हैं उस समय समुद्र और यन आदिके सहित यह सम्पूर्ण पृथिवी चलायमान हो जाती है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3431)
- **Original**: इनके गुणोंका अन्त गर्व, अपसरा, सिद्ध, किन्नर, नाग और चारण आदि कोई भी नहीं पा सकते; इसलिये ये अविनाश देव 'अनन्त' कहत्खते हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3432)
- **Original**: जिनका नाग- वधुओंद्वारा छेपित हरिचन्दन पुनः-पुनः श्वास-वायुसे छूट- छूटकर दिज्ञाओंको सुगन्बित करता रहता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3433)
- **Original**: जिनकी आयधनासे पूर्वकालीन महर्षि गगने समस्त ज्योतिर्मण्डल (ग्रहनक्षत्रादि) और शकुन-अपशकुनादि नैमिश्षिक फर्णोकों उत्वतः जाना था
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3434)
- **Original**: उन नागगश्रेष्ठ शेषजीने इस पथिवीको अपने मस्तकपर धारण किया हुआ है, जो स्क्यै भी देव, असुर और मनुष्येके सहित सम्पूर्ण व्येकमाल्ा (पातात्यदि समस्त ल्लेकों) के धारण किये हुए हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3435)
- **Original**: री इति श्रीविष्णुपुराणे ट्वितीयेंडशे पञ्चममोउध्याय:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3436)
- **Original**: न्न्क्त्त् औ करत छठा अध्याय प्रिन्न-भिन्न नरकोंका तथा भगवन्नामके माहात्व्यका वर्णन श्रीपराझर उवाच ततश्न नरका विप्र भुवो5धः सल्किलस्थ च
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3437)
- **Original**: पापिनो येघषु पात्यन्ते ताउच्छृणुष्ठ महामुने
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3438)
- **Original**: 9 रौरवः सूकरो रोध्वस्तालो व्रिशसनस्तथा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3439)
- **Original**: महाज्वालस्तप्तकुम्भो लकणो5थ विलोहित:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3440)
- **Original**: 2 रुधिराओो बैतरणि: कृमीश: कृमिभोजन: । असिपत्रवनं कृष्णो छालाभक्षश्ष दारुण:
- **Translation**: 

---

