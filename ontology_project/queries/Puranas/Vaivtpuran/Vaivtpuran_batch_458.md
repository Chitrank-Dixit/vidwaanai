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

### Verse 1 (Vaivtpuran 23.2122)
- **Original**: रोता रहा। माता-पिता उसे त्याग चुके थे। वह वह बालक जो केवल अण्डाकार था, ब्रह्माकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 23.2123)
- **Original**: निराश्रय होकर जलके अंदर समय व्यतीत कर आयुपर्यन्त ब्रह्माण्डगोलकके जलमें रहा। फिर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 23.2124)
- **Original**: रहा था। जो असंख्य ब्रह्माण्डका स्वामी है, उसीने समय पूरा हो जानेपर वह सहसा दो रूपोंमें प्रकर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 23.2125)
- **Original**: अनाथकी भाँति, आश्रय पानेकी इच्छासे ऊपरकी हो गया। एक अण्डाकार ही रहा और एक
- **Translation**: 

---

### Verse 5 (Vaivtpuran 23.2126)
- **Original**: ओर दृष्टि दौड़ायी। उसकी आकृति स्थूलसे भी शिशुके रूपमें परिणत हो गया। उस शिशुकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 23.2127)
- **Original**: स्थूल थी। अतएब उसका नाम ' महाविराट्‌” पड़ा। ऐसी कान्ति थी, मानो सौ करोड़ सूर्य एक साथ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 23.2128)
- **Original**: जैसे परमाणु अत्यन्त सूक्ष्मतम होता है, वैसे ही प्रकाशित हो रहे हों। माताका दूध न मिलनेके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 23.2129)
- **Original**: वह अत्यन्त स्थूलतम था। बह यालक तेजमें कारण भूखसे पीड़ित होकर वह कुछ समयतक
- **Translation**: 

---

### Verse 9 (Vaivtpuran 23.2130)
- **Original**: परमात्मा श्रीकृष्णके सोलहवें अंशकी बराबरी कर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 23.2131)
- **Original**: * संक्षिस अहस्ौयर्तपुराण « 66666746666666766766676174346464446164637417656
- **Translation**: 

---

### Verse 11 (Vaivtpuran 23.2132)
- **Original**: 44644464334 47744 46731 66616
- **Translation**: 

---

### Verse 12 (Vaivtpuran 23.2133)
- **Original**: 6761 66666 44 4 8 रहा था। परमात्मस्वरूपा प्रकृति-संज्ञ़क राधासे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 23.2134)
- **Original**: अलग-अलग ब्रह्मा, विष्णु और शिव हैं। बेटा उत्पन्न यह महान्‌ विराट्‌ बालक सम्पूर्ण विश्वका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 23.2135)
- **Original**: नारद! देवताओंकी संख्या तीन करोड़ है। ये आधार है। यही 'महाविष्णु” कहलाता है। इसके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 23.2136)
- **Original**: सर्वत्र व्याप्त हैं। दिशाओंके स्वामी, दिशाओंकी प्रत्येक रोमकूपमें जितने विश्व हैं, उन सबकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 23.2137)
- **Original**: रक्षा करनेवाले तथा ग्रह एवं नक्षत्र-सभी इसमें संख्याका पता लगाना श्रीकृष्णके लिये भी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 23.2138)
- **Original**: सम्मिलित हैं। भूमण्डलपर चार प्रकारके वर्ण हैं। असम्भव है। वे भी उन्हें स्पष्ट बता नहीं सकते।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 23.2139)
- **Original**: नीचे नागलोक है। चर और अचर सभी प्रकारके जैसे जगत्‌के रज:ःकणको कभी नहीं गिना जा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 23.2140)
- **Original**: प्राणी उसपर निवास करते हैं। सकता, उसी प्रकार इस शिशुके शरीरमें कितने नारद! तदनन्तर वह विराट्स्वरूप बालक ब्रह्मा और विष्णु आदि हैं-यह नहीं बताया जा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 23.2141)
- **Original**: बार-बार ऊपर दृष्टि दौड़ाने लगा। वह गोलाकार सकता। प्रत्येक ब्रह्माण्डमें ब्रह्मा, विष्णु और शिव
- **Translation**: 

---

