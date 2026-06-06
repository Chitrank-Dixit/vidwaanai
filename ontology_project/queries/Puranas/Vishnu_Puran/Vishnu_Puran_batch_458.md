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

### Verse 1 (Vishnu Puran 0.9141)
- **Original**: 6 श्रीपराइरजी खोलछे--ब्न्‍्दोगृहसे छूटते ही वसुदेवजी नन्दजोंके छकड़ेके पास गये तो उन्हें इस समाचारसे अत्यत्त प्रसन्न देखा कि 'मेरे पुत्रका जन्म हुआ है'
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9142)
- **Original**: तब यसुदेवजीने भी उनसे आदरपूर्वक कहा--- अब दृद्धावस्थामें भी आपने पुत्रका मुख देख लिया यह बड़े ही सौभाग्यकी बात है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9143)
- **Original**: आपलोग जिसलिये यहाँ आये थे वह राजाका सारा यार्षिक कर दे ही चुके हैं। यहाँ घनवान्‌ पुरुषोंक्रों और अधिक न ठहरना चाहिये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9144)
- **Original**: आपस्भेग जिसल्त्ये यहाँ आये थे वह क्यर्य पूरा हो चुका, अब और अधिक किसलिये ठहरे हुए है ? [ यहाँ देरतक टहरना ठीक नहीं है] अठः हे नन्‍दजी
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9145)
- **Original**: आपल्तरेग शीघ्र ही अपने गोकुलको जाइये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9146)
- **Original**: यहाँपर रोहिणीसे उत्पन्न हुआ जो मेरा पुत्र है उसकी भी आप उसी तरह रक्षा कीजियेगा जैसे अपने इस याल्ककी
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9147)
- **Original**: वसुदेवजीके ऐसा कहनेपर नन्‍द आदि महाबलखान्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9148)
- **Original**: 320 चर अओविष्णुपराण अर आ 8 बसतां गोकुले तेषां पूतना बालघातिनी
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9149)
- **Original**: गोपगण छकड़ोंमें रखकर लाये हुए भाष्डोंसे कर चुकाकर सुप्तें कृष्णमुपादाय रात्रौ तस्मै स्तन॑ ददौ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9150)
- **Original**: चले गये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9151)
- **Original**: उनके गोकुरूमें रहते समय बालखातिनी सम्रायच्छति पूतनाने राज्रिकि समय सोये हुए कृष्णको गोदमें लेकर यस्मै यस्मे हल दि पूतता स । उसके मुझमें अपना स्तन दे दिया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9152)
- **Original**: रात्रिफे समय क़त्प तस् के बालकस्योपहन्यते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9153)
- **Original**: 8 पूतना जिस-जिस बालूकके मुखमें अपना स्तन दे देती थी कृष्णस्तु तत्स्तनं गा कराभ्यामतिपीडितम्‌ । डसीका शरीर तत्काल नष्ट हो जाता था
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9154)
- **Original**: कृष्णचन्द्रने गृहीत्वा प्राणसहित पपौ क्रोधसमन्वित:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9155)
- **Original**: 9 सातिमुक्तमहारावा विच्छिन्नसत्रायुबन्धना । पपात पूतना भूमौ प्रियमाणातिभीषणा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9156)
- **Original**: 10 तन्नादश्रुतिसन्त्रस्ता: प्रबुद्धास्ते ब्रजौकस: । ददृशु: पूतनोत्सड्े कृष्ण तां च निपातिताम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9157)
- **Original**: 11 आदाय कृष्णं सन्त्नस्ता यशोदापि द्विजोत्तम । गोपुच्छभ्रामणेनाथ. बाल्दोषमपाकरोत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9158)
- **Original**: 12 गोकरीषपुपादाय नन्दगोषो5पि मस्तके । कृष्णस्य प्रददी रक्षां कुर्वश्नैतदुदीरयन्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9159)
- **Original**: 13 नन्दगोष उवाच रक्षतु त्वामशेषाणां भूतानां प्रभवो हरि: । यस्य नाभिसमुद्धृतपड्डुजादभवज्जगत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9160)
- **Original**: 14 थेन देंष्टाअ्विधृता धारयत्यबनिर्जगत्‌। खराहरूपधृग्देवस्स त्वां रक्षतु केशव:
- **Translation**: 

---

