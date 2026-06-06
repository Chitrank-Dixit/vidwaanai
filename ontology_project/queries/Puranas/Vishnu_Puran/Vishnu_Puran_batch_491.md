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

### Verse 1 (Vishnu Puran 0.9801)
- **Original**: है केशव ! स्त्री और ब्रास्म्कोंके सहित सभो व्रजवासियोंक्यी आपपर अत्यन्त प्रीति है। आपका यह कर्म तो देवताओंके लिये भो दुष्कर है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9802)
- **Original**: हे कृष्ण ! आपकी यह आल्यावस्था, विचित्र बक-बीर्य और हम-जैसे नीच पुरुषों्सें जन्म लेना--हे अमेयात्मन्‌ ! ये सब बातें विचार: करनेपर हमें शंकामें डाल देती हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9803)
- **Original**: आप देवता हों, दानव हों, यक्ष हों अथवा गय्धर्य हों; इन बातोंका विचार करनेसे हमें क्या प्रयोजन है ? हमारें तो आप बन्धु ही है, आत: आपको नमस्कार है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9804)
- **Original**: अ्रीपराशरजी खोले--गोपगणके ऐसा कहनेपर महामति क्ृण्णचन्द्र कुछ देरतक चुप रहे और फिर कुछ प्रणयजन्य कोपपूर्यक इस प्रकार कहने लगे---
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9805)
- **Original**: आ्रीभगवानने कहा--हे गोपगण ! यदि आपस्थ्रेगोंको मेरे सम्बन्धसे किसी प्रकारकी कृज्जा न हो, तो मैं आपल्मेगोंसे प्रशेसनीय हूँ इस ब्रातका क्चार करनेकी भी क्या आवश्यकता है ?
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9806)
- **Original**: यदि मुझमें आपको प्रीति है और यदि मैं आपकी प्रशोसाका पात्र हूँ तो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9807)
- **Original**: 5433 नाह देवो न गन्धरवों न यक्षो न चर दानव: । अहं वो बान्धवों जातो नैतच्चिन्त्यमितो5न्यथा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9808)
- **Original**: 12 श्रीपराश्र उवाच इति श्रुत्वा हरेवाकक्‍्यं बद्धमौनास्ततो वनम्‌। ययुर्गोपा महाभाग तस्मिग्णयकोपिनि
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9809)
- **Original**: 13 कृष्णस्तु विमलं व्योम दारघन्रस्य चन्द्रिकाम्‌ । तदा कुमुदिनी फुल्छामामोदितदिगन्तराम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9810)
- **Original**: 14 बनराजिं तथा कूजदभूड्डमालामनोहराम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9811)
- **Original**: विलोक्य सह गोपीभिर्मनश्रक्रे रति प्रति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9812)
- **Original**: 15 बिना रामेण मधुरमतीव वनिताप्रियम्‌ । जगौ कलपद शौरिस्तारमद्रकृतक्रमम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9813)
- **Original**: 16 रम्यं गीतध्यनिं भ्रुत्वा सन्त्यज्यावसधांस्तदा । आजयप्पुस्त्वरिता गोष्यो यत्रास्ते मधुसूदन:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9814)
- **Original**: 97 जानैइ्शानैर्जगौ गोपी काचित्तस्य लयानुगम्‌ । दत्तावधाना काचिश तमेव मनसास्मरत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9815)
- **Original**: 18 काचित्कृष्णोति कृष्णोति प्रोच्य छूजामुपाययो । ययौ च काचित्रेमान्धा तत्पार्धमविलम्बितम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9816)
- **Original**: 19 काचिश्चावसथस्पान्ते स्थित्वा दृष्ठा बहिर्गुरुम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9817)
- **Original**: तन्ययत्वेन गोविन्द दध्यों मीलितलोचना
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9818)
- **Original**: 20 तशचित्तविमलाह्लादक्षीणपुण्यत्ॉया._ तथा । तदप्राप्तिमहादुःस्ववित्लीनाशेषषातका. _
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9819)
- **Original**: 21 चिन्तयन्ती जगत्सूति परब्रह्मस्वरूपिणम्‌ निरुच्छासतया मुक्ति गतान्या गोपकन्यका
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9820)
- **Original**: 22 गोपीपरिवृतो रात्रि, झरशन्ब्रमनोरमाम्‌ । मानयामास गोविन्दो रासारम्भरसोत्सुकः
- **Translation**: 

---

