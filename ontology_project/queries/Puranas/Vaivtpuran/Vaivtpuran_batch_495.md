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

### Verse 1 (Vaivtpuran 28.4306)
- **Original**: [दिन तथा अन्नप्राशनके शुभ समयपर यत्रपूर्वक “5 6. - 3
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.4307)
- **Original**: देबीकी पूजा होने लगी। सर्वत्र इसका पूरा 6»
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.4308)
- **Original**: प्रचार हो गया। स्वयं राजा प्रियव्रत भी पूजा देवीने कहा--तुम स्वायम्भुव मनुके पुत्र
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.4309)
- **Original**: करते थे। हो। त्रिलोकीमें तुम्हाशा शासन चलता है। तुम
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.4310)
- **Original**: सुत्रत! अब भगवती देवसेनाका ध्यान, सर्वत्र मेरी पूजा कराओ और स्वयं भी करो। पूजन, स्तोत्र कहता हूँ, सुनो। यह प्रसम्र तब मैं तुम्हें कमलके समान मुखवाला यह
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.4311)
- **Original**: कौथुमशाखामें वर्णित हैं। धर्मदेवके मुखसे मनोहर पुत्र प्रदान करूँगी। इसका नाम सुत्रत
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.4312)
- **Original**: सुननेका मुझे अवसर मिला था। मुने! शालग्रामकी होगा। इसमें सभी गुण और विवेकशक्ति विद्यमान
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.4313)
- **Original**: प्रतिमा, कलश अथवा बटके मूलभागमें या रहेगी। यह भगवान्‌ नारायणका कलाबतार तथा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.4314)
- **Original**: दीवालपर पुत्तलिका बनाकर प्रकृतिके छठे अंशसे प्रधान योगी होगा। इसे पूर्वजन्मकी बातें याद
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.4315)
- **Original**: प्रकट होनेवाली शुद्धस्वरूपिणी इन भगवतीकी रहेंगी। क्षत्रियोंमें श्रेष्ठ यह बालक सौ अश्वमेध-
- **Translation**: 

---

### Verse 11 (Vaivtpuran 28.4316)
- **Original**: इस प्रकार पूजा करनी चाहिये। विद्वान्‌ पुरुष यज्ञ करेगा। सभी इसका सम्मान करेंगे। उत्तम
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.4317)
- **Original**: इनका इस प्रकार ध्यान करे--'सुन्दर पुत्र, बलसे सम्पन्न होनेके कारण यह ऐसी शोभा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.4318)
- **Original**: कल्याण तथा दया प्रदान करनेवाली ये देवी पायेगा, जैसे लाखों हाथियोंमें सिंह। यह धनी,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.4319)
- **Original**: जगत्‌की माता हैं। श्वेत चम्पकके समान इनका (637] सं0 ब्र0 वै0 पुराण 9 51 7)). 5 कं आर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.4320)
- **Original**: धर 25 0, पक, ह
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.4321)
- **Original**: वर्ण है। रत्रमय भूषणोंसे ये अलंकृत हैं। इन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.4322)
- **Original**: भक्तोंको प्रत्यक्ष दर्शन देनेवाली तथा सबके लिये परम पतित्रस्वरूपिणी भगवती देवसेनाकी मैं सम्पूर्ण कार्योंमें पूजा प्राप्त करेकी अधिकारिणी उपासना करता हूँ।' विद्वान्‌ पुरुष यों ध्यान
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.4323)
- **Original**: स्वामी कार्तिकेयकी प्राणप्रिया देवी षष्ठीको बार- करनेके पश्चात्‌ भगवतीकों पुष्पाज्लि समर्पण
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.4324)
- **Original**: बार नमस्कार है। मनुष्य जिनकी सदा वन्दना करे। पुनः ध्यान करके मूलमन्त्रसे इन साध्वी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.4325)
- **Original**: करते हैं तथा देवताओंकी रक्षामें जो तत्पर रहती देवीकी पूजा करनेका विधान है। पाद्य, अर्घ्य,
- **Translation**: 

---

