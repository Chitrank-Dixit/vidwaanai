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

### Verse 1 (Vaivtpuran 13.11922)
- **Original**: शीघ्र ही आ रहा हूँ, क्षणभर प्रतीक्षा करो।' ऐसा राजा अम्बरीष बड़े भारी जितेन्द्रिय, शान्तस्वरूप
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11923)
- **Original**: कहकर मुनि चले गये। तथा विष्णुसम्बन्धी ब्रतोंके पालनमें तत्पर रहते
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11924)
- **Original**: ब्राह्मण दुर्वासके चले जानेपर राजर्षि थे। वे एकादशीका व्रत रखते और श्रीकृष्णकी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11925)
- **Original**: अम्बरीषको बड़ी भारी चिन्ता हुई। द्वादशी तिथि आराधनामें संलग्र रहते थे। उनके सारे कर्म
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11926)
- **Original**: प्रायः बीत चली है; यह देख वे डर गये। इसी श्रीकृष्णको समर्पित थे और वे उनमें कभी लिप्त
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11927)
- **Original**: समय गुरु वसिष्ठ वहाँ आ गये। तब प्रसन्नतापूर्वक नहीं होते थे। उन्हें नमस्कार करके राजाने सारी बातें उन्हें भगवान्‌का सोलह अरोंसे युक्त और अत्यन्त
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11928)
- **Original**: बतायीं और पूछा--“गुरुदेब! मुनिवर दुर्वासा तीक्ष्ण जो सुदर्शन नामक चक्र है, वह करोड़ों
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11929)
- **Original**: अभीतक आ नहीं रहे हैं और पारणाके लिये सूर्योके समान प्रकाशमान तथा श्रीहरिके ही तुल्य
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11930)
- **Original**: विहित द्वादशी तिथि बीती जा रही है। ऐसे तेजस्वी है। ब्रह्मा आदि भी उसकी स्तुति करते
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11931)
- **Original**: संकटके समय मुझे क्या करना चाहिये? इसपर हैं। वह अस्त्र देवताओं और असुरोंसे भी पूजित
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11932)
- **Original**: भलीभाँति विचार करके मुझे शीघ्र बताइये कि है। भगवानने अपने उस चक्रकों राजाकी निरन्तर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11933)
- **Original**: कया करना शुभ है और कया अशुभ?! रक्षाके लिये उनके पास ही रख दिया था। वसिष्ठजीने कहा--द्वादशीको बिताकर एक समयकी बात है। राजा अम्बरीष
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11934)
- **Original**: त्रयोदशीमें पारण करना पाप है और अतिथिसे एकादशी-बव्रतका अनुष्ठान करके द्वादशीके दिन
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11935)
- **Original**: पहले भोजन कर लेना भी पाप है। ऐसी दशामें समयानुसार विधिपूर्वक स्नान और पूजन करके तुम भोजन न करके भगवान्‌का चरणोदक ले ब्राह्मणोंको भोजन करा स्वयं भी भोजनके लिये
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11936)
- **Original**: लो। इससे पारणा भी हो जायगी और अतिथिकी बैठे। इसी समय तपस्वी ब्राह्मण दुर्वासा भूखसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11937)
- **Original**: अवहेलना भी नहीं होगी। व्याकुल हो वहाँ राजाके समक्ष आ गये। उन्होंने।.. महामुने! ऐसा कहकर ब्रह्मपुत्र वसिष्ठजी दण्ड और छत्र ले रखा था, उनके शरीरपर श्वेत चुप हो गये। राजाने श्रीकृष्ण-चरणारविन्दोंका वस्त्र शोभा पा रहे थे। ललाटमें उज्वल तिलक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11938)
- **Original**: चिन्तन करते हुए थोड़ा-सा चरणोदक पी लिया। चमक रहा था। सिरपर जटाएँ थीं और शरीर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11939)
- **Original**: ब्रह्मन्‌! इतनेमें ही मुनीश्चर दुर्वासा आ पहुँचे। अत्यन्त कृश हो रहा था। वे ज़स्त-से जान पड़ते
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11940)
- **Original**: वे सर्वज्ञ तो थे ही, अपना अपमान समझकर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11941)
- **Original**: 528 न संक्षिप्त ब्रह्मवैबर्तपुराण ह £मफससफमम कप ऋ कफ ऊ अऋ 8 ### 85555 69585 #/ 54% 885 644 ऋ# 46 #5# $ 4 % 5 4 #% 4 68 / % ऋकऋ# 44 44
- **Translation**: 

---

