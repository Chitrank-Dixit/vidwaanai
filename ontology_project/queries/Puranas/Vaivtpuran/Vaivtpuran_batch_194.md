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

### Verse 1 (Vaivtpuran 13.6610)
- **Original**: अद्भुतेजसे आच्छादित न होकर जगतकों प्रकाशित भय दूर हो जाना चाहिये। मेरे रहते आपको
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.6611)
- **Original**: कर रहे हो। शम्भुनन्दन! तुम तो जगद्व्यापी भय कैसा? यह कर्मभोग दुर्निवार्य है, इसे कौन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.6612)
- **Original**: विष्णु हो, अत: इन कृत्तिकाओंके व्याप्य नहीं हटा सकता है। इसी बीच सेनापति नन्दिकेश्वर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.6613)
- **Original**: हो, जैसे आकाश किसीका व्याप्य नहीं है, बल्कि भी वहाँ कार्तिकेयके समक्ष उपस्थित हुए और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.6614)
- **Original**: वह स्वयं ही सबका व्यापक है। तुम विषयोंसे कृत्तिकाओंसे बोले। निर्लिप्त योगीन्द्र हो तथा विश्वेके आधार और नन्दिकेश्वरने कहा-- भ्राता ! संहारकर्ता सुरश्रेष्ठ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.6615)
- **Original**: परमेश्वर हो। ऐसी दशामें कृत्तिकाओंके भवनमें शंकर और माता पार्वतीद्वारा भेजे गये शुभ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.6616)
- **Original**: तुम सर्वेश्वरका निवास होना उसी प्रकार सम्भव समाचारको मुझसे श्रवण करो। कैलासपर्वतपर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.6617)
- **Original**: नहीं है, जैसे क्षुद्र गौरैयाके उदरमें गरुड़का रहना गणेशके माड्भनलिक जन्मोत्सवके अवसरपर सभामें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.6618)
- **Original**: असम्भव है। तुम भक्तोंके लिये मूर्तिमान्‌ अनुग्रह ब्रह्मा, विष्णु और शिव आदि सभी देवता
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.6619)
- **Original**: तथा गुणों और तेजोंकी राशि हो। देवगण तुम्हें उपस्थित हैं। वहाँ गिरिराजकिशोरीने जगत्‌का
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.6620)
- **Original**: उसी तरह नहीं जानते जैसे योगहीन पुरुष ज्ञानसे पालन करनेवाले विष्णुकों सम्बोधित करके उनसे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.6621)
- **Original**: अनभिज्ञ होता है। जैसे मोहितचित्तवाले भक्तिहीन तुम्हारे अन्वेषणके लिये कहा। तब बविष्णुने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.6622)
- **Original**: मनुष्योंको हरिकी उत्कृष्ट भक्तिका ज्ञान नहीं होता, तुम्हारी प्राप्तिक निमित्त क्रमश: उन सभी देवोंसे
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.6623)
- **Original**: उसी तरह ये कृत्तिकाएँ तुम्हें कैसे जान सकती पूछा। उनमेंसे प्रत्येकने यथोचित उत्तर भी दिया।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.6624)
- **Original**: हैं; क्योंकि तुम अनिर्वचनीय हो। भ्राता! जो लोग उन्हींमें धर्म-अधर्मके साक्षी धर्म आदि सभी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.6625)
- **Original**: जिसके गुणको नहीं जानते, वे उसका अनादर देवताओंने परमेश्वरको तुम्हारे यहाँ कृत्तिकाओंके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.6626)
- **Original**: ही करते हैं; जैसे मेढक एक साथ रहनेवाले भवनमें रहनेकी सूचना दी। प्राचीनकालमें शिब-
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.6627)
- **Original**: कमलोंका आदर नहीं करते। पार्वतीकी जो एकान्त क्रौड़ा हुई थी, उसमें। कार्तिकेयने कहा-- भ्राता ! जो भूत, भविष्यतू देवताओंद्वारा देखे जानेपर शम्भुका शुक्र भूतलपर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.6628)
- **Original**: बर्तमान-तीनों कालोंका ज्ञान है, वह सब मुझे गिर पड़ा था। भूमिने उस शुक्रको अग्रिमें और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.6629)
- **Original**: ज्ञात है। तुम भी तो ज्ञानी हो; क्योंकि मृत्युझ्यके अग्निने उसे सरकंडोंके वनमें फैक दिया। वहाँसे
- **Translation**: 

---

