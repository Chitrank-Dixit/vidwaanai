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

### Verse 1 (Vishnu Puran 0.10981)
- **Original**: तदनन्तर इन्द्र भों ऐरबतपर चढ़कर देवलोंकव्त्रें गये तथा भगवान्‌ कृष्णचन्द्र सब द्रास्कावासियोंके देखते-देखते [ नरकासुरको मारने ] चले गये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10982)
- **Original**: हे द्विजोत्तम ! प्राग्ज्योतिषपुरके चारों ओर पृथिवी सौ योजनतक मुर दैत्यके बनाये हुए छुरेकी थाराके समान अति तीक्ष्ण पाशोंसे घिरी हुई थी
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10983)
- **Original**: भगवानने उन पाश्ञॉंको सुदर्शनचक्र फेंककर काट डाल्छा; फिर मुर दैत्य भी सामना करलनेके लिये उठा ठब श्रीकेशवने उसे भी मार डाल्ज
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10984)
- **Original**: तदनन्तर श्रीहरिने मुर्के साथ हजार पुत्रोंको भी अपने चक्रकों घाररूप अभ्िमें पतंगके समान भस्म कर दिया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10985)
- **Original**: है ट्विज ! इस प्रकार मतिमान्‌ भगवानने मुर, हयग्रीय एवं पक्षजन आदि दैत्योंकों मारकर बड़ी झन्नतासे प्राग्ज्योतिषपुरमें प्रवेश किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10986)
- **Original**: जहाँ पहुँचकर भगवानक़ा अधिक सेनाबाले नरकासुरसे युद्ध हुआ जिसमें श्रीगोविन्दने उसके सहस्रों दैत्योंको मार डाला
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10987)
- **Original**: दैत्यटरूफा दरून करनेवाले महाबल्यात्‌ भगवान्‌ चक्रपाणिने शख्तास्त्रको वर्षा करते हुए भूमिपुत्र नरकासुस्के सुदर्शनचक्र फेंककर दो डुकड़े कर दिये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10988)
- **Original**: नरब्यसुर्के मरते ही पृथिवी अदितिके कुण्डल क्लेकर उपस्थित हुई और श्रोजगन्नाथसे कहने लगो
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10989)
- **Original**: आ0 29 ] 387 पृथ्व्युवाच यदाहमुद्धता नाथ त्वया सूकरमूर्तिना । त्वत्स्पर्शसम्भव: पुत्रस्तदाय॑मव्यजायत
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10990)
- **Original**: 23 सो5यं त्वयैव दत्तो मे त्ववैब विनिपातितः । गृहाण कुण्डले चेमे पालयास्य च सन्ततिम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10991)
- **Original**: 24 भारावतरणार्थाय ममैव भगवानिप्रम्‌ । अंशेन लोकमायातः प्रसादसुमुखः प्रभो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10992)
- **Original**: 25 त्वें कर्ता च विकर्ता च संहर्ता प्रभवो5प्यय: । जगतां त्व॑ जगद्गभुप: स्तृयतेउच्युत कि तब
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10993)
- **Original**: 26 व्याप्तिव्याप्प॑ क्रिया कर्ता कार्य च भगवान्यथा । सर्वभूतात्मभूतस्य स्तूयते तब कि तथा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10994)
- **Original**: 27 परमात्मा च भूतात्मा त्वमात्मा चाव्ययो भवान्‌ । यथा तथा स्तुतिर्नाथ किमर्थ ते प्रवर्तते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10995)
- **Original**: 28 अ्रसीद सर्वभूतात्मन्नरकेण तु यत्कृतम्‌। तत्क्षम्यतामदोषाय ल्वत्सुतस्त्वन्निपातित:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10996)
- **Original**: 29 श्रीपताश्र उवाच तथेति चोक्‍त्या धरणी भगवान्भूतभावन: । रत्लानि नरकावासाज्ञआह मुनिसत्तम
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10997)
- **Original**: 30 कन्यापुरे स कन्यानां षोडशातुलबिक्रम: । झताधिकानि ददृहो सहस्राणि महामुने
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10998)
- **Original**: 31 चतुर्देष्टान्गजां क्षाग्रयान्‌ घदसहसां शव दृष्टवान्‌ । काम्बोजानां तथाश्चानां नियुतान्येकविंशतिम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10999)
- **Original**: 32 ता: कन्यास्तांस्तथा नागांस्तानश्रान द्वारका पुरीम्‌ प्रापयामास गोकिन्दस्सद्यों नरककिड्भरैः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11000)
- **Original**: 33 ददृशे वारुणं छत्र॑ तथैव मणिपर्वतम्‌ । आरोपयामास॒ हरि्गरुडे. पतगेश्वरे
- **Translation**: 

---

