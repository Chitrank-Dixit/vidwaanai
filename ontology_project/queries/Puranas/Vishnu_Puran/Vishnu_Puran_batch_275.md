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

### Verse 1 (Vishnu Puran 0.5481)
- **Original**: है नूप ! जो अन्न मन्त्रपूत और प्रशस्त हो तथा जो बासी न हो उसींको भोजन करे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5482)
- **Original**: परंतु फल, मूल और सूखी शाखाओंको तथा बिना पकाये हुए लेह्मा (चटनी) आदि और गुड़के पदार्थेकि
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5483)
- **Original**: तद्दद्धारीतकेभ्यश्ष गुडभक्ष्येभ्य एव च। भुञ्जीतोद्धृतसाराणि न कदापि नरेश्वर
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5484)
- **Original**: 85 नाहोर्ष पुरुषो>श्षीयादन्यत्र जगतीपते । मरध्वम्युदधिसर्पिभ्यस्सक्तृभ्यक्ष विवेकवान्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5485)
- **Original**: 86 अश्रीयात्तन्ययों भूत्वा पूर्व तु मधुरं रसम्‌। ललणाम्त्ते तथा मध्ये कदुतिक्तादिकांस्ततः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5486)
- **Original**: 87 अन्ते पुनर्द्वाशी तु बलारोग्ये न मुझ्नति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5487)
- **Original**: 88 अनिन्ध॑ भक्षयेदित्थ॑ वाग्यतोउश्नमकुत्सयन्‌ । पञ्चग्रासं महामौनं प्राणाह्याप्यायन॑ हि तत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5488)
- **Original**: 89 भुक्‍्त्वा सम्यगधाचम् प्राइमुखोदइमुखो5पि वा । यथावत्पुनराचामेत्याणी प्रक्षाल्य पूलत:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5489)
- **Original**: 90 स्वस्थ: प्रशान्तचित्तस्तु कृतासनपरियग्रह: । अभीष्टदेकतानां तु कुर्वीत स्मरणं नरः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5490)
- **Original**: 91 अभिराष्याययेद्धातुं पार्थिव पवनेरित: । दत्तावकाह नभसा जरयत्वस्तु मे सुखम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5491)
- **Original**: 92 अन्न बलाय मे भूपेरपामग्न्यनिछूस्थ च। भवत्येतत्परिणत॑ ममास्त्वव्याहत॑ सुखम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5492)
- **Original**: 93 प्राणापानसमानानामुदानव्यानयोस्तथा .। अन्न पुष्टिकरं चास्तु ममाप्यव्याहतं सुखम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5493)
- **Original**: 94 यक्छन्वरोगो मम चास्तु देहे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5494)
- **Original**: 95 प्रथानभूतोी.. भगवान्यथैक: । तेनात्तमशेषमन्न मारोग्यद॑ मे परिणाममेतु
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5495)
- **Original**: 96 विष्णुरत्ता तथैवान्नं परिणामश्न ले तथा। सत्येन तेन मद्धुक्ते जीर्यत्वन्नमिदं तथा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5496)
- **Original**: 97 डुत्युशार्य स्वहस्तेव परिमृज्य तथोदरम्‌। अनायासप्रदायीनि कुर्यात्कर्माण्यतन्द्रित:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5497)
- **Original**: 98 सत्येन तृतीय अंश 197 लिये ऐसा नियम नहीं है। हे नरेधर ! सारहीन पदार्थोंको कभी न साय
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5498)
- **Original**: हे पृचिवीपते ! विवेकी पुरुष मधु, जल, दही, घी और सत्तूके सिवा और किसी पदार्थको पूरा न साय
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5499)
- **Original**: भोजन एकापचित्त होकर करे तथा प्रथम मघुररस, फिर लवण और असम (खट्टा) रस तथा अन्तमें कट और तोखे पदार्थोंको साय
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5500)
- **Original**: जो पुरुष पहले द्रव पदार्थोको. बीचमें कठिन वस्तुओंको तथा अन्तमें फिर द्रव पदार्थोंको ही स्वाता है बह कभी बल तथा आरोम्यसे होन नहीं होता
- **Translation**: 

---

