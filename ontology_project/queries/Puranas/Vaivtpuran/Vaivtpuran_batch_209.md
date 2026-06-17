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

### Verse 1 (Vaivtpuran 13.10322)
- **Original**: दाहिका शक्ति और पृथ्वीमें गन्‍्ध होती है; इसी तथा करोड़ों कन्दर्पोकी लावण्यलीलासे अलंकृत
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10323)
- **Original**: प्रकार तुममें मैं व्याप्त हूँ। जैसे कुम्हार मिट्टौके थे। उन्होंने पीताम्बर पहन रखा था। उनके मुख
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10324)
- **Original**: बिना घड़ा नहीं बना सकता तथा जैसे स्वर्णकार और नेत्रोंमें प्रसन्षता छा रही थी। उनके दोनों
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10325)
- **Original**: सुवर्णके बिना कदापि कुण्डल नहीं तैयार कर चरण मणोन्द्रसारनिर्धित मज्जीरकी झनकारसे अनुरक्ञित
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10326)
- **Original**: सकता; उसी प्रकार मैं तुम्हारे बिना सृष्टि करनेमें थे। हाथोंमें उत्तम रत्नॉके सारतत््वसे बने हुए
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10327)
- **Original**: समर्थ नहीं हो सकता। तुम सृष्टिकी आधारभूता केयूर और कंगन शोभा दे रहे थे। उत्तम हो और मैं अच्युत बीजरूप हूँ। साध्वि! जैसे मणियोंद्वारा रचित कान्तिमान्‌ कुण्डलोंसे उनके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10328)
- **Original**: आभूषण शरीरकी शोभाका हेतु है, उसी प्रकार गण्डस्थलकी अपूर्व शोभा हो रहो थी। मणिराज , तुम मेरी शोभा हो। जब मैं तुमसे अलग रहता
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10329)
- **Original**: डंदड + संक्षिप्त ब्रह्मवैवर्तपुराण * 5688 £888## 44444 44468 4 44464 4484 86% 44 ##% ## 8 कह # ऋऋ कर कर # # # कक कर 4: 4 % ह# 888 44444 44 हूँ, तब लोग मुझे कृष्ण (काला-कलूटा) कहते
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10330)
- **Original**: अधिक प्रिय है। ब्रह्मा, अनन्त, शिव, धर्म, नर- हैं और जब तुम साथ हो जाती हो तो वे ही
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10331)
- **Original**: नारायण ऋषि, कपिल, गणेश और कार्तिकेय भी लोग मुझे श्रीकृष्ण (शोभाशाली श्रीकृष्ण)-कौ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10332)
- **Original**: मेरे प्रिय हैं। लक्ष्मी, सरस्वती, दुर्गा, सावित्री, संज्ञा देते हैं। तुम्हीं श्री हो, तुम्हों सम्पत्ति हो
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10333)
- **Original**: प्रकृति-ये देवियाँ तथा देवता भी मुझे प्रिय हैं; और तुम्हीं आधारस्वरूपिणी हो। तुम सर्वशक्तिस्वरूपा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10334)
- **Original**: तथापि वे राधा नामका उच्चारण करनेवाले हो और मैं अविनाशी सर्वरूप हूँ। जब मैं
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10335)
- **Original**: प्राणियोंके समान प्रिय नहीं हैं। उपर्युक्त सब तेज:स्वरूप होता हूँ, तब तुम तेजोरूपिणी होती
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10336)
- **Original**: देवता मेंरे लिये प्राणके समान हैं; परंतु सती हो। जब मैं शरीररहित होता हूँ, तब तुम भी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10337)
- **Original**: राधे! तुम तो मेरे लिये प्राणोंसे भी बढ़कर हो। अशरीरिणी हो जाती हो। सुन्दरिं! मैं तुम्हारे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10338)
- **Original**: वे सब लोग भिन्न-भिन्न स्थानोंमें स्थित हैं; किंतु संयोगसे ही सदा सर्व-बीजस्वरूप होता हूँ। तुम
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10339)
- **Original**: तुम तो मेरे वक्ष:स्थलमें विराजमान हो। जो मेरी शक्तिस्वरूपा तथा सम्पूर्ण स्त्रियोंका स्वरूप धारण
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10340)
- **Original**: चतुर्भुज मूर्ति अपनी प्रियाको वक्ष:स्थलमें धारण करनेवाली हो। मेरा अड्र और अंश हो तुम्हारा करती है, वही मैं श्रीकृष्णस्वरूप होकर सदा स्वरूप है। तुम मूलप्रकृति ईश्वरी हो। वरानने!
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10341)
- **Original**: स्वयं तुम्हारा भार वहन करता हूँ। शक्ति, बुद्धि और ज्ञानमें तुम मेरे ही तुल्य हो। यों कहकर श्रीकृष्ण उस मनोरम शब्यापर जो नराधम हम दोनोंमें भेदबुद्धि करता है, उसका
- **Translation**: 

---

