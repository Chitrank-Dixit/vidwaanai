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

### Verse 1 (Vaivtpuran 13.11102)
- **Original**: है >> अपन - नयी-नयी घास चरती हुई आगे बढ़ गयीं और
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11103)
- **Original**: उत्पन्न हुए कदम्बपर चढ़कर उस सर्पके भवनमें यमुनाका विषमिश्रित जल पीने लगीं। मुने ! दारुण
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11104)
- **Original**: बहुत-से नागोंके बीच कूद पड़े। उनके जलमें कालकी चेष्टसे वह विषाक्त जल पीकर कालकूटको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11105)
- **Original**: पड़ते ही उस कुण्डका पानी सौ हाथ ऊपर उठ ज्वालाओंसे संतप्त हो उन गौओंने तत्काल प्राण
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11106)
- **Original**: गया। नारद! यह देख ग्वालबालोंको पहले तो त्याग दिये। झुंड-की-झुंड गौओंको मरी हुई देख
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11107)
- **Original**: हर्ष हुआ, फिर वे बड़े दुःखका अनुभव करने गोपबालक चिन्तासे व्याकुल और भयभीत हो
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11108)
- **Original**: लगे। कालियसर्प मनुष्यकी आकृतिमें आये हुए उठे। उनके मुखपर विषाद छा गया और उन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11109)
- **Original**: श्रीहरिको देखकर क्रोधसे विह्ल हो उठा और सबने आकर मधुसूदन श्रीकृष्णसे यह बात कही।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11110)
- **Original**: तुरंत ही उन्हें निगल गया। जैसे किसी मनुष्यने सारा रहस्य जानकर जगन्नाथ श्रीहरिने उन सब
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11111)
- **Original**: जल्दबाजीमें तपे हुए लोहेको थाम लिया हो वैसे गौओंको जीवित कर दिया। वे गौएँ तत्काल
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11112)
- **Original**: ही ब्रह्मतेजसे उसका कण्ठ और पेट जलने लगा।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11113)
- **Original**: + भ्रीकृष्णजन्मखण्ड « ड95 अऋऋऋ$5########%%%%%%%%%#%#### ##&#####$% कक #####&####%ऊऋ$ कक ऋक़क्क़ह हक वह नाग उद्ठिग्न हो गया और “हाय! हाय! मेरे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11114)
- **Original**: श्रीराधिकाजीके लिये प्रेमके समुद्र हैं। अतः मेरे प्राण निकले जा रहे हैं '--यों कहकर उसने पुन:
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11115)
- **Original**: प्राणणाथका वध न कीजिये। आप विधाताके भी उन्हें उगल दिया। श्रीकृष्णके बज्रोपम अज्भोंको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11116)
- **Original**: विधाता हैं। इसलिये यहाँ मुझे पतिदान दीजिये। चबानेसे उसके सारे दाँत टूट गये और मुँह त्रिनेत्रधारी महादेवके पाँच मुख हैं; ब्रह्माजीके लहूलुहान हो गया। भगवान्‌ उस समय रक्तरपझ्जित
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11117)
- **Original**: चार और शेषनागके सहस्र मुख हैं; कार्तिकेयके मुखवाले कालिय नागके मस्तकपर चढ़ गये।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11118)
- **Original**: भी छः मुख हैं; परंतु ये लोग भी अपने मुख- विश्वम्भरके भारसे आक्रान्त हो कालिय नाग प्राण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11119)
- **Original**: समूहोंद्वारा आपकी स्तुति करनेमें जडवत्‌ हो जाते त्याग देनेको उच्चत हो गया। मुने! उसने रक्त
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11120)
- **Original**: हैं। साक्षात्‌ सरस्वती भी आपका स्तवन करनेमें वमन किया और मूर्च्छित होकर वह गिर पड़ा।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11121)
- **Original**: समर्थ नहीं हैं। सम्पूर्ण वेद, अन्यान्य देवता तथा उसे मूर्च्छित देख सब नाग प्रेमसे विह्लल हो
- **Translation**: 

---

