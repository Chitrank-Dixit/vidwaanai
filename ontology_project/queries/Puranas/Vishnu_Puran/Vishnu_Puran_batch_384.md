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

### Verse 1 (Vishnu Puran 0.7661)
- **Original**: ततस्त्वस्पष्टमूर्त्ति घरं चैनमालोक्य सत्राजित्सूर्यमाह । 13
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7662)
- **Original**: यथैव व्योप्रि वह्विपिण्डोपमं त्वामहमपइय॑ तथैवाद्याग्तो गतमप्यत्र भगवता किश्ञित्न प्रसादीकृतं विशेष-
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7663)
- **Original**: मवतायैंकान्ते न्‍्यस्तम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7664)
- **Original**: ततस्तमाताग्रोज्ज्वलं: हुस्ववपुषमीषदापिड्रल- नयनमादित्यमग्राक्षीत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7665)
- **Original**: कृतप्रणिपात- स्तवादिक॑ च सत्राजितमाह भगवानादित्यस्सहस्र- दीधितिर्व॑रमस्मत्तोईडभिमते वृणीघ्रेति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7666)
- **Original**: सच तदेव मणिरत्रमयाचत
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7667)
- **Original**: स चापि तस्मैतदत््वा दीक्ितिपतिर्वियति स्वधिष्णय- मारुरोह
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7668)
- **Original**: सत्राजिदप्पपलमणिरत्रसनाथकण्ठतया सूर्य डूब तेजोभिरशेषदिगन्तराण्युद्धासयन्‌ द्वारकां विवेश
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7669)
- **Original**: द्वारकावासी जनस्तु तपमायात्त- मवेक्ष्य भगवन्तमादिपुरुष॑ पुरुषोत्तममबनि- भारावतरणायांशेन मानुषरूपधारिणं प्रणिपत्याह
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7670)
- **Original**: भगवन्‌ भवतन्त द्रष्ट्र नूनमयमादित्य आयातीत्युक्तो भगवानुवाच ।
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7671)
- **Original**: भगवाज्नायमादित्य: सत्राजिदयमादित्यदत्त- स्थमन्तकाख्यं॑ महामणिरत्र बिश्रदन्नोपयाति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7672)
- **Original**: तदेनं विश्रब्धा: पश्यतेत्युक्तास्ते तथैब ददूशु:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7673)
- **Original**: सच त॑ स्यपत्तकमणिमात्मनिवेशने चक्रे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7674)
- **Original**: उनमेंसे सुमिज्रके अनमित्र, अनमित्रके निम्न तथा निप्नसे प्रसेन और सत्राजितूका जन्म हुआ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7675)
- **Original**: 8---10
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7676)
- **Original**: उस सत्राजितके मित्र भगवान्‌ आदित्य हुए
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7677)
- **Original**: एक दिन समुद्र-तटपर बैठे हुए सत्राजितने सूर्यभगवान्‌की स्तुति की। उसके तन्‍्मय होकर स्तुति करनेसे भगवान्‌ भास्कर ठसके सम्मुख प्रकट हुए
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7678)
- **Original**: उस समय उनको अस्पष्ट मूर्ति घारण किये हुए देखकर सत्राजितने सूर्यसे कहा--
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7679)
- **Original**: “आकाहशमें अभिपिष्डके समान आपको जैसा मैंने देस्ता है वैसा ही सम्मुख आनेपर भी देख रहा हूँ । यहाँ आपकी प्रसादस्वरूप कुछ बिश्ञेषता मुझे नहीं दीखती ।'' सत्राजितके ऐसा कहनेपर भगवान्‌ सूर्यने अपने गलेसे स्वमन्ततक नामकी उत्तम महामणि उतारकर अलग रख दी
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7680)
- **Original**: तब सज्राजितने भगवान्‌ सूर्यको देखा--उनक। झरीर किजित्‌ ताम्रवर्ण, अति उज्ज्वल और लघु था तथा उनके नेत्र कुछ पिंगलवर्ण थे
- **Translation**: 

---

