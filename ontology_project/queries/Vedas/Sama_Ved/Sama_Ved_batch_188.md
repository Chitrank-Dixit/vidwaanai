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

### Verse 1 (Sama Ved 0.3741)
- **Original**: 1465. ता नः शकतं पार्थिवस्य महो रायो दिव्यस्य
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3742)
- **Original**: महि वां क्षत्र॑ देवेषु
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3743)
- **Original**: देवों में प्रशंसनीय, क्षात्र बल से सम्पन्न हे मित्र वरुण देव ! आप हमें धरती और आंकाश का समस्त वैभव प्रदान करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3744)
- **Original**: 1466. ऋजमृतेन सपन्तेषिरं दक्षमाशाते । अद्गुहा देवों वर्थेते
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3745)
- **Original**: सत्य से सत्य का पालन करने वाले अभीष्ट बल को प्राप्त करते हैं । द्रोह न करने वाले मित्र और वरुण देव अपनी सामर्थ्य से वृद्धि पाते हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3746)
- **Original**: 467, वृष्टिद्यावा रीत्यापेषस्पती दानुमत्या: । बृहन्तं गर्तमाशाते
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3747)
- **Original**: वर्षा के लिए जिनकी वंदना की जाती है, नियमानुसार सब कुछ प्राप्त करने वाले, दान की प्रवृत्ति वाले, अन्नों के अधिपति वे मित्र और वरुण देव श्रेष्ठ स्थान में प्रतिष्ठित हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3748)
- **Original**: उत्तराचिकि त्रयोदशो5ब्याय: 13.5 1468. युझन्ति ब्रध्नमरुषं चरन्तं परि तस्थुष: । रोचन्ते रोचना दिवि
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3749)
- **Original**: आदित्यरूप, अग्निरूप, चलायमान दीखने वाले, पर स्थिर सूर्यदेव की हम आराधना करते हैं । सूर्य के तुल्य इन्द्रदेव की प्रकाश-किरणें समस्त नक्षत्र-लोक में प्रकाश फैलाती हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3750)
- **Original**: [सूर्य के स्थिर रहने (पृथ्वी के घूमने) का सिद्धासत वैदिक ऋषियों के लिए अनजाना नहीं था, ] 1469. युझन्त्यस्य काम्या हरी विपक्षसा रथे। शोणा थृष्णू नृवाहसा
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3751)
- **Original**: इन्द्ररूपी आत्मा को इच्छित स्थान पर ले जाने के लिए, शरीररूपी रथ, कर्म व ज्ञानरूपी अश्वों के द्वारा ख्वींचा जाता है, मनरूपी सारथी द्वारा चलाया जाता है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3752)
- **Original**: स्‍ 1470. केतुं कृण्वन्नकेतवे पेशो मर्या अपेशसे । समुषद्धिरजायथा:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3753)
- **Original**: हे मनुष्यो ! अज्ञानी को ज्ञानयुक्त करते हुए, कुरूप को रूपवान्‌ करते हुए, उषाकाल में ये सूर्यदेव प्रकट होते हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3754)
- **Original**: डति चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3755)
- **Original**: कु के के
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3756)
- **Original**: पंचम खण्ड:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3757)
- **Original**: 1479. अयं सोम इन्द्र तुभ्यं सुन्‍्वे तुभ्य॑ पवते त्वमस्य पाहि। त्वं ह य॑ं चकृषे त्व॑ं ववृष इन्दुं मदाय युज्याय सोमम्‌
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3758)
- **Original**: हे इन्द्रदेव ! यह सोमरस आपके निमित्त निकालकर शोधित किया जाता है । इस पवित्र हुए सोम का आप पान करें । आप ही इसके उत्पादक हैं, इस दीप्तिमान्‌ सोम को आनन्द के लिए, योग के लिए आप ग्रहण करें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3759)
- **Original**: 1472. स ईं रथो न भुरिषाडयोजि मह: पुरूणि सातये वसूनि। आदी विश्वा नहुष्याणि जाता स्वर्षाता बन ऊर्ध्वा नवन्त
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3760)
- **Original**: वे महान्‌ इन्द्रदेव अधिक भार धारण किये हुए, रथ के समान, हमें अपार वैभव प्रदान करने के निमित्त, नियुक्त किये गये हैं और हमारे विरोधी शत्रुओं को संग्राम में विनष्ट करते हैं
- **Translation**: 

---

