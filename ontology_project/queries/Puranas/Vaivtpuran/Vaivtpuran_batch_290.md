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

### Verse 1 (Vaivtpuran 13.11942)
- **Original**: 685 5 % 5 % 5%%%ऋशऋ 4666 %%ऋ##ऋऋ# ऋ#
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11943)
- **Original**: # # # 6 % कक # क कुषित हो उठे। उन्होंने राजाके सामने ही अपनी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11944)
- **Original**: वहाँसे भयभीत होकर भागे। अब वे डरकर एक जटा तोड़ डाली। उस जटासे शीघ्र ही एक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11945)
- **Original**: कैलास पर्वतपर भगवान्‌ शंकरकी शरणमें पुरुष प्रकट हुआ, जो अग्निशिखाके समान
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11946)
- **Original**: गये और बोले-'कृपानिधान! हमारी रक्षा तेजस्वी था। उसके हाथमें तलवार थी। वह
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11947)
- **Original**: कीजिये।' भगवान्‌ शिव सर्वज्ञ हैं। उन्होंने महाभयंकर पुरुष महाराज अम्बरीषको मार
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11948)
- **Original**: ब्राह्मण दुर्वासाका कुशल-समाचारतक नहीं डालनेके लिये उद्यत हो गया। यह देख करोड़ों [पूछा। जो क्षणभरमें जगत्‌का संहार करनेमें सूर्योंके समान प्रकाशमान श्रीहरिके सुदर्शनचक्रने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11949)
- **Original**: समर्थ तथा दीन-दुःखियोंके स्वामी हैं, वे उस कृत्या-पुरुषको काट डाला। अब वह बाबा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11950)
- **Original**: महादेवजी मुनिसे बोले। दुर्वासाको भी काटनेके लिये उच्चत हुआ। यह
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11951)
- **Original**: शंकरजीने कहा--द्विजश्रेष्ट ! सुस्थिर होकर देख विप्रवर दुर्वासा भयसे व्याकुल हो भाग चले मेरी बात सुनो। मुने! तुम महर्षि अत्रिके पुत्र तथा उन्होंने अपने पीछे-पीछे प्रज्वलित अग्निशिखाके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11952)
- **Original**: जगत्स्नष्टा ब्रह्माजीके पौत्र हो। वेदोंके विद्वान तथा समान तेजस्वी चक्रको आते देखा। वे अत्यन्त
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11953)
- **Original**: सर्वज्ञ हो, परंतु तुम्हारा कर्म मूखोंके समान है। व्याकुल हो सारे ब्रह्माण्डका चक्कर लगाते-लगाते
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11954)
- **Original**: बेदों, पुराणों और इतिहासॉमें सर्वत्र जिन सर्वेश्वरका थक गये, खिन्न हो गये और ब्रह्माजीको सम्पूर्ण
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11955)
- **Original**: निरूपण हुआ है; उन्हींको तुम मूढ़ मनुष्यकी जगत्‌का रक्षक मान उनकी शरणमें गये।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11956)
- **Original**: भाँति नहीं जानते हो। जिनके भ्रूभड्की लीलामात्रसे *बचाइये-बचाइये '--पुकारते हुए उन्होंने ब्रह्माजीकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11957)
- **Original**: मैं, ब्रह्मा, रुद्र, आदित्य, वसु, धर्म, इन्द्र, सम्पूर्ण सभामें प्रवेश किया। ब्रह्माजीने उठकर विप्रवर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11958)
- **Original**: देवता, मुनीन्द्र और मनु उत्पन्न और विलीन होते दुर्वासाका कुशल-मज़ल पूछा। तब उन्होंने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11959)
- **Original**: रहते हैं; उन्हीं श्रीहरिके प्राणोंसे भी बढ़कर प्रिय आदिसे ही सारा वृत्तान्त विस्तारपूर्वक कह
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11960)
- **Original**: भक्तको तुम किसकी शक्तिसे मारने चले थे? सुनाया। सुनकर ब्रह्माजीने लम्बी साँस ली और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11961)
- **Original**: उनका चक्र उन्हींके तुल्य तेजस्वी है। उसे रोकना भयसे व्याकुल होकर कहा। सर्वथा कठिन है। उस चक्रको यद्यपि उन्होंने ब्रह्माजीनी कहा--बेटा! तुम किसके
- **Translation**: 

---

