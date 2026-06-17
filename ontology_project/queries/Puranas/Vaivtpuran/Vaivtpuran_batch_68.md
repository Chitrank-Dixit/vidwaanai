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

### Verse 1 (Vaivtpuran 6.2579)
- **Original**: तपस्या कौ। इंससे वे अत्यन्त कृशकाय हो गयीं। उन्होंके दिये ज्ञानसे तथा उन्होंके लिये किये गये
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.2580)
- **Original**: श्रीकृष्णने देखा, राधा चन्द्रमाकी एक कलाके तपके प्रभावसे बे उनके समान ही महान्‌ एबं
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.2581)
- **Original**: समान अत्यन्त कृश हों गयी हैं, अब इनके सर्वेश्वर हुए हैं। उन परमात्मा श्रीकृष्णके ज्ञानके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.2582)
- **Original**: शरीरमें साँसका चलना भी बंद हो गया है, तब प्रभावसे ही भगवान्‌ विष्णु महान्‌ विभूतिसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.2583)
- **Original**: वे प्रभु करुणासे द्रवित हो उन्हें छातीसे लगाकर सम्पन्न, सर्वज्ञ, सर्वदर्शी, सर्वव्यापी, सबके रक्षक,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.2584)
- **Original**: फूट-फूटकर रोने लगे। उन्होंने राधाकों वह सम्पूर्ण सम्पत्ति प्रदान करनेमें समर्थ, सर्वेश्वर तथा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.2585)
- **Original**: सारभूत वर दिया, जो अन्य सब लोगोंके लिये समस्त जगत्‌के अधिपति हुए हैं। उन्हींके ज्ञानसे,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.2586)
- **Original**: दुर्लभ है। वे बोले-'प्राणबल्लभे! तुम्हारा स्थान उन्होंके लिये की गयी तपस्यासे तथा उन्होंके प्रति
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.2587)
- **Original**: मेरे वक्ष:स्थलपर है, तुम यहीं रहो। मुझमें तुम्हारी भक्ति और उन्हींकी सेवासे प्रकृति सर्वशक्तिमती
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.2588)
- **Original**: अविचल प्रेम-भक्ति हो। सौभाग्य, मान, प्रेम और भहामाया और सर्वेश्वरी हुई है। उन्हींके ज्ञान,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.2589)
- **Original**: गौरवकी दृष्टिसे तुम मेरे लिये सबसे श्रेष्ठ और भजन, तपस्या एबं सेवा करनेसे देवमाता सावित्री
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.2590)
- **Original**: सर्वाधिक प्रियतमा बनी रहो। संसारकी समस्त वेदोंकी अधिष्ठात्री देवी और बेदमाता हुई हैं,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.2591)
- **Original**: युवतियोंमें तुम्हाशा सबसे ऊँचा स्थान है। तुम
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.2592)
- **Original**: 118 + संक्षिप्त ग्रह्मवैयर्तपुराण « सबसे अधिक महत्त्व तथा गौरव प्राप्त करो। मैं
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.2593)
- **Original**: प्रसन्नताके लिये लाख दिव्य वर्षोतक गन्धमादन का रपपर 75ः पर्वतपर तपस्या करके सबकी बन्‍्दनीया हुई हैं। £
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.2594)
- **Original**: लक्ष्मी सौ दिव्य युगोंतक पुष्करतीर्थमें तपस्यापूर्वक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.2595)
- **Original**: श्रीकृष्णकी आराधना करके समस्त सम्पदाओंको
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.2596)
- **Original**: देनेमें समर्थ हुई हैं। सावित्री मलयाचलपर साठ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.2597)
- **Original**: हजार दिव्य वर्षोतक तप एबं श्रीकृष्ण-चरणोंका 70
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.2598)
- **Original**: चिन्तन करके द्विजोंकी पूजनीया हो गयी हैं। मुने! पूर्वकालमें ब्रह्मा, विष्णु तथा शिवने ; 5
- **Translation**: 

---

