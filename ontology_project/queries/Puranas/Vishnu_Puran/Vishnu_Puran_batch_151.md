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

### Verse 1 (Vishnu Puran 0.3001)
- **Original**: ले तपस्याके कारण सूख्यकर अत्यन्त कृद्षा हो गये और उनके शरीरकी शिरााएँ. (रक्तवाहिनो नाड़ियाँ) दिखायी देने ऊूगीं। अन्तमें अपने महाप्रस्थान किया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3002)
- **Original**: ! पिता ऋषभदेबजीने बन जाते समय अपना राज्य भरतजोको दिया था; अतः तबसे यह (हिमवर्ष) इस स्मेक्में भारतवर्ष नामसे प्रसिद्ध हुआ
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3003)
- **Original**: भरतजीके सुपति नामक परम धार्मिक पुत्र हुआ। पिता (भरत) ने यज्ञानुष्ठानपूर्वक यथेच्छ राज्य-सुख्त भोगकर उसे समतिको सौंप दिया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3004)
- **Original**: हे मुने ! महाराज भरतने पुत्रकों राज्यलक्ष्मी सौंपकर योगाभ्यासमें तत्पर हो अन्तमें शालआयक्षेत्रमें अपने ग्राण छोड़ दिये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3005)
- **Original**: फिर इन्होंने योगियोंके पवित्र कुलों ब्राह्मणरूपसे जन्म लिया । हे मैत्रेय
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3006)
- **Original**: ! इनका वह चरित्र मैं तुमसे फिर कहुँगा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3007)
- **Original**: तदनन्तर सुमतिके वोर्यसे इन्द्रद्मप्र॒का जन्म हुआ, उससे परमेछ्ठी और परमेष्ठीका पुत्र प्रतिहार हुआ
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3008)
- **Original**: प्रतिहारके प्रतिहर्ता नामसे विख्यात पुत्र उत्पन्न हुआ तथा प्रतिहर्ताका पुत्र भब, भबका उद्रीथ और उद्रीधका पुत्र अति समर्थ प्रस्ताव हुआ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3009)
- **Original**: प्रस्तावका पे पृथुका नक्त और नक्तका पुत्र गय हुआ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3010)
- **Original**: गयके नर और उसके विरद्‌ नामक पुत्र हुआ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3011)
- **Original**: उसका पुत्र महाचवीर्य था, उससे घीमान्‌का जन्य हुआ तथा धोमान्‌का पुत्र महान्त और उसका पुत्र हुआ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3012)
- **Original**: मनस्युका पुत्र त्वष्टा, त्वष्टाका विरज और विरजका पुत्र स्ज हुआ। हे घुने ! सजके पुत्र शातजित्के सौ पुत्र
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3013)
- **Original**: 108 श्रीकिष्णुपुराण [ आः 2 विष्ृग्ज्योतिः प्रधानास्ते यैरिमा बर््धिता: प्रजा: । तैरिदं भारत॑ वर्ष नवभेदमलझ्डूतम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3014)
- **Original**: 41 तेषां यंशप्रसूतैश् भुक्तेये भारती पुरा। कृतत्रेतादिसगेण .युगाख्यामेकसप्ततिम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3015)
- **Original**: 42 एप स्वायम्भुवः सर्गो येनेद पूरितं जगत्‌। उत्पन्न हुए
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3016)
- **Original**: उनमें विध्वग्ज्योति प्रधान था। उन सौ पुत्रोसे यहाँकी पा सहत ह॒त यढ़ गयी। तथ उन्होंने इस भारतवर्षको नौ विभूषित किया। [अर्थात्‌ ये उसी जप पृरडने कृठोतादे शुष्क वशधरोंरे कृतम्रेतादि इकह्तत्तर युगपर्यन्त इस भारतभूमिको भोगा था
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3017)
- **Original**: है झुने ! यही इस वाराहकल्पमें सबसे पहले मन्वन्तराधिप स्वायम्भुव्मनुका बंद है, जिसने उस समय इस सम्पूर्ण खाराहे तु मुने कल्पे पूर्वमन्वच्तराधिप:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3018)
- **Original**: संसारको व्याप्त किया हुआ था
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3019)
- **Original**: इति श्रीविष्णुपुराणे द्वितीयेंडशे प्रथमोष्ध्याय:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3020)
- **Original**: ज++- हऔ --+-- दूसरा अध्याय भूगोलूका खिवरण अमत्रेय उवाच कथितो भवता ब्रह्मन्सर्ग: स्वायप्भुवश्च मे । श्रोतुमिच्छाग्यहं त्कत्त: सकले मण्डल्ल भुषः
- **Translation**: 

---

