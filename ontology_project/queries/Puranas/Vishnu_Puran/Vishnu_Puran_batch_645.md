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

### Verse 1 (Vishnu Puran 0.12881)
- **Original**: हे गुरो ! मैं चार प्रकारकी राशि और तीन भ्रकासकी इक्तियाँ * जान गया तथा मुझे त्रिविध भाव- भावनाओंका' भी सम्वक्‌ बोध हो गया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12882)
- **Original**: हे द्विज ! आपकी कृपासे मैं, जो जानना चाहिये बह भली प्रकार जान गया कि यह सम्पूर्ण जगत्‌ श्रीविष्णुभगवानसे भिन्न यदेतदख्खिलं विष्णोर्जगन्न व्यतिरिच्यते
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12883)
- **Original**: नहीं है, इसलिये अब मुझे अन्य बातेंके जाननेसे कोई 1-देख्तिये---प्रथम अंश अध्याय 22 इल्मेक 23--33 । 2- », घष्ट अंदा अध्याय 7 दइल्मेक 69--63
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12884)
- **Original**: 3- ,,. पषष्ठ अंश अध्याय 7 इस्मेक 48--571।
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12885)
- **Original**: 456 सप्रर्षिभिस्तथा प्िष्णयैर्भिष्याधिपतिभिस्तथा । ब्राह्मणाह्यर्मनुष्यैश्न॒तथैव पशुभिर्मुगैः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12886)
- **Original**: 24 सरीसूपैर्विहड्रैश.. पलाशाह्यर्महीरुहै: । बनाअिसागरसरित्पातालै: सथरादिभि:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12887)
- **Original**: 25 शब्दादिभिश्न सहित ब्रह्माण्डमखिलं द्विज । मेरोरिवाणुर्यस्पैतद्यन्मयं च द्विजोत्तम
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12888)
- **Original**: 26 स॒ सर्व: सर्ववित्सर्वस्वरूपो रूपवर्जित: । भगवान्कीर्तितो विष्णुरत्र पापप्रणाशन:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12889)
- **Original**: 27 यद्श्वमेधावभृथे स्त्रातः प्राप्नोति मै फलम्‌। मानवस्तदबाप्रोति._ श्रुत्वैतन्पुनिसत्तम
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12890)
- **Original**: 28 प्रयागे पुष्करे चैब कुरुक्षेत्र तथार्णवे । कृतोपवास: प्राप्नोति तदस्य श्रवणान्नरः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12891)
- **Original**: 29 यदझिहोत्रे सुहुते वर्षेणाप्रोति मानवः। महापुण्यफलं विप्र तदस्य श्रवणात्सकृत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12892)
- **Original**: 30 यज्ज्येष्ठशुक्॒द्वादश्यां स्नात्वा वे यमुनाजले
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12893)
- **Original**: मथुरायां हरि दृष्टा प्राप्नोति पुरुष: फलम
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12894)
- **Original**: 31 तदाप्रोत्यखिलं सम्यगध्यायं यः श्रूणोति वै । पुराणस्थास्य विप्रर्षे केशवार्पितमानसः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12895)
- **Original**: 32 अमुनासलिलस्तात: पुरुषों मुनिसत्तम । ज्येष्ठामूले सिते पक्षे द्वादश्यां समुपोषितः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12896)
- **Original**: 33 समभ्यर्च्याच्युतं सम्यद् मथुरायां समाहित: । अश्वमेधस्य यज्ञस्य प्राप्रोत्यविकलं फलम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12897)
- **Original**: 34 एतत्किल्लेचुरन्येषां पितरः सपितामहा:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12898)
- **Original**: 35 कच्चिदस्पत्कुले जातः कालिन्दीसलिलाप्रत: । अर्च॑विष्यति गोविन्द मधुरायामुपोषित:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12899)
- **Original**: 36 ज्येष्टामूले सिते पक्षे येनेब॑ वयमप्युत । परामृद्धिमवाप्स्यामस्तारिताः स्वकुलोद्धलै:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12900)
- **Original**: 37 ज्येष्ठामूले सिते पक्षे समभ्यर्च्य जनार्दनम्‌। घन्यानां कुछज: पिण्डान्यमुनायां प्रदास्यति
- **Translation**: 

---

