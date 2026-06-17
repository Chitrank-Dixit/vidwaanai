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

### Verse 1 (Vaivtpuran 63.5620)
- **Original**: वायु, वरुण, देवीकी चेटी, बढु तथा चौंसठ अत्यन्त मूल्यवान्‌ रत्नोंक सार-भागके द्वारा ईश्वरेच्छासे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 63.5621)
- **Original**: योगिनी--इन सबका विधिवत्‌ पूजन करके यथाशक्ति निर्मित तथा सम्पूर्ण अद्ोंको शोभासम्पन्न बनानेवाला
- **Translation**: 

---

### Verse 3 (Vaivtpuran 63.5622)
- **Original**: भेंट--उपहार अर्पित करके विद्वान्‌ पुरुष स्तुति रत्रमय आभूषण ग्रहण करो। (धूप) देवि! वृक्षकी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 63.5623)
- **Original**: करे। कबचको भक्तिपूर्वक पढ़कर उसे गलेमें गोदके चूर्णको सुगन्धित वस्तुओंसे मिश्रित करके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 63.5624)
- **Original**: बाँध ले। फिर परिहारनामक स्तुति करके विद्वान्‌ अग्रिकी शिखासे शुद्ध किया गया है। इस धूपको
- **Translation**: 

---

### Verse 6 (Vaivtpuran 63.5625)
- **Original**: पुरुष देवीको नमस्कार करे। इस प्रकार उपहार दे स्वीकार करो। (दीप) परमेश्वरि ! घने अन्थकारको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 63.5626)
- **Original**: स्तुति करके कबच बाँधकर विद्वान्‌ पुरुष धरतीपर दूर करनेबाला यह परम पवित्र दीप दिव्य
- **Translation**: 

---

### Verse 8 (Vaivtpuran 63.5627)
- **Original**: माथा टेक दण्डबत्‌ प्रणाम करे और ब्राह्मणको रत्विशेष है। इसे ग्रहण करो। (शब्या) देवि! यह
- **Translation**: 

---

### Verse 9 (Vaivtpuran 63.5628)
- **Original**: दक्षिणा दे। (अध्याय 63-64) #+ल+/ अप त.....>>
- **Translation**: 

---

### Verse 10 (Vaivtpuran 65.5629)
- **Original**: + प्रकृतिखण्ड + 289 देवीके बोधन, आवाहन, पूजन और विसर्जनके नक्षत्र, इन सबकी महिमा, राजाको देवीका दर्शन एवं उत्तम ज्ञानका उपदेश देना नारदजीने पूछा--महाभाग! आपने जो
- **Translation**: 

---

### Verse 11 (Vaivtpuran 65.5630)
- **Original**: चाहिये; क्योंकि हिंसासे मनुष्य पापका भागी होता कुछ कहा है, वह अमृतरससे भी बढ़कर मधुर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 65.5631)
- **Original**: है, इसमें संशय नहीं। जो जिसका वध करता है, और उत्तम है। उसे पूर्णरूपसे मैंने सुन लिया।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 65.5632)
- **Original**: वह मार गया प्राणी भी जन्मान्तरमें उस मारनेवालेका प्रभो! अब भलीभाँति यह बताइये कि देवीका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 65.5633)
- **Original**: वध करता है--यह वेदकी वाणी है।* इसीलिये स्तोत्र और कवच क्या है? तथा उनके पूजनसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 65.5634)
- **Original**: वैष्णवजन वैष्णवी (हिंसारहित) पूजा करते हैं। किस फलकी प्राप्ति होती है? इस प्रकार पूरे वर्षतक भक्तिभावसे पूजन भारायणने कहा--आर्द्रा नक्षत्रमें देवीको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 65.5635)
- **Original**: करके गलेमें कवच बाँधकर राजाने परमेश्वरीका जगाबे और मूल नक्षत्रमें उनका प्रतिमामें प्रवेश
- **Translation**: 

---

### Verse 17 (Vaivtpuran 65.5636)
- **Original**: स्तवन किया। उनके द्वारा किये गये स्तवनसे या आवाहन करे। फिर उत्तराषाढ़ नक्षत्रमें पूजा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 65.5637)
- **Original**: संतुष्ट हुई देबीने उन्हें साक्षात्‌ दर्शन दिये। उन्होंने करके श्रवण नक्षत्रमें देवीका विसर्जन करे।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 65.5638)
- **Original**: सामने 'देवीको देखा, वे ग्रीष्म-ऋतुके सूर्यकी आद्रायुक्त नवमी तिथिमें देवीको जगाकर जो पूजा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 65.5639)
- **Original**: भाँति देदीप्यमान थीं। वे तेज:स्वरूपा, सगुणा एवं की जाती है, उस एक बारकी पूजासे मनुष्य सौ
- **Translation**: 

---

