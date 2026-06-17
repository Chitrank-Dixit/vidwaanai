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

### Verse 1 (Sama Ved 0.721)
- **Original**: हे इन्द्रदेव ! हमें यज्ञ कर्म में प्रवीण बनाएँ । पिता द्वारा पुत्र को दिये जाने वाले शिक्षण की भाँति हमें भी आप मार्गदर्शन दें । प्रजा द्वारा स्मरणीय हे इद्धदेव ! नित्य प्रति हम सूर्यदेव के दर्शन करें
- **Translation**: 

---

### Verse 2 (Sama Ved 0.722)
- **Original**: 260.मा न इन्द्र परा वृणग्भवा नः सधमाद्े । त्वं न ऊती त्वमिन्न आप्यं मा न इन्द्र परावृणक्‌
- **Translation**: 

---

### Verse 3 (Sama Ved 0.723)
- **Original**: पूर्वार्थिके ऐम्द्रपर्वीणणि तृतीय 5ध्याय: ल्‍ 3.5 हे इन्द्रदेव ! आप हमारे रक्षक तथा बन्धु हैं । हे इन्द्रदेव ! आप हमारे इस यज्ञ में पधारें, हमें अपने से कभी भी दूर न करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.724)
- **Original**: 261.वयं घ त्वा सुतावन्‍्त आपो न वृक्तबर्हिष: । पवित्रस्य प्रस्नवणेषु वृत्रहन्परि स्तोतार आसते
- **Translation**: 

---

### Verse 5 (Sama Ved 0.725)
- **Original**: हे वृत्रहन्ता इन्द्रदेव ! जिस प्रकार जल नीचे की ओर प्रवाहित होता है, उसी प्रकार शोधित सोमरस सहित हम आपको नमन करते हैं । पवित्र यज्ञ में कुश-आसन पर एक साथ बैठकर याजक आपकी उपासना करते हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.726)
- **Original**: 262. यदिन्द्र नाहुषीष्वा ओजो नृग्णं च कृष्टिषु । यद्दा पहक्षितीनां द्युम्नमा भर सत्रा विश्वानि पौंस्या
- **Translation**: 

---

### Verse 7 (Sama Ved 0.727)
- **Original**: हे इद्रदेव ! संगठित प्रजा में जो पराक्रम है, पांच जनों (पाँचों बगों ) में जो धन है, बैसा ही ऐश्वर्य आप हमें प्रदान करें । एकता से उत्पन्न होने वाली शक्ति हमें प्राप्त हो
- **Translation**: 

---

### Verse 8 (Sama Ved 0.728)
- **Original**: [ पंच जनों को संगति सपाज के पाँचों वर्णो ब्राह्मणु क्षत्रिय वैश्य शूद्र एवं निषाद, पैच भूतों तथा पंचकोशों सभी के साथ बैठती है ।]
- **Translation**: 

---

### Verse 9 (Sama Ved 0.729)
- **Original**: इत्ति पंचदश: खण्ड:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.730)
- **Original**: के के के
- **Translation**: 

---

### Verse 11 (Sama Ved 0.731)
- **Original**: षोडशः खण्ड:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.732)
- **Original**: 263.सत्यमित्था वृषेदर्सि वृषजूतिनोंठबिता । वृषा ह्युग्न श्रृण्विषि परावति वृषों अर्वावति श्रुतः
- **Translation**: 

---

### Verse 13 (Sama Ved 0.733)
- **Original**: हे वीर इन्द्रदेव ! दूर और पास के देशों में सर्वत्र शक्तिशाली रूप में आपकी ख्याति फैला हुई है । हे इन्रदेव ! आप निश्चित रूप से बलशाली हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.734)
- **Original**: सोमयज्ञ करने वाले हम याजकों के आवाहन पर आकर, आप हमारा संरक्षण करें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.735)
- **Original**: 264.यच्छक्रासि परावति यदर्वावति वृत्रहन्‌ । अतत्त्या गीर्भिद्युगदिन्द्र केशिभिः सुतावाँ आ विवासति
- **Translation**: 

---

### Verse 16 (Sama Ved 0.736)
- **Original**: हे सामर्थ्यवान्‌ वृत्रहन्ता इन्रदेव
- **Translation**: 

---

### Verse 17 (Sama Ved 0.737)
- **Original**: आप दूरस्थ हों या निकटस्थ हों, श्रेष्ठ घोड़ों के समान वेगवान्‌ स्तुतियों से सोमयज्ञ में याजक आपका आवाहन करते हैं।
- **Translation**: 

---

### Verse 18 (Sama Ved 0.738)
- **Original**: 265अभि वो वीरमन्धसो मदेषु गाय गिरा महा विचेतसम्‌ । इन्द्रं नाम श्रुत्यं शाकिनं वचो यथा
- **Translation**: 

---

### Verse 19 (Sama Ved 0.739)
- **Original**: है उदगाता ! हितकारी, असुरजयी, सोमरस से आनन्दित, बीर, मेधावी तथा कीर्तिमान्‌ इन्रदेव की विशेष स्तोत्रों से जैसे भी संभव हो, स्तुति करो
- **Translation**: 

---

### Verse 20 (Sama Ved 0.740)
- **Original**: 266. इन्द्र त्रिधातु शरणं त्रिवरूथं स्वस्तये । छर्दियच्छ मघवद्ध्यश्व मद्ां च यावया दिद्युमेभ्य:
- **Translation**: 

---

