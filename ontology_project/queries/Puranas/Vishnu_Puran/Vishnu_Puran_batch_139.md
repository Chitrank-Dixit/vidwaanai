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

### Verse 1 (Vishnu Puran 0.2761)
- **Original**: 12 पश्चिमस्यां दिज्चि तथा रजस: पुत्रमच्युतम्‌। केतुपन्त महात्पान॑ राजानं सोउभ्यपेचयत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2762)
- **Original**: 13 तथा हिरण्यरोमाणं पर्जन्यस्य प्रजापते: । उदीच्यां दिशि दुर्द्वँप राजानमभ्यषेचयत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2763)
- **Original**: 14 तैरियं पृथ्चिवी सर्वा सप्तद्वीपा सफ्तना। यथाप्रदेशमद्यापि धर्मत: परिपाल्यते
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2764)
- **Original**: 15 श्रीपराझ्रजी बोले--पूर्वकालमें. महर्षियोंने जब महाराज पृथुको राज्यपदपर अभिषिक्त किया तो लोक-पितामह श्रीत्रह्माजीने भी क्रमसे राज्योंका बैंटनारा किया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2765)
- **Original**: ब्रह्माजीने नक्षत्र, ग्रह, ब्राह्मण, सम्पूर्ण वनस्पति और यज्ञ तथा तप आदिके राज्यपर चद्रमाको नियुक्त किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2766)
- **Original**: इसो प्रकार विश्रवाके पुत्र कुबेस्जीको राजाओंका, वरुणक््रे जलॉका, विष्णुक्रो आदित्योंका और अग्निको वसुगर्णोंका अधिपति बनाया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2767)
- **Original**: दक्षको प्रजापतियोका, इन्द्रको मरुद्गणका तथा प्रह्मादजीको दैत्य और दानवॉका आशधिपत्य दिया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2768)
- **Original**: पितृगणके राज्यपदपर धर्मराज यमको अभिषिक्त किया और सम्पूर्ण गजराजोंका स्वामित्व ऐरावतकों दिया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2769)
- **Original**: गरूड़को पक्षियोंका, इन्द्रक्लो देवताओंका, उच्चैःश्रवाको घोड़ोंका और वृषभको गौओंका अधिपति बनाया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2770)
- **Original**: प्रमु कद्माजीने समस्त मृ्गों (जन्यपशुओं) का राज्य सिंहक्ो दिया और सर्पोंका स्वामी शेषनागकों बनाया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2771)
- **Original**: स्थाक्रोंका स्वामी हिमालयको, मुनिजनॉका कपिलदेवजीक्य और नस तथा दाढ़वाले म॒गगणका राजा व्याप्न (बाघ) को बनाया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2772)
- **Original**: तथा पक्ष (पाकर) को वनस्पतियोंका ग़जा किया। इसी प्रकार तरह्माजीने और-और जातियोंके प्राधान्‍्यकी भी व्यवस्था की
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2773)
- **Original**: इस प्रकार राज्यॉका विभाग करनेके अनन्तर पजापतियोंके स्वामी त्रह्माजीनी सब ओर दिक्पालोॉंकी स्थापना की
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2774)
- **Original**: उन्होंने पूर्व-दिशामें वैराज प्रजापतिके पुत्र राजा सुघन्वाकों दिक्‍्पालपदपर अभिषिक्त किया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2775)
- **Original**: तथा दक्षिण-दिशामें कर्दम प्रजापतिके पुत्र राजा शैखपदकी नियुक्ति की
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2776)
- **Original**: कभी च्युत न होनेवाले रजसपूत्र महात्मा केतुमानकों उन्होंने पश्चिम- दिज्ञा्ें स्थापित किया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2777)
- **Original**: और पर्जन्य प्रजापतिके पुत्र अति दुर्द्धथय राजा हिरण्यरोमाको उत्तर-दिल्ामें अभिषिक्त किया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2778)
- **Original**: वे आजतक सात द्वीप और अनेकों नगरोंसे युक्त इस सम्पूर्ण पृथिवीका अपने-अपने विभागानुसार धर्मपूर्वक पालन करते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2779)
- **Original**: है *---अभनमिशिक असम लीजिलमििलशिमिमिशिशशशकशिकिकिकि........«.' - नमन मिशिकिरिखि ऋककि शनि कल ह...66 श्रीविष्णुपुराण [ अ* 22 एते सर्वे प्रवृत्तस्य स्थितो विष्णोर्महात्मन: । विभूतिभूता राजानो ये चान्ये मुनिसत्तम
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2780)
- **Original**: 16 ये भविष्यन्ति ये भूता: सर्वे भूतेश्वरा द्विज । ते सर्वे सर्वभूतस्य विष्णोरंशा द्विजोत्तम
- **Translation**: 

---

