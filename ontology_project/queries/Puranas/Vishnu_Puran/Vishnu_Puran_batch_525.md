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

### Verse 1 (Vishnu Puran 0.10481)
- **Original**: पापी नन्‍्दको स्मेहेकी श्रुल्लल्म्में बाँधकर पकड़ ल्तरे तथा वृद्ध पुरुषोंके अयोग्य दण्ड देकर वसुदेवकों भी मार डालो
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10482)
- **Original**: मेरे सामने कृष्णके साथ ये जितने गोप्नालक उछल रहे हैं इन सबको भी मार डालो तथा इनकी गौएँ और जो कुछ अन्य धन हो वह सब छीन लो”
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10483)
- **Original**: जिस समय कंस इस प्रकार आज्ञा दे रहा था उसी समय श्रीमधुसूदन हैँसते-हैँसते उछऊकर मझपर चढ़ गये और झीघ्रतासे उसे पकड़ रित्र्या
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10484)
- **Original**: भगवान्‌ कृष्णने उसके केशोंको खींचकर डसे पृथिवीपर पटक दिया तथा उसके ऊपर आप भी कूद पड़े, इस समय उसका मुकुट सिरले खिसककर अलग जा पड़ा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10485)
- **Original**: सम्पूर्ण जगत्‌के आधार भगवान्‌ कृष्णके ऊपर गिरते ही उपग्रसेनात्मण राजा कंसने अपने प्राण छोड़ दिये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10486)
- **Original**: तब महाबली कृष्णचन्द्रने मृतक कंसके केश फ्कड़कर उसके देहको रंगभूमिमें घसौटा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10487)
- **Original**: केसका देह बहुत आरी था, इसलिये उसे घसोटनेसे जल्के महान्‌ वेगसे हुई दरास्के समान पृथित्रीपर परिघा बन गयी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10488)
- **Original**: श्रोकृष्णचन्द्रद्ाय कंसके फ्कड़ लिये जानेपर ठसके भाई सुमालीने कऋोधपूर्वक आक्रमण किया। उसे बलरामजोने ल्त्रैलासे हो मार डाला
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10489)
- **Original**: इस प्रकार मथुरापति केसको कष्णचन्द्रद्धारा अवज्ञापूर्वक मय हुआ देखकर रैगभूमिमें उपस्थित सम्पूर्ण जनता हाहाकार करने लगी
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10490)
- **Original**: उसी समय महाबाहु कृष्णचन्द्र नल्देकजी- सहित बसुदेव और देबकीके चरण पकड़ लिये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10491)
- **Original**: तब वसुदेव और देखकीक्म पूर्वजन्मपें कहे हुए भगवदजाक्थोंका स्मरण हो आया और उन्होंने श्रीजनार्दनकों पृथिवोपरसे डा लिया तथा उनके सामने प्रणतभावसे खड़े हो गये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10492)
- **Original**: श्रीयसुदेवजी बोले--है प्रभो ! अब आप हमपर प्रसन्न होइये। हे केशव ! आपने आर्त्त देवगणोंको जो बर दिया था वह हम दोनॉपर अनुग्रह करके पूर्ण कर दिया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10493)
- **Original**: भगवन्‌ ! आपने जो मेरी आराधनासे दुष्टजनोंके नाशके र्ल्ये मेरे घरमें जन्म लिया, उससे हमारे कुल्को पवित्र कर दिया है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10494)
- **Original**: आप सर्वभूतमय है और समस्त भूतोंके भीतर स्थित हैं। हे समस्तात्पन्‌ ! भूत और भविष्यत्‌ आपहीसे प्रवृत्त होते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10495)
- **Original**: आर 20 ] पश्कम अंश आ 20
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10496)
- **Original**: आज आ पश्रमअंश >> >> >> कें69 है अचिन्य ! हे सर्वदेनपय ! हे अच्युत ! समस्त असर सयसवेब पुर । यष्टा च यज्वनां
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10497)
- **Original**: यज्ञोसे आपह्कीका यजन किया जाता है तथा हे परमेधर ! समुद्धवस्समस्तस्य जगतत्त्व॑जनार्दन
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10498)
- **Original**: 98 सापहरय॑ मम मनो यदेतस्‍््वयि जायते। देवक्याश्रात्मजप्रीत्या तदत्यन्तविडम्बना
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10499)
- **Original**: 99 त्वं कर्ता सर्वभूतानामनादिनिधनो भवान्‌ । त्वां मनुष्यस्थ कस्पैषा जिड्डा पुत्रेति वक्ष्यति
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10500)
- **Original**: 100 जगदेतज्जगन्नाथ सम्भूतमस्िलं यत: । कया युक्‍त्या विना मायां सो उस्मत्त: सम्धतिष्यति
- **Translation**: 

---

