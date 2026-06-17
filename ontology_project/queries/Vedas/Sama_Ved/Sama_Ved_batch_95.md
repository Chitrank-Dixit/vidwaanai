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

### Verse 1 (Sama Ved 0.1881)
- **Original**: [सप्त ऋत्विजू, यज़स्थल पर विध्यपान सप्त संसद ( होतू, पोतृ, नेष्ट, आस्नीच, प्रशास्तु, अध्वर्य और बहन) काबोच कराते हैं।] 724.बत्रिकद्दुकेषु चेतनं देवासो यज्ञमत्नत
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1882)
- **Original**: तमिद्दर्धन्तु नो गिर:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1883)
- **Original**: श्रेरणादायी, उत्साह बढ़ाने वाले, तीन चरणों में सम्पन्न होनेवाले, यज्ञ का विस्तार देवगण करते हैं, उिधज* साधकगण प्रशंसा करते हैं
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1884)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1885)
- **Original**: के केके
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1886)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1887)
- **Original**: 725.अवं त इन्द्र सोमो निपूतो अधि बर्हिषि
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1888)
- **Original**: एहीमस्य द्रवा पिब
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1889)
- **Original**: हे इन्द्रदेव ! आपके लिए शोधित सोमरस तैयार है । इसके पान के लिए आप शीघ्र ही यज्ञवेदी पर पधारें
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1890)
- **Original**: 726.शाचिगो शाचिपूजनायं॑ रणाय ते सुतः। आखण्डल प्र हूयसे
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1891)
- **Original**: शत्रुनाशक, शक्तिवान्‌, पूज्य, सामर्थ्यवान्‌, तेजस्वी हे इन्रदेव ! आपके आनन्द के लिए ही सोमरस तैयार किया गया है । इसलिए हम आपका आवाहन करते हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1892)
- **Original**: 727.यस्ते श्रृड्रवृषो णपात्प्रणपात्कुण्डपाय्य: । न्यस्मिन्‌ दध्न आ मन:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1893)
- **Original**: हे प्रखर तेजस्वी इद्धदेव ! सरलता से पान करने योग्य सोम के लिए इस कुण्डपायी सोमयज्ञ की ओर आप उन्मुख हों
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1894)
- **Original**: 728,आ तू न इन्द्र क्षुमन्तं चित्र ग्राभं सं गृभाय । महाहस्ती दक्षिणेन
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1895)
- **Original**: महान्‌ भुजाओं वाले हे इन्द्रदेव ! आप हमें न्यायोपार्जित ऐश्वर्य दाहिने (सम्मानपूर्वक) हाथ से प्रदान करें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1896)
- **Original**: 729.विद्या हि त्वा तुविकूर्मि तुविदेष्णं तुवीमघम्‌। तुविमात्रमवोभि:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1897)
- **Original**: हे इन्द्रदेव ! हम आपको ऐश्वर्यशाली, बहुमुखी पराक्रम करने वाले, व्यापक आकार युक्‍त संरक्षणकर्त्ता के रूप में जानते हैं
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1898)
- **Original**: 730,न हि त्वा शूर देवा न मर्तासो दित्सन्तम्‌। भीम॑ न गां बारयन्ते
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1899)
- **Original**: जैसे बलिष्ठ बैल को कोई नहीं हटा सकता, उसी प्रकार हे वीरेन्द्र ! दान देने में प्रवृत्त आपको देवता या मनुष्य कोई भो नहीं डिगा सकता
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1900)
- **Original**: उत्तराचिकि द्वितीयों 5 ध्याय: 2.3 7391.अभि त्वा वृषभा सुते सुतं सृजामि पीतये
- **Translation**: 

---

