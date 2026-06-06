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

### Verse 1 (Vishnu Puran 0.9621)
- **Original**: 22 पर्जन्यस्सर्वलोकस्योद्धकथाय भुवि वर्षति
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9622)
- **Original**: 23 तस्मात्मावृषि राजानस्सरवें शक्रं मुदा युताः । मस्ैस्सुरेशमर्चन्ति वयमन्ये न मानवा:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9623)
- **Original**: 24 श्रीपराशर उवात्त नन्दगोपस्थ वचन श्रुल्वेत्थ॑ शक्रपूजने । रोषाय त्रिदझेन्द्र्म प्राह दामोदरस्तदा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9624)
- **Original**: 25 नबय॑ कृषिकर्त्तारो बाणिज्याजीबिनो न च । गावोउत्मदैवत॑ तात वबय॑ वनचरा यत:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9625)
- **Original**: 26 आन्वीक्षिकी त्रयी वार्त्ता दण्डनीतिस्तथा परा । विद्या चतुष्ट्य चैतद्वार्तामात्र श्रृणुप्र॒ में
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9626)
- **Original**: 27 कृषिर्वणिज्या तद्॒द्य तृतीय पशुपालनम्‌ । विद्या ह्वोका महाभाग वार्चा वृत्तित्रयाश्रया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9627)
- **Original**: 28 कर्षकाणां कृषिर्वृत्ति: पण्यंविपणिजीविनाम्‌ । अस्माकं गौ: परा वृत्तिर्वात्तिभिदेरिय॑ ब्रिभि:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9628)
- **Original**: 29 विद्यया यो यया युक्तस्तस्य सा दैवतं महत्‌ । सैव पूज्यार्चनीया च सैब तस्योपकारिका
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9629)
- **Original**: 30 यो यस्य फलमश्नन्त्र॑ पूजयत्यपरं नरः। ड॒ह च प्रेत्य चैवासो न तदाप्रोति शोभनम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9630)
- **Original**: 319 कृष्यान्ता प्रधिता सीमा सीमान्तं च पुनर्वनम्‌ बनान्ता गिरयस्सवें ते चास्माकं परा गति:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9631)
- **Original**: 32 न ब्वारबन्धावरणा न गृहक्षेत्रिणस्तथा । सुखिनस्त्वखिले लोके यथा वै चक्रचारिण:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9632)
- **Original**: 33 श्रूयन्ते गिरयश्चैव बनेउस्मिन्कामरूपिण: । तत्तदरर्प समास्थाय रमन्ते स्वेघु सानुषु
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9633)
- **Original**: 34 पुष्ट होकर वत्सबती एवं दूध देनेवाली होती हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9634)
- **Original**: जिस भुमिपर खरसनेवाले मेघ दिखायी देते हैं उसपर कभी अन्न और तृणक्त्र अभाव नहीं होता और न कभी वहाँके स्म्रेग भूखे रहते ही देखे जाते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9635)
- **Original**: यह पर्जन्यदेव (इन्द्र) पृथिवीके जलको सूर्यकिरणोंद्वारा खाँचकर सम्पूर्ण प्राणियॉकी वृद्धिके ल्ये उसे मेघोंद्राय पृथिवीपर बरसा देते हैं। इसलिये वर्षाऋतुमें समस्त राजालोग, हम और अन्य मनुष्यगण देवराज इन्द्रकों यज्ञोद्वारा प्रसत्नतापूर्वक पूजा किया करते हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9636)
- **Original**: अीपराशरजी जओोले--इचह्ककी पूजाके विषयमें नन्दजीके ऐसे क्चन सुनकर श्रीदामोदर देखराजकों कुपित करलेके लिये हो इस प्रकार कहने लगे--
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9637)
- **Original**: “हे तात ! हम न तो कृषक हैं और न व्यापारी, हमारे देवता तो गौएँ ही हैं; क्योंकि हमलोग बनचर हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9638)
- **Original**: आन्वीक्षिकी (तर्कदास्त्र), त्रयी (कर्मकाण्ड) ,दण्डनीति और वार्ता--ये चार विद्याएँ हैं, इनमेंसे केवल वार्ताका जिंवरण सुनो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9639)
- **Original**: हे महाभाग ! बार्ता नामकी विद्या कृषि, वाणिज्य और पशुपालन इन तीन बुत्तियोंकी आश्रयभूता है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9640)
- **Original**: यातके इन तीनों भेदोमेंसे कृषि किसानोंकी, वाणिज्य व्यापारियॉंकी और गोपाल्न हमलोगोंकी उत्तम वृत्ति है
- **Translation**: 

---

