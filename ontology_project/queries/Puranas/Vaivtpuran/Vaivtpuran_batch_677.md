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

### Verse 1 (Vaivtpuran 75.9188)
- **Original**: तलवारका काम देता है तथा आपके चरणारविन्दोंमें परमेश्वरीका दर्शन करके सब देवताओंको बड़ा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 75.9189)
- **Original**: स्थान दिलानेका एकमात्र हेतु है। आप जन्म- आश्चर्य हुआ। उनके सम्पूर्ण मनोरथ पूरे हो
- **Translation**: 

---

### Verse 3 (Vaivtpuran 75.9190)
- **Original**: जन्ममें मुझे अपने चरणारविन्दोंकी भक्ति गये थे। अत: उन सब देवताओंने पुनः भगवान्‌की
- **Translation**: 

---

### Verse 4 (Vaivtpuran 75.9191)
- **Original**: प्रदान कीजिये। स्तुति आरम्भ कौ-- भगवान्‌ नारायण कहते हैं--इस प्रकार ब्रह्मोवाच स्तुति करके पूर्णमनोरथ हुए वे तीनों देवता तब चरणसरोजे मन्मनश्चद्धरीको कामनाओंकी पूर्ति करनेवाले श्रीराधावल्लभके भ्रमतु सततमीश प्रेमभक्त्या सरोजे।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 75.9192)
- **Original**: सामने खड़े हो गये। देवताओंकी यह स्तुति भ्रवनमरणरोगात्‌ पाहि शान्त्यौषधेन सुनकर कृपानिधान श्रीकृष्णके मुखारविन्दपर मन्द मु सुदृग्सुपरिपक्यां देहि भक्ति च दास्यम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 75.9193)
- **Original**: मुस्कान खिल उठी। वे उनसे हितकर एबं सत्य ब्रह्माजी बोले--परमेश्वर! मेरा चित्तरूपी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 75.9194)
- **Original**: वचन बोले।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 75.9195)
- **Original**: 418 » संक्षिमत ब्रह्म॑वैवर्तधुरण « ककऋडककऋऋकऋऋ कक कऋऋऋऋ््ऋ्ऋऋऋ %
- **Translation**: 

---

### Verse 9 (Vaivtpuran 75.9196)
- **Original**: %$ 4 # 4 64 # ## # #### ### ## ### कक क्क्कऋऋऊऋ कक आ श्रीकृष्णने कहा--तुम सब लोग इस
- **Translation**: 

---

### Verse 10 (Vaivtpuran 75.9197)
- **Original**: बहती रहती है। मेरी आज्ञासे ही आग जलती समय मेरे धाममें पधारे हो। यहाँ तुम्हारा स्वागत
- **Translation**: 

---

### Verse 11 (Vaivtpuran 75.9198)
- **Original**: और सूर्य तपते हैं। देवताओ! मेरी आज्ञासे ही है, स्वागत है। शिवके आश्रयमें रहनेवाले
- **Translation**: 

---

### Verse 12 (Vaivtpuran 75.9199)
- **Original**: सब शरीरोंमें रोग निवास करते हैं। समस्त लोगोंका तो कुशल पूछना उचित नहीं है। यहाँ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 75.9200)
- **Original**: प्राणियोंमें मृत्युका संचार होता है तथा वे समस्त आकर तुम निश्चिन्त हो जाओ। मेरे रहते तुम्हें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 75.9201)
- **Original**: जलधर वर्षा करते हैं। मेरे शासनसे ही ब्राह्मण क्या चिन्ता है? मैं समस्त जीवॉके भीतर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 75.9202)
- **Original**: ब्राह्मणत्वमें, तपोधन तपस्यामें, ब्रह्मर्षि ब्रह्ममें और बिराजमान हूँ; परंतु स्तुतिसे ही प्रत्यक्ष होता हूँ।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 75.9203)
- **Original**: योगी योगमें निष्ठा रखते हैं। वे सब-के-सब मेरे तुम्हारा जो अभिप्राय है, वह सब मैं निश्चितरूपसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 75.9204)
- **Original**: भयसे भीत होकर ही स्वधर्म-कर्मके पालनमें जानता हूँ। देवताओ! शुभ-अशुभ जो भी कर्म
- **Translation**: 

---

### Verse 18 (Vaivtpuran 75.9205)
- **Original**: तत्पर हैं। जो मेरे भक्त हैं वे सदा निःशड्ढ रहते हैं; है, वह समयपर ही होगा। बड़ा और छोटा--
- **Translation**: 

---

### Verse 19 (Vaivtpuran 75.9206)
- **Original**: क्‍योंकि वे कर्मका निर्मुलन करनेमें समर्थ हैं। सब कार्य कालसे ही सम्पन्न होता है। वृक्ष। दे 4ताओ! मैं कालका भी काल हूँ। विधाताका अपने-अपने समयपर ही सदा फूलते और फलते
- **Translation**: 

---

### Verse 20 (Vaivtpuran 75.9207)
- **Original**: भी विधाता हूँ। संहारकारीका भी संहारक तथा हैं। समयपर ही उनके फल पकते हैं और
- **Translation**: 

---

