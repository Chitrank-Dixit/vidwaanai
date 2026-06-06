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

### Verse 1 (Vishnu Puran 0.10361)
- **Original**: प्रातःफाल होनेपर समस्त मछोंपर नागरिक लोग और राजमज्ञोंपर अपने अनुचरोंके सहित राजालोग बैठे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10362)
- **Original**: तदनन्तर रंगभूमिके मध्य भागके समीप कंसने युद्धपरीक्षकॉंकों बैठाया और फिर स्वयं आप भी एक ऊँचे सिंहासनपर बैठा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10363)
- **Original**: वहाँ अन्तःपुरव सखियोंके लिये पथक्‌ मचान बनाये गये थे तथा मुख्य-मुख्य वागंगनाओं और नगस्की महित्तरओके लिये भी अलग-अलग मम्र थे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10364)
- **Original**: कुछ अन्य मछोंपर नन्‍्दगोप आदि गोपगण बिठाये गये थे और उन मझोँके पास ही अक्रूर और चसूदेखजीं बैठे थे।28
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10365)
- **Original**: नगरकी नारियोंके बोचमें चलो, अन्त्कालमें ही पुत्रका मुख तो देख छैँगी' ऐसा विचास्कर पुत्रके लिये मद्जनऊूकामना करती हुई देवकीजी बैडी थीं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10366)
- **Original**: तदनत्तर जिस समय तूर्य आदिके बजने तथा चाणूरके अह्यत्त उछलने और मुष्टिकके ताल ठॉकनेपर दर्शकगण हाहाकार कर रहे थे, गोपवेषधारो वीर बालक बलभद्र और कृष्ण कुछ हैंसते हुए रंगभूमिके द्वारपर आये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10367)
- **Original**: वहाँ आते ही महावतकी प्ररणासे कुबलयापीढ नामक हाथी उन दोनों गोपकुमारोंकों मारनेके लिये बड़े नेगसे दौड़ा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10368)
- **Original**: हे द्विजश्रेष्ट
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10369)
- **Original**: उस समय रैगभूमिमें महान्‌ हाहाकार मच गया तथा बलदेयजीने अपने अनुज कष्णकी ओर देखकर कहा--“हे सहाभाग ! इस हाथीको शज्रुने ही प्रेरित किया है; अतः इसे मार डालना चाहिये'
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10370)
- **Original**: हे द्विज ! ज्ये्ठ आता बलरामजीके ऐसा कहनेपर बात्रुसूदनश्रीश्यामसुन्दने यड़े जोरसे सिंहनाद किया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10371)
- **Original**: फिर केदिनिषृदन भगवान्‌ श्रीकष्णने
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10372)
- **Original**: आ> 20 ] ईशो5पि सर्वजगतां बाललीलानुसारत: । क्रीडित्वा सुचिरं कृष्ण: करिदन्तपदान्तरे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10373)
- **Original**: 37 उत्पात्य वामदन्तं तु दक्षिणेनेव पाणिना । ताड़यामास यन्तारं तस्यासीच्छतथ्वा शिर:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10374)
- **Original**: 38 दक्षिण दन्तमुत्पाव्य बलभद्रो5पि तत्क्षणात्‌ । सरोषस्तेन पार्श्ृस्थान्‌ गजपालानपोथयत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10375)
- **Original**: 39 बेगेन रोहिणेयो महाबल:। जघान बामपादेन मस्तके हस्तिन रुषा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10376)
- **Original**: 40 स॒पपात हतस्तेन बलभद्रेण लीलया। सहस्राक्षेण वस्रेण ताड़ित: पर्वतो यथा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10377)
- **Original**: 49 मृगमध्ये यथा सिंहौ गर्वलीलावलोकिनौ । प्रथिष्टो. सुमहारड़ू. बलभद्रजनार्दनी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10378)
- **Original**: 43 हाहाकारो महाज़ज्े महारथ्डे त्वनन्तरम्‌। कृष्णो5यं बलभब्रोउ्यमिति लोकस्य विस्मय:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10379)
- **Original**: 44 सो5यं येन हता घोरा पूतना बालघातिनी । क्षिप्तं तु शकटं येन भमौ तु यमलार्जुनो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10380)
- **Original**: 45 सो5य॑ यः कालियं नागं ममर्दारुद्य बालक: । धृतो गोवर्द्धनो येन सप्तरात्र महागिरि:
- **Translation**: 

---

