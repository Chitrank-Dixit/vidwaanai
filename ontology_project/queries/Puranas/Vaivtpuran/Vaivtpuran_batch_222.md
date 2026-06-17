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

### Verse 1 (Vaivtpuran 13.10582)
- **Original**: तथा वे सबकी कारणस्वरूपा हैं। ऐसी श्रीराधाका मध्यभागमें उनका स्थान है। थे रासकी अधिष्ठात्री
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10583)
- **Original**: मैं भजन करता हूँ। इस प्रकार ध्यान करके देवी हैं। रासेश्वरके वक्ष:स्थलमें वास करती हैं। श्रीकृष्फे साथ उनका पूजन करे*। रासकी रसिका हैं। रसिकशेखर श्यामसुन्दरकी प्रतिदिन भक्तिभावसे सोलह उपचार चढ़ाकर प्रिया हैं। रसिकाओंमें श्रेष्ठ हैं। सुरम्य रमारूपिणी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10584)
- **Original**: पूजा करे। ब्रती पुरुष प्रत्येक उपचारकों पृथक्‌- हैं। प्रियतमके साथ रमणके लिये उत्सुक रहती
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10585)
- **Original**: पृथक्‌ करके सबको बारी-बारीसे प्रसन्नतापूर्वक हैं। उनके नेत्र शरत्कालके प्रफुल्ल कमलोंकी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10586)
- **Original**: अर्पित करे। मुने! नित्यप्रति एक सौ आठ दिव्य शोभाको तिरस्कृत करते हैं। वे बाँकी भौंहोंसे सहस्लदत कमल लेकर उनकी एक सौ आठ सुशोभित होती हैं। उनके नेत्रोंमें सुरमा शोभा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10587)
- **Original**: आहुतियाँ दे। भक्तिभावसे 'कृष्णाय स्वाहा' इस पा रहा है। शरत्पूर्णिमाके चन्द्रमाकी भाँति सुन्दर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10588)
- **Original**: मन्त्रका उच्चारण करके यल्पूर्वक वे आहुतियाँ मुखपर मन्द मुस्कानकौ प्रभाके कारण उनकी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10589)
- **Original**: देनी चाहिये। आम और केलेके कच्चे या पके मनोहरता बहुत बढ़ गयी है। मनोहर चम्पाके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10590)
- **Original**: फलको लेकर उसकी एक सौ आठ आहुतियाँ समान उनकी अद्भगकान्ति सुनहरी दिखाबी देती
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10591)
- **Original**: भक्तिभावसे दे। फल अखण्ड होने चाहिये। मुने ! है। चन्दन, कस्तूरीकी बेंदी तथा सिन्दूर-बिन्दुसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10592)
- **Original**: प्रतिदिन सौ ब्राह्मणोंको भक्तिपूर्वक भोजन करावे। उनका श्रृज्ञार किया गया है। कपोलॉपर मनोहर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10593)
- **Original**: व्रतीकों नित्य एक सौ आठ आहुतियोंका हवन पत्रावलीकौ रचना शोभा देती है। अग्निशुद्ध दिव्य
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10594)
- **Original**: करना चाहिये। वे आहुतियाँ भक्तिपूर्वक राधिकासहित वस्त्रसे उनकी उज्ज्वलता बढ़ गयी है। उत्तम
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10595)
- **Original**: श्रीकृष्णोो देनी चाहिये। नारद! घृतमिश्रित सलोंद्वारा. निर्मित कुण्डलोंकी कान्तिसे उनके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10596)
- **Original**: तिलसे भी हजन करे। नित्य बाजे बजावे और सुन्दर कपोल प्रकाशित हो रहे हैं। रत्लेन्द्रसाररचित श्रीहरिका कीर्तन कराबे। हारसे बक्ष:स्थल उद्धासित हो रहा है। रत्लनिर्मित
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10597)
- **Original**: तीन मासतक इस नियमका पालन करके कल्कूण, केयूर तथा किल्धलिणी रलसे उनके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10598)
- **Original**: उसके बाद ब्रतकी प्रतिष्ठा करे। नारद! प्रतिष्ठाके * ध्यायेत्‌ तदा राधिकां च ध्यान माध्यन्दिनेरितम्‌ । राधां रासेश्वरों रम्यां. रासोललासरसोत्सुकाम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10599)
- **Original**: रासमण्डलमध्यस्थां रासाधिष्ठातृदेवताम्‌ू । रासेशवक्ष:स्थलस्थां.. रसिकां. रसिकप्रियाम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10600)
- **Original**: रसिकप्रवरां. रम्यां. रमां च॒ रमणोत्सुकाम्‌। शरद्राजीवराजोनां प्रभामोचनलोचनाम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10601)
- **Original**: वक्रध्ूभड्भसंयुक्तामजनेनैव रज्जिताम्‌ । शरत्पार्वणचन्ध्रास्थामीषद्धास्यमनोहरान्‌
- **Translation**: 

---

