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

### Verse 1 (Vaivtpuran 16.3374)
- **Original**: रस्सीमें बाँध दिया। इससे तुम्हारे साथ जगत्‌के अधीन हैं। समयानुसार वृक्ष उगते, उनपर शाखाएँ
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3375)
- **Original**: व्यवहारमें मैं फँस गया। पुनः: विलग हो जाना फैलतों, पुष्प लगते और क्रमशः वे फलसे लद॒
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3376)
- **Original**: बिधिकी इच्छापर ही निर्भर है। शोक एवं विपत्ति जाते हैं। फिर काल हीं उन फलोंको पकाता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3377)
- **Original**: सामने आनेपर अज्ञानी व्यक्ति घबराता है न कि भी है। बादमें कालके प्रभावसे फूल-फलकर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3378)
- **Original**: पण्डित पुरुष। कालचक्रके क्रमसे सुख और वे सम्पूर्ण वृक्ष नष्ट भी हो जाते हैं। सुन्दरि!
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3379)
- **Original**: दुःख एकके बाद एक आते-जाते ही रहते हैं। समयपर विश्व उत्पन्न होता है और समयानुसार
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3380)
- **Original**: अब तुम्हें निश्चय ही वे सर्वेश भगवान्‌ नारायण उसकी अन्तिम घड़ी आ जाती है। कालकी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3381)
- **Original**: साक्षात्‌ पतिरूपमें प्राप्त होंगे, जिनके लिये बदरी- महिमा स्वीकार करके ब्रह्मा सृष्टि करते हैं और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3382)
- **Original**: आश्रममें रहकर तुम तपस्या कर चुकी हो। विष्णु पालनमें तत्पर रहते हैं। रुद्रका संहार-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3383)
- **Original**: तपस्या तथा ब्रह्माके बर-प्रदानसे तुम्हें पानेका कार्य भी कालके संकेतपर ही निर्भर है। सभी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3384)
- **Original**: सुअवसर मुझे प्राप्त हुआ था। कामिनि ! उस समय क्रमशः कालानुसार अपने व्यापारमें नियुक्त होते
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3385)
- **Original**: तुम भगवान्‌ श्रीहरिके लिये तप कर रही थी। हैं। ब्रह्मा, विष्पु और शिव आदि प्रधान
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3386)
- **Original**: अत: अब उन्हींको प्राप्त करोगी। गोलोकमें देवताओंके भी अधीश्वर हैं-परमात्मा श्रीकृष्ण।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3387)
- **Original**: बृन्दावन है। वहीं तुम भगवान्‌ गोविन्दको जो प्रकृतिसे परे हैं, उन्हींकों स्रष्टा, पाता और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3388)
- **Original**: पाओगी। मैं भी इस दानवी शरीरका परित्याग संहर्ता कहते हैं। वे सदा अपने सम्पूर्ण अंशसे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3389)
- **Original**: करके उसी दिव्यलोकमें चलूँगा। बहीं तुम मुझे विराजमान रहते हैं। वे ही समयपर स्वेच्छापूर्वक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3390)
- **Original**: देख सकोगी और मैं तुम्हें। इस समय जो मैं प्रकृतिको उत्पन्न करके विश्वमें रहनेवाले सम्पूर्ण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3391)
- **Original**: परम दुर्लभ भारतवर्षमें आया हूँ, इसमें कारण चराचर पदार्थोंको रचते हैं। उन्हें सर्वेश, सर्वरूप,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3392)
- **Original**: केवल श्रीराधाजीका शाप है। प्रिये! सुनो! मेरा सर्वात्मा और परमेश्वर कहते हैं। वे जनसे जनको
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3393)
- **Original**: गोलोकमें पुनः: जाना सर्वथा निश्चित है। अतः सृष्टि करते, जनसे जनकी रक्षा करते तथा जनसे
- **Translation**: 

---

