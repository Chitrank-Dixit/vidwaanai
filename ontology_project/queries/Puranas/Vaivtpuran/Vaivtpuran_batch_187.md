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

### Verse 1 (Vaivtpuran 13.3109)
- **Original**: प्राप्त कर लोगी।' इस प्रकार कहकर देवेश्वर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.3110)
- **Original**: श्डड + संक्षिप्त श्रह्म॑वैश्वर्तपुराण + भगवान्‌ श्रीकृष्ण भी अन्तर्धान हो गये। गुरो!
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.3111)
- **Original**: तुलसीके मुखपर हँसी छा गयी। उसके मनमें मैंने अपना वह शरीर त्याग दिया और अब इस
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.3112)
- **Original**: अपार हर्ष हुआ। उसने महाभाग ब्रह्माको प्रणाम भूमण्डलपर उत्पन्न हुई हूँ। सुन्दर विग्रहवाले
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.3113)
- **Original**: किया और वह कहने लगी। शान्तस्वरूप भगवान्‌ नारायणको मैं प्रियतम तुलसीने कहा--पितामह! मैं बिलकुल पतिरूपसे प्राप्त करनेके लिये वर माँग रही हूँ।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.3114)
- **Original**: सच्ची बातें कहती हूँ--दो भुजासे शोभा पानेवाले आप मेरी अभिलाषा पूर्ण करनेकी कृपा करें।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.3115)
- **Original**: श्यामसुन्दर भगवान्‌ श्रीकृष्णकों पानेके लिये मेरी ख्रह्माजी बोले-- भगवान्‌ श्रीकृष्णके अज़्से जैसी अभिलाषा है, बैसी चतुर्भुज श्रीविष्णुके प्रकट सुदामा नामक एक गोप भी इस समय
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.3116)
- **Original**: लिये नहीं है; परंतु उन गोबिन्दकी आज्ञासे ही राधिकाके शापसे भारतवर्षमें उत्पन्न है। उस परम
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.3117)
- **Original**: मैं चतुर्भुज श्रीहरिके लिये प्रार्थना करती हूँ। तेजस्वी गोपको श्रीकृष्णका साक्षात्‌ अंश कहते
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.3118)
- **Original**: ओह! बे गोविन्द मेरे लिये परम दुर्लभ हो गये हैं। शापवश उसे दनुके कुलमें उत्पन्न होना पड़ा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.3119)
- **Original**: हैं। भगवन्‌। आप ऐसी कृपा करें कि उन्हीं है। 'शड्खचूड़” नामसे वह प्रसिद्ध है। त्रिलोकीमें गोविन्दकों मैं पुनः निश्चय ही प्राप्त कर सकूँ। कोई भी ऐसा नहीं है जो उससे बढ़कर हो।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.3120)
- **Original**: साथ ही मुझे राधाके भयसे भी मुक्त कर दीजिये। वह सुदामा इस समय समुद्रमें विराजमान है।। . ब्रह्माजी बोले--देवी ! मैं तुम्हारे प्रति भगवती भगवान्‌ श्रीकृष्णका अंश होनेसे उसे पूर्वजन्मकी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.3121)
- **Original**: राधाके षोडशाक्षर-मन्त्रका उपदेश करता हूँ। तुम सभी बातें स्मरण हैं। सुन्दरि! शोभने! तुम भी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.3122)
- **Original**: इसे हृदयमें धारण कर लो। मेरे बरके प्रभावसे पूर्वजन्मके सभी प्रसड्रोंसे परिचित हो। इस
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.3123)
- **Original**: अब तुम राधाको प्राणके समान प्रिय बन जाओगी। जन्ममें वह श्रीकृष्णका अंश तुम्हारा पति होगा।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.3124)
- **Original**: सुभगे! भगवान्‌ गोविन्दके लिये तुम वैसी ही इसके बाद शान्तस्वरूप भगवान्‌ नारायण तुम्हें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.3125)
- **Original**: प्रेयसी बन जाओगी जैसी राधा हैं। पतिरूपसे प्राप्त होंगे। लीलावश वे ही नारायण। मुने! इस प्रकार कहकर जगद्धाता ब्रह्माने तुमको शाप दे देंगे। अतः अपनी कलासे तुम्हें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.3126)
- **Original**: तुलसीकों भगवती राधाका षोडशाक्षर-मन्त्र बता वृक्ष बनकर भारतमें रहना पड़ेगा और समस्त
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.3127)
- **Original**: दिया। साथ ही स्तोत्र, कवच, पूजाकी सम्पूर्ण जगत्‌को पवित्र करनेकी योग्यता तुम्हें प्राप्त होगी।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.3128)
- **Original**: विधियाँ तथा किस क्रमसे अनुष्ठान करना सम्पूर्ण पुष्पोंमें तुम प्रधान मानी जाओगी। भगवान्‌
- **Translation**: 

---

