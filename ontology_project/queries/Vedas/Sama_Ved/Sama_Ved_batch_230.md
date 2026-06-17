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

### Verse 1 (Sama Ved 0.4581)
- **Original**: हे इन्द्रदेव ! आप वाणी से न बोल पाने वाले अज्ञानी के स्तुति पाठ को भी जानते हैं तथा बोले जाने वाले स्तोत्र को भी जानते हैं और गेय 'गायत्न-साम' को भी जानते ही हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.4582)
- **Original**: 1806. मा न इन्द्र पीयलवे मा शर्धते परा दा: । शिक्षा शचीव: शचीभि:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.4583)
- **Original**: . हे इन्धदेव ! हिंसक शत्रुओं और उपेक्षित करने वालों के आश्रय पर आप हमें मत छोड़े । अपने बल से हमें इष्ट ऐश्वर्य प्रदान करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.4584)
- **Original**: 1807. एन्द्र याहि हरिभिरुप कण्वस्य सुष्टुतिम्‌ । दिवो अमुष्य शासतो दिवं यय दिवावसो
- **Translation**: 

---

### Verse 5 (Sama Ved 0.4585)
- **Original**: हे इन्रदेव ! आप घोड़ों से पहुँचकर यजमान कौ स्तुतियों को ग्रहण करें । हे चुलोक निवासक इन्धरदेव ! हम आपके इस दिव्य शासन में सुखपूर्वक रहते हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.4586)
- **Original**: 1808. अत्रा वि नेमिरेषामुरां न धूनुते वृक: । दिवो अमुष्य शासतो दिवं यय दिवावसो
- **Translation**: 

---

### Verse 7 (Sama Ved 0.4587)
- **Original**: भेड़िये के भय से कॉपती हुई भेंड़ के समान, पाषाणों की घारें कूटे जाने वाले सोम को कंपाती हैं । हे द्ुलोक निवासी इन्द्रदेव ! हम आपके दिव्य शासन में सुख पूर्वक रहते हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.4588)
- **Original**: 1809, आ त्वा ग्रावा वदन्निह सोमी घोषेण वक्षतु । दिवो अमुष्य शासतो दिवं यय दिवावसो
- **Translation**: 

---

### Verse 9 (Sama Ved 0.4589)
- **Original**: उत्तराचिंके विजो5धघ्यायः 20.7 हे इन्द्र ! इस यज्ञ में सोम कूटने का शब्द करते हुए पाषाण द्वारा आपको शब्द करने वाला सोम प्राप्त हो । हे दुलोक निवासक इन्द्र !हम आपके दिव्य शासन में अत्यन्त सुखपूर्वक रहते हैं, आप अपने लोक को जाएँ
- **Translation**: 

---

### Verse 10 (Sama Ved 0.4590)
- **Original**: 1810. पवस्व सोम मन्दयन्निन्द्राय मधुमत्तम:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.4591)
- **Original**: है सोम ! अत्यन्त मधुर रस से भरे हुए आप हर्ष उत्पन्न करते हुए इन्द्रदेव के निमित्त शोधित हों
- **Translation**: 

---

### Verse 12 (Sama Ved 0.4592)
- **Original**: 1811. ते सुतासो विपश्चित: शुक्रा वायुमसृक्षत
- **Translation**: 

---

### Verse 13 (Sama Ved 0.4593)
- **Original**: वह मेधावर्द्धक सोम शोधित होकर वायु देवता के निमित्त प्रकट होता है
- **Translation**: 

---

### Verse 14 (Sama Ved 0.4594)
- **Original**: 1812, असग्र॑ देववीतये वाजयन्तो रथा इब
- **Translation**: 

---

### Verse 15 (Sama Ved 0.4595)
- **Original**: यह सोमरस अन प्राप्ति के अभिच्छु यजमानों द्वारा देवों के लिए तैयार किया जाता है । रथों को सुसज्जित करने के समान सोमरस को तैयार किया जाता है
- **Translation**: 

---

### Verse 16 (Sama Ved 0.4596)
- **Original**: इति चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.4597)
- **Original**: और के के
- **Translation**: 

---

### Verse 18 (Sama Ved 0.4598)
- **Original**: पंचम: खण्ड:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.4599)
- **Original**: 1813. अग्नि होतारं मन्ये दास्वन्तं वसो: सूनुं सहसो जातवेदसं विप्र॑ न जातवेदसम्‌ । य ऊर्ध्वया स्वध्वरो देवो देवाच्या कृपा । घृतस्य विश्राष्टिमनु शुक्रशोचिष आजुद्बलानस्य सर्पिष:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.4600)
- **Original**: सर्वज्ञाता, सर्वस्थापक, बलोत्पन्ल, ज्ञानसम्पन, पूज्य, स्वप्रकाशित, दैदीप्यमान, यज्ञ वाहक, घृत आदि के अनुरूप तेज प्रवाहक अग्निदेव को हम यज्ञ सिद्ध करने वाला, देवों को बुलाने वाला मानते हैं
- **Translation**: 

---

