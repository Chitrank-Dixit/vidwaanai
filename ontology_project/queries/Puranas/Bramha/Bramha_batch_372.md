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

### Verse 1 (Bramha 0.7421)
- **Original**: उसका पाप छूट जाता है। संसारमें अन्न बलकी है। देवता, ऋषि, पितर और मनुष्य अन्नकी ही
- **Translation**: 

---

### Verse 2 (Bramha 0.7422)
- **Original**: वृद्धि करनेवाला है। उसका दान करनेसे मनुष्य प्रशंसा करते हैं; क्योंकि अन्नदानसे मनुष्य स्वर्गलोककों
- **Translation**: 

---

### Verse 3 (Bramha 0.7423)
- **Original**: बलबान्‌ बनता है। सत्पुरुषोंके मार्गपर चलनेसे सब प्रातत होता है। स्वाध्यायशील ब्राह्मणोंके लिये
- **Translation**: 

---

### Verse 4 (Bramha 0.7424)
- **Original**: पाप दूर हो जाते हैं। दानवेत्ा पुरुषोंने जो मार्ग न्यायोपार्जित उत्तम अन्नका प्रसन्नचित्तसे दान करना . बताया है और जिसपर मनीषी पुरुष चलते हैं, यही चाहिये। जिसके प्रसन्नचित्तसे दिये हुए अन्नकों
- **Translation**: 

---

### Verse 5 (Bramha 0.7425)
- **Original**: अन्नदाताओंका भी मार्ग है। उन्हींसे सनातन धर्म है। दस ब्राह्मण भोजन कर लेते हैं, वह कभी पशु- ' मनुष्यको सभी अवस्थाओंमें न्यायोपार्जित अन्नका पक्षी आदिकी योनिमें नहों पड़ता। सदा पापॉमें
- **Translation**: 

---

### Verse 6 (Bramha 0.7426)
- **Original**: दान करना चाहिये। क्योंकि अन्न सर्वोत्तम गति है। संलग्न रहनेबाला मनुष्य भी यदि दस हजार
- **Translation**: 

---

### Verse 7 (Bramha 0.7427)
- **Original**: अन्नदानसे मनुष्य परमगतिको प्रात होता है। इस ब्राह्मणॉंको भोजन करा दे तो वह अधर्मसे मुक्त
- **Translation**: 

---

### Verse 8 (Bramha 0.7428)
- **Original**: लोकमें उसकी समस्त कामनाएँ पूर्ण होती हैं और हो जाता है। बेदोंका अध्ययन करनेवाला ब्राह्मण । मृत्युके बाद भी वह सुखका भागी होता है।
- **Translation**: 

---

### Verse 9 (Bramha 0.7429)
- **Original**: मोहादधर्म॑ यः कृत्वा पुनः समनुतप्यते। मनःसमाधिसंयुक्तों न सर सेयेत दुष्कृतम्‌
- **Translation**: 

---

### Verse 10 (Bramha 0.7430)
- **Original**: यथा यथा मनस्तस्य दुष्कृतं कर्म गहते। तथा तथा शरीरं तु तेनाधरमेंण मुच्यते
- **Translation**: 

---

### Verse 11 (Bramha 0.7431)
- **Original**: यदि थिप्रा: कथयते विप्राणां धर्मबादिताम्‌। ठतो5धर्मकृतात्क्षिप्रमपराधात्प्रमुच्यते
- **Translation**: 

---

### Verse 12 (Bramha 0.7432)
- **Original**: अथा यथा नरः सम्यगथर्ममनुभाषते। समाहितेव मनसा विमुझति तथा तथा
- **Translation**: 

---

### Verse 13 (Bramha 0.7433)
- **Original**: अन्नस्थ हि प्रदानेन वरो याति परां गतिम्‌
- **Translation**: 

---

### Verse 14 (Bramha 0.7434)
- **Original**: सर्वकामसमायुक्त: प्रेत्य चाप्वश्नुते सुखम्‌। (218। 26-27)
- **Translation**: 

---

### Verse 15 (Bramha 0.7435)
- **Original**: 360 संक्षिप्त ब्रह्मपुराण इस प्रकार पुण्यवान्‌ मनुष्य पापोंसे मुक्त होता
- **Translation**: 

---

### Verse 16 (Bramha 0.7436)
- **Original**: संसार-बन्धनमें भी नहीं बँधता, अपितु सम्पूर्ण है। अतः अन्यायरहित अन्नका दान करना चाहिये।
- **Translation**: 

---

### Verse 17 (Bramha 0.7437)
- **Original**: कामनाओंसे तृप्त हो मृत्युके बाद सुखका भागी जो गृहस्थ सदा प्राणार्निहोत्रपूर्वूक अन्न-भोजन
- **Translation**: 

---

### Verse 18 (Bramha 0.7438)
- **Original**: होता है। इस प्रकार पुण्यकर्मसे युक्त मनुष्य करता है, वह अन्नदानसे प्रत्येक दिनकको सफल
- **Translation**: 

---

### Verse 19 (Bramha 0.7439)
- **Original**: निश्चित्त होकर आनन्दका भागी होता है। उसे बनाता है। जो मनुष्य वेद, न्याय, धर्म और , रूप, कोर्ति और धनकी प्राप्ति होती है। ब्राह्मणों! इतिहासके ज्ञाता सौ विद्वानोंको प्रतिदिन भोजन
- **Translation**: 

---

### Verse 20 (Bramha 0.7440)
- **Original**: इस प्रकार मैंने तुम्हें अन्नदानका महान्‌ फल कराता है, वह घोर नरकमें नहीं पड़ता और
- **Translation**: 

---

