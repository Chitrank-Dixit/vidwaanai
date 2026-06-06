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

### Verse 1 (Sama Ved 0.2041)
- **Original**: 787,पवमानस्य ते बयं पवित्रमभ्युन्दटः । सखित्वमा वृणीमहे
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2042)
- **Original**: है सोमदेव ! परिष्कृत और शोधित होने वाले आपसे, हम मित्र के रूप में सहयोग पाने की कामना करते हैं
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2043)
- **Original**: 788.ये ते पवित्रमूर्मयो 5भिक्षरन्ति धारया। तेभिर्न: सोम मृडय
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2044)
- **Original**: है सोमदेव! आपकी लहरों में से जो धारा शोधित हो रही है, उसके द्वारा हमें उललसित करने का अनुग्रह करें
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2045)
- **Original**: 789.स न: पुनान आ भर रवि बीरवतीमिषम्‌ । ईशान: सोम विश्वत:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2046)
- **Original**: है सोमदेव ! आप जगत्‌ नियन्ता हैं। शोधित होने के बाद आप हमें धन-धान्य के साथ सुसन्तत्ति प्रदान करें
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2047)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2048)
- **Original**: ऊँ के के
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2049)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2050)
- **Original**: 790.अरन दूतं वृणीमहे होतारं विश्ववेदसम्‌ । अस्य यज्ञस्य सुक्रतुम्‌
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2051)
- **Original**: देवी शक्तियों को श्रेष्ठ कार्य की ओर प्रेरित करने वाले, ऐश्वर्यवान, इस यज्ञ को उत्तम विधि से सम्पन्न कराने वाले, हविदाहक अग्निदेव का हम आवाहन करते हैं
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2052)
- **Original**: 791.अग्निमग्निं हवीमभि: सदा हवन्त विश्पतिम्‌
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2053)
- **Original**: हव्यवाहं पुरुप्रियम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2054)
- **Original**: प्रजापालक, देवों नकः हवि पहुँचाने वाले, परम प्रिय, कुशल नेतृत्त्व प्रदान करने वाले है अग्निदेव ! हम याजक हवनीय मंत्रों से आपको सदा बुलाते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2055)
- **Original**: 792.अमने देवाँ इहा वह जज्ञानों वृक्तबर्हिषे । असि होता न ईड्च:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2056)
- **Original**: उत्तराच्कि तृतीयों 5ध्याय ड3 हे स्तुत्य, सखा, देवाराधक अग्निदेव ! अरणियों से उत्पन्न हुए आप देवावाहन करने वाले साधकों के लिए देवशक्तियों को इस यज्ञ में बुलाएँ
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2057)
- **Original**: 793.मित्र॑ं वयं हवामहे वरुणं सोमपीतये । या जाता पूतदक्षसा
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2058)
- **Original**: यज्ञ में आवाहित दैवोशक्तियों, परम पवित्र एवं बलशालो मित्र और वरुण देवों का हम आवाहन कर ते हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2059)
- **Original**: 794.ऋतेन यावृतावृधावृतस्य ज्योतिषस्पती । ता मित्रावरुणा हुवे
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2060)
- **Original**: सत्यमार्ग पर चलने वालों का उत्साह बढ़ाने वाले हे तेजस्वी मित्रावरुणो
- **Translation**: 

---

