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

### Verse 1 (Vaivtpuran 44.8357)
- **Original**: अतिथिरूपसे प्राप्त हुए हैं, इससे मेरा जन्म सफल बस्त्र, शुक्ल यज्ञोपवीत, दण्ड, छत्र और ललाटपर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 44.8358)
- **Original**: और जीवन धन्य हो गया। कृपासागर परिपूर्णतम उज्ज्वल तिलक धारण किये हुए था। उसके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 44.8359)
- **Original**: श्रीकृष्ण लोगोंके उद्धारके लिये पुण्यक्षेत्र भारतमें गलेमें तुलसीकी माला पड़ी थी। उसका रूप
- **Translation**: 

---

### Verse 4 (Vaivtpuran 44.8360)
- **Original**: अपनी कलासे अवतीर्ण हुए हैं। जिसने अतिथिका परम मनोहर था, मुखपर मन्‍्द मुसकान थी और
- **Translation**: 

---

### Verse 5 (Vaivtpuran 44.8361)
- **Original**: आदर-सत्कार किया है, उसने मानो सम्पूर्ण वह रत्नोंक बाजूबंद, कद्डूण और रत्रमालासे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 44.8362)
- **Original**: देवताओंकी पूजा कर ली; क्योंकि जिसपर विभूषित था। पैरोंमें रत्नोंक नूपुर थे। मस्तकपर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 44.8363)
- **Original**: अतिथि प्रसन्न हो जाता है, उसपर स्वयं श्रीहरि बहुमूल्य रल्नोंक मुकुटकी उज्ज्वल छटा थी और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 44.8364)
- **Original**: प्रसन्न हो जाते हैं। समस्त तीथ्थोंमें स्नान करनेसे, कपोलोंपर रत्ननिर्मित दो कुण्डल झलमला रहे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 44.8365)
- **Original**: सर्वस्व दान करनेसे, सभी प्रकारके ब्रतोपवाससे, थे, जिससे उसकी विशेष शोभा हो रही थी।' सम्पूर्ण बज्ञोंमें दीक्षा ग्रहण करनेसे, सभी प्रकारकी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 44.8366)
- **Original**: 390 * संक्षिप्त ब्रह्मवैवर्तपुराण * 304 4 3 3 3
- **Translation**: 

---

### Verse 11 (Vaivtpuran 44.8367)
- **Original**: 3) 0) 2) 000 ]070)0+404:0.09+94..]) तपस्याओंसे और नित्य-नैमित्तिकादि विविध
- **Translation**: 

---

### Verse 12 (Vaivtpuran 44.8368)
- **Original**: हुए समस्त पदार्थोंको ज्ञानदीपकरूपी नेत्रसे दिखलाता कर्मानुष्ठानोंस जो फल प्राप्त होता है-वह
- **Translation**: 

---

### Verse 13 (Vaivtpuran 44.8369)
- **Original**: है, उससे बढ़कर बान्धव कौन है? गुरुद्वारा दिये अतिथिसेवाकी सोलहवीं कलाकी समानता नहीं
- **Translation**: 

---

### Verse 14 (Vaivtpuran 44.8370)
- **Original**: गये मन्त्र और तपसे अभीष्ट सुख, सर्वज्ञता और कर सकता। अतिथि जिसके गृहसे निराश एवं
- **Translation**: 

---

### Verse 15 (Vaivtpuran 44.8371)
- **Original**: समस्त सिद्धियोंकी प्राप्ति होती है; अतः गुरुसे रुष्ट होकर चला जाता है, उसका पुण्य निश्चय
- **Translation**: 

---

### Verse 16 (Vaivtpuran 44.8372)
- **Original**: बढ़कर बान्धव दूसरा कौन है? गुरुद्वारा दी गयी ही नष्ट हो जाता है। विद्याके बलसे मनुष्य सर्वत्र समयपर विजयी श्रीनारायण कहते हैं--नारद! शंकरके वचन
- **Translation**: 

---

### Verse 17 (Vaivtpuran 44.8373)
- **Original**: होता है, इसलिये जगत्‌में गुरुसे बढ़कर पूज्य और सुनकर जगत्पति स्वयं श्रीहरि संतुष्ट हो गये और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 44.8374)
- **Original**: उनसे अधिक प्रिय बन्धु कौन हो सकता है? जो मेघके समान गम्भीर वाणीद्वारा उनसे बोले।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 44.8375)
- **Original**: मूर्ख विद्यामद अथवा धनमदसे अंधा होकर विष्णुने कहा--शिवजी! आप लोगोंके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 44.8376)
- **Original**: गुरुकी सेवा नहीं करता, वह ब्रह्महत्या आदि कोलाहलको जानकर कृष्णभक्त परशुरामकी रक्षा
- **Translation**: 

---

