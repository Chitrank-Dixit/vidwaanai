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

### Verse 1 (Vishnu Puran 0.5161)
- **Original**: 37 आश्रमाणां च सर्वेषामेते सामान्यलक्षणा: । गुणांस्तथापद्धमौँश्ञ॒बिप्रादीनामिमाज्छूणु
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5162)
- **Original**: 38 क्षात्रं कर्म द्विजस्योक्ते बैइ्य कर्म तथाउपदि । राजन्यस्थ च वैश्योक्त शुद्रकर्म न चैतयोः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5163)
- **Original**: 39 आअ08
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5164)
- **Original**: तृतीयअंश
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5165)
- **Original**: #झ#आझआ 985 185 विफ्यमें ऋतुगासी होना ही ब्राह्मणके लिये प्रशंसनीय कर्म है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5166)
- **Original**: क्षत्रि्को उचित है कि ब्राह्मणोंको यथेच्छ दान दे, विविध यज्ञॉंका अनुष्ठान करे और अध्ययन करे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5167)
- **Original**: जास्त्र धारण करना और पृथिवोकी रक्षा करना ही क्षत्रियकी उत्तम आजीविका है; इनमें भी पृथियी-पालन ही उत्कष्टतर है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5168)
- **Original**: पृथिवों-पालनसे ही राजात्त्रेग कृतकृत्प हो जाते हैं, क्योंकि पृथिवीमें होनेवाले यज्ञादि कर्मोंका अदा राजाको मिलता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5169)
- **Original**: जो राजा अपने वर्णघर्मको स्थिर रखता है बह दुष्टोंको दण्ड देने और साधुयनोंका पाछन करनेसे अपने अषीष्ट र्रेकोंको प्राप्त कर लेता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5170)
- **Original**: है नरनाथ! लोकपितामह ब्रह्माजीने वैद्योंको पशु-पालन, वाणिज्य और कृषि--ये जीक्कारूपसे दिये हैं।30
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5171)
- **Original**: अध्ययन, यज्ञ, दान और नित्य- नैमित्तिकादि कर्मोंका अनुष्ठान--ये कर्म उसके लिये भी लिहित हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5172)
- **Original**: शुद्रका कर्तव्य यही है कि द्विजातियोंकी प्रयोजन- सिद्धिके लिये कर्म करें और उसीसे अपना पालन-पोषण करे, अथवा [आपल्काल्में, जब उक्त उपायसे जीविक)ा- निर्वाह न हो सके तो] यस्तुओंके लेने-ग्रेचने अथवा कारीगरीके कामोंसे निर्वाह करे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5173)
- **Original**: अति नम्नता, ज्ौच, निष्कपट स्वामि-सेवा, मज्नहीन यज्ञ, अस्तेय, सत्सड् और ब्राह्मणकी रक्षा करना--ये शूद्रके प्रधान कर्म हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5174)
- **Original**: है राजन्‌ ! शूद्रको भी उचित है कि दान दे, बलिवैश्वदेव अथवा नमस्कार आदि अल्प यज्ञॉका अनुष्ठान करे, पितृश्रादध आदि कर्म करे, अपने आश्रित संग्रह करें और ऋतुकालमें अपनी ही खीसे प्रसम्र करें
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5175)
- **Original**: हे नरेंश्वर
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5176)
- **Original**: इनके अतिरिक्त समस्त प्राणियॉपर दया, सहनज्ञोल्ता, अमानिता, सल्य, शौच, अधिक परिश्रम न करना, मड्जगस्म्रचरण, प्रियवादिता, मैत्री, निष्कामता, अकृपणता और किसीके दोष न देखना--ये समस्त वर्णोके सामान्य गुण हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5177)
- **Original**: सब वर्णोकि सामान्य लक्षण इसी प्रकार हैं। अब इन ब्राह्मणादि चारों वणेकि आपद्धर्म और गृणोंका श्रवण करे।
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5178)
- **Original**: आपत्तिके समय बत्मणको क्षत्रिय और बैदय वर्णोंकी यत्तिका अवलम्यन करना चाहिये तथा क्षत्रियको केवल लैश्यवृत्तिका ही आश्रय लेना चाहिये । ये दोनों झूद्रका कर्म (सेवा आदि) कभी न करें
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5179)
- **Original**: 186 ध्88 रख सखः जअज्रीविष्णपुराण आफ 1 [ अ0 9 सामशथ्यें सति तत्याज्यमुभाभ्यामपि पार्धिव । हे ऱजन्‌ ! इन उपरोक्त वृत्तियोंकों भी सामर्थ्य होनेपर त्याग तदेबापदि कर्तव्य न कुर्यात्कर्मसड्भूरम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5180)
- **Original**: दे; केवल आपत्कालमें हो इनका आश्रय ले, कर्म-सद्भुरता इत्येते कथ्िता राजन्वर्णधर्मा मया तब । (कर्मोंका मेल) न करे
- **Translation**: 

---

