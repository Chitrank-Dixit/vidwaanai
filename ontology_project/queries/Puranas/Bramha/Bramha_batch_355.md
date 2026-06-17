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

### Verse 1 (Bramha 0.7081)
- **Original**: उनके जशरीरकों विदीर्ण कर देते हैं। भी शरीर ग्रहण करता है, उसे हो यमराजके दूत
- **Translation**: 

---

### Verse 2 (Bramha 0.7082)
- **Original**: जो अपने ऊपर विश्वास करनेवाले स्वामी, यमलोकमें ले जाते हैं। वे उसे कालपाशमें
- **Translation**: 

---

### Verse 3 (Bramha 0.7083)
- **Original**: मित्र अथवा स्त्रीकी हत्या कराते हैं, ये शस्त्रोंद्वार बाँधकर पैरोंमें बेड़ी डाल देते हैं। बेड़ीकी साँकल , छिन्न-भिन्न और व्याकुल होकर यमलोकके मार्गपर बज्रके समान कठोर होतो है। यमकिंकर क्रोधमें
- **Translation**: 

---

### Verse 4 (Bramha 0.7084)
- **Original**: जाते हैं। जो निरपराध जोबोंको मारते और भरकर उस बँधे हुए जीवको भलीभाँति पीटते हुए
- **Translation**: 

---

### Verse 5 (Bramha 0.7085)
- **Original**: मरबाते हैं, थे राक्षसोंके ग्रास बनकर उस पथसे ले जाते हैं। यह लड़खड़ाकर गिरता है, रोता है
- **Translation**: 

---

### Verse 6 (Bramha 0.7086)
- **Original**: यात्रा करते हैं। जो परायी स्थ्रियोंके वस्त्र उतारते और “हाय बाप! हाय मैया! हाय पुत्र!” कहकर
- **Translation**: 

---

### Verse 7 (Bramha 0.7087)
- **Original**: हैं, वे मरनेपर नंगे करके दौड़ते हुए यमलोकरमें
- **Translation**: 

---

### Verse 8 (Bramha 0.7088)
- **Original**: केडेढ * संक्षिप्त ब्रह्मपुराण « लाये जाते हैं। जो दुरात्मा पापाचारी अन्न, वस्त्र,
- **Translation**: 

---

### Verse 9 (Bramha 0.7089)
- **Original**: उसके चार सुन्दर दरवाजे हैं। उसकी चहारदीवारी सोने, घर और खेतका अपहरण करते हैं, उन्हें
- **Translation**: 

---

### Verse 10 (Bramha 0.7090)
- **Original**: सोनेको बनी है, जो दस हजार योजन ऊँची है। यमलोकके मार्गपर पत्थरों, लाठियों और डंडोंसे
- **Translation**: 

---

### Verse 11 (Bramha 0.7091)
- **Original**: यमपुरीका पूर्वद्वार बहुत ही सुन्दर है। वहाँ मारकर जर्जर कर दिया जाता है और वे अपने
- **Translation**: 

---

### Verse 12 (Bramha 0.7092)
- **Original**: फहराती हुई सैकड़ों पताकाएँ उसकी शोभा अद्भ-प्रत्यज्नसे प्रचुर रक्त बहाते हुए यमलोकमें
- **Translation**: 

---

### Verse 13 (Bramha 0.7093)
- **Original**: बढ़ाती हैं। हीरे, नीलम, पुखराज और मोतियोंसे जाते हैं। जो नराधम नरककी परवा न करके इस
- **Translation**: 

---

### Verse 14 (Bramha 0.7094)
- **Original**: वह द्वार सजाया जाता है। वहाँ गन्धर्वों और लोकमें ब्राक्षणका धन हड्प लेते, उन्हें मारते
- **Translation**: 

---

### Verse 15 (Bramha 0.7095)
- **Original**: अप्सराओंके गीत और नृत्य होते रहते हैं। उस और गालियाँ सुनाते हैं, उन्हें सूखे काठमें बाँधकर
- **Translation**: 

---

### Verse 16 (Bramha 0.7096)
- **Original**: द्वारसे देवताओं, ऋषियों, योगियों, गन्धर्वों, सिद्धों, उनकी आँखें फोड़ दी जाती और नाक-कान
- **Translation**: 

---

### Verse 17 (Bramha 0.7097)
- **Original**: यक्षों और विद्याधरोंका प्रवेश होता है। उस काट लिये जाते हैं। फिर उनके शरीरमें पीब और
- **Translation**: 

---

### Verse 18 (Bramha 0.7098)
- **Original**: नगरका उत्तरद्वार घण्टा, छत्र, चैंवर तथा नाना रक्त पोत दिये जाते हैं तथा कालके समान गीध
- **Translation**: 

---

### Verse 19 (Bramha 0.7099)
- **Original**: प्रकारके रत्नोंसे अलंकृत है। वहाँ वीणा और और गीदड़ उन्हें नोच-नोचकर खाने लगते हैं।
- **Translation**: 

---

### Verse 20 (Bramha 0.7100)
- **Original**: वेणुकी मनोहर ध्यनि गूँजती रहती है। गीत, इस दशामें भी क्रोधमें भरे हुए भयानक यमदूत
- **Translation**: 

---

