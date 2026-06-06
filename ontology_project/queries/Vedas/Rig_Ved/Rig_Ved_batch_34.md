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

### Verse 1 (Rig Ved 0.661)
- **Original**: 295, यच्चिद्धि शश्वता तना देवन्देवं यजापहे
- **Translation**: 

---

### Verse 2 (Rig Ved 0.662)
- **Original**: त्वे डद्घूयते हवि:
- **Translation**: 

---

### Verse 3 (Rig Ved 0.663)
- **Original**: है अस्निदेव ! इन्र, वरुण आदि अन्य देवताओं के लिए प्रतिदिन विस्तृत आहुतियाँ अर्पित करने पर भी सभी हविष्यान्न आपको ही प्राप्त होते हैं
- **Translation**: 

---

### Verse 4 (Rig Ved 0.664)
- **Original**: 296. प्रियो नो अस्तु विश्पतिहोंता मन्द्रो वरेण्य:। प्रिया: स्वग्नयो वयम्‌
- **Translation**: 

---

### Verse 5 (Rig Ved 0.665)
- **Original**: यज्ञ सम्पन करने वाले प्रजापालक, आनन्दवर्धक, वरण करने योग्य हे अग्निदेव ! आप हमें प्रिय हों तथा श्रेष्ठ विधि से यज्ञाग्ति की रक्षा करते हुए हम सदैव आपके प्रिय रहें
- **Translation**: 

---

### Verse 6 (Rig Ved 0.666)
- **Original**: 297, स्वग्नयो हि वाय॑ देवासो दथिरे च न:। स्वग्नयो मनामहे
- **Translation**: 

---

### Verse 7 (Rig Ved 0.667)
- **Original**: उत्तम अग्नि से युक्त होकर देदीप्यमान ऋ्त्विजों ने हमारे लिए ऐश्वर्य को धारण किया है, बैसे ही हम उत्तम अग्नि से युक्त होकर इनका (ऋत्विज्‌ का ) स्मरण करते हैं
- **Translation**: 

---

### Verse 8 (Rig Ved 0.668)
- **Original**: ड्ड ऋछ्वेद संहिता घाग-1 298. अथा न उभयेषाममृत मर्त्यानाम्‌। मिथ: सन्तु प्रशस्तयः
- **Translation**: 

---

### Verse 9 (Rig Ved 0.669)
- **Original**: अपरत्व को धारण करने वाले हे अग्निदिव ! आपके और हम मरणशील मनुष्यों के बीच स्नेहयुक्त, प्रशंसनीय वाणियों का आदान - प्रदान होता रहे
- **Translation**: 

---

### Verse 10 (Rig Ved 0.670)
- **Original**: 299. विश्वेभिरग्ने अग्निभिरिमं यज्ञमिदं बच:
- **Translation**: 

---

### Verse 11 (Rig Ved 0.671)
- **Original**: चनो धा: सहसो यहो
- **Translation**: 

---

### Verse 12 (Rig Ved 0.672)
- **Original**: बल के पुत्र (अरणि मन्धन रूप शक्ति से उत्पन) है अग्निदेव ! आप (आहवनीयादि) अग्नियों के साथ यज्ञ में पधारें और स्तुतियों को सुनते हुए हमें अन्‍न (पोषण) प्रदान करें
- **Translation**: 

---

### Verse 13 (Rig Ved 0.673)
- **Original**: [ सूक्त - 27 ] [ऋषि - शुन: शेष आजीगर्ति (कृत्रिम देवरात वैश्वामित्र) । देवता - 1-12 अग्नि, 13 देवतागण । छन्द-1-12 गायत्री, 13 त्रिप्टप्‌। ] 300, अश्व॑ न त्वा वारवन्तं वन्दध्या अग्नि नमोभि:। सप्राजन्तमध्वराणाम्‌
- **Translation**: 

---

### Verse 14 (Rig Ved 0.674)
- **Original**: तप्रोनाशक, यज्ञों के सप्राट्‌ स्वरूप हे अग्निदेव ! हम स्तुतियों के द्वारा आपकी बन्दना करते हैं। जिस प्रकार अश्व अपनी पूँछ के बालों से मक्खी - मच्छरों को दूर भगाता है, उसी प्रकार आप भी अपनी ज्वालाओं से हमारे विरोधियों को दूर भगायें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.675)
- **Original**: 301. स घा नः सूनुः शवसा पृथुप्रगामा सुशेव:। मीद्वाँ अस्माक॑ बभूयात्‌
- **Translation**: 

---

### Verse 16 (Rig Ved 0.676)
- **Original**: हम इन अग्निदेव की उत्तम विधि से उपासना करते हैं । वे बल से उत्पन्न, शीघ्र गतिशील अग्निदेव हमें अभीष्ट सुखों को प्रदान करें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.677)
- **Original**: 302, स नो दूराच्चासाच्च नि मर्त्यादघायो:। पाहि सदमिद्विश्नायु:
- **Translation**: 

---

### Verse 18 (Rig Ved 0.678)
- **Original**: है अग्निदेव ! सब मनुष्यों के हितचितक आप दूर से और निकट से, अनिष्ट चिन्तकों से सदैव हमारी रक्षा करें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.679)
- **Original**: 303. इममू घु त्वमस्मार्क सनि गायत्र॑ नव्यांसम्‌। अस्ने देवेषु प्र वोच:
- **Translation**: 

---

### Verse 20 (Rig Ved 0.680)
- **Original**: है अग्निदेव ! आप हमारे गायत्री परक प्राण-पोषक स्तोत्रों एवं नवीन अन्न (हव्य) को देवों तक (देव वृत्तियों के पोषण हेतु) पहुँचायें
- **Translation**: 

---

