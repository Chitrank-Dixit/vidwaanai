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

### Verse 1 (Vishnu Puran 0.5321)
- **Original**: आ* 11 ] तृतीय अंश ज्राहो मुहूर्ते चोत्थाय मनसा मतिमात्रुप । प्रबुद्धश्चिन्तयेद्ध्ममर्थ चाप्यविरोधिनम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5322)
- **Original**: अपीडबा तयो: काममुभयोरपि चिन्तयेत्‌ । दृष्टादृष्टविनाशाय त्रिवर्ण समदर्शिता
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5323)
- **Original**: 6 परित्यजेदर्थकामाौ थर्मपीडाकरौ नृप । धर्ममप्यसुखोद्क॑ लोकविद्विप्रलेच च
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5324)
- **Original**: 7 ततः कल्य॑ समुत्याय कुर्यान्यूत्र नरेश्वर
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5325)
- **Original**: 8 नैक्रत्यामिषुविक्षेपमतीत्याभ्यधिक॑ भुतः । दूरादावसथान्प्ृश्न॑पुरी्ष च बविसर्जयेत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5326)
- **Original**: 9 पादावनेजनोच्छिष्टे प्रक्षिपेन्न गृहाड्रणे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5327)
- **Original**: 10 आत्मच्छारयां तरुच्छायां गोसूर्वाग्न्यनिल्लांस्तथा । गुरुद्विजादीस्तु बुधो नाथिमेहेत्कदालन
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5328)
- **Original**: 11 न कृष्टे सह््यमध्ये वा गोव्रजे जनसंसदि। न वर्त्तनि न नद्यादितीर्थेषु पुरुषर्षभ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5329)
- **Original**: 12 नाप्सु नैवाम्भसस्तीरे इमशाने न समाचरेत्‌ । उत्सर्ग वै पुरीषस्य मृत्नस्य च विसर्जनम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5330)
- **Original**: 13 4 0 मूत्र विपरीतमुखो निशि। ्राज्ञो मूत्रोत्स्ग च पार्थिव
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5331)
- **Original**: 14 तृणैरास्तीर्य बसुधां बस्त्रप्रावृतमस्तक: । ति्ठे्नातिचिरं तत्र नैव किल्निदुदीरयेत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5332)
- **Original**: 15 वल्मीकमूषिकोद्धूतां मृर्दे नान्तर्जलां तथा । शौचावशिष्टां गेहाश्व नाद््याल्केपसम्भवाम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5333)
- **Original**: 16 अपुप्राण्युपपन्नां च हलोत्खातां च पार्थिव । परित्यजेन्मृदो होतास्सकलाइज्ौचकर्मणि
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5334)
- **Original**: 17 एका लिड्डे गुदे तिस्नो दशा वामकरे नृप । हस्तह्ये चर सप्त स्प॒र्मृदबशौचोपपादिका:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5335)
- **Original**: 18 अच्छेनागन्धलेपेन जलेनाबुदबुदेन च। आज्नामेध्च मृदं भूयस्तथाद्य्यात्समाहित:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5336)
- **Original**: 19 निष्पादिताडप्रिशौचस्तु पादावभ्युक्ष्य तै: पुन: । त्रि:पिलेत्सलिलं तेन तथा द्विः परिमार्जयेत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5337)
- **Original**: 20 शीर्षण्यानि ततः ख्ानि मूर्द़ानें च समालभेत्‌ । बाहू नाभि व तोयेन हृदयं चरापि संस्पृझेत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5338)
- **Original**: 21 है नृप ! बुद्धिमान पुरुष स्वस्थ चित्तसे ब्राहममुहूर्तमें 7
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5339)
- **Original**: जगकर अपने धर्म और धर्मायिरोधी अर्थका चिन्तन करे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5340)
- **Original**: तथा जिसमें धर्म और अर्थकी क्षति न हो ऐसे कामका भी चिन्तन करे। इस प्रकार दुष्ट और अदृष्ट अनिष्टकी नियृत्तिके लिये धर्म, अर्थ और काम इस ब्रिवर्गके प्रति समान भाव रखना चाहिये
- **Translation**: 

---

