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

### Verse 1 (Sama Ved 0.1181)
- **Original**: सम्पूर्ण शत्रुओं के संहारक ते, यज्ञ-स्थल पर निश्चित रूप से पूर्ण मनोयोग से उपस्थित रहते हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1182)
- **Original**: 451. उषा अप स्वसुष्टम: सं बर्तयति वर्तनिं सुजातता
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1183)
- **Original**: यह उषा अपनी बहिनरूपी रात्रि के अन्धकार को, अपनी रश्मियों से दूर करती है और उत्तम प्रकाश से अपने मार्ग को भी प्रकाशित करतो है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1184)
- **Original**: 452. इमा नु क॑ भुवना सीषधेमेन्द्रश्व विश्वे च देवा:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1185)
- **Original**: (मंत्रद्रष्टा क्रग्रष का कथन है कि) सुख-प्राप्ति की कामना से इस समस्त भूमण्डल को अपने अनुशासन में चलाता हूँ । इस कार्य में इन्द्र आदि सभो टेवगण हमारी मदद करते है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1186)
- **Original**: 453. वि खुतयो यथा पथा इन्द्र त्वद्यन्तु रातय:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1187)
- **Original**: हे इद्धदेव ! जैसे छोटे-छोटे रास्ते राजमार्ग में मिल जाते हैं, उसी प्रकार आपसे मिलने वाले दान सभी को प्राप्त होते हैं
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1188)
- **Original**: 454. अया वाजं देवहितं सनेम मदेम शतहिमाः सुवीरा:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1189)
- **Original**: इस स्तुति से (प्रसन) देव शक्तियों द्वारा प्रदत्त अन्न और बल हमें प्राप्त हो । उत्तम पराक्रमी सन्तानों से युवत होकर हम आनन्दपूर्वक रहें तथा शतायु हों
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1190)
- **Original**: ब्ट्द सामवेट-संहिता 455. ऊर्जा मित्रो वरुण: पिन्वतेडा: पीवरीमिषं कृणुही न इन्द्र
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1191)
- **Original**: है इन्द्रदेव ! मित्रावरुण देवता हमें बलवर्द्धक अन्न प्रदान करते हैं। आप हमारे अन्न को और अधिक पौष्टिक बनाएँ
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1192)
- **Original**: 456, इन्द्रो विश्वस्थ राजति
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1193)
- **Original**: इन्द्रदेव समस्त विश्वत्रह्माण्ड के शासक हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1194)
- **Original**: इति पद्ञत्रिश: खण्ड:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1195)
- **Original**: ऋऔ के के
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1196)
- **Original**: षट्त्रिश: खण्ड:
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1197)
- **Original**: 457. त्रिकद्रुकेषु महिषो यवाशिरं तुविशुष्मस्तृम्पत्सोममपिबद्धिष्णुना सुतं यथावशम्‌ । सईं भमाद महि कर्म कर्तवे महामुरुं सैनं सश्चद्देवो देवं सत्य इन्दुः सत्यमिन्द्रम्‌
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1198)
- **Original**: अत्यन्त बली, पूजनीय इन्द्रदेव ने तीनों लोकों में व्याप्त, तृप्तिदायक, दिव्य सोम को जौ के आटे के साथ मिलाकर विष्णुदेव के साथ इच्छानुसार पान किया । उस सोम ने महान्‌ इन्द्रदेव को श्रेष्ठ कार्य करने के लिए प्रेरित किया । उत्तम दिव्य गुणों से युक्त वह दिव्य सोमरस इन्द्रदेव को प्राप्त हुआ
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1199)
- **Original**: 458. अय॑ सहस्नरमानवो दृशः कबीनां मतिज्योतिर्विधर्म । ब्रध्न: समीचीरुषस: समैरयदरेपस: सचेतसः स्वसरे मन्युमन्तश्चिता गो:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1200)
- **Original**: सहस्त्रों मानवों का हितकारी, दर्शनीय, मेधावी, भ्रजा का धारक, तेजस्वी यह सुर्य निर्मल और तमरहित तेजस्वी उषाओं (रश्मियों) को भेजता है । इन सूर्य किरणों के सम्मुख चमकने वाले चन्द्र आदि अन्य नक्षत्र दिन में फीके हो जाते हैं
- **Translation**: 

---

