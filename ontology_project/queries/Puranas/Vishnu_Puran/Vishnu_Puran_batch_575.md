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

### Verse 1 (Vishnu Puran 0.11481)
- **Original**: 39 ततः काशीबलं भूरि प्रमथानां तथा बलम्‌ । समस्तशस्त्रास््रयुतं चक्रस्याभिमुखं यबों
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11482)
- **Original**: 40 शस्त्रास्त्रमोक्षचतुरं॑ दग्ध्वा तदलमोजसा । कृत्यागर्भामशोषां तां तदा वाराणसी पुरीम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11483)
- **Original**: 41 सभूभृदभृत्यपौरां तु साश्वमातड्रमानवाम्‌। ज्वाल्ममालाओंसे पूर्ण था तथा उसके केश अग्निविखाके समान दीप्तिमान्‌ और ताम्रवर्ण थे। वह ब्र्े्पूर्वक “कृष्ण ! कृष्ण !!' कहती द्वारकापुरीमें आयी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11484)
- **Original**: है मुने ! उसे देखकर लोगोंने भय-विचलित नेत्रोंसे जगदति भगवान्‌ मधुसूदनकी शरण ली
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11485)
- **Original**: जब भगवान्‌ चक्रपाणिने जाना कि श्रीशकस्की उपासनाकर काशिराजके पुत्रने ही यह महाकुत्या उत्पन्न की है तो अक्षक्रीडामें लगे हुए उन्होंने लीत्मसे ही यह कहकर कि 'इस अग्रिज्वालामयी जटाओँवाली भयंकर कृत्याक्रो मार डाल' अपना चक्र छोड़ा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11486)
- **Original**: तब भगवान्‌ विष्णुके सुदर्शन चक्रने उस अग्नि- मालामष्डित जराओंवाली और अग्निज्वाछाओंके कारण भयानक मुख्याली कृत्याका पीछा किया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11487)
- **Original**: उस चक्रके तेजसे दग्ध होकर छिल्न-भिन्न होती हुई बह माहेश्वरी कृत्या अति येगसे दौड़ने लगी तथा वह चक्र भी उतने ही खेगसे उनका पीछा करने रूगा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11488)
- **Original**: हे मुनिश्रेष्ठ ! अन्तमें विष्णुचक्रसे हतप्रभाव हुई कृत्याने शीघ्रतासे काज्ञीमें ही प्रवेश किया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11489)
- **Original**: उस समय काशी- नरेशकी सम्पूर्ण सेना और प्रथम-गण अख्ब-शखोंसे सुसज्जित होकर उस चक्रके सम्मुख आये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11490)
- **Original**: तब वह चक्र अपने तेजसे शस्मास््र-प्रयोगमें कुशल उस सम्पूर्ण सेनाको दग्धकर कृत्याके सहित सम्पूर्ण बाराणसीकों जलाने लगा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11491)
- **Original**: जो राजा, प्रजा और सेककॉसे पूर्ण थी; घोड़े, हाथी और मनुष्योंसे भरी थी; अशेषगोष्ठकोझां तो दुर्निरीक्ष्यां सुरैरपि
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11492)
- **Original**: सम्पूर्ण गो8 और कोशोंसे युक्त थी और देवताओंके र0#
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11493)
- **Original**: 0......नललतनतनतन-तननलीदलदलदणदणझीणीीीीीीीनीनीनओीी - सडननइ- + इस वाक्वका अर्थ यह भी होता है कि 'मेरे बधके लिये मेरे पिताके मारनेबाले कृष्णके पास कृत्या उत्पन्न हो।' इसलिये यदि इस वरका जिपरीत परिणाम हुआ तो उसमें शंका नहीं करनी चाहिये।
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11494)
- **Original**: आ0 35 ] पक्कम अंश 400 ज्वाल्प्रपरिष्कृताशेषगृहप्राकारचत्वराम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11495)
- **Original**: छिये भी दुर्दर्नीय थी उसी काशीपुरीको भगवान्‌ विष्णुके अश्षीणामर्षमयप्रसाध्यसाधनसस्यृहप..।...
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11496)
- **Original**: कस था और जिककी दो चार ओर फैट रह ी वह तक प्रस्फुरद्यीप़ि विष्णोरभ्याययौं करम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11497)
- **Original**: फिर लौटकर भगवान्‌ विष्णुके हाथमें आ गया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11498)
- **Original**: बा» जौ “न+ इति श्रीविष्णुपुराणे पञ्षमेंडशे चतुस्विशो5ध्याय:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11499)
- **Original**: जज+-+ औलनया पैंतीसवाँ अध्याय साम्बका बियाह श्रौमैत्रेय उवाच भूय एवाहमिच्छामि बलभद्रस्य धीमत: । श्रोतुं पराक्रम॑ ब्रह्मन्‌ तनन्‍्पमाख्यातुमहसि
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11500)
- **Original**: यमुनाकर्षणादीनि श्रुतानि भगवन्पया
- **Translation**: 

---

