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

### Verse 1 (Sama Ved 0.1721)
- **Original**: हे भित्रावरुण ! हमारी इस्द्रियों के आवास (देह) को तेजस्विता से युक्त करें और ऊर्ध्वलोकों को भी श्रेष्ठ रसों (भावों) से सिंचित करें
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1722)
- **Original**: 664.उरुशंसा नमोवृधा मह्ना दक्षस्थ राजथः । द्राधिष्ठाभि: शुचित्रता
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1723)
- **Original**: हे पवित्रकर्मा मित्रावरुणो
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1724)
- **Original**: आप हविष्यानन एवं महान्‌ स्तुतियों द्वारा पुष्ट होकर अपने गरिमामय श्रेष्ठ यश को प्राप्त करते हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1725)
- **Original**: 665,गृणाना जमदग्निना योनावृतस्य सीदतम्‌
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1726)
- **Original**: पात॑ सोममृतावृधा
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1727)
- **Original**: जमदम्नि ऋषि द्वारा स्तुति किये गये हे मित्रावरणो ! आप यज्ञ स्थान पर विराजें और हपारे द्वारा सिद्ध किये गये सोमरस का पान करें
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1728)
- **Original**: 666.आ याहि सुषुमा हि त इन्द्र सोम॑ पिबा इमम्‌ । एं बहहिं: सदो मम
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1729)
- **Original**: हे इन्द्देव ! आप पधारें और हमारे द्वारा निकाले गये सोमरस का पान कर श्रेष्ठ आसन पर विराजें
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1730)
- **Original**: 667.आ त्वा ब्रह्मययुजा हरी वहतामिन्द्र केशिना । उप ब्रह्मणि न: शूणु
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1731)
- **Original**: डे इद्धदेव ! मंत्र सुनते ही रथ में जुड़ जाने वाले श्रेष्ठ अश्वों के माध्यम से आप निकट आकर हमारी प्रार्थनाओं पर ध्यान दें
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1732)
- **Original**: 668.ब्रह्माणस्त्वा युजा बयं सोमपामिन्द्र सोमिन: । सुतावन्तों हवामहे
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1733)
- **Original**: हे इन्द्रदेव ! हम ब्रह्मनिष्ठ सोमयज्ञकर्त्ता और सोमरस तैयार करने वाले साधक .सोमरस पीने वाले आपको उपयुक्त स्तुतियों द्वारा बुलाते हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1734)
- **Original**: 669.इन्द्राग्नी आ गत॑ सुतं गीर्भिन भो वरेण्यम्‌। अस्य पातं धियेषिता
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1735)
- **Original**: उत्तराचिंके तृतीयो 5ध्याय: 1.3 हे इद्ध एवं अग्निदेव ! हमारी स्तुतियों से प्रभावित, आकाश से- ऊँचे पर्वत शिखरों से- आया हुआ यह श्रेष्ठ सोमरस है । हमारे भक्ति-भाव को स्वीकार कर इस सोमरस का पान करें
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1736)
- **Original**: 670. इन्द्राग्नी जरितु: सचा यज्ञों जिगाति चेतनः। अया पातमिमं सुतम्‌
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1737)
- **Original**: हे इन्दाग्ने ! आप स्तुति करने वालों के सहायक बनें । स्तुतियों द्वारा बुलाये गये आप स्फूर्तिदाता एवं यज्ञ के साधनभूत सोमरस का पान करें
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1738)
- **Original**: 6791.इन्द्रमग्निं कविच्छदा यज्ञस्य जूत्या वृणे। ता सोमस्येह तृम्पताम्‌
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1739)
- **Original**: यज्ञीय प्रेरणा से स्तुति करने वालों के लिए योग्य फलदाता इन्ध और अग्निदेव की हम पूजा करते हैं । वे दोनों देव इस यज्ञ में सोमरस पान से संतृष्ट हों
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1740)
- **Original**: इति द्वितीय: खण्ड:
- **Translation**: 

---

