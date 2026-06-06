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

### Verse 1 (Vaivtpuran 45.4421)
- **Original**: सिद्धा हैं; मैं इन भगवती मनसाकी उपासना करता विख्यात हुई हैं। जगत्पूज्य योगी महात्मा मुनिवर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 45.4422)
- **Original**: हूँ।' इस प्रकार ध्यान करके मूलमन्त्रसे भगवतीकी जरत्कारुकी प्यारी पत्नी होनेके कारण ये 'जरत्कारुप्रिया'
- **Translation**: 

---

### Verse 3 (Vaivtpuran 45.4423)
- **Original**: पूजा करनी चाहिये। अनेक प्रकारके नैवेद्य तथा नामसे विख्यात हुईं। जरत्कारु, जगद्गौरी, मनसा,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 45.4424)
- **Original**: गन्ध, पुष्प और अनुलेपनसे देवीकी पूजा होती :20252%/270:::04 वैष्णवी, नागभगिनी, शैवी, नागेश्वरी,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 45.4425)
- **Original**: है। सभी उपचार मूलमन्त्रको पढ़कर अर्पण करने जरत्कारुप्रिया, आस्तीकमाता, विषहरी और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 45.4426)
- **Original**: चाहिये। मुने! इनके मूलमन्त्रका नाम है--“मूल महाज्ञानयुता--इन बारह नामोंसे विश्व इनकी पूजा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 45.4427)
- **Original**: कल्पतरु'-यह सुसिद्ध मन्त्र है। इसमें बारह * जरत्कारुजंगद्वरीरी. मनसा. सिद्धयोगिनी । वैष्णवी नागभगिनों शैवी नागेश्वरी तथा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 45.4428)
- **Original**: जरत्कारुप्रिया55स्तीकमाता_ विषहरोति च । महाज्ञानयुता चैव सा देवी विश्वपूजिता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 45.4429)
- **Original**: द्वादशैतानि नामानि पूजाकाले तु यः पठेत्‌ । तस्य नागभयं नास्ति तस्य वंशोद्धवस्प च
- **Translation**: 

---

### Verse 10 (Vaivtpuran 45.4430)
- **Original**: (प्रकृतिखण्ड 45। 15--17)
- **Translation**: 

---

### Verse 11 (Vaivtpuran 45.4431)
- **Original**: अक्षर हैं। इसका वर्णन वेदमें है। यह भक्तोंके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 45.4432)
- **Original**: अध्ययन कराया और भगवान्‌ श्रीकृष्णके कल्पवृक्षरूप मनोरथको पूर्ण करनेबाला है। मन्त्र इस प्रकार
- **Translation**: 

---

### Verse 13 (Vaivtpuran 45.4433)
- **Original**: अष्टाक्षर-मन्त्रका उपदेश किया। है--' 30 हीं श्रीं क्लीं ऐं मनसादेव्यै स्वाहा।' पाँच. मन्त्रका रूप ऐसा है--लक्ष्मीबीज, मायाबीज लाख मन्त्र जप करनेपर यह मन्त्र सिद्ध हो जाता
- **Translation**: 

---

### Verse 14 (Vaivtpuran 45.4434)
- **Original**: और कामबीजका पूर्वमें प्रयोग करके कृष्ण है। जिसे इस मन्त्रकी सिद्धि प्राप्त हो गयी, वह
- **Translation**: 

---

### Verse 15 (Vaivtpuran 45.4435)
- **Original**: शब्दके अन्तमें 'डे” विभक्ति लगाकर नमः पद धरातलपर सिद्ध है। उसके लिये विष भी अमृतके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 45.4436)
- **Original**: जोड़ दिया जाता है (श्रीं हीं क्लीं कृष्णाय समान हो जाता है। उस पुरुषकी धन्वन्तरिसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 45.4437)
- **Original**: नमः )। भगवान्‌ शंकरकी कृपासे जब मुनिकुमारी तुलना की जा सकती है। मनसाको उक्त मन्त्रके साथ त्रैलोक्यमड्गल नामक ब्रह्मन्‌! जो पुरुष आषाढ़की संक्रान्तिके दिन
- **Translation**: 

---

### Verse 18 (Vaivtpuran 45.4438)
- **Original**: कवच, पूजनका क्रम, सर्वमान्य स्तवन, भुवनपावन “गुडा' (कपास या सेंहुड) नामक वृक्षकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 45.4439)
- **Original**: ध्यान, सर्वसम्मत वेदोक्त पुरश्षरणका नियम तथा शाखापर यल्रपूर्वक इन भगवती मनसाका आवाहन
- **Translation**: 

---

### Verse 20 (Vaivtpuran 45.4440)
- **Original**: मृत्युअय-ज्ञान प्राप्त हो गया, तब वह साध्वी उनसे करके भक्तिभावके साथ पूजा करता है तथा ।
- **Translation**: 

---

