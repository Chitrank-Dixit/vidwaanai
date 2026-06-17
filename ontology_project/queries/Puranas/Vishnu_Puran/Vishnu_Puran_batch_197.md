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

### Verse 1 (Vishnu Puran 0.3921)
- **Original**: 21 वृष्टधा धृतमिदं सर्वमन्न॑ निष्पाशते यया। सापि निष्पाते वृष्टि: सवित्ना मुनिसत्तम
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3922)
- **Original**: 22 आधारभूत: सवितुर्धघुवो मुनिवरोत्तम । घुवस्य शिशुमारो सो सो5पि नारायणात्मक:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3923)
- **Original**: 23 हृदि नारायणस्तस्य शिशुमारस्य संस्थितः । विभर्ता सर्वभूतानामादिभूत: सनातनः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3924)
- **Original**: 24 पोषण करता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3925)
- **Original**: है विप्र ! उस वृष्टिके जलसे परम वृद्धिक्े प्राप्त होकर समस्त ओषधियाँ और फल फ्कनेपर सूख जानेवाले [ गोथूम, यव आदि अन्न ] प्रजावर्गकि[ शरीरकी उत्पत्ति एवं पोषण आदिके ] साधक होते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3926)
- **Original**: उनके द्वारा शास््रविद्‌ मसनीषिगण नित्यप्रति यथाविधि गज्ञानुष्ठान करके देवताओंको सल्तुष्ट करते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3927)
- **Original**: इस प्रकार सम्पूर्ण यज्ञ, वेद, ब्राह्मणादि वर्ण, समस्त देवसमूह और प्राणिगण वृष्टिके ही आश्रित हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3928)
- **Original**: हे मुनिश्रेष्ठ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3929)
- **Original**: अन्नको उत्पन्न करनेवाली वृष्टि ही इन सबको घारण करती है तथा उस वुष्टिकी उत्पत्ति सूर्यसे होती है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3930)
- **Original**: हे मुनिवरोत्तम ! सूर्यका आधार ध्रुव है, घुजक्ा शिश्लुभार है तथा शिक्ुुमास्के आश्रय श्रीनारायण हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3931)
- **Original**: उस खझिशुमारके हृदयमें श्रोनारायण स्थित हैं जो समस्त प्राणियोकि पालनकर्ता तथा आदिभूत सनातन पुरुष हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3932)
- **Original**: _कसक नौ है 4 जमन-+- इति श्रीविष्णुपुराणे द्वितीयेंठशें नवमोउध्यायः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3933)
- **Original**: _ +- हा ारौर+ दसवाँ अध्याय द्वादझ् सूर्षोकि नाम एवं अधिकारियोंका वर्णन अीप्राञर उवाच साशीतिमण्डलशतं काप्ठयोरन्तरं द्वयो: । आरोहणावरोहाभ्यां भानोरब्देन या गति:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3934)
- **Original**: 41 स रथो5घिष्ठितो देवैरादित्यैऋषिभिस्तथा । गन्धर्वैरप्सरोभिश्न॒ आमणीसर्पराक्षसै:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3935)
- **Original**: 2 धाता क्रतुस्थला चैव पुलस्त्यो वासुकिस्तथा । रथभृदग्रामणीहितिस्तुप्बुरुअओव सप्तम:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3936)
- **Original**: 3 एते वसन्ति वै चैत्रे मधुमासे सदैव हि। मैत्रेय स्यन्दने भानो: सप्त मासाधिकारिण:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3937)
- **Original**: 4 अर्यमा पुलहअ्रैब रथोजा: पुक्षिकस्थला । प्रहेतिः कच्छबीरश्न नारदभ रथे रखे:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3938)
- **Original**: 5 माश्ववे निषसन्त्येते शुचिसंज्े निखोध मे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3939)
- **Original**: 6 श्रीपरावारजी बोले--आरोह और अवरोहके द्वारा सूर्यकी एक वर्षमें जितनी गति है उस सम्पूर्ण मार्गकी दोनों काक्ाऑका अन्तर एक सौ अस्सी मण्डल है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3940)
- **Original**: सूर्यका रथ [ प्रति मास ] भिन्न-भिन्न आदित्य, तऋहंषि, गन्धर्न, अप्सण, यक्ष, सर्प और राक्षसगणोंसे अधिष्ठित होता है
- **Translation**: 

---

