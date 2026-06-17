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

### Verse 1 (Vishnu Puran 0.1541)
- **Original**: है सुनिवरों ! उन तीम्र वेगवाले परधनहारी चोरोंके उत्पातसे ही यह बड़ी भारी घूलि उड़ती दीख् रहो है”
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1542)
- **Original**: तब उन सब मुनीश्चरोने आपसमें सत्म्रह कर उस पुत्रहीन ग़जाकी जंघाका पुत्रके लिये यत्रपूर्वक मन्थन किया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1543)
- **Original**: उसकी जंघाके मथनेपर उससे एक पुरुष उत्पन्न हुआ जो जले द्वैँठके समान काल्त्न, अत्यन्त नाटा और छोटे मुखवाल्म था
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1544)
- **Original**: उसने अति आतुर होकर उन सब ग्रह्मणोंसे कहा--*“मैं क्या करूँ ?” उन्होंने कहा-- निषीद (जैठ)” अतः खह “निषाद” कहल्लाया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1545)
- **Original**: इसलिये हे मुनिशार्ट्ल ! उससे उत्पन्न हुए. ह्मेग विश्याचलनिवासी पाप-परायण निषादगण हुए
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1546)
- **Original**: ठस निषादरूप ट्वारसे राजा वेनका सम्पूर्ण पाप निकल गया। अतः निषादगण वेनके पापोंका नाश करनेवाले हुए
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1547)
- **Original**: फिर उन ब्राह्मणोनि उसके दायें हाथका मन्धन किया। उसका मन्थन करनेसे परमप्रतापी जेनसुबन पृथु प्रकट हुए, जो अपने शरीरसे प्रज्वल्ित अप्रिके समान देदीप्पान थे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1548)
- **Original**: इसी समय आजगब नामक आइ्य (सर्वप्रथम) शिव-धनुष और दिव्य वाण तथा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1549)
- **Original**: आः0 13 ] अ्रधप अंधा 55 तस्मिन्‌ जाते तु भूतानि सम्प्रहाशानि सर्वश:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1550)
- **Original**: कवच आकाइसे गिरे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1551)
- **Original**: उनके उत्पन्न होनेसे सभी सत्पुत्रेणेव जातेन बेनो5पि त्रिदिव ययौ जीवोॉंको अति आनन्द हुआ और केवल सत्पुत्र्के हो जन्म पुन्नाग्रो नरकात्‌ त्रातः खग ऐ डर लेनेसे बेन भी स्वर्गलोककों चल्म्र गया। इस प्रकार पुन्न रकात्‌ त्रातः सुमहत्मता महात्मा पुत्रके कारण ही उसकी पुम्‌ अर्थात्‌ नस्कसे ते समुद्राश्ष नद्यश्न रल्लान्यादाय सर्वश:।
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1552)
- **Original**: रक्षा हुई
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1553)
- **Original**: तोयानि चाभिषेकार्थ सर्वाण्येवोपतस्थिरे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1554)
- **Original**: 43 महाराज पृथुके अभिषेकके रित्ये सभी समुद्र और पितामहक्ष॒ भगवान्देवैराड्रिसि: सह। नदियाँ सब प्रकारके रन्न और जलकू लेकर उपस्थित हुए
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1555)
- **Original**: उस समय आंगिरस देवगरणणोंके सहित पितामह स्थावराणि च भूतानि जड्जमानि च सर्वशः । ब्रद्माजीनी और समस्त स्थावर-जंगम प्राणियोनि वहाँ समागम्य तदा वैन्यमभ्यसिश्षत्रराधिपम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1556)
- **Original**: आकर महाराज बैन्य (वेनपुत्र) का राज्याभिषेक किया हस्ते तु दक्षिणे चक्रे दृष्टवा तस्यथ पितामह: ।
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1557)
- **Original**: उनके दाहिने हाथमें चक्रका चिह्न देखकर उन्हें विष्णोरंश पृर्थु मत्वा परितोष पर ययौ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1558)
- **Original**: विष्णुका अकलान दिनाक अल जलन तत5 2 ववष्णुचक्र सर्वेषां
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1559)
- **Original**: 5 ह्व्सा विष्णुचक्रे करे चिह्ढं सर्वेषां चक्रवर्तिनाम्‌ । चक्रवरतों राजाओंकि हाथमें हुआ करता है। उनका प्रभाव भवत्यव्याहतो यस्य॒प्रभावस्त्रिददीरपि
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1560)
- **Original**: कभी देवतांओंसे भी कुष्ठित नहीं होता
- **Translation**: 

---

