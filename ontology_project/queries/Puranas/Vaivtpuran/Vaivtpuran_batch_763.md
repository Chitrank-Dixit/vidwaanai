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

### Verse 1 (Vaivtpuran 543.13574)
- **Original**: वियोगका यह रोग दूर हो जाय। ही प्रकृति है, जो सदा सम्पूर्ण शक्तियोंकी जननी गिरिराज! ऐसा कहकर लक्ष्मीपति भगवान्‌ होती है। उससे संयुक्त होनेके कारण वे परमात्मा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13575)
- **Original**: विष्णु चुप हो गये। तदनन्तर महेश्वरने प्रकृतिके 'सगुण' कहे जाते हैं। वे ही सबके आधार, स्तवनका कार्य आरम्भ किया। उन्होंने स्नान करके सनातन, सर्वे श्वर, सर्वसाक्षी तथा सर्वत्र फलदाता
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13576)
- **Original**: श्रीकृष्ण और ब्रह्माको भक्तिपूर्वक हाथ जोड़ होते हैं। शम्भो! शरीर भी दो प्रकारका होता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13577)
- **Original**: नमस्कार किया। उस समय उनका अद्भ-अज्जञ है--एक नित्य और दूसरा प्राकृत। नित्य शरीरका
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13578)
- **Original**: पुलकित हो उठा था। विनाश नहीं होता; परंतु प्राकृत शरीर सदा नश्वर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13579)
- **Original**: . महेश्वर बोले--' 5» नमः प्रकृत्यै' होता है। भगवन्‌! हम दोनोंके शरीर नित्य हैं। 35% (सच्विदानन्दमयी) प्रकृतिदेवीको हमारे अंशभूत जो अन्य जीव हैं, उनके शरीर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13580)
- **Original**: नमस्कार है। त्रिगुणात्मिका प्रकृतिसे उत्पन्न होनेके कारण। ब्राहि! तुम ब्रह्मस्वरूपिणी हो। सनातनि!
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13581)
- **Original**: » भ्रीकृष्णजन्मखण्ड « 75 अ####### ## ###### $ 45 $$# *%# 4 ऊ कक 1 4 ## # ## ## $# # 4 # 4 44 ## # # % $ % 4 5 % % 5 % 55 $ 4 #£ 54 8 % 4 4 परमात्मस्वरूंपे! परमानन्दरूपिणि! तुम मुझपर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13582)
- **Original**: यशस्वियोंसे पूजित और यशकी निधि हो; मेरे प्रसन्न हो जाओ। भद्रे! तुम भद्र अर्थात्‌ कल्याण
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13583)
- **Original**: ऊपर कृपा करो। देवि! तुम समस्त जगत्‌ एवं प्रदान करनेवाली हो। दुर्गे! तुम दुर्गम संकटका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13584)
- **Original**: रत्रोंकी आधारभूता वसुन्धरा हो, चर और निवारण तथा दुर्गतिका नाश करनेवाली हो।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13585)
- **Original**: अचरस्वरूपा हो; मुझपर शीघ्र ही प्रसन्न होओ। भवसागरसे पार उतारनेके लिये नूतन एवं सुदृढ़
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13586)
- **Original**: सिद्धयोगिनि! तुम योगस्वरूपा, योगियोंकी स्वामिनी, नौकास्वरूपिणी देवि! मुझपर कृपा करो। सर्वस्वरूपे !
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13587)
- **Original**: योगको देनेवाली, योगकी कारणभूता, योगकी सर्वे श्रि! सर्वबीजस्वरूपिणि ! सर्वाधारे! सर्वविद्ये !
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13588)
- **Original**: अधिष्ठात्री देवी और देवियोंकी ईश्वरी हो; मेरे विजयप्रदे! मुझपर प्रसन्न होओ। सर्वमड्जले! तुम
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13589)
- **Original**: ऊपर कृपा करो। सिद्धेश्वरि! तुम सम्पूर्ण सिद्धिस्वरूपा, सर्वमड्रलरूपा, सभी मड्गलोंको देनेबाली तथा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13590)
- **Original**: समस्त सिद्धियोंको देनेवाली तथा सभी सिद्धियोंका सम्पूर्ण मज़लॉंकी आधारभूता हो; मेरे ऊपर कृपा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13591)
- **Original**: कारण हो; मुझपर प्रसन्न होओ। महे धरि ! विभिन्न करो। भक्तवत्सले ! तुम निद्रा, तन्द्रा, क्षमा, श्रद्धा,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13592)
- **Original**: मतोंके अनुसार जो समस्त शास्त्रोंका व्याख्यान तुष्टि, पुष्टि, लज्जा, मेधा और बुद्धिरूपा हो; मुझपर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13593)
- **Original**: है, उसका तात्पर्य तुम्हीं हो। ज्ञानस्वरूपे परमे श्वरि ! प्रसन्न होओ। वेदमात: ! तुम वेदस्वरूपा, वेदोंका
- **Translation**: 

---

