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

### Verse 1 (Vishnu Puran 0.4261)
- **Original**: देखो, पृथिवीपर तो मेरे पैर रखे हैं, पैरोंके ऊपर ज॑घाएँ हैं और जंघाओंके ऊपर दोनों ऊह तथा ऊरुओंके ऊपर उदर है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4262)
- **Original**: उदरके ऊपर वक्षःस्थल्ल, बाहु और क्ोंकी स्थिति है तथा कन्धोंके ऊपर यह शिव्ििका रखी है। इसमें मेरे ऊपर कैसे बोझा रहा ?
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4263)
- **Original**: इस दिबिकामें जिसे तुम्हारा कहा जाता है वह शरीर रखा हुआ है । वास्तवमें तो 'तुम वहाँ (विबिकामें) हो और मैं यहाँ (पृथिवीपर) हूँ'--ऐसा कहना सर्वधा मिथ्या है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4264)
- **Original**: 68 । है राजन्‌ ! मैं, तुम और अन्य भी समस्त जीव पहषभूतोंसे ही वहन किये जाते हैं। तथा यह भूतवर्ग भी गुणोके प्रबाहमें पड़कर ही बहा जा रहा है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4265)
- **Original**: हे पृथिवीपते ! ये सत्त्यादि गुण भी कर्मोके लशोभूत हैं और समस्त जीवॉमें कर्म अविद्याजन्य ही हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4266)
- **Original**: आत्मा तो शुद्ध, अक्षर, शान्त, निर्गुण और प्रकृतिसे परें है तथा समस्त जीतॉमें
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4267)
- **Original**: 152 यदा नोपचयस्तस्थ न चैवापचयों नृप। तदापीवानसीतीत्थ कया युक्‍त्या त्वयेरितम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4268)
- **Original**: 72 भूपादजद्भाकस्घूरूजठरादिषु. संस्थिते। दिबिकेये यथा स्कन्थे तथा भार: समस्त्वया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4269)
- **Original**: 73 तथान्यैर्जन्तुभिर्भूप शिबिकोढा न केवलम्‌ । शैलद्मगृहोत्थोडपि पृथिवी सम्भवो5पि वा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4270)
- **Original**: 7ड यदा पुंसः पृथग्भावः प्राकृतैः कारपौनूप । सोढव्यस्तु तदायास: कर्थ वा नृपते मया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4271)
- **Original**: 75 यदद्रव्या शिबिका चेय॑ तद्द्व॒व्यो भूतसंग्रह: । भवतो मे5उखिलस्यास्थ ममत्वेनोपबृंहित:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4272)
- **Original**: 76 अ्रीपएशर उबाच एबमुक्त्वाभवन्मौनी स वहज्छिबिकां द्विज । सो5पि राजावतीयोंव्याँ तत्यादो जगृहे त्वरन्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4273)
- **Original**: (77 राजोबाच भो भो विसृज्य शिविकां प्रसाद कुरु मे ट्विज । कथ्यतां को भवानत्र जाल्मरूपधर: स्थित:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4274)
- **Original**: 78 यो भवान्यश्षिमित्त वा यदागमनकारणम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4275)
- **Original**: तत्सर्व कथ्यतां विद्वन्पह्मंं शुभ्रंषवे त्वया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4276)
- **Original**: 79 ब्राह्मण उवाच श्रूयतां सो5हमित्येतद्वक्ु
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4277)
- **Original**: भूप न शकक्‍्यते । उपभोगनिमित्त चर सर्वश्रागमनक्रिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4278)
- **Original**: 80 सुखदुःखोपभोगौ तु तो देहाद्युपपादको । धर्माधर्मोद्धनों भोक्तुं जन्तुर्देहादिमृच्छति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4279)
- **Original**: 891 सर्वस्यैव हि भूषाल जन्तो: सर्वत्र कारणम्‌ । धर्माधर्मो यत: कस्मात्कारणं पृच्छयते त्वया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4280)
- **Original**: 82 गरफेवाच धर्माधमों न सन्देहस्सर्वकार्येषु कारणम्‌। उपभोगनिपित्त चर देहह्ेहान्तरागम:
- **Translation**: 

---

