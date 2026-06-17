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

### Verse 1 (Vaivtpuran 13.3089)
- **Original**: किया। तब जगत्‌की सृष्टि करनेमें निपुण देखकर किसीके साथ तुलना करनेमें असमर्थ
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.3090)
- **Original**: विधाताने उससे कहा। हो जाते थे; अतएव विद्वानू पुरुषोंने उसका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.3091)
- **Original**: गब्रह्माजी बोले--तुलसी ! तुम मनो$भिलषित नाम 'तुलसी' रखा। भूमिपर पधारते ही वह
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.3092)
- **Original**: वर माँग सकती हो। भगवान्‌ श्रीहरिको भक्ति, ऐसी सुयोग्या बन गयी, मानो साक्षात्‌ प्रकृति
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.3093)
- **Original**: उनको दासी बनना अथवा अजर एवं अमर देवी हो हो।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.3094)
- **Original**: होना जो भी तुम्हारी इच्छा हो, मैं देनेके लिये सब लोगोंके मना करनेपर भी उसने तपस्या
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.3095)
- **Original**: तैयार हूँ। करनेके विचारसे बदरीवनको प्रस्थान किया। वहाँ
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.3096)
- **Original**: तुलसीने कहा--तात पितामह ! सुनिये, मेरे रहकर बह दीर्घकालतक कठिन तपस्या करती
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.3097)
- **Original**: मनमें जो अभिलाषा है, उसे बता रही हूँ, आप सर्वज्ञ हैं; अत: आपके सामने मुझे लज्जा ही क्या है। पूर्बजन्ममें मैं तुलसी नामकी गोपी थी। 33
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.3098)
- **Original**: हट ् गोलोक मेरा निबास-स्थान था। भगवान्‌ श्रीकृष्णकी “छू:
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.3099)
- **Original**: प्रिया, उनकी अनुचरी, उनकी अर्द्धाड्नी तथा .....75»#
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.3100)
- **Original**: उनकी प्रेयली सखी-सब कुछ होनेका सौभाग्य «5
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.3101)
- **Original**: मुझे प्राप्त था। गोविन्द नामसे सुशोभित उन प्रभुके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.3102)
- **Original**: साथ मैं हास-बिलासमें रत थी। उस परम सुखसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.3103)
- **Original**: अभी मैं तृप्त नहीं थी। इतनेमें एक दिन रासकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.3104)
- **Original**: अधिष्ठात्री देवी भगवती राधाने रासमण्डलमें रही। उसके मनका निश्चित उद्देश्य यह था कि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.3105)
- **Original**: पधारकर रोषसे मुझे यह शाप दे दिया कि 'तुम स्वयं भगवान्‌ नारायण मेरे स्वामी हों। ग्रीष्मकालमें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.3106)
- **Original**: मानव-योनिमें उत्पन्न होओ।' उसी समय भगवान्‌ वह पश्चाग्रि तपती और जाड़ेके दिनोंमें जलमें गोबिन्दने मुझसे कहा--'देवी! तुम भारतवर्षमें रहकर तपस्या करती। वर्षा-ऋतुमें वह वृष्टिकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.3107)
- **Original**: रहकर तपस्या करो। ब्रह्मा बर देंगे, जिससे मेरे धाराका वेग सहन करती हुई खुले मैदानमें आसन
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.3108)
- **Original**: स्वरूपभूत अंश चतुर्भुज श्रीविष्णुको तुम पतिरूपसे लगाकर बैठी रहती। हजारों वर्षोतक वह फल
- **Translation**: 

---

