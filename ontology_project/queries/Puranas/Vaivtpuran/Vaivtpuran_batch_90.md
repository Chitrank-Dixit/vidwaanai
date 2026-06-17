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

### Verse 1 (Vaivtpuran 7.9533)
- **Original**: भयभीत हुए सूर्य आदि सभी ग्रह आकाशमें हैं तथा प्रवचनकुशल हैं। आपको रिझाना या
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.9534)
- **Original**: अपनी गतिके क्रमको लाँघकर मीन लग्नमें जा लाँघना कठिन ही नहीं, असम्भव है। आपके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.9535)
- **Original**: पहुँचे। शुभ और अशुभ सभी वहाँ एकत्र हो गये। निःश्वाससे वेदोंका प्राकट्य हुआ है; इसलिये आप
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.9536)
- **Original**: विधाताकी आज्ञासे एक मुहूर्तके लिये वे सभी उनके प्रादुर्भावमें हेतु हैं। सम्पूर्ण वेद आपके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.9537)
- **Original**: ग्रह प्रसन्नतापूर्वक ग्यारहवें स्थानमें जाकर वहाँ स्वरूप हैं। छन्‍्द आदि वेदाड़ भी आपसे भिन्न
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.9538)
- **Original**: सानन्द स्थित हो गये। मेघ वर्षा करने लगे। नहीं हैं। आप वेदवेत्ता और सर्वव्यापी हैं।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.9539)
- **Original**: ठंढी-ठंढी हवा चलने लगी। पृथ्वी अत्यन्त प्रसन्न ऐसा कहकर देवताओंने बारंबार उनको
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.9540)
- **Original**: थी। दसों दिशाएँ स्वच्छ हो गयी थीं। ऋषि, मनु, प्रणाम किया। उन सबके नेत्रोंमें हर्षक आँसू यक्ष, गन्धर्व, किन्नर, देवता ओर देवियाँ सभी छलक रहे थे। उन सबने फूलोंकी वर्षा की।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.9541)
- **Original**: प्रसन्न थे। अप्सराएँ नृत्य करने लगीं। गन्धर्वराज जो पुरुष प्रातः:काल उठकर (मूल श्लोकमें कहे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.9542)
- **Original**: और विद्याधरियाँ गीत गाने लगीं। नदियाँ सुखपूर्वक गये) बयालीस नामोंका पाठ करता है, वह
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.9543)
- **Original**: बहने लगीं। अग्निहोत्रकी अग्रियाँ प्रसत्नतापूर्वक श्रीहरिकी दृढ़भक्ति, दास्थभाव तथा मनोवाज्छित
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.9544)
- **Original**: प्रज्वलित हो उठीं। स्वर्ममें दुन्दुभियों और आनकोंकी फल पाता है*। मनोहर ध्वनि होने लगी। खिले हुए पारिजातके भगवान्‌ नारायण कहते हैं--इस प्रकार
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.9545)
- **Original**: पुष्पॉकी झड़ो लग गयीं। पृथ्वी नारीका रूप स्तुति सुनाकर देवतालोग अपने-अपने धामको
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.9546)
- **Original**: धारण करके स्वयं सूतिकागारमें गयी। वहाँ जय- चले गये। फिर जलकी यृष्टि होने लगी। सारी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.9547)
- **Original**: जयकार, शब्वनाद तथा हरिकीर्तनका शब्द गूँज मथुरा नगरी निश्चेष्ट होकर सो रही थी। मुने! वह
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.9548)
- **Original**: रहा था। इसी समय सती देवकी वहाँ गिर पड़ीं। रात्रि घोर अन्धकारसे व्याप्त थी। जब रातके सात
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.9549)
- **Original**: उनके पेटसे वायु निकल गयी और वहीं भगवान्‌ मुहूर्त निकल गये और आठवाँ उपस्थित हुआ,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.9550)
- **Original**: श्रीकृष्ण दिव्यरूप धारण करके देवकीके हृदयकमलके तब आधी रातके समय सर्वोत्कृष्ट शुभ लग्न कोशसे प्रकट हो गये। उनका शरीर अत्यन्त आया। वह वेदोंसे अतिरिक्त तथा दूसरोंके लिये
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.9551)
- **Original**: कमनीय और परम मनोहर था। दो भुजाएँ थीं। दुर्शेय लग्न था। उस लग्नपर केवल शुभ ग्रहोंकी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.9552)
- **Original**: हाथमें मुरली शोभा पा रही थी। कानोमें * देवा ऊचु:-- जगद्योनिरयोनिस्त्वमतन्तो व्यय एव च । ज्योतिःस्वरूपो हानघ: सगुणों निर्ुणों महान्‌
- **Translation**: 

---

