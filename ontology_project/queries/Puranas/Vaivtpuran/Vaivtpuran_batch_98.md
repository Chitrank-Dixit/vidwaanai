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

### Verse 1 (Vaivtpuran 7.9693)
- **Original**: समस्त पापोंका नाश करनेवाली होती है। सम्पूर्ण जन्माध्यायमें बतायी गयी कथाका भक्तिभावसे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.9694)
- **Original**: उपवास-द्रतोमें दिनको ही पारणा करनेका विधान श्रवण करे। उस समय ब्रती पुरुष रातमें कुशासनपर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.9695)
- **Original**: है। वह उपवास-ब्रतका अड्भभूत, अभीष्ट फलदायक बैठकर जागता रहे। प्रातःकाल नित्यकर्म सम्पन्न
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.9696)
- **Original**: तथा शुद्धिका कारण है। पारणा न करनेपर फलमें करके श्रीहरिका सानन्द पूजन करे तथा ब्राह्मणोंको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.9697)
- **Original**: कमी आती है। रोहिणीब्रतके सिवा दूसरे किसी भोजन कराकर भगवतन्नामोंका कीर्तन करे। त्रतमें रातको पारणा नहीं करनी चाहिये। नारदजीने पूछा--वेदवेत्ताओंमें श्रेष्ठ नारायण-
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.9698)
- **Original**: महारात्रिको छोड़कर दूसरी रात्रिमें पारणा को जा देव! ब्रतकालकी सर्वसम्मत वेदोक्त व्यवस्था
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.9699)
- **Original**: सकती है। ब्राह्मणों और देवताओंकी पूजा करके क्या है? यह बताइये। साथ ही वेदार्थ तथा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.9700)
- **Original**: पूर्वाह्वकालमें पारणा उत्तम मानी गयी है। प्राचीन संहिताका विचार करके यह भी बतानेकी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.9701)
- **Original**: रोहिणी-व्रत सबको सम्मत है। उसका कृपा कीजिये कि ब्रतमें उपवास एवं जागरण
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.9702)
- **Original**: अनुष्ठान अवश्य करना चाहिये। यदि बुध अथवा करनेसे क्या फल मिलता है अथवा उसमें भोजन
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.9703)
- **Original**: सोमवारसे युक्त जयन्ती मिल जाय तो उसमें ब्रत कर लिया जाय तो कौन-सा पाप लगता है?
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.9704)
- **Original**: करके ब्रती पुरुष गर्भमें वास नहीं करता है। भगवान्‌ नारायणने कहा--यदि आधी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.9705)
- **Original**: यदि उदयकालमें किझ्लिन्मात्र कुछ अष्टमी हो रातके समय अष्टमी तिथिका एक चौथाई अंश
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.9706)
- **Original**: और सम्पूर्ण दिन-रातमें नवमी हो तथा बुध, सोम भी दृष्टिगोचर होता हो तो वही ब्रतका मुख्य
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.9707)
- **Original**: एवं रोहिणी नक्षत्रका योग प्राप्त हो तो वह सबसे काल है। उसीमें साक्षात्‌ श्रीहरिने अवतार ग्रहण
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.9708)
- **Original**: उत्तम ब्रतका समय है। सैकड़ों वर्षोंमें भी ऐसा किया है। वह जय और पुण्य प्रदान करती है;
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.9709)
- **Original**: योग मिले या न मिले, कुछ कहा नहीं जा इसलिये 'जयन्ती' कही गयी है। उसमें उपवास-
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.9710)
- **Original**: सकता। ऐसे उत्तम ब्रतका अनुष्ठान करके ब्रती भ्रत करके विद्वान्‌ पुरुष जागरण करे। यह समय
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.9711)
- **Original**: पुरुष अपनी करोड़ों पीढ़ियोंका उद्धार कर देता है। सबका अपवाद, मुख्य एवं सर्वसम्मत है, ऐसा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.9712)
- **Original**: जो सम्पत्तिसे रहित भक्त मनुष्य हैं, वे द्रतसम्बन्धी वेदवेत्ताओंका कथन है। पूर्वकालमें ब्रह्माजीने भी
- **Translation**: 

---

