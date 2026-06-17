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

### Verse 1 (Rig Ved 0.1001)
- **Original**: (हे याजकों ! आप) बल बढ़ाने वाले, शत्रु नाशक, दीप्तिमान्‌ मरुद्गणों की सामर्थ्य और यश का मंत्रों से विशिष्ट गान करें
- **Translation**: 

---

### Verse 2 (Rig Ved 0.1002)
- **Original**: 446. प्र शंसा गोष्वघ्न्यं क्रोलुं यच्छर्थों मारुतम्‌ । जम्मे रसस्य बावृधे
- **Translation**: 

---

### Verse 3 (Rig Ved 0.1003)
- **Original**: (हे याजकों ! आप) किरणों द्वारा संचरित दिव्य रसों का पर्याप्त सेवन कर बलिष्ठ हुए उन मरुद्‌गणों के अविनाशी बल की प्रशंसा करें
- **Translation**: 

---

### Verse 4 (Rig Ved 0.1004)
- **Original**: 447. को वो वर्षिष्ठ आ नरो दिवश्न ग्मश्न धृतयः। यत्सीमन्त न धूनुथ
- **Translation**: 

---

### Verse 5 (Rig Ved 0.1005)
- **Original**: चुलोक और भूलोक को कम्पित करने वाले है मरुतो ! आप में बरिष्ट कौन है ? जो सदा वृक्ष के अग्रभाग को हिलाने के समान शत्रुओं को प्रकम्पित कर दे
- **Translation**: 

---

### Verse 6 (Rig Ved 0.1006)
- **Original**: 448. नि वो यामाय मानुषो दश्न उग्राय मन्यवे । जिहीत पर्वतो गिरि:
- **Translation**: 

---

### Verse 7 (Rig Ved 0.1007)
- **Original**: हे मस्ट्गणो ! आपके प्रचण्ड संघर्षक आवेश से भयभीत मनुष्य सुदृढ़ सहाय दूँढ़ता हैँ, क्योंकि आप बड़े पर्वतों और टीलों को भी कंँपा देते हैं
- **Translation**: 

---

### Verse 8 (Rig Ved 0.1008)
- **Original**: रत उक्त आह 449. येघामज्मेषु पृथिवी जुजुर्वा इब विश्पति:। भिया यामेषु रेजते
- **Translation**: 

---

### Verse 9 (Rig Ved 0.1009)
- **Original**: उन मरुदगणों के आक्रमणकारी बलों से यह पृथ्वी जरा-जीर्ण नृपति की भाँति भयभीत होकर प्रकम्पित हो उठती है
- **Translation**: 

---

### Verse 10 (Rig Ved 0.1010)
- **Original**: ष्ड्ड ऋग्वेट संहिता भाग-1 450, स्थिरं हि जानमेषां बयो मातुन्रितवे। यत्सीमनु द्विता शव:
- **Translation**: 

---

### Verse 11 (Rig Ved 0.1011)
- **Original**: इन वीर मरुतों की मातृ भूमि आकाश स्थिर है । ये मातृ भूमि से पक्षी के बेग के समान निर्बाधित होकर चलते हैं। उनका बल दुगुना होकर व्याप्त होता है
- **Translation**: 

---

### Verse 12 (Rig Ved 0.1012)
- **Original**: 451. उदु त्ये सूनबों गिरः काष्ठा अज्मेष्वलत। वाश्रा अभिज्ञु यातवे
- **Translation**: 

---

### Verse 13 (Rig Ved 0.1013)
- **Original**: शब्द नाद करने वाले मछुतों ने यज्ञार्थ जलों को नि: सृत किया । प्रवाहित जल का पान करने के लिये रैंभाती हुई गौएँ घुटने तक पानी में जाने के लिए बाध्य होती हैं
- **Translation**: 

---

### Verse 14 (Rig Ved 0.1014)
- **Original**: 2. त्यं चिद्धा दीर्घ पृथुं मिहो नपातममृश्चम्‌। प्रच्यावयन्ति यामभि:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.1015)
- **Original**: विज्ञाल और व्यापक, न बिंध सकने वाले, जल वृष्टि न करने वाले मेघों को भी वीर मरुदूगण अपनी तेजगति से उड़ा ले जाते हैं
- **Translation**: 

---

### Verse 16 (Rig Ved 0.1016)
- **Original**: 453. मरुतो यद्धू वो बल॑ जनाँ अचुच्यवीतन
- **Translation**: 

---

### Verse 17 (Rig Ved 0.1017)
- **Original**: गिरी रचुच्यवीतन
- **Translation**: 

---

### Verse 18 (Rig Ved 0.1018)
- **Original**: । है मरुतो
- **Translation**: 

---

### Verse 19 (Rig Ved 0.1019)
- **Original**: आप अपने बल से लोगों को विचलित कराते हैं, आप पर्वतों को भी विचलित करने में समर्थ हैं
- **Translation**: 

---

### Verse 20 (Rig Ved 0.1020)
- **Original**: 454. यद्ध यान्ति परुतः सं ह ब्ुवते5 ध्वज्ना। शूणोति कश्मिदेषघाम्‌
- **Translation**: 

---

