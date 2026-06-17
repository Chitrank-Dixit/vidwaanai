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

### Verse 1 (Vaivtpuran 36.8022)
- **Original**: यह समस्त मन्त्रसमुदायका मूर्तिमान्‌ स्वरूप है। श्री नारायणेशायै स्वाहा' सदा मेरे कण्ठकौ रक्षा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 36.8023)
- **Original**: धर्मात्मा पुरुष ब्राह्मणको मेरुके समान सुवर्णका करे। '3& श्रीं केशवकान्तायै स्वाहा' सदा मेरे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 36.8024)
- **Original**: पहाड़ दान करके जो फल पाता है, उससे कहाँ कंधोंकी रक्षा करें। '37 श्रीं पढानिवासिन्यै
- **Translation**: 

---

### Verse 4 (Vaivtpuran 36.8025)
- **Original**: अधिक फल इस कबचसे मिलता है। जो मनुष्य स्वाहा' सदा नाभिकीौ रक्षा करे। '& हीं श्रीं
- **Translation**: 

---

### Verse 5 (Vaivtpuran 36.8026)
- **Original**: विधिवत्‌ गुरुकी अर्चना करके इस कवचकों संसारमात्रे स्वाहा' सदा मेरे वक्षःस्थलकी रक्षा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 36.8027)
- **Original**: गलेमें अथवा दाहिनी भुजापर धारण करता है, करे। '3 श्रीं श्रीं कृष्णकान्तायै स्वाहा' सदा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 36.8028)
- **Original**: वह प्रत्येक जन्ममें श्रीसम्पन्न होता है और उसके पीठकी रक्षा करे। 5» हीं श्रीं श्रिय स्वाहा'
- **Translation**: 

---

### Verse 8 (Vaivtpuran 36.8029)
- **Original**: घरमें लक्ष्मी सौ पीढ़ियोंतक निश्वलरूपसे निवास सदा मेरे हाथोंकी रक्षा करे। ' 3» श्रीं निवासकान्तायै
- **Translation**: 

---

### Verse 9 (Vaivtpuran 36.8030)
- **Original**: करती हैं। वह देवेन्धों तथा राक्षसराजोंद्वारा निश्चय स्वाहा' सदा मेरे पैरोंकी रक्षा करे। '3» हीं श्रीं
- **Translation**: 

---

### Verse 10 (Vaivtpuran 36.8031)
- **Original**: ही अवध्य हो जाता है। जिसके गलेमें यह कबच क्लीं भ्रियै स्वाहा' मेरे सर्वाड्रकी रक्षा करे। पूर्व
- **Translation**: 

---

### Verse 11 (Vaivtpuran 36.8032)
- **Original**: विद्यमान रहता है, उस बुद्धिमानने सभी प्रकारके दिशामें 'महालक्ष्मी' और अग्रिकोणमें 'कमलालया'
- **Translation**: 

---

### Verse 12 (Vaivtpuran 36.8033)
- **Original**: पुण्य कर लिये, सम्पूर्ण यज्ञोमें दीक्षा ग्रहण कर मेरी रक्षा करें। दक्षिणमें ' पद्मा' और नैरत्यकोणमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 36.8034)
- **Original**: ली और समस्त तीथर्थोमें स्नान कर लिया। लोभ, * श्रीहरिप्रिया' मेरी रक्षा करें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 36.8035)
- **Original**: पश्चिममें 'पद्मालया'
- **Translation**: 

---

### Verse 15 (Vaivtpuran 36.8036)
- **Original**: मोह और भयसे भी इसे जिस-किसीको नहीं और वायबव्यकोणमें स्वयं 'श्री' मेरी रक्षा करें। देना चाहिये; अपितु शरणागत एवं गुरुभक्त उत्तरमें 'कमला' और ईशानकोणमें 'सिन्धुकन्यका '
- **Translation**: 

---

### Verse 16 (Vaivtpuran 36.8037)
- **Original**: शिष्यके सामने ही प्रकट करना चाहिये। इस रक्षा करें। ऊर्ध्वभागमें 'नारायणेशी' रक्षा करें।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 36.8038)
- **Original**: कवचका ज्ञान प्राप्त किये बिना जो जगज्जननी अधोभागमें 'विष्णुप्रिया' रक्षा करें। 'विष्णुप्राणाधिका '
- **Translation**: 

---

### Verse 18 (Vaivtpuran 36.8039)
- **Original**: लक्ष्मीका जप करता है, उसके लिये करोड़ोंकी सदा सब ओरसे मेरी रक्षा करें। संख्यामें जप करनेपर भी मन्त्र सिद्धिदायक नहीं बत्स! इस प्रकार मैंने तुमसे इस सर्व श्चर्यप्रद
- **Translation**: 

---

### Verse 19 (Vaivtpuran 36.8040)
- **Original**: होता।* (अध्याय 38) >+>थेए9-000 * नारायण उचाच प्रजापति:। ऋषिश्छन्द्व॒ बृहती देवी पद्मालया स्वयम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 36.8041)
- **Original**: प्रकीरततिंत: । पुण्यवीज॑ च महतां कवच श्रीं मे पातु कपाल॑ च लोचने श्रीं ब्रिये नम:
- **Translation**: 

---

