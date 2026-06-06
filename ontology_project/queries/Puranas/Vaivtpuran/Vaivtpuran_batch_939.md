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

### Verse 1 (Vaivtpuran 543.17094)
- **Original**: समझकर शीघ्र हो देवकौ और रुक्मिणीके हाथों
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17095)
- **Original**: सौंप दिया; फिर यलपूर्वक मड्भल-महोत्सव कराया, ब्राह्मणोंकों भोजन कराया और उन्हें बहुत-सा धन-दान किया। (अध्याय 620) उन्होंने पद्माद्वारा समर्चित श्रीकृष्णके चरणकमलोंमें #3/#07//0 9 2: /450500000000
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17096)
- **Original**: + श्रीकृष्णजन्मखण्ड * 757 छ%$%%कऋ$%%ऋ$%कऋ%%%%%%%ऋ$%$%$%$ऋऋ$कऋऋ%ऊऋकऋकऋऋ$%ऊकऋ$%ऋकऋऊऋऊऋ$%ऋऊऊऋऊ$ऊऋ$%ऊऋऋऋ5+ऊऋ$%$$%$ऋऊऋऊऋक#ऊ$%$%ऊऋ%ऋऊऋऊऋ$ऊ%$%ऊऋ$%ऊऋड$%$%$%$%क$%$%कक श्रृगालोपाख्यान श्रीनारायण कहते हैं--नारद ! एक समयकी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17097)
- **Original**: करो। यदि तुम शरणागत होकर मेरी शरणमें नहीं बात है। श्रीकृष्ण अपने गणोंके साथ सुधर्मा-
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17098)
- **Original**: आ जाओगे तो मैं क्षणभरमें ही द्वारकाकों भस्म सभामें विराजमान थे। उसी समय वहाँ एक
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17099)
- **Original**: कर डालूँगा। मैं अकेला ही लीलापूर्वक क्षणभरमें ब्राह्मणदेवता आये, जो ब्रह्मतेजसे प्रज्वलित हो
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17100)
- **Original**: सेना, पुत्र, गण और बन्धु-बान्धवोंसहित तुम्हें रहे थे। वहाँ आकर उन्होंने पुरुषोत्तम श्रीकृष्णता
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17101)
- **Original**: जला डालनेमें समर्थ हूँ। दर्शन किया और भक्तिपूर्वक उनकी स्तुति की।। मुने! यों कहकर बह ब्राह्मण मौन हो गया। फिर बे शान्त एवं भयभीत हो विनयपूर्बक मधुर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17102)
- **Original**: उसे सुनकर सदस्योंसहित श्रीकृष्ण ठठाकर हँस बचन बोले। पड़े। फिर उन्होंने ब्राह्मणका भलीभाँति आदर- ज्ाह्णने कहा--प्रभो! वासुदेव श्रृगाल
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17103)
- **Original**: सत्कार करके उन्हें चारों प्रकारके पदार्थ (भक्ष्य, नामका एक मण्डलेश्वर राजाधिराज है; वह
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17104)
- **Original**: भोज्य, लेह्य, चोष्य) भोजन कराये। श्रृगालके आपकी अत्यन्त निन्दा करता है और कहता है
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17105)
- **Original**: वाग्बाण उनके मनमें कसक पैदा कर रहे थे; कि “वबैकुण्ठमें चतुर्भन देवाधिदेव लक्ष्मीपति
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17106)
- **Original**: इसलिये बड़े क्षोभसे उन्होंने बह रात बितायी। बासुदेव मैं ही हूँ। मैं ही लोकोंका विधाता और
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17107)
- **Original**: प्रातःकाल होते ही वे बड़ी ठतावलीके साथ ब्रह्माका पालक हूँ। पृथ्बीका भार उतारनेके लिये
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17108)
- **Original**: हर्षपूर्वक्त गणोंसहित रधपर सवार हो सहसा वहाँ ब्रह्माने मेरी प्रार्था की थी; इसी कारण
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17109)
- **Original**: जा पहुँचे, जहाँ राजा श्रृगाल था। उनके आनेका भारतवर्षमें मेरा आगमन हुआ है। मैंने महाबली
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17110)
- **Original**: समाचार सुनकर राजा श्रृगाल कृत्रिम-रूपसे चार दैत्ययाज हिरण्यकशिपु, हिरण्याक्ष, मधु और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17111)
- **Original**: भुजा धारण करके गणोंसहित युद्धके लिये कैटभको मारकर सृष्टिकी रक्षा की है। मैं ही
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17112)
- **Original**: श्रीहरिके स्थानपर आया। श्रीकृष्णने मित्र-बुद्धिसे स्वयं ब्रह्मा, मैं ही स्वयं शिव तथा मैं ही लोकोंका
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17113)
- **Original**: उसकी ओर स्नेहभरी दृष्टिसे देखकर मुस्कराते पालक एवं दुष्टोंका संहारक विष्णु हूँ। सभी
- **Translation**: 

---

