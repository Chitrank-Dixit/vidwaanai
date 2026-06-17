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

### Verse 1 (Vaivtpuran 16.3334)
- **Original**: रत्द्वारा निर्मित विमानपर बैठी थीं। उनका विग्रह शंकरका दूत हूँ। मेरा नाम पुष्पदन्त है।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3335)
- **Original**: लाल रंगके वस्त्रसे सुशोभित था। उनके गलेमें शंकरजीकी कही हुई बातें हो मैं यहाँ आपसे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3336)
- **Original**: लाल पुष्पोंकी माला थी। सभी अड्ज लाल कह रहा हूँ, सुननेकी कृपा करें। अब आप
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3337)
- **Original**: चन्दनसे अनुलिप्त थे। नाचना, हँसना, हर्षके देवताओंका राज्य तथा उनका अधिकार उन्हें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3338)
- **Original**: उल्लासमें भरकर मीठे स्वरोंमें गाना, भक्तोंको लौटा दें; क्‍योंकि वे देवेश्वर श्रीहरिकी शरणमें
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3339)
- **Original**: अभय प्रदान करना तथा शत्रुओंको डराना उन गये थे। उन प्रभुने अपना त्रिशूल देकर आपके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3340)
- **Original**: अभयस्वरूपिणी भगवती भद्रकालीका सहज गुण विनाशके लिये शंकरकों भेजा है। त्रिनेत्रधारी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3341)
- **Original**: बअन गया था। उनके मुखमें बड़ी विकराल लंबी भगवान्‌ शिव इस समय चन्द्रभागा नदीके तटपर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3342)
- **Original**: जीभ लपलपा रही थी। शह्कु, चक्र, गदा, पद्म, बटवृक्षेके नीचे विराजमान हैं। आप या तो
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3343)
- **Original**: ढाल, तलवार, धनुष, बाण, एक योजन विस्तृत देवताओंका राज्य लौटा दें या निश्चित रूपसे युद्ध
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3344)
- **Original**: वर्तुलाकार गम्भीर खप्पर, गगनचुम्बी त्रिशूल, करें। मुझे यह भी बता दें कि मैं भगवान्‌ शंकरके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3345)
- **Original**: एक योजनमें फैली हुई शक्ति, मुद्वर, मुसल, वज्र, पास जाकर उनको क्‍या उत्तर दूँ? पाश, खेटक, प्रकाशमान फलक, बैष्णवास्त्र, नारद! दूतके रूपमें गये हुए पुष्पदन्तकी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3346)
- **Original**: बारुणास्त्र, आग्रेयास्त्र, नागपाश, नागयणास्त्र, ब्रह्मास्त्र, बात सुनकर शब्डचूड़ ठठाकर हँस पड़ा और
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3347)
- **Original**: गन्धर्व, गरुड़, पार्जन्य एबं पाशुपतास्त्र, जृम्भणास्त्र, बोला--' दूत! मैं कल प्रात:ःकाल चलूँगा, तुम
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3348)
- **Original**: पार्वतास्त्र, माहेश्वरास्त्र, वायव्यास्त्र, सम्मोहन दण्ड, जाओ ।' तब पुष्पदन्त तुरंत बटके नीचे विराजमान
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3349)
- **Original**: शतशः: अमोघ अस्त्र तथा सैकड़ों दिव्य अस्त्रको भगवान्‌ शंकरके पास लौट गया और उनसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3350)
- **Original**: धारण करके भगवती भद्रकाली अनन्त योगिनियोंके शह्लुचूड़की बात, जो स्वयं उसने अपने मुखसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3351)
- **Original**: साथ वहाँ आकर विराज गयीं। उनके साथमें कही थी, कह सुनायी। साथ ही, उसके पास जो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3352)
- **Original**: अत्यन्त भयंकर असंख्य डाकिनियोंका यूथ भी सेना आदि युद्धोपकरण थे, उनका भी परिचय
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3353)
- **Original**: सुशोभित था। भूत, प्रेत, पिशाच, कृष्माण्ड, दिया। इतनेमें योजनानुसार कार्तिकेय शंकरके
- **Translation**: 

---

