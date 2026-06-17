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

### Verse 1 (Vaivtpuran 543.13314)
- **Original**: परंतु परिणाममें सुख देनेवाला हो। ऐसा वचन ब्रह्माजीकी प्रार्थनासे ही बे तुम्हारी पुत्रीको ग्रहण
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13315)
- **Original**: दयालु और धर्मशील पुरुष ही अपने भाई- करेंगे। उसे ग्रहण करनेका दूसरा कारण यह है
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13316)
- **Original**: बन्धुओंको समझानेके लिये कहता है। तीसरी कि तुम्हारी कन्याकी तपस्याके अन्तमें उन्होंने उसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13317)
- **Original**: उत्कृष्ट श्रेणेका वचन वह है जो कानोंमें पड़ते ही अपनानेकी प्रतिज्ञा कर ली है। इन दो कारणोंसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13318)
- **Original**: अमृतके समान मधुर प्रतीत हो तथा सर्वदा ही योगिराज शिव विवाह करेंगे। सुखकी प्राप्ति करानेवाला हो। उसमें सारतत्त्व ऋषियोंकी यह बात सुनकर हिमवान्‌ हँसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13319)
- **Original**: सत्य होता है और उसमें सबका हित होता है। और कुछ भयभीत हो अत्यन्त विनयपूर्वक बोले।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13320)
- **Original**: ऐसा वचन सर्वश्रेष्ठ तथा सभीको अभीष्ट होता है। हिमालयने कहा--मैं शिवके पास कोई
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13321)
- **Original**: गिरिराज! इस प्रकार नौतिशास्त्रमें तीन प्रकारके राजोचित सामग्री नहीं देखता। न रहनेके लिये
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13322)
- **Original**: बचनोंका निरूपण किया गया है। अब तुम्हों कहो कोई घर है, न ऐश्वर्य। यहाँतक कि उनके कोई
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13323)
- **Original**: इन तीनोंमेंसे कौन-सा वचन तुमसे कहूँ? तुम्हें स्वजन-बान्धव भी नहीं हैं। जो अत्यन्त निर्लिप्त कैसी बात सुननेकी इच्छा है? देवेश्वर शंकर योगी हो, उसके हाथ कन्या देना उचित नहीं
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13324)
- **Original**: वास्तवमें बाह्य धन-सम्पत्तिसे रहित हैं; क्योंकि है। आप लोग ब्रह्माजीके पुत्र हैं। अतः अपना
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13325)
- **Original**: उनका मन एकमात्र तत्त्वज्ञानके समुद्रमें निमग्र सत्य एवं निश्चित मत प्रकट कीजिये। यदि पिता
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13326)
- **Original**: रहता है। बाह्य धन-सम्पत्ति आपाततः रमणीय कामना, लोभ, भय अथवा मोहके वशीभूत हो
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13327)
- **Original**: जान पड़ती है; परंतु वह बिजलीकी चमककी सुयोग्य पात्रके हाथमें अपनी कन्या नहीं देता
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13328)
- **Original**: भाँति शीघ्र ही नष्ट हो जानेवाली है। नित्यानन्दस्वरूप है तो सौ वर्षोतक नरकमें पड़ा रहता है;* अतः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13329)
- **Original**: स्वात्माराम परमेश्ररकों इस तरहकी सम्पत्तिके मैं स्वेच्छासे शूलपाणिको अपनी कन्या नहीं दूँगा। लिये क्‍या इच्छा होगी? गृहस्थ मनुष्य ऐसे ऋषियो ! इस विषयमें जो उचित कार्य हो; वह
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13330)
- **Original**: पुरुषको अपनी पुत्री देता है, जो राज्य-वैभवसे आप कीजिये। सम्पन्न हो। जिसके मनमें स्त्रीसे द्वेष हो, ऐसे वरको हिमवान्‌की बात सुनकर वेद-वेदाड्रोंके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13331)
- **Original**: कन्या देनेवाला पिता कन्याघाती होता है; परंतु दिद्वान्‌ ब्रह्मपुत्र वसिष्ठ वेदोक्त मत प्रकट करनेके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13332)
- **Original**: कौन कह सकता है कि भगवान्‌ शंकर दुःखी लिये उद्यत हुए। हैं ? क्योंकि धनाध्यक्ष कुबेर भी उनके किड्डूर हैं। *नानुरूपाय पात्राय पिता कन्यां ददाति चेत्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13333)
- **Original**: कामाप्नेभाद्धयान्मोहाच्छताब्द॑ नरक॑ ब्रजेत्‌
- **Translation**: 

---

