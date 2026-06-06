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

### Verse 1 (Markende Puran 0.3321)
- **Original**: इसी प्रकार शुम्भने भी जो दिव्य अस्त्र चलाये, उन्हें परमेश्वरीने भयद्भूर हुद्लार शब्दके उच्चारण आदिद्वारा खिलवाड़में ही नष्ट कर डाला
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3322)
- **Original**: तब उस असुरने सैकड़ों बाणोंसे देबीको आच्छादित कर दिया। यह देख क्रोधमें भरी हुई उन देवीने
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3323)
- **Original**: भी बाण मारकर उसका धनुष काट डाला
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3324)
- **Original**: धनुष कट जानेपर फिर दत्यराजने शक्ति हाथमें ली, किन्तु देवीने चक्रसे उसके हाथकी शक्तिकों 3. पा0-हू0। 2. पा>--सा च। 3, पा»-वत ता हन्तुं दैत्या0
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3325)
- **Original**: 4. इसके बाद किसी-किसी प्रतिमें--' अश्चांश् पातयामास रथं सारधिना सह।' इतना अधिक पाठ है। 5. पा0--वेगवान्‌।
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3326)
- **Original**: 2065 4 #4232.2::07 0 5 666. 4.2::000++ 4.62 0*: भी काट गिराय।
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3327)
- **Original**: तत्पश्चात्‌ दैत्योंके स्थागी शुभ्भने सौ चाॉदवाली चमकती हुई ढाल और तलवार झाथरमें लें उस समय देतीपर धाबां क्रिवा
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3328)
- **Original**: उसके आते ही चण्डिकाने अपने धनुषसे छोड़े हुए तंखे बा्णेद्यास उसकी सूर्य-करणोंके समान उज्न्तल द्वाल और तलकास्कों तुरंत काट दिया
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3329)
- **Original**: फिर उस दैल्यक्रे थोड़े और सारथ मारे गये, धनुष तो पहले ही कट चुका था, अब उसने अम्बिकाक्ये मारनेके लिये उद्यत हो भमंकर मुद्गर हाथमें लिया
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3330)
- **Original**: उसे आते देख देवीने अपने तीक्षण बाणंसे उसका मुट्टर भो काट डाला, तिसपर भी बह असुर मुक्क् तातकत् बड़े बैगसे देखीकी ओर जझञपथ
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3331)
- **Original**: उस दैत्यएजने देवीकी छात्रीमें मुक्का माय, तब उन देबीने भी उसकी ऋतीमें एक चाँटा जड़ दिया
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3332)
- **Original**: देवोका भ्रप्पड़ खाकर दैत्यराज शुम्भ पृथ्वीपर गिर पड़ा, किन्तु पुन: सहसा पूर्बबत्‌ उठकर खड़ा हो गया
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3333)
- **Original**: फिर वह उछल्ा और देवीको ऊपर ले जाकर आकशमे खड़ा हो गया; तब चण्डिका आक्राशमें भी बिना किसी आधारके ही झुम्धके साथ युद्ध करने लगीं
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3334)
- **Original**: उस समय दैत्व और चण्डिका आकाशमें एक-दूसेरेसे लड़ने लगे। उनका वह थुद्ध पहले सिद्ध और मुनिर्योक्रो विस्मत्रपें डालनेवाले हुआ
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3335)
- **Original**: फिर अम्ग्रिकाने शुम्भके साथ बहुत्त देसतक युद्ध करनेके पश्चात्‌ उसे उठकर घुमाया और पृथ्बीपर पटक दिया
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3336)
- **Original**: पटके जानेपर पृध्वीपर आनेके बआद वह दुषवत्मा दैत्य पुनः चण्डिकाका वध करनेके लिये उनकी ओर बड़े वेगसे दौड़ा
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3337)
- **Original**: तन समस्त दैत्योंक एजा शुप्भको अपनी ओर आते देख देवीने ब्रिशुलसे डसकों छातों छेदकर डसे पृथ्वीपर गिरा दिया
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3338)
- **Original**: देलीके शूलत्र खारसे खायल होनेपर -खाघ * ड्र5 4
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3339)
- **Original**: .4:2:300%+ 45 4..4.4 74 #+ 4 &6.2.:05$ 58 #
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3340)
- **Original**: 282:5:75+752 528:6+ उड़ उक्षके प्राण पश्ेछ्न उड़ गये और वह समुद्नें, द्वीगों तथा पर्वतॉसह्रित समूच्री पृथ्यीकों कैंपाता हुआ जानेपर सम्पूर्ण जगतू प्रसन्न एवं पूर्ण स्वस्थ हो गया। आकाश स्वच्छ दिखायी देने लगा
- **Translation**: 

---

