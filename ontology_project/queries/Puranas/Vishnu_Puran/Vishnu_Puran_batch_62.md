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

### Verse 1 (Vishnu Puran 0.1221)
- **Original**: 40 प्र॒व उवाच नाहमर्थमभीष्सामि न राज्य द्विजसत्तमा: । तत्स्थानमेकमिच्छामि भुक्ते नानयेन यत्पुरा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1222)
- **Original**: 41 एतन्प्रे क्रियर्ता सम्यक्कथ्यतां प्राप्पते यथा । स्थानमग्र्यं समस्तेभ्य: स्थानेभ्यो मुनिसत्तमा:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1223)
- **Original**: 42 मरीचिस्वाच अनाराधितगोविन्दैनर: स्थान नृपात्मज । न हि सम्प्राप्यते श्रेष्ठ तस्पादाराधयाच्युतम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1224)
- **Original**: 43 अन्रिरुवान्न परः पराणां पुरुषों यस्य तुष्ठो जनार्दनः । स्‌ ग्राप्रोत्यक्षय स्थानमेतत्सत्य॑ मयोदितम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1225)
- **Original**: 44 अड्लिय उवाच यस्यान्त: सर्वमेवेदमच्युतस्थाव्ययात्मन: । तमाराश्य गोविन्द स्थानमग्रयं यदीच्छसि
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1226)
- **Original**: 45 पुलत्त्य उवात्त पर॑ ब्रह्म पर॑ं धाम योउसो ब्रह्म तथा परम्‌ । तमाराध्य हरि याति मुक्तिमप्यतिदुर्लभाम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1227)
- **Original**: 46 4 के उत्पन्न हुआ राजा उत्तानपादका पत्र जानें। मैं आत्म- ग्ल्मनिके कारण आपके निकट आया हूँ
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1228)
- **Original**: ऋषि बोले--राजकुमार
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1229)
- **Original**: अभी तो तू चार-पाँच यर्षका ही बाउक है। अभी ऐरे निर्वेदका कोई कारण नहीं दिखायी पड़ता
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1230)
- **Original**: तुझे कोई चिन्ताका तिषय भी नहीं है, क्योकि अभों तेश पिता राजा जीवित है और हे बालक ! तेरी कोई इष्ट बस्तु खो गयी हो ऐसा भी हमें दिखायी नहीं टेता
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1231)
- **Original**: तथा हमें तेरे दारीरमें भी कोई व्याध्ि नहीं दीख पड़ती फिर बता, तेरी ग्लानिकां क्या कारण है ?
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1232)
- **Original**: श्रीपराधारजी बोले--तजब सूरुचिने उससे जो कुछ कहा या वह सब उसने कह सुनाया। उसे सुनकर ये ऋषिगण आपसमें इस प्रकार कहने छगे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1233)
- **Original**: 'अच्डे ! क्षात्रतेज कैसा प्रबक है, जिससे बालक्रमें भी इतनी अक्षमा है कि अपनी विपाताका कथन उसके हृदयसे नहीं टल्ता
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1234)
- **Original**: हे क्षत्रियक्रुमार ! इस निर्वेदके कारण तूने जो कुछ करनेका निश्चय किया है, यदि तुझे रुचे तो, बह हमल्ोगोंसे कह दे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1235)
- **Original**: और हे अतुलिततेजस्वी ! यह भी बता कि हम तेरी क्या सहायता वें, क्योंकि हमें ऐसा प्रतीत होता है कि तू कुछ कहना चाहता है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1236)
- **Original**: धुवने कहा--हे ट्विजश्रेष्ठ ! मुझे न तो धनकी इच्छा है और न ग़ज्यकी; मैं तो केवल एक उसी स्थानकों चाहता हूँ जिसको पहले कभो किसीने न भोगा हो
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1237)
- **Original**: हे मुनिश्रेष्ठ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1238)
- **Original**: आपकी यही सहायता होगी कि आप मुझे भट्मे प्रकार यह बता दें कि क्या करनेसे वह सबसे अग्रगण्य स्थान प्राप्त हो सकता है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1239)
- **Original**: मरीलि बोले--हे राजपुत्र ! बिना रोकिन्दकी आराधना किये मनुष्यको यह श्रेष्ठ स्थान नहीं मिल सकता; अतः तू श्रीअच्युतकी आराधना कर
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1240)
- **Original**: अन्रि बोले--जो पर प्रकृति आदिसे भी परे हैं ये परमपुरुष जनार्दन जिससे सन्‍्तृष्ट होते हैं उसीको वह अक्षयपद मिलता है यह में सत्य-सत्य कहता हूँ
- **Translation**: 

---

