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

### Verse 1 (Vishnu Puran 0.11241)
- **Original**: क्रीडन्तीमुपलक्ष्योच्चैः स्पृहां चक्रे तदाभ्रयाम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11242)
- **Original**: 191 ततस्सकलचित्तज्ञा गौरी तामाह भामिनीम्‌ । अलमत्यर्थतापेन भर्त्रा त्वमपि रंस्यसे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11243)
- **Original**: 12 इत्युक्ता सा तया चक्रे कदेति मतिमात्मन:ः । को वा भर्ता ममेत्याह पुनस्तामाह पार्वती
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11244)
- **Original**: 13 पार्वत्युकाच बैज्ञाखशुक्धद्वादरयां स्वप्ने योअभिभवं तब । करिष्यति स ते भर्ता राजपुत्रि भविष्यति
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11245)
- **Original**: 14 अपराज्तर उवाच तस्यां तिथाबुषास्वप्ने यथा देव्या समीरितम्‌ । तथैवाभिभवं चक्रे कश्निद्रागं च तत्र सा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11246)
- **Original**: 15 ततः प्रबुद्धा पुरुषमपश्यन्ती समुत्सुका। क्व गतोउसीति निर्लज्ञा मैत्रेयोक्ततती सखीम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11247)
- **Original**: 16 याणस्य मन्त्री कुम्भाण्डइचित्रलेखा च तत्सुता । तस्या: सख्यभवत्सा च प्राह को5यं त्वयोच्यते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11248)
- **Original**: 17 यदा लज्जाकुला नास्यै कथयामास सा सखी । तदा विश्वासमानीय सर्वमेवाभ्यवादयत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11249)
- **Original**: 18 श्रीक्षिष्णुपुराण [ अ0 32 इन सब पुत्रोमें रुक्मिणीनन्दन प्रद्युम्न सबसे बड़े थे; प्रधुप्रसे अनिरुद्धका जन्म हुआ और अनिरुद्धसे वज्र उत्पन्न हुआ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11250)
- **Original**: हे द्विजोत्तम ! महाबली अनिरुद्ध युद्धमें किसीसे रोके नहीं जा सकते थे। उन्होंने बलिकी पौत्री एवं बाणासुरकी पुत्री उघासे विवाह किया था
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11251)
- **Original**: उस विवाहमें श्रोहरि और भगवान्‌ शंकरका घोर युद्ध हुआ था और श्रीकृष्णचद्धने बाणासुरकी सहस्त भुजाएँ काट डाली थीं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11252)
- **Original**: श्रीमैत्रेयजी बोले--हे ब्रह्मनू! ठषाके लिये श्रीमहादेव और कृष्णका युद्ध क्यों हुआ और श्रीहरिने बाणासुरका भुजाएँ क्यों काट डालीं ?
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11253)
- **Original**: हे महाभाग ! आप मुझसे यह सम्पूर्ण कृत्तान्त कहिये; मुझे श्रीहस्की यह कथा सुननेका बड़ा कुतृहल हो रहा है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11254)
- **Original**: श्रीपराह्ारजी बोस्ठे--हे विप्र ! एक बार बाणासुरकी पुत्री उषाने श्रीशंकर्के साथ पार्वतीजीव्मे क्रीडा करती देख स्वये भी अपने पतिके साथ र्मण करनेकी इच्छा की
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11255)
- **Original**: तब सर्वान्तर्यामिनी श्रीपार्वतीजीने उस सुकुमारीसे कहा--“तू अधिक सन्तप्त मत हो, यथासमय सू भी अपने पतिके साथ रमण करेगी”
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11256)
- **Original**: पार्वतीजीके ऐसा कहनेपर उषाने मन-ही-मन यह सोचकर कि “न जाने ऐसा कब होगा ? और मेरा पति भो कौन होगा ?' [इस सम्बख्में
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11257)
- **Original**: पार्वतीजीसे पूछा, तब पार्बतीजीने उससे फिर कहा--
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11258)
- **Original**: पार्वतीजी बोली--हे राजपुत्रि ! बैज्ञाख शुक्ला द्वादशीकी रात्रिको जो पुरुष स्वप्रमें तुझसे हठात्‌ सम्भोग करेगा वही तेरा पति होगा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11259)
- **Original**: डपाकी ख्वप्नावस्थामें किसी पुरुषने उससे, जैसा श्रीपार्वतीदेवीने कहा था, उसी प्रकार सम्भोग किया और डसका भी उसमें अनुराग हो गया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11260)
- **Original**: हे मैत्रेय
- **Translation**: 

---

