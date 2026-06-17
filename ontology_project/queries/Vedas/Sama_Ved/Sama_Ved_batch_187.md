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

### Verse 1 (Sama Ved 0.3721)
- **Original**: 1457. मा नो अज्ञाता वृजना-दुराध्यो3 माशिवासो5व क्रमु: । त्वया वय॑ प्रवतः शश्वतीरपो5ति शूर तरामसि
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3722)
- **Original**: हे इन्द्रदेव ! अज्ञात, पापी, दुष्ट, कुटिल, अमंगलकारी, हम पर आक्रमण न करें । हे श्रेष्ठ वीर ! आपके संरक्षण में हम विध्नों, अवरोधों के प्रवाहों से पार हों
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3723)
- **Original**: 1458. अद्याद्या श्वःश्व इन्द्र त्रास्व परे च न: । विश्वा च नो जरितृन्त्सत्पते अहा दिवा नकत॑ च रक्षिष:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3724)
- **Original**: हे इद्धदेव ! वर्तमान और भविष्य में आपका संरक्षण प्राप्त हो । हे सज्जनों के पालक इन्द्रदेव
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3725)
- **Original**: सर्वदा दिन और रात हमारे (याजकों के) आप रक्षक रहें
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3726)
- **Original**: 13.4 सामवेद-संहिता 1459. प्रभड्री शूरो मघवा तुवीमघः सम्मिश्लो वीर्याय कम्‌। उभा ते बाहू वृषणा शतक्रतो नि या बच्र॑ मिमिक्षतु:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3727)
- **Original**: हे सामर्थ्यवान्‌ इद्धदेब ! आप अपने पराक्रम से शत्रुओं की सामर्थ्य को चूर-चूर करने वाले हैं। आप सब में व्यापक और ऐश्वर्यवान्‌ हैं । हे शतकर्मा इन्द्रदेव ! आपकी दोनों भुजाएँ जो वज़ को धारण करती हैं, विशिष्ट सामर्थ्य से युक्त हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3728)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3729)
- **Original**: । कर्क
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3730)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3731)
- **Original**: 1460. जनीयन्तो न्वग्रकः पुत्रीयन्तः सुदानव: । सरस्वन्तं हवामहे
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3732)
- **Original**: स््री-पुत्र आदि की कामना करते हुए, यज्ञ-दानादि श्रेष्ठ कर्मों में अग्रणी हम याजकगण माँ सरस्वती का आवाहन करते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3733)
- **Original**: 14691. उत नः प्रिया प्रियासु सप्तस्वसा सुजुष्टा । सरस्वती स्तोम्या भूत्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3734)
- **Original**: परम प्रिय गायत्री आदि सातों छन्द और गंगा आदि सरिताएँ जिन देवी सरस्वती की बहिलनें हैं, वे देवी सरस्वती हमारे लिए स्तुत्य हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3735)
- **Original**: (462. तत्सवितुर्वरेण्यं भर्गों देवस्थ धीमहि। थियो यो न: प्रचोदयात्‌
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3736)
- **Original**: जो हमारी बुद्धियों को सन्‍्मार्ग की ओर प्रेरित करते हैं, उन सविता देवता के वरण करने योग्य तेज को हप धारण करते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3737)
- **Original**: 1463. सोमानां स्वरणं कृणुष्िि ब्रह्मणस्पते । कक्षीवन्तं य औशिज:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3738)
- **Original**: हे बह्मणस्पते ! (ज्ञानपते !) सोमाभिषव करने वाले हमें, उसी प्रकार यशस्वी और ज्ञान-सम्पन्न बनाएँ, जिस प्रकार (पूर्वकाल में) उशिज पुत्र कक्षीवान्‌ को बनाया था #4
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3739)
- **Original**: 1464. अग्न आयूंषि पवस आ सुवोर्जमिषं च न: । आरे बाधस्व दुच्छुनाम्‌
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3740)
- **Original**: हे अग्निदेव ! विभिन्‍न प्रकार के पोषक तत्त्वों के साथ आप हमें बल और दीर्घायुष्य प्रदान करें । दुष्टों को हमारे पास से दूर करें
- **Translation**: 

---

