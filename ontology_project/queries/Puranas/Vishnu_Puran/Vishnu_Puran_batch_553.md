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

### Verse 1 (Vishnu Puran 0.11041)
- **Original**: 11--13
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11042)
- **Original**: है प्रभो! आपकी माया ही परमार्थकत्वके न जाननेवाले पुरुषोंको मोहित करनेवाली है जिससे मूढ पुल्ष अनात्पामें आत्पबुद्धि करके बन्धनमें पड़ जाते
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11043)
- **Original**: अ0 30 ] अस्वे स्वमिति भावोउन्न यत्युंसामुपजायते । अह मेति भावो यत्ायेणैवाभिजायते। संसारमातुर्मायायास्तवैतन्नाथ चेष्टितम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11044)
- **Original**: 15 यै: स्वथर्मपर्नाथ नरैराराधितों भवान्‌। ते तरन्त्यखिलामेतां मायामात्मविमुक्तये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11045)
- **Original**: 16 “77773 देवा : पशवस्तथा । :..
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11046)
- **Original**: 17 आराध्य त्वामभीप्सन्ते कामानात्मभवक्षयम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11047)
- **Original**: यदेते पुरुषा माया सवेर्य भगर्वस्तव
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11048)
- **Original**: 18 मया त्वे पुत्रकामिन्या सैरिपक्षजयाय च। आराधितो न मोक्षाय मायाविलसितं हि तत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11049)
- **Original**: 19 कप सफाइनआाक कक ऋापहाकत वाउछा तलपहमादि । यदपुण्यानां ह 4
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11050)
- **Original**: 20 तस्रसीदाखिलजगन्भायामोहकराव्यय_। अज्ञान॑ ज्ञानसद्धावभूत॑ भूतेश नाशय
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11051)
- **Original**: 21 नमस्ते चक्रहस्ताय शार्डहस्ताय ते नमः । गदाहस्ताय ते विष्णो झद्भ॒हस्ताव ते नम:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11052)
- **Original**: 22 एतत्पश्यामि ते रूप॑ स्थूलचिह्रोपलक्षितम। न जानामि परं यत्ते प्रसीद परमेश्वर
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11053)
- **Original**: 23 श्रीपताझर उवाच अदिल्यैवं स्तुतो विष्णु: प्रहस्याह सुरारणिम्‌! । माता देवि त्वमस्मार्क प्रसीद वरदा भव
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11054)
- **Original**: 24 अदितिस्वाच एबमस्तु तथेच्छा ते त्वमशेषैस्सुरासुरैः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11055)
- **Original**: अजेय: पुरुषव्याष्न मर्त्बलोके भविष्यसि
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11056)
- **Original**: 25 औपररशर उवाच ततः कृष्णास्य पत्नी च झक्रपल्यासहादितिम्‌। सत्यभामा प्रणम्याह प्रसीदेति पुनः पुनः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11057)
- **Original**: 26 अदितिल्वाच मत्प्रसादान्न ते सुभ्रु जरा वैरूप्यमेव वा । भविष्यत्यनवद्याड्डि सुस्थिरें नवयौवनम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11058)
- **Original**: 27 1- दीपयिवीम्‌ 389 हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11059)
- **Original**: है नाथ ! पुरुषको जो अनात्मामें आत्पबुद्धि और 'पैं-मेर' आदि भाव प्रायः उत्पन्न होते हैं वह सब आपकी जगज्जननी मायाका ही विल्लास है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11060)
- **Original**: हे नाथ ! जो स्वधर्मपरायण पुरुष आपकी आराधना करते हैं वे अपने मोक्षके लिये इस सम्पूर्ण मायाको पार कर जाते हैं
- **Translation**: 

---

