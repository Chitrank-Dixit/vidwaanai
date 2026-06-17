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

### Verse 1 (Vishnu Puran 0.3681)
- **Original**: अर & ] एवं पुष्करमध्येन यदा याति दिवाकरः । ब्रिशद्धागन्तु मेदिन्यास्तदा मौहूर्तिकी गति:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3682)
- **Original**: 26 कुलालचक्रपर्यन्तोी भ्रमन्नेच दिवाकरः । करोत्यहस्तथा रात्रि विधुश्नन्मेदिनों ह्विज
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3683)
- **Original**: 27 अयनस्पोत्तरस्थादों मकरं याति भास्कर: । तत: कुम्भ चर मीन च्ञ राहो राहयन्तर द्विज
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3684)
- **Original**: 28 त्रि्नेतेघ्ठथ भुक्तेषु ततो बैबुबर्ती गतिम्‌। प्रयाति सविता कुर्वन्नहोरात्रं ततः समम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3685)
- **Original**: 29 ततो रात्रि: क्षयं याति वर्द्धतेउनुदिनं दिनम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3686)
- **Original**: 30 ततश्न पिथुनस्थान्ते परां काष्ठामुपागत: । राशिं कर्कटकं प्राप्य कुरुते दक्षिणायनम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3687)
- **Original**: 39 कुलालचक्रपर्यन्तों यथा झीघ्र प्रवर्त्तते । दक्षिणप्रक्रमे सूर्यस्तथा शीघ्र प्रवर्तते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3688)
- **Original**: 32 अतिवेगितया काले यायुवेगबलाचरन्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3689)
- **Original**: तस्मात्मकृष्टां भूमि तु कालेनाल्‍पेन गच्छति
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3690)
- **Original**: 33 सूर्यो द्वादशभि: शैघ्रयान्मुहूतैंदक्षिणाबने । त्रयोदशार्द्धपृक्षाणामह्ला तु चरति द्विज। मुहूर्तैस्तावदृक्षाण.. नक्तमष्टादशैश्षरन्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3691)
- **Original**: 34 कुलालचक्रमध्यस्थो यथा मनन्‍्द प्रसर्पति । तथोदगयने सूर्य: सर्पते मन्दविक्रम:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3692)
- **Original**: 35 तस्माद्दीेण कालेन भूमिमल्पां तु गच्छति । अष्टादशमुहूते यदुत्तरायणपश्चिमम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3693)
- **Original**: 36 अहर्भवति तन्चापि चरते मन्दविक्रम:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3694)
- **Original**: 37 त्रयोदशार्द्ममह्ला तु ऋक्षाणां चरते रखि: । राज्ौ द्वादशभिश्षरन्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3695)
- **Original**: 38 अतो मन्दतर नाभ्यां चक्र भ्रमति वै यथा । मृत्पिण्ड डुब मध्यस्थों धरुवो भ्रमति वै तथा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3696)
- **Original**: 39 द्वितीय अंश 131 है, किन्तु सूर्य-अस्त हो जानेपर उसमें दिनका प्रवेश हो जाता है; इसलिये दिनके प्रवेशके कारण ही रात्रिके समय खह शुक्नतर्ण हो जाता है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3697)
- **Original**: इस प्रकार जब सूर्य पुष्करद्वीपके मध्यमें पहुँचकर पृथ्वोका तीसवाँ भाग पार कर लेता है तो उसकी बह गति एक मुहूर्तकों होती है । [ अर्थात्‌ उतने भागके अतिक्रमण करनलेमें उसे जितना समय लगता है वही मुहूर्त कहलाता है ]
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3698)
- **Original**: हे द्विज ! कुलाल-चक्र (कुम्हारके चाक) के सिरेपर घूमते हुए जोक्के समान भ्रमण करता हुआ यह सूर्य पृथिवीके तीसों भागोंक़ा अतिक्रमण करनेपर एक दिन-रात्रि करता है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3699)
- **Original**: हे द्विज! उत्तरायणके आरम्भमें सूर्य सबसे पहले मकरराशिमें जाता है, उसके पश्चात्‌ वह कुम्म और मीन राज्चियोंमें एक राशिसे दूसरी ग़शिमें जाता है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3700)
- **Original**: इन तीनों गरशियोक्त्रे भोग चुकनेपर सूर्य रात्रि और दिनको समान करता हुआ बैषुबती गतिका अवलम्बन करता है, [ अर्धात्‌ वह भूमध्य-रेखाके बीचमें ही चलता है ]
- **Translation**: 

---

