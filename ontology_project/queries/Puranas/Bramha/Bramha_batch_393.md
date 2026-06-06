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

### Verse 1 (Bramha 0.7841)
- **Original**: करनेकी प्रवृत्ति और कटुबचन बोलनेका स्वभाव वह गुस्के विपरीत कोई आचरण न करे। उन्होंकी
- **Translation**: 

---

### Verse 2 (Bramha 0.7842)
- **Original**: होना अच्छा नहीं माना गया है। जो गृहस्थ इस आज्ञसे उनके सामने बैठकर एकाग्रचित्तसे वेदका
- **Translation**: 

---

### Verse 3 (Bramha 0.7843)
- **Original**: प्रकार उत्तम विधिका पालन करता है, वह सब अध्ययन करे। गुरुका आदेश मिलनेपर भिक्षाका अन्न
- **Translation**: 

---

### Verse 4 (Bramha 0.7844)
- **Original**: प्रकारके बन्धनोंसे मुक्त हो उत्तम लोकोंमें जाता है। ऋण करे। जब आचार्य पहले स्नान कर लें तो स्वयं
- **Translation**: 

---

### Verse 5 (Bramha 0.7845)
- **Original**: गृहस्थ पुरुष बुढ़ापा आनेपर अपनी स्त्रीका भार जलमें प्रवेश कस्के अवगाहन करे। प्रतिदिन प्रात:-
- **Translation**: 

---

### Verse 6 (Bramha 0.7846)
- **Original**: पुत्रॉंको सौंप दे और स्वयं तपस्याके लिये बनमें काल आचार्यके लिये समिधा और जल आदि ले
- **Translation**: 

---

### Verse 7 (Bramha 0.7847)
- **Original**: चला जाय अथवा स्त्रीको भी साथ ही लेता जाय। आये। जब ग्रहण करनेके योग्य वेदोंका पूर्णरूपसे
- **Translation**: 

---

### Verse 8 (Bramha 0.7848)
- **Original**: वहाँ पत्तियाँ, मूल और फल आदिका आहार करते अध्ययन कर ले, तब विद्वान्‌ पुरुष गुरदक्षिणा देकर
- **Translation**: 

---

### Verse 9 (Bramha 0.7849)
- **Original**: हुए पृथ्वीपर शयन करे। सिरके बाल, दाढ़ी और गुरुकी आज्ञा ले गृहस्थाश्रमें प्रवेश करे। मूँछ न कटाये। वानप्रस्थ मुनिके लिये सब लोग विधिपूर्वक योग्य स्त्रीसे बिबाह करके अपने
- **Translation**: 

---

### Verse 10 (Bramha 0.7850)
- **Original**: अतिथि हैं। बह मृगचर्म, कास और कुश आदिकी वर्णोचित कर्मद्वारा धनका उपार्जन करे और
- **Translation**: 

---

### Verse 11 (Bramha 0.7851)
- **Original**: कौपीन एवं चादर धारण करें। उसके लिये तीनों उसीसे यथाशक्ति गृहस्थका सारा कार्य पूर्ण करे।
- **Translation**: 

---

### Verse 12 (Bramha 0.7852)
- **Original**: समय स्तान करना उत्तम माना गया है। देवपूजन, श्राद्धके द्वारा पितरों, यज्ञद्वारा देवताओं, अन्नसे
- **Translation**: 

---

### Verse 13 (Bramha 0.7853)
- **Original**: होम, सम्पूर्ण अतिथियोंका पूजन, भिक्षा और अतिथियों, स्वाध्यायसे मुनियों, संतानोत्पादनसे ! प्राणियोंकों बलि-समर्पण--ये सब बातें वानप्रस्थके प्रजापति, बलिवैश्वदेवसे सम्पूर्ण भूतों और सत्यवचनके
- **Translation**: 

---

### Verse 14 (Bramha 0.7854)
- **Original**: लिये श्रेष्ठ मानी गयो हैं। वह अपने शरीरमें जंगलो द्वारा सम्पूर्ण जगत्‌का पूजन करें। ऐसा करनेवाला
- **Translation**: 

---

### Verse 15 (Bramha 0.7855)
- **Original**: फल आदिके तेल लगा सकता है। उसका मुख्य पुरुष अपने कर्माँद्वारा उपार्जित उत्तम लोकोंमें , कर्तव्य है तपस्था--शीत और उष्ण आदि द्वद्दोंका जाता है। भिक्षापर निर्वाह करनेवाले संन्‍्यासी और
- **Translation**: 

---

### Verse 16 (Bramha 0.7856)
- **Original**: सहन। जो वानप्रस्थ मुनि नियमपूर्वक रहकर पूर्वोक्त ब्रह्मचारी भी गृहस्थोंके ही अबलम्बसे रहते हैं,
- **Translation**: 

---

### Verse 17 (Bramha 0.7857)
- **Original**: रूपसे अपने कर्तव्यका पालन करता है, वह अत: गार्हस्थ्य-आश्रम श्रेष्ठ माना गया है। जो
- **Translation**: 

---

### Verse 18 (Bramha 0.7858)
- **Original**: अग्निकी भाँति अपने सब दोषोंको जला देता और ब्राह्मण वेदाध्ययन, तीर्थस्नान और पृथ्वोके दर्शनके
- **Translation**: 

---

### Verse 19 (Bramha 0.7859)
- **Original**: सनातन लोकोंको प्राप्त होता है। लिये भूतलपर भ्रमण करते हैं, जिनका कोई घर
- **Translation**: 

---

### Verse 20 (Bramha 0.7860)
- **Original**: मुनियो! मनीषी पुरुष जो भिक्षुका चतुर्थ नहीं है, जो प्रायः निराहार रहते हैं और जहाँ
- **Translation**: 

---

