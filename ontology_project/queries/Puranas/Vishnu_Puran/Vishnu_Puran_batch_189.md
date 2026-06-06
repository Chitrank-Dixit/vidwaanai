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

### Verse 1 (Vishnu Puran 0.3761)
- **Original**: इसर्ये सम्योपासनकर्मका उल्हेघन कभी न काना चाहिये। जो पुरुष सम्ध्योपासन नहीं कस्ता वह भगवान्‌ सूर्यका घात करता है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3762)
- **Original**: तदनच्तर [उन राक्षसोंका वध करनेके पश्चात्‌) भगवान्‌ सूर्य संसारके पारनमें प्रवत्त हो यालखिल्यादि ब्राह्मणॉसे सुरक्षित होकर गमन करते है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3763)
- **Original**: पद्रह निमेषकी एक काष्ठा होती है और तीस काप्ठाकी । एक कत्त्र गिनी जाती है। तीस कल्त्रऑंका एक मुहूर्त होता
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3764)
- **Original**: है और तोस सुहृर्तोकि सम्पूर्ण रात्रि-दिन होते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3765)
- **Original**: दिनोंका हास अथवा वृद्धि क्रमशः प्रातः:काल, मध्याह्वकाल आदि दिवसांदॉकि हास-वूद्धिक कारण होते हैं; किन्तु दिनोंके घटते-नढ़ते रतनेपर भी सन्ध्या सर्वदा समान भानरो एक मुहर्तकी ही होती है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3766)
- **Original**: उदयसे लेकर सूर्यकी तीन मुहूर्तकी गतिके कालको 'प्रात:काल' कहते हैं, यह सम्पूर्ण दिनका पाँचयाँ भाग होता है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3767)
- **Original**: इस प्रातःकाल्के अनन्तर तीन मुहूर्तका समय 'सद्भगब' कहलाता हैं तथा सक्नवकाल्के पश्चात्‌ तीन मुहूर्तका 'मध्याह्' होता है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3768)
- **Original**: मध्याह्कालसे पीछेका समय “अपगड़ कहत्खता है इस काल-भागको भी बुघजन तीन मुहूर्तका ही बताते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3769)
- **Original**: अपराह्के बीतनेपर सायाह' आता है। इस प्रकार [सम्पूर्ण दिनमें] पन्द्रह मुहूर्त और [प्रत्येक दिवसोंझमें] तीन मुहूर्त होते हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3770)
- **Original**: वैदुबत दिवस पन्द्रह मुहूर्तका होता है, किन्तु उत्तरायण और दक्षिणायनमें क्रमशः उसके बद्धि और हास होने लगते हैं । इस प्रकार उत्तरायणमें दिन रात्रिका प्रास करने लगता है और दक्षिणायनमें यात्रि दिनका प्रास करती रहती है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3771)
- **Original**: शरद और वसत्तऋतुके मध्यमें सूर्वके तुल्म अथवा मेषराशिमें झानेपर 'लिषु्ा होता है। उस समय दिन और रात्रि समान होते हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3772)
- **Original**: सूर्यके कर्कराशिमें उपस्थित होनेपर दक्षिणायन कहा जाता है और उसके मकरराद्विपर आनेसे उत्तरायण कहल्मता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3773)
- **Original**: है अह्मन्‌ ! मैंने जो तीस मुहूर्तके एक रात्रि-दिन कहे हैं ऐसे पन्द्रह रात्रि-दिवसका एक 'पक्ष' कहा जाता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3774)
- **Original**: दो पक्षका एक मास होता है, दो सौरमासकी फक ऋतु और तीन ऋतुव्त एक अयन होता है तथा दो अयन ही [ मिल्म्कर ] एक वर्ष कहे जाते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3775)
- **Original**: श3 4 आ श्रीषिष्यापराण (आ8 84 संबत्सरादय: पश्च चतुर्मासविकल्पिता: । (आशच् 8 (सौर, सावन, चान्द्र तथा नाक्षत्र-इन] चार प्रकारके निश्चय: सर्वकालस्य युगमित्यभिधीयते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3776)
- **Original**: मासेके अनुसार विविधरूपसे कल्पित संबत्सरादि पाँच संबत्सरस्तु प्रथमो द्वितीय: परिवत्सरः । इद्वत्सरस्तृतीयस्तु चत्ुर्धश्चानुवत्सरः । वत्सरः पश्चमश्नात्र कालो5य॑ युगसंज्ञित:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3777)
- **Original**: 72 यः श्रेतस्योत्तरः हैल: श्ूड़बानिति विश्रुतः । श्रीणि तस्य तु श्रूज्ञाणि यैरयं श्ूड्रवान्स्पृत:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3778)
- **Original**: 73 दक्षिणं चोत्तरं चैब मध्य बैधुबत तथा। शरइसन्तयोम॑ध्ये तद्धानुः प्रतिपद्यते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3779)
- **Original**: मेषादौ च तुलादौ च मैत्रेय विषुवत्स्थित:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3780)
- **Original**: 74 तदा तुल्यमहोरात्र करोति तिमिरापह: । दह्मपश्चमुहुत॑ वे तदेतदुभय॑ स्मृतम्‌
- **Translation**: 

---

