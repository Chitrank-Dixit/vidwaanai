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

### Verse 1 (Vishnu Puran 0.6801)
- **Original**: लिन जज _अषणकजा0 8-8 इति श्रीविष्णुफुराणे चतुर्थे$शो तृतीयोउध्याय:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6802)
- **Original**: चतुर्थ अंश चोथा अध्याय सगर, सौदास, खदवाड़ु और भगवान्‌ रामके चरित्रका वर्णन ऑपयशर उवाच काश्यपदुहिता सुमतिर्तिदर्भगाजतनया केझिनी अच दे भायें सगरस्यास्ताम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6803)
- **Original**: ताथ्यां चापत्यार्थमार्वः परमेण . समाधिनाराधितो वरमदात्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6804)
- **Original**: एका बंशकरमेक॑ पुत्रमपरा षष्टि पुत्रसहस्ताणां जनयिष्यतीति यस्या यदभिमत॑ तदिच्छया गृह्मतामित्युक्ते केशिन्येक वस्यामास
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6805)
- **Original**: सुमति: पुत्रसहस्नाणि वरष्टिं खब्ने
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6806)
- **Original**: तथेत्युक्ते अल्पैरहोभि: केशिनी पुत्रमेक- मसपखुसनामानं बंशकरमसूत
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6807)
- **Original**: काइयप- तनयायास्तु सुमत्या: वष्टिः पुत्रसहस्राण्यभवन्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6808)
- **Original**: तस्मादसमझ्सादंझुमान्नाम कुमारो जज्ञे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6809)
- **Original**: स त्वसमझसो बाल्ओे बाल्यादेवा- सदयृत्तो5भूत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6810)
- **Original**: पिता चास्यात्रिन्तयदय- मतीतबाल्य: सुबुद्धिमान्‌ भविष्यतीति
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6811)
- **Original**: अथ तत्रापि च वयस्यतीते असश्वरितमेनं पिता तत्वाज
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6812)
- **Original**: तान्यपि पष्टिः पुत्नसहस्ना- ण्यसमझसचरितमेबानुचक्कुः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6813)
- **Original**: ततश्चासमझसचरितानुकारिभिस्सागरैरप- ध्वस्तयज्ञादिसब्मागें जगति देवास्सकलविद्या- मयमसंस्पृष्टमशेषदोपैर्भगवतः पुरुषोत्तमस्थांश- भूत॑ कपिल प्रणम्यतदर्थमूचु:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6814)
- **Original**: भ्रगवश्नेभिस्सगरतनयैरसमझसचरितमनु- गम्यते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6815)
- **Original**: कथमेभिरसदवृत्तमनुसरद्धि- ज॑गद्धविष्यतीति
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6816)
- **Original**: अत्यारत्तजगत्परित्राणाय जा भगवतोउत्र शारीरग्रहणमित्याकर्ण्य भगवाना- हाल्पैरेव दिनेथिंनब्लूयन्तीति
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6817)
- **Original**: श्रीपराशरजी बोले--काइयपसुता सुमति और विदर्भराज-कत्या केशिनी ये राजा सगरकी दो स्ियोँ थीं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6818)
- **Original**: उनसे सच्लानोत्पत्तिके लि परम समाधिद्वारा आराधना किये जानेपर भगवान्‌ और्चनेी यह वर दिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6819)
- **Original**: 'एकसे वेशाकी तद्धि करनेलाल्म एक पूत्र तथा दूसरीसे साठ हजार पुत्र उत्पन्न होंगे, इनमेंसे जिसको जो अभीष्ट हो वह इच्छापूर्वक उसीक्वे पहण कर सकती है।' उनके ऐसा कहनेपर केशििनीने एक तथा सुमतिने साठ हजार पुत्रॉका वर माँगा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6820)
- **Original**: महर्फिके 'तथास्तु' कहनेपर कुछ ही दिनोंमें केडिनीने चैशकों बदानेबाले असमझस नामंके एक पूत्रकों जन्म दिया और काइयपकुमारी सुमतिसे साठ सहल्् पुत्र उत्पन्न हुए
- **Translation**: 

---

