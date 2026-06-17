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

### Verse 1 (Bramha 0.4241)
- **Original**: व्याकुल हो गये और ऐराबत हाथीको छोड़कर अत: उस समय छींकना, जँभाई लेना तथा
- **Translation**: 

---

### Verse 2 (Bramha 0.4242)
- **Original**: समुद्रके फेनमें घुस गये। फिर वज़में फेन भोजन करना भी मना है। ये सब कार्य सदा
- **Translation**: 

---

### Verse 3 (Bramha 0.4243)
- **Original**: लपेटकर उस फेनसे ही इन्द्रने अपने शत्रुका संहार ओटमें ही करने चाहिये। विशेषतः हँसना तो
- **Translation**: 

---

### Verse 4 (Bramha 0.4244)
- **Original**: कर डाला। जब नमुचिकी मृत्यु हो गयी तब दूसरोंके सामने हो ही नहीं। संध्याकालमें कभी
- **Translation**: 

---

### Verse 5 (Bramha 0.4245)
- **Original**: उसके छोटे भाई मयने अपने बड़े भाईके घातकका कंमरेके भीतर न रहे। प्रिये! मूसल, ऊखल,
- **Translation**: 

---

### Verse 6 (Bramha 0.4246)
- **Original**: विनाश करनेके लिये बड़ी भारी तपस्या कौ। सूप, पीढ़ा और ढक्कन आदिको दिन या रातमें
- **Translation**: 

---

### Verse 7 (Bramha 0.4247)
- **Original**: उसने अनेक प्रकारकी माया प्राप्त की, जो कभी न लाँघना। उत्तरकी ओर सिरहाना करके
- **Translation**: 

---

### Verse 8 (Bramha 0.4248)
- **Original**: देवताओंके लिये अत्यन्त भंयकर थों। उसने तथा संध्याकालमें कभी न सोना। झूठ न
- **Translation**: 

---

### Verse 9 (Bramha 0.4249)
- **Original**: सम्पूर्ण लोकोंकों शरण देनेवाले भगवान्‌ विष्णुसे बोलना। दूसरोंके घर न जाना। पतिके सिवा
- **Translation**: 

---

### Verse 10 (Bramha 0.4250)
- **Original**: भी वर प्राप्त किया। मय दानी और प्रियभाषी था। और किसी पुरुषपर कहीं भी दृष्टि न डालना।। उसने इन्द्रको जीतनेके लिये अग्नि और ब्राह्मणोंका
- **Translation**: 

---

### Verse 11 (Bramha 0.4251)
- **Original**: 208 * संक्षिप्त ब्रह्मपुराण +* पूजन आरम्भ किया। वह याचकोंको मुँहमाँगी
- **Translation**: 

---

### Verse 12 (Bramha 0.4252)
- **Original**: इन्द्रने 'बहुत अच्छा' कहकर मयकी प्रशंसा वस्तुएँ देने लगा। वन्दीजन सदा उसकी स्तुति
- **Translation**: 

---

### Verse 13 (Bramha 0.4253)
- **Original**: की और बिनीतकी भाँति माता दितिके पास गये। करते थे। इन्द्रने वायुसे अपने मायावी शत्रु मबकी
- **Translation**: 

---

### Verse 14 (Bramha 0.4254)
- **Original**: बहाँ जाकर दैत्यमाताकी सेवा-शुश्रुषामें लग गये। गति-बविधि जान ली। तब वे ब्राह्मणका येष
- **Translation**: 

---

### Verse 15 (Bramha 0.4255)
- **Original**: उनके मनमें क्या है, इस बातको दिति नहीं बनाकर उसके पास गये और बोले--' दैत्यराज!
- **Translation**: 

---

### Verse 16 (Bramha 0.4256)
- **Original**: जानती थीं। उनके गर्भमें जो मुनिका अमोघ तेज मैं याचक हूँ, मुझे मनोवाज्छित बर दीजिये। मैंने
- **Translation**: 

---

### Verse 17 (Bramha 0.4257)
- **Original**: था, वह किसीके लिये भी दुर्धर्ष था। इन्द्र गर्भके सुना है-आप दाताओंके सिस्मौर हैं। अतः
- **Translation**: 

---

### Verse 18 (Bramha 0.4258)
- **Original**: भीतर प्रवेश करनेकी इच्छासे अवसरकौ प्रतीक्षा आपके पास आया हूँ।' मयने उन्हें ब्राह्मण
- **Translation**: 

---

### Verse 19 (Bramha 0.4259)
- **Original**: करते हुए बहुत समयतक वहाँ रहे। एक दिन जानकर कहा-'दिया हुआ ही समझो। सामने
- **Translation**: 

---

### Verse 20 (Bramha 0.4260)
- **Original**: दिति संध्याकालमें उत्तरकी ओर सिरहाना करके याचककों पाकर दाता यह विचार नहीं करते कि
- **Translation**: 

---

