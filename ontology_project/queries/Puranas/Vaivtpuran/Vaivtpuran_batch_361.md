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

### Verse 1 (Vaivtpuran 17.954)
- **Original**: फिर मेरे पुत्रके रूपमें प्रतिष्ठित हो जायँगे। प्राणियोंके लिये परम कल्याणकारक थी।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 17.955)
- **Original**: भूतलपर उनके रहनेका जो समय नियत था, ब्राह्मण बोले--देवताओ ! यह उपबर्हणकी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 17.956)
- **Original**: उसका कुछ भाग अभी शेष है। उसके अनुसार भार्या और चित्ररथकी कन्या है। पतिशोकसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 17.957)
- **Original**: इस समय इनकी आयु अभी एक सहस्न वर्षतक पीड़ित होकर इसने स्वामीके जीवनदानके लिये
- **Translation**: 

---

### Verse 5 (Vaivtpuran 17.958)
- **Original**: और बाकी है। मैं स्वयं भगवान्‌ विष्णुकी कृपासे याचना की है । अब इस कार्यके लिये निश्चितरूपसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 17.959)
- **Original**: उपबर्हणको जीवन-दान दूँगा। जिससे इस ...._ उपायका अवलम्बन करना चाहिये? सब
- **Translation**: 

---

### Verse 7 (Vaivtpuran 17.960)
- **Original**: देवसमुदायकों शापका स्पर्श न हो, वह उपाय मैं देवता मिलकर मुझे बह उपाय बतायें, जो सदा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 17.961)
- **Original**: अवश्य करूँगा। ब्रह्म! आपने जो यह कहा कि काममें लाने योग्य और समयोचित हो।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 17.962)
- **Original**: यहाँ भगवान्‌ विष्णु क्‍यों नहीं आये, सो ठीक नहीं मालावती श्रेष्ठ सती एवं तेजस्बिनी है। वह
- **Translation**: 

---

### Verse 10 (Vaivtpuran 17.963)
- **Original**: है; क्योंकि भगवान्‌ विष्णु तो सर्वत्र विद्यमान हैं। अपना मनोस्थ सफल न होनेपर समस्त देवताओंको
- **Translation**: 

---

### Verse 11 (Vaivtpuran 17.964)
- **Original**: वे ही सबके आत्मा हैं। आत्माका पृथक्‌ शरीर शाप देनेके लिये उद्यत है। अत: आप लोगोंके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 17.965)
- **Original**: कहाँ होता है? वे स्वेच्छामय परब्रह्म परमात्मा कल्याणके लिये मैं यहाँ आया हूँ और मैंने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 17.966)
- **Original**: भक्तोंपर अनुग्रह करनेके लिये ही दिव्य शरीर सतीको समझा-बुझाकर शान्त किया है। सुना
- **Translation**: 

---

### Verse 14 (Vaivtpuran 17.967)
- **Original**: धारण करते हैं। वे सनातनदेव सर्वत्र हैं, सर्वज्ञ है, आप लोगोंने श्वेतद्वीपमें श्रीहरिकी भी स्तुति
- **Translation**: 

---

### Verse 15 (Vaivtpuran 17.968)
- **Original**: हैं और सबको देखते हैं।“विष्‌' धातु व्यापतिवाचक की थी; परंतु आप लोगोंके वे स्वामी भगवान्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 17.969)
- **Original**: है और “णु' का अर्थ सर्वत्र है। वे सर्वात्मा श्रीहरि विष्णु यहाँ आये कैसे नहीं? आकाशवाणी हुई
- **Translation**: 

---

### Verse 17 (Vaivtpuran 17.970)
- **Original**: सर्वत्र व्यापक हैं; इसलिये विष्णु कहे गये हैं। थी कि तुम लोग चलो, पीछेसे भगवान्‌ विष्णु
- **Translation**: 

---

### Verse 18 (Vaivtpuran 17.971)
- **Original**: कोई अपवित्र हो या पवित्र अथवा किसी भी भी जायँंगे। आकाशवाणीकी बात तो अटल
- **Translation**: 

---

### Verse 19 (Vaivtpuran 17.972)
- **Original**: अब्स्थामें क्यों न हो, जो कमलनयन भगवान्‌ होती है; फिर वह विपरीत कैसे हो गयी?
- **Translation**: 

---

### Verse 20 (Vaivtpuran 17.973)
- **Original**: विष्णुका स्मरण करता है, वह बाहर-भीतरसहित ब्राह्मणकी यह बात सुनकर साक्षात्‌ जगदुरु
- **Translation**: 

---

