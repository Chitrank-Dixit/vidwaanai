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

### Verse 1 (Bavishya Puran 0.761)
- **Original**: जोत्पत्तिजायते... यशय जोदयपीडितैरपि #
- **Translation**: 

---

### Verse 2 (Bavishya Puran 0.762)
- **Original**: एकचूले द्विचूलक्ा प्रिशिखः पश्चयूलक:
- **Translation**: 

---

### Verse 3 (Bavishya Puran 0.763)
- **Original**: सहस््नरिररूपस्तु चन्द्रकेतुतित. स्थित:
- **Translation**: 

---

### Verse 4 (Bavishya Puran 0.764)
- **Original**: ब्रह्मकिणुशिवात्पक: । अनेकशिल्ल: केतु; स ते पीड़ी व्यपोह्तु
- **Translation**: 

---

### Verse 5 (Bavishya Puran 0.765)
- **Original**: एले अहा महार्पान: सूर्यार्चनपरा: स्लदा। शान्ति कूर्यनतु ते ढशाः सदाकाले हितेक्षणाः
- **Translation**: 

---

### Verse 6 (Bavishya Puran 0.766)
- **Original**: (ब्राह्मपर्थ 175
- **Translation**: 

---

### Verse 7 (Bavishya Puran 0.767)
- **Original**: 36--50) ह-फ्यासकः. पद्मर्ण.. पद्फानिभेक्षण:
- **Translation**: 

---

### Verse 8 (Bavishya Puran 0.768)
- **Original**: कमण्डलुघर: औमान्‌ू. देवगन्धर्वपूजितः
- **Translation**: 

---

### Verse 9 (Bavishya Puran 0.769)
- **Original**: अतुर्पुस््रों टेजफति: सूर्यार्चसपर: सदा । सुह्ण्येश्ो. महातेजा:. सर्वलोकप्रजापति:
- **Translation**: 

---

### Verse 10 (Bavishya Puran 0.770)
- **Original**: अरह्मझब्देन दिव्येत ब्रह्मा झऋन्‍्ति करोंतु ते
- **Translation**: 

---

### Verse 11 (Bavishya Puran 0.771)
- **Original**: पीताम्बरघये. देख. आजियोदयितः सदा । शद्भगुचक्रगदापाणिः इ्यामवर्ण#तुर्भुज:
- **Translation**: 

---

### Verse 12 (Bavishya Puran 0.772)
- **Original**: यज्ञदेहः क्रमों देव आलेयीदयित: सदा
- **Translation**: 

---

### Verse 13 (Bavishya Puran 0.773)
- **Original**: शद्भयक्रगदापाणिर्ण प्रवो मधुसूदनः
- **Translation**: 

---

### Verse 14 (Bavishya Puran 0.774)
- **Original**: अयुदुकण: वये वरेण्यों वरदों देवदेयों महेश्वर:
- **Translation**: 

---

### Verse 15 (Bavishya Puran 0.775)
- **Original**: आदित्यदेहसम्भूतः सर ते शान्ति करोतु खै
- **Translation**: 

---

### Verse 16 (Bavishya Puran 0.776)
- **Original**: (ब्राह्मपर्व 176
- **Translation**: 

---

### Verse 17 (Bavishya Puran 0.777)
- **Original**: जाहापर्य ] + सौर-धर्ममें शान्तिक कर्म एवं अभिषेक-विधि « 167 तदनन्तर सभी मातृकाओंसे झाक्षिके लिये प्रार्थना करे -- “पद्चरागके समान आभावाली, अक्षमाल्य एवं कमण्डलु शारण करनेवाल्ी, आदित्यकी आगंधनामें तथा आज्ञीर्वाद देनेमें तत्पर, सौम्यबदनवाली ब्रह्माणी प्रसन्न होकर तुम्हें शाक्ति प्रदान करें । हिम, कुन्द-पुष्प तथा चन्द्रमाके समान वर्णयाली, आपको चान्ति प्रदान करें
- **Translation**: 

---

### Verse 18 (Bavishya Puran 0.778)
- **Original**: सिन्दूरके समान अरुण विग्रहवाली, सभी अलंकारोंसे विभूषित, हाथमें पाक्ति धारण करनेवाली, मयूरवाहिनी देवी कौमारी आपको शान्ति प्रदान करें
- **Translation**: 

---

### Verse 19 (Bavishya Puran 0.779)
- **Original**: गदा एवं चक्रकों धारण करनेवाली, पीताम्बरधारिणी, सूर्यार्चनमें नित्य तत्पर रहनेयाली, असुरमर्दिनी, देवताओंके द्वारा पूजित चतुर्भुजा देवी वैष्णबी आपको नित्य शान्ति प्रदान करें। ,, ऐशावत्पपर आरूढ, हाथमें चज्र॒ धारण करनेवाली, महाबलदालिनी, सिद्ध-गन्धवॉसे सेवित, सघी अलंकारोंसे विभूषित, चित्र-विचित्र अरुणवर्णवाली, सर्वत्रल्लोचना देवी इन्द्राणा आपको ज्ञाक्ति प्रदान करें। बराहके समान नासिकावाली, श्रेष्ठ यगहपर आरूढ, विकटा,दौख, चक्र तथा 1-पद्मग़गप्रा देखी अतुर्वदनपडुजा । अक्षमाल्प्र्पितकर.. कमप्डलुघपए.. झुधा
- **Translation**: 

---

### Verse 20 (Bavishya Puran 0.780)
- **Original**: सिद्धगन्धर्वनम्ता सर्वाऊैकारभूषिता । इद्धाणी ते सदा देवी सात्तिमासु करोतु थै
- **Translation**: 

---

