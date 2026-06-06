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

### Verse 1 (Markende Puran 0.3561)
- **Original**: सम्पूर्ण भूतोंकी रक्षा करती हैं
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3562)
- **Original**: मनुष्योंके भवकाले नृणां सैत्र लक्ष्मीवृद्धिप्रंदा गृहे। अभ्युटयके समय वे हो घरमें लक्ष्मीके रूपमें स्थित सैबाभावे. तथालक्ष्मीविनाशायोपजायते।
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3563)
- **Original**: हो उन्नति प्रदान ऋरती हैं और ये हो अधातके समय स्तुता सम्पूजिता पण्वैर्धुपगन्धादिभिस्तशा। दख्तता बनकर बिनाशका कारण होती हैं
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3564)
- **Original**: ददातिविज पुत्रांक्ष मतिं ध्षे गति शुभाष
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3565)
- **Original**: अलंत4ड1
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3566)
- **Original**: पुष्प, धूप और गन्ध आदिसे पूजन करके उनकी ऋषि कहते हैं--
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3567)
- **Original**: यों कहकर प्रत्तण्ड
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3568)
- **Original**: स्तुति कानेपर वे धन, पुत्र, थार्सिक सुद्धि तथा उत्तम पराक्रमवाली भगवती चण्डिा सब देवलाओंके
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3569)
- **Original**: गति प्रदान करती हैं
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3570)
- **Original**: $9 #गाज्ण्डेग्युशाणे फ़कर्निल म्रकातरें रेवीमयहरम्यें #जपुदिकाग काइशोउव्याय: 4174 3%4 $, अभलेको 2. शलकरकाः उ> एक्स 42, एचकादित! 0571 # इस प्रकार श्रीपार्कण्डेचपुराणमें सायर्णिक मन्वन्तरकी कथाके अन्तर्गत वेजामाहात्प्यमें 'फलस्तुति' नामक्त बारहयाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3571)
- **Original**: 17 कऔीफकरक्‍जल> 5, वा: « तो रावदेवा0 2, पत-तथ।
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3572)
- **Original**: *सुर्थ और बैश्यका दंत्रीका सरटान+ 37757 कर #9 #
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3573)
- **Original**: # # 191 77 #- # 4 4 8 $: 4488 6 । 239 तऋयोवशोडथ्याय: सुरथ और वैश्यको देवीका वरदान ध्यान ( <घालार्कमण्डलाभासां चतुर्बाहूं विलोचनाप। पाशाडुशवराभीत्तीर्धारयर््ती शिवां भजे
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3574)
- **Original**: जो उदयकालके सूर्यमण्डलकी-सी कान्ति धारण करनेवाली हैं, जिनके चार भुजाएँ और तीन नेत्र हैं तथा जो अपने हाथोंमें पाश, अक्भुश, बर एवं अभयकी मुद्रा धारण कियें रहतो हैं, ठन शिवा देवींका मैं ध्यान ऋस्ता हूँ।) अन्रषिस्वाचा
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3575)
- **Original**: * 8 ' एतत्ते कच्चितं भूप देवीपाहात्म्यपुन्मप्‌। एरप्रभावा सा देवी ययेदं धार्यते जगत्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3576)
- **Original**: विद्या तथैब क्रियते भगवष्ठिष्णुमायया। तया त्वमेष चैश्यश्व तथैवान्ये विवेक्तिन:
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3577)
- **Original**: मोहान्ते मोहिताओब प्रोहमेष्यन्ति चापरे। तामुपैहि, महाराज शरण परमेश्वरीम्‌
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3578)
- **Original**: आराधिता सैव नृणां भोगस्वर्गापवर्गदा
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3579)
- **Original**: ऋषि कहते हैं--
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3580)
- **Original**: राजन्‌ ! इस प्रकार मैंने तुमसे देवीके अनुपम माहात्म्यका वर्णन क्रिया। जो इस जगत्‌को धारण करतों हैं, उन देवीकां ऐसा ही प्रभाव है
- **Translation**: 

---

