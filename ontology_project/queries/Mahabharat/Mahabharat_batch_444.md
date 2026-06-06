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

### Verse 1 (Mahabharat 0.4431)
- **Original**: अर्जुनके सिवा ..और ... ऐसा... कयोन ._ है. जो... साक्षात्‌ मार्गसे स्वयं ही यमराजके पास चल्झ्रा जाऊँगा। धृतराष्ट्रनदन
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4431)
- **Original**: अर्जुनके सिवा ..और ... ऐसा... कयोन ._ है. जो... साक्षात्‌ मार्गसे स्वयं ही यमराजके पास चल्झ्रा जाऊँगा। धृतराष्ट्रनदन
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4432)
- **Original**: विष्णुभगवानसे सुरक्षित यादबोंके राजभवनको बल्हात्‌ नीचा दुर्बोधन सर्वदा ही मेरे कल्याणके लिये प्रयत्र कस्ते रहे हैं।
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4432)
- **Original**: विष्णुभगवानसे सुरक्षित यादबोंके राजभवनको बल्हात्‌ नीचा दुर्बोधन सर्वदा ही मेरे कल्याणके लिये प्रयत्र कस्ते रहे हैं।
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4433)
- **Original**: दिखाकर स्वयं पुरुषोत्तम श्रीकृष्णदी छोटी बहिनका हरण उनके लिये मैं अपने प्रिय भोग और दुल्यज प्राणोंको भी
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4433)
- **Original**: दिखाकर स्वयं पुरुषोत्तम श्रीकृष्णदी छोटी बहिनका हरण उनके लिये मैं अपने प्रिय भोग और दुल्यज प्राणोंको भी
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4434)
- **Original**: कर सके तथा तीनों त्थेकोंके अधीक्चरोंके भी ईश्वर भगवान्‌ निछावर कर सकता हूँ। मुझे यह श्रेष्ठ रंथ भगवान्‌
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4434)
- **Original**: कर सके तथा तीनों त्थेकोंके अधीक्चरोंके भी ईश्वर भगवान्‌ निछावर कर सकता हूँ। मुझे यह श्रेष्ठ रंथ भगवान्‌
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4435)
- **Original**: झंकरकों युद्धेके लिये छलकार सके। जब विराट-नग्रपें परशुरामजीने दिया था; इसकी धुरी जरा भी झब्द नहीं
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4435)
- **Original**: झंकरकों युद्धेके लिये छलकार सके। जब विराट-नग्रपें परशुरामजीने दिया था; इसकी धुरी जरा भी झब्द नहीं
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4436)
- **Original**: गोहरणके समय पुरुषश्रेष्ठ अर्जुनने तुम्हें सारी सेना और कस्ती। इसमें तरह-तरहके धनुष, ध्वजा, गदा, आण, खड़
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4436)
- **Original**: गोहरणके समय पुरुषश्रेष्ठ अर्जुनने तुम्हें सारी सेना और कस्ती। इसमें तरह-तरहके धनुष, ध्वजा, गदा, आण, खड़
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4437)
- **Original**: द्रोणाचार्य, अश्वत्यामा एवं भीष्मके सहित परास और अनेकों बढ़िया-बढ़िया हथियार रखे हुए हैं। किया था, उस समय तुमने उसे क्यों नहीं जीत लिया ? अब समय यह चलता है, इससे वज़््पातके समान भीषण
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4437)
- **Original**: द्रोणाचार्य, अश्वत्यामा एवं भीष्मके सहित परास और अनेकों बढ़िया-बढ़िया हथियार रखे हुए हैं। किया था, उस समय तुमने उसे क्यों नहीं जीत लिया ? अब समय यह चलता है, इससे वज़््पातके समान भीषण
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4438)
- **Original**: आज तुम्हारे वधके लिये हीं यह दूसरा युद्ध उपस्थित घरघराहट होने लगती है। इसमें सफेद घोड़े जुते हुए हैं तथा
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4438)
- **Original**: आज तुम्हारे वधके लिये हीं यह दूसरा युद्ध उपस्थित घरघराहट होने लगती है। इसमें सफेद घोड़े जुते हुए हैं तथा
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4439)
- **Original**: हुआ है। यदि तुम झब्रुके भंयसे भाग न गये तो अवश्य हीं अच्छे-अच्छे तरकस सुझोभित हैं। इस श्रेष्ठ रथमें बैठकर मैं
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4439)
- **Original**: हुआ है। यदि तुम झब्रुके भंयसे भाग न गये तो अवश्य हीं अच्छे-अच्छे तरकस सुझोभित हैं। इस श्रेष्ठ रथमें बैठकर मैं
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4440)
- **Original**: मारे जाओगे। अवश्य ही अर्जुनको मार डालूँगा। यदि-स्वयं. काल भी
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4440)
- **Original**: मारे जाओगे। अवश्य ही अर्जुनको मार डालूँगा। यदि-स्वयं. काल भी
- **Translation**: 

---

