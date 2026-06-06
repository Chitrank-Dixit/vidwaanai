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

### Verse 1 (Vishnu Puran 0.4721)
- **Original**: स्यारहवाँ मनु धर्मसावर्णि होगा । उस समय होनेवाले देवताओंके विहक्षम, कामगम और निर्वाणरति नामक मुख्य गण होंगे--झनमेंसे प्रत्येकमें तीस-तीस देखता रहेंगे और बरष नामक इन्द्र होगा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4722)
- **Original**: उस समय होनेयाले सप्तर्षियोंके नाम निःस्वर, अग्नितेजा, वपुष्पान, घृणि, आरुणि, हविष्मान्‌ और अनघ हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4723)
- **Original**: तथा धर्मसावर्णि मनुके सर्वत्रग, सुधर्मा, और देवानीक आंदि पुत्र उस समयके राज्याकिकारी पृथिवीपति होंगे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4724)
- **Original**: रुद्रपुत्र॒ सावर्णि बारहबाँ मनु होगा। उसके समय ऋतुधामा नामक इन्द्र होगा तथा तत्कालीन देवताओंके नाम ये हैं सुनो--
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4725)
- **Original**: टे द्विज ! उस समय दस-दस देवताओंके हरित, रोहित, सुना, सुकर्मा और सुराप नामक पाँच गण होंगे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4726)
- **Original**: तपस्वी, सुतपा, तपोमूर्ति, तपोराति, तपोधृति, तपोच्चुति तथा तपोधन--ये सात सप्तर्षि होंगे। अब सनुपुत्रोंके नाम सुनो---
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4727)
- **Original**: उस समय उस मनुके देवबान, उपदेव और देवश्रेष्ठ आदि महावीर्यश्ञाल्ली पुत्र तत्कालीन सप्राट होंगे 36
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4728)
- **Original**: हे मुने ! त्तेरहवाँ रूचि नामक मनु होगा। इस मन्क्‍न्तरमें सुत्रामा, सुकर्मा और सूधर्मा नामक देवगण होंगे इनगेंसे प्रत्येकमें तैतीस-रैंतोस देवता रहेंगे; तथा महावबलवान्‌ दिवस्पति उनका इन्द्र होगा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4729)
- **Original**: 37--39
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4730)
- **Original**: निमोंह, तत्वदर्शों, निष्प्रकम्प, निरुत्सुक, धृतिमान्‌, अन्यय और सुतपा--ये तत्कालीन सप्तरर्षि होंगे। अब मनुपुत्रोके नाम भी सुनो
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4731)
- **Original**: उस्र मन्वन्तरमें चित्रसेम और विचित्र आदि मनुपूत्र राजा होंगे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4732)
- **Original**: औआ8 2 ) भौमशचतुर्दश्श्ात्र मैत्रेय भविता मनु: । शुचिरिन्द्रः सुरगणास्तत्र पक्ष श्ृणुष्न तान्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4733)
- **Original**: डर चाक्षुषाश्न पब्रित्नाश्न कनिष्ठा भ्राजिकास्तथा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4734)
- **Original**: वाचावृद्धाश्न वे देवास्सप्त्षीनपि मे श्रृणु
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4735)
- **Original**: 43 अम्निबाहु: शुच्रि: शुक्रों पागधो5प्रिध एव च युक्तस्तथा जितश्चान्यो मनुपुत्रानतः श्यूणु
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4736)
- **Original**: डड ऊरुगम्भीरबुद्धयाद्या मनोस्तस्य सुता नृपा: । कश्चिता मुनिझार्दूल पालयिष्यन्ति ये महीम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4737)
- **Original**: 45 चतुर्युगान्ते बेदानों जायते किल विप्लव: । प्रवर्तयन्ति तानेत्य भुर्व॑ सप्तर्षयो दिव:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4738)
- **Original**: 46 कृते कृते स्मृतेर्थिप्र प्रणेता जायते मनु; । देबा यज्ञभुजस्ते तु यावन्पन्वन्तरें तु तत्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4739)
- **Original**: 47 भवन्ति ये मनोः पुत्रा यावन्मन्वन्तरं तु तैः । तदन्वयोद्धवैज्ञेव तावद्धू: परिपाल्यते
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4740)
- **Original**: 48 मनुस्सप्तर्षषो देवा भूपालाश्व मनोः सुता; । मन्वन्तरे भवन्तेते शक्रश्लैवाधिकारिण:
- **Translation**: 

---

