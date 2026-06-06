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

### Verse 1 (Vishnu Puran 0.9521)
- **Original**: 18 रौद्रं शकटचक्राक्ष॑ पादन्‍्यासचलःत्क्षितिम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9522)
- **Original**: अभीतमनसा तेन रक्षसा रोहिणीसुतः । हिचमाणस्तत: कृष्णमिर्द वचनमत्रवीत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9523)
- **Original**: 19 कृष्ण कृष्ण हिये होष पर्वतोटग्रमूर्त्तिना । केनापि पह्य दैत्येन गोपालच्छदारूपिणा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9524)
- **Original**: 20 यदत्र साम्प्रत॑ कार्य मया मधुनिषूदन। तत्कथ्यताँ प्रयात्येष दुरात्यातित्वरान्वित:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9525)
- **Original**: 21 औपराचर उयाच तमाह राम॑ गोविन्द: स्मितभिन्नोप्ठसम्पुट: । महात्मा रौहिणेयस्य बलबीर्यप्रमाणबित्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9526)
- **Original**: 22 उकवाच किमय॑ मानुषो भावों व्यक्तमेबावलम्ब्यते । सर्वात्मिन्‌ सर्बगुह्मानां गुह्गुह्मात्मना त्वथा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9527)
- **Original**: 23 स्मराशेषजगद्दीजकारणं. कारणाग्रजम्‌ । आत्मानमेकं तद्ब॒च्च जगत्येकार्णवे च यत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9528)
- **Original**: रड कि न वेत्सि यथाहं च त्वं चैक कारणं भुवः । भारावतारणार्थाय. मर्त्वलोकमुपागतो
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9529)
- **Original**: 25 नभदिदरस्तेउम्बुवहाश्व केशाः पादौ श्षितिर्वक्त्रमनन्त यहिः। पञ्णचम अंश छैडढे बालक उठे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9530)
- **Original**: तत्र श्रीदामाके साथ कृष्णचन्द्र, अ्रलम्बके साथ बत्ठरगम और इसी ग्रकार अन्यान्य गोपोंके साथ और-और ग्वाल्बार [ होड़ बदकर ] उछलते हुए चलने रूणे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9531)
- **Original**: अन्तमें, कृष्णचनद्धने श्रीदामाको, बलरामजीने प्रऊुम्बक्ों तथा अन्‍्यान्य कृष्णपक्षोय गोपोंने अपने प्रतिपक्षियोंक्त्रे हता दिया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9532)
- **Original**: डस खेलमें जो-जो बालक हारे थे वे सब जीत्तनेवास्त्रेंको अपने- अपने कचोंपर चढ़ाकर भाण्डीरवटतक ले जाकर वहाँसे फिर लौट आये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9533)
- **Original**: कित्तु प्रलम्बासुर अपने ऋचन्‍्धेपर बलरामजीको चढ़ाकर चद्रमाके सहित मेसके समान अत्यन्त बेगसे आकाहामण्डकको चछ दिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9534)
- **Original**: वह दानवश्नेष्ठ येहिणीननदन श्रीबलभद्रजीके आरको सहन न कर सकतेके कारण वर्षाकालीन सेयके समान बढ़कर अत्यन्त स्थूल शरीरवाला हो गया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9535)
- **Original**: तब मात्न्र और आभूषण धारण किये, सिरपर मुकुट पहने, गाड़ीके पहियोकि समान भयानक नेत्रॉवाले, अपने पघादप्रहारसे पृथ्वोको कम्पायमान करते हुए तथा दग्धपर्वतके समान आकास्वाले उस दैत्यकों देखकर उस निर्मय राक्षसके द्वारा ले जाबे जाते हुए बलभद्रजीने ऊृष्णचन्द्रसे कहा--
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9536)
- **Original**: “भैया कृष्ण ! देखो, छड़ापूर्वक गोपवेष धारण करनेखाला कोई पर्वतके समान महाकाय दैल्य मुझे हरे लिये जाता है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9537)
- **Original**: हे मधुसूदन ! अब मुझे क्या करना चाहिये, यह बतलाओ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9538)
- **Original**: देखो, यह दुरात्मा बड़ी झीघ्रतासे दौड़ा जा रहा है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9539)
- **Original**: श्रीपाशरजी गोले--ठबव॒ रोहिणीनन्दतके बह़वीर्यको जाननेबाले महात्मा श्रीकृष्णचद्धने मधुर- मुसकानसे अपने ओषछ्ठसम्पुटकों खोलते हुए उन बलरामजीसे कहा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9540)
- **Original**: श्रीकृष्णचन्द्र बोले--हे सर्वात्मन्‌ ! आप सम्पूर्ण गुड़ा पदार्थो्में अत्यन्त गृद्मस्वरूप होकर भी यह स्पष्ट मानव-भाव क्‍यों अवल्म्बत कर रहे हैं ?
- **Translation**: 

---

