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

### Verse 1 (Rig Ved 0.1101)
- **Original**: नू चित्स दभ्यते जन:
- **Translation**: 

---

### Verse 2 (Rig Ved 0.1102)
- **Original**: जिस याजक को, ज्ञान सम्पल वरुण, मित्र और अर्यमा आदि देवों का संरक्षण प्राप्त है, उसे कोई भी नहीं दबा सकता
- **Translation**: 

---

### Verse 3 (Rig Ved 0.1103)
- **Original**: मं0 है सू0 डर 59 491. य॑ बाहुतेव पिप्रति पान्ति मर्त्य रिघ:। अरिष्ट: सर्व एधते
- **Translation**: 

---

### Verse 4 (Rig Ved 0.1104)
- **Original**: अपने बाहुओं से विविध धनों को देते हुए, वरुणादि देवगण जिस मनुष्य को रक्षा करते हैं, शत्रुओं से अहिंसित होता हुआ वह वृद्धि पाता है
- **Translation**: 

---

### Verse 5 (Rig Ved 0.1105)
- **Original**: [ज्ख देवगण साधक को सत्पात्र पासकर उसे दैवी साप्पदा प्रदान करते हैं, तो अहितकर प्रवृत्तियों से वह अग्रभावित रहकर सतत प्रगतिशील रहता है ।] 492. वि दुर्गा वि द्विष: पुरो घ्नन्ति राजान एषाम्‌। नयन्ति दुरिता तिर;
- **Translation**: 

---

### Verse 6 (Rig Ved 0.1106)
- **Original**: राजा के सदृश वरुणादि देवगण, शत्रुओं के नगरों और किलों को विशेष रूप से नष्ट करते है । वे याज़कों को दुःख के मूलभूत कारणों (पापों ) से दूर ले जाते हैं
- **Translation**: 

---

### Verse 7 (Rig Ved 0.1107)
- **Original**: 493. सुग: पन्‍्था अनृक्षर आदित्यास ऋजतं यते। नात्रावखादो अस्ति व:
- **Translation**: 

---

### Verse 8 (Rig Ved 0.1108)
- **Original**: है आदित्यो ! आप के यज्ञ में आने के मार्ग अतिसुगम और कण्टकहीन हैं। इस यज्ञ में आपके लिए श्रेष्ठ हविष्यानत समर्पित है
- **Translation**: 

---

### Verse 9 (Rig Ved 0.1109)
- **Original**: 494. य॑ यज्ञ नयथा नर आदित्या ऋजुना पथा। प्र व: स्‌ धीतये नशत्‌
- **Translation**: 

---

### Verse 10 (Rig Ved 0.1110)
- **Original**: हे आदित्यो ! जिस यज्ञ को आप सरल मार्ग से सम्पादित करते हैं, वह यज्ञ आपके ध्यान में दिशेष रूप से रहता है । वह भला कैसे विस्पृत हो सकता है ?
- **Translation**: 

---

### Verse 11 (Rig Ved 0.1111)
- **Original**: 495, स रल॑ मरत्यों वसु विश्व तोकमुत त्मना। अच्छा गच्छत्यस्तृत:
- **Translation**: 

---

### Verse 12 (Rig Ved 0.1112)
- **Original**: है आदित्यो ! आपका याजक किसी से पराजित नहीं होता । वह धनादि रल और सन्तानों को प्राप्त करता हुआ प्रगति करता है
- **Translation**: 

---

### Verse 13 (Rig Ved 0.1113)
- **Original**: 496, कथा राधाम सखाय: स्तोमं मित्रस्थार्यम्ण: । महि प्सरो वरुणस्य
- **Translation**: 

---

### Verse 14 (Rig Ved 0.1114)
- **Original**: हे मित्रो ! पित्र, अर्यमा और वरुण देवों के महान्‌ ऐश्यर्य साधनों का किस प्रकार वर्णन करें ? अर्थात्‌ इनकी महिमा अपार है
- **Translation**: 

---

### Verse 15 (Rig Ved 0.1115)
- **Original**: 497 मा वो घ्नन्त॑ मा शपन्तं प्रति बोचे देवयन्तम्‌। सुप्नैरिद्र आ विवासे
- **Translation**: 

---

### Verse 16 (Rig Ved 0.1116)
- **Original**: हे देवो ! देवत्व प्राप्ति की कामना बाले साधकों को कोई कटुववनों से और क्रोधयुक्त बचनों से प्रताड़ित न करने पाये । हम स्तुति बचनों द्रारा आपको प्रसन्न करते हैं
- **Translation**: 

---

### Verse 17 (Rig Ved 0.1117)
- **Original**: 498. चतुरक्षिदददमानाद्विभीयादा निधातो:। न दुरुक्ताय स्पृहयेत्‌
- **Translation**: 

---

### Verse 18 (Rig Ved 0.1118)
- **Original**: जैसे जुआ खेलने में चार पाँसे गिरने तक (हार-जीत का) भय रहता है, उसी प्रकार बुरे वचन कहने से भी डरना चाहिये । उससे स्नेह नहीं करना चाहिए
- **Translation**: 

---

### Verse 19 (Rig Ved 0.1119)
- **Original**: [सूक्त - 42 ] [ऋषि- कण्वघौर । देवता- पूषा । छत्द- गायत्री । ] 499. सं पृषन्नध्वनस्तिर व्यंड्ो विमुचो नपात्‌। सक्ष्वा देव प्र णस्पुर:
- **Translation**: 

---

### Verse 20 (Rig Ved 0.1120)
- **Original**: हे पृषादेव ! हम पर सुखों को न्योछावर करें । पाप मार्गों से हमें पार लगाएँ । हे देव ! हमे आगे यढ़ाएँ
- **Translation**: 

---

