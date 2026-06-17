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

### Verse 1 (Bramha 0.6361)
- **Original**: हृदयमें स्नेहके कारण उनके स्तनोंसे दूध बहने अन्तकालमें भी तो एक बार पुत्रका मुँह देख लूँ।
- **Translation**: 

---

### Verse 2 (Bramha 0.6362)
- **Original**: लगा। वसुदेवजी तो मानों समीप आयी हुई इसी समय रकज्जभूमिमें तुरही आदि बाजे बज
- **Translation**: 

---

### Verse 3 (Bramha 0.6363)
- **Original**: वृद्धावस्थाको छोड़कर युवा हो गये। उनकी दृष्टि उठे। चाणूर उछलने और मुष्टिक ताल ठोंकने
- **Translation**: 

---

### Verse 4 (Bramha 0.6364)
- **Original**: अपने दोनों पुत्रोंपर ही लगी हुई थी, मानो वे ही लगा। लोगोमें हाहाकार मच-गया। बलराम और
- **Translation**: 

---

### Verse 5 (Bramha 0.6365)
- **Original**: उनके लिये महान्‌ उत्सव हों। रनिवासकी स्त्रियाँ श्रीकृष्ण रद्रभूमिके द्वारपर आये और महावतसे
- **Translation**: 

---

### Verse 6 (Bramha 0.6366)
- **Original**: एकटक नेत्रोंसे श्रीकृष्ण और बलरामको निहारती प्रेरित कुबलयापीड नामक हाथीको मारकर भीतर
- **Translation**: 

---

### Verse 7 (Bramha 0.6367)
- **Original**: थीं। नगरकी स्त्रियाँ तो उनकी ओरसे दृष्टि ही घुस गये। उस समय उनके अड्जोंमें हाथीका मद
- **Translation**: 

---

### Verse 8 (Bramha 0.6368)
- **Original**: नहीं हटातो थीं। और रक्त लगे हुए थे। उसके बड़े-बड़े दाँतोंको
- **Translation**: 

---

### Verse 9 (Bramha 0.6369)
- **Original**: . स्त्रियाँ आपसमें कहने लगौं--'सखियो! ही उन्होंने अपना आयुध बना लिया था। वे दोनों
- **Translation**: 

---

### Verse 10 (Bramha 0.6370)
- **Original**: श्रीकृष्णणा मुख तो देखो, कैसी कमल-जैसी भाई गर्वपूर्ण लीलामयी चितबनसे निहारते हुए
- **Translation**: 

---

### Verse 11 (Bramha 0.6371)
- **Original**: सुन्दर आँखें हैं। कुवलयापीड हाथीसे युद्ध करनेके उस महान रघ्जोत्सवमें इस प्रकार प्रविष्ट हुए,
- **Translation**: 

---

### Verse 12 (Bramha 0.6372)
- **Original**: कारण जो परिश्रम हुआ है, उससे इनके मुखपर मानो मृगोंके झुंडमें दो सिंह आ गये हों। उनके
- **Translation**: 

---

### Verse 13 (Bramha 0.6373)
- **Original**: पसीनेकी बूँदें निकल आयी हैं। इन स्वेदविन्दुओंसे आते ही रघ्अभूमिमें चारों ओर महान्‌ कोलाहल
- **Translation**: 

---

### Verse 14 (Bramha 0.6374)
- **Original**: सुशोभित इनका प्रसन्न मुख ऐसा जान पड़ता है, हुआ। सब लोग विस्मयके साथ कहने लगे, “ये
- **Translation**: 

---

### Verse 15 (Bramha 0.6375)
- **Original**: मानो खिले हुए कमलपर ओसके कण शोभा पा ही कृष्ण हैं, ये ही बलभद्र हैं। ये कृष्ण वे ही
- **Translation**: 

---

### Verse 16 (Bramha 0.6376)
- **Original**: रहे हों। इस मनोहर मुखकी झाँकी करके आज हैं, जिन्होंने भयंकर राक्षसी पूतनाका वध किया,
- **Translation**: 

---

### Verse 17 (Bramha 0.6377)
- **Original**: अपना जन्म सफल कर लो। अहा! भामिनी! इस छकड़े उलट दिये और दोनों अर्जुन यृक्षोंको
- **Translation**: 

---

### Verse 18 (Bramha 0.6378)
- **Original**: बालकके वक्ष:स्थलपर तो दृष्टिपात करो। श्रीवत्स- डखाड़ डाला। जिन्होंने बालक होते हुए भी
- **Translation**: 

---

### Verse 19 (Bramha 0.6379)
- **Original**: चिहसे इसकी कैसी शोभा हो रही है। यह सम्पूर्ण कालिय नागके मस्तकपर नृत्य किया, सात
- **Translation**: 

---

### Verse 20 (Bramha 0.6380)
- **Original**: जगतूका आश्रय है और इसकी दोनों भुजाएँ रातोंतक गोवर्धन पर्वतको हाथपर रखा और
- **Translation**: 

---

