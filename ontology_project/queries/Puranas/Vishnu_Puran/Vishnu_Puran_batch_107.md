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

### Verse 1 (Vishnu Puran 0.2121)
- **Original**: 9 दितेः पुत्रों महात्रीयों हिरण्यकशिपु: पुरा । त्रैलोक्य॑ बशमानिन्ये ब्रह्मणो वरदर्पित:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2122)
- **Original**: 2 बुन्द्रत्वमकरोहैत्यः स चासीत्सविता स्वयम्‌ । वायुरओरपां नाथ: सोमश्माभून्महासुरः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2123)
- **Original**: 3 धनानामधिप: सो5भूत्स एवासीत्स्वय यम: । यज्ञभागानशोषांस्तु स स्वयं बुभुजेउसुर:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2124)
- **Original**: 4ड देवा: स्वर्ग परित्यज्य तत्लासान्मुनिसत्तम । विचेरुरवनों सर्वे बिश्राणा मानु्षी तनुम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2125)
- **Original**: 5 जिल्वा त्रिम्ुवन सर्व त्रैलोक्यैश्वर्यदर्पित:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2126)
- **Original**: उपगीयमानो गश्धर्वर्शुभुजे विषयात्रियान्‌। 6 पानासक्ते महात्मानं॑ हिरण्यकशिपुं तदा। उपासाश्चक्रिरे सर्वे सिद्धगन्धर्वपन्नगा:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2127)
- **Original**: 7 अवादयन्‌ जगुआझ्नान्ये जयशब्द तथापरे। दैत्यराजस्य पुरतश्चक्कुः सिद्धा मुद्ान्विता: । 8 तत्र श्रनृत्ताप्सरसि स्फाटिकाभ्रमयेउसुरः । पपौ पान मुदा युक्त: प्रासादे सुमनोहरे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2128)
- **Original**: 9 तस्थ पुत्रों महाभाग: प्रह्मदों नाम नामत: । पपाठ बालपाठ्यानि गुरुगेहड्रतो3र्भक:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2129)
- **Original**: 10 एकदा तु स॒ धर्मात्मा जगाम गुरुणा सह। पानासक्तस्थ पुरतः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2130)
- **Original**: 11 श्रीपराइरजी बोले--हे मैत्रेय ! उन सर्वदा उदारचरित परमबुद्धिमान्‌ महात्मा प्रह्मदजीका चरित्र तुप् ध्यानपूर्वक श्रवण करो
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2131)
- **Original**: पूर्वकालमें दितिके पुत्र महाबली हिरण्यक्रदिपुने, क्रद्माजीके वरसे गर्वयुक्त (सशाक्त) होकर सम्पूर्ण व्िस्त्रेकीकों अपने वशोभूत कर लिया था
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2132)
- **Original**: यह दैत्य इन्द्रपदका भोग करता था । यह महान्‌ असुर स्बय॑ ही सूर्य, वायु, अम्नि, खरूण और चन्द्रमा खना हुआ था
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2133)
- **Original**: यह स्थय॑ ही फुलेर और यमराज भी था और यह असुर स्वयं ही सम्पूर्ण यज्ष-भागोंकी भोगता था
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2134)
- **Original**: हे मुतिसत्तम ! उसके भयसे देवगण स्वर्गकों जोड़कर मनुष्य-शरणेर घारणकर भूमण्डलमें त्रिचरते रहते थे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2135)
- **Original**: इस प्रकार सम्पूर्ण त्रिलोकीकों जीतकर ब्रिभुबनके वैंभवसे गर्लित हुआ और गन्क्‍्वोंसि अपनी स्तुति सुनता हुआ वह अपने अभीष्ट भोगोंकों भोगता था
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2136)
- **Original**: उस समय उस मद्यपानासक्त महाकाय हिरण्यकश्ञिपुकों हो समस्त सिद्ध, गन्धर्व और नाग आदि उपासना कस्ते थवे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2137)
- **Original**: उस दैत्यराजके सामने कोई सिद्धगण तो प्रसन्न होकर जयजयकार करते
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2138)
- **Original**: तथा यह असुरणज वहाँ स्फटिक एल अभ्न-दिलाके बने हुए मनोहर महरूसें, जहाँ अप्सराओॉका उत्तम जृत्व हुआ करता था, प्रसन्नताके साथ मद्यपान करता रहता था
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2139)
- **Original**: उसका प्रद्धमाद नामक महाभाग्ययाग्‌ पुत्र था। यह यआलक गुल्के यहाँ जाकर बालोचित पाठ पढ़ने लगा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2140)
- **Original**: एक दिन वह धर्मात्मा चालक गुरुजीके साथ अपने पिता दैत्यराजके पास गया जो ठस समय
- **Translation**: 

---

