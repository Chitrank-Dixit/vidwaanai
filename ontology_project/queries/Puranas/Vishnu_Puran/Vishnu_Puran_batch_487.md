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

### Verse 1 (Vishnu Puran 0.9721)
- **Original**: पर्व॑तकों उखाड़ लेनेपर शूरनन्दन श्रीइ्यामसुन्दरने गोपोंसे हँसकर कहा-- 'आओओ, शीघ्र ही इस पर्वतके नीचे आ जाओ, मैंने वर्षासे बचनेका प्रबन्ध कर दिया है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9722)
- **Original**: यहाँ वायुहीन स्थानॉमें आकर सुल्वपूर्वक्ष बैठ जाओ; निर्भय होकर प्रवेश करो, पर्बतके गिरने आदिका भय मत करो”
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9723)
- **Original**: श्रोकृष्णचन्द्रके ऐसा कहनेपर जलकी धाराओंसे पीडित गोष और गोपी अपने बर्तन-भाँडोंको छकड़ोंमे रखकर गौओंके साथ पफ््वतके नीचे चले गये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9724)
- **Original**: ब्रज-वासियोंद्रारा हर्ष और विस्मयपूर्वक टकटकों लगाकर देखे जाते हुए श्रीकृष्णचन्द्र भी गिरिराजको अत्पन्त निश्चलतापूर्वक धारण किये रहे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9725)
- **Original**: जो प्रीतिपूर्बक आँस्थे फाड़कर देख रहे थे उन हर्षित-चित्त गोपष और गोपियोंसे अपने चरितोंका स्तवन होते हुए. श्रीकृष्णचन्द्र पर्वतको धारण किये रहे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9726)
- **Original**: हे त्रिप्र ! गोपोंके नाशकर्ता इन्द्रकी प्रेरणासे नन्‍्टजीके गोकुल्में सात राप्रितक महाभयंकर मेघ बरसते रहे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9727)
- **Original**: किंतु जब श्रीकृष्णचद्धनें पर्बत धारणकर गोकुल्की रक्षा को तो अपनी प्रतिज्ञा व्यर्थ हो जानेसे इन्द्रने मेघोंको रोक दिया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9728)
- **Original**: आकाशके मेघहोन हो जानेसे इन्द्रकी प्रतिज्ञा भंग हो जानेपर समस्त गोकुल्थ्बासी वहाँसे निकलकर अप्रसन्नतापूर्वकः फिर अपने-अपने स्थानोंपर आ गये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9729)
- **Original**: और कृष्णबद्धने भी उन ब्रज्वासियोंके विस्मयपूर्वक देखते-देशते गिरिराज गोवर्थनक्ो अपने स्थानपर रख दिया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9730)
- **Original**: नमन जी अनन«-»न इति श्रीविष्णुपुगाणे पञ्ममेंइशे एकादशोउध्यायः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9731)
- **Original**: >0-_-_--- जुड़. 00000
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9732)
- **Original**: अ«* 12 ] 'फक्कम अंश 349 बारहवाँ अध्याय दाक़-कृष्ण-संखाद, कृष्पा-स्तुति श्रीपताञ्र उवाब धृते गोवर्धने शौले परित्राते च गोकुले । रोचयामास कृष्णस्य दर्शन पाकशासन:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9733)
- **Original**: 95 सोउथिरुद्दा महानागमैरावतममित्रजित्‌ । गोबर्धनगिरौ कृष्ण ददर्श त्रिदशेश्वरः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9734)
- **Original**: 2 चारयन्तं महावीय॑ गास्तु गोपवपुर्धरम्‌। कुर्स्त्रस्य जगतो गोप॑ यृत॑ गोपकुमारकै:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9735)
- **Original**: 3 गरुढड च॒ ददणशोशिस्न्तर्द्धानगतं ट्विज । कृतच्छायं हरेमूह्नि पक्षाभ्यां पक्षिपुड्डलम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9736)
- **Original**: 4 अवसरुह्य स॒नागेद्धादेकान्ते मधुसूदनम्‌। शक्रस्सस्मितमाहेद॑ प्रीतिविस्तारितेक्षण:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9737)
- **Original**: 5 इन्द्र उवान कृष्ण कृष्ण श्ृणुप्लेदे यदर्थमहमागत: । त्वत्समीपं मरहायाहो नैतशिन्त्यं त्ववान्धथा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9738)
- **Original**: 6 भारावतारणार्थाय पृथिव्या: पृथिवीतले । अवतीणों5खिलाधार ॒त्वमेव परमेश्वर
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9739)
- **Original**: 7 मस्वभड्डविरोधेन मया गोकुलनाशकाः । सरमादिष्टा पहामेघास्तैख्वेंद कदन॑ कृतम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9740)
- **Original**: 8 ब्रातास्ताश्न त्वया गावस्समुत्पाट्य महीधरम्‌ । तेनाई तोषितो बीरकर्मणात्यद्धतेन ते
- **Translation**: 

---

