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

### Verse 1 (Vaivtpuran 4.8967)
- **Original**: रमणीय भूषण उनकी शोभा बढ़ाते थे। बारह लाख उसकी रक्षाके लिये व्रजराज बसुभानु नियुक्त थे।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8968)
- **Original**: गोप आज्ञाके अधीन रहकर राजाधिराजकी भाँति देवतालोग उनसे मिले। वे किशोर-अवस्थाके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8969)
- **Original**: उनकी शोभा बढ़ाते थे। उनका मुखारविन्द प्रसन्नतासे सुन्दर एवं श्रेष्ठ पुरुष थे। हाथमें मणिमय दण्ड
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8970)
- **Original**: खिला था। वे रत्रमय सिंहासनपर विराजमान थे। लिये हुए थे। रमणीय आभूषणोंसे विभूषित हो
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8971)
- **Original**: उनके हाथमें बेंतकी छड़ी शोभा पाती थी। रत्नसिंहासनपर बैठे थे। पके बिम्बफलके समान। बे तीनों देवेश्वर उनसे बातचीत करके लाल ओषछ्ठ और मन्द-मन्द मुस्कानसे वे अत्यन्त
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8972)
- **Original**: प्रसन्नतापूर्वकत आठवें द्वारपर गये। वह पूर्वोक्त मनोहर दिखायी देते थे। सातों द्वारोंसे विलक्षण एबं विचित्र शोभाशाली देवतालोग उनसे पूछकर पाँचवें ट्वारपर गये।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8973)
- **Original**: था। वहाँ उन्होंने सुपार्थ नामक मनोहर द्वारपालको वह हीरेकी दीवारोंपर अक्लित विचित्र चित्रोंसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8974)
- **Original**: देखा, जो मन्द मुस्कराहटके साथ बड़े सुन्दर अत्यन्त प्रकाशमान दिखायी देता था। वहाँ देवभानु
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8975)
- **Original**: दिखायी देते थे। वे भालदेशमें धारित चन्दनके नामक द्वारपाल मिले, जो रत्॒मय आभूषण धारण
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8976)
- **Original**: तिलकसे अत्यन्त उद्धासित दिखायी देते थे। करके मनोहर सिंहासनपर आसीन थे। उनके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8977)
- **Original**: उनके ओठ बन्धुजीवपुष्प (दुपहरिया)-के समान मस्तकपर मोरपंखका मुकुट शोभा दे रहा था और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8978)
- **Original**: लाल थे। रत्नोंके कुण्डल उनके गण्डस्थलको वे रत्नोंक हारसे अलंकृत थे। कदम्बोंके पुष्पसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8979)
- **Original**: अलंकृत किये हुए थे। वे समस्त अलंकारोंकी सुशोभित, उत्तम रत्नमय कुण्डलोंसे प्रकाशित तथा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8980)
- **Original**: शोभासे सम्पन्न थे। रत्रमय दण्ड धारण करते थे चन्दन, अगुरु, कस्तूरी और कुंकुमके द्रवसे चर्चित
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8981)
- **Original**: और उनके साथ बारह लाख गोप थे। वहाँसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8982)
- **Original**: *-श्रीकृष्णजन्मखण्ड * डर )घ 2 )] 2) )0])4)3])3]3]4] 8
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8983)
- **Original**: 7((7(4]77044]0]0)
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8984)
- **Original**: 0 7 8 3] 3 28020 250 4. अनुमति मिलनेपर वे देवता शीघ्र ही नें अभीष्ट
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8985)
- **Original**: हुई बहुत-सी वेदिकाएँ प्रकाशित हो रही थीं। द्वारपर गये। वहाँ हीरे आदि उत्तम रत्रोंकी चार
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8986)
- **Original**: वह विचित्र द्वार सबके लिये दुर्लभ, अदृश्य और वेदियाँ बनी थीं। वह द्वार अपूर्व चित्रोंसे सज्जित
- **Translation**: 

---

