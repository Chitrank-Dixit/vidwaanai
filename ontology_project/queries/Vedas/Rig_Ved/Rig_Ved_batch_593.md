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

### Verse 1 (Rig Ved 0.11841)
- **Original**: जो विषयुक्त, लोहे के फल लगा, हिंसक अग्रभाग वाला यह बाण है, पर्जन्य से जिनका पराक्रम बढ़ता है, उन बाण देवता को हमारा नमस्कार है
- **Translation**: 

---

### Verse 2 (Rig Ved 0.11842)
- **Original**: 5130. अवसृष्टा परा पत शरव्ये ब्रह्मसंशिते । गच्छामित्रान्म पद्चस्व मामीषां क॑ चनोच्छिष:
- **Translation**: 

---

### Verse 3 (Rig Ved 0.11843)
- **Original**: हे बाण रूपो अस्त्र ! मज्रों के प्रयोग से तीक्ष्ण किये हुए आप हमारे द्वारा छोड़े जाते हुए शत्रु सेना पर एक साथ प्रहार करें और उन्हें संतप्त करें । उनके शरीरों में प्रविष्ट होकर सभी का विनाश करें तथा किसी भी दुष्ट को जीवित न बचने दें
- **Translation**: 

---

### Verse 4 (Rig Ved 0.11844)
- **Original**: 5131. यत्र बाणा: सम्पतन्ति कुमारा विशिखाइव
- **Translation**: 

---

### Verse 5 (Rig Ved 0.11845)
- **Original**: तत्रा नो ब्रह्मणस्पतिरदितिः शर्म यच्छतु विश्वाहा शर्म यच्छतु
- **Translation**: 

---

### Verse 6 (Rig Ved 0.11846)
- **Original**: 104 ऋग्ेद संहिता भाग - 2 जहाँ शिखारहित बालकों (चंचल वालकों) के समान बाण गिरते हों, वहाँ ब्रह्मणसपति और अदिति हमें सुख प्रदान करें और हमारा सदा कल्याण करें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.11847)
- **Original**: 5132 मर्माणि ते वर्मणा छादयामि सोमस्तवा राजामृतेनानु वस्ताम्‌। ररोवरीयो वरुणस्ते कृणोतु जय त्वानु देवा मदन्तु
- **Translation**: 

---

### Verse 8 (Rig Ved 0.11848)
- **Original**: हे रथी ! आपके पर्मस्थलों को हम कवच से युक्त करते हैं । सोप्रदेव आपको अपृत से युक्त करें । वरुणदेव आपको सुख्ध प्रदान कं । आपकी विजय से देवगण आनर्दित हों
- **Translation**: 

---

### Verse 9 (Rig Ved 0.11849)
- **Original**: 5133 यो न: स्वो अरणो यश्ष निष्टयो जिधांसति। देवास्तं सर्वे धूर्वनु ब्रह्म वर्म ममान्तरम्‌
- **Translation**: 

---

### Verse 10 (Rig Ved 0.11850)
- **Original**: जो हमारे बन्धु होकर द्रेष करते हैं, गुप रूप से हमर संहार की इच्छा रखते हैं, उन्हें सव देवगण यष्ट कर दें । वेदमत्र ही हमारे कवचछूप हैं; वे हमारा कल्याण करें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.11851)
- **Original**: इति घष्ठं मण्डल समापतम्‌
- **Translation**: 

---

