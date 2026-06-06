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

### Verse 1 (Vaivtpuran 13.10062)
- **Original**: इस समय श्रीकृष्णकी आज्ञासे यहाँ अयोनिसम्भवा ज्येष्ठ पुत्र॒का नाम जैसा मैंने सुना था, बैसा बताया
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10063)
- **Original**: होकर प्रकट हुई हैं। ये ही देवी मूल-प्रकृति है। नन्द! अब मैं अपने घरकों जाऊँगा। तुम
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10064)
- **Original**: ईश्वरी हैं। इन सती-साध्वी राधाने मायासे माताके अपने भवनमें सुखपूर्वक रहो। गर्भको वायुपूर्ण करके बरायुके निकलनेके समय ब्राह्मणणी यह बात सुनकर नन्‍्दजी स्त॒ब्ध
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10065)
- **Original**: स्वयं शिशु-विग्रह धारण कर लिया। ये साक्षात्‌ रह गये। नन्दपत्री भी निश्चेष्ट हो गयीं और वह
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10066)
- **Original**: कृष्ण-माया हैं और श्रीकृष्णके आदेशसे पृथ्वीपर बालक स्वयं हँसने लगा। तब नन्‍्दने गर्गजीको
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10067)
- **Original**: प्रकट हुई हैं। जैसे शुक्लपक्षमें चन्द्रमाकी कला प्रणाम करके दोनों हाथ जोड़ लिये और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10068)
- **Original**: बढ़ती है, उसी प्रकार ब्रजमें राधा बढ़ रहीं हैं। भक्तिभावसे मस्तक झुकाकर विनयपूर्वक कहा।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10069)
- **Original**: श्रीकृष्णके तेजके आधे भागसे वे मूर्तिमती हुई जन्‍्द बोले--ब्रह्मं! यदि आप चले गये
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10070)
- **Original**: हैं। एक ही मूर्ति दो रूपोंमें विभक्त हो गयी तो कौन महात्मा इस कर्मको करायेंगे; अत: आप
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10071)
- **Original**: है। इस भेदका निरूपण वेदमें किया गया है। स्वयं हो शुभ-दृष्टि करके इन बालकोंका [ये स्त्री हैं, वे पुरुष हैं, किंवा वे ही स्त्री हैं नामकरण एवं अन्नप्राशन-संस्कार कराइये। राधा-
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10072)
- **Original**: और ये पुरुष हैं। इसका स्पष्टीकरण नहीं हो बन्धुसे लेकर राधाप्राणाधिकतक जो नाम-समूह
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10073)
- **Original**: पाता। दो रूप हैं और दोनों ही स्वरूप, गुण बताये गये हैं, उनमें जो राधा नाम आया है,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10074)
- **Original**: एवं तेजकी दृष्टिसे समान हैं। पराक्रम, बुद्धि, वह राधा कौन है और किसकी पुत्री है?
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10075)
- **Original**: ज्ञान और सम्पत्तिकी दृष्टिसे भी उनमें न्यूनता नन्‍्दकी यह बात सुनकर मुनिवर गर्ग हँसने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10076)
- **Original**: अथवा अधिकता नहीं है। किंतु वे गोलोकसे लगे और बोले-'यह परम निगूढ़ तत्त्व एवं
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10077)
- **Original**: यहाँ पहले आयी हैं; इसलिये अवस्थामें श्रीकृष्णसे राधाबन्धू राधिकात्मा राधिकाजीवन: स्वयम्‌ । राधिकासहचारी च राधामानसपूरकः
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10078)
- **Original**: राधाधनो... राधिकाड़रों.. राधिकासक्तमानस: । राधाप्राणो राधिकेशों राधिकारमण: स्वयम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10079)
- **Original**: राधिकाचित्तचौरक्ष राधाप्राणाधिक: प्रभु: । परिपूर्णतम ब्रह्म गोविन्दो गरुडध्वज:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10080)
- **Original**: नामान्येतानि कृष्णस्य अ्रुतानि साम्प्रत॑ ब्नज । जम्ममृत्युहराण्येव रक्ष नन्‍्द शुभक्षणे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10081)
- **Original**: (13। 75-80)
- **Translation**: 

---

