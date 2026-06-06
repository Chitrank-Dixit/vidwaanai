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

### Verse 1 (Vaivtpuran 543.13114)
- **Original**: (कल्याण), मोक्ष और संहारकर्ता। इसके अतिरिक्त जन्म ग्रहण करती हैं। उन सबका वह जन्म अपने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13115)
- **Original**: अन्य अर्थमें इस शब्दका प्रयोग नहीं देखा जाता। अभीष्ट पतिकी उपलब्धिके लिये ही होता है,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13116)
- **Original**: शिव शब्दका दूसरा कोई अर्थ बेदमें नहीं निरूपित ऐसा श्रुतिमें सुना गया है। पूर्व-जन्मका जो पति
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13117)
- **Original**: हुआ है। सुन्दरि! यदि तुम संहारकर्ता शिवको है, वही स्त्रियोंके प्रत्येक जन्ममें पति होता है।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13118)
- **Original**: चाहती हो, तब तो सर्वलोकभयंकर रुद्रको अपने जो स्त्री जिनकी पत्नी नियत है, वही उन्हें प्रत्येक
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13119)
- **Original**: प्रति अनुरक्त पाओगी। न तो तुम्हारा मोक्ष होगा जन्ममें प्राप्त होती है; अत: इस जन्ममें घोरतर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13120)
- **Original**: और न अपने अभीष्ट देवताकी सेवा ही उपलब्ध तपके पश्चात्‌ भी पतिको न पाकर मैं यहाँ इस
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13121)
- **Original**: होगी। भगवान्‌ श्रीहरिका स्मरण अमोघ है, वह शरीरकों अग्रिकुण्डमें होम दूँगी। मेरा यह
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13122)
- **Original**: सदा सब प्रकारसे सम्पूर्ण मड्रलॉका दाता है। कार्य पतिकी कामनाको लेकर होगा; इसलिये
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13123)
- **Original**: अब तुम शीघ्र ही अपने पिताके घर जाओ। वहाँ परलोकमें मैं उन्हें अवश्य प्राप्त करूँगी। मेरे आशीर्वादसे और अपने तपके फलसे तुम्हें यों कहकर पार्वती वहाँ ब्राह्मणके बार-बार
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13124)
- **Original**: परम दुर्लभ शिवके दर्शन प्राप्त होंगे। मना करनेपर भी उसके सामने ही अग्निकुण्डमें।. ऐसा कहकर ब्राह्मण वहीं अन्तर्धान हो समा गयी। परमेश्वरी राधे! पार्वतीके अग्नि-प्रवेश
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13125)
- **Original**: गया। दुर्गा “महादेव! महादेव!" का उच्चारण करते ही उसकी तपस्याके प्रभावसे वह अग्नि
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13126)
- **Original**: करती हुई पिताके घरकी ओर चल दी। पार्वतीका तत्काल चन्दनके समान शीतल हो गयी।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13127)
- **Original**: आगमन सुनकर मेना और हिमालय दिव्य यानको वृन्दावनविनोदिनि! एक क्षणतक अग्रिकुण्डमें
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13128)
- **Original**: आगे करके हर्षविद्वल हो अगवानीके लिये चले। रहकर जब शिवा ऊपर आने लगी, तब शिवने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13129)
- **Original**: सारा नगर सजाया गया। मार्गोपर चन्दन, कस्तूरी पुनः: सहसा उससे पूछा। आदिका छिड़काव हुआ। बाजे बजने लगे। श्रीमहादेवजी बोले--भद्े! तुम्हारी तपस्या
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13130)
- **Original**: शड्खध्वनि गूँज उठी। सड़कोंपर सिन्दूर तथा क्या है? (सफल है या असफल?) यह कुछ चन्दनके जलसे कीच मच गयी। नगरमें प्रवेश भी मेरी समझमें नहीं आया। जिस तपके प्रभावसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13131)
- **Original**: करके दुर्गाने माता-पिताके दर्शन किये। वे दोनों अग्निने तुम्हारा शरीर नहीं जलाया, उसीसे तुम्हारी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13132)
- **Original**: अत्यन्त प्रसन्‍न हो दौड़ते हुए सामने आये। उनके मनोवाज्छित कामना पूर्ण नहीं हुई; यह आश्चर्यकी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13133)
- **Original**: नेत्रोमें हर्षक आँसू भरे थे और अब्ज-अज्जञ बात है। तुम कल्याणस्वरूप शिवकों पति बनाना
- **Translation**: 

---

