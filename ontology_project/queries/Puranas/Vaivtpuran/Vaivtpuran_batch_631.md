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

### Verse 1 (Vaivtpuran 63.5500)
- **Original**: मूलप्रकृति ईश्वरी महादेवीका नित्य ध्यान शरण लो। “कृष्ण” यह दो अक्षरोंका मन्त्र करे। वे सनातनी देवी ब्रह्मा, विष्णु और शिव श्रीकृष्णदास्य प्रदान करनेवाला है। तुम इसे ग्रहण
- **Translation**: 

---

### Verse 2 (Vaivtpuran 63.5501)
- **Original**: आदिके लिये भी पूजनीया तथा बन्दनीया हैं। करो और दुष्कर सिद्धिकी प्राप्ति करानेवाले
- **Translation**: 

---

### Verse 3 (Vaivtpuran 63.5502)
- **Original**: उन्हें नारायणी और विष्णुमाया कहते हैं। वे पुष्करतीर्थमें जाकर इस मन्त्रका दस लाख जप
- **Translation**: 

---

### Verse 4 (Vaivtpuran 63.5503)
- **Original**: वैष्णवीदेबी विष्णुभक्ति देनेवाली हैं। यह सब करो। दस लाखके जपसे ही तुम्हारे लिये यह
- **Translation**: 

---

### Verse 5 (Vaivtpuran 63.5504)
- **Original**: कुछ उनका ही स्वरूप है। वे सबकी ईश्वरी, मन्त्र सिद्ध हो जायगा। सबकी आधारभूता, परात्परा, सर्वविद्यारूपिणी, ऐसा कहकर भगवती प्रकृति वहाँ अन्तर्धान
- **Translation**: 

---

### Verse 6 (Vaivtpuran 63.5505)
- **Original**: सर्वमन्त्रमयी तथा सर्वशक्तिस्वरूपा हैं। वे सगुणा हो गयीं। मुने! उन्हें भक्तिभावसे नमस्कार करके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 63.5506)
- **Original**: और निर्गुणा हैं। सत्यस्वरूपा, श्रेष्ठा, स्वेच्छामयी समाधि वैश्य पुष्करतीर्थमें चला गया। पुष्करमें एवं सती हैं। महाविष्णुकी जननी हैं। श्रीकृष्णके दुष्कर तप करके उसने परमेश्वर श्रीकृष्णको प्राप्त
- **Translation**: 

---

### Verse 8 (Vaivtpuran 63.5507)
- **Original**: आधे अड्भसे प्रकट हुईं हैं। कृष्णप्रिया, कृष्णशक्ति कर लिया। भगवती प्रकृतिके प्रसादसे वह
- **Translation**: 

---

### Verse 9 (Vaivtpuran 63.5508)
- **Original**: एवं कृष्णबुद्धिकी अधिष्ठात्री देवी हैं। श्रीकृष्णने श्रीकृष्णणा दास हो गया। उनकी स्तुति, पूजा और बन्दना की है। वे भगवान्‌ नारायण कहते हैं--महाभाग
- **Translation**: 

---

### Verse 10 (Vaivtpuran 63.5509)
- **Original**: कृपामयी हैं। उनकी अड्भकान्ति तपाये हुए सुवर्णके नारद! राजा सुरथने जिस क्रमसे देवी परा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 63.5510)
- **Original**: समान है। उनकी प्रभा करोड़ों सूर्योंकी दीप्तिको प्रकृतिकी आराधना को थी, वह वेदोक्त क्रम
- **Translation**: 

---

### Verse 12 (Vaivtpuran 63.5511)
- **Original**: भी लज्जित करती है। उनके प्रसन्न मुखपर मन्द- जता रहा हूँ, सुनो। महाराज सुरथने स्नान करके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 63.5512)
- **Original**: मन्द हास्यकी छटा छायी हुई है। वे भक्तोंपर आचमन किया। फिर त्रिविध न्यास, करन्यास,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 63.5513)
- **Original**: अनुग्रह करनेके लिये व्याकुल हैं। उनका नाम अड्जन्यास तथा मन्त्राड्न्यास करके भूतशुद्धि की।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 63.5514)
- **Original**: दुगदिवी है। वे सौ भुजाओंसे युक्त हैं और महती इसके बाद प्राणायाम करके शह्लु-शोधनके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 63.5515)
- **Original**: दुर्गतिका नाश करनलेवाली हैं। त्रिनेत्रधारी महादेवजीकी अनन्तर देवीका ध्यान किया और मिट्टीकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 63.5516)
- **Original**: प्रिया हैं। साध्वी हैं। त्रिगुणमयी एवं त्रिलोचना हैं। प्रतिमामें उनका आवाहन किया। फिर भक्तिभावसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 63.5517)
- **Original**: त्रिलोचन शिवकी प्राणरूपा हैं। उनके मस्तकपर ध्यान करके प्रेमपूर्वक उनका पूजन किया। देवीके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 63.5518)
- **Original**: विशुद्ध अर्द्धचद्धका मुकुट है। वे मालतीकी दाहिने भागमें लक्ष्मीको स्थापना करके परम
- **Translation**: 

---

### Verse 20 (Vaivtpuran 63.5519)
- **Original**: पुष्पमालाओंसे अलंकृत केशपाश धारण करती धार्मिक नरेशने उनकी भी भक्तिभावसे पूजा की।
- **Translation**: 

---

