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

### Verse 1 (Vishnu Puran 0.2361)
- **Original**: उन अनन्तसे ही दक्ष और मरीचि आदि तथा अन्यान्य ऋषीश्चरोंकों धर्म, किन्‍्हीं अन्य मुनीधरोंको अर्थ एवं अन्य किन्हींको कामकी प्राप्ति हुई है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2362)
- **Original**: किन्हीं अन्य महापुरुषेनि ज्ञान, ध्यान और समाधिके द्वारा उन्होंके तत्वको जानकर अपने संसार-बन्धनक्त्रे काटकर मोक्षपद प्राप्त किया है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2363)
- **Original**: अतः सम्पत्ति, फेश्वर्य, माहात्प्य, ज्ञान, सत्तति और कर्म तथा सोक्ष--इन स्रबकी एकमात्र मूल श्रीहरिकी आराधना ही उपार्जनीय है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2364)
- **Original**: हे ट्विजगण ! इस प्रकार, जिनसे अर्थ, धर्म, काम और मोक्ष--ये चारों ही फल प्राप्त छोते हैं उनके लिये भी आप ऐसा क्यों कहते हैं कि 'अनन्तसे तुझे क्या प्रयोजन है ?'
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2365)
- **Original**: और बहूत कहनेसे क्या ल्थप ? आपसल्ोग तो मेरे गुरु हैं; उचित-अनुधित सभी कुछ कह
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2366)
- **Original**: ओऔ* 18 ] प्रथम अँझ 85 मत किक न परत जप हलत, स॒ एव जगतः पति:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2367)
- **Original**: स कर्त्ता च विकर्त्ता च संहर्ता च हृदि स्थित:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2368)
- **Original**: 27 स भोक्ता भोज्यमप्येब॑ स एवं जगदीश्वरः: । अवद्धिरेतत्क्षन्तव्य बाल्यादुक्ते तु यन्पया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2369)
- **Original**: 28 पुरोहित ऊचचु दह्यामानस्त्वभस्माभिरप्रिना बाल रक्षित: । भूयो न वक्ष्यसीत्येव॑ नैव ज्ञातोउस्यबुद्धिमान्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2370)
- **Original**: 29 यदास्मद्गचनागभोहग्राह॑ न॒त्यक्ष्यते भवान्‌। ततः कृत्यां विनाझाय तब स््रक्ष्याप दुर्मते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2371)
- **Original**: 30 अरह्माद उवात्त कः केन हन्यते जन्तुजजन्तुः कः केन रक्ष्यते हन्ति रक्षति चैलात्मा हासत्साथु सपाचरन्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2372)
- **Original**: 31 कर्मणा जायते सर्व कर्मैव गतिसाधनम्‌ । तस्मात्सर्वप्रयत्लेन साधुकर्म समाचरेत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2373)
- **Original**: 32 ओपयदार उवाच इत्युक्तास्तेन ते क्ुद्धा दैत्यराजपुरोहिता: । कृत्यामुत्पादयामासुर्ज्वालामाल्तेस्ज्वलाकृतिम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2374)
- **Original**: 33 अतिभीमा समागम्य पादन्यासक्षतक्षिति: । शुलेन साधु सड्क़ुद्धा तं जघानाशु वक्षसि
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2375)
- **Original**: 34 तत्तस्थ हृदय प्राप्य शुलं बाल्स्य दीप्ििमत्‌ । जगाम ख्वण्ड्ित॑ भूमौ तत्नापि झतथा गतम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2376)
- **Original**: 35 यत्रानपायी भगवान्‌ हथास्ते हरिरीश्वर:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2377)
- **Original**: भझे भवति बज्रस्य तत्र शूलस्य का कथा भवति वज्स्य तत्र शूलस्य का कथा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2378)
- **Original**: 36 अपापे तत्र पापैश्न पातिता दैत्यवाजकै: । तानेख सा जघानाझु कृत्या नाश जगाम च
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2379)
- **Original**: 37 कृत्यया द्ह्वामानांस्तान्विल्लेक्य स महामतिः । त्राहि कृष्णेत्यनन्तेति बदन्नभ्यवपच्मत
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2380)
- **Original**: 38 प्रह्मद उताच सर्वव्यापिन्‌ू जगद्रुप जगर्स्रष्टर्जनादन । पाहि विप्रानिमानस्मादु:सहान्मन्त्रपावकात्‌
- **Translation**: 

---

