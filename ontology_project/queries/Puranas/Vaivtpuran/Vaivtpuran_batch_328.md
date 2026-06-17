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

### Verse 1 (Vaivtpuran 15.8690)
- **Original**: संकटमें पड़ गये हैं। दैत्योंने हमें ग्रस लिया। वहाँ उसने देखा, देवेश्वर ब्रह्मा ब्रह्मतेजसे जाज्वल्यमान
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.8691)
- **Original**: आप ही जगतके स्रष्टा हैं, शीघ्र ही हमारा उद्धार हो रहे हैं तथा बड़े-बड़े ऋषि, मुनीन्र तथा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.8692)
- **Original**: कीजिये। ब्रह्मन्‌! आप हो इस पृथ्वीकी गति हैं; सिद्धेद्रगण सानन्द उनकी सेवामें उपस्थित हैं।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.8693)
- **Original**: इसे शान्ति प्रदान करें। पितामह! यह पृथ्वी ब्रह्माजी 'कृष्ण” इस दो अक्षरके परक्रह्मस्वरूप
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.8694)
- **Original**: जिस भारसे पीड़ित है, उसीसे हम भी दुःस्वी मन्त्रका जप कर रहे थे। उनके नेत्र भक्तिजनित
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.8695)
- **Original**: हैं, अतः आप उस भारका हरण कीजिये।' आनन्दके आँसुओंसे भरे थे तथा सम्पूर्ण अड्ञोमें।. देबवताओंकी बात सुनकर जगत्स्रष्टा रोमाञ्न हो आया था। मुने! देवताओंसहित पृथ्वीने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.8696)
- **Original**: ब्रह्माने पृथ्वीसे पूछा--' बेटी ! तुम भय छोड़कर भक्तिभावसे चतुराननको प्रणाम किया और दैत्योंके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.8697)
- **Original**: मेरे पास सुखपूर्वक रहो। पद्मलोचने! बताओ, भार आदिका सारा वृत्तान्त कह सुनाया। आँसूभरे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.8698)
- **Original**: किनका ऐसा भार आ गया है, जिसे सहन करनेमें नेत्रों और पुलकित शरीरसे वह ब्रह्माजीकी स्तुति
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.8699)
- **Original**: तुम असमर्थ हो गयी हों। भद्गे! मैं उस भारको तथा रोदन करने लगी। दूर करूँगा। निश्चय ही तुम्हारा भला होगा। तब जगद्धाता ब्रह्मने उससे पूछा--भट्े !
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.8700)
- **Original**: ब्रह्माजीका यह वचन सुनकर पृथ्वीके मुखपर तुम क्‍यों स्तुति करती और रोती हो? बताओ,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.8701)
- **Original**: और नेत्रोंमें प्रसन्नता छा गयी। वह जिस-जिस # 5
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.8702)
- **Original**: 402 + संक्षिप्त ब्रह्मवैवर्तपुराण * ।444
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.8703)
- **Original**: ।4/048/04।4 44 । । 44444 454505554440 5495 5050.55--2>><4<5<##ूूूूननने $$%ऋऋऋ#ऋ######& ## # ## #ऋऊ$% 4 # 6 # ####### 4 ######%#%$%%%%$ कारणसे इस तरह पीड़ित थी, अपनी पीड़ाकी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.8704)
- **Original**: ट्वेष करते हैं; उनके भारसे मैं पीड़ित रहती हूँ। उस कथाकों कहने लगी--'तात! सुनिये, मैं
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.8705)
- **Original**: विधे! शद्बुचूड़के भारसे जिस तरह मैं पीड़ित थी, अपने मनकी व्यथा बता रही हूँ। विश्वासी बन्धु-
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.8706)
- **Original**: उससे भी अधिक दैत्योंके भारसे पीड़ित हूँ। बान्धवके सिवा दूसरे किसीको मैं यह बात नहीं
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.8707)
- **Original**: प्रभो! यह सब कष्ट मैंने कह सुनाया। यही मुझ बता सकती; क्योंकि स्त्री-जाति अबला होती है।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.8708)
- **Original**: अनाथाका निवेदन है। यदि आपसे मैं सनाथ हूँ अपने सगे बन्धु, पिता, पति और पुत्र सदा उसकी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.8709)
- **Original**: तो आप मेरे कष्टेके निवारणका उपाय कीजिये।' रक्षा करते हैं; परंतु दूसरे लोग निश्रय ही उसकी
- **Translation**: 

---

