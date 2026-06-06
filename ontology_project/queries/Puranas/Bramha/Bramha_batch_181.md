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

### Verse 1 (Bramha 0.3601)
- **Original**: चृद्धाने कहा--पूर्वकालमें ही आप मेरे पति 5
- **Translation**: 

---

### Verse 2 (Bramha 0.3602)
- **Original**: नियत कर दिये गये हैं। अब दूसरा कोई मेरा पति (]
- **Translation**: 

---

### Verse 3 (Bramha 0.3603)
- **Original**: [अं से आका; विधाताने आपको मुझे दिया है; अतः अब आप मुझे अस्वीकार न करें। मुझमें कोई दोष नहीं है। मैं आपमें भक्ति रखती हूँ; तब ्। !
- **Translation**: 

---

### Verse 4 (Bramha 0.3604)
- **Original**: भी यदि आप मुझे ग्रहण करना नहीं चाहते तो
- **Translation**: 

---

### Verse 5 (Bramha 0.3605)
- **Original**: आपके देखते-देखते अभी अपने प्राण त्याग दूँगी। 6058 71
- **Translation**: 

---

### Verse 6 (Bramha 0.3606)
- **Original**: यदि अभीष्ट वस्तुकी प्राप्ति न हो तो प्राणियोंकि लिये वृद्धाने कहा--आर्टिपेणके प्रिय पुत्र ऋतध्वज
- **Translation**: 

---

### Verse 7 (Bramha 0.3607)
- **Original**: मर जाना ही अच्छा है। प्रेमीजनके परित्यागसे जो पक रा हो हे; 'क हिल थे" चुकी ला: चुतकर गौठपने कहा-बु - तत्पर । एक हैं बाठ सुनकर कहा-- शिकार खेलनेके लिये वनमें आये और इसी !न तपस्या है न विद्या। मैं कुरूप और निर्धन हूँ,
- **Translation**: 

---

### Verse 8 (Bramha 0.3608)
- **Original**: *» सुपणा-संगम, पुरूरवस्तीर्थ, पञ्मतीर्थ, शमीतीर्भ, सोम आदि तीर्थोंकी महिमा « 175 अतः तुम्हारे लिये योग्य बर नहीं हो सकता।
- **Translation**: 

---

### Verse 9 (Bramha 0.3609)
- **Original**: अगस्त्यकी यह बात सुनकर गौतम उस पहले सुन्दर रूप और उत्तम विद्याकी प्राप्ति करके
- **Translation**: 

---

### Verse 10 (Bramha 0.3610)
- **Original**: बृद्धाके साथ गौतमी:तटपर गये और कठोर मुझे तुम्हारी बात माननी चाहिये।' तपस्था करने लगे। उन्होंने भगवान्‌ शंकर और यृद्धाने कहा--ब्रह्मन्‌! मैंने अपनी तपस्यासे
- **Translation**: 

---

### Verse 11 (Bramha 0.3611)
- **Original**: विष्णुकां स्तवन किया तथा पलीके लिये गज्जाजीको सरस्वतीदेवीको संतुष्ट किया है, साथ ही रूप
- **Translation**: 

---

### Verse 12 (Bramha 0.3612)
- **Original**: भी संतुष्ट किया। देनेवाले अग्नि भी मुझपर प्रसन्न हैं; अत: बागीश्वरी
- **Translation**: 

---

### Verse 13 (Bramha 0.3613)
- **Original**: गौतम बोले--शिव ! जिनका हृदय व्यधित देवी आपको विद्या देंगी और रूपवान्‌ अग्निदेव
- **Translation**: 

---

### Verse 14 (Bramha 0.3614)
- **Original**: है, ऐसे पुरुषोंके लिये संसारमें पार्वतीसहित आप रूप प्रदान करेंगे। ही शरण हैं-ठीक वैसे ही, जिस प्रकार मरुभूमिके यों कहकर बृद्धाने सरस्वती और अग्निकी
- **Translation**: 

---

### Verse 15 (Bramha 0.3615)
- **Original**: पथिकोंके लिये वृक्ष ही आश्रय होता है। भगवान्‌ प्रार्था करके गौतमको विद्वान्‌ और सुरूपवान्‌ बना
- **Translation**: 

---

### Verse 16 (Bramha 0.3616)
- **Original**: श्रीकृष्ण! आप ही छोटे-बड़े सब भूतोंके पापोंका दिया। तब उन्होंने बड़ी प्रसन्नताके साथ वृद्धाको
- **Translation**: 

---

### Verse 17 (Bramha 0.3617)
- **Original**: सर्वधा निवारण करनेवाले हैं, जैसे सूखती हुई अपनी पत्नी बनाया और कितने ही वर्षोतक उसके
- **Translation**: 

---

### Verse 18 (Bramha 0.3618)
- **Original**: खेतीको मेघ ही सींचकर हरा-भरा करता है। साथ विहार किया। एक दिन वसिष्ट और वामदेव
- **Translation**: 

---

### Verse 19 (Bramha 0.3619)
- **Original**: सुधामयी तरक्षलेंसे सुशोभित गौतमी ! तुम वैकुण्ठरूपी आदि महर्षि पुण्यतीर्थो्में भ्रमण करते हुए उस
- **Translation**: 

---

### Verse 20 (Bramha 0.3620)
- **Original**: दुर्गमें पहुँचनेके लिये सीढ़ी हो। हम अधोगतिमें गुफामें आये। गौतम और उनकी पत्लीने वहाँ आये
- **Translation**: 

---

