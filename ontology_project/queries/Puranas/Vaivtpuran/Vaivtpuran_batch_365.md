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

### Verse 1 (Vaivtpuran 17.1034)
- **Original**: कर डालते हैं। आप लोग भावुक हैं, बताइये निन्‍दा करता है तथा जो नराधम सभाके बीचमें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 17.1035)
- **Original**: तो सही, यदि विष्णु सदा और सर्वत्र व्यापक बैठकर उस निन्दाकों सुनता और हँसता है, वह
- **Translation**: 

---

### Verse 3 (Vaivtpuran 17.1036)
- **Original**: हैं तो आप लोग उनसे बर माँगनेके लिये * विष्णुपुराण प्रथम अंश अध्याय 3 के श्लोक 15 से 17 तक यह बात बतायी गयी है कि 'एक सहस्र चतुर्युग बीतनेपर ब्रह्माजीका एक दिन पूरा होता है। ब्रह्माजीके एक दिनमें चौदह मनु होते हैं। सप्तर्षि, देवगण, इन्द्र, मनु तथा मनुपुत्र-ये एक ही कालमें उत्पन्न होते हैं और एक ही कालमें उनका संहार होता है।' इससे सूचित होता है कि चौदहवें इन्द्रके बोतनेपर ब्रह्माका दिन पूरा होता है; परंतु यहाँ 28 वें इन्द्रके गत होनेपर ब्रह्माका एक दिन बताया गया है। इसकी संगति तभी लग सकती है, जब एक मन्वन्तरमें दो इन्द्रकी सृष्टि और संहार माने जायें। परंतु ऐसा माननेपर अन्य पुराणोंसे एकवाक्यता नहों होगी।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 17.1037)
- **Original**: » ख्रह्मखण्ड «» 84 %&5%%44$ 5 44 445 454 4 4 454 4 5445 # 54 555 #$ 4 5 454 44 4 54 4644 44 4 44 / 4 & 58 6 88 88 8
- **Translation**: 

---

### Verse 5 (Vaivtpuran 17.1038)
- **Original**: 8 84 8 8 # 8 # 4 4 555 श्रेतद्वीपमें क्यों गये थे? अंश और अंशीमें भेद
- **Translation**: 

---

### Verse 6 (Vaivtpuran 17.1039)
- **Original**: श्रीकृष्णरूपसे निवास करते हैं। वहाँ बहुत-सी नहीं है तथा आत्मामें भी भेदका अभाव है, यदि
- **Translation**: 

---

### Verse 7 (Vaivtpuran 17.1040)
- **Original**: गोपाड्ननाएँ, गौएँ तथा द्विभुज गोप-पार्षद उनकी यही आपका निश्चित मत है तो बताइये श्रेष्ठ पुरुष
- **Translation**: 

---

### Verse 8 (Vaivtpuran 17.1041)
- **Original**: सेवामें उपस्थित रहते हैं। वे गोलोकाधिपति कला (अंश)-का त्याग करके पूर्णतम (अंशी)-
- **Translation**: 

---

### Verse 9 (Vaivtpuran 17.1042)
- **Original**: श्रीकृष्ण ही परिपूर्णतम ब्रह्म हैं। वे ही समस्त की उपासना क्‍यों करते हैं? यद्यपि पूर्णतम
- **Translation**: 

---

### Verse 10 (Vaivtpuran 17.1043)
- **Original**: देहधारियोंके आत्मा हैं। वे सदा स्वेच्छामय रूप भगवान्‌ श्रीकृष्णणी कोटि जन्मोंतक आराधना
- **Translation**: 

---

### Verse 11 (Vaivtpuran 17.1044)
- **Original**: धारण करके दिव्य बृन्दावनके अन्तर्गत रासमण्डलमें करके भी उन्हें बशमें कर लेना अत्यन्त कठिन
- **Translation**: 

---

### Verse 12 (Vaivtpuran 17.1045)
- **Original**: विहार करते हैं। दिव्य तेजोमण्डल ही उनकी है और असाधु पुरुषोंके लिये तो वे सर्वथा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 17.1046)
- **Original**: आकृति है। वे करोड़ों सूर्यॉंके समान कान्तिमान्‌ असाध्य हैं, तथापि लोगोंकी बलबती आशा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 17.1047)
- **Original**: हैं। योगी एबं संत-महात्मा सदा उन्हीं निरामय उन्हींकी सेवा करना चाहती है। क्या छोटे और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 17.1048)
- **Original**: परमात्माका ध्यान करते हैं। नूतन जलधरके क्या बड़े, सभी परम पदको पाना चाहते हैं।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 17.1049)
- **Original**: समान उनकी श्याम कान्ति है। दो भुजाएँ हैं। जैसे बावना अपने दोनों हाथोंसे चन्द्रमाको छूना
- **Translation**: 

---

### Verse 17 (Vaivtpuran 17.1050)
- **Original**: श्रीअद्ञोंपर दिव्य पीताम्बर शोभा पाता है। उनका चाहे, उसी तरह लोग उन पूर्णतम परमात्माको
- **Translation**: 

---

### Verse 18 (Vaivtpuran 17.1051)
- **Original**: लावण्य करोड़ों कन्दर्पोसे भी अधिक है। वे हस्तगत करना चाहते हैं। जो विष्णु हैं, वे एक
- **Translation**: 

---

### Verse 19 (Vaivtpuran 17.1052)
- **Original**: लीलाधाम हैं। उनका रूप अत्यन्त मनोहर है। विषय (देश)-में रहते हैं। विश्वके अन्तर्गत
- **Translation**: 

---

### Verse 20 (Vaivtpuran 17.1053)
- **Original**: किशोर अवस्था है। थे नित्य शान्त-स्वरूप श्वेतद्वीपमें निवास करते हैं। आप, ब्रह्मा, महादेव,
- **Translation**: 

---

