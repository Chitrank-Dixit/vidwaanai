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

### Verse 1 (Vaivtpuran 35.7782)
- **Original**: मैंने जिनके मुखसे धर्म श्रवण किया है, आप कर्म कर डाला, वह हलवाहा भी नहीं कर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 35.7783)
- **Original**: उनके गुरुके भी गुरु हैं। जो कर्मवश ब्राह्मण- सकता। मेरे धर्मात्मा पिताने तो तुम-जैसे नरेशको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 35.7784)
- **Original**: कुलमें उत्पन्न हुआ है, ब्रह्म-चिन्तन करता है उपवास करते देखकर भोजन कराया और तुमने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 35.7785)
- **Original**: और अपने धर्ममें तत्पर एवं शुद्ध है, इसीलिये उन्हें वैसा फल दिया! राजन? तुमने शास्त्रोंका
- **Translation**: 

---

### Verse 5 (Vaivtpuran 35.7786)
- **Original**: वह ब्राह्मण कहलाता है। जो मनन करनेके कारण अध्ययन किया है, तुम प्रतिदिन ब्राह्मणोंको
- **Translation**: 

---

### Verse 6 (Vaivtpuran 35.7787)
- **Original**: नित्य बाहर-भीतर कर्म करता रहता है, सदा विधिपूर्वक दान देते हो और तुम्हारे यशसे सारा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 35.7788)
- **Original**: मौन धारण किये रहता है और समय आनेपर जगत्‌ व्याप्त है। फिर बुढ़ापेमें तुम्हागी अपकीर्ति बोलता है, वह मुनि कहलाता है। जिसकी सुवर्ण कैसे हुई? प्राचीन कालके वन्दीगण ऐसा कहते
- **Translation**: 

---

### Verse 8 (Vaivtpuran 35.7789)
- **Original**: और मिट्टीके ढेलेमें, घर और जंगलमें तथा हैं कि भूतलपर कार्तवीर्यार्जुनके समान दाता,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 35.7790)
- **Original**: कीचड़ और अत्यन्त चिकने चन्दनमें समताकी सर्वश्रेष्ठ, धर्मात्मा, यशस्वी, पुण्यशाली और उत्तम
- **Translation**: 

---

### Verse 10 (Vaivtpuran 35.7791)
- **Original**: भावना है, वह योगी कहा जाता है। जो सम्पूर्ण बुद्धिसम्पन्न न कोई हुआ है और न आगे होगा।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 35.7792)
- **Original**: जीवोंमें समत्व-बुद्धिसे विष्णुकी भावना करता जो पुराणोंमें विख्यात है, उसकी ऐसी अपकीर्ति !
- **Translation**: 

---

### Verse 12 (Vaivtpuran 35.7793)
- **Original**: है और श्रीहरिकी भक्ति करता है, वह हरिभक्त आश्चर्य है। राजन्‌! प्राणियोंके लिये दुर्वाक्य तीखे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 35.7794)
- **Original**: कहा जाता है*। ब्राह्मणॉंका धन तप है। चूँकि अस्त्रसे भी बढ़कर दुस्सह होता है; इसीलिये
- **Translation**: 

---

### Verse 14 (Vaivtpuran 35.7795)
- **Original**: तपस्या कल्पतरु और कामधेनुके समान है, संकट-कालमें भी सत्पुरुषोंके मुखसे दुर्बचन नहीं
- **Translation**: 

---

### Verse 15 (Vaivtpuran 35.7796)
- **Original**: इसीलिये उनकी निरन्तर तपमें इच्छा लगी रहती निकलते। राजेन्द्र ! मैं तुमपर दोषारोपण नहीं कर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 35.7797)
- **Original**: है। रजोगुणी पुरुष कर्मोके रागवश राजसिक कार्य रहा हूँ, बल्कि सच्ची बात कह रहा हूँ; अत:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 35.7798)
- **Original**: करता है और रागान्ध होकर रजोगुणी कार्योँमें इस राजसभामें तुम मुझे उत्तर दो। इस सभामें
- **Translation**: 

---

### Verse 18 (Vaivtpuran 35.7799)
- **Original**: लगा रहता है; इसी कारण वह राजा कहा जाता सूर्य, चन्द्र और मनुके वंशज विद्यमान हैं; अत:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 35.7800)
- **Original**: है। मुने! रागबश मैंने कामधेनुकी याचना की सभामें तुम ठीक-ठीक बतलाओ, जिसे तुम्हारे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 35.7801)
- **Original**: थी; अत: मुझ अनुरागी क्षत्रियका इसमें कौन- पितर और देवगण भी सुनें। साथ ही सत्‌-
- **Translation**: 

---

