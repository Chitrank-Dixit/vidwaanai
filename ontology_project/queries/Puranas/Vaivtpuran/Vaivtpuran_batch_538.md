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

### Verse 1 (Vaivtpuran 35.7862)
- **Original**: ही जीवन्मुक्त, सर्वज्ञ, सम्पूर्ण सिद्धियोंका स्वामी रक्षा करे। '30 महेश्वराय रुद्राय नमः' सदा मेरे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 35.7863)
- **Original**: और मनके समान वेगशाली हो जाता है। इस नितम्बकी रक्षा करे। “30 ह्रीं श्रीं भूतनाथाय
- **Translation**: 

---

### Verse 3 (Vaivtpuran 35.7864)
- **Original**: कबचको बिना जाने जो भगवान्‌ शंकरका भजन स्वाहा' सदा पैरोंकी रक्षा करें। '3 सर्वेश्वराय
- **Translation**: 

---

### Verse 4 (Vaivtpuran 35.7865)
- **Original**: करता है, उसके लिये एक करोड़ जप करनेपर भी सर्वाय स्वाहा' सदा सर्वाड्गकी रक्षा करे। पूर्वमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 35.7866)
- **Original**: मन्त्र सिद्धिदायक नहीं होता।* (अध्याय 35) “0: 00“ 09#%9%005.....00 * नारायण उवाच- कवच शृृणु विप्रेन्न शंकरस्थ महात्मनः । ब्रह्माण्डविजयं नाम सर्वावियवरक्षणम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 35.7867)
- **Original**: पुरा दुर्वाससा दत्त मत्स्यराजायः धीमते । दत्वा पड़क्षर॑ मन्त्र. सर्वपापप्रणाशनम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 35.7868)
- **Original**: स्थिते च कवचे देहे नास्ति मृत्युश्व जीविनाम्‌ू । अस्त्रे शस्त्रे जले वहाँ सिद्धिश्रेन्नास्ति संशय:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 35.7869)
- **Original**: यद्‌ धृत्वा पठनातू सिद्धों दुर्वासा विश्वपूजित:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 35.7870)
- **Original**: जैगीषव्यों महायोगी पठनाद्‌ धारणाद्‌ यतः
- **Translation**: 

---

### Verse 10 (Vaivtpuran 35.7871)
- **Original**: यद्‌ धृत्वा वामदेयश्ष देवलश्च्यवनः: स्वयम्‌ । आग्त्यक्ष पुलस्त्यक्ष बभूवष विश्वपूणित:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 35.7872)
- **Original**: नमः शिवायेति च मस्तक॑ मे सदाउवतु । 3 नमः शिवायेति च स्वाहा भाल॑ सदा5वतु
- **Translation**: 

---

### Verse 12 (Vaivtpuran 35.7873)
- **Original**: हीं शिवायेति स्वाहा नेत्रे सदाउवतु । 3 हीं क्लीं हूं शिवायेति नमो मे पातु नासिकाम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 35.7874)
- **Original**: नमः शिवाय शान्ताय स्वाहा कण्ठं सदाउवतु । 3 हों अ्रीं हूं संहारकर्त्रे स्वाहा कर्णी सदाउवतु
- **Translation**: 

---

### Verse 14 (Vaivtpuran 35.7875)
- **Original**: हीं श्रीं पश्॒वक्‍्त्राय स्वाहा दन्त॑ सदाउवतु । <& हीं महेशाय स्वाहा चाधरं पातु मे सदा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 35.7876)
- **Original**: हां श्रों क्लों त्रिनेत्राय स्वाहा केशान्‌ सदाउवतु । <*# हीं
- **Translation**: 

---

### Verse 16 (Vaivtpuran 35.7877)
- **Original**: * गणपतिखण्ड * 373 8/![[][
- **Translation**: 

---

### Verse 17 (Vaivtpuran 35.7878)
- **Original**: 44 44:32 एइए-*" अफखख अफष््न्न्न्ग्न्ण ।00000020]])0 0 4 4 4 4 4
- **Translation**: 

---

### Verse 18 (Vaivtpuran 35.7879)
- **Original**: नि न [([[8][48 8 4 00040. मत्स्थराजके बधके पश्चात्‌ अनेकों राजाओंका आना और परशुरामद्वारा मारा जाना, : राजा और परशुरामका युद्ध, परशुरामद्वारा कालीस्तवन, ब्रह्माका पाकर परशुरामको युक्ति बताना, परशुरामका राजा सुचन्दठसे मन्त्र और कबच माँगकर उसका वध करना श्रीनारायण कहते हैं--नारद! युद्धमें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 35.7880)
- **Original**: । परशुराम बोले--आप शंकरजीकी प्रियतमा मत्स्यराजके गिर जानेपर महाराज कार्तवीर्यके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 35.7881)
- **Original**: पत्नी हैं, आपको नमस्कार है। सारस्वरूपा आपको भेजे हुए बृहद्वल, सोमदत्त, विदर्भ, मिथिलेश्वर,
- **Translation**: 

---

