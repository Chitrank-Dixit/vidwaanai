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

### Verse 1 (Sama Ved 0.2381)
- **Original**: तद्विदच्छर्यणावति
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2382)
- **Original**: अन्तरिश्ष में स्थित मेघों के अन्दर विद्यमान विद्युत्‌ शक्ति को इन्द्रदेव ने प्राप्त किया और उससे आसुरी शक्तियों (अनाचारियों) का संहार किया
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2383)
- **Original**: 915.अन्राह गोरमन्वत नाम त्वष्ट्रपीच्यम्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2384)
- **Original**: इत्था चन्द्रमसो गृहे
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2385)
- **Original**: गतिशौल चन्द्रमण्डल में परोक्ष रूप से विद्यमान सूर्यदेव की तेजस्वी किरणें ही रात्रि में प्रकाशित होती हैं-- ऐसी मान्यता है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2386)
- **Original**: [ चऋत्यमा में स्वयं का प्रकाश न होने और सूर्य द्वारा उसके प्रकाशित होने का विज़ान- सिस्द्ध तथ्य प्रकर किया गया है ।] 916.इयं वामस्य मन्मन इन्द्राग्नी पूर्व्यस्तुति:ः। अश्राद्वृष्टिरिवाजनि
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2387)
- **Original**: हे इन्र और अम्निदेव ! श्रेष्ठ सम्माननौय विद्वानों द्वारा, आप दोनों की प्रधम बार की गई यह स्तुति, मेघों से होने वाली वर्षा की भाँति (सहज रूप से ) उत्पन्न हुई है
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2388)
- **Original**: 917.श्रृणुतं जरितुर्हवमिद्धाग्नी वनत॑ गिर: । ईशाना पिप्यतं धिय:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2389)
- **Original**: हे इन्द्राग्नी ! स्तुति करने वाले साधकों की प्रार्थना को आप सुनें । आप दोनों समर्थ शासक के रूप में उनके (स्तोता के, श्रेष्ठ) कर्मों के (श्रेष्ठ) फल प्रदान करें
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2390)
- **Original**: 918.मा पापत्वाय नो नरेन्द्राग्नी माभिशस्तये । मा नो रीरेधतं निदे
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2391)
- **Original**: प्रगति की ओर ले जाने वाले नेता स्वरूप, है इन्द्र और अग्निदेव ! आप हमें हिंसा और पाप कर्मों से बचाएँ । निन्दनीय कार्यों से हमें दूर रखें
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2392)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2393)
- **Original**: कु के के
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2394)
- **Original**: उत्तराचिके पञ्वमो5 ध्याय: 5.5
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2395)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2396)
- **Original**: 919.पवस्व दक्षसाथनो देवेभ्यः पीतये हरे । मरुद्भद्यो वायवे मद:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2397)
- **Original**: शक्ति ब उल्लास बढ़ाने वाले, हे हरिताभ सोम ! आप वायु एवं मरुत्‌ देवताओं को तृप्त करने के लिए पवित्र हों
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2398)
- **Original**: 920.सं देव: शोभते वृषा कवियोनावधि प्रियः । पवमानो अदाध्य:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2399)
- **Original**: ज्ञान और बल से सम्पन्न, शुद्ध-संस्कारित होने के कारण सभी के परमप्रिय, किसी के बन्धन में न रहने वाले सोमदेव, देवताओं के मध्य शोभा को प्राप्त हो रहे हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2400)
- **Original**: 921.पवमान धिया हितो35भि योनिं कनिक्रदत्‌
- **Translation**: 

---

