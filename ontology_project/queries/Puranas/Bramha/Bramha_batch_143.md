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

### Verse 1 (Bramha 0.2841)
- **Original**: इस प्रकार भगवानको प्रसन्न करके साष्टाड़
- **Translation**: 

---

### Verse 2 (Bramha 0.2842)
- **Original**: 'शड्ख, चक्र और गदा धारण करनेवाले, दण्डवत्‌ करे। तत्पश्चात्‌ पुष्प, वस्त्र और चन्दन
- **Translation**: 

---

### Verse 3 (Bramha 0.2843)
- **Original**: सर्वव्यापी, जगन्नाथ एवं आदि-अन्तसे रहित आदिसे भक्तिपूर्वक गुरुकी पूजा करे। क्योंकि गुरु
- **Translation**: 

---

### Verse 4 (Bramha 0.2844)
- **Original**: भगवान्‌ पुरुषोत्तम मुझपर प्रसन्न हों।' और भगवानूमें कोई अन्तर नहीं है। तदनन्तर
- **Translation**: 

---

### Verse 5 (Bramha 0.2845)
- **Original**: यों कहकर ब्राह्मणोंकी तीन यार प्रदक्षिणा करे। भाँति-भौतिके पुष्पोंसे भगवान्‌के ऊपर एक सुन्दर
- **Translation**: 

---

### Verse 6 (Bramha 0.2846)
- **Original**: इसके बाद मस्तक झुकाकर आचार्यको भक्तिपूर्वक पुष्प-मण्डप बनाये, फिर श्रद्धा और एकाग्रतापूर्वक
- **Translation**: 

---

### Verse 7 (Bramha 0.2847)
- **Original**: प्रणाम करे । प्रणामके पश्चात्‌ उन्हें विदा करे। फिर रात्रिपें जागरण करे। भगवान्‌ बासुदेवकी कथा और
- **Translation**: 

---

### Verse 8 (Bramha 0.2848)
- **Original**: अन्य ब्राह्मणोंको भी गाँवकी सीमातक पहुँचा दे। गीतकी व्यवस्था रखे। इस प्रकार विद्वान्‌ पुरुष अन्तमें सबको नमस्कार करके लौट आये। फिर ध्यान, पाठ और स्तुति करते हुए रात्रि व्यतीत करे।
- **Translation**: 

---

### Verse 9 (Bramha 0.2849)
- **Original**: स्वजनों, बान्धवों, अन्य उपासकों, दीनों, भिखमंगों तत्पश्चात्‌ निर्मल प्रभात होनेपर द्वादशीको बारह
- **Translation**: 

---

### Verse 10 (Bramha 0.2850)
- **Original**: और अन्न चाहनेवाले अन्य लोगोंको भोजन कराकर ब्राह्मणोंको निमन्त्रित करे। वे ब्राह्मण स्नातक, वेदोंमें
- **Translation**: 

---

### Verse 11 (Bramha 0.2851)
- **Original**: फिर मौन होकर भोजन करे । ऐसा करके समस्त नर- पारंगत, इतिहास-पुराणके ज्ञता, श्रोत्रिय और जितेन्द्रिय
- **Translation**: 

---

### Verse 12 (Bramha 0.2852)
- **Original**: नारी एक हजार अश्वमेध तथा सी राजसूय-यज्ञोंका होने चाहिये। इसके बाद स्वयं भी विधिपूर्वक स्नान ' फल पाते हैं और ऐसा करनेवाला बुद्धिमान्‌ पुरुष करके धुला हुआ वस्त्र पहने और इन्द्रियसंयमपूर्वक
- **Translation**: 

---

### Verse 13 (Bramha 0.2853)
- **Original**: सूर्यके समान तेजस्वी और इच्छानुसार चलनेवाले पहले भगवान्‌को स्नान कराकर उनकी पूजा करें।
- **Translation**: 

---

### Verse 14 (Bramha 0.2854)
- **Original**: विमानके द्वारा भगवान्‌ विष्णुके लोकमें जाता है। " किले मर कहते
- **Translation**: 

---

### Verse 15 (Bramha 0.2855)
- **Original**: +तीर्थोंक भेद, वामनका बलिसे भूमिदान-ग्रहण * 139 तीर्थोके भेद, वामनका बलिसे भूमिदान-ग्रहण तथा गड़ाजीका महेश्वरकी जटामें गमन ब्रह्मजी कहते हैं--ट्विजवरो! सब तीर्थों और
- **Translation**: 

---

### Verse 16 (Bramha 0.2856)
- **Original**: वह तीनों लोकोंमें विख्यात है। बेटा! वह क्षेत्रोंमे जो जप, होम, त्रत और तपस्या तथा
- **Translation**: 

---

### Verse 17 (Bramha 0.2857)
- **Original**: कर्मभूमि है, इसलिये उसे तीर्थ कहते हैं। पहले दानके फल प्राप्त होते हैं, उनमेंसे कोई ऐसा नहीं
- **Translation**: 

---

### Verse 18 (Bramha 0.2858)
- **Original**: मैंने तुम्हें जो बताये हैं, वे सब तीर्थ भारतवर्षमें दिखायी देता, जो पुरुषोत्तमक्षेत्रमें रहनेके फलकी
- **Translation**: 

---

### Verse 19 (Bramha 0.2859)
- **Original**: ही हैं। हिमालय और विन्ध्यपर्वतके बीचमें छः समानता कर सके। अब बारंबार अधिक कहनेकी
- **Translation**: 

---

### Verse 20 (Bramha 0.2860)
- **Original**: ऐसी नदियाँ हैं, जिनका प्राकट्य ब्रह्मा, विष्णु तथा क्या आवश्यकता, वह पुरुषोत्तमक्षेत्र सबसे महान्‌
- **Translation**: 

---

