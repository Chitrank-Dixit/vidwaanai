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

### Verse 1 (Vaivtpuran 13.11002)
- **Original**: लाल रंगके ओठ पके बिम्बफलको लज्जित कर यह शीघ्र हमें इसी समय बता दो। रहे थे। वे परिपक्व अनारके दानोंकी भाँति सुन्दर गोपोंकी बात सुनकर ब्राह्मणियाँ हर्षसे खिल
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11003)
- **Original**: दन्तपर्कक्त धारण किये थे। सिरपर मोरपंखका उठीँ। उनके नेश्रोंमें आनन्दके आँसू छलक आये।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11004)
- **Original**: मुकुट शोभा दे रहा था। कानोंके मूलभागमें दो सारे अज्भ पुलकित हो उठे। उनके मनमें बड़ी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11005)
- **Original**: कदम्बके फूल उनकी शोभा बढ़ा रहे थे। वे इच्छा थी कि हमें श्रीकृष्ण-चरणोंके दर्शन हों।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11006)
- **Original**: परात्पर परमात्मा योगियोंके भी ध्यानमें नहीं उन्होंने सोने, चाँदी और फूलकी थालियोंमें
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11007)
- **Original**: आनेवाले हैं। तथापि भक्तोंपर अनुग्रह करनेके प्रसब्नतापूर्वक भाँति-भाँतिके व्यञ्ञनोंसे युक्त अत्यन्त
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11008)
- **Original**: लिये व्याकुल रहते हैं। ब्रह्मा, शिव, धर्म, शेषनाग मनोहर अगहनीके चावलका भात, खीर, स्वादिष्ट
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11009)
- **Original**: तथा बड़े-बड़े मुनीश्चर उनकी स्तुति करते हैं। पीठा, दही, दूध, घी और मधु रखकर श्रीकृष्णके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11010)
- **Original**: ऐसे परमेश्वरके दर्शन करके नब्राह्मणपत्रियोंने निकट प्रस्थान किया। वे मन-ही-मन नाना
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11011)
- **Original**: भक्तिभावसे उन्हें प्रणाम किया और अपने ज्ञानके प्रकारके मनोरध लेकर जानेको उत्सुक हुईं। अनुरूप उन मधुसूदनकी स्तुति की। ब्राह्मणपत्नरियाँ धन्य और पतिन्नतपरायणा थीं। किए 170 कक. इसीलिये उनके मनमें श्रीकृष्णदर्शनकी उत्कण्ठा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11012)
- **Original**: . ह पक जाग उठी। उन्होंने वहाँ पहुँचकर बालकोंसहित
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11013)
- **Original**: अन्थि 4 श्रीकृष्ण और बलरामके दर्शन किये। श्रीकृष्ण
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11014)
- **Original**: 60 बटके मूलभागके निकट बालकोंके बीचमें बैठे थे; अत: तारोंके बीच विराजमान चन्द्रमाके समान
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11015)
- **Original**: £5 शोभा पा रहे थे। श्याम अज्र, किशोर अवस्था
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11016)
- **Original**: /# (06 और शरीरपर रेशमी पीताम्बरसे वे बड़े सुन्दर 83 लगते थे। मुखपर मन्द मुस्कान खेल रही थी। [77] शान्तस्वरूप राधाकान्त बड़े मनोहर प्रतीत होते थे। उनका मुख शरत्कालकी पूर्णिमाके चन्द्रमाको विप्रपत्रियाँ बोलीं-- भगवन्‌! आप स्वयं लज्जित कर रहा था। वे रत्रमय अलंकारोंसे ही परब्रह्म, परमधाम, निरीह, अहड्ढभगररहित, विभूषित थे तथा रत्ननिर्मित दो कुण्डलोंसे उनके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11017)
- **Original**: निर्गुण-निराकार तथा सगुण-साकार हैं। आप ही गण्डस्थलकी बड़ी शोभा हो रही थी। हाथोंमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11018)
- **Original**: सबके साक्षी, निर्लेप एवं आकाररहित परमात्मा रत्रमय केयूर और कड्भरन तथा पैरोंमें रत्ननिर्मित हैं। आप ही प्रकृति-पुरुष तथा उन दोनोंके परम नूपुर उनके आभूषण थे। उन्होंने गलेमें आजानुलम्बिनी
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11019)
- **Original**: कारण हैं। सृष्टि, पालन और संहारके विषयमें शुभ्र रत्रमाला धारण कर रखी थीं। मालतीकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11020)
- **Original**: नियुक्त जो ब्रह्मा, विष्णु और शिव--ये तीन देवता मालासे उनके कण्ठ और वक्ष:स्थल दोनों
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11021)
- **Original**: कहे गये हैं, वे भी आपके ही सर्वबीजमय अंश सुशोभित थे। चन्दन, अगुरु, कस्तूरी और
- **Translation**: 

---

