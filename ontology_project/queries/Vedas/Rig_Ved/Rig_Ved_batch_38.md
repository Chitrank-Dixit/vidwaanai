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

### Verse 1 (Rig Ved 0.741)
- **Original**: 331. सं यन्मदाय शुष्मिण एना ह्ास्योदरे
- **Translation**: 

---

### Verse 2 (Rig Ved 0.742)
- **Original**: समुद्रो न व्यघो दथे
- **Translation**: 

---

### Verse 3 (Rig Ved 0.743)
- **Original**: समुद्र में एकत्र हुए जल के सदृश सोमरस इन्‍्द्रदेव के पेट में एकत्र होकर उन्हें हर्ष प्रदान करता है
- **Translation**: 

---

### Verse 4 (Rig Ved 0.744)
- **Original**: 2. अयमु ते समतसि कपोत इब गर्भधिम्‌। वचस्तच्चिन्न ओहसे
- **Translation**: 

---

### Verse 5 (Rig Ved 0.745)
- **Original**: हे इन्द्रदेव ! कपोत जिस स्नेह के साथ गर्भवती कपोती के पास रहता है, उसी प्रकार (स्नेहपूर्वक) यह सोमरस पके लिये प्रस्तुत है । आप हमारे निवेदन को स्वीकार करें
- **Translation**: 

---

### Verse 6 (Rig Ved 0.746)
- **Original**: 38 ऋग्वेद संहिता धाग-9 333 स्तोत्र राधानां पते गिर्वाहो वीर यस्य ते। विभूतिरस्तु सूनृता
- **Translation**: 

---

### Verse 7 (Rig Ved 0.747)
- **Original**: जो (स्तोतागण) हे इन्द्र ! हे धनाधिपत्ि ! हे स्तुतियों के आश्रयभूत ! हे बीर ! (इत्यादि) स्तुतियाँ करते हैं, उनके लिये आपकी विभूतियाँ प्रिय एवं सत्य सिद्ध हों
- **Translation**: 

---

### Verse 8 (Rig Ved 0.748)
- **Original**: 334. ऊर्ध्वस्तिष्ठा न ऊतये स्मिन्वाजे शतक्रतो । समन्येषु ब्रवावहै
- **Translation**: 

---

### Verse 9 (Rig Ved 0.749)
- **Original**: सैकड़ों यज्ञादि श्रेष्ठ कार्यों को सम्पन करने वाले हे इद्धदेव ! संघर्षों (जीवन - संग्राम) में हमारे संरक्षण के लिये आप प्रयलशील रहें
- **Translation**: 

---

### Verse 10 (Rig Ved 0.750)
- **Original**: हम आप से अन्य (श्रेष्ठ) कार्यो के विषय में भी परस्पर विचार-विनिमय करते रहें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.751)
- **Original**: 335, योगेयोगे तवस्तरं बाजेवाजे हवामहे। सखाय इन्द्रमूतये
- **Translation**: 

---

### Verse 12 (Rig Ved 0.752)
- **Original**: सत्कर्मों के शुभारम्भ में एवं हर प्रकार के संग्राम में बलशाली इन्द्रदेव का हम अपने संरक्षण के लिये मित्रवत्‌ आवाहन करते हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.753)
- **Original**: 336. आ घा गमद्यदि श्रवत्सहस्रिणीभिरूतिभि: । वाजेभिरुप नो हवम्‌
- **Translation**: 

---

### Verse 14 (Rig Ved 0.754)
- **Original**: हमाएँ प्रार्थना से प्रसन्‍न होकर वे इन््रदेव निश्चित ही सहसौरों रक्षा - साधनों तथा अन्न, ऐश्बर्य आदि सहित हमारे पास आयेंगे
- **Translation**: 

---

### Verse 15 (Rig Ved 0.755)
- **Original**: 337 अनु प्रलनस्यौकसो हुवे तुविप्रति नरम्‌। य॑ ते पूर्व॑ पिता हुवे
- **Translation**: 

---

### Verse 16 (Rig Ved 0.756)
- **Original**: हम सहायता के लिये स्वर्गधाम के वासी, बहुतों के पास पहुँचकर उन्हें नेतृत्व प्रदान करने वाले इद्धदेव का आवाहन करते हैं । हमारे पिता ने भी ऐसा ही किया था
- **Translation**: 

---

### Verse 17 (Rig Ved 0.757)
- **Original**: 338. त॑ त्वा बयं विश्ववारा शास्महे पुरुहूत। सखे वसो जरितृभ्यः
- **Translation**: 

---

### Verse 18 (Rig Ved 0.758)
- **Original**: हे विश्ववरणीय इन्द्रदेव ! बहुतों द्वारा आवाहित किये जाने वाले आप स्तोताओं के आश्रय दाता और मित्र हैं। हम (ऋत्विग्गण) आप से उन (स्तोताओं ) को अनुगृहीत करने की प्रार्थना करते हैं
- **Translation**: 

---

### Verse 19 (Rig Ved 0.759)
- **Original**: 339. अस्माकं शिप्रिणीनां सोमपा: सोमपान्वाम्‌। सखे वश्रनिन्सखीनाम्‌
- **Translation**: 

---

### Verse 20 (Rig Ved 0.760)
- **Original**: हे सोम पीने वाले वद्भधारी इन्द्रदेव ! सोम पीने के योग्य हमारे प्रियजनों और मित्रजनों में आप ही श्रेष्ठ सामर्थ्य वाले हैं
- **Translation**: 

---

