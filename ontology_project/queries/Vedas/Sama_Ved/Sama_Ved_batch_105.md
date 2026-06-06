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

### Verse 1 (Sama Ved 0.2081)
- **Original**: इति द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2082)
- **Original**: क््ड सामवेद-संहिता
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2083)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2084)
- **Original**: 803.वृषा पवस्व धारया मरुत्वते च मत्सर:। विश्वा दधान ओजसा
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2085)
- **Original**: है सोमदेव ! आप बलवर्द्धक बनकर शोधित हों । सभी ऐश्वर्यों सहित मरुतों के सखा इन्द्रदेव को आप आनन्द प्रदान करें
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2086)
- **Original**: 804.त॑ त्वा धर्तारमोण्यो3: पवमान स्वर्द्शम्‌
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2087)
- **Original**: हिन्वे वाजेषु वाजिनम्‌
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2088)
- **Original**: है शोधित सोमदेव ! आप आत्मदर्शों बलवान, चुलोक से पृथ्वीलोक तक सभी को संरक्षण प्रदान करने वाले हैं । ऐसे सोम को हम संग्राम (जीवन-संग्राम) के लिए प्रेरित करते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2089)
- **Original**: 805.अया चित्तों विपानया हरि: पवस्व धारया। युज॑ वाजेषु चोदय
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2090)
- **Original**: हे हरे रंग वाले सोम ! अँगुलियों से परिष्कृत किये गये आप दिव्य कलश में शोधित होने के लिए, ख्नवित हों और अपने सखा इन्द्रदेव को संग्राम में जाने के लिए प्रेरित करें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2091)
- **Original**: 806.वृषा शोणो अभिकनिक्रदद्गा नदयन्नेषि पृथिवीमुत द्याम्‌। इन्द्रस्थेव वग्नुरा श्रूण्व आजौ प्रचोदयननर्षसि वाचमेमाम्‌
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2092)
- **Original**: निरन्तर गतिशील, सुखों की वर्षा करने वाले, हे दिव्य सोमदेव ! दुलोक से पृथ्वो तक किरणों के बीच मेघ जैसी गर्जना (प्रतिध्वनियाँ) उत्पन्न करते हुए आप संव्याप्त हैं। हम इन्द्रदेव (स्वामी) की तरह आपके निर्देशों को सुनते हैं। आप भी अपनी उपस्थिति का बोध कराते हुए हमारी स्तुतियों को स्वीकार करते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2093)
- **Original**: <807.रसाय्य: पयसा पिन्वमान ईरयन्नेषि मधुमन्तमंशुम्‌ । पवमान सन्तनिमेषि कृण्वन्निन्द्राय सोम परिधिच्यमान:
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2094)
- **Original**: अपने आप में मधुर, गाय के दूध में मिश्रित होने के बाद अधिक सुस्वाद हुए हे सोमदेव ! पानी में शोधित होकर धाररूप में (निरन्तर) आप इन्धदेव को प्राप्त हों
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2095)
- **Original**: 808,एवा पवस्व मदिरों मदायोदग्राभस्थ नमयन्वधस्नुम्‌ । परि वर्ण भरपाणो रुशन्तं गव्युनों अर्थ परि सोम सिक्‍तः
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2096)
- **Original**: हे उत्साहवर्द्धक सोमदेव ! छाये हुए मेघों को जल वृष्टि के लिए प्रेरित करते हुए आप आनन्ददायी बनें । पानी के साथ श्वेत वर्ण धारण कर, गाय के दूध के रूप में, हमारे चारों ओर स्नवित हों
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2097)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2098)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2099)
- **Original**: 809.त्वामिद्धि हवामहे सातौ वाजस्थ कारव: । त्वां वृत्रेष्विन्द्र सत्प्ति नरस्त्वां काष्ठास्वर्वत:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2100)
- **Original**: हे इन्द्रदेव ! हम स्तोता आपको अन वृद्धि के लिए आवाहित करते हैं । हे इद्धदेव ! विज्ञजन संघर्ष के समय आपको ही मदद के लिए पुकारते हैं
- **Translation**: 

---

