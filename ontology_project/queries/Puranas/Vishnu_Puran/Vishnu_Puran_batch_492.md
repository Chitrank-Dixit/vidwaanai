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

### Verse 1 (Vishnu Puran 0.9821)
- **Original**: 23 गोप्यश्न वृन्द॒झ्कः कृष्णचेष्टास्वायत्तमूर्तय: । अन्यदेशं गते कृष्णे चेरुबुन्दावनान्तरम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9822)
- **Original**: 24 कृष्णे निवद्धहदया इदपूलु: परस्परम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9823)
- **Original**: 25 श्रीविष्णुपुराण के आआआआओतिष्णुपुराण आओ रेस आपस्मेग मुझमें बान्धय-बुद्धि डी कॉँ
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9824)
- **Original**: मैं न टेख हूँ, न गर्व हूँ, न यक्ष हूँ और न दानव हूँ । मैं तो आपके बान्धवरूपसे ही उत्पन्न हुआ हैँ; आपत्म्रेगोंको इस विषयमें और कुछ बिचार न करना चाहिये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9825)
- **Original**: अ्रीपराइरजी बोले--हे महाशार ! श्रीहरिके प्रणवकोपयुक्त होकर कहे हुए इन वाक्योंकों सुनकर वे समस्त गोपगण चुपचाप वनको चले गये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9826)
- **Original**: तब श्रीकृष्णचन्द्रने निर्मल आकादा, शारबन्द्रकी चन्द्रिका और दिशाओंकों सुराभित करनेबाली विकसित कुमुदिनी तथा बन-सप्ष्टीकों मुखर मधुकरोंसे मनोहर देखकर गोपियोंके साथ र्मण करनेको इच्छा की
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9827)
- **Original**: 14-105
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9828)
- **Original**: उस समय खलरामजीके बिना ही श्रीम्रछीमनोहर स्त्रियोंकों प्रिय लूगनेबाला अत्यन्त मधुर, अस्फुट एवं मृदूल पद ऊँचे और धोमे स्वस्से गाने लगे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9829)
- **Original**: उनकी उस सुरम्य गीतध्यनिको सुनकर गोपियाँ अपने-अपने घरोंकों छोड़कर तत्काल जहाँ श्रोमधुसूदन थे जहाँ चली आयीं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9830)
- **Original**: यहाँ आकर कोई गोपी तो उनके स्वर-में स्वर मिलाकर धीरे-धीरे गाने छगी और कोई सन-हो-पन उन्होंका स्मरण करने छगी
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9831)
- **Original**: कोई 'हे कृष्ण, हे कृष्ण' ऐसा कहती हुई लूज्जावश रांकुचित हो गयी और कोई प्रेमोन्‍्मादिनी होकर तुरन्त उनके पास जा खड़ी हुई
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9832)
- **Original**: कोई गोपी आहर गुरुजनॉको देखकर अपने घरमें ही रहकर आँख मूँदकर तन्मयभावसे श्रीगोविददका ध्यान करने लगी
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9833)
- **Original**: तथा कोई गोपकुमारी जगत्‌के कारण परमह्मस्वरूप श्रीकृष्णचद्धका चिन्तन करते-करते [ मूर्च्छावस्थामें ] ग्राणापानके ढक जानेसे मुक्त हो गयी, क्योंकि भगवद्ध्यानके विमल आइह्वादसे उसको समस्त पुण्यराशि क्षीण हो गया और भगवान्‌की अगप्राप्िकि महान्‌ दुःखसे उसके समस्त पाप स्तन हो गये थे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9834)
- **Original**: गोपियोंसे घिरे हुए रासारम्भरूप रसके लिये उल्कण्ठित श्रीगोविन्दने उस दारशन्द्रसुज्ञोभिता राजिकों [ रास करके ] सम्मानित किया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9835)
- **Original**: उस समय भगवान्‌ कण्णके अन्यत्र थे जानेपर कृष्णचेष्टाफे अधीन हुईं गोपियाँ यूथ बनाकर वृन्दावनके अन्दर बिचरने लूगों
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9836)
- **Original**: कृष्णमें निब्रद्धंचित्त हुईं वे त्रजाड्रनाएँ परस्पर इस प्रकार वार्तातु्नाप करने छर्गीं--
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9837)
- **Original**: उसमेंसे एक गोपी कहती थी-- ] “मैं ही कृष्ण हैं; देखो, कैसी सुन्दर चालसे चलता हूँ; तनिक -मेरी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9838)
- **Original**: आौै 13 ) कृष्णोहहमेष ललित ब्रजाम्यालोक्यतां गति: । अन्‍्या ब्रवीति कृष्णस्य मम गीतिर्निशम्यताम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9839)
- **Original**: 26 दुष्टकालिय तिष्ठात्र कृष्णोडहह्वमिति चापरा । बाहुमास्फोट्य कृष्णस्य लीलया सर्वमाददे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9840)
- **Original**: 27 अन्या ब्रवीति भो गोपा निदशह्ठै: स्थीयतामिति । अल वृष्टिभयेनात्र धृतो गोवर्धनो मबा
- **Translation**: 

---

