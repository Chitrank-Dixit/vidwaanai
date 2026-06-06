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

### Verse 1 (Vaivtpuran 6.9431)
- **Original**: बिना मृदा घट कतुँ यथा नाल॑ कुलालक:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.9432)
- **Original**: विना स्वर्ण स्वर्णकारोउलंकारं कर्तुमक्षम:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.9433)
- **Original**: स्वयमात्मा यथा नित्यस्तथा त्व॑ प्रकृति: स्वयम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.9434)
- **Original**: सर्वशक्तिसमायुक्ता. सर्वाधाया. सनातनी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.9435)
- **Original**: ( श्रीकृष्णजन्मखण्ड 6। 214-218)
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.9436)
- **Original**: 4डर26 * संक्षिप्त ब्रह्मबैकर्तपुराण « ###$##%%4% 55%: 54% #$ $ 5 % अऊकअऋअंऊअऊड कक श्ऊडऊकअऋऋऊ भऋ फऋडऋक अर अंक कक कक डर अऋ अड अब क ह कह उपकार, बाराणसौपुरीका दहन, महादेवजीको
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.9437)
- **Original**: तुम्हारे जिम्मे लगाया है, वह सब यथासमय पूरा जृम्भणास्त्रसे बाँधना, बाणासुर्की भुजाओंको काटना,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.9438)
- **Original**: होगा। ब्रजेश्वरि! राधे! गणेशजीकों छोड़कर शेष पारिजातका अपहरण, अन्यान्य कर्मोंका सम्पादन,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.9439)
- **Original**: छोटे-बड़े सभी देवताओं और देवियोंका कलाद्वारा प्रभासतीर्थकी यात्रामें जाना, वहाँ मुनिमण्डलीका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.9440)
- **Original**: भूतलपर अवतरण होगा। दर्शन करना, व्रजंके बन्धुजनोंसे वार्तालाप, पिताके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.9441)
- **Original**: ._ तदनन्तर लक्ष्मी, सरस्वती तथा श्रीराधासहित यज्ञका सम्पादन, वहीं शुभ बेलामें पुनः तुम्हारे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.9442)
- **Original**: पुरुषोत्तम श्रीहरिको भक्तिभावसे प्रणाम करके सब साथ मिलन तथा गोपियोंका साक्षात्कार आदि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.9443)
- **Original**: देवता आनन्दपूर्वक अपने-अपने स्थानको चले कार्य मुझे करने हैं। फिर तुम्हें अध्यात्मज्ञानका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.9444)
- **Original**: गये। श्रीहरिने जिस कार्यका आयोजन किया था, उपदेश देकर वास्तवमें तुम्हारे साथ नित्य मिलनका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.9445)
- **Original**: उसे सफल बनानेके लिये बे व्यग्रतापूर्वक सौभाग्य प्राप्त करूँगा। इसके बाद मेरे साथ दिन-
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.9446)
- **Original**: भूतलपर पधारे; क्योंकि स्वामीका बताया हुआ रात तुम्हारा संयोग बना रहेगा। कभी क्षणभरके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.9447)
- **Original**: स्थान देवताओंके लिये भी दुर्लभ था। लिये भी वियोग न होगा। इतना ही नहीं, वहाँसे श्रीकृष्णने राधासे कहा--प्रिये! तुम तुम्हारे साथ मेरा पुनः न्रजमें आगमन होगा।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.9448)
- **Original**: पूर्वनिश्चित गोप-गोपियोंके समुदायके साथ वृषभानुके प्राणवल्लभे ! वियोगकालमें भी स्वप्रमें तुम्हारे साथ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.9449)
- **Original**: निवासगृहकों पधारो। मैं मथुरापुरीमें वसुदेवके घर मेरा सदैव मिलन होता रहेगा। तुमसे बिछुड़कर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.9450)
- **Original**: जाऊँगा। फिर कंसके भयका बहाना बनाकर द्वारकामें जानेपर मेरे और मेंरे नारायणांशके द्वारा
- **Translation**: 

---

