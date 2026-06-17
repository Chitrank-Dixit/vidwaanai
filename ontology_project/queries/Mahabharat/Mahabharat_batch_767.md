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

### Verse 1 (Mahabharat 941.7661)
- **Original**: धर्मकी उपासना करते हैं, वह सब मैंने तुन्हें सुना दिया
- **Translation**: 

---

### Verse 2 (Mahabharat 941.7661)
- **Original**: धर्मकी उपासना करते हैं, वह सब मैंने तुन्हें सुना दिया
- **Translation**: 

---

### Verse 3 (Mahabharat 941.7662)
- **Original**: हडड संक्षिप्त महाभारत [ अनुझासनपर्व है। अब जो कुछ बाकी रह गया हो उसको भगवान्‌
- **Translation**: 

---

### Verse 4 (Mahabharat 941.7662)
- **Original**: हडड संक्षिप्त महाभारत [ अनुझासनपर्व है। अब जो कुछ बाकी रह गया हो उसको भगवान्‌
- **Translation**: 

---

### Verse 5 (Mahabharat 941.7663)
- **Original**: विभाग करते हुए सूर्यरूपमें उदित होते हैं। उत्तरायण और श्रीकृष्णसे सीखना। इन आ्रीकृष्णका जो स्वरूप है और जो
- **Translation**: 

---

### Verse 6 (Mahabharat 941.7663)
- **Original**: विभाग करते हुए सूर्यरूपमें उदित होते हैं। उत्तरायण और श्रीकृष्णसे सीखना। इन आ्रीकृष्णका जो स्वरूप है और जो
- **Translation**: 

---

### Verse 7 (Mahabharat 941.7664)
- **Original**: दक्षिणायन इन्हींके दो मार्ग हैं। ये प्रत्येक मासमें यज्ञ करते हैं इनका पुरातन बल है, उसे ठीक-ठीक मैं जानता हूँ। भगवान्‌
- **Translation**: 

---

### Verse 8 (Mahabharat 941.7664)
- **Original**: दक्षिणायन इन्हींके दो मार्ग हैं। ये प्रत्येक मासमें यज्ञ करते हैं इनका पुरातन बल है, उसे ठीक-ठीक मैं जानता हूँ। भगवान्‌
- **Translation**: 

---

### Verse 9 (Mahabharat 941.7665)
- **Original**: और वेदज्ञ ब्राह्मण इन्हींके गुण गाते हैं। ये महातेजस्थी और श्रीकृष्ण अप्रमेय हैं, अतः तुम्हारे मनमें संदेह होनेपर ये ही तुम्हें
- **Translation**: 

---

### Verse 10 (Mahabharat 941.7665)
- **Original**: और वेदज्ञ ब्राह्मण इन्हींके गुण गाते हैं। ये महातेजस्थी और श्रीकृष्ण अप्रमेय हैं, अतः तुम्हारे मनमें संदेह होनेपर ये ही तुम्हें
- **Translation**: 

---

### Verse 11 (Mahabharat 941.7666)
- **Original**: सर्वत्र व्याप्त रहनेवाले श्रीकृष्ण अकेले ही सम्पूर्ण जगतको धर्मका उपदेश करेंगे। श्रीकृष्णने ही इस पृथ्वी, आकाश और
- **Translation**: 

---

### Verse 12 (Mahabharat 941.7666)
- **Original**: सर्वत्र व्याप्त रहनेवाले श्रीकृष्ण अकेले ही सम्पूर्ण जगतको धर्मका उपदेश करेंगे। श्रीकृष्णने ही इस पृथ्वी, आकाश और
- **Translation**: 

---

### Verse 13 (Mahabharat 941.7667)
- **Original**: धारण करते हैं। युधिश्लिर ! तुम इन्हींको अन्यकारनाशक सूर्य स्वर्गकी सृष्टि की है। ये ही भयंकर बलवाले वाराहके रूपयें
- **Translation**: 

---

### Verse 14 (Mahabharat 941.7667)
- **Original**: धारण करते हैं। युधिश्लिर ! तुम इन्हींको अन्यकारनाशक सूर्य स्वर्गकी सृष्टि की है। ये ही भयंकर बलवाले वाराहके रूपयें
- **Translation**: 

---

### Verse 15 (Mahabharat 941.7668)
- **Original**: समझो। ये पञ्चमहाभूतोंके केद्र हैं। इन्होंने ही आकाश, प्रकट हुए थे तथा इन्हीं पुराणपुरुषने पर्वतों और दिज्ञाओंको
- **Translation**: 

---

### Verse 16 (Mahabharat 941.7668)
- **Original**: समझो। ये पञ्चमहाभूतोंके केद्र हैं। इन्होंने ही आकाश, प्रकट हुए थे तथा इन्हीं पुराणपुरुषने पर्वतों और दिज्ञाओंको
- **Translation**: 

---

### Verse 17 (Mahabharat 941.7669)
- **Original**: पृथ्वी, स्वर्ग, अन्तरिक्ष, बन और पर्वतोंकी सृष्टि की है। ये उत्पन्न किया है। अत्तरिक्ष,स्वर्ग, चारों दि्लाएँ और चारों
- **Translation**: 

---

### Verse 18 (Mahabharat 941.7669)
- **Original**: पृथ्वी, स्वर्ग, अन्तरिक्ष, बन और पर्वतोंकी सृष्टि की है। ये उत्पन्न किया है। अत्तरिक्ष,स्वर्ग, चारों दि्लाएँ और चारों
- **Translation**: 

---

### Verse 19 (Mahabharat 941.7670)
- **Original**: इच्दिपोंके नियन्‍ता और अत्यन्त प्रज्यल्तित अग्निके समान कोण--ये सब भगवान्‌ श्रीकृष्णसे नीचे हैं। इन्हींसे इस
- **Translation**: 

---

### Verse 20 (Mahabharat 941.7670)
- **Original**: इच्दिपोंके नियन्‍ता और अत्यन्त प्रज्यल्तित अग्निके समान कोण--ये सब भगवान्‌ श्रीकृष्णसे नीचे हैं। इन्हींसे इस
- **Translation**: 

---

