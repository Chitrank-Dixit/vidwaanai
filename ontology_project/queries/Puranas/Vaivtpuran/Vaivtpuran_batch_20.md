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

### Verse 1 (Vaivtpuran 3.265)
- **Original**: उसीसे महान्‌ बिराट्‌ पुरुषकी उत्पत्ति हुई, जो जलने सम्पूर्ण विश्वकों आप्लावित कर दिया।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 3.266)
- **Original**: सम्पूर्ण विश्वके आधार हैं। उन विराट्‌ पुरुषके उसके किश्चित्‌ कणमात्र जलने उस प्रज्वलित
- **Translation**: 

---

### Verse 3 (Vaivtpuran 3.267)
- **Original**: एक-एक रोम-कृपमें एक-एक त्रह्माण्डकी स्थिति अग्रिको शान्त कर दिया। तभीसे जलके द्वारा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 3.268)
- **Original**: है। वे स्थूलसे भी स्थूलतम हैं। उनसे बड़ा दूसरा आग बुझने लगी। तत्पश्चात्‌ वहाँ एक पुरुषका
- **Translation**: 

---

### Verse 5 (Vaivtpuran 3.269)
- **Original**: कोई नहीं है। बे परमात्मा श्रीकृष्णके सोलहवें प्रादर्भाव हुआ, जो उस अग्निके अधिदेवता थे।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 3.270)
- **Original**: अंश हैं। उन्हींको “महाविष्णु” जानना चाहिये। फिर पूर्वोक्त जलसे एक पुरुषका उत्थान हुआ,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 3.271)
- **Original**: वे ही सबके सनातन आधार हैं। जैसे जलमें जिनका नाम “वरुण' हुआ। वे ही जलके अधिष्ठाता
- **Translation**: 

---

### Verse 8 (Vaivtpuran 3.272)
- **Original**: कमलका पत्ता रहता है, उसी प्रकार बे महार्णवके देवता और समस्त जल-जन्तुओंके स्वामी हुए।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 3.273)
- **Original**: जलमें शयन करते हैं। उनके शयन करते समय इसके बाद उस अग्रिदेवके वामपार्श्सने एक
- **Translation**: 

---

### Verse 10 (Vaivtpuran 3.274)
- **Original**: कानोंके मलसे दो दैत्य प्रकट हुए। वे दोनों जलसे कन्याका आविर्भाव हुआ, जिसका नाम 'स्वाहा'
- **Translation**: 

---

### Verse 11 (Vaivtpuran 3.275)
- **Original**: उठकर ब्रह्माजीको मार डालनेके लिये उच्चत हो था। मनीषी पुरुष उसे अग्रिकी पत्नी कहते हैं।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 3.276)
- **Original**: गये। तब भगवान्‌ नारायणने उन दोनोंकों अपने जलेश्वर वरुणके वामपार्श्से भी एक कन्या प्रकट
- **Translation**: 

---

### Verse 13 (Vaivtpuran 3.277)
- **Original**: जघन-देशमें सुलाकर चक्रसे काट डाला। उन हुई, जो 'वरुणानी' के नामसे विख्यात थी। बही
- **Translation**: 

---

### Verse 14 (Vaivtpuran 3.278)
- **Original**: दोनोंके सम्पूर्ण मेदेसे यह सारी पृथ्वी निर्मित बरुणकी सती साध्वी प्रिया हुई। भगवान्‌ श्रीकृष्णकी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 3.279)
- **Original**: हुई, जिससे इसका नाम “मेदिनी” हुआ। उसीपर निःश्वास वावुसे श्रीमान्‌ “पवन” का प्रादुर्भाव [सम्पूर्ण विश्वकी स्थिति है। उसकी अधिष्ठात्री हुआ, जो समस्त देहधारियोंके प्राण हैं। श्रास-
- **Translation**: 

---

### Verse 16 (Vaivtpuran 3.280)
- **Original**: देवीका नाम “वसुन्धरा' है। (अध्याय 4) #># 080 #सप 0: 0000000 ब्राह्र आदि कल्पोंका परिचय, गोलोकमें श्रीकृष्णका नारायण आदिके साथ रासमण्डलमें निवास, श्रीकृष्णके बामपार्श्बसे श्रीराधाका प्रादुर्भाव; राधाके रोमकूपोंसे गोपाड्रनाओंका प्राकट्य तथा श्रीकृष्णसे गोपों, गौओं, बलीवर्दों, हंसों, श्वेतघोड़ों और सिंहोंकी उत्पत्ति; श्रीकृष्णद्वारा पाँच रथोंका निर्माण तथा पार्षदोंका प्राकट्य; भेरव, ईशान और डाकिनी आदिकी उत्पत्ति महर्षि शौनकके पूछनेपर सौति कहते
- **Translation**: 

---

### Verse 17 (Vaivtpuran 3.281)
- **Original**: सत्ययुग, त्रेता, द्वापर और कलियुग-ये चारों हैं-त्रह्मनू! मैंने सबसे पहले ब्रह्मकल्पके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 3.282)
- **Original**: युग क्रमसे कहे गये हैं, वैसे ही वे कल्प भी चरित्रका वर्णन किया है। अब वाराहकल्प और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 3.283)
- **Original**: हैं। तीन सौ साठ युगोंका एक दिव्य युग माना पाद्यकल्प-इन दोनोंका वर्णन करूँगा, सुनिये।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 3.284)
- **Original**: गया है। इकहत्तर दिव्य युगोंका एक मन्वन्तर मुने! ब्राह्य, वाराह और पाद्य-ये तीन प्रकारके
- **Translation**: 

---

