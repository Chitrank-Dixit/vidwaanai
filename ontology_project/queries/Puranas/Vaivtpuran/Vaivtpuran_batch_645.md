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

### Verse 1 (Vaivtpuran 66.5766)
- **Original**: कवचकों धारण करता है, वह विष्णु ही है, भद्रकालीने रक्तबीजका संहार किया, देवराज
- **Translation**: 

---

### Verse 2 (Vaivtpuran 66.5767)
- **Original**: इसमें संशय नहीं है। मुने ! सम्पूर्ण तीर्थोंकी यात्रा इन्द्रने खोयी हुई राज्य-लक्ष्मी प्राप्त की, महाकाल
- **Translation**: 

---

### Verse 3 (Vaivtpuran 66.5768)
- **Original**: और पृथ्वीकी परिक्रमा करनेपर मनुष्यको जो चिरजीवी और धार्मिक हुए, नन्‍्दी महाज्ञानी होकर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 66.5769)
- **Original**: फल मिलता है, वही इस कवचको धारण करनेसे सानन्द जीवन बिताने लगा, परशुरामजी शत्रुओंको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 66.5770)
- **Original**: मिल जाता है। पाँच लाख जप करनेसे निश्चय भय देनेवाले महान्‌ योद्धा बन गये तथा जिसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 66.5771)
- **Original**: ही यह कवच सिद्ध हो जाता है। जिसने कबचको धारण करके ज्ञानिशिरोमणि दुर्वासा भगवान्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 66.5772)
- **Original**: सिद्ध कर लिया है, उस मनुष्यको रणसंकटमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 66.17870)
- **Original**: 790 संक्षिम ग्रह्मलैकर्तपुराण * ऊऋ$%ऋऋ$%$%%/##5/#####$######$4%4#%
- **Translation**: 

---

### Verse 9 (Vaivtpuran 66.17871)
- **Original**: $% 8 # कक $ऋऋ%ऋऋऋ्ऋ्क्ऋ् कक #ऋक्क ऋऋऋऋऋऋऋऋऋ कक श्रद्धा पुष्टिश्न तन्द्राच लजा शोभा दया तथा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 66.17872)
- **Original**: सतां .. सम्पत्स्वरूपा श्रीर्विपत्तिस्‍सतामिह
- **Translation**: 

---

### Verse 11 (Vaivtpuran 66.17873)
- **Original**: प्रीतिरूपा पुण्यवतां पापिनां कलहाडुरा । शश्वत्कर्ममयी शक्ति: सर्वदा सर्बजीविनाम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 66.17874)
- **Original**: देवेभ्य: स्वपदो दात्री धातुर्धात्री कृपामयी । हिताय. सर्वदेवानां. सर्वासुरविनाशिनी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 66.17875)
- **Original**: योगनिद्रा योगरूपा योगदात्री च्र योगिनाम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 66.17876)
- **Original**: सिद्धिस्वरूपा सिद्धानां सिद्धिदा सिद्धियोगिनी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 66.17877)
- **Original**: माहेश्वरी च ब्रह्माणी विष्णुमाया च बैष्णवी । भद्दा भद्रकाली चर सर्वलोकभयंकरी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 66.17878)
- **Original**: ग्रामे ग्रामे ग्रामदेखी गृहदेवी गृहे गृहे । सतां कीर्ति: प्रतिष्ठा चर निन्दा त्वमसतां सदा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 66.17879)
- **Original**: महायुद्धे महामारी दुष्ट्संहाररूपिणी । रक्षास्सरूपा शिष्टानां सातेव हितकारिणी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 66.17880)
- **Original**: बन्द्या पूज्या स्तुता त्व॑ च ब्रह्मादीनां च सर्वदा । ब्लाह्मण्यरूपा विप्राणां तपस्या चर तपस्विनाम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 66.17881)
- **Original**: विद्या विद्यावतां त्वंच बुद्धिर्युद्धिमतां सताम्‌ । मेथास्मृतिस्वरूपा च्ञ प्रतिभा प्रतिभावताम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 66.17882)
- **Original**: राज्ञां प्रतापरूपा चर बिशां बाणिज्यरूपिणी । सृष्टी सृष्टिस्वकूपा त्व॑ं रक्षारूपा च पालने
- **Translation**: 

---

