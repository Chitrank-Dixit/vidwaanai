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

### Verse 1 (Rig Ved 0.5501)
- **Original**: 2420. इन्ध आशाभ्यस्परि सर्वाध्यो अभयं करत्‌। जेता शत्रून्विचर्षणि:
- **Translation**: 

---

### Verse 2 (Rig Ved 0.5502)
- **Original**: शत्रुविजेता, प्रज्ञावान्‌ इन्द्रदेव सभी दिशाओं से हमें निर्भव बनायें
- **Translation**: 

---

### Verse 3 (Rig Ved 0.5503)
- **Original**: 2421. विश्वे देवास आ गत शृणुता म इमं हवम्‌। एदं बर्हिरनि घीदत
- **Translation**: 

---

### Verse 4 (Rig Ved 0.5504)
- **Original**: हे सम्पूर्ण देवगणो ! आप इस यज्ञ में आकर कुश के आसन पर विशजमान हों तथा हमारी इस प्रार्थना को स्वीकार करें
- **Translation**: 

---

### Verse 5 (Rig Ved 0.5505)
- **Original**: 2422. तीव्रो यो मधुमाँ अय॑ शुनहोत्रेषु मत्सर:। एवं पिबत काम्यम्‌
- **Translation**: 

---

### Verse 6 (Rig Ved 0.5506)
- **Original**: हे सम्पूर्ण देवगणो ! पवित्रता प्रदान करने वाले इस यज्ञ में आनन्ददायी, तीक्ष्ण तथा मधुर सोमरस आपके निमित्त तैयार किया गया है, आप सभी आयें तथा इच्छानुसार इस सोमरस का पान करें
- **Translation**: 

---

### Verse 7 (Rig Ved 0.5507)
- **Original**: पघं0 2 सू0 डर श्र 2423. इन्द्रज्येष्ठा मरूद्गणा देवास: पृषरातयः । विश्वे मम श्रुता हवम्‌
- **Translation**: 

---

### Verse 8 (Rig Ved 0.5508)
- **Original**: जिन मरुदगणों पें सर्वश्रेष्ठ इन्द्रदेव हैं, जिन्हें पोषण देने वाले पृषादेव हैं, वे मरुद्गण हमारी प्रार्थना को स्वीकार करें
- **Translation**: 

---

### Verse 9 (Rig Ved 0.5509)
- **Original**: 2424. अम्बितमे नदीतमे देवितमे सरस्वति। अप्रशस्ता इब स्मसि प्रशस्तिमम्ब नस्कृधि
- **Translation**: 

---

### Verse 10 (Rig Ved 0.5510)
- **Original**: हे नदियों, मातृगण्णों, देवों में सर्वश्रेष्ठ माता सरस्वती ! हम मूर्ख बालकों के समान हैं; अतः हमें उत्तम ज्ञान प्रदान करें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.5511)
- **Original**: 2425, त्वे विश्वा सरस्वति श्रितायुंषि देव्याम्‌ । ब शुनहोत्रेषु मत्स्व प्रजां देवि दिदिडूढि न:
- **Translation**: 

---

### Verse 12 (Rig Ved 0.5512)
- **Original**: हे माता सरस्वती ! आपके तेजस्वी आश्रय में ही सम्पूर्ण जीवन-सुख आश्रित है, अत: हे माता ! आप पवित्र करने वाले यज्ञ में आनन्दित होकर हमें उत्तम सन्तति प्रदान करें
- **Translation**: 

---

### Verse 13 (Rig Ved 0.5513)
- **Original**: 2426. इमा ब्रह्म सरस्वति जुघस्व वाजिनीवति । या ते मन्म गृत्समदा ऋक्तावरि प्रिया देवषु जुद्धति
- **Translation**: 

---

### Verse 14 (Rig Ved 0.5514)
- **Original**: हे माता सरस्वती ! आप अन्न तथा बल प्रदान करके सत्य मार्ग पर चलाने वाली हैं; अतः देवों को प्रिय लगने वाले गृत्समद ऋषि द्वारा बनाये गये उत्तम स्तोत्र हम आपको सुनाते है; आप इन स्तोत्रों को स्वोकार करें
- **Translation**: 

---

### Verse 15 (Rig Ved 0.5515)
- **Original**: 2427 प्रेतां यज्ञस्थ शम्भुवा युवामिदा वृणीमहे। अर्ग्नि च हव्यवाहनम्‌
- **Translation**: 

---

### Verse 16 (Rig Ved 0.5516)
- **Original**: हे मंगलकारी द्यावा - पृथिवि ! हव्यवाहक अग्निदेव के साथ आप दोनों का हम वरण करते हैं। आप _ हमारी प्रार्थना को स्वीकार करके यज्ञ में आयें
- **Translation**: 

---

### Verse 17 (Rig Ved 0.5517)
- **Original**: 2428. द्यावा नः पृथिवी इमं सिश्चमद्य दिविस्पृशम्‌। यज्ञ देवेषु यच्छताम्‌
- **Translation**: 

---

### Verse 18 (Rig Ved 0.5518)
- **Original**: हे चावा - पृथिवि ! सुख के साधक तथा आकाश तक हमारी हवि को स्पर्श कराने वाले यज्ञ को आज आप दोनों देयों तक ले जायें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.5519)
- **Original**: 2429. आ जामुपस्थमह्ठुहा देवा: सीदन्तु यज्ञिया:। इहाद्य सोमपीतये
- **Translation**: 

---

### Verse 20 (Rig Ved 0.5520)
- **Original**: परस्पर सम्बद्ध रहने वाली (द्रोह न करने वाली) हे द्यावा-पृथिवी देवियो ! आज इस यज्ञ में देवगण सोमपान के निमित्त आपके पास बैठें
- **Translation**: 

---

