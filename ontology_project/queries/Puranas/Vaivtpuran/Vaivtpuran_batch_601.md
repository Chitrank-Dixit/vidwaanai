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

### Verse 1 (Vaivtpuran 49.4854)
- **Original**: दिन-रात अविरामगतिसे चक्रकी भाँति घूमना पड़ता साँपोंका मल-मूत्र खानेको विवश होता है।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 49.4855)
- **Original**: है। वह आगकी लपटोंसे जलता और यमदूतोंद्वारा तदनन्तर भारतमें सात-सात जन्मोंतक वह अपनी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 49.4856)
- **Original**: पीटा जाता है। इस प्रकार वह महापापी प्रतिदिन सात पोढ़ीके पूर्वजोंसहित गिरगिट और मेढक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 49.4857)
- **Original**: नरक-यातना भोगता है। घोर प्राकृतिक महाप्रलय होता है। इसके बाद विशाल वनमें सेमलका वृक्ष
- **Translation**: 

---

### Verse 5 (Vaivtpuran 49.4858)
- **Original**: बीतनेपर जब पुनः सृष्टिका आरम्भ होता है तो वह होता है। तत्पश्चात्‌ गूँगा मनुष्य एवं शूद्र होकर फिर वैसा ही हो जाता है। नरक-यातनाके पश्चात्‌ वह शुद्धि-लाभ करता है। हजारों वर्षोतक उसे विष्ठाका कौड़ा होना पड़ता आस्तीक बोले--गुरुपन्रीगमन करनेपर मानव
- **Translation**: 

---

### Verse 6 (Vaivtpuran 49.4859)
- **Original**: है। तदनन्तर वह पत्नीहीन नपुंसक चाण्डाल होता मातृगामी समझा जाता है। मातृगमन करनेपर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 49.4860)
- **Original**: है। तत्पश्चात्‌ उसे सात जन्मोंतक गलित कोढ़से मनुष्योंके लिये प्रायश्चित्त नहीं मिलता। नृपश्रेष्ठ !
- **Translation**: 

---

### Verse 8 (Vaivtpuran 49.4861)
- **Original**: युक्त शूद्र एवं नपुंसक होना पड़ता है। इसके बाद भारतवर्षमें मातृगामी पुरुषोंकों जो दोष प्राप्त होता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 49.4862)
- **Original**: वह कोढ़ी, अन्धा एवं नपुंसक ब्राह्मण होता है। है, वह शुद्रोंको ब्राह्मणेके साथ समागम करनेपर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 49.4863)
- **Original**: इस प्रकार सात जन्म धारण करनेके पश्चात्‌ उस लगता है। यदि ब्राह्मणी शूद्रके साथ मैथुन करे तो
- **Translation**: 

---

### Verse 11 (Vaivtpuran 49.4864)
- **Original**: महापापीकी शुद्धि होती है। उसे भी उतना ही दोष प्राप्त होता है। कन्या, मुनि बोले--इस प्रकार हमने शास्त्रके पुत्रवधू, सास, गर्भवती भौजाई और भगिनीके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 49.4865)
- **Original**: अनुसार सब बातें बतायीं। राजन्‌! तुम इन साथ समागम करनेपर भी वैसा ही दोष लगता है।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 49.4866)
- **Original**: विप्रवरको प्रणाम करों और निश्चय ही इन्हें अपने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 49.4867)
- **Original**: ] प्रकृतिखण्ड ] 259 538848#888# 8888 8448 88 88 # 88 # 8 # ## # 5 ### 8 8 ## 868 # 4 $ 4 % 8 % 8 % 5 8 5 4 4 4 5 4 55 45 5 84 88 888 8 घरको लौटा ले चलो। वहाँ यत्नपूर्वक ब्राह्मण-
- **Translation**: 

---

### Verse 15 (Vaivtpuran 49.4868)
- **Original**: पर फिर यहाँ आओगे। देवताका पूजन करके इनका आशीर्वाद लो। पार्वति! ऐसा कहकर सब मुनि, देवता, महाराज! इसके बाद शीघ्र ही वनको जाओ और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 49.4869)
- **Original**: राजा तथा बन्धुवर्गके लोग तुरंत अपने-अपने तपस्या करो। ब्राह्मणके शापसे छुटकारा मिलने-
- **Translation**: 

---

### Verse 17 (Vaivtpuran 49.4870)
- **Original**: स्थानको चले गये। (अध्याय 52) #जन+>>मगिपाय050..000 सुतपाके द्वारा सुयज्ञको शिवप्रदत्त परम दुर्लभ महाज्ञानका उपदेश श्रीपार्वतीजीने पूछा--प्रभो! मुनिसमूहोंके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 49.4871)
- **Original**: उन्होंने मेरे दिये हुए सर्वदुर्लभ परम तत्त्वका उन्हें चले जानेपर मनुष्योंके कर्मफलका वर्णन सुननेके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 49.4872)
- **Original**: उपदेश दिया। अनन्तर ब्रह्मशापसे विह्डल हुए नृपश्रेष्ठ सुयज्ञने अतिथि बोले--ब्रह्माजीके पुत्र मरीचि हैं। क्या किया? अतिथि ब्राह्मणने भी क्‍या किया ?
- **Translation**: 

---

### Verse 20 (Vaivtpuran 49.4873)
- **Original**: उनके पुत्र स्वयं कश्यपजी हैं। कश्यपके प्रायः वे लौटकर राजाके घरमें गये या नहीं, यह
- **Translation**: 

---

