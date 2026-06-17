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

### Verse 1 (Vaivtpuran 13.11062)
- **Original**: हुई, जो बड़े-बड़े मुनीश्वरों तथा योगसिद्ध विभूतियोंका वर्णन किया गया है। सबके जनक
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11063)
- **Original**: पुरुषोंक लिये भी दुर्लभ है। पूर्वकालमें ये श्रीहरि ही हैं। जप, तप, व्रत, ज्ञान, वेदाध्ययन,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11064)
- **Original**: पुण्यवती स्त्रियाँ कौन थीं और किस दोषसे इस पूजन, तीर्थ-सत्रान और उपवास--सबके फलदाता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11065)
- **Original**: भूतलपर आयी थीं। मेरे इस संदेहका निवारण श्रीकृष्ण ही हैं। जिसने श्रीकृष्णी सेवा कर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11066)
- **Original**: करनेवाली बात कहिये। ली, उसे तपस्याओंके फलोंसे क्‍या प्रयोजन है? भगवान्‌ श्रीनारायण बोले--नारद! ये जिसे कल्पवृक्षकी प्राप्ति हो गयी, वह दूसरे किसी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11067)
- **Original**: देवियाँ सप्तर्षियोंकी सुन्दर रूप-गुण-सम्पन्ना पतिव्रता वृक्षकों लेकर क्‍या करेगा? जिसके हृदयमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11068)
- **Original**: पत्नियाँ थीं। एक बार अनलदेवने इनका अज्जभ * अहोउतिधन्या यूय॑ च दृष्टो युप्माभिरीक्वर: । अस्माक॑ जीवन॑ व्यथ॑ वेदपाठो5प्यनर्थक:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11069)
- **Original**: वेदे पुराणे सर्वत्र विद्ृद्धि: परिकोर्तितम्‌ । हरेविभूतयं: सर्वा: सर्वेषां जनको हरि:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11070)
- **Original**: तपों जपो ब्रत॑ दान॑ वेदाध्ययनमर्चनम्‌ । तीर्थस्नानमनशन॑ सर्वेषां . फलदोी. हरि:
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11071)
- **Original**: श्रीकृष्ण: सेवितों येन कि तस्य तपसां फलै:ः । प्राप्त: कल्पतरुर्येंन कि. तस्यान्येन शाखिना
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11072)
- **Original**: श्रीकृष्णे इदये यस्य कि तस्य कर्मभि: कृतैः । कि. पीतसागरस्यैव. पौरुष॑ कूपलबूने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11073)
- **Original**: (18। 66--70 )
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11074)
- **Original**: ] श्रीकृष्णजन्मखण्ड ल्‍ 493 ###%### # #### # # # # # ## # #ऋऋ# #ऋ%&######ऋ##ऋ##ऋ#ऋ#%ऊऋऋऋ#%%क#%# 44 ## 4 # 48 ###%######% 55% %% स्पर्श कर लिया। इससे ससप्तर्षियोंमें अद्विराको
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11075)
- **Original**: महत्त्शाली हुआ। नीच पुरुषसे मिली हुई बड़ा क्षोभ हुआ और उन्होंने अग्रिको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11076)
- **Original**: सम्पत्ति भी निन्‍्दनीय है; किंतु महात्मा पुरुषसे 'सर्वभक्ष्य' होनेका तथा इन पत्नियोंको मानुषी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11077)
- **Original**: प्राप्त हुई विपत्ति भी श्रेष्ठ है। अहो! साधुपुरुषोंका योनिमें जानेका शाप दे दिया। ये सब रोती हुई
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11078)
- **Original**: कोप तत्काल ही उपकारमें बदल जाता है। बोलौं--'हम लोग निर्दोष हैं, पतित्रता हैं।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11079)
- **Original**: विपत्तिक बिना भूतलपर किसीकी महिमा कैसे हमारा त्याग न करें। आप हम डरी हुई
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11080)
- **Original**: प्रकट हो सकती है? पतियोंके परित्यागसे भूमिपर अबलाओंको अभय प्रदान करें।' उत्पन्न हुई ब्राह्मणपत्नियाँ श्रीहरिके दर्शनसे सदाके इनके करुण-क्रन्दससे मुनिकों दया आ
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11081)
- **Original**: लिये भवबन्धनसे मुक्त हो गयीं*। इस प्रकार गयी। वे भी दुःखी हो गये। अन्तमें उन्होंने
- **Translation**: 

---

