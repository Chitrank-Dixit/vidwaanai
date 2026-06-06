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

### Verse 1 (Vaivtpuran 23.1562)
- **Original**: लिये अयोग्य है। शौचाचारका पालन करके शुद्ध प्राणी रहते हों, जहाँ पेड़से गिरे हुए पत्तोंके ढेर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.1563)
- **Original**: हुआ ब्राह्मण स्रानके पश्चात्‌ दो धुले हुए बस्त्र लगे हों तथा जहाँकी भूमि हलसे जोती गयी हो,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.1564)
- **Original**: धारण करके पैर धो आचमनके पश्चात्‌ प्रातः- वहाँकी भी मिट्टी न ले। कुश और दूवके जड़से
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.1565)
- **Original**: कालकी संध्या करे। निकाली गयी, पोफ्लकी जड़के निकटसे लायी इस प्रकार जो कुलीन ब्राह्मण तीनों संध्याओंके गयी तथा शयनकी बेदीसे निकाली गयी मिट्टीकों
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.1566)
- **Original**: समय संध्योपासना करता है, वह समस्त तीथ्थोंमें भी शौचके काममें न लाये
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.1567)
- **Original**: चौराहेकी, गोशालाकी,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.1568)
- **Original**: स्नानके पुण्यका भागी होता है। जो त्रिकाल संध्या गायकी खुरीकी, जहाँ खेती लहलहा रही हो, उस
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.1569)
- **Original**: नहीं करता, वह अपवित्र है। समस्त कर्मोंके खेतकी तथा उद्यानकी मिट्टीको भी त्याग दे।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.1570)
- **Original**: अयोग्य है। वह दिनमें जो काम करता है, उसके ब्राह्मण नहाया हो अथवा नहीं, उपर्युक्त
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.1571)
- **Original**: फलका भागी नहीं होता। जो प्रातः और सायं शौचाचारके पालनमात्रसे शुद्ध हो जाता है तथा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.1572)
- **Original**: संध्याका अनुष्ठान नहीं करता, वह शूद्रके समान जो शौचसे हीन है, वह नित्य अपवित्र एबं समस्त
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.1573)
- **Original**: है। उसको समस्त ब्राह्मणोचित कर्मसे बाहर कर्मोंके अयोग्य है। विद्वान्‌ ब्राह्मण इस शौचाचारका
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.1574)
- **Original**: निकाल देना चाहिये।* प्रातः, मध्याह्न और सायं- * नोपतिष्ठति यः पूर्वां नोपास्ते यस्तु पश्चिमाम्‌ ।स॒शूद्रवद्वहिष्कार्य: सर्वस्माद्‌ द्विजकर्मण:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.1575)
- **Original**: (ब्रह्मणण्ड 26। 53)
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.1576)
- **Original**: संध्याका परित्याग करके द्विज प्रतिदिन त्रह्महत्या
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.1577)
- **Original**: है। तुम मेरे अद्रोंपर आरूढ़ हो समस्त पापोंको और आत्महत्याके पापका भागी होता है। जो
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.1578)
- **Original**: दूर कर दो। महाभागे! पुण्य प्रदान करो और एकादशीके व्रत और संध्योपासनासे हीन है, वह
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.1579)
- **Original**: मुझे स्नान करनेके लिये आज्ञा दो।' द्विज शूद्रजातिकी स्त्रीसे सम्बन्ध रखनेवाले पापीकी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.1580)
- **Original**: तपोधन! ऐसा कहकर नाभितक जलनमें भाँति एक कल्पतक कालसूत्र नामक नरकमें
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.1581)
- **Original**: प्रवेश करे और मन्त्रोच्चारणपूर्वक चार हाथ निवास करता है। प्रातःकालकी संध्योपासना करके
- **Translation**: 

---

