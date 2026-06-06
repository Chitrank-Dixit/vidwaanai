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

### Verse 1 (Vaivtpuran 543.14594)
- **Original**: उपाधिके मिट जानेपर समस्त चित्‌ प्रतिबिम्ब--जीव महायोगका वर्णन कीजिये। मेरे मनमें उसे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14595)
- **Original**: मुझमें ही अन्तर्हित हो जाते हैं । प्रिये! समयानुसार
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14596)
- **Original**: + श्रीकृष्णजन्मखण्ड * 633 &#%4$#$ $ 5 % 5 $ # $5 45 $ ## ## ## 44% ## # # # 4 4 /% 4 ## $# % % 4 $### ## 6 #% 4 44% % 4 #ऋ कक 4 कक समस्त जीवधारियोंकी मृत्यु हो जानेपर जीव
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14597)
- **Original**: तरह विश्वत्नह्माण्डसे बाहर है, जैसे गोलोक। मुझसे ही संयुक्त होता है। हम दोनों सदा समस्त
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14598)
- **Original**: सत्यलोकमें तुम्हीं संरस्वती तथा त्रह्मप्रिया सावित्री जन्तुओंमें विद्यमान हैं। सम्पूर्ण जगत्‌ आधेय है
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14599)
- **Original**: हो। शिवलोकमें जो मूलप्रकृति ईश्वरी शिवा हैं, और मैं इसका आधार हूँ। आधारके बिना आधेय
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14600)
- **Original**: वे भी तुमसे भिन्न नहीं हैं, वे दुर्गम संकटका नाश उसी तरह नहीं रह सकता, जैसे कारणके बिना
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14601)
- **Original**: करनेके कारण सर्वदुर्गतिनाशिनी 'दुर्गा' कहलातो कार्य। सुन्दरि! संसारके समस्त द्रव्य नश्वर हैं। हैं। वे ही दक्षकन्या सती हैं और वे ही हैं कहीं किन्हीं पदार्थोंका आविर्भाव अधिक होता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14602)
- **Original**: गिरिराजकुमारी पार्वती। कैलासमें सौभाग्यशालिनी है और कहीं कम। कुछ देवता मेरे अंश हैं, कुछ
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14603)
- **Original**: पार्वती शिवके वक्ष:स्थलपर विराजमान होती हैं। कला हैं, कुछ कलाकी कलाके भी अंश हैं और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14604)
- **Original**: तुम्हीं अपने अंशसे सिन्धुकन्या होकर क्षीरसागरमें कुछ उस अंशके भी अंशांश हैं। मेरी अंशस्वरूपा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14605)
- **Original**: श्रीविष्णुके बक्षःस्थलपर विराजमान होती हो। प्रकृति सूक्ष्मरूपिणी है। उसकी पाँच मूर्तियाँ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14606)
- **Original**: सृष्टिकालमें मैं ही अपने अंशसे ब्रह्मा, विष्णु और हैं--सरस्वती, लक्ष्मी, दुर्गा, तुम (राधा) और
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14607)
- **Original**: शिवरूप धारण करता हूँ तथा तुम लक्ष्मी, शिवा, बेदजननी सावित्री। जितने भी मूर्तिधारी देवता हैं,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14608)
- **Original**: धात्री एवं सावित्री आदि पृथक्‌-पृथक्‌ रूप धारण वे सब प्राकृतिक हैं। मैं सबका आत्मा हूँ और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14609)
- **Original**: करती हो। गोलोकके रासमण्डलमें तुम स्वयं ही भक्तोंके ध्यानके लिये नित्य देह धारण करके सदा रासेश्वरीके पदपर प्रतिष्ठित हो। रमणीय स्थित हूँ। राधे! जो-जो प्राकृतिक देहधारी हैं, वे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14610)
- **Original**: वृन्दावनमें वृन्दा तथा विरजा-तटपर विरजाके प्राकृत प्रलयमें नष्ट हो जाते हैं। सबसे पहले मैं रूपमें तुम्हीं शोभा पाती हो। वही तुम इस समय हो था और सबके अन्तमें भी मैं हो रहूँगा। जैसा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14611)
- **Original**: सुदामाके शापसे पुण्यभूमि भारतवर्षमें आयी हो। मैं हूँ, वैसी ही तुम भी हो। जैसे दूध और उसकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14612)
- **Original**: सुन्दरि! भारतवर्ष और वृन्दावनको पवित्र करना धवलतामें कभी भेद नहीं होता, उसी प्रकार
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14613)
- **Original**: ही तुम्हारे शुभागमनका उद्देश्य है। समस्त लोकोंमें निश्चय ही हम दोनोंमें भेद नहीं है। प्रारम्भिक
- **Translation**: 

---

