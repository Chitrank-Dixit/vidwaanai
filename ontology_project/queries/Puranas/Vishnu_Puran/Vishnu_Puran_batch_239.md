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

### Verse 1 (Vishnu Puran 0.4761)
- **Original**: है मैत्रेय ! स्थितिकारक भगवान्‌ विष्णु चारों युगॉमें जिस प्रकार व्यवस्था करते हैं, स्रो सुनो--
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4762)
- **Original**: समस्त प्राणियोंके कल्याणमें तत्पर वे सर्वभूतात्मा सत्ययुगर्मे कपिल आदिरूप धारणकर परम ज्ञानका उपदेश करते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4763)
- **Original**: त्रेताबुगमें वे सर्वसमर्थ प्रभु चक्रवर्ती भूपाल झोकर दुष्टोंका दमन करके त्रिलोकीकी एस्षा करते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4764)
- **Original**: [ अ»3 करोति बहूलं भूयो वेदव्यासस्वरूपधृक्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4765)
- **Original**: 58 वेदांस्तु द्वापरे व्यस्थ कलेरन्ते पुनहीरिः । कल्किस्वरूपी दुर्वृत्तान्पा्गे स्थापयति प्रभु:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4766)
- **Original**: 59 एबमेतजगत्सर्व॑ शश्चत्पाति करोति च। हन्ति चान्तेष्नन्तात्मा नास््यस्मादव्यतिरेकि यत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4767)
- **Original**: 60 भूत भव्य भविष्यं च॒ सर्वभूतात्महात्मन: । तदत्नान्यत्र वा विप्र सद्भाव: कथितस्तव
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4768)
- **Original**: 61 मन्वन्तराण्यशेषाणि कथितानि म्या तव । लदनत्ततर द्वापस्युगमें ले वेदव्यासरूप धारणकर एक येदके चार विभाग करते हैं और सैकड़ों शाख्राओंमें बाॉँटकर उसका बहुत विस्तार बर देते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4769)
- **Original**: इस प्रकार द्वापरमें येदोंका विस्तार कर करियुगके अन्तरमें भगवान्‌ कल्किरूप हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4770)
- **Original**: इसी प्रकार, अनन्तात्पा प्रभु निरन्तर इस सम्पूर्ण जगत्‌के उत्पत्ति, पालन और नाश करते रहते हैं। इस संसारमें ऐसी कोई वस्तु नहीं है जो उससे भिन्न हो
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4771)
- **Original**: है दिप्र ! झाजोप् औ# परल्प्रेक्में भूत, भक्िष्यत्‌ और वर्तमान जितने भी पदार्थ हैं वे सब महात्मा भगवान्‌ विष्णुसे ही उत्पन्न हुए डै--यह सब मैं तुमसे कह चुका हूँ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4772)
- **Original**: मैंने तुमसे सम्पूर्ण मन्चन्तरों और मन्वन्तराधिकारियोंका मन्वन्तराधिपांशैल किमन्यत्कथयामि ते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4773)
- **Original**: बर्णन कर दिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4774)
- **Original**: कहो, अब और क्या सुनाऊँ ?
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4775)
- **Original**: 62 नलततन औ “-+ इति श्रीविष्णुपुराणे ततीयें5शे द्वितीयो5घ्याय:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4776)
- **Original**: अऋरणनन जौ अनसणणक, तीसरा अध्याय खतुर्युगानुसार भिन्न-भिन्न व्यासोके नाम तथा ब्रह्म-ज्ञानके माहात्यका वर्णन श्रोमैत्रेय उवाच ज्ञातमेतन्मया त्कत्तो यथा सर्वमिदं जगत्‌। विष्णुर्विष्णो विष्णुतश्न न परं विद्यते तत:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4777)
- **Original**: 9 एतत्तु श्रोतुमिच्छामि व्यस्ता वेदा महात्मना । वेदव्यासस्वरूपेण तथा तेन युगे युगे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4778)
- **Original**: 2 यस्मिन्यस्मिन्युगे व्यासो यो व आसोन्महामुने । ते तपाचक्ष्व भगवउ्छाखाभेदांश्व मे वद
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4779)
- **Original**: 3 औपराशर उवाच वेदह्मस्थ॒मैत्रेय. शाखाभेदास्सहस्नश: । न दाक्तो विस्तराह्नक्ुुं सल्लेपेण श्रृणुष्च तम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4780)
- **Original**: 4 द्वापरे द्वापरे किष्णुव्यासरूपी महामुने । बेदमेक॑ सुबहुधा कुरुते जगतों हितः:
- **Translation**: 

---

