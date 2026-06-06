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

### Verse 1 (Vaivtpuran 29.7398)
- **Original**: कल्पोंतक जप करनेपर भी मन्त्र सिद्धिदायक नहीं था। इसे जिस-किसीको नहीं बतलाना चाहिये।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 29.7399)
- **Original**: होता। वत्स! इस कवचको धारण करके तुम जो विधिपूर्वक गुरुका पूजन करके इस कवचको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 29.7400)
- **Original**: आनन्दपूर्वक नि:शड्डू होकर अनायास ही इक्कीस गलेमें अथवा दाहिनी भुजापर धारण करता है,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 29.7401)
- **Original**: बार पृथ्वीको क्षत्रियोंसे शून्य कर डालो। बेटा! वह भी विष्णुतुल्य हो जाता है; इसमें संशय॑
- **Translation**: 

---

### Verse 5 (Vaivtpuran 29.7402)
- **Original**: प्राणसंकटके समय राज्य दिया जा सकता है, सिर नहीं है। वह भक्त जहाँ रहता है, वहाँ लक्ष्मी और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 29.7403)
- **Original**: कटाया जा सकता है और प्राणोंका परित्याग भी सरस्वती निवास करती हैं। यदि उसे कवच सिद्ध
- **Translation**: 

---

### Verse 7 (Vaivtpuran 29.7404)
- **Original**: किया जा सकता है; परंतु ऐसे कवचका दान नहीं हो जाता है तो वह जीवन्मुक्त हो जाता है और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 29.7405)
- **Original**: करना चाहिये*। (अध्याय 31) 942 * महादेव उवाच-- वत्सागच्छ महाभाग भूगुबंशसमुद्धव । पुत्राधिकोउसि प्रेम्णा मे कबच॑ ग्रहणं कुरु
- **Translation**: 

---

### Verse 9 (Vaivtpuran 29.7406)
- **Original**: श्रेण.. राम प्रवक्ष्यामि ब्रह्माण्डे परमाद्भधुतम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 29.7407)
- **Original**: त्ैैलोक्यविजय॑ नाम श्रीकृष्णस्य जयावहम्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 29.7408)
- **Original**: श्रीकृष्णेणे पुरा दत्त गोलोके राधिकाश्रये । रासमण्डलमध्ये च महां पृन्दावने बने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 29.7409)
- **Original**: अतिगुद्वतरं तत्त्वं सर्वमन्त्रौधविप्रहम्‌ । पुण्यात्‌ पुण्यतरं चैव परं स्लरेहाद्‌ वदामि ते
- **Translation**: 

---

### Verse 13 (Vaivtpuran 29.7410)
- **Original**: यदू धृत्वा पठनाद्‌ देवी मूलप्रकृतिरीश्वरी । शुम्भ॑ निशुम्प॑ महिष॑ रक्तबीज॑ जघान ह
- **Translation**: 

---

### Verse 14 (Vaivtpuran 29.7411)
- **Original**: यद्‌ धृत्वाह॑ं च जगतां संहर्ता सर्वतत््ववित्‌ पूर्व यद्‌ धृत्वा कूर्मराजश्ष॒ शेष॑ धत्तेउवलीलया । यदू धृत्वा भगवान्‌ वायुर्विश्वाधारों विभुः स्वयम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 29.7412)
- **Original**: यद्‌ धृत्वा वरुण: सिद्ध: कुबेरश्ष धनेश्वःः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 29.7413)
- **Original**: यद्‌ धृत्वा पठनादिन्द्रों देबानामधिप: स्वयम्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 29.7414)
- **Original**: यद्‌ धृत्वा भाति तेजोराशि: स्वयं रथि: । यद्‌ धृत्या पठनाचन्‌्रों महाबलपराक्रम:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 29.7415)
- **Original**: अगस्त्य: सागरान्‌ू सप्त यद्‌ धृत्वा पठनात्‌ पपौ। चकार तेजसा जीर्ण दैत्य॑ वातापिसंज्ञकम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 29.7416)
- **Original**: यद्‌ धृत्वा पठनाद्‌ देवी सर्वाधारा वसुन्धरा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 29.7417)
- **Original**: यद्‌ धृत्वा पठनातू पूता गड्जा भुवनपावनी
- **Translation**: 

---

