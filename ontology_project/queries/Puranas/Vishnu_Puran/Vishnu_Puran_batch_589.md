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

### Verse 1 (Vishnu Puran 0.11761)
- **Original**: 619 गत्वा च॒ ब्रृहि कौन्तेयमर्जुन॑ वचनान्मम । पालनीयस्त्वया झक्‍त्या जनो5य॑ मत्परिप्रह:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11762)
- **Original**: 62 त्वमर्जुनेन सहितो द्वारतत्यां तथा जनम्‌। गृहीत्वा याहि वज्रश्च यदुराजों भविष्यति
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11763)
- **Original**: 63 अ्रीपराशर उवाच इत्युक्तो दारुकः कृष्ण प्रणिपत्य पुनः पुनः । प्रदक्षिणं च बहुत: कृत्वा प्रायाद्यथोदितम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11764)
- **Original**: 64 स च गत्वा तदाचष्ट द्वारकायां तथार्जुनम्‌। आनिनाय महाबुद्धि्वज़ज चक्रे तथा नृपम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11765)
- **Original**: 657 भगवानपि गोविन्दो वासुदेवात्मक॑ परम्‌। ब्रह्मात्मनि समारोप्य सर्वभूतेष्रघारयत्‌ । निष्प्रपश्ले महाभाग संयोज्यात्मानमात्मनि । तुर्बावस्थ सलीलं च शेते सम पुरुषोत्तम:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11766)
- **Original**: 66 सम्मानयन्द्रिजवचो दुर्वासा यदुबाच ह। योगयुक्तो5भवत्पादं कृत्वा जानुनि सत्तम
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11767)
- **Original**: 67 आययोौ च जरानाम तदा तत्र स लुब्धक: । मुसलावशेषत्म्रेहेकसायकन्यस्ततोमर:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11768)
- **Original**: 68 स॒तत्पाद॑ मृगाकारमन्रेक्ष्यारादबस्थित तले विव्याध तेनैव तोमरेण द्विजोत्तम
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11769)
- **Original**: 69 ततश्षल ददूृशे तत्र चतुर्वाहुधरं नरम्‌ । प्रणिपत्याह चैवैन॑ प्रसीदेति पुनः पुनः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11770)
- **Original**: 70 अजानता कृतमिद मया हरिणशड्डया । क्षम्यत्तां मप्र पापेन दग्ध मां आतुपरहसि
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11771)
- **Original**: 71 श्रीप्राद्गर उत्ाच ततस्त॑ भगवानाह न तेउस्तु भयमण्वपि। गरुछ त्वं मत्मसादेन लुब्ध स्वर्ग सुरास्पदम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11772)
- **Original**: 72 विमानमागतं सह्स्तद्वाव्यसमनन्तरम्‌ । आरुह्म प्रययो स्वर्ग लुब्धकस्तत्मसादत:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11773)
- **Original**: 73 ही फिर कोई भी व्यक्ति द्वारकामें न रहे; जहाँ वे कुरुनन्दन जायें वहीं सब लोग चले जायें
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11774)
- **Original**: कुत्तीपुत्र अर्जुनसे तुम मेरी ओरसे कहना कि '' अपनी सामर्थ्यानुसार तुम मेरे परियारके छोगोंकी रक्षा करना”
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11775)
- **Original**: और तुम द्वारकाजासी सभी ल्लेगॉंको लेकर अर्जुनके साथ चले जाना । [हमारे पीछे] वज्र यदुवंशका राजा होगा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11776)
- **Original**: श्रीपरादारजी बोत्छे--भगवान्‌ श्रीकृष्णचन्द्रके इस प्रकार कहनेपर दारुकने उन्हें बारम्बार प्रणाम किया और उनकी अनेक परिक्रमाएँ, कर उनके कथनानुसार चला गया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11777)
- **Original**: उस महाबुद्धिने द्वास्कामें पहुँचकर सम्पूर्ण वृत्तात्त सुना दिया और अर्जुनको वहाँ व्मकर वल्नको राज्याभिषिक्त किया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11778)
- **Original**: इधर भगवान्‌ कृष्णचन्रने समस्त भूतोंमें व्याप्त बासुदेवस्वरूप परब्रह्मको अपने आत्मामें आरोपित कर उनका ध्यान किया तथा हे महाभाग ! वे पुरुषोत्तम ल्लैल्से ही अपने चित्तको निष्प्रपक्ष परमात्मामें लीनकर तुरीयपदमें स्थित हुए
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11779)
- **Original**: हे मुनिश्रेष्न ! दुर्बासाजीने [ श्रीकृष्णचन्द्रके लिये ] जैसा कहा था उस द्विज- वाक्यका * मान रखनेके लिये वे अपनी जानुऑपर चरण रखकर योगयुक्त होकर बैठे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11780)
- **Original**: इसी समय, जिसने मूसछके बचे हुए तोमर (बाणमें लगे हुए लोहेके टुकड़े) के आकारवाले लोहखण्छको अपने बाणकी नॉकपर लगा लिया था; वह जय नामक व्याध वहाँ आया
- **Translation**: 

---

