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

### Verse 1 (Bramha 0.3641)
- **Original**: किसी तरह अम्बिका-वनमें पहुँचा दो। उसके हो गये हैं। वे बहुत बड़ी सेना साथ लेकर शिकार
- **Translation**: 

---

### Verse 2 (Bramha 0.3642)
- **Original**: भीतर प्रवेश करते ही यह राजा स्त्री हो जायगा। खेलनेके लिये बनमें गये। बहाँ उनकी बुद्धिमें
- **Translation**: 

---

### Verse 3 (Bramha 0.3643)
- **Original**: भद्रे ! यह काम तुम्हीं कर सकती हो। मेरे लिये कुछ दूसरा ही निश्चय हुआ। उन्होंने अमात्योंसे
- **Translation**: 

---

### Verse 4 (Bramha 0.3644)
- **Original**: यह उचित न होगा।' कहा--'आप सब लोग मेरे पुन्रद्वाता पालित, यक्षिणीने पूछा--नाथ ! अम्बिका-वन तो नगरमें चले जायेँ। देश, कोश, बल, राज्य तथा
- **Translation**: 

---

### Verse 5 (Bramha 0.3645)
- **Original**: बड़ा सुन्दर है। तुम उसमें क्‍यों नहीं जा सकते ? मेरे पुत्रकी भी रक्षा करें। महर्षि वसि्ठ भी हमारे
- **Translation**: 

---

### Verse 6 (Bramha 0.3646)
- **Original**: यदि तुम भी चले जाओ तो क्‍या दोष होगा ? यह लिये पिताके समान हैं। ये भी अग्निहोत्रकी
- **Translation**: 

---

### Verse 7 (Bramha 0.3647)
- **Original**: हमें ठीक-ठीक बताओ। अग्नियोंको लेकर मेरी पत्नियोंके साथ लौट, यक्षने कहा--एक समय पार्वतीने एकान्त जायें। मैं अभी इस वनमें ही निवास करूँगा।' [बैठे हुए भगवान्‌ शंकरसे कहा--देवेश्वर ! 'बहुत अच्छा” कहकर सब लोग चले गये और , स्त्रियॉंकी यह स्वाभाविक इच्छा होती है कि राजा धीरे-धीरे रत्नमय हिमालय पर्वतपर जाकर
- **Translation**: 

---

### Verse 8 (Bramha 0.3648)
- **Original**: उनकी रतिक्रीड़ा सदा गुप्त रहे। इसलिये मुझे ऐसा वहीं निवास करने लगे। एक दिन उन्होंने उस
- **Translation**: 

---

### Verse 9 (Bramha 0.3649)
- **Original**: नियत स्थान दीजिये, जो आपकी आज्ञासे सुरक्षित पर्वतपर एक गुफा देखी, जो नाना प्रकारके रत्नोंसे
- **Translation**: 

---

### Verse 10 (Bramha 0.3650)
- **Original**: हों। मैं स्थान वही चाहती हूँ, जो उमावनके विचित्र शोभा पा रही थी। उस गुफामें यक्षोंका
- **Translation**: 

---

### Verse 11 (Bramha 0.3651)
- **Original**: नामसे प्रसिद्ध है। उसमें आप, गणेश, कार्तिकेय राजा समन्‍्यु रहता था। उसके साथ उसकी
- **Translation**: 

---

### Verse 12 (Bramha 0.3652)
- **Original**: और नन्दीके सिवा जो कोई भी प्रवेश करे, बह पतिब्रता पत्नी समा भी रहा करती थी। उस समय
- **Translation**: 

---

### Verse 13 (Bramha 0.3653)
- **Original**: स्त्री हो जाय।' शंकरजीने प्रसन्न होकर कहा--' ऐसा वह यक्ष मृगरूप धारण करके अपनी पत्नीके साथ
- **Translation**: 

---

### Verse 14 (Bramha 0.3654)
- **Original**: हो हो।' इसलिये उमाके उस बनमें मुझे नहीं विचर रहा था। भाँति-भाँतिके रत्नोंसे चित्रित,
- **Translation**: 

---

### Verse 15 (Bramha 0.3655)
- **Original**: जाना चाहिये। उसका वह विशाल गृह सूना पड़ा था। अत:
- **Translation**: 

---

### Verse 16 (Bramha 0.3656)
- **Original**: अपने स्वामीका यह वचन सुनकर इच्छानुसार राजा अपनी भारी सेनाके साथ वहीं ठहर गये।। रूप धारण करनेवाली वह यक्षिणी विशाल नेत्रोंवाली यह यक्ष अधर्मके कोपसे पत्नीके साथ मृगरूप
- **Translation**: 

---

### Verse 17 (Bramha 0.3657)
- **Original**: मृगी बनकर राजाके सामने आयी। यक्ष वहाँ ठहर धारण करके रहता था। उसने सोचा-*इस राजाने
- **Translation**: 

---

### Verse 18 (Bramha 0.3658)
- **Original**: गया। राजाने मृगीकों देखा। मृगयामें तो उनकी मेरा घर छीन लिया। मैं इसे जीत सकता नहीं
- **Translation**: 

---

### Verse 19 (Bramha 0.3659)
- **Original**: आसक्ति थी ही। मृगीपर दृष्टि पड़ते ही वे अकेले और यह माँगनेपर देगा नहीं। अब क्या करूँ ?'
- **Translation**: 

---

### Verse 20 (Bramha 0.3660)
- **Original**: घोड़ेपर जा बैठे और उसका पीछा करने लगे। इसी चिन्तामें पड़कर वह मृगीरूपधारिणो अपनी
- **Translation**: 

---

