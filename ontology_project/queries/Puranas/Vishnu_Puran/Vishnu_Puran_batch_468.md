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

### Verse 1 (Vishnu Puran 0.9341)
- **Original**: वज़पातके समान उनके इन अमड्ल वाक्योंकों सुनकर गोपगण और यश्ञोदा आदि गोपियाँ तुरेत ही काछोदहपर दौड़ आयी
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9342)
- **Original**: 'हाय ! हब! बे कृष्ण कहाँ गये ?' इस प्रकार अत्यन्त व्याकुछतापूर्वक येती हुई गोपियाँ यज्ञोदाके साथ उभ्रतासे गिरती-पड़ती चलें
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9343)
- **Original**: नन्‍दजी तथा अन्यान्य गोपगण और अद्भुत-विक्रमशाली बलरामजी भी कृष्णदर्शानकी लालसासे शीघ्रतापूर्वक यमुना-तटपर आये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9344)
- **Original**: वहाँ आकर उन्होंने देखा कि कृष्णचन्द्र सर्पराजके चंगुल्में फैसे हुए हैं और उसने उन्हें अपने शरीरसे लपेटकर निरुपाय कर दिया है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9345)
- **Original**: हे मुनिसत्तम ! महाभागा यज्ञोदा और नन्दगोप भी पुत्रके मुख़पर टकटकी लगाकर चेष्टाशुन्य हो गये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9346)
- **Original**: अन्य गोपियोंने भी जब कृष्णचन्द्रको इस दशामें देखा तो ये शोकाकुछ होकर येने ऊुगीं और भय तथा व्याकुलताके कारंग गद्ददवाणीसे उनसे प्रीतिपूर्वक कहने छगीं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9347)
- **Original**: गोपियाँ बोलीं--- अब हम सब भी यशोदाके साथ इस सर्पराजके महाकुप्डमें ही डूनी जाती हैं, अब हमें श्रजमें जाना उचित नहीं है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9348)
- **Original**: सूर्यके ब्रिना दिन कैसा ? चन्रमाके बिना रात्रि कैसी ? सॉड़के बिना गौएँ क्‍या ? ऐसे ही कृष्णके बिना त्रजमें भी क्या रखा है 2
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9349)
- **Original**: ] विनाकृता न यास्पाम: कृष्णेनानेन गोकुलम्‌ । अर्य॑ नातिसेव्य च्व वारिहीन यथा सर:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9350)
- **Original**: 28 यत्र॒नेन्दीवरदलइयामकान्तिरय॑ हरिः । तेनापि मातुर्वासेन रतिरस्तीति विस्मय:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9351)
- **Original**: 29 उल्फुल्लपड्टजदलस्पष्टकान्तिविकोचनम्‌ । अपध्यन्त्यो हरि दीना: कर्थ गोष्ठे भविष्यथ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9352)
- **Original**: 30 अत्यन्तमधुरालापहताशोषमनोरथम्‌__
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9353)
- **Original**: न बिना पुण्डरीकाक्ष॑ यास्यामो नन्दगोकुलम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9354)
- **Original**: 39 भोगेनावेष्टितस्यापि सर्पराजस्य पश्यत । स्मितशोभि सुख गोप्य: कृष्णस्यास्मद्विलोकने
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9355)
- **Original**: 32 अऔपराशर उता इति गोपीवच: श्रुत्वा रौहिेणेयो महाजलः । गोपांश्व त्रासविधुरान्विलोक्य स्तिमितेक्षणान्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9356)
- **Original**: 33 नन्‍्द चर दीनमत्यर्थ न्यस्तदृष्टिं सुतानने। पूर्छाकुलां यझ्योदां च कृष्णमाहात्मसंज्ञया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9357)
- **Original**: 34 किमिदं देवदेवेश भावो5य॑ मानुषस्त्वया । व्यज्यतेःत्यन्तमात्मान॑ किमनरन्त न वेत्सि यत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9358)
- **Original**: 35 त्यमेव जगतो नाभिरराणामिव संश्रयः । कर्त्तापहर्त्ता पाता च त्रैल्ौक्य त्व॑ त्रयीपय:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9359)
- **Original**: । 36 सेठ. रुद्राम्िवसुभिरादित्यैर्मस्दश्चिभि: । चिन््यसे त्यमचित्त्यात्मन्‌ समस्तैश्ैव योगिपि:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9360)
- **Original**: 37 जगत्यर्थ जगन्नाथ. भारावत्तरणेच्छया । अबतीर्णोजसि मर्त्येषु तवांशआहमग्रज:
- **Translation**: 

---

