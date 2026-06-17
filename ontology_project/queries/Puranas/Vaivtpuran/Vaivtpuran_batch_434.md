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

### Verse 1 (Vaivtpuran 23.1642)
- **Original**: पूजा करे। मूलमशत्रका यथाशक्ति जप करके इष्टदेवके गया। अब पूजनकी विधि सुनो। श्रीहरिकी पूजा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1643)
- **Original**: मन्त्रका विसर्जन करे। फिर भाँति-भाँतिके उपहार बहुसंख्यक सज्जनोंद्रारा सम्मानित है। अत: शास्त्रके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1644)
- **Original**: निवेदित करके स्तुतिके पश्चात्‌ कबचका पाठ करे।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1645)
- **Original**: + ग्रह्दखण्ड « 3 अफ श्र अऋ#8 8 4 8
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1646)
- **Original**: हक 8 5 58 88948 88#8 54988 % 48/15/4641 454 /ऋफ 4: /फ्ऊ 4 ड़ डक़्ऊड 5 $ हक कड़क क तत्पश्चात्‌ विसर्जन करके पृथ्वीपर माथा टेककर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1647)
- **Original**: दान करें। यह सब करके पुण्यात्मा साधक प्रणाम करे। इस तरह देबपूजा सम्पन्न करके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1648)
- **Original**: आवश्यक आहार-विहारमें प्रवृत्त हो। श्रुतिमें बुद्धिमान्‌ू एवं विद्वान्‌ पुरुष श्रौत तथा स्मार्त
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1649)
- **Original**: पूजनका यही क्रम सुना गया है। नारद! इस अग्रिसे युक्त यज्ञका अनुष्ठान करे। मुने! यज्ञके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1650)
- **Original**: प्रकार मैंने तुमसे सम्पूर्ण वेदोक्त उत्तम सूत्रका पश्चात्‌ दिक्‍्याल आदिको बलि देनी चाहिये। फिर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1651)
- **Original**: तथा ब्राह्मणोंक आहिक कर्मका वर्णन किया। यथाशक्ति नित्य-श्राद्ध और अपने वैभवके अनुसार
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1652)
- **Original**: अब और क्या सुनना चाहते हो? (अध्याय 26) न ब्राह्मणोंके लिये भक्ष्याभक्ष्य तथा कर्तव्याकर्तव्यका निरूपण नारदजीने पूछा--प्रभो! गृहस्थ ब्राह्मणों, पाप खाता है, इसमें संशय नहीं है। नारद! यतियों, वैष्णवों, विधवा स्त्रियों और ब्रह्मचारियोंके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1653)
- **Original**: एकादशौका दिन प्राप्त होनेपर गृहस्थ ब्राह्मणोंको लिये क्‍या भक्ष्य है और क्‍या अभक्ष्य? क्‍या
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1654)
- **Original**: कदापि अन्न नहीं खाना चाहिये, नहीं खाना कर्तव्य है और क्‍या अकर्तव्य ? अथवा उनके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1655)
- **Original**: चाहिये, नहीं खाना चाहिये। जन्माष्टमीके दिन, लिये क्‍या भोग्य है और क्‍या अभोग्य? आप
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1656)
- **Original**: रामनवमीके दिन तथा शिवरात्रिके दिन जो अन्न सर्वज्ञ, सर्वेध्र और सबके कारण हैं, अत: मेरी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1657)
- **Original**: खाता है, वह भी दूने पातकका भागी होता है। पूछी हुई सब बातें बताइये। जो सर्वथा उपवास करनेमें समर्थ न हो, वह महादेवजीने कहा--मुने! कोई तपस्वी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1658)
- **Original**: फल-मूल और जल ग्रहण करे; अन्यथा उपवबासके ब्राह्मण चिरकालतक मौन रहकर बिना आहारके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1659)
- **Original**: कारण शरीर नष्ट हो जानेपर मनुष्य आत्महत्याके ही रहता है। कोई वायु पीकर रह जाता है और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1660)
- **Original**: पापका भागी होता है। जो ब्रतके दिन एक कोई फलाहारी होता है। कोई गृहस्थ ब्राह्मण
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1661)
- **Original**: बार हविष्यात्र खाता अथवा भगवान्‌ विष्णुके अपनी स्त्रीके साथ रहकर यथोचित समयपर अन्न
- **Translation**: 

---

