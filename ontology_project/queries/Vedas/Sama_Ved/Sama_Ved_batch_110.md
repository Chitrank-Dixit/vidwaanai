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

### Verse 1 (Sama Ved 0.2181)
- **Original**: हे उत्तम कर्मों के अधिष्ठाता, ऐश्वर्यवान्‌ू तेजस्वी सोमदेव ! कष्ट एवं पीड़ा को महत्त्व न देने वाले गरुड़ आपको झच्युलोक से पृथ्वी पर लाएँ
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2182)
- **Original**: 839.अथा हिन्वान इन्द्रियं ज्यायो महित्वमानशे । अभिष्टिकृद्धिचर्षणि:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2183)
- **Original**: इसके बाद (पृथ्वी पर आकर) ज्ञानसम्पन्न एवं इष्ट फलदायी सोम, शोधित होकर अपनी क्षमता को, और अधिक बढ़ाकर, और भी श्रेष्ठ बन जाता है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2184)
- **Original**: 840,विश्वस्मा इत्‌ स्वर्दशे साधारणं रजस्तुरम्‌। गोपामृतस्थ विर्भरत्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2185)
- **Original**: यज्ञ रक्षक, जल- प्रेरक, स्वयं प्रकाशित देव शक्तियों को सहजता से प्राप्त होने वाला दिव्य सोम आकाश को संय्याप्त कर लेता है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2186)
- **Original**: 8491.इथे पवस्व धारया मृज्यमानों मनीषिभि: । इन्दो रुचाभि गा इहि
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2187)
- **Original**: प्रज्ञावान्‌ साधकों द्वारा शोधित हे सोमदेव ! आप अपने तेज से पौष्टिक अल तथा सुन्दर गौएँ प्रदान करने के लिए स्रवित हों
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2188)
- **Original**: 12 842.पुनानों वरिवस्कृध्यूज॑ जनाय गिर्वण:। हरे सृजान आशिरम्‌
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2189)
- **Original**: हे हरिताभ, स्तुत्य सोमदेव ! दूध के साथ मिलाकर शोधित आप, याजकों को अन्नादि से भरपूर करें
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2190)
- **Original**: 843.पुनानो देववीतय इन्द्रस्य याहि निष्कृतम्‌ । ब्युतानो वाज़िभिहितः
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2191)
- **Original**: दिव्यशक्तियों से युक्त तेजस्वी हे सोमदेव ! देवशक्तियों के लिए हितकारी शोधित, आप इद्धदेव को प्राप्त हों
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2192)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2193)
- **Original**: केक ऊक॑
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2194)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2195)
- **Original**: 844.अग्निनाग्नि: समिध्यते कविर्गृहपतिरयुवा । हव्यवाड्‌ जुद्मास्य:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2196)
- **Original**: यज्ञस्थल के रक्षक, दूरदर्शी, युवा, आहुतियों को देवों तक पहुँचाने वाले ज्वालायुक्त यज्ञाग्नि को, अरणि-मंथन द्वारा उत्पन्न अग्निदेव से प्रज्वलित किया जाता है
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2197)
- **Original**: <845.यस्त्वामग्ने हविष्पतिर्दूतं देव सपर्यति । तस्य स्म प्राविता भव
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2198)
- **Original**: हे अग्निदेव ! देवगणों तक हविष्यान्न पहुँचाने वाले जो याजक, आप (देव-दूत) की उत्तम-विधि से अर्चना करते हैं, आप उनकी भली-भाँति रक्षा करें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2199)
- **Original**: 846.यो अग्नि देववीतये हविष्माँ आविवासति
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2200)
- **Original**: तस्मै पावक मृडय
- **Translation**: 

---

