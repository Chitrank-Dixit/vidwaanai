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

### Verse 1 (Vaivtpuran 13.11842)
- **Original**: बहुत कठिन होता है। वह बिना कारण ही और परलोकमें सबसे बड़ा बन्धु है। कुलवधुओंके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11843)
- **Original**: पतिको प्रतिदिन जली-कटी सुनाती थी। जिनके लिये पतिसे बढ़कर दूसरा कोई प्रियतम नहीं
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11844)
- **Original**: डरसे सारा जगत्‌ काँपता था, वे ही मुनि उस है। पति ही उनका महान्‌ गुरु है। देवपूजा, त्रत,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11845)
- **Original**: कन्दलीके कोपसे थर-थर काँपते थे और उसकी दान, तप, उपवास, जप, सम्पूर्ण तीर्थोमें स्नान, की हुई कटूक्तिको चुपचाप सह लेते थे। समस्त यज्ञोंकी दीक्षा, पृथ्वीकी परिक्रमा तथा दयानिधान मुनि मोहवश उसे तत्काल समझाने ब्राह्मणों और अतिथियोंका सेवन--ये सब पतिसेवाकी [लगते थे। कुछ ही कालमें उसकी सौ करृक्तियाँ सोलहवीं कलाके समान भी नहीं हैं। पतिब्रताकों [पूरी हो गयीं तो भी मुनिने कृपापूर्वक उसकी इन सबसे क्‍या प्रयोजन है? समस्त शास्त्रोंमें सौसे भी अधिक कदृक्तियोंको क्षमा किया। पतिसेवाको परम धर्म कहा गया है। अपनी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11846)
- **Original**: पत्नीकी जली-कटी बातोंसे मुनिका हृदय दग्ध
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11847)
- **Original**: + श्रीकृष्णजन्सखण्ड « प्र5 ऋ4#
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11848)
- **Original**: क कक ऋ% 8
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11849)
- **Original**: ##+ ##8### 8859 88 ## 2 हऋ#44# 455 क# हक 4 कक्ष कक ऊश्क
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11850)
- **Original**: कक अर कक 88 5 अक कक होता रहता था। दिये हुए बचनके अनुसार उस
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11851)
- **Original**: भी बढ़कर प्यारी है। फिर भी दुर्वचनके कारण कटूक्तिकारिणी स्त्रीके अपराध पूरे हो गये।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11852)
- **Original**: एक क्षणमें हम दोनोंके बीच तत्काल शत्रुता पैदा दुर्वासामुनि यद्यपि स्वत्माराम और दयालु थे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11853)
- **Original**: हो गयी। प्रभो! जो बीत गया सो गया। यह तथापि क्रोधकों नहीं छोड़ सके थे। उन्होंने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11854)
- **Original**: सब काम-दोषसे हुआ था। अब आप मेरा सारा मोहवश पत्नीको शाप दे दिया--' अरी तू राखका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11855)
- **Original**: अपराध क्षमा कर दें और बतावें इस समय मुझे ढेर बन जा।' मुनिके संकेतमात्रसे वह जलकर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11856)
- **Original**: क्‍या करना चाहिये। मैं क्या करूँ? कहाँ जाऊँ? भस्म हो गयी। जो ऐसी उच्छूछ्डुला स्त्रियाँ हैं,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11857)
- **Original**: कहाँ मेरा जन्म होगा? मैं तीनों लोकोंमें आपके उनका तीनों लोकोंमें कल्याण नहीं होता। शरीरके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11858)
- **Original**: सिवा किसीकी भार्या नहीं होऊँगी। भस्म हो जानेपर आत्माका प्रतिबिम्बरूप जीव
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11859)
- **Original**: यों कहकर कन्दलीका जीवात्मा मौन हो आकाशमें स्थित हो पतिसे विनवपूर्वक बोला।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11860)
- **Original**: गया। इधर शोकसे अचेत हो दुर्वासामुनि मूर्च्छित जीवने कहा--हे नाथ! आप अपनी ज्ञान-
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11861)
- **Original**: हो गये। वे स्वात्माराम और महाज्ञानी होकर भी दृष्टिसे सदा सब कुछ देखते हैं। सर्वज्ञ होनेके
- **Translation**: 

---

