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

### Verse 1 (Bramha 0.6001)
- **Original**: क्रोधमें आकर वर्षाकालके मेघकी भाँति उसने खेलते हुए वनमें घूमते थे। कभी झूला झूलकर
- **Translation**: 

---

### Verse 2 (Bramha 0.6002)
- **Original**: अपने शरीरकों बढ़ा लिया। बलरामजीने देखा, और कभी आपसमें कुश्ती लड़कर महाबली
- **Translation**: 

---

### Verse 3 (Bramha 0.6003)
- **Original**: उस दैत्यका रंग जले हुए पर्वतके समान है। श्रीराम और श्रीकृष्ण व्यायाम करते थे। उन
- **Translation**: 

---

### Verse 4 (Bramha 0.6004)
- **Original**: उसके गलेमें बहुत बड़ा हार लटक रहा था। दोनोंकों खेलते देख प्रलम्ब नामक दानव उन्हें
- **Translation**: 

---

### Verse 5 (Bramha 0.6005)
- **Original**: मस्तकपर बहुत बड़ा मुकुट था। आँखें गाड़ीके पकड़ ले जानेकी इच्छासे वहाँ आया। उसने
- **Translation**: 

---

### Verse 6 (Bramha 0.6006)
- **Original**: पहिये-जैसी घूम रही थीं। उसके पैर रखनेसे ग्वाल-बालोंके वेषमें अपने वास्तविक रूपकों
- **Translation**: 

---

### Verse 7 (Bramha 0.6007)
- **Original**: धरती डगमगाने लगती थी। उसका रूप बड़ा ही छिपा रखा था। मनुष्य न होते हुए भी मनुष्यका
- **Translation**: 

---

### Verse 8 (Bramha 0.6008)
- **Original**: भयंकर था। ऐसे राक्षसके द्वार अपनेको हरे जाते रूप धारण करके दानवोंमें श्रेष्ठ प्रलम्ब ग्वाल-
- **Translation**: 

---

### Verse 9 (Bramha 0.6009)
- **Original**: देख बलरामने श्रीकृष्णसे कहा--' कृष्ण! कृष्ण! बालोंकी उस मण्डलीमें बेखटके जा मिला। वह इधर तो देखो, ग्वाल-बालोंके वेषमें छिपा हुआ राम और कृष्ण दोनोंकों उठा ले जानेका अवसर
- **Translation**: 

---

### Verse 10 (Bramha 0.6010)
- **Original**: कोई दैत्य मुझे हरकर लिये जाता है। इसकी ढूँढने लगा। उसने कृष्णको तो सर्वथा अजेय
- **Translation**: 

---

### Verse 11 (Bramha 0.6011)
- **Original**: विकराल मूर्ति पर्वतके समान दिखायी देती है। समझा। अत: रोहिणीनन्दन बलरामको ही मारनेका
- **Translation**: 

---

### Verse 12 (Bramha 0.6012)
- **Original**: मधुसूदन! बताओ, इस समय मुझे क्‍या करना निश्चय किया। चाहिये। यह दुरात्मा बड़ी उतावलीके साथ भागा तदनन्तर उन ग्वाल-बालोंमें हरिणाक्रीडन नामक
- **Translation**: 

---

### Verse 13 (Bramha 0.6013)
- **Original**: जाता है।' खेल आरम्भ हुआ। यह बालकोंका वह खेल है, , यह सुनकर भगवान्‌ श्रीकृष्णक॑ ओठ मन्द जिसमें दो-दो बालक एक साथ हिरणकी तरह
- **Translation**: 

---

### Verse 14 (Bramha 0.6014)
- **Original**: मुसकानसे खिल उठे। वे रोहिणीनन्दन बलरामके उछलते हुए किसी निश्चित लक्ष्यतक जाते हैं।
- **Translation**: 

---

### Verse 15 (Bramha 0.6015)
- **Original**: बल और पराक्रमको जानते थे। अत: उनसे आगे पहुँचनेवाला विजयी होता है। हारा हुआ
- **Translation**: 

---

### Verse 16 (Bramha 0.6016)
- **Original**: बोले--'सर्वात्मन्‌! यह क्‍या बात है, आप तो बालक विजयीको अपनी पीठपर बिठाकर नियत
- **Translation**: 

---

### Verse 17 (Bramha 0.6017)
- **Original**: स्पष्टरूपमें मनुष्यकी-सी चेष्टा करने लगे। आप स्थानतक ले आता है। इस खेलमें सब लोग
- **Translation**: 

---

### Verse 18 (Bramha 0.6018)
- **Original**: सम्पूर्ण गुह्य पदार्थोंमें गुड्लसे भी गुह्मा हैं। जरा सम्मिलित हुए। दो-दो बालक एक साथ उछलते
- **Translation**: 

---

### Verse 19 (Bramha 0.6019)
- **Original**: अपने उस स्वरूपका तो स्मरण कीजिये, जो हुए चले। श्रीदामाके साथ श्रीकृष्ण, प्रलम्बके
- **Translation**: 

---

### Verse 20 (Bramha 0.6020)
- **Original**: सम्पूर्ण जगत्‌का कारण, कारणोंका भी पूर्ववर्ती, साथ बलराम तथा अन्य ग्वाल-बालोंके साथ
- **Translation**: 

---

