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

### Verse 1 (Vaivtpuran 543.13554)
- **Original**: प्राकृत कहलाते हैं। प्राकृत शरीर सदा ही होती है। महेश्वर! यदि इनके बीज नष्ट हो जाये
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13555)
- **Original**: विनाशशील हैं। रुद्र आदि तुम्हारे अंश हैं और तो ये सब स्वतः नष्ट हो जाते हैं। चम्बल मन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13556)
- **Original**: विष्णुरूपधारी मेरे अंश। मेरे भी दो रूए ही पुण्य और पापका बीज है। शम्भो! सम्पूर्ण
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13557)
- **Original**: हैं>द्विभुज और चतुर्भुज। चतुर्भुज मैं हूँ और इन्द्रियॉंसहित मन मेरा अंश है। सबका जनक
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13558)
- **Original**: वैकुण्ठधाममें लक्ष्मी तथा पार्षदोंके साथ रहता जो अहंकार है, उसके अधिष्ठाता चेतन तुम हो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13559)
- **Original**: हूँ। द्विभुजरूपसे मैं श्रीकृष्ण कहलाता हूँ और और ये ब्रह्मा बुद्धिके अधिष्ठाता हैं। परब्रह्म
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13560)
- **Original**: गोलोकमें गोपियों तथा राधाके साथ निवास परमात्मा एक हैं। गुण-भेदसे हो सदा उसके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13561)
- **Original**: करता हूँ। भिन्न-भिन्न रूप होते हैं। वह ब्रह्मतत्त् एक
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13562)
- **Original**: जो ब्रह्मको ट्विविध बताते हैं, उनके मतमें होनेपर भी अनेक प्रकारका है। शिव! वह सगुण
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13563)
- **Original**: दो प्रधान तत्त्व हैं--नित्य पुरुष तथा नित्या प्रकृति भी है और निर्गुण भी। जो मायारूप उपाधिका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13564)
- **Original**: ईश्वरी। शिव! वे दोनों सदा परस्पर संयुक्त रहते आश्रय लेता है, वह सगुण और जो मायातीत
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13565)
- **Original**: हैं। वे ही सबके माता-पिता हैं। वे दोनों अपनी है, वह निर्गुण कहलाता है। भगवान्‌ स्वेच्छामय
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13566)
- **Original**: इच्छाके अनुसार कभी साकार और कभी निराकार हैं। वे अपनी इच्छासे ही विविध रूपोंमें प्रकट
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13567)
- **Original**: होते हैं। दोनों ही सर्वस्वरूप हैं। जैसे पुरुषकी होते हैं। उनकी इच्छाशक्तिका ही नाम प्रकृति
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13568)
- **Original**: नित्य प्रधानता है, उसी तरह प्रकृतिकों भी है। है। वह नित्यस्वरूपा और सदा सबकी जननी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13569)
- **Original**: शम्भो! यदि तुम सतीको पाना चाहते हो तो है। कुछ लोग ज्योति:स्वरूप सनातन ब्रह्मको एक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13570)
- **Original**: प्रकृतिका स्तबन करो। तुमने पूर्वकालमें दुर्वासाकों ही बताते हैं तथा कुछ दूसरे विद्वान्‌ उसे प्रकृतिसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13571)
- **Original**: प्रसन्नतापूर्वक जिस स्तोत्रका उपदेश दिया था, युक्त होनेके कारण ट्विविध कहते हैं। जो एक
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13572)
- **Original**: वह दिव्य है और उसका कण्वशाखामें वर्णन बताते हैं, उनका मत सुनो। ब्रह्म माया तथा किया गया है। तुम उसीके द्वारा जगदम्बाकी जीवात्मा दोनोंसे परे है। उस ब्रह्मसे ही वे दोनों
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13573)
- **Original**: आराधना करो। शिव! मेरे आशीर्वादसे तुम्हारे (माया और जीवात्मा) प्रकट होते हैं; अत: ब्रह्म शोकका नाश हो। तुम्हें कल्याणको प्राप्ति हो और ही सबका कारण है। वह परब्रह्म एक होकर [ तुम्हारे लिये विप्लवका कारण बना हुआ पत्नीके भी स्वेच्छासे दो हो जाता है। उसकी इच्छाशक्ति
- **Translation**: 

---

