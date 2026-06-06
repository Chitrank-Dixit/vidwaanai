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

### Verse 1 (Vishnu Puran 0.10101)
- **Original**: अब् 97
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10102)
- **Original**: ] अप्यड्रमेतद्धनवत्प्रसादा- त्तदड़सड़े फलवन्मम स्थात्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10103)
- **Original**: 27 अप्येष पृष्ठे मम हस्तपद्यं यस्पाडुलिस्पर्शहताखिलाघै- रवाप्यते सिद्धिरपास्तदोषा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10104)
- **Original**: 28 येनाभिविद्युद्विरशिमिमाला- करालप्रत्युग्रमपेतचक्रम्‌ । चक्र प्लता दैत्यपतेईतानि दैत्याडुनानां. नयनाक्लनानि
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10105)
- **Original**: 29 यत्राम्बु विन्यस्थ बल्िमनोज्ञा- नवाप त्रिदशाधिपत्व मन्वन्तरं पूर्णमपेतशश्नरुम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10106)
- **Original**: 30 अप्येष मां कंसपरिग्रहेण दोषास्पदीभूतमदोषदुष्टम्‌ू._। कर्तावमानोपहते.. धिगस्तु तज्जन्प यत्साधुबहिष्कृतस्य
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10107)
- **Original**: 39 ज्ञानात्मकस्थामलसत्त्वराशे- रपेतदोषस्थ सदा स्फुटस्य । कि वा जगत्यत्र समस्तपुंसा- मज्ञातमस्पास्ति हृदि स्थितस्थ
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10108)
- **Original**: 32 भक्तिविनग्रचेता ब्रजामि. सर्वेश्वरमीश्वराणाम्‌ । अंशावतारं पुरुषोत्तमस्य ः तथामरत्वं तस्मादहं पञ्चम अंदा 355 भ्रगवल्कृपासे इनका अंगसंग पाकर मेरा शरीर भी कृतकृत्य हो सकेगा ?
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10109)
- **Original**: जिनकी अँगुलीके स्पर्शमाजसे सम्पूर्ण पापोंसे मुक्त हुए पुरुष निर्दोषसिद्धि (कैनल्यमोक्ष) प्राप्त कर छेते हैं क्या वे अनन्तमूर्ति श्रीमान्‌ हरि पेरी पीठपर अपना करकमल रखेंगे ?
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10110)
- **Original**: जिन्होंगे अम्रि, चिद्युत्‌ और सूर्यकी किरणमालाके समान अपने उग्र चक्रका प्रहारकर दैत्यपतिकी सेनाको नष्ट करते हुए असुर-सुन्दरियोंको आँखोंके अज्जन धो छाले थे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10111)
- **Original**: जिनको एक जलबिन्दु प्रदान करनेसे राजा बलिने पृथिवीतलूमें अति मनोज्ञ भोग और एक मन्वन्तरतक देवत्व-त्म्रभपूर्वक शात्रुविहोन इन्द्रपद प्राप्त किया था
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10112)
- **Original**: वे हो थविष्णुभगवान्‌ मुझ निर्दोषको भी कंसके संसर्गसे दोषी ठहराकर क्या मेरी अबज्ञा कर देंगे ? मेरे ऐसे साधुजन-यहिष्कृत . पुरुषके जन्मव घिकार है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10113)
- **Original**: अथवा संसारमें ऐसी कौन वस्तु है जो उन ज्ञानस्वरूप, शुद्धसत््वराहि, दोषहीन, नित्य-प्रकारश और समस्त भूतोंके हदयस्थित प्रभुको विदित न हो ?
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10114)
- **Original**: अतः मैं उन ईश्वरोंके ईश्वर, आदि, मध्य और अन्तरहित पुरुषोत्तम भगवान्‌ चिष्णुके अशाबतार श्रीकृष्णचच्रके पास शभक्ति-विनम्रचित्तस. जाता हूँ। [ मुझे पूर्ण आज्ञा है, वे मेरी कभी अवज्ञा न हानादिमध्यान्तमजस्य विष्णों:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10115)
- **Original**: करेंगे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10116)
- **Original**: _हररीगन-+>न
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10117)
- **Original**: है. कक इति श्रीविष्णुपुराणे पश्षमेंउशें सप्तदशोउध्यायः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10118)
- **Original**: “>> कं ----
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10119)
- **Original**: 356 सर अखश्रीविष्णपुराण कक्रऊ़्ू॑ू_ आ* 18 [ अर 18 अठारहवाँ अध्याय भगवानका मशथुराको प्रस्थान, गोपियोंकी विरह-कथा और अक्वूरजीका मोह श्रीपराझर उत्ताच चिन्तयन्निति गोविन्दमुपगम्य स यादव: । अक्कूरोउस्मीति चरणों ननाम शिरसा हरेः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10120)
- **Original**: 5 सो5प्येन॑ ध्वजवज्राब्नकृतचिह्लेन पाणिना । संस्पृश्याकृष्य च॒ प्रीत्या सुगार्द परिषस्वजे
- **Translation**: 

---

