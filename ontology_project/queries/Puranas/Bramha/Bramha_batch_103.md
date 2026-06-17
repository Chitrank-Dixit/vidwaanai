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

### Verse 1 (Bramha 0.2041)
- **Original**: मेरी रक्षा कीजिये। भगवन्‌! आपका श्रोअड्ज वाद्य, सुगन्ध, संगीत, अद्भराग, इन्द्रनील, महानील,
- **Translation**: 

---

### Verse 2 (Bramha 0.2042)
- **Original**: अज्ञनके समान श्याम है। भक्तवत्सल! आपको पद्मराग, सोना, चाँदी, हीरा, स्फटिक आदि
- **Translation**: 

---

### Verse 3 (Bramha 0.2043)
- **Original**: नमस्कार है। अनिरुद्ध! आपको प्रणाम है। मणियाँ, राग, अर्थ, काम, वन्य पदार्थ अथवा
- **Translation**: 

---

### Verse 4 (Bramha 0.2044)
- **Original**: आप मेरी रक्षा करें और वरदायक बनें। सम्पूर्ण दिव्य वस्तुओंसे भी उनके मनको संतोष नहीं
- **Translation**: 

---

### Verse 5 (Bramha 0.2045)
- **Original**: देवताओंके निवासस्थान! आपको नमस्कार है। होता था। पत्थर, मिट्टी और लकड़ीमेंसे इस देवप्रिय! आपको प्रणाम है। नारायण! आपको पृथ्बीपर सर्वोत्तम वस्तु कौन है? किससे भगवान्‌
- **Translation**: 

---

### Verse 6 (Bramha 0.2046)
- **Original**: नमस्कार है। आप मुझ शरणागतकी रक्षा कीजिये। विष्णुकी प्रतिमाका निर्माण ठीक हो सकता है?
- **Translation**: 

---

### Verse 7 (Bramha 0.2047)
- **Original**: बलवानोंमें श्रेष्ठ बलराम! आपको प्रणाम है। इस प्रकारकी चिन्तामें पड़े-पड़े उन्होंने पाछरात्रको
- **Translation**: 

---

### Verse 8 (Bramha 0.2048)
- **Original**: हलायुध! आपको नमस्कार है। चतुर्मुख ! जगद्धाम ! विधिसे भगवान्‌ पुरुषोत्तमका पूजन किया और
- **Translation**: 

---

### Verse 9 (Bramha 0.2049)
- **Original**: प्रपितामह! मेरी रक्षा कीजिये। नील मेघके अन्तमें इस प्रकार स्तवन आरम्भ किया-- समान आभावाले घनश्याम! आपको नमस्कार *वासुदेव! आपको नमस्कार है। आप मोक्षके
- **Translation**: 

---

### Verse 10 (Bramha 0.2050)
- **Original**: है। देवपूजित परमेश्वर! आपको प्रणाम है। कारण हैं। आपको मेरा नमस्कार है। सम्पूर्ण
- **Translation**: 

---

### Verse 11 (Bramha 0.2051)
- **Original**: सर्वव्यापी जगन्नाथ! मैं भवसागरमें डूबा हुआ लोकोंके स्वामी परमेश्वर! आप इस जन्म-मृत्युरूपी ; हूँ, मेरा उद्धार कीजिये।* हर वासुदेव नमस्तेउस्तु नमस्ते मोक्षकारण । त्राहि मां सर्वलोकेश जन्मसंसारस्तागरातू
- **Translation**: 

---

### Verse 12 (Bramha 0.2052)
- **Original**: निर्मलाम्बरसंकाश नमस्ते. पुरुषोत्तम । संकर्षण नमस्ते5स्तु त्राहिं मां धरणीधर
- **Translation**: 

---

### Verse 13 (Bramha 0.2053)
- **Original**: नमस्ते हेमगर्भाय नमस्ते मकरध्बज । रतिकान्त नमस्ते5स्तु त्राहि मां शम्बरान्तक
- **Translation**: 

---

### Verse 14 (Bramha 0.2054)
- **Original**: जमस्तेउजनसंकाश नमस्ते भरवत्सल
- **Translation**: 

---

### Verse 15 (Bramha 0.2055)
- **Original**: अनिरुद्ध नमस्तेउस्तु ज्राहि मां घरदों भव
- **Translation**: 

---

### Verse 16 (Bramha 0.2056)
- **Original**: नमस्ते विबुधाबास नमस्ते विबुधप्रिय ! नारायण नमस्ते5स्तु ज्राहि मां शरणागतम्‌
- **Translation**: 

---

### Verse 17 (Bramha 0.2057)
- **Original**: 102 * संक्षिप्त ब्रह्मपुराण « प्रलयाग्रिके समान तेजस्वी तथा दहकते हुए
- **Translation**: 

---

### Verse 18 (Bramha 0.2058)
- **Original**: उपचारसे ही कहे गये हैं; आप तो अट्ठैत हैं। फिर नेत्रोंवाले महापराक्रमी दैत्यशत्रु नूसिंह! आपको
- **Translation**: 

---

### Verse 19 (Bramha 0.2059)
- **Original**: कोई भी मनुष्य आपको द्वैतरूप कैसे कह सकता नमस्कार है। आप मेरी रक्षा कीजिये। पूर्वकालमें
- **Translation**: 

---

### Verse 20 (Bramha 0.2060)
- **Original**: है। हरे! आप एकमात्र व्यापक, चित्स्वभाव तथा महावाराहरूप धारणकर आपने जिस प्रकार इस
- **Translation**: 

---

