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

### Verse 1 (Vishnu Puran 0.3041)
- **Original**: 15 प्रेरेश्नतुर्दिश तत्तु नवसाहस्नविस्तृतम्‌। इलावूत महाभाग चत्वारश्नात्र पर्वता:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3042)
- **Original**: 16 किष्कम्पा रचिता मेरोयोजनायुतमुच्छिता:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3043)
- **Original**: 17 पूर्वेण मन्दरों नाम दक्षिणे गन्धमादन: । विपुलः पश्लिमे पार्श्वे सुपार्श्रश्षोत्तरे स्मृत:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3044)
- **Original**: 18 कदम्बस्तेषु जम्बूश्ष पिप्पलो वट एव च। एकादहशझतायामाः पादपा गिरिकेतवः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3045)
- **Original**: 19 जम्बूद्ीपस्प सा जम्बूर्नामहेतुर्महामुने । महागजप्रमाणानि जम्ब्वास्तस्था: फलानि वे । पतन्ति भूभृत: पृष्ठे शीर्यमाणानि सर्वत:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3046)
- **Original**: 20 रसेन तेषां प्रस्याता तत्र जाम्बूनदीति वे । सरित्यवर्तती च्रापि पीयते तप्निवासिभि:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3047)
- **Original**: 21 न स्वेदो न च दोर्गःथ्यं न जरा नेद्धियक्षय: । तत्पानात्स्कच्छमनसां जनानों तत्र जायते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3048)
- **Original**: 22 तीरपृत्तदर्स प्राप्प सुखवायुविज्ञोषिता । जाम्बूनदाख्यं भवति सुबर्ण सिद्धभूषणम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3049)
- **Original**: 23 भ्वाक्च॑ पूर्वतो मेरोः केतुमाल; चर पश्चिमे । वर्षे द्वे तु मुनिश्रेष्ठ तयोर्मध्यमिलावृतः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3050)
- **Original**: 24 यह पर्वत इस पृथिबीरूप कमलकी कर्णिका (कोइ) के समान है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3051)
- **Original**: इसके दक्षिणमें हिसवान, हेमकुट और निषध तथा उत्तरमें नील, श्वेत और श्रृत्री नामक वर्षपर्वत हैं (जो भिन्न-भिन्न वर्षोका विभाग करते हैं]
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3052)
- **Original**: उनमें बीचके दो पर्वत [निषध और नील] एक-एक लाख योजनतक फैले हुए हैं, उनसे दूसरे-दूसरे दस-दस हजार योजन कम हैं। [अर्थात्‌ हेमकूट और अत नब्बे-नब्बे हजार योजन तथा हिमवान्‌ और श्री अस्पी-अस्सी सहस्र योजनतक फैले हुए हैं।] वे सभी दो-दो सहस्र योजन ऊँचे और इतने ही चौड़े हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3053)
- **Original**: हे ट्विज ! मेरुपर्वतके दक्षिणकी ओर पहत्ख भारतवर्ष है तथा दूसरा किम्पुरुषवर्थ और तीसरा हरिषर्ष है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3054)
- **Original**: उत्तरकी ओर प्रथम रम्यक, फिर हिरण्मय और तदनन्तर उत्तरकुरूबर्ष है जो ([ट्वीपमण्डलको सोमापर होनेके कारण] भारतवर्षके समान [घनुषाकार] है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3055)
- **Original**: है ट्विजश्रेष्ठ ! इनमेंसे प्रत्येकका विस्तार नौ-नौ हजार योजन है तथा इन सबके बीचमें इल्म्रयतयर्ष है जिसमें सुवर्णमय सुमेरुपर्वत खड़ा हुआ है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3056)
- **Original**: हे महाभाग ! यह इल्त्रवृतवर्ष सुभेरुके चारों ओर नौ हजार योजनतक फैत्ता हुआ है। इसके चारों ओर चार पर्वत हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3057)
- **Original**: ये चारों पर्वत मानो सुमेरको धारण करनेके स्थये ईश्वरर्कृत कीलियाँ हैं (क्योंकि इनके बिना ऊपरसे विस्तृत और मूलमें संकुचित होनेके क्ररण सुमेरुके गिरनेकी सम्भावना है] । इनमेंसे मन्दराचल्ठ पूर्वमें, गन्धमादन दक्षिणमें, विपुल पक्षिममें और सुपार्श्व उत्तरमें है। ये सभी दस-दस हजार योजन ऊँचे है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3058)
- **Original**: इनपर पर्वतोंबी ध्वजाओंके समान क्रमशः ग्यारह-ग्यारह सौ योजन ऊँचे कटम्प, जम्बू , पीपल और वटके वृक्ष हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3059)
- **Original**: है महाम॒ुने! इनमें जम्बू (जामुन) वक्ष जम्बूद्वीपके नामका कारण है। उसके फल महान्‌ गजराजके समान बडे होते हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3060)
- **Original**: जब वे पर्वतपर गिरते हैं तो फटकर सब ओर फैल जाते हैं
- **Translation**: 

---

