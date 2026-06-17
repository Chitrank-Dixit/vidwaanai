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

### Verse 1 (Vishnu Puran 0.3201)
- **Original**: जम्बूद्ीपका लिस्तार एक लक्ष योजन है; और हे ब्रह्मन्‌ ! एक्षद्वीफका उससे दूना कहा जाता है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3202)
- **Original**: प्नक्षद्वीपके स्वामी मेघातिथिके सात पुत्र हुए। उनमें सबसे बड़ा शान्तहय था और उससे छोटा शिदिर
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3203)
- **Original**: उनके अनन्त क्रमशः सुस्तोदय, आनन्द, शित्र और क्षेमक थे तथा सातवाँ घुव था। ये सब प्लक्षद्वीफिी. अधीधर हुए
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3204)
- **Original**: [उनके अपने-अपने अधिकृत वर्षोमें! प्रथम दान्तहयवर्ष है तथा अन्य शिशिरवर्ष, सुखोदयबर्ष, आनन्दवर्ष, झिववर्ष, क्षेमकर्ष और धुबनर्ष हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3205)
- **Original**: तथा उनको मर्यादा निश्चित करनेबाके अन्य सात पर्वत है। हे मुनिश्रेष्ठ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3206)
- **Original**: उनके नाम ये हैं, सुनो--
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3207)
- **Original**: गोमेद, चन्द्र, नारद, दुन्दुधि, सोमक, सुमना सौर सातवाँ लैध्राज
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3208)
- **Original**: इन अति सुरुम्य वर्ष-पर्वतों और चर्षोंपें देवता और गन्धर्वोकि सहित सदा निष्पाप प्रजा निवास करती है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3209)
- **Original**: सहाँके निवासीगण पुण्यवान्‌ होते हैं और ले चिरकालतक जीवित रहकर मरते हैं; उनको किसी प्रकास्की आधि- व्याधि नहीं होती, निरन्तर सुख ही रहता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3210)
- **Original**: ठन वर्षोंकों सात ही समुद्रगामिनी नदियाँ हैं । उनके नाम मैं तुम्हे खतलाता हूँ जिनके श्रवणमात्रसे वे पापोंकों दूर कर देती हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3211)
- **Original**: वहाँ अनुतप्ता, झिखी, विपाशा, त्रिदिवा, अछमा, अमृता और -सुकृता--ये ही सात नदियाँ हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3212)
- **Original**: आअण्ड ] द्वितीय अंझ 117 एते झैलास्तथा नह्य: प्रधाना: कथितास्तव । क्षुद्रशौलास्तथा नद्यमस्तत्र सन्ति सहस्तहा: । ता: पिबन्ति सदा हष्टा नदीर्जनपदास्तु ते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3213)
- **Original**: 12 अपसर्पिणी न तेषां बै न चैवोत्सर्पिणी द्विज । न त्वेबास्ति युगावस्था तेषु स्थानेषु सप्तसु
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3214)
- **Original**: 13 ज्रेतायुगसम: कालः सर्वदैव महामते । प्रक्षद्वीपादिषु ब्रह्मम्छाकद्वीपान्तिकेषु तै
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3215)
- **Original**: 14 पञ्न वर्षसहस्नाणि जना जीवन्त्यनामया: । धर्मा: पञ्नञ॒ तथैतेषु वर्णाअ्रमविभागशः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3216)
- **Original**: 157 वर्णाश्न तत्र चत्वारस्ताश्निबोध वदामि ते
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3217)
- **Original**: 16 आर्यकाः कुरराश्चैव विदिश्या भाविनश्न ते । विप्रक्षत्रियवैश्यास्त शृद्राश्ष मुनिसत्तम
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3218)
- **Original**: 17 जम्बूवृक्षप्रमाणस्तु तत्मध्ये सुमहांस्तरु:। प्रक्षस्तन्नामसंज्ञो5यं प्र॒क्षद्वीपो द्विजोत्तम
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3219)
- **Original**: 18 इज्यते तत्र भगवांस्तैर्वएैरार्यकादिभि: । सोमरूपी जगर्स्रष्टा सर्व: सर्वेश्वरो हरि:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3220)
- **Original**: 19 प्रक्षद्वीपप्रमाणेन प्रक्षद्वीप: समावृतः । तथैवेक्षुरसोदेन परिवेषानुकारिणा
- **Translation**: 

---

