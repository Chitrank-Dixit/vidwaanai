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

### Verse 1 (Vaivtpuran 13.10762)
- **Original**: उनके सौ जन्मोंका पुण्य नष्ट हो जाता है। मिलकर पति-सेवाकी सोलहवाँ कलाके बराबर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10763)
- **Original**: पतिब्रताका अपने पतिके प्रति सर्वदा समान स्नेह भी नहीं हैं। जो स्त्रियाँ पतिकी सेवा नहीं करतीं
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10764)
- **Original**: होता है। दूध पीते बच्चेपर माताओंका अधिक और पतिसे कटुवचन बोलती हैं, वे चन्द्रमा और । स्नेह देखा जाता है, परंतु वह पतित्नताके सूर्यकी सत्तापर्यन्‍्त कालसूत्र नरकमें गिरकर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10765)
- **Original**: पतिविषयक स्नेहकी सोलहवीं कलाके बराबर यातना भोगती हैं। वहाँ सपोंके बराबर बड़े-बड़े
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10766)
- **Original**: भी नहीं है। पतिसे बढ़कर कोई बन्धु, प्रिय देवता कीड़े दिन-रात उन्हें डँैसते रहते हैं और सदा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10767)
- **Original**: क्रथा गुरु नहीं है। स्त्रीके लिये पतिसे बढ़कर विपरीत एवं भयंकर शब्द किया करते हैं। उस
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10768)
- **Original**: धर्म, धन, प्राण तथा दूसरा कोई पुरुष नहीं है। नरकमें स्त्रियोंकों मल, मूत्र तथा कफका भोजन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10769)
- **Original**: जैसे वैष्णवोंका मन श्रीकृष्णचरणारविन्दमें हो करना पड़ता है। यमराजके दूत उनके मुखमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10770)
- **Original**: निमग्र रहता है, उसी प्रकार साध्वी स्त्रियोंका जलती लुआठौ डालते हैं। नरकका भोग पूरा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10771)
- **Original**: चित्त अपने प्रियतम पतिमें ही संलग्न रहता है। करके वे नारियाँ कृमियोनिमें जन्म लेती हैं और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10772)
- **Original**: ब्रह्मन्‌! पतिके बिना पतित्नता स्त्री एक क्षण भी सौ जन्मोंतक रक्त, मांस तथा बिष्ठा खाती हैं।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10773)
- **Original**: जीवित नहीं रह सकती। पतिके बिना साध्वी वेदवाक्योंमें यह निश्चित सिद्धान्त बताया गया है।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10774)
- **Original**: स्त्रियोंके लिये मरण ही जीवन है और जीवन मैं अबला हूँ। विद्वानोंके मुखसे सुनकर उपर्युक्त
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10775)
- **Original**: मृत्युसे भी अधिक कष्ट देनेवाला है। ब्रह्मन्‌! बातोंको कुछ-कुछ जानती हूँ। आप तो बेदोंका
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10776)
- **Original**: यदि मेरे बिना ही आप इन्हें मुक्त कर देंगे तो भी प्राकट्य करनेवाले हैं। प्रभु हैं। विद्वानों, प्रभो! मैं आपको शाप देकर स्त्री-हत्याका दारुण योगियों, ज्ञानियों तथा गुरुके भी गुरु हैं। अच्युत!
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10777)
- **Original**: पाप प्रदान करूँगी। * ब्रत॑ पतिद्रतायाश पतिरिव. श्रुताौ. श्रुतम्‌ । गुरुआषभीष्टदेवश्ष तपोधर्ममयः पति:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10778)
- **Original**: सर्वेषां च॒ प्रियतमो न बन्धु: स्वामिन: पर: । सर्वधर्मात्पा ब्रह्मनू पतिसेवा सुदुर्लभा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10779)
- **Original**: स्वामिसेवाचिहोनाया: सर्व॑ तन्निष्फल भवेत्‌। (17
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10780)
- **Original**: 67-69)
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10781)
- **Original**: ] श्रीकृष्णजन्मखण्ड न ड89 4#8#% #कऋऋ 4 % 4 % # # #$ # ##& 56 # ## 4 # 444 4 # # # ### 44% 4 4 हक ऋड ऋ #ऋ कक कक # 4 #
- **Translation**: 

---

