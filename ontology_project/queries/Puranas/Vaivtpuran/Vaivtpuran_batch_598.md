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

### Verse 1 (Vaivtpuran 49.4794)
- **Original**: सब-के-सब प्रत्येक दोषसे प्रत्येक फलके भागी ब्राह्मणोंकों दक्षिणासहित सौ अच्छी और दुधारू
- **Translation**: 

---

### Verse 2 (Vaivtpuran 49.4795)
- **Original**: होते हैं। सत्कर्म, सत्य, पुण्य, स्वधर्म, तप, गौंओंका दान करे। प्रायश्चित्तसे पाप क्षीण हो
- **Translation**: 

---

### Verse 3 (Vaivtpuran 49.4796)
- **Original**: प्रतिज्ञा, दान, स्वगोष्टी-परिपालन, गुरुकृत्य, देवकृत्य, जानेपर भी मनुष्य अपने सम्पूर्ण पापसे मुक्त नहीं
- **Translation**: 

---

### Verse 4 (Vaivtpuran 49.4797)
- **Original**: कामकृत्य, द्विजपूजन, नित्य-कृत्य, विश्वास, होता। जो पाप शेष रह जाता है, उसीके फलसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 49.4798)
- **Original**: और परप्रदान-इनमें स्थित हुए मनुष्योंका वह दुःखी एवं चाण्डाल होता है। यदि आतिदेशिक
- **Translation**: 

---

### Verse 6 (Vaivtpuran 49.4799)
- **Original**: वध करता है, वह पापिष्ठ कृतघ्न कहा गया हत्या हुई हो अर्थात्‌ साक्षात्‌ गोवध आदि न होकर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 49.4800)
- **Original**: इनके लिये जो लोक हैं, वे उस जन्मसे उसके समान बताया गया कोई पापकर्म बन गया
- **Translation**: 

---

### Verse 8 (Vaivtpuran 49.4801)
- **Original**: योनियोंमें उपलब्ध होते हैं। राजेन्द्र! हो तो उसमें साक्षात्‌ की हुई हत्यासे आधा फल
- **Translation**: 

---

### Verse 9 (Vaivtpuran 49.4802)
- **Original**: कृतन्न जिन-जिन नरकोंमें जाते हैं, वे-वे नरक भोगना पड़ता है। अनुकल्परूप प्रायक्षित्तसे उस
- **Translation**: 

---

### Verse 10 (Vaivtpuran 49.4803)
- **Original**: निश्चय ही यमलोकमें विद्यमान हैं। हत्याका पाप यद्यपि क्षीण हो जाता है तथापि
- **Translation**: 

---

### Verse 11 (Vaivtpuran 49.4804)
- **Original**: सुयज्ञने पूछा--प्रभो! किस प्रकारके कृतप्र उससे पूर्णतया छुटकारा नहीं मिलता। कौन-सा कर्म करके किन-किन भयंकर नरकॉमें शुक्रने कहा--स्त्रीकी हत्या करनेपर निश्चय
- **Translation**: 

---

### Verse 12 (Vaivtpuran 49.4805)
- **Original**: जाते हैं? इसे एक-एक करके मैं सुनना चाहता ही गोहत्यासे दूना पाप लगता है। स्त्रीहत्यारा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 49.4806)
- **Original**: हूँ। आप बतानेकी कृपा करें। हजारों बर्षोतक कालसूत्र नामक नरकमें निवास कात्यायनने कहा--जों शपथ खाकर भी करता है। तदनन्तर बह महापापी मानव सात
- **Translation**: 

---

### Verse 14 (Vaivtpuran 49.4807)
- **Original**: अपने सत्यको मिटा देता है, उसका पालन नहीं जन्मोंतक सूअर और सात जन्मोंतक सर्प होता
- **Translation**: 

---

### Verse 15 (Vaivtpuran 49.4808)
- **Original**: करता, वह कृतप्र अवश्य ही चार युगोंतक है। इसके बाद उसकी शुद्धि होती है। कालसूत्र नरकमें निवास करता है। फिर सात- बृहस्पति बोले--स्त्रीहत्यासे दूना पाप
- **Translation**: 

---

### Verse 16 (Vaivtpuran 49.4809)
- **Original**: सात जन्मोंतक कौआ और उल्लू होकर पुनः सात लगता है नब्रह्महत्यामें। ब्रह्महत्यागा एक लाख
- **Translation**: 

---

### Verse 17 (Vaivtpuran 49.4810)
- **Original**: जन्मोंतक महारोगी शूद्र होता है। इसके बाद वर्षोतक निश्चय ही महाभयंकर कुम्भीपाक नरकमें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 49.4811)
- **Original**: उसकी शुद्धि होती है। तत्पश्चात्‌ सर्वश्री सननन्‍्दन, निवास करता है। तदनन्तर उस महापापीकों सौ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 49.4812)
- **Original**: सनातन, पराशर, जरत्कारु, भरद्वाज और विभाण्डकने वर्षोंतक विष्ठाका कीड़ा होना पड़ता है, इसके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 49.4813)
- **Original**: विभिन्न कृतप्लोंके भेद तथा उनको प्राप्त होनेवाली बाद सात जन्मोंतक सर्प होकर वह उस पापसे
- **Translation**: 

---

