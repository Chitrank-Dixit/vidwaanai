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

### Verse 1 (Bramha 0.2621)
- **Original**: उनके अष्टाक्षर-मनत्रसे अद्ञन्यास और करन्यास माना गया है। विशेषतः: चतुर्दशीको उसमें किया
- **Translation**: 

---

### Verse 2 (Bramha 0.2622)
- **Original**: करे। मनको भुलावेमें डालनेबवाले अन्य बहुत-से हुआ स्रान सब पापोंका नाश करनेवाला है।
- **Translation**: 

---

### Verse 3 (Bramha 0.2623)
- **Original**: मन्क्रेंक्ी क्या आवश्यकता है, “3: नपो मातयणाय'-- समुद्रका स्नान सब समय उत्तम होता है, विशेषत:
- **Translation**: 

---

### Verse 4 (Bramha 0.2624)
- **Original**: यह अष्टाक्षर-मन्त्र ही सब मनोरथोंको सिद्ध पूर्णिमाकों उसमें स्नान करनेसे अश्वमेध-यज्ञका
- **Translation**: 

---

### Verse 5 (Bramha 0.2625)
- **Original**: करनेबाला है। नरसे प्रकट होनेके कारण जलकों 'फल मिलता है। मार्कण्डेयहद, अक्षयवट, श्रीकृष्ण-
- **Translation**: 

---

### Verse 6 (Bramha 0.2626)
- **Original**: नार कहते हैं। वह पूर्वकालमें भगवान्‌ विष्णुका बलराम, समुद्र तथा इन्द्रशुम्न-ये पुरुषोत्तमक्षेत्रक
- **Translation**: 

---

### Verse 7 (Bramha 0.2627)
- **Original**: अयन (निवासस्थान) रहा है, इसलिये उन्हें पाँच तीर्थ हैं। जब ज्येष्ट मासकी पूर्णिमाको ज्येष्ठा
- **Translation**: 

---

### Verse 8 (Bramha 0.2628)
- **Original**: नारायण कहते हैं। समस्त बेदोंका तात्पर्य भगवान्‌ नक्षत्र हो तब विशेषरूपसे तीर्थराज समुद्रकी यात्रा
- **Translation**: 

---

### Verse 9 (Bramha 0.2629)
- **Original**: नारायणमें ही है। सम्पूर्ण द्विज नारायणको ही करनी चाहिये। उस समय मन, वाणी और
- **Translation**: 

---

### Verse 10 (Bramha 0.2630)
- **Original**: उपासनामें तत्पर रहते हैं। यज्ञों और क्रियाओंकी शरीरसे शुद्ध हो भगबान्‌में मन लगाये रहे और
- **Translation**: 

---

### Verse 11 (Bramha 0.2631)
- **Original**: समाप्ति भी नारायणमें ही है। पृथ्वी नारायणपरक कहीं मनको न ले जाय। सब प्रकारके टन्द्दोंस
- **Translation**: 

---

### Verse 12 (Bramha 0.2632)
- **Original**: है। जल नारायणपरक है। अग्नि नारायणपरक है मुक्त रहे, राग और द्वेषको दूर कर दे। कल्पवृक्ष-
- **Translation**: 

---

### Verse 13 (Bramha 0.2633)
- **Original**: और आकाश भी नारायणपरक है। वायु और बट बहुत रमणीय स्थान है, वहाँ स्नान करके
- **Translation**: 

---

### Verse 14 (Bramha 0.2634)
- **Original**: मनके आश्रय भी नारायण ही हैं। अहंकार और एकाग्र चित्तसे तीन बार भगवान्‌ जनार्दनकी
- **Translation**: 

---

### Verse 15 (Bramha 0.2635)
- **Original**: बुद्धि दोनों नारायणस्वरूप हैं। भूठ, वर्तमान तथा परिक्रमा करे। उनके दर्शनसे सात जन्मोंके पापोंसे
- **Translation**: 

---

### Verse 16 (Bramha 0.2636)
- **Original**: आनेवाले सभी जीव, स्थूल और सूक्ष्म--सब छुटकारा मिल जाता है। प्रचुर पुण्य तथा अभीष्ट
- **Translation**: 

---

### Verse 17 (Bramha 0.2637)
- **Original**: कुछ नारायणस्वरूप है। शब्द आदि विषय, श्रवण गतिकी प्राप्ति होती है। प्रत्येक युगके अनुसार
- **Translation**: 

---

### Verse 18 (Bramha 0.2638)
- **Original**: आदि इर्द्रियाँ, प्रकृति और पुरुष--सभी नायायणस्वरूप बटके नाम और प्रमाण बतलाये जाते हैं। बट,
- **Translation**: 

---

### Verse 19 (Bramha 0.2639)
- **Original**: हैं। जल, स्थल, पाताल, स्वर्गलोक, आकाश तथा वरटेश्वर, कृष्ण तथा पुराणपुरुष-ये सत्य आदि
- **Translation**: 

---

### Verse 20 (Bramha 0.2640)
- **Original**: पर्वत-इन सबको व्याप्त करके भगवान्‌ नारायण युगोंमें क्रमशः बटके नाम कहे गये हैं। सत्ययुगमें
- **Translation**: 

---

