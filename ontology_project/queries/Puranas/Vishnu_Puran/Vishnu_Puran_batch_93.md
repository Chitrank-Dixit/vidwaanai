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

### Verse 1 (Vishnu Puran 0.1841)
- **Original**: ख्वीको तो किसीने मोह उपजानेके लिये ही रचा है !
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1842)
- **Original**: 'मुझे अपने मनको जीतकर छहों ऊर्मर्भयों" से अतीत परबह्मकों जानना चाहिये'--- जिसने मेरी इस प्रकारकी बुद्धिकों नष्ट कर दिया, उस क्यमरूपी महाअहकों घिक्कार है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1843)
- **Original**: नगरकग्रामके मार्गरूप इस ख््रोके संगसे वेदवेद्य भगवानकी प्राप्तिके कारणरूप मेरे समस्त ब्रत नष्ट हो गये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1844)
- **Original**: इस प्रकार उन थर्मज्ञ मुनिवरने अपने-आप ही अपनी निनन्‍्दा करते हुए वहाँ बेठो हुई उस अप्सयसे कहा--
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1845)
- **Original**: “'अरी पापिनि ! अब तेरी जहाँ इच्छा हो चल्ली जा, तूने अपनी भावभंगीसे मुझे मोहित करके इन्द्रका जो कार्य था वह पूरा कर लिया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1846)
- **Original**: मैं अपने क्रोधसे प्रज्वलित हुए अग्निद्वारा तुझे मस्म नहीं करता हूँ, क्योंकि सज्ननोंकी मित्रता सात पग साथ रहनेसे हो जाती है और मैं तो [ इतने दिन ] तेरे साथ चुका हूँ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1847)
- **Original**: अथवा इसमें तेरा दोष भी क्‍या है, जो में तुझपर क्रोध करूँ ? दोष तो साश मेरा ही है, क्योंकि मैं बड़ा ही अजितेन्द्रिय हूँ
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1848)
- **Original**: तू महामोहकी पिटारी और अत्यन्त निन्‍्दनीया है। हाय ! तूने इन्द्रके स्वार्थक लिये मेरी तपस्या नष्ट कर दी !! तुझे घिकार है !!!
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1849)
- **Original**: सोमने कहा--वे ब्रह्मर्षि उस सुन्दरोसे जबतक ऐसा कहते रहे क्तनतक बह
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1850)
- **Original**: भयके कारण ] पसीनेमें सराजोर होकर अत्यन्त काँपती रही
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1851)
- **Original**: इस प्रकार जिसका समस्त शरीर पसीनेमें डूबा हुआ था और जो भयसे धर- धर काँप रही थी उस प्रस्‍्लोचासे मुनिश्रेष्ठ कप्डुने क्रोधपूर्वक कहा-- अरी ! तू चल्मी जा ! चल्त्रे जा !!
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1852)
- **Original**: तब बारम्बार फटकारे जानेपर वह उस आश्रमसे + श्षुघा, फिपासा, ल्टोभ, मोह, जग और मृत्यु--ये क्तः कर्मियाँ हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1853)
- **Original**: 66 निर्मार्जमाना गात्राणि गलत्स्वेदजलानि वै । वृक्षादवृक्ष ययो बाला तदग्रारुणपललबै:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1854)
- **Original**: 47 ऋषिणा यस्तदा गर्भस्तस्या देहे समाहितः । निर्जाम स॒रोमाझइस्वेदरूपी तदडभतः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1855)
- **Original**: 48 ते वृक्षा जगृहुर्गर्भपेके चक्रे तु मारुतः । मया चाप्यायितो गोभि: स तदा वव॒धे झनैः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1856)
- **Original**: 49 बृक्षाअगर्भसम्भूता मारिषाख्या वरानना। तां प्रदास्यन्ति वो वृक्षा: कोप एप प्रश्ञाम्यताम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1857)
- **Original**: ! 50 कण्डोरपत्यमेत्ं॑ सा वृक्षेभ्यक्ष समुद्गता ममापत्य तथा वायो: प्रम्लोचातनया च सा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1858)
- **Original**: 51 शरीपराग़र उवाच स चापि भगवान्‌ कण्डु: क्षीणे तपसि सत्तम: । पुरुषोत्तमाख्य॑ मैत्रेय विष्णोरायतनं ययौ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1859)
- **Original**: 52 तत्रैकाअमतिर्भूला चकाराराधनं हरे: । बह्मपारमय कुर्वज्ञपमेकाग्रमानस: । ऊर्ध्वबाहुर्महायोगी स्थित्वासौ भूपनन्दना:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1860)
- **Original**: 53 अचेतस ऊचुः बह्मपारं मुने: श्रोतुमिच्छामः परम स्तवम्‌। जपता कण्डुना देवो येनाराध्यत केशव:
- **Translation**: 

---

