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

### Verse 1 (Vaivtpuran 23.2162)
- **Original**: स्वाहा' यह मन्त्रका स्वरूप है। इस मन्त्रका जप
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.2163)
- **Original**: भक्त है, उसे सदा जीवन्मुक्त समझना चाहिये। करनेसे सम्पूर्ण विन्न टल जाते हैं। जो आपकी भक्तिसे विमुख है, बह मूर्ख जीते ब्रह्मपुत्र नारद! मन्त्रोपदेशके पश्चात्‌ परम प्रभु
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.2164)
- **Original**: हुए भी मरेके समान है। जिस अज्ञानीजनके श्रीकृष्णने उस बालकके भोजनकी जो व्यवस्था
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.2165)
- **Original**: हृदयमें आपकी भक्ति नहीं है, उसे जप, तप, की, बह तुम्हें बताता हूँ, सुनो! प्रत्येक विश्वमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.2166)
- **Original**: यज्ञ, पूजन, न्रत, उपवास, पुण्य अथवा तीर्थ- वैष्णवजन जो कुछ भी नैवेद्य भगवान्‌को अर्पण
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.2167)
- **Original**: सेवनसे क्या लाभ? उसका जीवन ही निष्फल करते हैं, उसमेंसे सोलहवाँ भाग विष्णुको मिलता
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.2168)
- **Original**: है। प्रभो! जबतक शरीरमें आत्मा रहता है, है और पंद्रह भाग इस बालकके लिये निश्चित
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.2169)
- **Original**: तबतक शक्तियाँ साथ रहती हैं। आत्माके चले है; क्योंकि यह बालक स्वयं परिपूर्णतम श्रीकृष्णका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.2170)
- **Original**: जानेके पश्चात्‌ सम्पूर्ण स्वतन्त्र शक्तियोंकी भी सत्ता विराट्-रूप है। वहाँ नहीं रह जाती। महाभाग! प्रकृतिसे परे वे विप्रवर! सर्वव्यापी श्रीकृष्णने उस उत्तम
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.2171)
- **Original**: सर्वात्मा आप ही हैं। आप स्वेच्छामय सनातन मन्त्रका ज्ञान प्राप्त करानेके पश्चात्‌ पुनः उस
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.2172)
- **Original**: ब्रह्मज्योति:स्वरूप परमात्मा सबके आदिपुरुष हैं। विराट्मय बालकसे कहा-पुत्र! तुम्हें इसके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.2173)
- **Original**: नारद! इस प्रकार अपने हृदयका उद्वार प्रकट सिवा दूसरा कौन-सा वर अभीष्ट है, वह भी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.2174)
- **Original**: करके बह बालक चुप हो गया। तब भगवान्‌ मुझे बताओ। मैं देनेके लिये सहर्ष तैयार
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.2175)
- **Original**: श्रीकृष्ण कानोंको सुहावनी लगनेवाली मधुर हूँ।! उस समय विराट्‌ व्यापक प्रभु हो बालकरूपसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.2176)
- **Original**: वाणीमें उसका उत्तर देने लगे। विराजमान था। भगवान्‌ श्रीकृष्णकी बात सुनकर भगवान्‌ श्रीकृष्णने कहा--वत्स ! मेरी ही उसने उनसे समयोचित बात कही। भाँति तुम भी बहुत समयतक अत्यन्त स्थिर &जर्रुू््ु होकर विराजमान रहो। असंख्य ब्रह्माओंके जीवन समाप्त हो जानेपर भी तुम्हारा नाश नहीं होगा। प्रत्येक ब्रह्माण्डमें अपने क्षुद्र अंशसे तुम विराजमान * रहोगे। तुम्हारे नाभिकमलसे विश्वलष्टा ब्रह्मा प्रकट
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.2177)
- **Original**: होंगे। ब्रह्मके ललाटसे ग्यारह रुद्रोंका आविर्भाव होगा। शिवके अंशसे वे रुद्र सृष्टिके संहारकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.2178)
- **Original**: व्यवस्था करेंगे। उन ग्यारह रुद्रोंमें 'कालाग्रि' « >>प-- 2+ 255
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.2179)
- **Original**: नामसे जो प्रसिद्ध हैं, वे ही रुद्र विश्वके संहारक बालकने कहा--आपके चरणकमलोमें मेरी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.2180)
- **Original**: होंगे। विष्णु विश्वकी रक्षा करनेके लिये तुम्हारे अविचल भक्ति हो-मैं यही वर चाहता हूँ। मेरी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.2181)
- **Original**: क्षुद्र अंशसे प्रकट होंगे। मेरे बुरके प्रभावसे तुम्हारे आयु चाहे एक क्षणकी हो अथवा दीर्घकालकी;
- **Translation**: 

---

