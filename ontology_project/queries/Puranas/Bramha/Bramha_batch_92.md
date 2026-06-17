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

### Verse 1 (Bramha 0.1821)
- **Original**: तथा अनेक प्रकारके पत्रित्र जलाशय सब ओरसे विख्यात क्षेत्र बाराणसीके समान कोटि शिवलिबड्रोंसे
- **Translation**: 

---

### Verse 2 (Bramha 0.1822)
- **Original**: उस स्थानकी शोभा बढ़ाते हैं। युक्त एवं शुभ है। उसमें आठ तीर्थ हैं। पूर्व/ उस क्षेत्रमें साक्षात्‌ भगवान्‌ शक्कूर सब लोकोंका कल्पमें वहाँ एक आमका वृक्ष था। ठउसीके नामसे
- **Translation**: 

---

### Verse 3 (Bramha 0.1823)
- **Original**: हित करनेके लिये निवास करते हैं। वे भोग और वह एकाम्नकक्षेत्रके रूपमें विख्यात हुआ। वह
- **Translation**: 

---

### Verse 4 (Bramha 0.1824)
- **Original**: मोक्ष दोनोंके दाता हैं। इस पृथ्वीपर जितने तीर्थ, स्थान हृष्ट-पुष्ट मनुष्योंसे भरा रहता है, वहाँ
- **Translation**: 

---

### Verse 5 (Bramha 0.1825)
- **Original**: नदियाँ, सरोबर, पुष्करिणी, तड़ाग, बापी, कूप स्त्रियाँ भी रहती हैं और पुरुष भी। उस क्षेत्रमें
- **Translation**: 

---

### Verse 6 (Bramha 0.1826)
- **Original**: और सागर हैं, उन सबसे पृथक्‌-पृथक्‌ जलकी विद्वानोंकी अधिकता है, बह धन-धान्यसे सम्पन्न
- **Translation**: 

---

### Verse 7 (Bramha 0.1827)
- **Original**: बूँदें संगृहोत करके देवताओंसहित भगवान्‌ शद्भूरने स्थान है। घर और गोपुर बहाँकी शोभा बढ़ाते हैं।
- **Translation**: 

---

### Verse 8 (Bramha 0.1828)
- **Original**: उस क्षेत्रमें सम्पूर्ण लोकोंके हितके लिये बिन्दुसर वहाँ अनेकों व्यवसायी भरे हुए हैं। भाति-भाँतिके
- **Translation**: 

---

### Verse 9 (Bramha 0.1829)
- **Original**: नामक तीर्थ स्थापित किया। इसीलिये बह विन्दुसरके रत्न उस क्षेत्रकी शोभा बढ़ाते हैं। नगर, अटारी,
- **Translation**: 

---

### Verse 10 (Bramha 0.1830)
- **Original**: नामसे विख्यात है। अगहनके कृष्णपक्षकी अष्टमीको सड़क और राजहंसॉंके समान श्वेत महल आदिके
- **Translation**: 

---

### Verse 11 (Bramha 0.1831)
- **Original**: जो वहाँकी यात्रा करता है तथा जो जितेन्द्रिय द्वारा उसकी बड़ी शोभा होती है। उसके चारों
- **Translation**: 

---

### Verse 12 (Bramha 0.1832)
- **Original**: भावसे विषु्रयोगमें श्रद्धेके साथ बिधिपूर्वक ओर सफेद चहारदीवारी बनी है। शरस्त्रोंद्रारा उस
- **Translation**: 

---

### Verse 13 (Bramha 0.1833)
- **Original**: विन्दुसरोवरमें स्नान करके तिल और जलसे नाम- पुरकी रक्षा होती है। अनेकों खाइयोंसे वह क्षेत्र
- **Translation**: 

---

### Verse 14 (Bramha 0.1834)
- **Original**: गोत्रके उच्चारणपूर्वक देवताओं, ऋषियों, मनुष्यों अलड्जूत है। वहाँ प्रतिदिन उत्सवका आनन्द छाया
- **Translation**: 

---

### Verse 15 (Bramha 0.1835)
- **Original**: एवं पितरोंका तर्पण करता है, वह अश्बमेध- रहता है। नाना प्रकारके बराजोंकी ध्वनि सुनायी
- **Translation**: 

---

### Verse 16 (Bramha 0.1836)
- **Original**: यज्ञका फल पाता है। जो ग्रहण, बिषुबयोग, पड़ती है। चहारदीवारी और बगीचोंसे युक्त अनेक , संक्रान्ति, अयनारम्भ, छियासी युगादि तिथि तथा दिव्य देवमन्दिर सब ओर उस क्षेत्रकी शोभा
- **Translation**: 

---

### Verse 17 (Bramha 0.1837)
- **Original**: अन्यान्य शुभ तिथधियोंमें वहाँ ब्राह्मणॉंकों धन बढ़ाते हैं। वहाँके ब्राह्मण, क्षत्रिय, वैश्य तथा शुद्र
- **Translation**: 

---

### Verse 18 (Bramha 0.1838)
- **Original**: आदिका दान करते हैं, वे अन्य तीर्थोंकी अपेक्षा बड़े धार्मिक हैं। बे अपने-अपने धर्मांमें संलग्र
- **Translation**: 

---

### Verse 19 (Bramha 0.1839)
- **Original**: सौगुना फल पाते हैं। जो विन्दुसरोबरके तटपर रहते हैं। उस क्षेत्रमें निर्धन, मूर्ख, दूसरोंसे द्वेष
- **Translation**: 

---

### Verse 20 (Bramha 0.1840)
- **Original**: पितरोंको पिण्डदान देते हैं, बे उन पितगेंको रखनेवाले, रोगी, मलिन, नीच, मायावी, रूपहीन,
- **Translation**: 

---

