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

### Verse 1 (Bramha 0.7821)
- **Original**: गुण बताये गये हैं। चारों आश्रमोके लिये भी ये यजन करे और स्वाध्यायमें संलग्न रहे। शस्त्र
- **Translation**: 

---

### Verse 2 (Bramha 0.7822)
- **Original**: सामान्य गुण हैं। ब्राह्मणो! अब ब्राह्मण आदि चलाकर जीवन-निर्वाह करना और पृथ्वीका
- **Translation**: 

---

### Verse 3 (Bramha 0.7823)
- **Original**: वर्णोके उपधर्म बतलाये जाते हैं। आपत्तिकालमें पालन करना--ये दो क्षत्रियकी मुख्य जीविकाएं
- **Translation**: 

---

### Verse 4 (Bramha 0.7824)
- **Original**: ब्राह्मणके लिये क्षत्रियका कर्म, क्षत्रियके लिये हैं। उनमें भो पृथ्वीकी रक्षा उसके लिये मुख्य ' वैश्यका कर्म तथा वैश्य और क्षत्रिय दोनोंके लिये आजोविका है। पृथ्वीका पालन करनेसे ही राजा
- **Translation**: 

---

### Verse 5 (Bramha 0.7825)
- **Original**: शूद्रका कर्म कर्तव्य बताया गया है। सामर्थ्य रहते कृतार्थ होते हैं, क्योंकि उसीसे उनके यज्ञ आदि
- **Translation**: 

---

### Verse 6 (Bramha 0.7826)
- **Original**: इन दोनोंको शूद्रका कर्म नहीं करना चाहिये, परंतु कार्योंकी रक्षा होती है। जो राजा दुष्ट पुरुषोंका
- **Translation**: 

---

### Verse 7 (Bramha 0.7827)
- **Original**: आपत्तिकालमें वही कर्तव्य हो जाता है। आपत्ति न दमन और साधु पुरुषोंका पालन करके सब
- **Translation**: 

---

### Verse 8 (Bramha 0.7828)
- **Original**: होनेपर कर्म-संकर कदौपि न करे। ब्राह्मणो! इस वर्णॉंको अपने-अपने धर्ममें स्थापित करता है,
- **Translation**: 

---

### Verse 9 (Bramha 0.7829)
- **Original**: प्रकार मैंने वर्णधर्मका वर्णन किया है। वह मनोवाजञ्छत लोकोंको प्रात होता है। लोकपितामह
- **Translation**: 

---

### Verse 10 (Bramha 0.7830)
- **Original**: . अब आश्रमधर्मका भलीभाँति वर्णन करता हूँ, ब्रह्माजोने वैश्योंके लिये पशुओंका पालन, व्यापार
- **Translation**: 

---

### Verse 11 (Bramha 0.7831)
- **Original**: सुनो। उपनयन-संस्कार होनेपर ब्रह्मचारी बालक और खेतो-ये तीन आजीविकाएँ प्रदान की हैं।
- **Translation**: 

---

### Verse 12 (Bramha 0.7832)
- **Original**: एकाग्रचित हो गुर्के घरपर रहते हुए वेदोंका * सर्वलोकहित॑ कुर्यालाहित॑ कस्यचिद्‌ द्विजा:। मैत्री समस्तसत्वेषु ग्राह्मणस्योत्तमं धनम्‌
- **Translation**: 

---

### Verse 13 (Bramha 0.7833)
- **Original**: 5 (222। 5)
- **Translation**: 

---

### Verse 14 (Bramha 0.7834)
- **Original**: 376 + संक्षिप्त ब्रह्मपुरण » अध्ययन करे। शौच और सदाचारका पालन करते
- **Translation**: 

---

### Verse 15 (Bramha 0.7835)
- **Original**: सदा उनका स्वागत-सत्कार करना चाहिये। उन्हें हुए गुरुकी सेवा करे। पवित्र बुद्धिसे क्रतके पालनपूर्वक
- **Translation**: 

---

### Verse 16 (Bramha 0.7836)
- **Original**: शय्या, आसन और भोजन देना चाहिये। जिसके वेदोंकी शिक्षा ग्रहण करे। दोनों संध्याओंके समय
- **Translation**: 

---

### Verse 17 (Bramha 0.7837)
- **Original**: घरसे अतिथि निराश होकर लौटता है, बह उसे एकाग्रचित्त हो सूर्योपस्थान, अग्निहोत्र और गुरुका
- **Translation**: 

---

### Verse 18 (Bramha 0.7838)
- **Original**: अपना पाप दे बदलेमें उसका पुण्य लेकर चल देता अभिवादन करे। गुरुदेव खड़े हों तो स्वयं भी खड़ा
- **Translation**: 

---

### Verse 19 (Bramha 0.7839)
- **Original**: है।* गृहस्थ पुरुषमें दूसरोंके प्रति अवहेलना, रहे। वे जाते हों तो पौछे-पीछे जाय और बे बैठे हों
- **Translation**: 

---

### Verse 20 (Bramha 0.7840)
- **Original**: अपनेमें अहंकार, दम्भ, परनिन्दा, दूसरोॉपर चोट तो उनसे नीचे आसनपर बैठे। शिष्यको चाहिये कि
- **Translation**: 

---

