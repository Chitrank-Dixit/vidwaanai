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

### Verse 1 (Vishnu Puran 0.11681)
- **Original**: 30 श्रीपताज्ञर उन्नाच एवमुक्ते तु कृष्णेन यादवप्रवरस्ततः । महाभागवतः प्राह प्रणिपत्योडबो हरिम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11682)
- **Original**: 31 खिं> 80 14--- सुनिये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11683)
- **Original**: हे भगबवन्‌ ! देवताओंकी प्रेरणासे उनके ही साथ पृथिवीका भार उतारनेके लिये अवतीर्ण हुए आपको सौ वर्षसे अधिक बीत चुके हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11684)
- **Original**: अब आप दुराचारी दैल्योंकों मार चुके और पृथित्रीका भार भी उत्तार चुके, अतः [हमारी भ्रार्थना है कि] अब देवगण सर्वद। स्वर्गमें ही आपसे सनाथ हों [अर्थात्‌ आप स्वर्ग पधास्कर देवताओंकों सनाथ करें]
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11685)
- **Original**: है जगन्नाथ ! आपको भूमण्डर्में पधारे हुए सौ वर्षसे अधिक हो गये, अब यदि आपको पसन्द आबवे तो स्वर्गलोक पधारिये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11686)
- **Original**: है देव! देवशणका यह भी कथन है कि यदि आपको यहीं रहना आच्छा लगे तो रहें, सेवक्य्रेंका तो यही धा। है कि [ स्वामीको
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11687)
- **Original**: यथासमय कर्तव्यका निवेदन कर दे”
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11688)
- **Original**: श्रीभगवान्‌ बोले--हे द्वूत ! तुम जो कुछ कहते हो वह मैं सब जानता हूँ, इसलिये अब मैंने यादवोके नाशका आरम्म कर ही दिया है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11689)
- **Original**: इन यादवोंका संहार हुए बिना अभीतक पृथिवीका भार हल्का नहीं हुआ है, अत: अब सात रात्रिके भीतर [ इनका संहार करके ] पृथिवीका भार उतारकर मैं शीघ्र ही [ जैसा तुम कहते हो ] वही करूँगा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11690)
- **Original**: जिस फ्रकार यह द्वारकाकी भूमि मैंने समुद्रसे माँगी थी इसे उसी प्रकार उसे ल्त्रैटाकर
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11691)
- **Original**: तथा यादवॉका उपसंहारकर मैं स्वर्गलोकमें आऊँगा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11692)
- **Original**: अब देवराज इन्द्र और देवताओंको यह समझना
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11693)
- **Original**: चाहिये कि सँकर्षणके सहित मैं मनुष्य-शरीरकों स्लेड़कर
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11694)
- **Original**: स्वर्ग पहुँच ही चुका हूँ
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11695)
- **Original**: पृथिवीके भारभूत जो जरासख्थ आदि अन्य ग़जागण मारे गये हैं, ये यदुकुमार भी उनसे कम नहीं हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11696)
- **Original**: अतः तुम देक्ताओंसे जाकर कहो कि मैं पृधिजीके इस महाभारको उतारकर हो देव- ल्त्रेकका पालन करनेके लिये स्वर्गपें आऊँगा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11697)
- **Original**: श्रीपराशरजी बोले--हे मैत्रेय ! भगवान्‌ वासुदेवके इस प्रकार कहनेपर देवदूत वायु उन्हें प्रणाम करके अपनी दिज्य गतिसे देजराजके पास चले आये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11698)
- **Original**: भगवानतने देखना कि द्वारकापुरीमें रात-दिन नाशके सूचक दिव्य, भौस और अन्तरिक्ष-सम्बन्धी महान्‌ उत्पात हो रहे हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11699)
- **Original**: उन उत्पातोंकों टेखकर भगवान्‌ने यादबोंसे कहा-- “देखो, ये कैसे घोर उपद्रव हो रहे हैं, चल्ले, सोम ही इनकी शान्तिके र्तये प्रभासक्षेत्रकों चें"'
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11700)
- **Original**: श्रीपराशरजी घोले--कृष्णचन्द्रके ऐसा कहनेपर महाभागवत यादवश्रेष्ठ उद्धबने श्रीहरिको प्रणाम करके
- **Translation**: 

---

