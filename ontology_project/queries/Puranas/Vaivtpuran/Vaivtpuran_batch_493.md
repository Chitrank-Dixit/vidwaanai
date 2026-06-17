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

### Verse 1 (Vaivtpuran 28.4266)
- **Original**: ग्रस्त हो चुके थे। इन देवीने स्वयं सेना बनकर चुकी थीं। उसे देखकर समस्त नारियाँ तथा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.4267)
- **Original**: देवताओंका पक्ष ले युद्ध किया था। इनकी कृपासे बान्धवोंकी स्त्रियाँ भी रो पड़ीं। पुत्रंके असह्या
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.4268)
- **Original**: देवता विजयी हो गये थे। अतएब इनका नाम शोकके कारण माताको मूर्च्छ आ गयी।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.4269)
- **Original**: 'देवसेना' पड़ गया। महाराज प्रियव्रतकी बात मुने! राजा प्रियत्रत उस मृत बालककों
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.4270)
- **Original**: सुनकर ये उनसे कहने लगीं। लेकर श्मशानमें गये। उस एकान्त भूमिमें पुत्रको भगवती देवसेनाने कहा--राजन्‌! मैं ब्रह्माकी छातीसे चिपकाकर आँखोंसे आँसुओंकी धारा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.4271)
- **Original**: मानसी कन्या हूँ। जगत्पर शासन करनेबाली मुझ बहाने लगे। इतनेमें उन्हें वहाँ एक दिव्य विमान
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.4272)
- **Original**: देवीका नाम “देवसेना' है। विधाताने मुझे उत्पन्न दिखायी पड़ा। शुद्ध स्फटिकमणिके समान
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.4273)
- **Original**: करके स्वामी कार्तिकेवको सौंप दिया है। मैं चमकनेवाला वह विमान अमूल्य रज्नोंसे बना था।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.4274)
- **Original**: सम्पूर्ण मातृकाओंमें प्रसिद्ध हूँ। स्कन्दकी पतिब्रता तेजसे जगमगाते हुए उस विमानकी रेशमी वस्त्रोंसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.4275)
- **Original**: भार्या होनेका गौरव मुझे प्राप्त है। भगवती अनुपम शोभा हो रही थी। अनेक प्रकारके अद्भुत
- **Translation**: 

---

### Verse 11 (Vaivtpuran 28.4276)
- **Original**: मूलप्रकृतिके छठे अंशसे प्रकट होनेके कारण चित्रोंसे वह विभूषित था। पुष्पोंको मालासे वह
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.4277)
- **Original**: विश्वमें देवी 'षष्ठी' नामसे मेरी प्रसिद्धि है। मेरे सुसज्जित था। उसीपर बैठी हुई मनको मुग्ध प्रसादसे पुत्रहीन व्यक्ति सुयोग्य पुत्र, प्रियाहीन करनेवाली एक परम सुन्दरी देवीको राजा प्रिगव्रतने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.4278)
- **Original**: जन प्रिया, दरिद्री धन तथा कर्मशील पुरुष कर्मोके देखा। श्वेत चम्पाके फलके समान उनका उज्ज्वल
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.4279)
- **Original**: उत्तम फल प्राप्त कर लेते हैं। राजन्‌! सुख, वर्ण था। सदा सुस्थिर तारुण्यसे शोभा पानेवाली
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.4280)
- **Original**: दुःख, भय, शोक, हर्ष, मड्भल, सम्पत्ति और वे देवी मुस्करा रही थीं। उनके मुखपर प्रसन्नता
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.4281)
- **Original**: विपत्ति--ये सब कर्मके अनुसार होते हैं। अपने छायी थी। रत्रमय भूषण उनकी छवि बढ़ाये हुए
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.4282)
- **Original**: ही कर्मके प्रभावसे पुरुष अनेक पुत्रोंका पिता थे। योगशास्त्रमें पारंगत वे देवी भक्तोंपर अनुग्रह
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.4283)
- **Original**: होता है और कुछ लोग पुत्रहीन भी होते हैं। करनेके लिये आतुर थीं। ऐसा जान पड़ता था
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.4284)
- **Original**: किसीको मरा हुआ पुत्र होता है और किसीको मानो वे मूर्तिमती कृपा ही हों। उन्हें सामने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.4285)
- **Original**: दीर्घजीवी-यह कर्मका ही फल है। गुणी, विराजमान देखकर राजाने बालककों भूमिपर रख
- **Translation**: 

---

