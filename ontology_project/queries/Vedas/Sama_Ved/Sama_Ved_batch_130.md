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

### Verse 1 (Sama Ved 0.2581)
- **Original**: हे सुख प्रदाता इन्द्र और अग्निदेव ! ये स्तोतागण आप दोनों की वन्दना करते हैं । आप दोनों सोमरंस का पान करें
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2582)
- **Original**: 992.या वां सन्ति पुरुस्पृहों नियुतो दाशुषे नरा ।इन्द्राग्गी ताभिरा गतम्‌
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2583)
- **Original**: जगत्‌ के नायक हे इद्ध और अग्नि देवो ! याजकों द्वारा प्रशंसा किये जाते हुए, आप दोनों उससे प्रदत्त हविष्यान्न के लिए, यज्ञशाला में अपने द्रुतगामी वाहनों (अश्वों) की सहायता से पधारें तथा दानदाताओं की सहायता करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2584)
- **Original**: ; 993.ताभिरा गच्छतं नरोपेदं सबन॑ सुतम्‌ । इन्द्राग्नी प्तोमपीतये
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2585)
- **Original**: हे सृष्टि के नायक इन्द्र और अग्नि देवो ! विधिपूर्वक पवित्रता को प्राप्त इस सोमरस के पास इसका पांन करने के लिए, आप अपने वाहनों के साथ पधारें ।12
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2586)
- **Original**: इति तृतीय: खण्ड:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2587)
- **Original**: के के के
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2588)
- **Original**: चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2589)
- **Original**: 994.अर्षा सोम द्युमत्तमो5भि द्रोणानि रोरुवत्‌ । सीदन्योनौ वनेष्वा
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2590)
- **Original**: है अति तेजस्वी सोम ! पवित्र हुए आप, जल के साथ मिश्रित (अथवा काष्ठ-पात्र में पहले से विद्यमान) शब्द (ध्वनि) करते हुए द्रोण कलश में स्थिर हों
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2591)
- **Original**: 995.अप्सा इन्द्राय वायवे वरुणाय मरुदभ्य: । सोमा अर्पन्तु विष्णवे
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2592)
- **Original**: जल-मिश्रित शुद्ध सोमरस इन्द्र वायु, वरुण, मरुत्‌ एवं विष्णुदेवों की तृप्ति के लिए कलश में स्थिर हो
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2593)
- **Original**: 996.इष॑ तोकाय नो दधदस्मभ्यं सोम विश्वतः। आ पवस्व सहस्त्रिणम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2594)
- **Original**: - हे दिव्य सोम ! हमारी सन्‍्तानों के लिए आप सहसौरों प्रकार का अन्न, धनादि बैभव सभी ओर से लाकर प्रदान करें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2595)
- **Original**: : 997.सोम उ ष्वाण: सोतृभिरधि ष्णुभिरवीनाम्‌ । अश्वयेव हरिता याति धारया मन्द्रया याति धारया
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2596)
- **Original**: क्द्रत्विजों द्वारा निचोड़ा गया, आनन्दवर्द्धक, हरिताभ सोमरस, अश्व के समान वेगपूर्वक छनते हुए, कलश में स्थिर होता है
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2597)
- **Original**: 998.अनूपे गोमान्‌ गोभिरक्षा: सोमो दुग्धाभिरक्षा: । समुद्र न संवरणान्यग्मन्मन्दी मंदाय तोशते
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2598)
- **Original**: 6.6 सामवेद-संहिता आनन्द प्राप्ति के लिए तैयार किया जाने वाला, प्रकाशित, गो- दुग्ध मिश्रित, आनन्दवर्द्धक यह सोमरस, अपने पोषक तत्वों के साथ पात्र में उसी प्रकार स्थिर हो रहा है, जिस प्रकार सभी नदियाँ अपने आश्रयदाता समुद्र के पास पहुँचती और स्थिर होती हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2599)
- **Original**: 999.यत्सोम चित्रमुक्थ्य॑ दिव्यं पार्थिवं वसु । तन्न: पुनान आ भर
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2600)
- **Original**: पवित्रता को प्राप्त होने वाले हे दिव्य सोम ! इस पृथ्वी पर जो भी अदभुत प्रशंसनीय दिव्य वैभव है, वह सब आप हमें प्रदान करें
- **Translation**: 

---

