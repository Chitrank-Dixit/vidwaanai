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

### Verse 1 (Vishnu Puran 0.12241)
- **Original**: 28 तस्मादपि महातापतप्ता लोकात्तत: परम्‌। गच्छन्ति जनलोकं ते दशावृत्त्या परैषिण:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12242)
- **Original**: 29 ततो दग्ध्वा जगत्सर्व रुद्ररूपी जनार्दनः । मुखनि:श्वासजान्पेघान्करोति मुनिसत्तम
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12243)
- **Original**: 30 ततो गजकुलप्रख्यास्तडित्वन्तोउतिनादिनः । उत्तिष्ठन्ति तथा व्योप्ि घोरास्संबर्तका घना:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12244)
- **Original**: 39 केचिन्नीलोत्पलश्यामा: केचित्कुपुदसत्रिभा: । धूप्रवर्णा घना: केचिस्केचित्पीता: पयोधरा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12245)
- **Original**: 32 केचिद्रासभवर्णाभा लाक्षारसनिभास्तथा । केचिहैडयसड्भाशा इ्ननीलनिभा: क्कच्तित्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12246)
- **Original**: 33 शब्बकुन्दनिभाश्चान्ये जात्यज्ञननिभा: परे । इन््रगोपनिभा: केचित्ततश्शिखिनिभास्तथा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12247)
- **Original**: 34 मनहिशलाभा: केचिद्दै हरितालनिभा: परे । चाषपत्रनिभा: केचिदुत्तिप्ठन्ने महाघनाः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12248)
- **Original**: 35 केचित्पुरवराकारा: केचित्पर्वतसन्निभा: । कूटागारनिभाश्षान्ये केचित्स्थलनिभा घना:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12249)
- **Original**: 36 महारावा महाकाया: पूरयन्ति नभ:स्थलम्‌ । वर्धन्तस्ते. महासारांस्तमभिमतिभैरवम्‌ । शमयन्त्यस्लं विप्र त्ैलोक्यान्तरधिष्ठितम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12250)
- **Original**: 37 नष्टे चाम्ो च सतत वर्षमाणा ह्वाहर्निशम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12251)
- **Original**: प्रावयन्ति जगत्सर्वमम्भोभिर्मुनिसत्तम
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12252)
- **Original**: 38 [ अन् 3 तन, सबको नष्ट करनेके छिये उच्यत हुए श्रोहरि क्यालाप्रिरुद्ररूपसे शेषनागके मुखरो प्रकट होकर नीचेसे पातास्जेंकों जल््रना आरम्भ करते हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12253)
- **Original**: वह महान अग्नि समस्त पातालॉंको जल्मकर पृथिवीपर पहुँचता है और सम्पूर्ण भूतकको भस्म कर डालता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12254)
- **Original**: तय यह दारूण अप्नि घुनलेंक तथा स्वर्गलोकको जल्त्र डालता है. और वह ज्वाला-समूहका महान्‌ आवर्त वहीं चक्कर लगाने लगता है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12255)
- **Original**: इस प्रकार अग्निके आवर्तोसे घिरकर सम्पूर्ण चराचरके नष्ट हो जानेपर समस्त त्रिल्त्रेकी एक तप्त कराहके समान भ्रत्तीत होने लगती है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12256)
- **Original**: हे महामुने ! तदनन्तर अवस्थाके परिवर्तनसे परलोककी चाहबाले भुबलॉंक ओर स्वर्गल्लेकमें रहनेवाले
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12257)
- **Original**: मन्‍्यादि
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12258)
- **Original**: अधिकारिगण अग्रिज्वाल्से सन्तप्त होकर महर्स्कको चले जाते हैं किन्तु वहाँ भी उस उम्र कालानलके महातापसे सत्तप्त होनेके कारण ये उससे बचनेके लिये जनल्त्रेकमें चले जाते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12259)
- **Original**: हे मुनिश्रेष्ठ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12260)
- **Original**: तदनन्तर रुद्ररूपी भगतान्‌ तिष्णु सम्पूर्ण संसारको दग्ध करके अपने मुख-निःधाससे मेघोंको उत्पन्न करते हैं
- **Translation**: 

---

