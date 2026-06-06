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

### Verse 1 (Vaivtpuran 13.12182)
- **Original**: कवच पाकर त्रिपुरासुरका वध किया था। *सनातनी ' कहा गया है। 'जय' शब्द कल्याणका
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12183)
- **Original**: . इसी स्तोत्रसे दुर्गाका स्तबन करके गोपकुमारियेनि वाचक है और 'आकार' दाताका। जो देवी सदा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12184)
- **Original**: श्रीहरिको प्राणवल्लभके रूपमें प्राप्त कर लिया। जयदेती हैं, उनका नाम “जया' है। 'सर्वमड्गल'
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12185)
- **Original**: इस स्तोत्रका ऐसा हो प्रभाव है। गोपकन्याओंद्वारा शब्द सम्पूर्ण ऐश्वर्वका बोधक है और “आकार'
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12186)
- **Original**: किया गया “सर्वमड्जल” नामक स्तोत्र शीघ्र ही का अर्थ है देनेवाला। ये देवी सम्पूर्ण ऐश्वर्यको
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12187)
- **Original**: समस्त विप्लॉंका विनाश करनेवाला और मनोवाब्छित देनेवाली हैं; इसलिये “सर्वमड्रला' कही गयी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12188)
- **Original**: वस्तुको देनेबाला है। शैव, वैष्णव अथवा शाक्त हैं। ये देवीके आठ नाम सारभूत हैं और यह
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12189)
- **Original**: कोई भी क्यों न हो, जो मानव तीनों संध्याओंके स्तोन्र उन नामोंके अर्थसे युक्त है। समय प्रतिदिन भक्तिभावसे इस स्तोत्रका पाठ भगवान्‌ नारायणने नाभिकमलपर बैठे हुए
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12190)
- **Original**: करता है, वह संकटसे मुक्त हो जाता है। स्तोत्रके ब्रह्मको इसका उपदेश दिया था। उपदेश देकर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12191)
- **Original**: स्मरणमात्रसे मनुष्य तत्काल ही संकटमुक्त एवं वे जगदीश्वर योगनिद्राका आश्रय ले सो गये निर्भय हो जाता है। साथ ही सम्पूर्ण उत्तम ऐश्वर्य तदनन्तर जब मधु और कैटभ नामक दैत्य [एवं मनोबाज्छित वस्तुको शीघ्र प्राप्त कर लेता ब्रह्माजीको मारनेके लिये उद्यत हुए तब त्रह्माजीने
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12192)
- **Original**: है। पार्वतीकी कृपासे इहलोकमें श्रीहरिकी सुदृढ़ इस स्तोत्रके द्वारा दुर्गाजीका स्तवन एवं नमन
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12193)
- **Original**: भक्ति और निरन्तर स्मृति पाता है एवं अन्तमें किया। उनके द्वारा स्तुति की जानेपर साक्षात्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12194)
- **Original**: भगवान्‌के दास्यसुखकों उपलब्ध करता है। दुर्गने उन्हें “सर्वरक्षण' नामक दिव्य श्रीकृष्ण- इस स्तवराजके द्वारा ब्रजाड्रनाओंने एक कबचका उपदेश दिया। कवच देकर महामाया
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12195)
- **Original**: मासतक प्रतिदिन बड़ी भक्तिके साथ ईश्वरीका अदृश्य हो गयीं। उस स्तोत्रके ही प्रभावसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12196)
- **Original**: स्तवन एवं नमन किया। जब मास पूरा हुआ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12197)
- **Original**: 7538 + संक्षिम्त ब्रह्मवैवर्तपुराण * $%5%%%%%#######ऋ#ऋ%:%$%% अं ### कक कह
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12198)
- **Original**: # 4 2 8 2
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12199)
- **Original**: 0 00) 0 )) "0 ]:9.]7.] तो ब्रतकी समाप्तिके दिन वे गोपियाँ अपने
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12200)
- **Original**: जान पड़ता है, वरुणके अनुचर तुम्हारे वस्त्र उठा वस्त्रोंको तटपर रखकर यमुनाजीमें स्नानके लिये
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12201)
- **Original**: ले गये। अब तुम नंगी होकर घरको कैसे उतरीं। नारद! रज्नोंके मोलपर मिलनेवाले नाना
- **Translation**: 

---

