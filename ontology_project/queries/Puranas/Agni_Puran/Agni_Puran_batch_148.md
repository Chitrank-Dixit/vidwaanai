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

### Verse 1 (Agni Puran 0.2941)
- **Original**: :7--10
- **Translation**: 

---

### Verse 2 (Agni Puran 0.2942)
- **Original**: सूर्य (गोरखककड़ी), त्रिदश (काला घतूरा), पक्ष (पुत्रजीबक) और पर्वत (अधःपुष्पा)--इन ओषधियोंका अपने शरीरमें लेप करनेसे स्त्री बशमें चाहिये तथा लाजवन्ती आदिको. वाम. पार्श्रमें।
- **Translation**: 

---

### Verse 3 (Agni Puran 0.2943)
- **Original**: होती है। चन्द्रमा ( मेढ़ासिंगी ), इन्द्र: (रुद्रदन्तिका), मयूरशिखाको पैरमें तथा घृतकुमारीको मस्तकपर
- **Translation**: 

---

### Verse 4 (Agni Puran 0.2944)
- **Original**: नाग (मोरशिखा), रुद्र (घीकुआर)--इन ओषधियोंका धारण करना चाहिये। रुद्रजटा, गोरखककडी
- **Translation**: 

---

### Verse 5 (Agni Puran 0.2945)
- **Original**: योनिमें लेप करनेसे स्त्रियाँ वशमें होती हैं। तिथि * ओषधियोंके चतुष्क, क्राम, विशेष संकेत और उपयोग निष्नाद्धित चक्रसे जानने चाहिये-
- **Translation**: 

---

### Verse 6 (Agni Puran 0.2946)
- **Original**: _ सका अधिक नाणकली
- **Translation**: 

---

### Verse 7 (Agni Puran 0.2947)
- **Original**: प्रथम चतुष्क
- **Translation**: 

---

### Verse 8 (Agni Puran 0.2948)
- **Original**: 1 भृक्कराज 2 सहदेयों
- **Translation**: 

---

### Verse 9 (Agni Puran 0.2949)
- **Original**: 3 मयूरशिला
- **Translation**: 

---

### Verse 10 (Agni Puran 0.2950)
- **Original**: 4 पुत्रजीवक . विशेष संकेत हू यहिं 3 (चौग 8 पक्ष 2 नेज घूष-उद्दर्तन द्वितीय चतुष्क
- **Translation**: 

---

### Verse 11 (Agni Puran 0.2951)
- **Original**: 5 अध:पुष्पा 6 रुदत्िका
- **Translation**: 

---

### Verse 12 (Agni Puran 0.2952)
- **Original**: 7 कुमारी < रद्रजय मुनि 7 मतु हृष शिव 11 बसु 8 चतुष्क
- **Translation**: 

---

### Verse 13 (Agni Puran 0.2953)
- **Original**: 9 विष्णुक्रासता 11 लखालुका
- **Translation**: 

---

### Verse 14 (Agni Puran 0.2954)
- **Original**: 12 मोहलता विशेष संकेत दिशा 10 चौथा चतुष्क
- **Translation**: 

---

### Verse 15 (Agni Puran 0.2955)
- **Original**: 13 कृष्ण धत्तूर
- **Translation**: 

---

### Verse 16 (Agni Puran 0.2956)
- **Original**: 14 गोरक्षकर्कटी
- **Translation**: 

---

### Verse 17 (Agni Puran 0.2957)
- **Original**: 15 मेषपृज्री 16 स्नुही विशेष संकेत ऋतु 6 सूर्य 12 चच्मा 1 तिथि 15 दि
- **Translation**: 

---

### Verse 18 (Agni Puran 0.2958)
- **Original**: (सेंहुड); दिक्‌ (अपराजिता), युग (लाजवन्ती) और : बाण (श्वेतार्क)--इन ओषधियोंके द्वारा बनायी - हुई गुटिका (गोली) लोगोंकों वशमें करनेवाली होती है। किसीको वशमें करना हो तो“डसके लिये भक्ष्य, भोज्य और पेय पदार्थमें इसकी एक गोली मिला देनी चाहिये
- **Translation**: 

---

### Verse 19 (Agni Puran 0.2959)
- **Original**: ऋत्विक्‌ (भँगरैया), ग्रह (मोहलता), नेत्र (पुत्रजीबक) तथा पर्वत (अधःपुष्पा)-इन ओषधियोंको मुखमें धारण किया जाय तो इनके प्रभावसे शत्रुओंके चलाये हुए अस्त्र-शस्त्नोंका स्तम्भन हो जाता है--वे घातक आघात नहीं कर पाते। पर्वत (अध:ःपुष्पा), इन्द्र (रुद्रदन्ती), वेद (लाजवन्ती) तथा रन्श्र (मोहलता)--इन ओषधियोंका अपने शरीरमें लेप करके मनुष्य पानीके भीतर निवास कर सकता है। बाण (श्वेतार्क); नेत्र (पुत्रजीवक), मनु (रुद्रदन्ती) तथा रुद्र (घीकुआरि)--इन ओषधियोंसे बनायी हुई बटी भूख, प्यास आदिका निवारण करनेबालोी होती है। त्तीन (सहदेइया), सोलह (भैँगरैया), दिशा (अपराजिता) तथा बाण ( श्वेतार्क)--इन ओषधियोंका लेप करनेसे दुर्भगा स्त्री सुभगा बन जाती है। त्रिशद (काला घतूरा); अक्षि (पुत्रजीवक) तथा दिशा (विष्णुक्रान्ता) और नेत्र ( सहदेइया)-- इन दवाओंका अपने शरीरमें लेप करके मनुष्य सर्पोके साथ क्रीडा कर सकता है। इसी प्रकार त्रिदश (काला धतूरा), अक्षि (पुत्रजीवक), शिव (घृतकुमारी) और सर्प (मयूरशिखा)-से उपलक्षित दवाओंका लेप करनेसे स्त्री सुखपूर्वक प्रसव कर सकती है
- **Translation**: 

---

### Verse 20 (Agni Puran 0.2960)
- **Original**: 13--15
- **Translation**: 

---

