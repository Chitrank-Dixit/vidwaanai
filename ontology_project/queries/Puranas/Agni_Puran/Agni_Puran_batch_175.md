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

### Verse 1 (Agni Puran 0.3481)
- **Original**: एक त्राह्मणका वध करता है, तो वे सब-के-सब जाव, उस कार्यकों 'हनन' कहते हैं। जो राग, द्वेष
- **Translation**: 

---

### Verse 2 (Agni Puran 0.3482)
- **Original**: 'घातक' माने जाते हैं। ब्राह्मण किसीके द्वारा अथवा प्रमादवश दूसरेके द्वारा या स्वयं ब्राह्मणका
- **Translation**: 

---

### Verse 3 (Agni Puran 0.3483)
- **Original**: निन्दित होनेपर, मारा जानेपर या बन्धनसे पीड़ित 1. विष्णये यिष्णये नित्य विष्णये विश्णये नमः । नमामि विष्णु. चित्तस्थमहंकारगतिं हरिस्‌
- **Translation**: 

---

### Verse 4 (Agni Puran 0.3484)
- **Original**: वित्तत्थमौशमध्यक्रमततमपताजितम्‌ । चिष्णुमीडयमशेपेण. अनादिनिध्न विधुम्‌
- **Translation**: 

---

### Verse 5 (Agni Puran 0.3485)
- **Original**: विष्शुक्षितततोी.. यन्‍ये.. विष्णुबुंद्धिततक्ष. यतू । यव्चाहंकारगों. विष्णुर्य्विष्णुमयि.. सैस्थित:
- **Translation**: 

---

### Verse 6 (Agni Puran 0.3486)
- **Original**: करोति कर्मभूतोईसौी स्थावरस्थ अरस्य चल
- **Translation**: 

---

### Verse 7 (Agni Puran 0.3487)
- **Original**: तत्‌ पाप॑ नाजमायातु उठस्मिन्रेव हि चिन्तिते
- **Translation**: 

---

### Verse 8 (Agni Puran 0.3488)
- **Original**: ध्यातों हरति यत्‌ पाप॑ स्वष्ने दृष्टस्तु भावत्रात्‌ू। तमुपेन््रमह. विष्नुं. अ्णतातिंहर॑ हरिमू
- **Translation**: 

---

### Verse 9 (Agni Puran 0.3489)
- **Original**: ,. जगत्यस्मिश्रिताधारे मजमाने तमस्यध: । हस्तावलम्बन॑ विष्णु प्रणमामि. परात्परम्‌
- **Translation**: 

---

### Verse 10 (Agni Puran 0.3490)
- **Original**: सर्वेश्वरेश्वर विभो घरमात्मक्रधोक्षज । हपीकेश हृषोकेश हृपोकेश नमोउस्तु ते
- **Translation**: 

---

### Verse 11 (Agni Puran 0.3491)
- **Original**: सू्सिहानतनता गोयिन्द धूतभावन केशव
- **Translation**: 

---

### Verse 12 (Agni Puran 0.3492)
- **Original**: दुरुक्त दुष्कृत॑ ध्यात॑ शमवाध॑ त्रमोउस्तु तेड यन्मया. चिच्तित॑ दुए स्वचित्तवशवर्तिता । अकार्य॑ महदस्युप्रं तच्छम॑ नय_ क्रेशवञर अ्रह्मण्यदेय गोविन्द परमार्थपरायण । जगन्नाथ जगद्धात: पाप॑ प्रश्तमयाच्युतब यथापराद्टे सायाद्षे मध्याहे च॑ तथा निशि। कायेन मनसा साचा कृत पापयजानता
- **Translation**: 

---

### Verse 13 (Agni Puran 0.3493)
- **Original**: जानता च इहृषोकेश पुण्डरोकाक्ष साधव। नामत्रयोच्चारणत: पाप॑ यातु मम क्षयम्‌
- **Translation**: 

---

### Verse 14 (Agni Puran 0.3494)
- **Original**: शरीरं॑ में हषीकेजश् पुण्डरीकाक्ष माधव
- **Translation**: 

---

### Verse 15 (Agni Puran 0.3495)
- **Original**: पाप प्रशमयाद्य त्व॑ याककृतं॑ मम माघव
- **Translation**: 

---

### Verse 16 (Agni Puran 0.3496)
- **Original**: यद्‌ भुझन्‌ यतू स्वपंस्तिष्ठनू गच्छन्‌ जाग्रदू यदास्थित: । कृतवानू फापमधाहँ कायेतन मनसा गिराआ यू स्वल्पमपि यत्‌ स्थूल॑ कुयोनिनरकायहम्‌ । तद्‌ यातु प्रशम॑ सव॑ वासुदेवानुकोर्तत्रातु
- **Translation**: 

---

### Verse 17 (Agni Puran 0.3497)
- **Original**: पर॑ ब्राप्न फं धाम पवित्र परम अर यत्‌। तस्मिन्‌ प्रकीर्तिते खिष्णौ यत्‌ पाप तत्‌ प्रणश्यतु
- **Translation**: 

---

### Verse 18 (Agni Puran 0.3498)
- **Original**: यत्‌ प्राप्प न निवतंन्ते गन्धस्पर्शादिवर्जितम्‌। सूरयस्तत्‌ पद विष्णोस्तत्‌ सर्व शमयत्वचम्‌
- **Translation**: 

---

### Verse 19 (Agni Puran 0.3499)
- **Original**: (अग्निपुराण 172। 2--18 ) प्रापप्रणाशर्न .. स्तोत्र. य: पठेच्छृणुयादपि । शारीरेमात्सवार्जै: कृत: पाप: प्रमुच्यते
- **Translation**: 

---

### Verse 20 (Agni Puran 0.3500)
- **Original**: सर्वपाप्ग्रहादिभ्यों याति बिष्णों: परं॑ पदम्‌ । तस्मात्‌ पापे कुते जर्ष्य स्तोत्र सर्वाघसर्दनम्‌
- **Translation**: 

---

