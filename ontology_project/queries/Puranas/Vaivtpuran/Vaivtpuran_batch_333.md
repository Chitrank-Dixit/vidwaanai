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

### Verse 1 (Vaivtpuran 15.19259)
- **Original**: कृष्णवामाड्ूसम्भूता तेन कृष्णेन कीर्तिता
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.19260)
- **Original**: परमानन्दराशिश्ष स्वयं पूर्तितती सती । श्रुतिभि: कीर्तिता तेन परमानन्दरूपिणी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.19261)
- **Original**: कृषिर्मोक्षार्थचनो न एवोत्कृष्टवाचक: । आकारों दातृबचनस्तेन कृष्णा प्रकीर्तिता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.19262)
- **Original**: अस्ति बृन्दाबनं यस्यास्तेन बृन्दावनी स्मृता । बृन्दावनस्थाधिदेवी तेन बाथ प्रकीर्तिता
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.19263)
- **Original**: सड्ढः सखीनां यृन्द: स्थादकारो5प्यस्तिवाचक:। सखिवृन्दो5स्ति यस्याश्व सा बृन्दा परिकीर्तिता
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.19264)
- **Original**: वृन्दावने बिनोदश्च सो5स्या ह्वास्ति चतत्र वै
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.19265)
- **Original**: वेदा वदन्ति तां तेन वृन्दावनविनोदिनीम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.19266)
- **Original**: नखचन्द्रावली वक्त्रचन्द्रोडईस्ति यत्र संततम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.19267)
- **Original**: तेन चन्द्रावली सा चर कृष्णेन परिकीर्तिता
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.19268)
- **Original**: कान्तिरस्ति चन्द्रतुल्या सदा यस्या दिवानिशम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.19269)
- **Original**: सा चन्‍न्द्रकान्ता हर्षेण हरिणा परिकीर्तिता
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.19270)
- **Original**: शरच्चन्द्रप्रभा यस्याश्नाननेडस्ति दिवानिशम्‌। मुनिना कीर्तिता तेन शरच्चन्द्रप्रभानना
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.19271)
- **Original**: इदं बोडशनामोक्तमर्थव्याख्यानसंयुतम्‌ । नाराषणेन यहत्त॑ ब्रह्मणे नाभिपड्डजे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.19272)
- **Original**: ब्रह्मणा च पुरा दत्त धर्माय जनकाय में
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.19273)
- **Original**: धर्मेण. कृपया दत्त महामादित्यपर्वण । पुष्के च महातीर्थे पुण्याहे देवसंसदि
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.19274)
- **Original**: राधाप्रभावप्रस्तावे सुप्रसन्नेन चेतसा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.903)
- **Original**: ड6 आचरण नहीं करते*। क्योंकि वह महान्‌ वैर उत्पन्न करनेवाला, दोषोंका बीज और अमज्गलकारी होता है। जो अपने धर्मके आचरणमें लगा हुआ है, भगवान्‌के मन्त्रकी दीक्षा ले चुका है, श्रीहरिको समाराधनामें संलग्र है, गुरु, देवता और अतिथियोंका भक्त है, तपस्यामें आसक्त है, व्रत और उपवासमें लगा रहता है और सदा तोर्थसेवबन करता है, उसे देखकर रोग उसी तरह भाग जाते हैं, जैसे गरुड़को देखकर साँप। ऐसे पुरुषोंके पास जरा-अवस्था नहीं जाती है और न दुर्जय रोगसमूह ही उसपर आक्रमण करते हैं। पतिब्रते मालावति! वात, पित्त और कफ-ये तीन ज्वरके जनक हैं। ये जिस प्रकार देहधारियोंमें है संक्षिप्त ब्रह्मवैवर्तपुराण क पदार्थ, तक्ररहित दही, पके हुए बेल और तालके फल, ईखके रससे बनी हुई सब वस्तुएँ, अदरख, मूँगकी दालका जूस तथा शर्करामिश्रित तिलका चूर्ण--ये सब पित्तका नाश करनेवाली ओषधियाँ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.904)
- **Original**: हैं, जो तत्काल बल और पुष्टि प्रदान करती हैं पित्तका कारण और उसके नाशका उपाय
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.905)
- **Original**: बताया गया। अब दूसरी बात मुझसे सुनो। भोजनके बाद तुरंत सत्रान करना, बिना प्यासके जल पीना, सारे शरीरमें तिलका तेल मलना, ख्रिग्ध तैल
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.906)
- **Original**: तथा ज़्िग्ध आँवलेके द्रवका सेवन, बासी अन्नका भोजन, तक्रपान, केलेका पका हुआ फल, दही, वर्षाका जल, शक्करका शर्बत, अत्यन्त चिकनाईसे युक्त जलका सेवन, नारियलका जल, संचार करते और स्वयं जाते हैं, उसके विविध
- **Translation**: 

---

