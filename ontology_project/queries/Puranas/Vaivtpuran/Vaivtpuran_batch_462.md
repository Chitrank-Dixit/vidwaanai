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

### Verse 1 (Vaivtpuran 23.2202)
- **Original**: और पाताल--ब्रिलोकीके सम्पूर्ण चराचर प्राणियोंका जो इस समय भी विद्यमान हैं। इनकी सदा युवा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.2203)
- **Original**: उन्होंने सृजन किया। अवस्था रहती है। इनका श्याम रंगका वबिग्रह नारद! इस प्रकार महाविराट्‌ पुरुषके सम्पूर्ण है। ये पीताम्बर पहनते हैं। जलरूपी शब्यापर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.2204)
- **Original**: रोमकृपोंमें एक-एक करके अनेक ब्रह्माण्ड हुए। सोये रहते हैं। इनका मुखमण्डल मुस्कानसे प्रत्येक ब्रह्माण्डमें एक श्षुद्र विराट्‌ पुरुष, ब्रह्मा, सुशोभित है। इन प्रसन्नमुख विश्वव्यापी प्रभुको विष्णु एवं शिव आदि भी हैं। ब्रह्मन्‌! इस प्रकार *जनार्दन' कहा जाता है। इन्हींके नाभिकमलसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.2205)
- **Original**: भगवान्‌ श्रीकृष्णके मड्भरलमय चरित्रका वर्णन कर ब्रह्मा प्रकट हुए और उसके अन्तिम छोरका पता
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.2206)
- **Original**: दिया। यह सारभूत प्रसंग सुख एवं मोक्ष प्रदान लगानेके लिये वे उस कमलदण्डमें एक लाख करनेवाला है। ब्रह्म! अब तुम और क्या सुनना युगोंतक चक्कर लगाते रहे। नारद! इतना प्रयास चाहते हों? (अध्याय 3)
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.3859)
- **Original**: » प्रकृंतिखिण्ड « 171 55 ऋ$ 5 $ 4 64% 455 $ $ 4 $ 4 % 4 6 44 4 4 4 455 5544 444 #4 884 44444 46 /& # 4 4 # 4 55 # % #% 4 ऊ 55 5 5 55% मुक्त कर देता है। द्विजजों चाहिये कि यह
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.3860)
- **Original**: सायंकालकी संध्योपासना नहीं करता है, बह पूर्वाभिमुख होकर बैठे। हाथकों सर्पकौ फणके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.3861)
- **Original**: शूद्रकी भाँति समस्त द्विजोचित कर्मोंसे बहिष्कृत समान कर ले। वह हाथ ऊर्ध्वमुख हो और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.3862)
- **Original**: कर देने योग्य हो जाता है। जीवनपर्यन्त त्रिकाल- ऊपरकी ओरसे कुछ-कुछ मुद्रित (मुँदा-सा) रहे।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.3863)
- **Original**: संध्या करनेवाले ब्राह्मणमें तेज अथवा तपके उसे किश्लित्‌ झुकाये हुए स्थिर रखे। अनामिकाके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.3864)
- **Original**: प्रभावसे सूर्यके समान तेजस्विता आ जाती है। बिचले पर्वसे आरम्भ करके नीचे और बायें होते
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.3865)
- **Original**: ऐसे ब्राह्मणकी चरणरजसे पृथ्वी पवित्र हो जाती हुए तर्जनीके मूलभागतक अँगूठेसे स्पर्शपूर्वक जप
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.3866)
- **Original**: है। जिस ब्राह्मणके हृदयमें संध्याके प्रभावसे पाप करे। हाथमें जप करनेका यही क्रम है।* श्वेत [स्थान नहीं पा सके हों, बह तेजस्वी द्विज कमलके बीजोंकी अथवा स्फटिक मणिकी माला
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.3867)
- **Original**: जीवन्मुक्त ही है। उसके स्पर्शमात्रसे सम्पूर्ण तीर्थ बनाकर उसका संस्कार कर लेना चाहिये। इन्हीं
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.3868)
- **Original**: पवित्र हो जाते हैं। पाप उसे छोड़कर वैसे हो वस्तुओंकी माला बनाकर तीर्थमें अथवा किसी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.3869)
- **Original**: भाग जाते हैं; जैसे गरुड़को देखकर सर्पोर्मे देवताके मन्दिर्में जप करे। पीपलके सात
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.3870)
- **Original**: भगदड़ मच जाती है। त्रिकाल संध्या न करनेवाले पत्तोंपर संयमपूर्वक मालाकों रखकर गोरोचनसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.3871)
- **Original**: द्विजके दिये हुए पिण्ड और तर्पणकों उसके पितर अनुलिप्त करे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.3872)
- **Original**: फिर गायत्री-जपपूर्बक दिद्ठान्‌ पुरुष
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.3873)
- **Original**: इच्छापूर्वक ग्रहण नहीं करते तथा देवगण भी उस मालाको स्नान करावे। तत्पश्चात्‌ उसी मालापर
- **Translation**: 

---

