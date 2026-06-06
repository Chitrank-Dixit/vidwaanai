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

### Verse 1 (Vaivtpuran 13.3009)
- **Original**: लीलापूर्बक चलता रहा। अत्यन्त तपोनिष्ठ रहनेपर जन्म लेते ही सूतिकागृहमें स्पष्ट स्वरसे वेदके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.3010)
- **Original**: भी उसका शरीर हृष्ट-पुष्ट बना रहा। उसमें [637 ] सं0 स्र0 वै0 पुराण 6
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.3011)
- **Original**: दुर्बलता नहों आ सकौ। वह नवयौवनसे सम्पन्न
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.3012)
- **Original**: तू मेरे लिये ही अपने बन्धु-बान्धवोंके साथ बनी रही
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.3013)
- **Original**: एक दिन सहसा उसे स्पष्ट आकाशवाणी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.3014)
- **Original**: कालका ग्रास बनेगा; क्योंकि तुने कामभावसे मुझे सुनायी पड़ी--'सुन्दरि! दूसरे जन्ममें भगवान्‌ स्पर्श कर लिया है; अत: अब मैं इस शरीरको श्रीहरि तुम्हारे पति होंगे। ब्रह्मा प्रभृति देवता भी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.3015)
- **Original**: त्याग देती हूँ; देख ले।' बड़ी कठिनतासे जिनकी उपासना कर पाते हैं, देवी वेदवतीने इस प्रकार कहकर वहाँ उन्हीं परम प्रभुको स्वामी बनानेका सौभाग्य तुम्हें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.3016)
- **Original**: योगद्धार अपने शरीरका त्याग कर दिया। तब प्राप्त होगा।' रावणने उसका मृत शरीर गड्भामें डाल दिया और मुने! यह आकाशबाणी सुननेके पश्चात्‌ रुष्ट
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.3017)
- **Original**: मनमें इस प्रकार चिन्ता करते हुए घरकी ओर हो वह कन्या गन्धमादन पर्वतपर चली गयी और
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.3018)
- **Original**: प्रयाण किया-'अहो! मैंने यह कैसी अद्भुत वहाँ पहलेसे भी अधिक कठोर तप करने लगी।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.3019)
- **Original**: घटना देखी? यह मैंने क्या कर डाला ?'--इस वहाँ चिरकालतक तप करके विश्वस्त हो वहीं
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.3020)
- **Original**: प्रकार विचार कर अपने कुकृत्य और उस देवीके रहने लगी। एक दिन वहाँ उसे अपने सामने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.3021)
- **Original**: देहत्यागको याद करके रावण बहुत विषाद दुर्निवार रावण दिखायी पड़ा। वेदवतीने अतिथि-
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.3022)
- **Original**: करने लगा। मुने ! वह देवी साध्वी बेदबती दूसरे धर्मके अनुसार पाद्य, परम स्वादिष्ट फल और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.3023)
- **Original**: जन्ममें जनककी कन्या हुई और उस देवीका शीतल जल देकर उसका सत्कार किया। रावण
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.3024)
- **Original**: नाम सीता पड़ा; जिसके कारण रावणको बड़ा पापिष्ठ था। फल खानेके पश्चात्‌ बह
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.3025)
- **Original**: मृत्युका मुख देखना पड़ा था। वेदवती बड़ी वेदवतीके समीप जा बैठा और पूछने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.3026)
- **Original**: तपस्विनीं थी। पूर्वजन्मकी तपस्याके प्रभावसे लगा--' कल्याणी ! तुम कौन हो और क्‍यों यहाँ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.3027)
- **Original**: स्वयं भगवान्‌ श्रीराम उसके पति हुए। ये राम उहरी हुई हो ?' वह देवी परम सुन्दरी थी। उस
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.3028)
- **Original**: साक्षात्‌ परिपूर्णतम श्रीहरि हैं। देवी वेदवतीने साध्यी कन्याके मुखपर मन्द मुस्कानकी छटा
- **Translation**: 

---

