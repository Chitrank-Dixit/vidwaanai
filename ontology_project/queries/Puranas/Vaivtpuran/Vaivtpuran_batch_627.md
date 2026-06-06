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

### Verse 1 (Vaivtpuran 56.5452)
- **Original**: देती है। बैष्णवोंके कर्म-बन्धनका उच्छेद करनेके है, उन दुर्गतिग्रस्त जीवोंको मायाद्वारा ही
- **Translation**: 

---

### Verse 2 (Vaivtpuran 56.5453)
- **Original**: लिये परमात्मा श्रीकृष्णजी वह वैष्णवी शक्ति मोहजालसे बाँध देती है। फिर तो वे बर्बर जीव
- **Translation**: 

---

### Verse 3 (Vaivtpuran 56.5454)
- **Original**: तीखे शस्त्रका काम करती है। नरेश्वर! उस इस नश्वर एवं अनित्य संसारमें सदा नित्यबुद्धि शक्तिकी शक्ति भी दो प्रकारकों है। एक कर लेते हैं और परमेश्वरकी उपासना छोड़कर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 56.5455)
- **Original**: विवेचनाशक्ति और दूसरी आवरणी शक्ति। पहली दूसरे-दूसरे देवताओंकी सेवामें लग जाते हैं तथा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 56.5456)
- **Original**: अर्थात्‌ विवेचनाशक्ति तो वह भक्तोंको देती है उन्हीं देवताओंके मन्त्रका जप करते हैं। लोभवश
- **Translation**: 

---

### Verse 6 (Vaivtpuran 56.5457)
- **Original**: और दूसरी आवरणी शक्ति अभक्तके पल्ले बाँधती मनमें किसी मिथ्या निमित्तको स्थान देकर वे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 56.5458)
- **Original**: है। भगवान्‌ श्रीकृष्ण सत्यस्वरूप हैं। उनसे भिन्न इस तरह भटक जाते हैं। अन्य देवता भी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 56.5459)
- **Original**: सारा जगत्‌ नश्वर है। विवेचना-बुद्धि नित्यरूपा श्रीहरिकी कलाएँ हैं। उनका सात जन्मोंतक सेवन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 56.5460)
- **Original**: एवं सनातनी है। यह मेरी श्री है। यही वैष्णव करनेके पश्चात्‌ वे देवी प्रकृतिकी कृपासे उनकी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 56.5461)
- **Original**: भक्तोंको प्राप्त होती है। किंतु आवरणी बुद्धि आराधनामें संलग्न होते हैं। सात जन्मोंतक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 56.5462)
- **Original**: कर्मोंका फल भोगनेवाले अधम अवैष्णब पुरुषोंको
- **Translation**: 

---

### Verse 12 (Vaivtpuran 56.5463)
- **Original**: # प्रकृतिखण्ड « 283 ##ऋक कक ऋऋऋऋऋडऋऊऋऋकऋ कक अं 4
- **Translation**: 

---

### Verse 13 (Vaivtpuran 56.5464)
- **Original**: 8 क्ऋ्क्ऊ कक 4888 ## कक 468 89 प्राप्त हुआ करती है। राजन! मैं प्रचेताका पुत्र
- **Translation**: 

---

### Verse 14 (Vaivtpuran 56.5465)
- **Original**: दोनोंको दुर्गानीकी पूजाकी विधि, स्तोत्र, कबच और ब्रह्माजीका पौत्र हूँ तथा भगवान्‌ शंकरसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 56.5466)
- **Original**: और मन्त्रका उपदेश दिया। वैश्यने उन कृपामयी ज्ञान प्राप्त करके परमात्मा श्रीकृष्णका भजन करता
- **Translation**: 

---

### Verse 16 (Vaivtpuran 56.5467)
- **Original**: देवीकी आराधना करके मोक्ष प्राप्त किया तथा हूँ। महाराज! नदीके तटपर जाओ और सनातनी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 56.5468)
- **Original**: राजाकों अपना अभीष्ट राज्य, मनुका पद और दुर्गाका भजन करो। तुम्हारे मनमें राज्यकी कामना
- **Translation**: 

---

### Verse 18 (Vaivtpuran 56.5469)
- **Original**: मनोवाज्छित परम ऐश्वर्य प्राप्त हुआ। इस प्रकार है, इसलिये वे देवी तुम्हें आवरणी बुद्धि प्रदान
- **Translation**: 

---

### Verse 19 (Vaivtpuran 56.5470)
- **Original**: मैंने सुखद, सारभूत एवं मोक्षदायक परम उत्तम करेंगी तथा इस निष्काम वैष्णव वैश्यकों बे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 56.5471)
- **Original**: दुर्गाका उपाख्यान पूर्णरूपसे सुना दिया। अब तुम कृपामयी वैष्णवीदेवी शुद्ध विवेचना-बुद्धि देंगी।
- **Translation**: 

---

