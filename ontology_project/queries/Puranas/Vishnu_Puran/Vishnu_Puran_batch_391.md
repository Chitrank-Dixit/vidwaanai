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

### Verse 1 (Vishnu Puran 0.7801)
- **Original**: इसलिये उठिये और रथपर चढ़कर अतभन्वाके मारनेक्ा प्रयत्न कोजिये।' कृष्णचनद्रके ऐसा कहनेपर बलदेवजोंने भी “बहुत अच्छा' कह उसे स्वीकार किया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7802)
- **Original**: कृष्ण और बलदेयको [अपने बधके लिये] उद्यत जान दातधन्ताने कतवर्माके पास जाकर सहायताके ढिव्ये प्रार्था की
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7803)
- **Original**: तब कृतबर्मान इससे कहा--
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7804)
- **Original**: “मैं बलदेव और खासुदेशसे विरोध करतेमें समर्थ नहीं हुँ।' उसके ऐसा कहनेपर शतधन्वाने अक़ूरसे सहायता मांगी, तो अक्ूरने भी कहा--
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7805)
- **Original**: 'जो अपने पाद-प्रहारसे त्रित््रेकीको कम्पायमान कर देते हैं, देखहात्रु असुरगणकी स्लियोंको
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7806)
- **Original**: 276 आआआआआआआआआआआआआश्रीविष्यपुराण आर श्रीविष्णुपुराण ( आ> 13 मभिलष्यतामित्युक्तशशतघनुराह ।। 86
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7807)
- **Original**: यहा- स्मत्परित्राणासमर्थ भवानात्मानम्धिगच्छति तदयमस्मत्तस्तावन्‍्यणि: संगृह्य रक्ष्यतामिति
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7808)
- **Original**: एबमुक्त:. सोठप्याह
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7809)
- **Original**: यहान्त्यायामप्यवस्थायां न कस्मैचिद्धवान्‌ कथयविष्यति तदहमेत॑ ग्रहीष्यामीति
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7810)
- **Original**: तथेत्युक्ते चाक़ूरस्तन्मणिरल्नं जग्राह
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7811)
- **Original**: शतथनुरप्यतुलवेगां शतवोजनवाहिनीं बडवामारुह्मापक्रान्त:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7812)
- **Original**: _ शैव्यसुप्रीव- मेघपुष्पवलाहकाश्चचतुष्टययुक्तरथस्थितो बलदेव- यासुदेवौ तमनुप्रयाती
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7813)
- **Original**: सा च बड़वा झतयोजनप्रमाणमार्गमतीता पुनरपि बाह्यमाना मिथिलावनोहेशे प्राणानुत्ससर्ज
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7814)
- **Original**: झतधघनुरपि तां परित्यज्य पदातिरेवाद्रवत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7815)
- **Original**: कृष्णोषपि बलभद्रमाह ।
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7816)
- **Original**: तावदत्न स्यन्दने भवता. स्थेयपहपेनमधमाचार॑ पदातिरेव पदातिमनुगम्य यावद्धातयामि अन्न हि भूभागे दृष्टदोषास्सभया अतो नैतेउश्वा भवतेम॑ भूमि- भागमुल्लड्डनीया:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7817)
- **Original**: तथेत्युक्त्वा बलदेवो रथ एव तस्थों
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7818)
- **Original**: कृष्णोषपि ह्विक्रोशमात्र॑ भूमिभागमनुसृत्य दूरस्थितस्यैव चक्र क्षिप्वा शतथनुषश्शिरश्िच्छेद
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7819)
- **Original**: तच्छरीराम्बरादिषु च बहुप्रकार- मन्विच्छन्नपि स्यमत्तकमर्णिं नाबाप यदा तदोपगम्य बलभद्रमाह
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7820)
- **Original**: वृधैवास्मानि: शतधनु- धातितो न प्राप्तमस्विलजगत्सारभूत॑ तन्महारल्ल स्थमन्तकाख्यमित्याकण्योद्धतकोपो. . बलदेवो बैबन्यदान देते हैं तथा अति प्रतल झत्रु-सेनासे भी जिनका चक्र अप्रतिहत रहता है उन चक्रधारी भगवान्‌ वासुदेवसे तथा जो अपने मदोन्‍्मत्त नयनोंकी चितवनसे सबका दमत करनेवाले और भयड्ूर शबुसमृहरूप हाथियोंकों खींचनेके लिये अखण्ड महिमाशाली प्रयष्ड हल धारण करनेवाले हैं उन श्रीहलूघरसे युद्ध करनेमें तो निखिऊल-लोक-बन्दनीय देवगणमें भी कोई समर्थ नहीं है फ़िर मेरी तो बात ही क्या है 2
- **Translation**: 

---

