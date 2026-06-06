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

### Verse 1 (Bramha 0.8341)
- **Original**: त्रिलोकी एकार्णबमग्न हो जाती है। तदनन्तर नीचेके समस्त पातालोंकों जलाना आरम्भ करते
- **Translation**: 

---

### Verse 2 (Bramha 0.8342)
- **Original**: भगवान्‌ विष्णुके निःश्वाससे प्रकट हुई बायु उन हैं। सातों पातालॉको भस्म कर डालनेके पश्चात्‌
- **Translation**: 

---

### Verse 3 (Bramha 0.8343)
- **Original**: मेघोंकों छिन्न-भिन्न कर देती है और सौ वर्षोंसे वह प्रचण्ड अग्नि भूमिपर पहुँचकर सम्पूर्ण
- **Translation**: 

---

### Verse 4 (Bramha 0.8344)
- **Original**: अधिक कालतक बहती रहतो है। फिर विश्वके भूमण्डलकों भी भस्म कर डालती है। फिर , आदिकारण, अनादि, अचिन्त्य एवं सर्वभूतमय भुवलोंक और स्वलॉकको जलाकर ज्वाला-
- **Translation**: 

---

### Verse 5 (Bramha 0.8345)
- **Original**: भूतभावन भगवान्‌ सम्पूर्ण वायुको पीकर एकार्णवके मालाओंके महान्‌ आवर्तके रूपमें वह दारुण
- **Translation**: 

---

### Verse 6 (Bramha 0.8346)
- **Original**: जलमें शेषनागकी शय्यापर आसीन होते हैं। ये अग्नि सब ओर चक्कर लगाने लगती है। उस । आदिकर्ता भगवान्‌ श्रीहरि ब्रह्माजीका रूप धारण
- **Translation**: 

---

### Verse 7 (Bramha 0.8347)
- **Original**: डड00 > संक्षिप्र ब्रह्मपुराण + करके शयन करते हैं। उस समय जनलोकके ! तप्त होकर सूख जाता है। रसका अपहरण होनेसे सनकादि सिद्ध उनकी स्तुति करते हैं और
- **Translation**: 

---

### Verse 8 (Bramha 0.8348)
- **Original**: सम्पूर्ण जल तेज:स्वरूप हो जाता है। इस प्रकार ब्रह्मलोकके मुमुक्ष उनका चिन्तन करते रहते हैं।
- **Translation**: 

---

### Verse 9 (Bramha 0.8349)
- **Original**: जब तेजसे आवृत होकर जल अग्निकी-सी अवस्थामें वे परमेश्वर अपनी मायामयी दिव्य योगनिद्राका
- **Translation**: 

---

### Verse 10 (Bramha 0.8350)
- **Original**: पहुँच जाता है, तब अग्नितत्व्सब ओर फैलकर आश्रय ले अपने ही वासुदेव नामक स्वरूपका
- **Translation**: 

---

### Verse 11 (Bramha 0.8351)
- **Original**: उस जलको सोख लेता है। उस समय सम्पूर्ण चिन्तन करते हैं। विप्रवरो! यह नैमित्तिक नामका
- **Translation**: 

---

### Verse 12 (Bramha 0.8352)
- **Original**: जगतूमें धीरे-धीरि आगकी लपटें फैल जाती हैं। प्रलय है। इसमें निमित्त यहों है कि उस समय
- **Translation**: 

---

### Verse 13 (Bramha 0.8353)
- **Original**: जब सारा जगत्‌ ऊपर-नीचे और इधर-उधर अग्निकी ब्रह्मरूपधारी श्रीहरि शयन करते हैं। जबतक
- **Translation**: 

---

### Verse 14 (Bramha 0.8354)
- **Original**: ज्वालाओंसे व्याप्त हो जाता है, तब अग्निके सर्वात्मा श्रीहरि जागते हैं, तबतक सारा जगत्‌
- **Translation**: 

---

### Verse 15 (Bramha 0.8355)
- **Original**: प्रकाशक गुण रूपको वायुतत्त्व अपनेमें लीन कर सचेष्ट रहता है और जब वे मायामयी शब्यापर
- **Translation**: 

---

### Verse 16 (Bramha 0.8356)
- **Original**: लेता है। सबके कारणस्वरूप वायुमें जब अग्निका शयन करते हैं, उस समय सारा जगत्‌ विलीन हो
- **Translation**: 

---

### Verse 17 (Bramha 0.8357)
- **Original**: प्रकाशक तत्त्व-रूप बिलीन हो जाता है, तब जाता है। ब्रह्माजीका जो सहस्न चतुर्युगका दिन ' रूपतन्मात्राके नष्ट हो जानेसे अग्नितत््व रूपहीन हो होता है, एकार्णवर्में शबन करनेपर उनकी उतनी
- **Translation**: 

---

### Verse 18 (Bramha 0.8358)
- **Original**: स्वयं ही शान्त हो जाता है। फिर वायु प्रचण्ड ही बड़ी रात्रि होती है। रात्रिके बाद जागनेपर
- **Translation**: 

---

### Verse 19 (Bramha 0.8359)
- **Original**: गतिसे चलने लगती है। तेजस्तत्त्वके बायुमें स्थित ब्रह्मरूपधारी अजन्मा श्रीविष्णु पुनः सृष्टि करते हैं,
- **Translation**: 

---

### Verse 20 (Bramha 0.8360)
- **Original**: हो जानेसे जगतूमें प्रकाश नहीं रह जाता। तब यह बात मैं पहले बतला चुका हूँ। यह कल्पका , वायुतत््व अपने उद्धव और लयस्थान आकाशका संहार, अन्तर प्रलय अथवा नैमित्तिक प्रलय कहा
- **Translation**: 

---

