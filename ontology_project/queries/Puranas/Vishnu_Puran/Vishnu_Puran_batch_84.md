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

### Verse 1 (Vishnu Puran 0.1661)
- **Original**: महतस्तपस: पारे सबर्णायां महामते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1662)
- **Original**: 5 सवर्णाधत्त सामुद्री दश प्राच्ीनबर्हिष: । सर्वे प्रचेतसो नाम थरनुर्वेदस्य पारगा:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1663)
- **Original**: 6 अपृथग्धर्मचरणास्तेउतप्यन्त महत्तप: .। दक्षवर्षसहस्नाणि समुद्रसलिलेशया:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1664)
- **Original**: 7 श्रीमैत्रेय उताच यदर्थ ते महात्मानस्तपस्तेपुर्महामुने । समुद्राम्भस्येतदाख्यातुमहसि ।। 8 श्रीपराशर उवाच पित्रा प्रचेतस: प्रोक्ताः प्रजार्थममितात्मना । प्रजापतिनियुक्तेन जहुमानपुरस्सरम
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1665)
- **Original**: 9 प्राचीनबर्टिस्वाच ब्रह्मणा देवदेबेन समादिष्टो5स्म्यह सुता: । प्रजा: संवर्द्धनीयास्ते मया चोक्ते तथेति तत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1666)
- **Original**: 10 तन्यम प्रीतये पुत्रा: प्रजाबृ्धिमतन्द्रिता: । कुरुथ्वे माननीया वः सम्यगाज्ञा प्रजापते:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1667)
- **Original**: 11 श्रीपराञ्र उवाच ततस्ते तत्पितु: श्रुत्वा बच्चन नृपनन्दनाः। तथेत्युकत्वा च॒ ते भूय: पप्रच्छुः पितरं मुने
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1668)
- **Original**: 12 अरचेतस ऊन: येन तात प्रजाबृद्धौ समर्था: कर्मणा वयम्‌ । भवेम तत्‌ समस्त नः कर्म व्याख्यातुमहसि
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1669)
- **Original**: 13 बिल पु* 3-- अ्रीपराशरजी बोले--हे मैत्रेय ! पृथुके अन्तर्द्धीन और बादी नामक दो धर्मज्ञ पुत्र हुए; उनमेंसे अन्तर्दधानसे उसकी पत्नी शिखण्डिनोने हविर्धानको उत्पन्न किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1670)
- **Original**: हबिर्धानसे अग्निकुलीना घिषणाने ग्राचीनवर्हि, शुक्र, गय, कृष्ण, वृज और अजिन--ये छः पुत्र उत्पन्न किये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1671)
- **Original**: है महाभाग ! हविर्धानसे उत्पन्न हुए भगवान्‌ प्राचीनवर्हि एक महान प्रजापति थे, जिन्होंने यज्ञके द्वारा अपनी प्रजाकी बहुत वद्धि की
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1672)
- **Original**: है मुने ! उनके समयमें [ यज्ञानूष्ठानकी अधिकताके कारण ] प्राचीनाग्र कुद्या समस्त पृथिवीमें फैले हुए थे, इसलिये वे महाबलली 'आरचीनर्वाह नामसे जिख्यात हुए
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1673)
- **Original**: है महासते ! उन महीपतिने महान्‌ तपस्याके अनन्तर समुद्रको पुत्रो सवर्णासे क्लाह किया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1674)
- **Original**: उस समुद्र- कन्या सवर्णके प्राचीनवर्हिसि दस पुत्र हुए। वे प्रचेता- नामक सभी पुत्र घनुर्विद्याके पारगामी थे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1675)
- **Original**: उन्होंने सपुद्रके जलूमें रहकर दस हजार वर्षतक समान घर्मका आचरण करते हृए घोर तपस्या की
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1676)
- **Original**: श्रीमैश्रेयजी खोल्ले--है महामुने ! उन महात्मा अचेताओंने जिस लिये समुद्रके जलगें तपस्या की थी सो आप कहिये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1677)
- **Original**: श्रीपराशरजी कहने लगे--हे मैत्रेय ! एक बार प्रजापतिकी प्रेरणासे प्रयेताओंके महात्मा पिता ब्राद्यनअर्शनि उनसे अति सम्मानपूर्यक सत्तानोत्पत्तिके लिये इस प्रकार कहा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1678)
- **Original**: अ्रालीनअर्हि जोले--हे पुत्रों ! देवाधिदेव ब्रह्माजीने मुझे आज्ञा दी है कि 'तुम अजाकी वृद्धि करो' और मैंने भी उनसे “बहुत अच्छा' कह दिया है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1679)
- **Original**: अतः हे पूत्रणण ! तुम भी मेरी प्रसन्नताके लिये सावधानतापूर्वक प्रजाकी वृद्धि करो, क्योंकि प्रजापतिकी आज्ञा तुमको भी सर्वथा माननीय है।। 191
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1680)
- **Original**: भ्रीपराशरजी लोले--हे मुने ! उन राजकुमारोनि पिताके ये वचन सुनकर उनसे 'जो आज्ञा' ऐसा कहकर फिर पूछा
- **Translation**: 

---

