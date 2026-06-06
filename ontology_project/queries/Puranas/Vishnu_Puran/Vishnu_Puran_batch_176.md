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

### Verse 1 (Vishnu Puran 0.3501)
- **Original**: इन उपरोक्त पापोके समान और भी सहस्तों पाप-कर्म हैं, उनके फल मनुष्य भिन्न-भिन्न नरकॉमें भोगा करते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3502)
- **Original**: जो लोग अपने वर्णाश्रम-धर्मके विरुर मन, वचन अथवा कर्मसे कोई आचरण करते हैं वे नरकमें गिरते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3503)
- **Original**: अधोमुखनस्कनिवासियोक्र स्वर्ग- लोकमें देलगण दिखायी दिया करते हैं और देवता लोग नीचेके ल्तेकॉमें नास्की जीवोंकों देखते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3504)
- **Original**: पापी लोग नरकभोगके अनन्तर क्रमसे स्थावर, कृमि, जलचर, पक्षी, पशु, मनुष्य, धार्मिक पुरुष, देवगण तथा मुमुक्षु होकर जन्म ग्रहण करते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3505)
- **Original**: हे महाभाग ! मुमुक्षुपर्यक्त इन सबमें दूसरॉंकी अपेक्षा पहले प्राणो [संख्यामें] सहस्लगुण अधिक हैं।
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3506)
- **Original**: जितने जीव स्वर्गमें हैं उतने ही नरकमें हैं, जो पापी पुरुष [अपने पापका] प्रायश्चित्त नहीं करते ये ही नरकमें जाते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3507)
- **Original**: भिन्न-भिन्न पापोंके अनुरूप जो-जो प्रायश्चित्त हैं उन्हीं-उन्हींको महर्षियोंने वेदार्थका स्मरण कस्के बताया है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3508)
- **Original**: हे मैत्रेय ! स्वायम्भुजमनु आदि स्मृतिकारोंने महान्‌ पापोंके लिये महान्‌ और अल्पोंके लिये अल्प प्रायक्षित्तोंकी व्यवस्था की है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3509)
- **Original**: किन्तु जितने भी तपस्पात्मक और कर्मात्मक भ्रायश्चित्त है उन सबमें
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3510)
- **Original**: अ0& ] द्वितोय अंदा 1257 कते पापेउनुतापो वै यस्य पुंसः प्रजायते । ज्रायक्षित्त तु तस्वैक हरिसंस्मरण परम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3511)
- **Original**: 40 न जा आम उमकजरआाककदु सं न,
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3512)
- **Original**: सहद्य: पापक्षबाञ्रः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3513)
- **Original**: 495 वासुदेवे मनो यस्यथ जपहोमार्चनादिषु । तस्थान्तरायो मैश्रेय देवेद्वत्वादिक फलम
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3514)
- **Original**: 43 के जम जोर लसलजम पान नाकपृष्ठगमन॑ पुनरावृत्तिकक्षणम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3515)
- **Original**: तस्पादहरनिंशं विष्णु संस्मसन्‍पुरुषो मुने। न याति नरक॑ मर्त्य: सद्लीणाखिलपातक:ः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3516)
- **Original**: 45 मनः:प्रीतिकर: स्वर्गों नरकस्तद्विपर्ययः । नरकस्वर्गसंज्षे वे पापपुण्ये द्विजोत्तम
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3517)
- **Original**: 46 जार हु.फाय चुसाल भवन जा :खाय सुखायेष्यांगमाय च
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3518)
- **Original**: कोपाय च यतस्तस्माइस्तु वस्त्वात्मक कुत:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3519)
- **Original**: 47 पाक पे शा इ्याजमय- सम प्रीतये भूत्वा पुनर्द:खाय जायते। यतः प्रसादाय चल
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3520)
- **Original**: ड8 0 3:+04-2++0 चकिश्ित्सुखात्मकम्‌ मनसः परिणामोउ्य सुखदुःखादिलक्षण: । पे ड9 ज्ञानात्मकमिद विश्व॑ न ज्ञानादिहमते परम
- **Translation**: 

---

