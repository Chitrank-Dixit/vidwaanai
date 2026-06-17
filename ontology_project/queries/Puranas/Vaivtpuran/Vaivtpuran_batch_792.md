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

### Verse 1 (Vaivtpuran 543.14154)
- **Original**: कामासक्त नहुषने फिर बहुत-सी युक्तियोंके द्वारा और आसक्ति एवं मोहसे दूर रहता है। वह
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14155)
- **Original**: पुनः अपने उसी पापपूर्ण प्रस्तावको दुहराया। लोभवश स्वादिष्ट भोजन नहीं करता, स्त्रीका मुख तब शची बोलीं--हाय ! इस विवेकशून्य, नहीं देखता तथा ब्रतमें अटल रहकर किसी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14156)
- **Original**: कर्तव्याकर्तव्यको न जाननेबाले, मूढ़, कामातुर गृहस्थ पुरुषसे मनचाही भोज्य वस्तुके लिये
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14157)
- **Original**: पुरुषकी कितनी बातें आज मुझे सुननी पड़ेंगी! याचना भी नहीं करता। ब्रह्माजीने यही संन्यासियोंका कामने जिनके चित्तको चुरा लिया है, वे धर्म बताया है। बेटा! यह तुम्हें धर्मकी बात
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14158)
- **Original**: विवेकशून्य काममत्त कामी तथा मधुमत्त एवं बतायी है। अब तुम सुखपूर्वक अपने स्थानकों
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14159)
- **Original**: सुरामत्त मनुष्य अपनी मौतकों भी नहीं गिनते। जाओ। ऐसा कहकर मार्ममें मिली हुई इन्द्राणी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14160)
- **Original**: ओ मतवाले नरेश! आज मुझे छोड़ दे। मैं तेरे चुप हो रहीं और राजा नहुष गर्दन टेढ़ी करके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14161)
- **Original**: लिये माताके समान और रजस्वला हूँ। आज उनसे बोला। मेरी ऋतुका प्रथम दिन है। पहले दिन रजस्वला नहुषने कहा--देवि! तुमने जो कुछ कहा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14162)
- **Original**: स्त्री चाण्डालीके समान मानी जाती है। दूसरे है, वह सब उलटी बात है। यथार्थ वैदिक धर्म
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14163)
- **Original**: दिन म्लेच्छा और तीसरे दिन धोबिनके समान क्‍या है? यह मैं बताता हूँ, सुनो। सुरसुन्दरि!
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14164)
- **Original**: होती है। चौथे दिन वह अपने पतिके लिये शुद्ध इसमें संदेह नहीं कि सबको अपने कर्मोंका फल
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14165)
- **Original**: होती है; परंतु देवकार्य और पितृकार्यके लिये
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14166)
- **Original**: 616 न्‍] संक्षिप्त.ब्रह्मवैवर्तपुराण + %%$%$%$%%%5%%%%##%#####%######%ऋऊकऋककऋऋक्ऋ्क्कफककऋकऋऋऋऋकऋक्ऋककऋऋऊऋऋकऋुकऋऋकऋऋक ककऋक कक के वह उस दिन भी शुद्ध नहीं मानी जाती। दूसरेके । परमानन्दमय, परमात्मा एवं ईश्वर हैं। निर्गुण, लिये वह उस दिन असत्‌ शूद्राके समान होती
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14167)
- **Original**: निरीह, स्वतन्त्र, प्रकृतिसे परे, स्वेच्छामय परब्रह्म है। जो पहले दिन अपनी रजस्वला पत्नीके साथ
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14168)
- **Original**: हैं तथा भक्तोंपर अनुग्रह करनेके लिये ही शरीर समागम करता है, वह ब्रह्महत्याके चौथे अंशका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14169)
- **Original**: धारण करते हैं। उनके चिन्तनमें लगे और नेत्रोंसे भागी होता है, इसमें संशय नहीं है। वह पुरुष
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14170)
- **Original**: आनन्दके आँसू बहाते हुए गुरुदेवको शचीने देवकर्म तथा पितृकर्ममें सम्मिलित होने योग्य धरतीपर माथा टेककर प्रणाम किया। उस समय नहीं रह जाता। वह लोगोंमें अधम, निन्दित और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14171)
- **Original**: भक्तिके समुद्रमें मग्र हुई शची रोती और आँखोंसे अपयशका भागी समझा जाता है। जो दूसरे दिन
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14172)
- **Original**: आँसू बहाती थी। साथ हो वह शोक-सागरमें रजस्वला स्त्रीके साथ कामभावसे समागम करता
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14173)
- **Original**: भी डूब रही थी। भयभीत शची व्यथित-हृदयसे है, उसे अवश्य ही गो-हत्याका पाप लगता है।
- **Translation**: 

---

