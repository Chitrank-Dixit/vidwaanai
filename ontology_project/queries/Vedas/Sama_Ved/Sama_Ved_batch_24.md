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

### Verse 1 (Sama Ved 0.461)
- **Original**: हे इन्द्रदेव ! वेदिका पर रखे गये आसन पर शोधित सोमरस आपके लिए है । आप शीघ्र ही आकर इसका पान करें
- **Translation**: 

---

### Verse 2 (Sama Ved 0.462)
- **Original**: 160. सुरूपकृत्नुमूतये सुदुघामिव गोदुहे । जुहूमसि द्विद्यति
- **Translation**: 

---

### Verse 3 (Sama Ved 0.463)
- **Original**: प्रतिदिन मधुर दूध प्रदान करने वाली गाय को, जिस प्रकार बुलाया जाता है, उसी प्रकार हम अपने संरक्षण के लिए सौन्दर्य प्रदान करने वाले इद्धदेव का आवाहन करते हैं
- **Translation**: 

---

### Verse 4 (Sama Ved 0.464)
- **Original**: 1691. अभि त्वा वृषभा सुते सुतं सृजामि पीतये। तृम्पा व्यश्नुही मदम्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.465)
- **Original**: हे बलशाली इन्धदेव ! सोमरस पीने के लिए इस सोमयज्ञ में आपके लिये सोमरस समर्पित करते हैं। आप इस तप्तिकारक सोमरस का पान करें
- **Translation**: 

---

### Verse 6 (Sama Ved 0.466)
- **Original**: 2.6 सापवेद-संहिता 162. य इन्द्र चमसेष्वा सोमश्चमृषु ते सुत: । पिबेदस्य त्वमीशिषे
- **Translation**: 

---

### Verse 7 (Sama Ved 0.467)
- **Original**: हे सामर्थ्यशाली इन्द्रदेव ! आपके लिए शुद्ध सोमरस ( छोटे-बड़े) चमस पात्रों में भरकर रखा हुआ है । आप इस दिव्य रस का पान करें
- **Translation**: 

---

### Verse 8 (Sama Ved 0.468)
- **Original**: 163. योगेयोगे तवस्तरं वाजेवाजे हवामहे । सखाय इन्द्रमूतये
- **Translation**: 

---

### Verse 9 (Sama Ved 0.469)
- **Original**: सत्कर्मों के शुभारम्भ में एवं हर प्रकार के संग्राम में बलशाली इन्द्रदेव का, अपने संरक्षण के लिए मित्रयत्‌ आवाहन करते हैं
- **Translation**: 

---

### Verse 10 (Sama Ved 0.470)
- **Original**: 164, आ त्वेता नि षीदतेद्धमभि प्र गायत । सखाय: स्तोमवाहस:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.471)
- **Original**: हे याज्ञिक मित्रो ! इच्रदेव को प्रसत्न करने के लिये, प्रार्थना करने हेतु शीघ्र आकर बैठो और हर प्रकार से स्तुति करों
- **Translation**: 

---

### Verse 12 (Sama Ved 0.472)
- **Original**: इति पज्चम: खण्ड:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.473)
- **Original**: के के हे
- **Translation**: 

---

### Verse 14 (Sama Ved 0.474)
- **Original**: षष्ठ: खण्ड:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.475)
- **Original**: 165. इदं ह्ान्वोजसा सुतं राधानां पते । पिबा त्वा3स्य गिर्वण:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.476)
- **Original**: हे ऐश्वर्यों के स्वामी, स्तुति के योग्य इन्द्रदेव ! बलपूर्वक निकाले (मिचोड़े) गये, इस सोमरस का रूचिपूर्वक पान करें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.477)
- **Original**: 166. महाँ इन्द्र: पुरश्च नो महित्वमस्तु वच्रिणे। दार्न प्रथिना शव:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.478)
- **Original**: हमारे ये इन्द्रदेव श्रेष्ठ और महान्‌ हैं । वज़धारी इन्द्रदेव का यश चुलोक के समान व्यापक होकर फैले तथा इनके बल की प्रशंसा चतुर्दिक्‌ हो
- **Translation**: 

---

### Verse 19 (Sama Ved 0.479)
- **Original**: 167, आ तू न इन्द्र क्षुमन्तं चित्र ग्राभ॑ सं गृूभाय। महाहस्ती दक्षिणेन
- **Translation**: 

---

### Verse 20 (Sama Ved 0.480)
- **Original**: महान्‌ भुजाओं वाले हे इन्द्रदेव ! आप हमें न्यायोपार्जित, प्रशंसनीय ऐश्वर्य दाहिने हाथ से (सम्मानपूर्वक) प्रदान करें
- **Translation**: 

---

