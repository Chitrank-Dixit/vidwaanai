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

### Verse 1 (Vishnu Puran 0.9881)
- **Original**: यहाँ कृष्णने अवदय उस गोपीसे कहा नै '[ तू यहीं बैठ ] मैं शीघ्र ही जाता हूँ [ इस वनमें रहनेवाले राक्षसको मारकर ) पुनः तेरे पास ल्ज्ैट आऊँगा। इसीलिये यहाँ उनके चरणोंके चिह्न शीघ्र गतिके-से दीख रहे हैं'
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9882)
- **Original**: यहाँसे कृष्णचन्द्र गहन वनमें चले गये हैं, इसीसे उनके चरण- चिह्न दिखलायी नहीं देते; अब सब ल्जैट चलो; इस स्थानपर चन्द्रमाकी किरणें नहीं पहुँच सकती
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9883)
- **Original**: तदनन्तर बे गोपियाँ कृष्ण-दर्शनसे निराश होकर स्त्रैट आयी और यमुनातर॒पर आकर उनके चरितोंकों गाने लगों
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9884)
- **Original**: तब गोपियोंने. प्रसन्नमुखाराखिन्द त्रिभुचनरक्षक लोल्मविहारी श्रीकृष्णचखको य्ाँ आते देखा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9885)
- **Original**: उस समय कोई गोपी तो श्रीगोवित्दको आते देख्ककर अति हर्षित हो केवल “कृष्ण ! कृष्ण !! कृष्ण !!!' इतना ही' कहती रह गयी और कुछ न जोल सकी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9886)
- **Original**: कोई [त्रणयक्रेपवश] अपनी प्रूभंगीसे छलाट सिकोड़कर श्रीहरिको देखते हुए अपने नेत्ररूप अमरोंद्राय उसके सुस्क्मझका मकरन्द पान करने लगी
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9887)
- **Original**: कोई गोपी गोविन्दको देख नेत्र मैंदकर उन्हींके रूपका ध्यान करती हुई योगारूढ-सी भासित होने लगी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9888)
- **Original**: तब श्रीमाधज किसीसे प्रिय भाषण करके, किसीकी ओर ध्रूभंगीसे देखकर और किसोका हाथ पकड़कर उन्हें मनाने लो
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9889)
- **Original**: फिर ठदारयरित श्रीहरिति उन प्रसन्नचित्त गोपियोंके साथ रासमण्डरल. बनाकर आदरपूर्वक र्मण किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9890)
- **Original**: किन्तु उस समय कोई भी गोपी कृष्णचन्द्रकी सन्निधिको न छोड़ना चाहती थी; इसलिये एक ही स्थानपर स्थिर रहनेके कारण रासोचित मण्डल न बन सका
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9891)
- **Original**: तथ उन गोपियोंमेंसे एक-एकका हाथ पकड़कर श्रीहरिने रासमण्डलकी रचना की । उस समय उनके करस्पर्शसे प्रत्येक गोपीकी आँखें आननदसे मुँद जाती थीं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9892)
- **Original**: तदनन्तर रासक्रीडा आरम्भ हुई। उसमें गोपियोंके चमझ्लल कंकरणणोंकी झनकार होने ऊूगी और फिर क्रमञ्नः जरदर्णन-सम्बन्धी गीत होने लगे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9893)
- **Original**: उस समय कृष्णचन्द्र चन्द्रमा, चन्द्रिका और कुमुदबन-सम्बन्धी गान करने छगे; किन्तु गोपियोंने तो बारम्बार केबल कृष्णनामका ही गान किया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9894)
- **Original**: फिर एक गोपीने नृत्य करते-करते थककर चमझ्जछ कंकणकी झनकारसे युक्त
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9895)
- **Original**: अ>0 ₹4 ] काचित्रविलसद्दाहु: परिरभ्य चुचुम्ब तम्‌। गोपी गीतस्तुतिव्याजात्रिपुणा मधुसूदनम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9896)
- **Original**: 54 गोपीकपोलसंइलेषमभिगम्य हरेर्भुजौ । पुलकोद्मसस्याय स्वेदाम्बुघनतां गतौ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9897)
- **Original**: 55 रासगेयं जगौ कृष्णो यावत्तारतरथ्वनि: । साधु कृष्णेति कृष्णेति तावत्ता ड्विगुणं जगु:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9898)
- **Original**: 56 गतेथ्तुगमन॑ चक्कुर्वलने सम्मुख ययु:। प्रतित्मेमानुल्तेमाभ्यां भेजुर्गोपाज़ना हरिम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9899)
- **Original**: 57 स तथा सह गोपीभी ररास मधुसूदन: । यथाब्दकोटिप्रतिमः क्षणस्तेन विनाभवत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9900)
- **Original**: 58 ता वार्यमाणाः पतिभि: पितृभिभ्रांतृभिस्तंथा । कृष्ण गोपाडडना रात्रौ रमयन्ति रतिप्रिया:
- **Translation**: 

---

