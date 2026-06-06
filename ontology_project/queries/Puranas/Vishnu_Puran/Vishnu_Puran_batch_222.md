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

### Verse 1 (Vishnu Puran 0.4421)
- **Original**: लि भीम इति श्रीविष्णुपुराणे द्वितीयें5शे चतुर्दशो5घ्याय:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4422)
- **Original**: क्त्तत औ +- * अर्धात्‌ यदि आत्पा परमात्मासे भिन्न है तब तो गौ और अश्चके समान उनकी एकत हो नहीं सकती और यदि ब्रिम्व-प्रतिब्म्बिको भाँति अभिन्न है तो उपाधिके निराकरण्के अतिरिक्त और उनवत्र संयोग हो कया होगा ?
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4423)
- **Original**: अ* 17 ] द्वितोव अंश 157 पन्द्रहवाँ अध्याय ऋतभुका निदाघको अह्ैतज्ञानोपदेश औपराशर उवाच इत्युक्ते मौनिनं भूयश्चिन्तयान॑ महीपतिम्‌। प्रत्युवाचाथ विप्रोडसाव्वैतान्तर्गतां कथाम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4424)
- **Original**: 91 आह्मण उवाच श्रूयतां नृपशार्दूल यद्गीतमृभुणा पुरा। अवबोध॑ जनयता निदाघस्य महात्मन:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4425)
- **Original**: 2 ऋभुर्नामा$भवत्पुत्रो ब्रह्मण: परमेष्टिन: । विज्ञाततत्त्वसद्धावो निस॒गदिव भूपते
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4426)
- **Original**: 3 तस्य शिष्यो निदाघो5भूत्पुलस्त्यतनय: पुरा । प्रादादशेषविज्ञान॑ स तस्मै परया मुदा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4427)
- **Original**: 4 अबाज्ज्ञानतन्त्रस्थय॒न॒ तस्याह्वैतवासना । स॒ ऋशभुस्तर्कयामास निदाघस्य नरेश्वर । 5 देविकायास्तटे वीरनगरं नाम जै पुरम्‌। समृद्धमतिरम्य॑ च पुलस्त्येन निवेशितम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4428)
- **Original**: 6 रम्योपबनपर्यन्ते स तस्मिय्यार्थिवोत्तम । निदाघो नाम योगज्ञ ऋभुदिष्योउबसत्पुरा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4429)
- **Original**: 7 दिव्ये वर्षसहस्ने तु समतीते5स्थ तत्पुरम्‌। जगाम स ऋभुः शिष्यं निदाधमवलोकक:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4430)
- **Original**: 8 स॒तस्य॒ वैश्वदेवान्ते द्वारालोकनगोचरे। स्थितस्तेन गृहीताध्यों निज़वेइम प्रवेशित:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4431)
- **Original**: 9 प्रक्षात्ठिताडूघ्रिपाणिं च कृतासनपरिग्रहम्‌ । उवाच स द्विजश्रेष्ठो भुज्यतामिति सादरम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4432)
- **Original**: 10 ऋषुर्याच भो ब्िप्रवर्य भोक्तव्यं यदर्ल॑ भवतो गृहे। तत्कथ्यतां कदन्नेषु न प्रीति: सतत मम
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4433)
- **Original**: 11 निदाघ उवान सक्तुयावकवाट्यानामपूपानां ऋ्र में गृहे। यद्रोचते द्विजश्रेष्ठ तत्त्व भुड्क्ष्य यथेच्छया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4434)
- **Original**: 12 ऋषुत्वाच कदन्नानि द्विजैतानि मृष्टपन्न॑ प्रयच्छ में । संयावपायसादीनि द्र॒प्सफाणितवन्ति च
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4435)
- **Original**: 13 श्रीपराशरजी बोले--हे मैत्रेय ! ऐसा कहनेपर, राजाको मौन होकर मन- ही-मन सोच-विचार करते देख ये विप्रवर यह अद्वैत-सम्बन्धिनी कथा सुनाने छूगे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4436)
- **Original**: ब्राह्मण बोले--हे राजवदार्दूछ़ ! पूर्वकालसें महर्षि #भुने महात्मा निदाघक्यो उपदेश करते हुए, जो कुछ कहा था वह सनो
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4437)
- **Original**: है भूपते ! परमेप्री श्रीब्रह्माजीका ऋभु नामक एक पुत्र था, बह स्वभालसे हो परमार्थतत्वको जानगेबाला था
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4438)
- **Original**: पूर्वकालमें महर्षि पुलस्त्यका पूत्र निदाघ उने ऋणभुका छिष्य था। उसे उन्होने अति प्रसन्न होकर सम्पूर्ण तत्वज्ञानका उपदेश दिया था
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4439)
- **Original**: हे नरेश्वर ! ऋभुने देखा कि साप्पूर्ण दास्त्रोंका ज्ञान होते हुए भी निदाघकी अद्वैतों निष्ठा नहीं है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4440)
- **Original**: उस समय देविकानदीके तीरपर पुलस्त्यजीका बसाया
- **Translation**: 

---

