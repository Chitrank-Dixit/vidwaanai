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

### Verse 1 (Vishnu Puran 0.11721)
- **Original**: मेरे छोड़ देनेपर सम्पूर्ण ट्वासकाकों समुद्र जलमें डुजो देगा; मुझसे भय माननेके कारण केवल मेरे भवनकों छोड़ देगा; अपने इस भवनमें मैं भक्तोंकी हितकामनासे सर्वदा निवास करता हूँ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11722)
- **Original**: आपरादारजी बोल्ले--भगवानके ऐसा कहनेपर उद्धवजी उन्हें प्रणामकर तुरन्त ही उनके बतलाये हुए. तपोवन श्रीनरनागयणके स्थानकों चले गये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11723)
- **Original**: हे द्विज ! तदनन्तर कृष्ण और बलराम आदिके सहित सम्पूर्ण यादव झीघ्रगामी रथॉपर चढ़कर प्रभासक्षेत्रमें आये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11724)
- **Original**: वहाँ पहुँचकर कुकुर, अन्धक और वृष्णि आदि वेश्ञेकि समस्त यादवोनि कृष्णचन्रकी प्रेरणासे महापान और भोजन' किया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11725)
- **Original**: पान करते समय उनमें परस्पर कुछ विवाद हो जानेसे वहाँ कुवाक्यरूप ईंधनसे युक्त प्रल्यकारिणी कलहाप्रि घधक उडी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11726)
- **Original**: श्रीमैत्रेयजी बोले--हे ट्विज ! अपना-अपना भोजन करते हुए उन यादवोंमें किस कारणसे कलह (वाम्युद्ध) अथवा संघर्ष (हाथापाई) हुआ, सो आप कहिये
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11727)
- **Original**: श्रीपराशरजी खोले--'मेशा भोजन शुद्ध है तेरा अच्छा नहों है।' इस प्रकार भोजनके अच्छे बुरैकी चर्चा करते-करते उनमें परस्पर विज्ाद और हाथापाई हो गयी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11728)
- **Original**: तब ये दैवी प्रेरणासे लिबश होकर आपसमें क्रोघसे रक्तनेत्र हूए एक-दूसरेपर जास्प्रहार करने लगो और जब शस्त्र समाप्त हो गये सो पासहीमें उगे हुए सरकण्डे ले लिये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11729)
- **Original**: 1. मैत्रेयजीके अग्रिम प्रश्न और पराशरजीके उत्तरसे वहाँ यदुवंशियोक्त्र अन्न-भोजन करना भी सिद्ध होता है।
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11730)
- **Original**: अ0 37 ] पश्चम अंश 413 एरका तु गृहीता वै वच्रभूतेव लक्ष्यते। तया परस्पर जघुस्संप्रहिरे सुदारुणे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11731)
- **Original**: 45 अद्युम्नसाम्बप्रमुस्ता: कृतवर्माथ सात्यकि: । अनिरुद्धादबश्चान्ये पृथुर्विपृथुरेव. च
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11732)
- **Original**: 46 चारुवर्मा चारुकश्ष तथाक्र्रादयों द्विज। एरकारूपिभिर्वज़ैस्ते निज: परस्परम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11733)
- **Original**: 47 निवारबामास हरियादवांस्ते च केशवम्‌। सहाय॑ मेनिरेषरीणां प्राप्त जघ्ु: परस्परम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11734)
- **Original**: 48 कृष्णोषपि कुपितस्तेषामेरकामुष्टिमाददे । बधाय सोउपि मुसलं मुप्टिलौहमभूत्तदा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11735)
- **Original**: 49 जथान तेन निइशेषान्यादवानाततादिन: । जघुस्ते सहसाभ्येत्य तथान्येडपि परस्परम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11736)
- **Original**: 50 ततश्ञार्णबमध्येन जैत्रोउइसो चक्रिणो रथः । पश्यतो दारुकस्याथ प्रायाद्श्ैर्धतो द्विज
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11737)
- **Original**: 59 चक्र गदा तथा शाई तूणी शद्भोसिरेव च । अ्रदक्षिणं हरि कृत्वा जम्मुरादित्यवर्त्सना
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11738)
- **Original**: 52 क्षणेन. नाभवत्कशिद्यादवानामघातितः । ऋते कृष्ण महात्मानं दारुक च महामुने
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11739)
- **Original**: 53 चडक़रम्यमाणो तौ राम॑ वृक्षमूले कृतासनम्‌ । दद्शाते मुखाश्चास्य निष्क्रामन्त महोरगम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11740)
- **Original**: 54 निष्क्रम्य स मुखात्तस्य महाभोगो भुजड्रमः । त्रययावर्णब॑ सिद्धैः पूज्यमानस्तथोरगैः
- **Translation**: 

---

