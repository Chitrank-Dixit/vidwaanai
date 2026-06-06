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

### Verse 1 (Vaivtpuran 6.2599)
- **Original**: सौ मन्वन्तरोंतक श्रीकृष्ण-प्रीतिके लिये तपस्या सदा तुम्हारे गुण गाऊँगा, पूजा करूँगा। तुम सदा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.2600)
- **Original**: करके सृष्टि, पालन और संहारका अधिकार प्राप्त मुझे अपने अधीन समझो। मैं तुम्हारी प्रत्येक
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.2601)
- **Original**: किया था। धर्म सौ मन्वन्तरोतक तप करके आज्ञाका पालन करनेके लिये बाध्य रहूँगा।' ऐसा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.2602)
- **Original**: सर्वपूज्य हुए। नारद! शेषनाग, सूर्यदेव, इन्द्र तथा कहकर जगदीश्वर श्रीकृष्णने उन्हें सचेत किया
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.2603)
- **Original**: चन्द्रमाने भी एक-एक मन्वन्तरतक भक्तिपूर्वक और अपनी उन प्राणवल्लभाकों सौतके कष्टसे मुक्त
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.2604)
- **Original**: श्रीकृष्णकी प्रसन्नताके लिये तप किया था। कर दिया। वायुदेवता सौ दिव्य युगोंतक भक्तिभावसे तपस्या जिन-जिन देवताओंकी जो-जो देवियाँ पतिद्वारा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.2605)
- **Original**: करके सबके प्राण, सबके द्वारा पूजनीय तथा सम्मानित हुई हैं, उनके उस सम्मानमें श्रीकृष्णकी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.2606)
- **Original**: सबके आधार बन गये। इस प्रकार श्रीकृष्ण- आराधना ही कारण है। मुने! जिनकी जैसी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.2607)
- **Original**: प्रीतिके लिये तपस्या करके सब देवता, मुनि, तपस्या है, उन्हें बैसा ही फल प्राप्त हुआ है।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.2608)
- **Original**: मानव, राजा तथा ब्राह्मण लोकमें पूजित हुए हैं। देवी दुर्गान सहख्र दिव्य वर्षोतक हिमालयपर तप
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.2609)
- **Original**: इस प्रकार मैंने तुमसे यह पुराण तथा आगमका करते हुए श्रीकृष्ण-चरणोंका ध्यान किया। इससे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.2610)
- **Original**: सारभूत सारा तत्त्व सुना दिया। अब तुम और वे सबकी पूजनीया हो गयीं। सरस्वती श्रीकृष्णकी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.2611)
- **Original**: क्या सुनना चाहते हो? (अध्याय 7) 220>0«यरथ33क्‍80005000 पृथ्वीकी उत्पत्तिका प्रसड्र, ध्यान और पूजनका प्रकार तथा स्तुति एवं पृथ्वीके प्रति शास्त्रविपरीत व्यवहार करनेपर नरकोंकी प्राप्तिका वर्णन नारदजीने कहा--भगवन्‌! आपने बतलाया
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.2612)
- **Original**: हो जाते हैं। तब उस समय पृथ्वी छिपकर कहाँ है कि श्रीकृष्णके निमेषमात्रमें ब्रह्माकी आयु पूरी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.2613)
- **Original**: रहती है और सृष्टिके समय वह पुनः कैसे प्रकट हो जाती है। उनका सत्ताशून्य हो जाना हो
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.2614)
- **Original**: हो जाती है? धन्या, मान्या, सबकी आश्रयरूपा एवं “प्राकृतिक प्रलय' कहा जाता है। उस समय पृथ्वी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.2615)
- **Original**: विजयशालिनी होनेका सौभाग्य उसे पुनः कैसे प्राप्त अदृश्य हो जाती है। सम्पूर्ण विश्व जलमें डूब जाता
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.2616)
- **Original**: होता है? प्रभो! अब आप पृथ्वीकी उत्पत्तिके है। सब-के-सब परल्रह्म परमात्मा श्रीकृष्णमें लीन
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.2617)
- **Original**: मड्रलमय चरित्रको सुनानेकी कृपा कीजिये।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.2618)
- **Original**: भगवान्‌ नारायण बोले--नारद! श्रुति
- **Translation**: 

---

