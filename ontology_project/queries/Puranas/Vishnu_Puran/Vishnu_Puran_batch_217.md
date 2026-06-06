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

### Verse 1 (Vishnu Puran 0.4321)
- **Original**: अतः हे राजन्‌! इस “अहे झाब्दका मैं कहाँ प्रयोग करूँ ?
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4322)
- **Original**: तथा हे नपश्रेष्ट ! थटि मुझसे भिन्न कोई और भी सजातीय आत्पा हो तो भी “यह में हैँ और यह अन्य है' _ ऐसा कहा जा सकता था
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4323)
- **Original**: किन्तु, जब समस्त दारीरोमें एक ही आत्गा निराजमान हैं तल 'आप कौन हैं ? मैं वह हैं ।' ये सब वाक्य निष्फल ही हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4324)
- **Original**: 'तू राजा है, यह शिक्षिका है, ये सामते शिविकाबाहक हैं तथा ये सब तेरी प्रजा हैं'--हे नृप ! इनमेंसे कोई भी बात परमार्थतः सत्य नहीं है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4325)
- **Original**: हैं राजन्‌ ! वृक्षसे लकड़ो दुई और उससे तेरी यह शिविका बनी; तो बठा इसे त्ज्कड़ी कहा जाय या वक्ष ?
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4326)
- **Original**: क्ित्तु महाराज बृक्षपर बैठे हैं' ऐसा कोई नहीं कहता और न कोई तुझे लकड़ीपर बैठा हुआ ही बताता है ! सब ल्त्रेग शिबिकामें वैठा हुआ हो कहते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4327)
- **Original**: हे नृपश्रेष्ट ! रचनासिश्ेषमें स्थित लकाड़ियोंका समूह ही तो जिबिक्ा है। यदि कह उससे कोई धिन्न वस्तु है तो काप्ठकों अलग करके उसे ढूँढ़ों
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4328)
- **Original**: इसी ब्रकार छत्रकी शल्प्रकाओंकों अछगग रखकर छप्नका विचार करो कि वह कहाँ रहता है। यही न्याय तुममें और मुझमें ल्मगू होता है [अर्थात्‌ मेरे और सुम्हारे दारीर भी पहूभूतसे अतिरिक्त और कोई वस्तु नहीं हैं]
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4329)
- **Original**: पुरुष, स्त्री, गौ, अज (बकरा) अभ्र, गज, पक्षी और वक्ष आदि स्त्रैकिक संज्ञाओँका प्रयोग कर्महेतुक झरीरोंमें ही जानना चाहिये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4330)
- **Original**: हे राजन्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4331)
- **Original**: पुरुष (जोच) तो न देवता है, न मनुष्य है, न पशु है और न वृक्ष है। ये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4332)
- **Original**: 154 वस्तु ग़ाजेति यल्ल्जेके यज्व राजभटात्पकप्‌ । तथान्यज्च नृपेत्थ तन्न सत्सकुल्पनामयम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4333)
- **Original**: 99 यत्तु काल्लान्तरेणापि नान्यां संज्ञामुपैति वै । परिणामादिसब्धूतां तद्वस्तु नूप तच्च किम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4334)
- **Original**: 100 त्वे राजा सर्वलोकस्य पितु: पुत्रो रिपो रिपुः । पल्याः पति: पिता सूनो: कि त्वा भूप वदाम्यहम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4335)
- **Original**: 109 त्व॑किमेतच्छिर: कि नु ग्रीवा तब तथोदरम्‌ । किमु पादादिकं लव वा तवैतत्किं महीपते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4336)
- **Original**: 102 सपमस्तावयवेभ्यस्त्वं पृथग्भूय व्यवस्थित: । कोमित्यत्र निपुणो भूत्वा चिन्तय पार्थिव
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4337)
- **Original**: 103 एवं व्यवस्थिते तत्त्व मयाहमिति भाषितुम्‌ । पृथक्करणनिष्पाद्यं शक्यते नृपते कथम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4338)
- **Original**: 104 श्रीविष्णुप्राण [ अआ> एड सब तो कर्मजन्य दारारोंकी आकृतियोंके ही भेंट हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4339)
- **Original**: ल्पेकमें घन, राजा, राजाके सैनिक तथा और भी जोस्जो वस्तुएँ हैं, हे राजन्‌ ! ले परपार्थतः सत्य नहीं हैं, केचक कल्गनापय ही हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4340)
- **Original**: जिस बस्तुकी परिणामादिके कारण होनेवाली कोई संज्ञा काल्मन्तरमें भो नहीं होती, वही परमार्थ- बस्तु है
- **Translation**: 

---

