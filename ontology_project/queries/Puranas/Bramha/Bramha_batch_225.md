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

### Verse 1 (Bramha 0.4481)
- **Original**: भी ऐसा ही करें। भगवान्‌ नारायण तीनों शरीरमें लग गयीं तथा अपने हाथकी अंगुलियोंसे
- **Translation**: 

---

### Verse 2 (Bramha 0.4482)
- **Original**: लोकोंके एकमात्र आश्रय हैं। उनकी अनन्य पसीनेका जल पोंछकर फेंका। उस जलसे
- **Translation**: 

---

### Verse 3 (Bramha 0.4483)
- **Original**: चित्तसे उपासना करो।' पहले धर्मका प्रादुर्भाव हुआ। उसके बाद
- **Translation**: 

---

### Verse 4 (Bramha 0.4484)
- **Original**: भगवान्‌ शिवकी आज्ञासे इत्र गज्गाजीके लक्ष्मी प्रकट हुईं। फिर दान, उत्तम वृष्टि,
- **Translation**: 

---

### Verse 5 (Bramha 0.4485)
- **Original**: दक्षिण-तटपर मुनीश्चवर आपस्तम्बके पास गये सत्त्व, सरोवर, धान्य, पुष्प, फल, शस्त्र, शास्त्र,
- **Translation**: 

---

### Verse 6 (Bramha 0.4486)
- **Original**: और उनको साथ लेकर फेना तथा गद्जाके गृहोपयोगी अस्त्र, तीर्थ, बन तथा चराचर
- **Translation**: 

---

### Verse 7 (Bramha 0.4487)
- **Original**: पविश्न संगमपर भाँति-भाँतिके वैदिक मन्त्रों एवं जगत्‌का आविर्भाव हुआ। देवि! यह सब ! तपस्याके द्वारा भगवान्‌ जनार्दनकी स्तुति करने पापरहित सृष्टि थी। भगवती उमा! तुम्हारे
- **Translation**: 

---

### Verse 8 (Bramha 0.4488)
- **Original**: लगे। उनकी स्तुतिसे भगवान्‌ विष्णुकों बड़ी प्रभावसे संसारमें प्रचुर सुखकी वृद्धि हुई। सदा
- **Translation**: 

---

### Verse 9 (Bramha 0.4489)
- **Original**: प्रसन्नता हुई और वे प्रत्यक्ष प्रकट होकर सब ओर मज़जलमय कृत्य शोभा पाने लगे।! बोले-'इन्र! तुम्हें क्या वरदान दूँ?” वे बोले--'मुझे जगदम्ब! तुम सम्पूर्ण जगत्‌की स्वामिनी हो
- **Translation**: 

---

### Verse 10 (Bramha 0.4490)
- **Original**: एक ऐसा वीर दीजिये, जो मेरे शत्रुका वध कर और हम भयसे डरे हुए हैं। अत: तुम हमारी
- **Translation**: 

---

### Verse 11 (Bramha 0.4491)
- **Original**: सके।' भगवान्‌ने कहा-“दे दिया।' फिर तो रक्षा करो। कोई तर्क करते-करते मोहित हो
- **Translation**: 

---

### Verse 12 (Bramha 0.4492)
- **Original**: शिव, गड्जा तथा विष्णुके प्रसादसे जलके भोतरसे जाते हैं और कोई उसीमें लीन रहते हैं। परन्तु
- **Translation**: 

---

### Verse 13 (Bramha 0.4493)
- **Original**: एक पुरुष प्रकट हुआ। उसने भगवान्‌ शिव और हम तो शिव और शक्तिके सुन्दर अद्वत रूपको
- **Translation**: 

---

### Verse 14 (Bramha 0.4494)
- **Original**: विष्णु दोनोंके स्वरूप धारण किये थे। उसके सर्वदा नमस्कार करते हैं। हाथमें चक्र भी था और त्रिशूल भी। उसने इस प्रकार स्तुति करनेवाले इन्द्रके समक्ष
- **Translation**: 

---

### Verse 15 (Bramha 0.4495)
- **Original**: रसातलपें जाकर इन्द्रशत्ु महाशनिका वध किया। भगवान्‌ शंकर प्रकट हुए और बोले--' देवराज!
- **Translation**: 

---

### Verse 16 (Bramha 0.4496)
- **Original**: उसका नाम अब्जक और वृषाकषि हुआ। बह तुम क्‍या चाहते हो? अपना अभीष्ट मनोरथ
- **Translation**: 

---

### Verse 17 (Bramha 0.4497)
- **Original**: इन्द्रका सखा बन गया। इन्द्र स्वर्गमें रहते हुए कहो।' इन्द्रने कहा-' भगवन्‌! मेरा बलवान्‌
- **Translation**: 

---

### Verse 18 (Bramha 0.4498)
- **Original**: भी प्रतिदिन वृषाकपिके पास आते थे। उन्हें शत्रु महाशनि, जो देखनेमें वज़के समान भयंकर
- **Translation**: 

---

### Verse 19 (Bramha 0.4499)
- **Original**: अन्यत्र आसक्त देख शचीके हृदयमें प्रणणकोपका है, मुझे याँधकर रसातल ले गया था। वहाँ उसने
- **Translation**: 

---

### Verse 20 (Bramha 0.4500)
- **Original**: उदय हुआ। अनेक बार मेरा तिरस्कार किया और बचनरूपी
- **Translation**: 

---

