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

### Verse 1 (Vaivtpuran 16.3614)
- **Original**: समयतक तो चक्कर काटता रहा। तदनन्तर वह कहा--' हाँ, हाँ, बहुत ठीक--आप जो चाहें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3615)
- **Original**: शद्भुचूड़के ऊपर जा गिरा। उसके गिरते ही तुरंत सो ले सकते हैं।' तब अतिशय माया फैलाते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3616)
- **Original**: वह दानवेश्वर तथा उसका रथ--सभी जलकर हुए उन वृद्ध ब्राह्मणने कहा-“मैं तुम्हारा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3617)
- **Original**: भस्म हो गये।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3618)
- **Original**: दानव-शरीरके भस्म होते ही उसने एक
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3619)
- **Original**: पूजामें निरन्तर पवित्र माना जाता है। उसके दिव्य गोपका बेष धारण कर लिया। उसकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3620)
- **Original**: जलको श्रेष्ठ मानते हैं; क्योंकि देवताओंको प्रसन्न किशोर अवस्था थी। वह दो दिव्य भुजाओंसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3621)
- **Original**: करनेके लिये वह अचूक साधन है। उस पवित्र सुशोभित था। उसके हाथमें मुरली शोभा पा रही
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3622)
- **Original**: जलको तीर्थमय माना जाता है। उसके प्रति केवल थी और रत्रमय आभूषण उसके शरीरकों विभूषित
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3623)
- **Original**: शंकरकी आदरबुद्धि नहों है। जहाँ-कहीं भी कर रहे थे। इतनेमें अकस्मात्‌ सर्वोत्तम दिव्य
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3624)
- **Original**: शद्भुध्वनि होती है, वहाँ लक्ष्मीजी सम्यक्‌ प्रकारसे मणियोंद्वारा निर्मित एक दिव्य विमान गोलोकसे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3625)
- **Original**: विराजमान रहती हैं। जो शद्डुके जलसे स्नान कर उतर आया। उसमें चारों ओर असंख्य गोपियाँ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3626)
- **Original**: लेता है, उसे सम्पूर्ण तीर्थो्में स्नानका फल प्राप्त हो बैठी थीं। शब्बचूड़ उसीपर सवार होकर गोलोकके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3627)
- **Original**: जाता है। शह्लु साक्षात्‌ भगवान्‌ श्रीहरिका अधिष्ठान लिये प्रस्थित हो गया। है। जहाँपर शद्गु रहता है, वहाँ भगवान्‌ श्रीहरि मुने! उस समय वृन्दावनमें रासमण्डलके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3628)
- **Original**: भगवती लक्ष्मीसहित सदा निवास करते हैं। मध्य भगवान्‌ श्रीकृष्ण और भगवती श्रीराधिका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3629)
- **Original**: अमड्भल दूरसे ही भाग जाता है। विराजमान थीं। वहाँ पहुँचते ही शह्बुचूड़ने भक्तिक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3630)
- **Original**: . उधर शिव भी शब्बुचूड़कों मारकर अपने साथ मस्तक झुकाकर उनके चरणकमलोंमें साष्टाड़्
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3631)
- **Original**: लोकको पधार गये। उनके मनमें अपार हर्ष था। प्रणाम किया। अपने चिरसेवक सुदामाकों देखकर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3632)
- **Original**: वे वृषभपर आरूढ़ होकर अपने गणोंसहित चले उन दोनोंके श्रीमुख प्रसन्नतासे खिल उठे। उन्होंने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3633)
- **Original**: गये। अपना राज्य पा जानेके कारण देवताओंके अत्यन्त प्रसन्न होकर उसे अपनी गोदमें उठा
- **Translation**: 

---

