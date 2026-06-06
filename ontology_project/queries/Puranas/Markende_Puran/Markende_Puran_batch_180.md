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

### Verse 1 (Markende Puran 0.3581)
- **Original**: वे ही विद्या (ज्ञान) उत्फा करती हैं । भगवान्‌ विष्णुकी आवास्वरूपा उन भगव॑तीके द्वारा हीं तुम, ये वैश्य त्था अग्यान्य विवेकी जन मोहित होते हैं, मोहित छुए हैं तथा आगे भी मोहित हाँगे। महाराज! तुप उन्हों परमेश्वरीकी शरणमें जाओ
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3582)
- **Original**: आराधना करनेपर वे ही मनुष्योंकों भोग, स्वर्ग तथा मोक्ष प्रदान करती हैं
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3583)
- **Original**: मार्कण्डेंय उद्ाच # द
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3584)
- **Original**: इत्ति तस्य बच: भ्रुत्वा सुर: स नराधिपः
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3585)
- **Original**: प्रंणिप्रत्य महाभाग॑ तपृषिं शंसितद्वतम्‌। निर्विण्णो5तिममत्वेन ग्रज्यापहरणेन चा
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3586)
- **Original**: जगाम ख़दस्तपसें से ह्॑ वैश्यों महामुने। संदर्शनार्थमम्बाया नदीपुल्िनसंस्थितः
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3587)
- **Original**: सच बैश्यस्तप्स्तेषे देवीसूक्ते परं जपन्‌। तो तंस्मिन्‌ पुलिने देव्या: कृत्खा मूर्ति महीमयीम्‌
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3588)
- **Original**: अहणां अक्रतुस्तस्याः प्रुष्पधूपार्नितर्पणै:
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3589)
- **Original**: निराहारी सताहारी तन्मनस्कौ समाहितौ
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3590)
- **Original**: ददतुस्ता बर्लि चैव निज्ञगात्रासृगुक्षितम्‌। एवं समाराधयतोस्त्रिभि्वरर्यतात्मनों;
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3591)
- **Original**: परितुष्ठा जगद्धात्री प्रत्यक्ष प्राह चण्डिका
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3592)
- **Original**: पार्कण्डेबजी कहते हैं--
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3593)
- **Original**: क्रौष्टकिजी ! पेधामुनिके ये वचन सुनकर राजा सुरथने उत्तम ब्रतका पालन करनेवालें उन महांभाग महर्षिकों प्रणाम किया। ये अत्यन्त ममता और राज्यापहरणसे बहुत खिन्न हो चुके श्रे
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3594)
- **Original**: महामुने! इसलिये विरक्त होकर वे राजा तथा चैश्य जत्काल तपस्याकों चले गये और वे जगदम्बाके दर्शनके लिये नदीके तटपर रहकर तपस्या करने लगे
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3595)
- **Original**: बे वैश्य उत्तम देवीसूक्तका जप करते हुए तपस्यामें प्रंवृत्त हुए। वे दोनों नदीके तटपर देबीको मृण्मयों मूर्ति बनाकर पुष्प, धूप और हवन आदिकें द्वारा उनकी आशधना करने लगे। उन्होंने पहले तो आहारकों श्रीरे-भीरे कम किया; फिर बिल्कुल निराहार रहकर देवीमें ही 'पत लगाये एन्माग्रतापुर्चक उनका चिन्तन आरम्प क्रिया
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3596)
- **Original**: वे दोनों अपने शरीरके रक्तसे प्रोक्नचित बलि देते हुए लगातार तीन वर्षोततक संयमपूर्वक आराधना करते रहे
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3597)
- **Original**: इसपर प्रसन्न होकर जगत्‌कों धारण करनेबाली चशण्डिका
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3598)
- **Original**: र्ढड> > संक्षिप्त मार्कण्डेयपूराएं * कश्र7 *+ 0
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3599)
- **Original**: 2:54.436:##%08# 7770 +* » 05 3 571:3:2 2 2 45 फऋककऊ## # 7 » 2 » जा 2:5:35:2:4.2.2:4./# & 6 # 464 »50550क कक कर 8ह का 4 33 ऊँ! देवीने प्रत्यक्ष दर्शन देकर कहा
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3600)
- **Original**: देखुयात
- **Translation**: 

---

