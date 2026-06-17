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

### Verse 1 (Vaivtpuran 13.12262)
- **Original**: राधाकृत॑. हरे: स्तोत्र त्रिसंध्यं यः पठेन्नःः । हरिभक्ति चर दास्‍्यं च लभेद्राधागतिं धुवम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12263)
- **Original**: (27। 100--110)
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12264)
- **Original**: पडत क्र संक्षिप्त ब्रह्मवैवर्तपुराण
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12265)
- **Original**: 0 7 00000 00000 0000 8 6
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12266)
- **Original**: । 8 माना। जिस स्थानपर और जिस आधारमें जो
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12267)
- **Original**: द्रव्योंसे चौक पूरकर उसे सजा दे)। इसके बाद द्रव्य पहले रखा गया था, वस्त्रोंसहित वह सब
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12268)
- **Original**: बालूकी दशभुजा दुर्गामूर्ति बनावे। देवीके ललाटमें द्रव्य गोपकन्याओंकों उसी रूपमें प्राप्त हुआ। फिर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12269)
- **Original**: सिन्दूर लगावे और नीचेके अड्जोंमें चन्दन एवं तो वे सब-कौ-सब देवियाँ जलसे निकलकर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12270)
- **Original**: कपूर अर्पित करे। तदनन्तर ध्यानपूर्वक देवीका व्रत पूर्ण करके मनोवाजञ्छित वर पाकर अपने-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12271)
- **Original**: आवाहन करे। उस समय हाथ जोड़कर निम्नाद्धित अपने घरको चली गयीं। मन्त्रका पाठ करे। उसके बाद पूजा आरम्भ करनी नारदजीने पूछा--प्रभो! उस ब्रतका चाहिये। विधान है? क्‍या नाम है और क्या फल है? हे गौरि शंकरार्धाद्लि यथा त्वं शंकरप्रिया। उसमें कौन-कौन-सी वस्तुएँ और कितनी दक्षिणा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12272)
- **Original**: तथा मां कुरु कल्याणि कान्तकान्तां सुदुर्लभाम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12273)
- **Original**: देनी चाहिये। म्रतके अन्तमें कौन-सा मनोहर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12274)
- **Original**: “भगवान्‌ शंकरकी अर्धाड्रिनी कल्याणमयी रहस्य प्रकट हुआ? महाभाग! इस नारायण-
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12275)
- **Original**: गौरीदेवि! जैसे तुम शंकरजीको बहुत हो प्रिय कथाको विस्तारपूर्वक कहिये। हो, उसी प्रकार मुझे भी अपने प्रियतम पतिकी भगवान्‌ नारायण बोले--वत्स ! उस व्रतका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12276)
- **Original**: परम दुर्लभा प्राणवल्लभा बना दो।' सारा विधान मुझसे सुनो। उसका नाम गौरीब्रत
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12277)
- **Original**: इस मन्त्रको पढ़कर देवी जगदम्बाका ध्यान है। मार्गशीर्ष मासमें सबसे पहले स्त्रियोंने इसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12278)
- **Original**: करे। उनका गृढ़ ध्यान सामवेदमें वर्णित है, जो किया था। यह पुरुषोंको भी धर्म, अर्थ; काम
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12279)
- **Original**: सम्पूर्ण कामनाओंको देनेवाला है। नारद! वह और मोक्ष देनेवाला तथा श्रीकृष्णकी भक्ति प्रदान
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12280)
- **Original**: ध्यान मुनीद्रोंक लिये भी दुर्लभ है, तथापि मैं करनेवाला है। भिन्न-भिन्न देशोंमें इसकी प्रसिद्धि
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12281)
- **Original**: तुम्हें बता रहा हूँ। इसके अनुसार सिद्ध पुरुष है। यह त्रत पूर्वपरम्परासे पालित होनेवाला माना
- **Translation**: 

---

