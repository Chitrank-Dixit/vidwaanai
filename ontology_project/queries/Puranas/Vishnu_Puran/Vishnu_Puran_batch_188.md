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

### Verse 1 (Vishnu Puran 0.3741)
- **Original**: अभिहोन्नमें जो 'सूय्यों ज्योतति:' इत्यादि मन्जसे प्रथम आहूति दी जाती है उससे सहस्तांश[ दिननाथ देदीप्यमान हो जाते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3742)
- **Original**: 3>कार विश्व, तेजस और प्राज्ञरूप तीन धामोंसे युक्त भगवान्‌ विष्णु है तथा सम्पूर्ण वाणियों (लेदों) क्य अधिपति है, उसके उच्चारणमात्नसे ही वे राक्षसगण नष्ट हो जाते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3743)
- **Original**: सूर्य विष्णुभगवान्‌का अति श्रेष्ठ अंज्ञ और विकासरहित अन्त- ज्यौतिःस्वरूप है। 3#कार उसका जाचक है और बह उसे उन राक्षसॉके यधर्में अत्यन्त प्रेस्ति करनेवाला है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3744)
- **Original**: +% “ह्यूष्ट' और 'उष्ा' दिन और राज़िके लैदिक नाम हैं; यधा--'रात्रियाँ ठपा अहत्युष्रिः ।'
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3745)
- **Original**: आः&] द्वितीय अं 133 तेन सम्प्रेरितं ज्योतिरोद्धारेणाथ दीपिमत्‌। दहत्यशेंषरक्षांसि मन्देहाख्यान्यघानि वै
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3746)
- **Original**: 56 तस्मान्नोल्लड्ून कार्य सन्ध्योपासनकर्मण: । स हन्ति सूर्य सन्ध्याया नोपास्ति कुरुते तु व:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3747)
- **Original**: 57 ततः प्रयाति भगवान्ब्राह्वणैरभिरक्षितः । बालखिल्यादिभिश्वैव जगत: पालनोद्यतः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3748)
- **Original**: 58 काष्टा निमेषा दश पशञ्ञ चैव त्रिंशच्च काष्टा गणयेत्कलां चने । त्रिंझत्कलश्नेव. भरवेत्मुहूर्त- स्तैस्निशाता रात्यहनी समेते
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3749)
- **Original**: 59 डासवृद्धी त्वहर्भागैर्दिवसानां यथाक्रमम्‌। सन्ध्या पुहूर्तमात्रा वै ह्वासवृद्धणे: समा स्पृता
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3750)
- **Original**: 60 रेखाप्रभृत्यथादित्ये तरिमुहूर्तनते . रबौ । प्रात: स्मृतस्ततः कालो भागश्नाह्न: स पश्चम:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3751)
- **Original**: 61 तस्माद्मातस्तनात्कालात्रिपुहूर्तसतु. सद्गवः । मध्याहरि्रमुहूर्तस्तु तस्मात्कालात्तु सड्रवात्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3752)
- **Original**: 62 तस्मान्माध्याह्लिकात्कालादपराह्न डति स्मृतः । त्रय एब्र मुहूर्तास्तु कालभागः स्मृतो बुछैः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3753)
- **Original**: 63 अपराह्ने व्यतीते तु काल: सायाह्न एव च । दह्पश्नमुहूर्ता वै मुहूर्तात्नाय एवं च।
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3754)
- **Original**: 64 दह्पञ्ञमुहूत बे अहवैंषुबत॑ स्मृतम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3755)
- **Original**: 65 वर्दते हसते चैवाप्ययने दक्षिणोत्तरे । अहस्तु असते रात्रि रात्रिग्रंसति वासरम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3756)
- **Original**: 66 शरद्वसन्तयोर्मध्ये विषुबं॑ तु विभाव्यते । तुलामेषगते भानौ समरात्रिदिनं तु तत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3757)
- **Original**: 67 कर्कटावस्थिते भानौं दक्षिणायनमुच्यते । उत्तरायणप्रप्युक्त मकरस्थे._ दिवाकरे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3758)
- **Original**: 68 ब्रिशन्पुहृत॑ कथितमहोरात्र तु॒यन्मया । तानि पञ्चदश ब्रह्मन्‌ पक्ष इत्यभिधीयते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3759)
- **Original**: 69 मास: पक्षद्दयेनोक्तो है मासौ चार्कजावृतु: । ऋतुतन्नय॑ चाप्ययरन द्वेउ्यने वर्षसंज्ञिते
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3760)
- **Original**: 70 उस <*कारकी प्रेरणासे अति प्रदीम्त होकर वह ज्योति मन्देहा नामक सम्पूर्ण पापी यक्षसोंकों दग्ध कर देती है
- **Translation**: 

---

