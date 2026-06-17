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

### Verse 1 (Vishnu Puran 0.12061)
- **Original**: कलियुगके आनेपर राजाल्मेग प्रजाकी रक्षा नहीं करेंगे, बल्कि कर लेनेके बहाने प्रजाका ही घन छीनेंगे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12062)
- **Original**: उस समय जिस-जिसके पास बहुत-से हाथी, घोड़े और रथ होंगे कह-वह हो राजा होगा तथा जो-जो शक्तिहीन होगा बह-वह ही सेवक होगा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12063)
- **Original**: यैश्यगण कृषि-वाणिज्यादि अपने कर्मोंको छोड़कर शिल्पकारी आदिसे जीवन-निर्वाह करते हुए शूद्रवृत्तियोंमें ही लग जायैंगे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12064)
- **Original**: आश्रमादिके चिहसे रहित अधम शुद्रगण सैन्‍्यास लेकर भिक्षावृत्तिमें तत्पर रहेंगे और ल्त्रेगोंसे सम्मानित होकर पाषण्ड-वृत्तिका आश्रय लेंगे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12065)
- **Original**: प्रजाजन दुर्भिक्ष और करकी पीड़ासे अत्यन्त उपद्रवयुक्त और दु:खित होकर ऐसे देशॉमें चले जायैंगे जहाँ गेहूँ और जौकी अधिकता होगी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12066)
- **Original**: उस समय बेदमार्गका स््रेप, मनुष्योंमें पाषण्डकी प्रचुरता और अधर्मको वृद्धि हो जानेसे प्रजाकी आयु अल्प हो जायगी
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12067)
- **Original**: लोगोंके शास््रविरुद्ध थोर तपस्या करनेसे तथा राजाके दोषसे प्रजाओऑकी बाल्यावस्थामें मृत्यु होने लगोगी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12068)
- **Original**: 426 श्रीविष्णुपुराण 426 &9&9&9+ऋ+ऋ$9$&9 कअ्रोक्णपरण
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12069)
- **Original**: ॑-#॒ृ॒ै [1 भविता योषितां सूति: पद्चधघद्सप्तवार्षिकी । नवाष्टदशवर्षाणां मनुष्याणां तथा कल्छो
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12070)
- **Original**: 41 पलितोद्धवश्चन॒ भविता तथा द्वादशवार्षिक: । नातिजीवति वै कश्चित्कल्मै वर्षाणि विंशति:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12071)
- **Original**: 42 अल्पप्रज्ञा वृधालिड्रा दुष्टान्तः:करणा: कल्मे। यतस्ततो विनड्क्ष्यन्ति कालछेनाल्‍पेन मानवा:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12072)
- **Original**: 43 यदा यदा हि मैत्रेय हानिर्धर्मस्य लक्ष्यते । तदा तदा कलेव॑द्धिरनुमेवा विच्क्षणै:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12073)
- **Original**: डड यदा यदा हि पाषण्डवृद्धिमैत्रेय ल्क्ष्यते
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12074)
- **Original**: तदा तदा कलेव॑द्धिरनुमेया महात्मभि:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12075)
- **Original**: 45 यदा यदा सतां हानिर्वेदमार्गानुसारिणाम्‌ । तदा तदा कलेव॑द्धिरनुमेया विचक्षणैः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12076)
- **Original**: 46 प्रारम्भाश्नावसीदन्ति यदा धर्मभृतां नृणाम्‌। तदानुमेयं प्राधान्य॑ कलेमैत्रेय पण्डितै:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12077)
- **Original**: 47 यदा यदा न यज्ञानामीश्वर: पुरुषोत्तम: । इज्यते पुरुषैर्यज्ञेस्तदा ज्ञेय॑ कलेबलम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12078)
- **Original**: 48 न प्रीतिवेंदबादेषु पाषण्डेषु यदा रतिः। कलेव॑द्धिस्तदा प्राज्ञैरनुमेया विच्क्षणै:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12079)
- **Original**: 49 कलो जगत्पतिं विष्णुं सर्व्नष्टारमीश्वरम्‌ । नार्चयिष्यन्ति मैत्रेय पाषण्डोपहता जना:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12080)
- **Original**: 50 किंदेव: कि द्विजैवेंदे: कि झौचेनाम्बुजन्पना । इत्येव॑ विप्र वक्ष्यन्ति पाषण्डोपहता जना:
- **Translation**: 

---

