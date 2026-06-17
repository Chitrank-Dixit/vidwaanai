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

### Verse 1 (Sama Ved 0.3381)
- **Original**: है पुरुषो ! किरणां के आश्रयदाता सूर्यदेव की भाँति देवराज इद्ध विश्व के अपार वैभव को धारण करने वाले हैं। पिता द्वारा अर्जित सम्पत्ति का भाग प्राप्त करने के समान हम उनके (इन्द्र के) सामर्थ्य से प्रकट वैभव को ब्राप्त करते हैं
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3382)
- **Original**: 1320. अलर्पिराति वसुदामुप स्तुहि भद्रा इन्द्रस्थ रातय: । यो अस्य काम॑ विधतो न रोषति मनो दानाय चोदयन्‌
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3383)
- **Original**: हे स्तोताओ ! सात्विक पुरुषों को धनादि दान करने वाले इन््देव की स्तुति करो; क्योंकि इनके दान कल्याणप्रद प्रेरणा वाले हैं । जब ये इन्द्रदेव अपने मन को (याजकों के निमित्त) देने की प्रेरणा करते हैं, तो उपासक की कामना को नष्ट नहीं करते
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3384)
- **Original**: 1321.यत इन्द्र भयामहे ततो नो अभयं कृधि । मघवउ्छग्धि तव तन्‍न ऊतये वि द्विषो वि मृथो जहि
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3385)
- **Original**: हे इन्द्रदेव
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3386)
- **Original**: हिंसकों के भय से आप हमें निर्भयता प्रदान करें । अपनी साम्रर्थ्य से हमारी रक्षा करने में समर्थ, आप हमारे द्रेषियों और हिंसकों को नष्ट करें
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3387)
- **Original**: 1322. त्व॑ हि राधसस्पते राधसो मह: क्षयस्यासि विंधर्ता । त॑ त्वा वयं मघवन्निन्द्र गिर्वण: सुतावन्तो हवामहे
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3388)
- **Original**: हे ऐश्वर्यशाली इन्द्रदेव ! हमें देने के लिए आप असंख्य धन धारण करते हैं । हे स्तुति करने योग्य धनवान्‌ इन्द्रदेव ! शुद्ध सोम का आस्वादन करने के निमित्त, हम (साधक) आपको बुलाते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3389)
- **Original**: इति दशम: खण्ड:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3390)
- **Original**: ऊँ के के
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3391)
- **Original**: एकादशः खण्ड:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3392)
- **Original**: 1323. त्व॑ सोमासि धारयुर्मन्द्र ओजिष्ठो अध्वरे । पवस्व मंहयद्रयि:
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3393)
- **Original**: हे सोमदेव ! परम सुखप्रदायक, सामर्थ्यवान्‌ आप उत्तम यज्ञ में अपनी धाराओं को ऐश्वर्ययुक्त बनाएँ
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3394)
- **Original**: धन और बलप्रदायक हे सोमदेव ! आप कतश में शुद्ध हों
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3395)
- **Original**: 1324. त्वं सुतो मदिन्तमो दधन्वान्मत्सरिन्तमः । इन्दुः सत्राजिदस्तृत:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3396)
- **Original**: है सोमदेव ! शोधित हुए आप परम हर्षवर्द्धक, शक्ति-सम्पन, यज्ञ के आधार, दीप्तिवान्‌, उत्साहवर्द्धक, शत्रु-विजेता और अपराजेय हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3397)
- **Original**: 1325. त्वं सुष्वाणो अद्विभिरभ्यर्ष कनिक्रदत्‌ । द्युमन्त॑ शुष्ममा भर
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3398)
- **Original**: हे सोमरस ! पाषाणों से कूटकर रसरूप निष्पन आप शब्द करते हुए कलश में प्रविष्ट हों और हमें तेजस्विता युक्त सामर्थ्य प्रदान करें
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3399)
- **Original**: 10.10 सामवेद-संहिता 1326. पवस्व देववीतय इन्दो धाराभिरोजसा ।आ कलशं मधुमान्त्सोम न: सदः
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3400)
- **Original**: हे शक्तिसम्पन्न, मधुर सोमरस ! देवों की परिपुष्टि के लिए आप वेगपूर्वक धारारूप में हमारे कलश पात्र में ब्रविष्ट हों
- **Translation**: 

---

