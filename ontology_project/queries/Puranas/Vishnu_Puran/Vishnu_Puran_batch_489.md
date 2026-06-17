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

### Verse 1 (Vishnu Puran 0.9761)
- **Original**: 18 अ्रीभयवानुवाच जानामि भारते वंशे जात॑ पार्थ तवांशत: । तमहं पालयिष्यापि यावत्स्थास्यामि भूतले
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9762)
- **Original**: 19 यावच्महीतले शक्र स्थास्याम्यहमरिन्दम । न ताबर्दर्जुन॑ कश्निद्देवेन्र युधि जेख्यति
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9763)
- **Original**: 20 कंसो नाम महायाहूरदैत्यो5रिष्टस्तथासुरः । केशी कुवलयापीडो नरकाशास्‍््तथा परे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9764)
- **Original**: 29 हतेषु तेषु देवेन्र भविष्यति महाहव: । तत्र विद्धि सहस्नाक्ष भारावतरणं कृतम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9765)
- **Original**: 22 स लव गच्छ न सन्ताप॑ पुत्रार्थे कर्तुमहसि । नार्जुनस्य रिपु: कश्चिन्ममाग्रे प्रभविष्यति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9766)
- **Original**: 23 अर्जुनार्थे त्वाहं सर्वान्युधिष्ठिरपुरोगमान्‌ । निवृत्ते भारते युद्धे कुच्त्यै दास्याम्यविक्षतान्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9767)
- **Original**: 24 ओपराजर उवाच इत्युक्त: सम्परिष्ठज्य देवराजो जनार्दनम्‌। आस्द्वौरावत॑ नाग पुनरेव दिल ययो
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9768)
- **Original**: 25 कृष्णो हि सहितो गोभिगोपालैश्व पुनर्त्रजम्‌ । आजगामाथ गोपीनां दृष्टिपूतेन बर्त्मना
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9769)
- **Original**: 26 श्रीपराज्षरजी बोले--तदनन्तर इन्द्रने अपने बाहन गजरज पऐरवरठका घण्टा लिया और उसमें पवित्र जल अस्कर उससे कणष्णाचद्भका अभिषेक किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9770)
- **Original**: श्रीकृष्णच-रद्रकत्र अभिषेक होते समय गौओने तुरन्त ही अपने स्तनोंसे टपकते हुए दुग्धसे पृथित्रीकों भिगो दिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9771)
- **Original**: इस प्रकार गौओंके श्रीजनार्दनको उपेन्द्र-पदपर अभिषिक्त कर दाचीपति इन्द्रगे पुणः प्रीति और विनयपूर्वक कहा--
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9772)
- **Original**: “हे महाभाग ! यह तो मैंने गौओंका बचन पूरा किया, अब पृथिवीके भार उतारनेकी इच्छासे मैं आपसे जो कुछ और निवेदन करता हूँ वह भो सुनिये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9773)
- **Original**: हे पृथिवीधर ! हे पुल्षसिंह ! अर्जुन नामक मेरे अझने पृथिवीपर अवतार लिया है; आप कृपा करके उसकी सर्वदा रक्षा कॉों
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9774)
- **Original**: हे मघुसूदन ! बह बीर पृथिवीका भार उतारनेमें आपका साथ देगा, अतः आप उसकी अपने दरीरके समान ही रक्षा करें”
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9775)
- **Original**: ओीभगयान्‌ खोलछे--भरतकझमें पृथाके पुत्र अर्जुनने तुम्होरे अंशसे अवतार लिया है--यह मैं जानता हूँ। मैं जबतक पृथियीपर रहुँगा, उसकी रक्षा करूँगा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9776)
- **Original**: हे शग्रुसूदन देवेद्ध ! जबतक महीतलपर रहूँगा तबतक अर्जनको युद्धमें कोई भी न जीत सकेगा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9777)
- **Original**: हे देकेद्र ! विशाल भुजाओंवाला कंस नामक दैत्य, अरिषश्टसुर, केशी, कुनलयापीड़ और नसकासुर आदि अन्यान्य दैत्योंका नाश होनेपर यहाँ महाभारत-युद्ध होगा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9778)
- **Original**: है सहस्त्राक्ष! उसी समय पृथिवीका भार उतरा हुआ समझना
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9779)
- **Original**: अब तुम असन्नतापूर्वक जाओ, अपने पुत्र अर्जुनके छिल्ये तुम किसी प्रकारक्त चित्ता मत करो; मेंरे रहते हुए अर्जुनका कोई भी कात्रु सफल न हो सकेगा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9780)
- **Original**: अर्जुनके लिये ही मैं महाभारतके अन्तमें युधिष्टिस आदि समस्त पाण्डवॉको अक्षत-शरीरसे कुन्तोकों दूँगा
- **Translation**: 

---

